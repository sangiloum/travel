#!/usr/bin/env python3
# Usage:  python scripts/update_schedules.py
# Prereq: pip install requests pyyaml

import requests, yaml, datetime, pathlib, ssl, re
from requests.adapters import HTTPAdapter

# Force PyYAML to single-quote all strings so Ruby/Jekyll reads HH:MM times
# and comma-formatted fares correctly (unquoted, they trigger YAML 1.1 sexagesimal
# or numeric stripping in Ruby's Psych parser).
yaml.add_representer(str, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s, style="'"))

class LegacyTLSAdapter(HTTPAdapter):
    """Bypass SSL verification and allow legacy ciphers for bustago.or.kr."""
    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl._create_unverified_context()
        try:
            ctx.set_ciphers("DEFAULT:@SECLEVEL=1")
        except ssl.SSLError:
            ctx.set_ciphers("DEFAULT")
        kwargs["ssl_context"] = ctx
        super().init_poolmanager(*args, **kwargs)

    def send(self, request, **kwargs):
        kwargs["verify"] = False
        return super().send(request, **kwargs)

DATA_DIR = pathlib.Path("_data/schedules")
DATE = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y%m%d")
UPDATED = datetime.date.today().strftime("%B %Y")
BASE_URL = "https://www.bustago.or.kr/newweb/kr/ticket/ticketListJson3.do"
HEADERS = {
    "Referer": "https://www.bustago.or.kr/newweb/kr/ticket/ticket.do",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/x-www-form-urlencoded",
}
GRADE_MAP = {
    "시외우등":      "Deluxe (우등)",
    "프리미엄우등":   "Premium (프리미엄)",
    "심야우등1":     "Night Deluxe (심야우등)",
    "심야우등":      "Night Deluxe (심야우등)",
    "프리미엄심야우등": "Premium Night (프리미엄심야우등)",
}

CUTOFF = "02:00"

def first_bus(times):
    for t in times:
        if t >= CUTOFF:
            return t
    return times[0] if times else ""

def last_bus(times):
    late = [t for t in times if t < CUTOFF]
    return late[-1] if late else (times[-1] if times else "")

# Bustago terminal IDs are direction-specific for the Daejeon stops:
#   Government Complex: 9505 (대전청사) as arrival, 9536 (대전청사공항) as departure
#   Doryong:            9517 (대덕문화센터) as arrival, 9527 (대전도룡) as departure
# (9503 is 대전복합, the main complex terminal — same bus times but different fares.)
ROUTES = [
    {"file": "icn-govcomplex",  "dep": "9303", "arr": "9505"},
    {"file": "icn2-govcomplex", "dep": "9337", "arr": "9505"},
    {"file": "icn-doryong",     "dep": "9303", "arr": "9517"},
    {"file": "icn2-doryong",    "dep": "9337", "arr": "9517"},
    # Return direction: Daejeon -> Incheon Airport
    {"file": "govcomplex-icn",  "dep": "9536", "arr": "9303"},
    {"file": "govcomplex-icn2", "dep": "9536", "arr": "9337"},
    {"file": "doryong-icn",     "dep": "9527", "arr": "9303"},
    {"file": "doryong-icn2",    "dep": "9527", "arr": "9337"},
]
# Cheongju Airport <-> Yuseong is fetched from txbus (the TmoneyGO backend), NOT
# bustago: bustago omits several 서울고속/새서울고속 우등 departures on this route
# (e.g. 06:30, 09:20, 12:10, 15:20, 18:50), which the airport kiosk and TmoneyGO
# do show. txbus lists the full schedule and is a strict superset of bustago here.
# txbus terminal codes come from /otck/readTrmlList.do and differ from bustago IDs:
#   청주공항 = 2814201, 유성복합 = 3417501.
# (The ICN airport routes above stay on bustago -- txbus does not carry them.)
CJJ_YUSEONG_TX = {"dep": "2814201", "arr": "3417501"}
YUSEONG_CJJ_TX = {"dep": "3417501", "arr": "2814201"}

session = requests.Session()
session.mount("https://", LegacyTLSAdapter())
requests.packages.urllib3.disable_warnings()  # suppress InsecureRequestWarning
session.get("https://www.bustago.or.kr/newweb/kr/ticket/ticket.do")  # init session

def fetch(dep, arr):
    r = session.post(BASE_URL, headers=HEADERS,
        data=f"startType=1&orderDate={DATE}&depTerId={dep}&arrTerId={arr}&depTime=00&arrTime=24&goBusGrade=&goBackBusGrade=")
    return r.json().get("ticketSingleList", [])

def fmt_time(t):
    return f"{t[:2]}:{t[2:]}"

def fmt_fare(f):
    return f"{int(f):,}" if f else ""

# --- txbus (TmoneyGO backend) --------------------------------------------------
# txbus uses modern TLS, so a plain session works; it does require a browser
# User-Agent and a warmed session cookie. The booking endpoint (readAlcnList.do)
# rejects scripted requests, but the operation-info endpoint (readRunInfList.do)
# is open and returns the full daily timetable as an HTML page.
TXBUS_BASE = "https://txbus.t-money.co.kr"
tx_session = requests.Session()
tx_session.headers.update({"User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"})
tx_session.get(f"{TXBUS_BASE}/runinf/runInf.do")  # warm session cookie

def fetch_txbus(dep, arr):
    """Return sorted 'HH:MM' departure times for a txbus route.

    readRunInfList.do renders the row list twice, so we stop collecting at the
    first descending time (the start of the repeated copy)."""
    r = tx_session.post(f"{TXBUS_BASE}/runinf/readRunInfList.do",
        headers={"Referer": f"{TXBUS_BASE}/runinf/runInf.do"},
        data={"depr_Trml_Cd": dep, "arvl_Trml_Cd": arr, "depr_Dt": DATE,
              "depr_Time": "00:00", "bef_Aft_Dvs": "D", "req_Rec_Num": "80"})
    times = []
    for tr in re.findall(r"<tr>(.*?)</tr>", r.text, re.S):
        tm = re.search(r"\d{2}:\d{2}", tr)
        if tm and "<strong>" in tr:  # a real bus row carries a grade in <strong>
            if times and tm.group(0) < times[-1]:  # repeated copy begins
                break
            times.append(tm.group(0))
    return times

# ICN routes
for route in ROUTES:
    tickets = fetch(route["dep"], route["arr"])
    rows = [{"time": fmt_time(t["DEP_TIME"]),
             "class": GRADE_MAP.get(t.get("BUS_TYPE_NM", ""), t.get("BUS_TYPE_NM", "")),
             "fare": fmt_fare(t.get("FARE0"))}
            for t in tickets]
    times_list = [row["time"] for row in rows]
    data = {"updated": UPDATED,
            "first_bus": first_bus(times_list),
            "last_bus": last_bus(times_list),
            "rows": rows}
    out = DATA_DIR / f"{route['file']}.yml"
    out.write_text(yaml.dump(data, allow_unicode=True, default_flow_style=False))
    print(f"  {route['file']}.yml — {len(rows)} rows")

# CJJ <-> Yuseong (via txbus / TmoneyGO -- see note by the terminal codes above)
for fname, rt in [("cjj-yuseong", CJJ_YUSEONG_TX), ("yuseong-cjj", YUSEONG_CJJ_TX)]:
    times = fetch_txbus(rt["dep"], rt["arr"])
    if not times:  # transient txbus failure: keep the last-known-good YAML
        print(f"  {fname}.yml — SKIPPED (txbus returned no departures)")
        continue
    data = {"updated": UPDATED,
            "first_bus": first_bus(times),
            "last_bus": last_bus(times),
            "times": times}
    (DATA_DIR / f"{fname}.yml").write_text(yaml.dump(data, allow_unicode=True, default_flow_style=False))
    print(f"  {fname}.yml — {len(times)} departures (txbus)")
