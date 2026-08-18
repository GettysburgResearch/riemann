#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
control=json.loads((ROOT/"certificates/control.json").read_text())

def accepts(payload):
    if payload.get("rh_established") is not False: return False
    opens=set(payload.get("open",[]))
    if not set(control["required_open"]).issubset(opens): return False
    c=float(payload["c_star"])
    lo,hi=map(float,control["c_star_interval"])
    return lo<c<hi

p=json.loads((ROOT/"results/verification.json").read_text())
assert accepts(p)

m=dict(p); m["rh_established"]=True; assert not accepts(m)
m=dict(p); m["c_star"]="-0.3086"; assert not accepts(m)
m=dict(p); m["open"]=[]; assert not accepts(m)

print("PASS_T98070_MUTATION_CONTROLS")
