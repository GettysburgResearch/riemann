#!/usr/bin/env python3
"""
Exact regression for the Blaschke--Krylov finite-packet noncollapse theorem.

Standard library only.  All arithmetic is Fraction.

The replay checks:
  * Q4/half-plane reflection and J-unitary scalar invariance;
  * exact two-row Krylov Gram, reflected-pair eigenvalues, and capture cost;
  * the model-kernel telescoping identity;
  * an eight-point packet with one target reflected pair, two off-line
    nuisance pairs, and two critical-line nuisances;
  * convergence of the finite-packet capture cost toward the exact
    Szego-Schur limit 9800/81.
"""
from fractions import Fraction
import hashlib
import json


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]


def inverse(a):
    n = len(a)
    m = [
        list(row) + [Fraction(int(i == j)) for j in range(n)]
        for i, row in enumerate(a)
    ]
    for col in range(n):
        pivot = next(i for i in range(col, n) if m[i][col] != 0)
        m[col], m[pivot] = m[pivot], m[col]
        value = m[col][col]
        m[col] = [x/value for x in m[col]]
        for i in range(n):
            if i == col:
                continue
            factor = m[i][col]
            if factor:
                m[i] = [x-factor*y for x, y in zip(m[i], m[col])]
    return [row[n:] for row in m]


def quadratic(t, a):
    return sum(t[i]*a[i][j]*t[j]
               for i in range(len(t)) for j in range(len(t)))


def krylov_row(w, k):
    return [w**j for j in range(k)]


def gram(ws, k):
    v = [krylov_row(w, k) for w in ws]
    return matmul(v, transpose(v))


def target_schur(kmat, target_size=2):
    a = [row[:target_size] for row in kmat[:target_size]]
    b = [row[target_size:] for row in kmat[:target_size]]
    d = [row[target_size:] for row in kmat[target_size:]]
    correction = matmul(matmul(b, inverse(d)), transpose(b))
    return [
        [a[i][j]-correction[i][j] for j in range(target_size)]
        for i in range(target_size)
    ]


# 1. Scalar reflection/J-unitarity, checked on rational controls.
reflection_rows = 0
for a in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
    for x in (Fraction(1, 5), Fraction(2, 5), Fraction(3, 5)):
        # phi=(a-x)/(1-a*x); reflected x is 1/x.
        phi = (a-x)/(1-a*x)
        phi_reflected = (a-1/x)/(1-a/x)
        assert phi_reflected == 1/phi
        for k in range(1, 12):
            # diag(phi^k,phi_reflected^k)^T J diag(...) = J.
            assert phi**k * phi_reflected**k == 1
            reflection_rows += 1

# 2. Pair spectrum/capture identities.
pair_rows = 0
for r in (Fraction(1, 5), Fraction(1, 3), Fraction(1, 2),
          Fraction(2, 3), Fraction(4, 5)):
    for k in range(2, 25):
        aa = sum(r**(2*j) for j in range(k))
        bb = sum(r**(-2*j) for j in range(k))
        cross = Fraction(k)
        depth = aa * r**(-(k-1))
        assert aa*bb == depth*depth
        assert depth > k

        # The nonzero eigenvalues of ab^T+ba^T are k +/- depth.
        trace = 2*cross
        determinant = cross*cross-aa*bb
        lam_plus = cross+depth
        lam_minus = cross-depth
        assert lam_plus+lam_minus == trace
        assert lam_plus*lam_minus == determinant
        assert lam_minus < 0

        ginv = inverse([[aa, cross], [cross, bb]])
        capture = quadratic([Fraction(1), Fraction(-1)], ginv)
        closed = (aa+bb+2*cross)/(aa*bb-cross*cross)
        assert capture == closed
        pair_rows += 1

# 3. Model-kernel telescoping.
kernel_rows = 0
for x in (Fraction(1, 7), Fraction(1, 4), Fraction(2, 5)):
    for y in (Fraction(1, 8), Fraction(1, 3), Fraction(3, 7)):
        for k in range(1, 15):
            lhs = 1-(x*y)**k
            rhs = (1-x*y)*sum((x*y)**j for j in range(k))
            assert lhs == rhs
            kernel_rows += 1

# 4. Finite packet.
# target right/left: 1/3,3
# nuisance off-line pairs: 1/2,2 and 2/3,3/2
# critical-line nuisance phases: +1,-1.
packet = [
    Fraction(1, 3), Fraction(3),
    Fraction(1, 2), Fraction(2),
    Fraction(2, 3), Fraction(3, 2),
    Fraction(1), Fraction(-1),
]
capture_table = []
previous = None
for k in (8, 10, 12, 16, 20, 24, 32, 48, 64):
    kmat = gram(packet, k)
    schur = target_schur(kmat)
    capture = quadratic([Fraction(1), Fraction(-1)], inverse(schur))
    if previous is not None:
        assert capture < previous
    previous = capture
    capture_table.append({
        "k": k,
        "numerator": capture.numerator,
        "denominator": capture.denominator,
        "decimal": float(capture),
    })

# Exact limiting right-half Szego Schur.
w0 = Fraction(1, 3)
v1 = Fraction(1, 2)
v2 = Fraction(2, 3)
szego_limit = (
    Fraction(1, 1)/(1-w0*w0)
    * ((w0-v1)/(1-v1*w0))**2
    * ((w0-v2)/(1-v2*w0))**2
)
assert szego_limit == Fraction(81, 9800)
capture_limit = 1/szego_limit
assert capture_limit == Fraction(9800, 81)
assert capture_table[-1]["decimal"] < 128
assert capture_table[-1]["decimal"] > float(capture_limit)

result = {
    "classification": "PASS_EXACT_BLASCHKE_KRYLOV_FINITE_NONCOLLAPSE",
    "reflection_rows": reflection_rows,
    "pair_rows": pair_rows,
    "kernel_rows": kernel_rows,
    "packet_size": len(packet),
    "capture_table": capture_table,
    "szego_schur_limit": [szego_limit.numerator, szego_limit.denominator],
    "capture_limit": [capture_limit.numerator, capture_limit.denominator],
}
payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
print(json.dumps(result, indent=2, sort_keys=True))
