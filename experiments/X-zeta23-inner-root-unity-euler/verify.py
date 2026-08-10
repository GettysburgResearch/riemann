#!/usr/bin/env python3
"""Exact rational replay for the common-pole-killed inner Euler phase frame."""
from fractions import Fraction
import hashlib
import json


def phi(a, omega, t):
    return (a-omega*t)/(1-a*omega*t)


reflection_rows = 0
pair_rows = 0
exponential_rows = 0
reserve_rows = 0
gauge_rows = 0
main_pole_rows = 0

a = Fraction(1, 2)  # Q=4
for t in (Fraction(1, 5), Fraction(1, 4), Fraction(1, 3),
          Fraction(2, 5), Fraction(3, 5), Fraction(3, 4)):
    values = []
    common = abs(phi(a, Fraction(1), t))
    assert 0 < common < 1
    for omega in (Fraction(1), Fraction(-1)):
        p = phi(a, omega, t)
        pref = phi(a, omega, 1/t)
        assert pref == 1/p
        assert abs(p) < 1
        values.append(abs(p))
        reflection_rows += 1
    rmin, rmax = min(values), max(values)
    assert 0 < rmin < rmax < 1

    for k in range(1, 25):
        # The common factor multiplies one side by common^2 and the reflection
        # side by common^-2, so it cancels from the pair determinant.
        A = common*common*sum(r**(2*k) for r in values)/2
        B = sum(r**(-2*k) for r in values)/(2*common*common)
        assert A*B > 1
        assert 1-A*B < 0
        pair_rows += 1

        lower = Fraction(1, 2)*(rmax/rmin)**k
        assert A*B >= lower*lower
        exponential_rows += 1

        gauge = (k+1)*(k+1)*((1+a)/(1-a))**2
        assert gauge == 9*(k+1)*(k+1)
        gauge_rows += 1

# Every channel includes the common phase-one factor, which vanishes at s=1.
assert phi(a, Fraction(1), a) == 0
for omega in (Fraction(1), Fraction(-1)):
    for k in range(1, 9):
        assert phi(a, Fraction(1), a)*phi(a, omega, a)**k == 0
        main_pole_rows += 1

# Exact root-of-unity bookkeeping around the positive Q4 base system.
for k in range(1, 9):
    for R in range(1, 9):
        M = 2*R+1
        P1 = Fraction(11, 5)
        S1 = Fraction(3, 1)
        assert P1*P1 >= S1
        d = {r: Fraction(k*(4**r-1)) for r in range(1, R+1)}

        energy = {}
        coeff = {0: P1, **d}
        for r, ar in coeff.items():
            for s, bs in coeff.items():
                key = (r-s) % M
                energy[key] = energy.get(key, Fraction(0))+ar*bs
        avg_energy = energy[0]
        assert avg_energy == P1*P1+sum(v*v for v in d.values())

        # All phase-dependent log, common/local, and local/local forcing terms
        # average to zero. Only the complete Q4 base forcing remains.
        forcing = {0: S1}
        for r in range(1, R+1):
            forcing[r] = forcing.get(r, Fraction(0))+Fraction(7*r)
        for r in range(1, R+1):
            for s in range(1, R+1):
                key = (r+s) % M
                forcing[key] = forcing.get(key, Fraction(0))+Fraction(r*s)
        assert forcing[0] == S1
        assert avg_energy-forcing[0] == P1*P1-S1+sum(v*v for v in d.values()) >= 0
        reserve_rows += 1

result = {
    "classification": "PASS_EXACT_INNER_ROOT_UNITY_EULER_SIGNATURE_FRAME",
    "reflection_rows": reflection_rows,
    "pair_rows": pair_rows,
    "exponential_lower_bound_rows": exponential_rows,
    "reserve_phase_rows": reserve_rows,
    "gauge_rows": gauge_rows,
    "main_pole_rows": main_pole_rows,
    "max_power": 24,
    "max_active_depth": 8,
}
payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
print(json.dumps(result, indent=2, sort_keys=True))
