"""Combine the four per-edge winding sums of wall_complex2.py into
the full-contour certificate (see walk()'s docstring for why the
per-edge interval sums add soundly: associativity of the one step
sum, with deterministic identical corner boxes and the zero-length
closing term omitted). Endpoints cross processes as 40-digit decimal
strings; we outward-pad by 1e-30, which dwarfs the decimal
representation error at these precisions. rh_established = false.
"""
import json

import mpmath as mp

iv = mp.iv
iv.dps = 30
mp.mp.dps = 30

PAD = mp.mpf('1e-30')


def main():
    edges = []
    for e in range(4):
        edges.append(json.load(open(f'epstein/wall_complex2_edge{e}.json')))
    # contour closes: end of e == start of e+1 (exact rational strings)
    for e in range(4):
        assert edges[e]["edge"] == e
        assert edges[e]["end"] == edges[(e + 1) % 4]["start"], e
    lo = mp.mpf(0)
    hi = mp.mpf(0)
    steps = 0
    min_ell = mp.inf
    for d in edges:
        lo += mp.mpf(d["sum_lo"]) - PAD
        hi += mp.mpf(d["sum_hi"]) + PAD
        steps += d["steps"]
        min_ell = min(min_ell, mp.mpf(d["min_ell"]))
    tot = iv.mpf([mp.nstr(lo, 40), mp.nstr(hi, 40)])
    tot = iv.mpf([mp.mpf(tot.a) - PAD, mp.mpf(tot.b) + PAD])
    w = tot / (2 * iv.pi)
    wlo, whi = mp.mpf(w.a), mp.mpf(w.b)
    k = int(mp.nint(wlo))
    pinned = (abs(wlo - k) < mp.mpf('0.4') and abs(whi - k) < mp.mpf('0.4')
              and k == int(mp.nint(whi)))
    ok = pinned and k >= 1
    out = {
        "modulus": {"x": "4341/50000", "y": "3731/2500",
                    "context": "theta80 dirty probe of the C8 "
                               "archipelago campaign, exact-rationalized"},
        "rectangle": {"re": ["62/100", "77/100"],
                      "im": ["1886/100", "1904/100"]},
        "winding_interval": [mp.nstr(wlo, 20), mp.nstr(whi, 20)],
        "winding": k, "pinned": pinned, "steps": steps,
        "min_contour_enclosure_lower": mp.nstr(min_ell, 8),
        "parallelized_by_edge": True,
        "edge_steps": [d["steps"] for d in edges],
        "float_zero_location": "0.6940279890724 + 18.9467935267590 i",
        "conclusion": (f"Z_Q has {k} zero(s) in the rectangle; its left "
                       "edge Re s = 62/100 > 1/2: a PROVED complex "
                       "off-critical-line zero at an exact archipelago-"
                       "adjacent modulus." if ok else "NOT ESTABLISHED"),
        "verified": bool(ok),
        "rh_established": False,
    }
    json.dump(out, open('epstein/wall_complex2.json', 'w'), indent=1)
    print(f"winding interval: [{mp.nstr(wlo, 10)}, {mp.nstr(whi, 10)}]")
    print(f"steps {steps}, min ell {mp.nstr(min_ell, 4)}")
    print("VERIFIED winding = " + str(k) if ok else "NOT VERIFIED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
