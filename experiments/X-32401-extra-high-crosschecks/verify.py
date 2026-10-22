#!/usr/bin/env python3
from fractions import Fraction
import hashlib
import json

X = 50

V = {
    4:1, 5:-1, 6:1, 7:2, 8:-2, 9:-1, 10:3, 11:1, 12:-3, 13:1,
    17:2, 18:1, 19:4, 20:5, 21:-5, 22:-5, 23:-5,
}
for q in range(24, 51):
    V[q] = 5

def chi(n, j, q):
    return n // q - j // q - (n-j) // q

edge_values = []
for n in range(2, X+1):
    for j in range((n+3)//4, n//2 + 1):
        value = sum(V.get(q, 0) * chi(n, j, q) for q in range(2, X+1))
        if value < 0:
            raise AssertionError((n, j, value))
        edge_values.append((n, j, value))

assert len(edge_values) == 337
assert sum(value == 0 for _,_,value in edge_values) == 30
assert sum(value > 0 for _,_,value in edge_values) == 307
prefix_pairing = sum(V.get(q, 0) for q in range(2, 24))
assert prefix_pairing == -1

# Elementary zeta(3/2) majorant used in L-32401.
assert Fraction(71,100)**2 > Fraction(1,2)
assert Fraction(579,1000)**2 > Fraction(1,3)
assert Fraction(45,100)**2 > Fraction(1,5)
assert Fraction(56,125)**2 > Fraction(1,5)
zeta_upper = (
    Fraction(1)
    + Fraction(71,200)
    + Fraction(193,1000)
    + Fraction(1,8)
    + Fraction(9,100)
    + Fraction(112,125)
)
assert zeta_upper == Fraction(2659,1000)
assert zeta_upper < Fraction(8,3)

# Rational square bounds for B(1/2).
A = Fraction(8165,10000)
B = Fraction(7071,10000)
assert A*A - Fraction(2,3) == Fraction(67,12000000)
assert Fraction(1,2) - B*B == Fraction(959,100000000)
bulk_upper = (8*A - 5*B) / 3
assert bulk_upper == Fraction(5993,6000)
assert Fraction(999,1000) - bulk_upper == Fraction(1,6000)

payload = {
    "verdict": "PASS_EXACT_EXTRA_HIGH_REDO_CROSSCHECKS",
    "balanced_edges": len(edge_values),
    "separator_zero_edges": sum(value == 0 for _,_,value in edge_values),
    "separator_positive_edges": sum(value > 0 for _,_,value in edge_values),
    "monotone_prefix_pairing": prefix_pairing,
    "zeta_3_over_2_upper": [zeta_upper.numerator, zeta_upper.denominator],
    "bulk_row_upper": [bulk_upper.numerator, bulk_upper.denominator],
    "reserve_below_999_over_1000": [
        (Fraction(999,1000)-bulk_upper).numerator,
        (Fraction(999,1000)-bulk_upper).denominator,
    ],
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
print(json.dumps(payload, indent=2, sort_keys=True))
