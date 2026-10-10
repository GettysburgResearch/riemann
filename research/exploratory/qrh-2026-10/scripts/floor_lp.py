#!/usr/bin/env python3
"""Exact LP barriers for floor-bin (and near-critical-bin) cancellation.  PROPOSED / EXPLORATORY.

Extends barrier_lp.py (same variables v = (lx, ly, ell, s), same low-side rows, same exact
rational certificates).  A bin with real part a (delta = 2a - 1), row-sum exponent R (count R,
minus any assumed cancellation) and slot amplitude q = x delta contributes, at the top dyad d = h
(eq. 10.15 with beta* -> s):

    a(1 - ly) + h (R + delta/2 - 1/6) - ell/2 + x delta ell - s <= 0,   h = 1 - lx + ell.

d = h is the worst dyad whenever R + delta/2 - 17/50 > 0 (true for every row below).
Scenarios:
  floor(theta):        floor bin a0 with R = 1 - theta;  other bins ignored  (pure floor barrier)
  floor(theta) + DH:   plus density-hypothesis bins R = 1 - delta on a delta grid in (delta0, 0.70]
  near-critical(theta): every DH bin also gets R = max(1 - delta - theta, (1 - delta)/2)
energy: 'paper' = three low branches of barrier_lp.low_rows(); 'optimal' = branches E = M and
E = 2M + ell - 1 only, plus M >= 2 ell (as in barrier_lp Barrier 3).
"""
from fractions import Fraction as Fr
import barrier_lp as B

THETAS = [Fr(0), Fr(1, 20), Fr(1, 10), Fr(1, 4), Fr(1, 2)]
DGRID = [Fr(k, 150) for k in range(1, 101)]         # DH bins delta in (0, 2/3]: a <= 5/6 <= s always
# (s >= 5/6 in every scenario, so these bins have worst beta* = s and the row is linear;
#  bins with delta in (2/3, 5/6] are checked a posteriori with beta* = max(s, a)).


def bin_row(a, R, x=Fr(1, 2)):
    delta = 2*a - 1
    c_h = R + delta/2 - Fr(1, 6)
    # a - a ly + c_h (1 - lx + ell) - ell/2 + x delta ell - s <= 0
    return ([-c_h, -a, c_h - Fr(1, 2) + x*delta, Fr(-1)], -(a + c_h))


def rows_for(a0, theta, dh=False, theta_all=Fr(0), energy='paper', level=False):
    low = B.low_rows()
    if energy == 'optimal':
        low = [low[0], low[2], ([Fr(-1), Fr(-1), Fr(2), 0], Fr(0))]
    rows = low + B.validity_rows() + [bin_row(a0, 1 - theta)]
    if dh:
        d0 = 2*a0 - 1
        for dl in DGRID:
            if dl <= d0:
                continue
            R = max(1 - dl - theta_all, (1 - dl)/2)
            if level:                                # Hypothesis NC(theta): R = 1 - max(delta, theta)
                R = 1 - max(dl, theta)
            rows.append(bin_row((1 + dl)/2, R))
    return rows


def posterior_ok(x, a0, theta_all, dh, level=False):
    """check every bin delta in (delta0, 5/6] (grid 1e-3) with beta* = max(s, a) at the LP point"""
    if not dh:
        return True
    lx, ly, ell, s = x
    h = 1 - lx + ell
    worst = -1.0
    for k in range(1, 834):
        dl = k/1000
        if dl <= float(2*a0 - 1):
            continue
        a = (1 + dl)/2
        R = max(1 - dl - float(theta_all), (1 - dl)/2)
        if level:
            R = 1 - max(dl, float(theta_all))
        G = a*(1 - ly) + h*(R + dl/2 - 1/6) - ell/2 + 0.5*dl*ell
        worst = max(worst, G - max(s, a))
    return worst <= 1e-9


def value(rows, a0=None, theta_all=Fr(0), dh=False, level=False):
    res = B.solve(rows)
    ok, bound, _ = B.certify(rows, res)
    ok = ok and posterior_ok(res.x, a0, theta_all, dh, level)
    return float(res.fun), ok, bound, res.x[:3]


if __name__ == '__main__':
    for energy in ('paper', 'optimal'):
        print(f"=== energy = {energy} ===")
        for a0 in (Fr(51, 100), Fr(1, 2)):
            print(f"-- detector floor a0 = {float(a0):.6f}")
            for th in THETAS:
                v1, ok1, b1, g1 = value(rows_for(a0, th, energy=energy))
                v2, ok2, b2, g2 = value(rows_for(a0, th, dh=True, energy=energy), a0, Fr(0), True)
                v3, ok3, b3, g3 = value(rows_for(a0, th, dh=True, theta_all=th, energy=energy), a0, th, True)
                def fmt(v, ok, b):
                    s = f"{v:.6f}"
                    if ok and b.denominator < 10**5: s += f" (= {b})"
                    elif not ok: s += " (cert?)"
                    return s
                print(f"theta={float(th):4.2f}  floor-only {fmt(v1, ok1, b1):24s} floor+DH {fmt(v2, ok2, b2):24s}"
                      f" near-critical(theta all bins)+DH {fmt(v3, ok3, b3):24s} geom {tuple(round(float(t), 4) for t in g3)}")

    print("=== Hypothesis NC(theta) (level form): floor R = 1 - theta, bins R = 1 - max(delta, theta) ===")
    for energy in ('paper', 'optimal'):
        for a0 in (Fr(51, 100), Fr(1, 2)):
            vals = []
            for th in THETAS + [Fr(14, 75), Fr(1, 6)]:
                v, ok, b, g = value(rows_for(a0, th, dh=True, theta_all=th, energy=energy, level=True),
                                    a0, th, True, True)
                vals.append(f"{float(th):.4f}:{b if ok else '?'}")
            print(f"energy={energy:7s} a0={float(a0):.2f}  " + "  ".join(vals))
