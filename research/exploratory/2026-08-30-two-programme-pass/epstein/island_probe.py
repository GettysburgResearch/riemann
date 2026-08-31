"""Map the angular extent of the theta=75-deg departure island found by
C8: single detector calls at radius 0.5 for theta in {70, 72.5, 77.5,
80} deg plus a radial-depth call at (75 deg, 0.55), window (0.05, 20),
dps 40 (NON_DIRECTED_HIGH_PRECISION). Writes epstein/island_probe.json.
rh_established = false.
"""
import json
import math
import sys
import time

sys.path.insert(0, '.')
sys.path.insert(0, 'epstein')
import lab
from lab import mp

mp.dps = 40


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


out = {"meta": {"window": [0.05, 20.0], "dps": 40,
                "arithmetic_class": "NON_DIRECTED_HIGH_PRECISION",
                "rh_established": False}, "probes": {}}
CALLS = [(70.0, 0.5), (72.5, 0.5), (77.5, 0.5), (80.0, 0.5),
         (75.0, 0.55)]
for (deg, r) in CALLS:
    th = math.radians(deg)
    x, y = r * math.cos(th), 1.0 + r * math.sin(th)
    res = lab.off_line_detector(x, y, 0.05, 20.0)
    rec = {"z": [x, y], "line": res["n_line"], "box": res["n_box"],
           "disc": res["disc"]}
    out["probes"][f"theta{deg}_r{r}"] = rec
    say(f"theta={deg} r={r}: z=({x:.4f},{y:.4f}) line={res['n_line']} "
        f"box={res['n_box']} disc={res['disc']}")
    with open("epstein/island_probe.json", "w") as f:
        json.dump(out, f, indent=1)
say("island probe done")
