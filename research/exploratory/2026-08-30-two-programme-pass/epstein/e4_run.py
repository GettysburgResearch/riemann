"""E4 departure-locus sketch around z = i, plus resolution of the pending
path-A event (2026-08-31 continuation pass; the original E4 never ran —
its agent was lost to session limits).

All numerics NON_DIRECTED_HIGH_PRECISION at mp.dps = 40, truncation and
conventions exactly as in lab.py/run_experiments.py. Every 'zero',
'departure', 'pair' below means: numerically located to the stated
precision. rh_established = false.

Step 1 (path-A resolution): the pass-1 event on path A (x in (0.25, 0.35),
y = 1.02, window (0.05, 30)) had empty pair candidates and a note
suspecting a window-boundary entry near t = 30. Re-run x = 0.35 with the
window widened to (0.05, 35): if disc drops to 0 with the extra headroom,
the 'event' was a pair drifting across t = 30 (an artifact — withdrawn);
if disc persists, localize the pair by subwindow box counts.

Step 2 (E4 grid): directions from z = i (inside the fundamental domain):
(1,0), (0,1), (1,1)/sqrt2, (2,1)/sqrt5. For each, with t-window (0.05, 20):
coarse radii 0.2, 0.4, 0.6, 0.8; on the first radius with disc > 0, bisect
the radius to 0.01 between the last clean and first discrepant value.
A direction with no discrepancy through r = 0.8 is recorded as exactly
that (no claim beyond the window and radius searched).
"""
import json
import sys
import time

sys.path.insert(0, '.')
import lab
from lab import mp

mp.dps = 40
T0, T1E4 = 0.05, 20.0
LOG = open('e4.log', 'a')


def say(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)
    LOG.write(f"[{time.strftime('%H:%M:%S')}] {msg}\n")
    LOG.flush()


def disc_at(x, y, t0, t1):
    r = lab.off_line_detector(x, y, t0, t1)
    say(f"  z=({x:.4f},{y:.4f}) window=({t0},{t1}): n_line={r['n_line']} "
        f"n_box={r['n_box']} disc={r['disc']} anomaly={r['anomaly']}")
    return r


def main():
    out = {"meta": {"arithmetic_class": "NON_DIRECTED_HIGH_PRECISION",
                    "dps": 40, "mpmath_version": "1.3.0",
                    "note": "see module docstring; every statement is "
                            "numerical at stated precision",
                    "rh_established": False}}

    say("STEP 1: path-A event resolution at x=0.35, y=1.02, window (0.05,35)")
    r = disc_at(0.35, 1.02, 0.05, 35.0)
    verdict = {"x": 0.35, "y": 1.02, "window": [0.05, 35.0],
               "n_line": r['n_line'], "n_box": r['n_box'], "disc": r['disc']}
    if r['disc'] == 0:
        verdict["resolution"] = ("ARTIFACT WITHDRAWN: with headroom to t=35 "
                                 "the discrepancy vanishes — the pass-1 "
                                 "path-A 'event' was a zero pair drifting "
                                 "across the t=30 window boundary, not a "
                                 "departure from the critical line")
    else:
        subs = {}
        for (a, b) in ((0.05, 12.0), (12.0, 24.0), (24.0, 30.0), (30.0, 35.0)):
            rr = disc_at(0.35, 1.02, a, b)
            subs[f"({a},{b})"] = rr['disc']
        verdict["resolution"] = "PERSISTS; subwindow discs recorded"
        verdict["subwindows"] = subs
    out["path_A_resolution"] = verdict
    with open('e4_locus.json', 'w') as f:
        json.dump(out, f, indent=1)

    say("STEP 2: E4 grid")
    dirs = {"x_dir_(1,0)": (1.0, 0.0), "y_dir_(0,1)": (0.0, 1.0),
            "diag_(1,1)": (0.70710678, 0.70710678),
            "shallow_(2,1)": (0.89442719, 0.44721360)}
    locus = {}
    for name, (dx, dy) in dirs.items():
        say(f"direction {name}")
        rec = {"coarse": {}}
        clean, dirty = 0.0, None
        for rr in (0.2, 0.4, 0.6, 0.8):
            x, y = rr * dx, 1.0 + rr * dy
            d = disc_at(x, y, T0, T1E4)
            rec["coarse"][str(rr)] = d['disc']
            if d['disc'] > 0 and dirty is None:
                dirty = rr
                break
            clean = rr
        if dirty is None:
            rec["verdict"] = (f"no off-line discrepancy found for r <= 0.8 "
                              f"in t-window ({T0},{T1E4}); no claim beyond "
                              "that window/radius")
        else:
            lo, hi = clean, dirty
            while hi - lo > 0.01:
                mid = (lo + hi) / 2
                x, y = mid * dx, 1.0 + mid * dy
                d = disc_at(x, y, T0, T1E4)
                if d['disc'] > 0:
                    hi = mid
                else:
                    lo = mid
            rec["verdict"] = (f"first off-line discrepancy in t-window "
                              f"({T0},{T1E4}) at radius in ({lo:.3f}, "
                              f"{hi:.3f}]")
            rec["radius_bracket"] = [lo, hi]
        locus[name] = rec
        out["locus"] = locus
        with open('e4_locus.json', 'w') as f:
            json.dump(out, f, indent=1)
    say("E4 done")


if __name__ == "__main__":
    main()
