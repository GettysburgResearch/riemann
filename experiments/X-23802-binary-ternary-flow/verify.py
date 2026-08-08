#!/usr/bin/env python3
from fractions import Fraction
import hashlib
import json

X = 12
A = {n: Fraction(((-1) ** n) * (n % 5 + 1), 37) for n in range(2, X + 1)}


def splits(n):
    a3 = (n + 2) // 3
    b3 = n - a3
    a2 = n // 2
    b2 = n - a2
    return [(a3, b3, Fraction(1, 2)), (a2, b2, Fraction(1, 2))]


def chi(n, j, q):
    return n // q - j // q - (n - j) // q


def mobius(N):
    mu = [0] * (N + 1)
    mu[1] = 1
    primes = []
    lp = [0] * (N + 1)
    for i in range(2, N + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > N or p > lp[i]:
                break
            lp[i * p] = p
            mu[i * p] = 0 if p == lp[i] else -mu[i]
    return mu


# Construct the divergence from the signed split flow.
r = [Fraction(0) for _ in range(X + 1)]
for n, a in A.items():
    for j, k, p in splits(n):
        v = p * a
        r[n] += v
        r[j] -= v
        r[k] -= v

assert sum(Fraction(n) * r[n] for n in range(1, X + 1)) == 0

# Floor-transform carry target.
w = [Fraction(0) for _ in range(X + 1)]
for q in range(1, X + 1):
    w[q] = sum(r[n] * (n // q) for n in range(1, X + 1))
assert w[1] == 0

# Recover the divergence by Möbius tail inversion.
mu = mobius(X)
u = [Fraction(0) for _ in range(X + 2)]
for m in range(1, X + 1):
    u[m] = sum(Fraction(mu[k]) * w[m * k] for k in range(1, X // m + 1))
r2 = [Fraction(0) for _ in range(X + 1)]
for m in range(1, X + 1):
    r2[m] = u[m] - u[m + 1]
assert r2 == r

# Recover the original coefficients by the descending recurrence.
incoming = [Fraction(0) for _ in range(X + 1)]
A2 = {}
for n in range(X, 1, -1):
    A2[n] = r[n] + incoming[n]
    for j, k, p in splits(n):
        incoming[j] += p * A2[n]
        incoming[k] += p * A2[n]
assert r[1] + incoming[1] == 0
assert A2 == A

# Direct atomized carry loads agree with the floor transform.
loads = [Fraction(0) for _ in range(X + 1)]
for n, a in A.items():
    for j, k, p in splits(n):
        for q in range(2, X + 1):
            loads[q] += p * a * chi(n, j, q)
assert loads[2:] == w[2:]

proof = {
    "schema": "riemann.x23802.binary-ternary-flow.v1",
    "X": X,
    "coefficients": {str(k): str(v) for k, v in A.items()},
    "divergence": {str(k): str(r[k]) for k in range(1, X + 1)},
    "target": {str(k): str(w[k]) for k in range(1, X + 1)},
    "checks": [
        "size_moment_zero",
        "mobius_tail_reconstruction",
        "descending_recurrence",
        "node_one_closure",
        "direct_carry_loads",
    ],
}
blob = json.dumps(proof, sort_keys=True, separators=(",", ":")).encode()
proof["proof_object_sha256"] = hashlib.sha256(blob).hexdigest()
proof["verdict"] = "PASS_EXACT_BINARY_TERNARY_FLOW_ALGEBRA"
print(json.dumps(proof, sort_keys=True, indent=2))
