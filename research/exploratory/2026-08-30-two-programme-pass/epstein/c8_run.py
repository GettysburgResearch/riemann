"""C8: Epstein departure-radius campaign around z = i — 12 direction runs
with angular refinement near the rectangular funnel plus two
height-stratified windows, then geometric invariants per event point.

NON_DIRECTED_HIGH_PRECISION (dps 40, lab conventions); every 'departure'
means a certified box/line count discrepancy at stated precision.
Writes epstein/c8_campaign.json incrementally. rh_established = false.
"""
import json
import math
import sys
import time

sys.path.insert(0, '.')
import lab
from lab import mp

mp.dps = 40
LOG = open('c8.log', 'a')


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)
    LOG.write(f"[{time.strftime('%H:%M:%S')}] {m}\n")
    LOG.flush()


def disc_at(x, y, t0, t1):
    r = lab.off_line_detector(x, y, t0, t1)
    say(f"  z=({x:.4f},{y:.4f}) w=({t0},{t1}): line={r['n_line']} "
        f"box={r['n_box']} disc={r['disc']}")
    return r['disc']


# CM points with class number 1 (fundamental domain representatives)
CM = [(0.0, 1.0), (0.5, math.sqrt(3) / 2), (0.5, math.sqrt(7) / 2),
      (0.0, math.sqrt(2)), (0.5, math.sqrt(11) / 2), (0.0, 2.0),
      (0.5, math.sqrt(19) / 2), (0.5, math.sqrt(43) / 2)]


def hyp_dist(z1, z2):
    (x1, y1), (x2, y2) = z1, z2
    num = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return math.acosh(1 + num / (2 * y1 * y2))


def systole(x, y):
    best = None
    for m_ in range(-6, 7):
        for n_ in range(-6, 7):
            if (m_, n_) == (0, 0):
                continue
            q = ((m_ * x + n_) ** 2 + (m_ * y) ** 2) / y
            best = q if best is None else min(best, q)
    return best


def invariants(x, y):
    return {"cm_dist": min(hyp_dist((x, y), c) for c in CM),
            "systole": systole(x, y), "cusp_height": y}


RUNS = ([(math.radians(a), 0.05, 20.0) for a in
         (0, 15, 30, 45, 60, 75, 82.5, 86, 88, 90)]
        + [(math.radians(0), 18.0, 32.0), (math.radians(45), 18.0, 32.0)])

RADII = [0.2, 0.35, 0.5, 0.65, 0.8]


def main():
    out = {"meta": {"arithmetic_class": "NON_DIRECTED_HIGH_PRECISION",
                    "dps": 40, "mpmath_version": "1.3.0",
                    "rh_established": False},
           "runs": {}}
    for (theta, t0, t1) in RUNS:
        dx, dy = math.cos(theta), math.sin(theta)
        name = f"theta{math.degrees(theta):.1f}_w{t0:g}-{t1:g}"
        say(f"RUN {name}")
        rec = {"coarse": {}, "theta_deg": round(math.degrees(theta), 1),
               "window": [t0, t1]}
        clean, dirty = 0.0, None
        for r in RADII:
            x, y = r * dx, 1.0 + r * dy
            d = disc_at(x, y, t0, t1)
            rec["coarse"][str(r)] = d
            if d > 0:
                dirty = r
                break
            clean = r
        if dirty is None:
            rec["verdict"] = f"clean through r=0.8 in window ({t0},{t1})"
        else:
            lo, hi = clean, dirty
            while hi - lo > 0.02:
                mid = (lo + hi) / 2
                x, y = mid * dx, 1.0 + mid * dy
                if disc_at(x, y, t0, t1) > 0:
                    hi = mid
                else:
                    lo = mid
            rec["radius_bracket"] = [round(lo, 4), round(hi, 4)]
            xs, ys = hi * dx, 1.0 + hi * dy
            rec["invariants_at_first_dirty"] = invariants(xs, ys)
            rec["verdict"] = f"departure radius in ({lo:.3f}, {hi:.3f}]"
        out["runs"][name] = rec
        with open('c8_campaign.json', 'w') as f:
            json.dump(out, f, indent=1)
        say(f"  -> {rec['verdict']}")
    say("C8 done")


if __name__ == "__main__":
    main()
