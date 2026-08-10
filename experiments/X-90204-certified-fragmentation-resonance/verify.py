#!/usr/bin/env python3
"""Directed interval certificate for the first deterministic fragmentation resonance.

Certifies:
  * exactly one simple zero of Delta in a tiny disk around u0;
  * the n=2,p=2 exit numerator is nonzero throughout that disk;
  * the n=2 sparse-producer numerator is nonzero throughout that disk.

All finite recurrence coefficients are exact Fractions. Complex evaluation uses
mpmath interval arithmetic; infinite renewal tails are bounded analytically.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from mpmath import iv

iv.dps = 70
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results" / "verification.json"

CENTER_RE = "0.7422293980561885240550493534416845585452288947464107663790628089924"
CENTER_IM = "17.3619424994722740596801161362202749268628893017519727763861538918768"
RADIUS = "1e-18"
TRUNCATION = 20000


def lo(x):
    return x.a


def hi(x):
    return x.b


def ivq(x: Fraction | int) -> iv.mpf:
    if isinstance(x, Fraction):
        return iv.mpf(x.numerator) / x.denominator
    return iv.mpf(x)


def pow_neg(base, u):
    return iv.exp(-u * iv.log(base))


def delta(u):
    return 1 - iv.mpf("0.5") * (
        iv.exp((1-u) * iv.log(2))
        + iv.exp(-u * iv.log(3))
        + iv.exp(-u * iv.log(iv.mpf(3)/2))
    )


def delta_prime(u):
    return iv.mpf("0.5") * (
        iv.log(2) * iv.exp((1-u) * iv.log(2))
        + iv.log(3) * iv.exp(-u * iv.log(3))
        + iv.log(iv.mpf(3)/2) * iv.exp(-u * iv.log(iv.mpf(3)/2))
    )


def tau3(m: int) -> int:
    if m % 3 == 0:
        return 2*m//3
    if m % 3 == 1:
        return (m+2)//3
    return (2*m-1)//3


def exact_increment(boundary_g: dict[int, Fraction], N: int) -> list[Fraction]:
    g = [Fraction(0)] * (N+1)
    for m, v in boundary_g.items():
        g[m] = v
    for m in range(4, N+1):
        if m in boundary_g:
            continue
        children = (m//2, m-m//2, (m+2)//3, m-(m+2)//3)
        g[m] = sum((g[c] for c in children if c >= 2), Fraction(0)) / 2
    a = [Fraction(0)] * (N+1)
    for m in range(1, N+1):
        a[m] = g[m] - g[m-1]
    return a


def defect(a: list[Fraction]) -> list[Fraction]:
    b = [Fraction(0)] * 5
    for m in range(1, 5):
        b[m] = a[m] - a[(m+1)//2]/2 - a[tau3(m)]/2
    return b


def numerator_partial(u_box, sequences: dict[str, list[Fraction]]):
    defects = {name: defect(a) for name, a in sequences.items()}
    vals = {}
    for name, b in defects.items():
        vals[name] = sum(
            (ivq(b[m]) * pow_neg(m, u_box) for m in range(1, 5)),
            iv.mpc(0),
        )
    for r in range(1, TRUNCATION+1):
        d2 = pow_neg(2*r-1, u_box) - pow_neg(2*r, u_box)
        d3 = pow_neg(3*r-2, u_box) - pow_neg(3*r, u_box)
        if r % 2:
            d3 += (
                pow_neg(iv.mpf(3*r+1)/2, u_box)
                - pow_neg(iv.mpf(3*r)/2, u_box)
            )
        for name, a in sequences.items():
            vals[name] += ivq(a[r]) * (d2+d3) / 2
    return vals, defects


def tail_bound(A0, sigma, U):
    R = iv.mpf(TRUNCATION)
    alpha2 = 2 - 1/(R+1)
    alpha3 = 3 - 2/(R+1)
    bracket = (
        alpha2**(-sigma-1)
        + 2*alpha3**(-sigma-1)
        + iv.mpf("0.5")*(iv.mpf(3)/2)**(-sigma-1)
    )
    return iv.mpf(A0)/2 * U * bracket * R**(-sigma) / sigma


def main():
    rad = iv.mpf(RADIUS)
    center = iv.mpc([CENTER_RE, CENTER_RE], [CENTER_IM, CENTER_IM])
    box = iv.mpc(
        ["0.7422293980561885230550493534416845585452288947464107663790628089924",
         "0.7422293980561885250550493534416845585452288947464107663790628089924"],
        ["17.3619424994722740586801161362202749268628893017519727763861538918768",
         "17.3619424994722740606801161362202749268628893017519727763861538918768"],
    )

    Dc = delta(center)
    Dpc = delta_prime(center)
    sigma = iv.mpf("0.7422293980561885230550493534416845585452288947464107663790628089924")
    M2 = iv.mpf("0.5") * (
        iv.log(2)**2 * iv.exp((1-sigma)*iv.log(2))
        + iv.log(3)**2 * iv.exp(-sigma*iv.log(3))
        + iv.log(iv.mpf(3)/2)**2 * iv.exp(-sigma*iv.log(iv.mpf(3)/2))
    )
    rouche_error = abs(Dc) + M2*rad**2/2
    rouche_linear = abs(Dpc)*rad
    assert hi(rouche_error) < lo(rouche_linear)
    assert sigma > iv.mpf("0.5")

    exit_a = exact_increment({2: Fraction(2), 3: Fraction(0)}, TRUNCATION)
    exit3_a = exact_increment({2: Fraction(0), 3: Fraction(3)}, TRUNCATION)
    producer_a = exact_increment({2: Fraction(2), 3: Fraction(2)}, TRUNCATION)
    assert max(abs(x) for x in exit_a) == 4
    assert max(abs(x) for x in producer_a) == 2
    trace_relation_checks = 0
    for m in range(2, TRUNCATION+1):
        total_increment = Fraction(2) if m == 2 else Fraction(1)
        assert exit_a[m] + exit3_a[m] == total_increment
        assert producer_a[m] == exit_a[m] + Fraction(2, 3) * exit3_a[m]
        trace_relation_checks += 2

    vals, defects = numerator_partial(box, {"exit": exit_a, "producer": producer_a})
    U = hi(abs(box))
    tails = {
        "exit": tail_bound(4, sigma, U),
        "producer": tail_bound(2, sigma, U),
    }
    lower = {}
    for name in vals:
        lower[name] = lo(abs(vals[name])) - hi(tails[name])
        assert lower[name] > 0

    result = {
        "verdict": "PASS_X_90204_CERTIFIED_FRAGMENTATION_RESONANCE",
        "root_disk": {
            "center_re": CENTER_RE,
            "center_im": CENTER_IM,
            "radius": RADIUS,
            "delta_center_abs_upper": str(hi(abs(Dc))),
            "delta_prime_abs_lower": str(lo(abs(Dpc))),
            "delta_second_abs_upper": str(hi(M2)),
            "rouche_error_upper": str(hi(rouche_error)),
            "rouche_linear_lower": str(lo(rouche_linear)),
            "simple_zero_count": 1,
            "shifted_real_part_lower": str(sigma - iv.mpf("0.5")),
        },
        "numerators": {
            name: {
                "partial_interval": str(vals[name]),
                "partial_modulus_lower": str(lo(abs(vals[name]))),
                "tail_upper": str(hi(tails[name])),
                "full_modulus_lower": str(lower[name]),
                "defect": [str(x) for x in defects[name]],
            }
            for name in vals
        },
        "truncation": TRUNCATION,
        "exact_increment_bounds": {"exit": 4, "producer": 2},
        "trace_relation_checks": trace_relation_checks,
        "relation_note": "The exact total trace has G(m)=m; at every nonconservation characteristic zero, N_producer=N_exit/3.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(result["verdict"])
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
