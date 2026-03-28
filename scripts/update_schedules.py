#!/usr/bin/env python3
# Usage:  python scripts/update_schedules.py
# Prereq: pip install requests pyyaml

import requests, yaml, datetime, pathlib, ssl
from requests.adapters import HTTPAdapter

# Force PyYAML to single-quote all strings so Ruby/Jekyll reads HH:MM times
# and comma-formatted fares correctly (unquoted, they trigger YAML 1.1 sexagesimal
# or numeric stripping in Ruby's Psych parser).
yaml.add_representer(str, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s, style="'"))

class LegacyTLSAdapter(HTTPAdapter):
    """Bypass SSL verification and allow legacy ciphers for bustago.or.kr."""
    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl._create_unverified_context()
        ctx.set_ciphers("DEFAULT:@SECLEVEL=1")
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

ROUTES = [
    {"file": "icn-govcomplex",  "dep": "9303", "arr": "9503"},
    {"file": "icn2-govcomplex", "dep": "9337", "arr": "9503"},
    {"file": "icn-doryong",     "dep": "9303", "arr": "9517"},
    {"file": "icn2-doryong",    "dep": "9337", "arr": "9517"},
]
CJJ_YUSEONG = {"dep": "3182", "arr": "9502"}
YUSEONG_CJJ = {"dep": "9502", "arr": "3182"}

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

# CJJ → Yuseong
tickets = fetch(CJJ_YUSEONG["dep"], CJJ_YUSEONG["arr"])
times = [fmt_time(t["DEP_TIME"]) for t in tickets]
data = {"updated": UPDATED,
        "first_bus": first_bus(times),
        "last_bus": last_bus(times),
        "times": times}
(DATA_DIR / "cjj-yuseong.yml").write_text(yaml.dump(data, allow_unicode=True, default_flow_style=False))
print(f"  cjj-yuseong.yml — {len(times)} departures")

# Yuseong → CJJ
tickets = fetch(YUSEONG_CJJ["dep"], YUSEONG_CJJ["arr"])
times = [fmt_time(t["DEP_TIME"]) for t in tickets]
data = {"updated": UPDATED,
        "first_bus": first_bus(times),
        "last_bus": last_bus(times),
        "times": times}
(DATA_DIR / "yuseong-cjj.yml").write_text(yaml.dump(data, allow_unicode=True, default_flow_style=False))
print(f"  yuseong-cjj.yml — {len(times)} departures")
