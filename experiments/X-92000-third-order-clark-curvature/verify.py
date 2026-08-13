#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from fractions import Fraction as Q

try:
    import mpmath as mp
except ImportError:
    mp = None


def det3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def dd2(ts, fs):
    out = Q(0)
    for i in range(3):
        den = Q(1)
        for j in range(3):
            if i != j:
                den *= ts[i] - ts[j]
        out += fs[i] / den
    return out


def h_matrix(xs, ps):
    return [
        [(xs[i] * ps[i] + xs[j] * ps[j]) / (xs[i] + xs[j]) for j in range(3)]
        for i in range(3)
    ]


def factorized_det(xs, ps):
    ts = [x * x for x in xs]
    vand = (ts[1] - ts[0]) * (ts[2] - ts[0]) * (ts[2] - ts[1])
    den = Q(1)
    for i in range(3):
        for j in range(i + 1, 3):
            den *= (xs[i] + xs[j]) ** 2
    return (
        ps[0] * ps[1] * ps[2] * vand * vand
        * dd2(ts, [Q(1) / p for p in ps])
        * dd2(ts, [t * p for t, p in zip(ts, ps)]) / den
    )


def off_orbit_f(x, a, b):
    aa = a * a - b * b
    bb = 2 * a * b
    t = x * x
    return 4 * x * (t - aa) / ((t - aa) * (t - aa) + bb * bb)


def exact_control():
    xs = [Q(3, 5), Q(8), Q(36)]
    a, b = Q(2, 5), Q(14)
    fs = [off_orbit_f(x, a, b) for x in xs]
    ps = [f / x for f, x in zip(fs, xs)]
    determinant = det3(h_matrix(xs, ps))
    expected = -Q(201516024836691562500, 1055839030806150723363641645963)
    assert determinant == expected
    assert factorized_det(xs, ps) == determinant

    t = Q(7, 3)
    c = b * b - a * a
    B = 2 * a * b
    U = t + c
    reciprocal_second = B * B / (Q(2) * U**3)
    assert reciprocal_second > 0

    r2 = B * B / (U * U)
    theta = c / U
    numerator_scaled = theta * (1 - 3 * r2) + r2 * (3 - r2)
    assert r2 < Q(1, 3)
    assert numerator_scaled > 0

    return {
        "control_nodes": [str(x) for x in xs],
        "control_determinant": str(determinant),
        "factorization_exact": True,
        "one_orbit_reciprocal_second": str(reciprocal_second),
        "one_orbit_tp_curvature_numerator_scaled": str(numerator_scaled),
    }


def xi(s):
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def safe_curvatures(x):
    s = mp.mpf("0.5") + x
    log_xi = lambda z: mp.log(xi(z))
    F = mp.diff(log_xi, s, 1)
    F1 = mp.diff(log_xi, s, 2)
    F2 = mp.diff(log_xi, s, 3)
    q3 = x * x * F * F2 - 2 * x * x * F1 * F1 + x * F * F1 + F * F
    tp = x * x * F2 + x * F1 - F
    return F, q3, tp


def numerical_diagnostics():
    if mp is None:
        return {"available": False}
    mp.mp.dps = 80
    points = [mp.mpf(x) for x in ("0.5001", "0.55", "0.75", "1", "2", "5", "10", "20", "50", "100")]
    rows = []
    minimum_q3 = None
    maximum_tp = None
    for x in points:
        F, q3, tp = safe_curvatures(x)
        rows.append({
            "x": mp.nstr(x, 20),
            "F": mp.nstr(F, 30),
            "Q3": mp.nstr(q3, 30),
            "tp_second_numerator": mp.nstr(tp, 30),
        })
        minimum_q3 = q3 if minimum_q3 is None or q3 < minimum_q3 else minimum_q3
        maximum_tp = tp if maximum_tp is None or tp > maximum_tp else maximum_tp
    assert minimum_q3 > 0
    assert maximum_tp < 0
    return {
        "available": True,
        "rows": rows,
        "minimum_sample_Q3": mp.nstr(minimum_q3, 30),
        "maximum_sample_tp_second_numerator": mp.nstr(maximum_tp, 30),
        "rigorous": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", required=True)
    args = parser.parse_args()
    result = {
        "status": "PASS_THIRD_ORDER_CLARK_CURVATURE",
        "exact": exact_control(),
        "actual_xi_diagnostic": numerical_diagnostics(),
        "scope": {"exact_algebra": True, "actual_xi_interval_proof": False, "rh_proved": False},
    }
    with open(args.json, "w", encoding="utf-8") as handle:
        json.dump(result, handle, sort_keys=True, separators=(",", ":"))
        handle.write("\n")
    print(result["status"])


if __name__ == "__main__":
    main()
