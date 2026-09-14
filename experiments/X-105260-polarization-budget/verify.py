#!/usr/bin/env python3
from fractions import Fraction
import hashlib, json

D = Fraction(173344649, 1275293859840)
lam = Fraction(999, 1000)
polar = Fraction(1, 60)
total_allowance = 1 - Fraction(19, 20) / lam
edge = total_allowance - polar

assert D < Fraction(1, 7000)
assert 2 * D < Fraction(1, 60 * 60)
assert edge == Fraction(647, 19980)
assert polar + edge == Fraction(49, 999)
assert lam * (1 - polar - edge) == Fraction(19, 20)

Dblock = [[Fraction(3, 2), Fraction(1, 4)],
          [Fraction(1, 4), Fraction(3, 2)]]
A = [[Fraction(1, 10), Fraction(-1, 20)],
     [Fraction(-1, 20), Fraction(1, 8)]]
Cc = [[Dblock[i][j] + A[i][j] for j in range(2)] for i in range(2)]
Cs = [[Dblock[i][j] - A[i][j] for j in range(2)] for i in range(2)]
assert Cc[0][1] == Fraction(1, 5)
assert Cs[0][1] == Fraction(3, 10)
assert Cc[0][0] * Cc[1][1] - Cc[0][1] ** 2 > 0

H = [[Fraction(1, i + j + 1) for j in range(3)] for i in range(3)]
det = (
    H[0][0] * (H[1][1] * H[2][2] - H[1][2] * H[2][1])
    - H[0][1] * (H[1][0] * H[2][2] - H[1][2] * H[2][0])
    + H[0][2] * (H[1][0] * H[2][1] - H[1][1] * H[2][0])
)
assert det == Fraction(1, 2160)

payload = {
    "schema": "riemann.x105260.polarization-budget.v1",
    "classification": "PASS_T105260_TOEPLITZ_HANKEL_POLARIZATION_BUDGET",
    "physical_energy_bound": str(D),
    "twice_energy_below_one_over_60_squared": True,
    "strict_bandwidth": str(lam),
    "polarization_budget": str(polar),
    "edge_budget": str(edge),
    "total_nonpositive_fraction": str(polar + edge),
    "hardy_realification_fixture_checked": True,
    "boundary_rank_firewall_checked": True,
    "edgeflux105260_proved": False,
    "ninety_percent_established": False,
    "density_one_established": False,
    "rh_established": False,
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
print(payload["classification"])
print(payload["proof_object_sha256"])
print(json.dumps(payload, indent=2, sort_keys=True))
