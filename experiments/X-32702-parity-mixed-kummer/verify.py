#!/usr/bin/env python3
from fractions import Fraction
from math import comb
import hashlib
import json


def carry(n, j, d):
    return n // d - j // d - (n - j) // d


def oddpart(n):
    while n and n % 2 == 0:
        n //= 2
    return n


def v2int(n):
    c = 0
    while n and n % 2 == 0:
        n //= 2
        c += 1
    return c


rows_product = 0
rows_boundary = 0
rows_kummer = 0
rows_j2 = 0

# Exact four-adic product-carry identity from L-32704.16.
for n in range(2, 257):
    for j in range(n + 1):
        a = 4
        while a <= n:
            N = n // a
            J = j // a
            c = carry(n, j, a)
            for q in range(1, N + 1):
                lhs = carry(n, j, a * q)
                rhs = carry(N, J, q) + c * (1 if (N - J) % q == 0 else 0)
                assert lhs == rhs, (n, j, a, q, lhs, rhs)
                rows_product += 1
            a *= 4

# Kummer's binary-carry valuation cannot exceed the number of binary
# positions below the leading bit of n.
for n in range(2, 513):
    m = n.bit_length() - 1
    for j in range(n + 1):
        b = comb(n, j)
        assert v2int(b) <= m, (n, j, b, v2int(b), m)
        rows_kummer += 1

# Exact integer version of current-row mixed-boundary absorption:
# odd(N-J) <= odd(binomial(n,j)) whenever the 4^r carry is active.
for n in range(2, 513):
    for j0 in range(1, n):
        j = min(j0, n - j0)
        Bodd = oddpart(comb(n, j))
        a = 4
        while a <= n:
            c = carry(n, j, a)
            if c:
                N = n // a
                J = j // a
                assert N - J > 0
                assert oddpart(N - J) <= Bodd, (
                    n,
                    j,
                    a,
                    N,
                    J,
                    oddpart(N - J),
                    Bodd,
                )
                rows_boundary += 1
            a *= 4

# j=2 exact odd-binomial factorization used in L-32704.35.
for n in range(3, 513):
    lhs = oddpart(comb(n, 2))
    rhs = oddpart(n) * oddpart(n - 1)
    assert lhs == rhs, (n, lhs, rhs)
    rows_j2 += 1

# Exact rational coefficient moat in the j>=8 cofinal argument.
for j in range(8, 10000):
    moat = Fraction(49 * j * (j - 8) + 64, 64)
    assert moat > 0
assert Fraction(35, 8) < Fraction(9, 2)

payload = {
    "classification": "PASS_EXACT_FOUR_ADIC_MIXED_KUMMER_ALGEBRA",
    "product_carry_rows": rows_product,
    "binary_kummer_rows": rows_kummer,
    "boundary_absorption_rows": rows_boundary,
    "j2_rows": rows_j2,
    "uniform_moat": "[49*j*(j-8)+64]/64 > 0 for j>=8",
}
blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["proof_object_sha256"] = hashlib.sha256(blob).hexdigest()
print(json.dumps(payload, sort_keys=True, indent=2))
