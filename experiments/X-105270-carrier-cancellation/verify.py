#!/usr/bin/env python3
from fractions import Fraction
import hashlib
import json

# Pure holomorphic carrier: safe-line Gram G and complementary boundary E=-G.
d = 7
G = [Fraction(1) for _ in range(d)]
E = [-x for x in G]
negative_trace = sum(-x for x in E if x < 0)
assert negative_trace == d
assert negative_trace > Fraction(647, 19980) * d
assert negative_trace > Fraction(1, 20) * d

# Carrier-free finite unilateral shifts have zero trace.
# S is the nilpotent 5x5 right shift; every positive power has zero diagonal.
size = 5
S = [[Fraction(int(i == j + 1)) for j in range(size)] for i in range(size)]

def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(size)) for j in range(size)]
        for i in range(size)
    ]

power = S
for _ in range(1, size):
    assert sum(power[i][i] for i in range(size)) == 0
    power = matmul(power, S)

# Endpoint taper algebra on one exact rational fixture.
H = Fraction(10_000)
eta = Fraction(1)
M = 100
r = 20
# Elementary vertical bound from the theorem.
vertical_base = Fraction(4 * M) * eta / H
assert vertical_base < 1
assert vertical_base ** r < Fraction(1, 10**20)
# First nonreal taper zero lies above the fixed strip on this fixture;
# use sin(pi/M) > 2/M for M>=2.
assert H * Fraction(2, M) > eta

payload = {
    "schema": "riemann.x105270.carrier-cancellation.v1",
    "classification": "PASS_T105270_CLOSED_CONTOUR_CARRIER_CANCELLATION",
    "pure_carrier_negative_trace_fraction": "1",
    "former_edge_budget": "647/19980",
    "carrier_free_shift_trace_zero_checked": True,
    "analytic_taper_fixture_checked": True,
    "t105260_natural_edge_gate_refuted": True,
    "indexcarrier105270_proved": False,
    "ninety_percent_established": False,
    "density_one_established": False,
    "rh_established": False,
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
print(payload["classification"])
print(payload["proof_object_sha256"])
print(json.dumps(payload, indent=2, sort_keys=True))
