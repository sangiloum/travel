#!/usr/bin/env python3
# Usage:  python scripts/update_schedules.py
# Prereq: pip install requests pyyaml

import requests, yaml, datetime, pathlib, ssl, re, os, collections
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

# --- Korail trains: Cheongju Airport <-> Daejeon ---------------------------------
# data.go.kr Korail open API (B551457/run/v2). travelerTrainRunInfo2 returns one
# row per train per station, but only for days that have already run, and its
# times are the recorded (actual) ones. So we read the last three days with data
# and keep, per train, the most common departure/arrival time; a train must
# appear on at least two of those days. (travelerTrainRunPlan2 covers future
# dates but only lists each train's origin and terminus; Chungbuk Line trains
# pass through Cheongju Airport rather than starting there, so it can't be used.)
# The service key lives in the KORAIL_API_KEY environment variable (a GitHub
# Actions secret in CI); without it the train files are left unchanged.
KORAIL_URL = "https://apis.data.go.kr/B551457/run/v2/travelerTrainRunInfo2"
KORAIL_KEY = os.environ.get("KORAIL_API_KEY")
KORAIL_DAYS = 3
# The API does not give the train type. On the Chungbuk Line through Cheongju
# Airport, trains 1701/1702 are ITX; the others are Mugunghwa. Update this set if
# Korail renumbers the ITX service.
ITX_TRAINS = {"1701", "1702"}

def fetch_korail_stops(day, station):
    rows, page = [], 1
    while True:
        r = requests.get(KORAIL_URL, timeout=60, params={
            "serviceKey": KORAIL_KEY, "returnType": "JSON", "pageNo": page, "numOfRows": 1000,
            "cond[run_ymd::GTE]": day, "cond[run_ymd::LTE]": day, "cond[stn_nm::EQ]": station})
        body = r.json()["response"]["body"]
        items = body["items"]["item"]
        rows += items
        if not items or len(rows) >= body["totalCount"]:
            return {row["trn_no"]: row for row in rows}
        page += 1

def korail_day(day, origin, dest):
    """{train: (departure, arrival)} for trains stopping at origin, then dest."""
    dep, arr = fetch_korail_stops(day, origin), fetch_korail_stops(day, dest)
    out = {}
    for no, d in dep.items():
        a = arr.get(no)
        if a and d["trn_dptre_dt"] and a["trn_arvl_dt"] and a["trn_arvl_dt"] > d["trn_dptre_dt"]:
            out[no.lstrip("0")] = (d["trn_dptre_dt"][:16], a["trn_arvl_dt"][:16])
    return out

def korail_trains(origin, dest):
    days = []
    for back in range(1, 15):
        day = (datetime.date.today() - datetime.timedelta(days=back)).strftime("%Y%m%d")
        trains = korail_day(day, origin, dest)
        if trains:
            days.append(trains)
        if len(days) == KORAIL_DAYS:
            break
    rows = []
    for no in {no for d in days for no in d}:
        seen = [d[no] for d in days if no in d]
        if len(seen) < min(2, len(days)):
            continue
        fmt = "%Y-%m-%d %H:%M"
        dep_t = collections.Counter(s[0][11:] for s in seen).most_common(1)[0][0]
        arr_t = collections.Counter(s[1][11:] for s in seen).most_common(1)[0][0]
        mins = collections.Counter(
            int((datetime.datetime.strptime(s[1], fmt) - datetime.datetime.strptime(s[0], fmt)).total_seconds() // 60)
            for s in seen).most_common(1)[0][0]
        rows.append({"train": no, "type": "ITX" if no in ITX_TRAINS else "Mugunghwa",
                     "departure": dep_t, "arrival": arr_t, "minutes": str(mins)})
    return sorted(rows, key=lambda row: row["departure"])

if not KORAIL_KEY:
    print("  train-*.yml — SKIPPED (KORAIL_API_KEY not set)")
else:
    for fname, origin, dest in [("train-cjj-daejeon", "청주공항", "대전"),
                                ("train-daejeon-cjj", "대전", "청주공항")]:
        rows = korail_trains(origin, dest)
        if not rows:  # API outage: keep the last-known-good YAML
            print(f"  {fname}.yml — SKIPPED (Korail returned no trains)")
            continue
        data = {"updated": UPDATED,
                "first_train": rows[0]["departure"],
                "last_train": rows[-1]["departure"],
                "rows": rows}
        (DATA_DIR / f"{fname}.yml").write_text(yaml.dump(data, allow_unicode=True, default_flow_style=False))
        print(f"  {fname}.yml — {len(rows)} trains (Korail)")
