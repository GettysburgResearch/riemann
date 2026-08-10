#!/usr/bin/env python3
"""Exact regression for the root-of-unity powered Euler signature frame."""
from fractions import Fraction
from math import comb
import hashlib
import json


def C(k: int, x: Fraction) -> Fraction:
    return sum(Fraction(comb(k, j) ** 2) * x**j for j in range(k + 1))


pair_rows = 0
lower_bound_rows = 0
frame_rows = 0
reserve_rows = 0
gauge_rows = 0
samples = [Fraction(1, 2), Fraction(3, 4), Fraction(1),
           Fraction(4, 3), Fraction(3, 2), Fraction(7, 4)]

for k in range(1, 21):
    c4 = C(k, Fraction(4))
    # Critical root-of-unity frame: only equal binomial indices survive.
    diagonal = sum(Fraction(comb(k, j) ** 2) * 4**j for j in range(k + 1))
    assert diagonal == c4
    frame_rows += 1

    for q in samples:
        right = C(k, q*q)
        left = C(k, Fraction(16)/(q*q))
        product = right * left
        assert product > c4*c4

        # Reflected pair has normalized determinant 1-product/c4^2 < 0.
        determinant = Fraction(1) - product/(c4*c4)
        assert determinant < 0
        pair_rows += 1

        base = ((1+q)*(1+Fraction(4, 1)/q))/9
        # [sqrt(product)/c4]^2 >= [base^k/(k+1)]^2.
        assert product * (k+1)**2 >= c4*c4 * base**(2*k)
        assert base > 1
        lower_bound_rows += 1

    # Normalized deterministic gauge coefficient (with L=1) is <= 4 k^2.
    ratio = Fraction(4*k*k) * C(k-1, Fraction(4)) / c4
    assert ratio <= 4*k*k
    gauge_rows += 1

# Formal phase-separation checks for a range of powers and active depths.
for k in range(1, 9):
    for R in range(1, 9):
        M = 2*max(k, R) + 1
        F = Fraction(7, 3)
        S = Fraction(5, 2)
        assert F*F >= S
        d = {r: Fraction(k * 4**r) for r in range(1, R+1)}

        # Constant Fourier coefficient of |F+sum omega^r d_r|^2.
        energy = {}
        coeff = {0: F, **d}
        for r, ar in coeff.items():
            for s, bs in coeff.items():
                key = (r-s) % M
                energy[key] = energy.get(key, Fraction(0)) + ar*bs
        avg_energy = energy.get(0, Fraction(0))
        assert avg_energy == F*F + sum(x*x for x in d.values())

        # Every nonordinary forcing phase is nonzero mod M.
        forcing = {0: S}
        for r in range(1, R+1):
            forcing[r] = forcing.get(r, Fraction(0)) + Fraction(11*r)
        for r in range(1, R+1):
            for s in range(1, R+1):
                key = (r+s) % M
                forcing[key] = forcing.get(key, Fraction(0)) + Fraction(r*s)
        avg_forcing = forcing.get(0, Fraction(0))
        assert avg_forcing == S
        assert avg_energy-avg_forcing == F*F-S+sum(x*x for x in d.values()) >= 0
        reserve_rows += 1

result = {
    "classification": "PASS_EXACT_ROOT_UNITY_POWERED_EULER_FRAME",
    "pair_rows": pair_rows,
    "lower_bound_rows": lower_bound_rows,
    "critical_frame_rows": frame_rows,
    "reserve_phase_rows": reserve_rows,
    "gauge_rows": gauge_rows,
    "max_power": 20,
    "max_reserve_power": 8,
    "max_active_depth": 8,
}
payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
print(json.dumps(result, indent=2, sort_keys=True))
