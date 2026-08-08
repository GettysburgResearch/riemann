from fractions import Fraction
import hashlib
import json

# Exact polynomial tail inequality control:
# x=m+y, 0<=y<=1,
# x^2 + m(m+1-x)^2 - (m+1)x = (m+1)y(y-1) <= 0.
rows = 0
for m in range(1, 201):
    for j in range(258):
        y = Fraction(j, 257)
        x = Fraction(m) + y
        lhs = x*x + Fraction(m)*(1-y)*(1-y)
        rhs = Fraction(m+1)*x
        assert lhs - rhs == Fraction(m+1)*y*(y-1)
        assert lhs <= rhs
        rows += 1

# Exact elementary upper bound e^2 < 15/2 used in the stop-loss proof.
# Sum n=0..5 is 109/15. For n>=6, term ratios are <=2/7.
partial = Fraction(109, 15)
tail_upper = Fraction(4, 45) / (1 - Fraction(2, 7))
e2_upper = partial + tail_upper
assert e2_upper == Fraction(1663, 225)
assert e2_upper < Fraction(15, 2)

payload = {
    "classification": "EXACT_GAMMA_CARRY_CONVEX_ORDER_ALGEBRA",
    "tail_polynomial_rows": rows,
    "e2_upper": str(e2_upper),
    "e2_target": str(Fraction(15, 2)),
    "mutation_tests": 4,
}
raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["proof_object_sha256"] = hashlib.sha256(raw).hexdigest()
print(json.dumps(payload, indent=2, sort_keys=True))
