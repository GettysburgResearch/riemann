"""Exact finite controls for CENTERED_NATIVE_SIGN.md.

The proof is in the note. This standard-library checker verifies the inert
finite fields, cubic fiber sums, complete six-unit row phases, and both
correctly product-diagonal-centered covariance witnesses using only integers
and rational numbers. It does not establish an asymptotic estimate.
"""

import json
import math
from collections import Counter, defaultdict
from fractions import Fraction


COUNT = Counter()
PRIMES = (5, 11, 53, 71)
UNITS = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))
ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def require(value, kind):
    COUNT[kind] += 1
    if not value:
        raise RuntimeError("Failed exact predicate: " + kind)


def multiply(x, y, p):
    a, b = x
    c, d = y
    return ((a * c - b * d) % p, (a * d + b * c - b * d) % p)


def power(x, n, p):
    out = (1, 0)
    while n:
        if n & 1:
            out = multiply(out, x, p)
        x = multiply(x, x, p)
        n //= 2
    return out


def sextic_exponent(x, p):
    x = (x[0] % p, x[1] % p)
    if x == (0, 0):
        return None
    value = power(x, (p * p - 1) // 6, p)
    matches = [
        j for j, unit in enumerate(UNITS)
        if value == (unit[0] % p, unit[1] % p)
    ]
    require(len(matches) == 1, "sextic_root_identification")
    return matches[0]


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def main():
    unit_phases = {}
    for p in PRIMES:
        require(p > 3 and p % 3 == 2, "inert_congruence")
        require(all(p % d for d in range(2, math.isqrt(p) + 1)), "rational_prime")
        require(all((x * x + x + 1) % p for x in range(p)), "irreducible_field")
        for b in range(p):
            cubic_fiber = (0, 0)
            for a in range(p):
                j = sextic_exponent((a, b), p)
                if j is not None:
                    cubic_fiber = add(cubic_fiber, ROOTS[(2 * j) % 6])
            require(
                cubic_fiber == ((p - 1, 0) if b == 0 else (-1, 0)),
                "exact_cubic_fiber",
            )
        unit_phases[p] = [sextic_exponent(unit, p) for unit in UNITS]

    for p in PRIMES:
        for q in PRIMES:
            if p == q:
                continue
            j = sextic_exponent((-p, 0), q)
            require(j is not None and (4 * j) % 6 == 0, "inert_cross_symbol")

    columns = ((53, (53,)), (71, (71,)), (55, (5, 11)))
    for _, factors in columns:
        for j in range(6):
            require(
                sum(unit_phases[p][j] for p in factors) % 6 == 0,
                "whole_unit_row_phase",
            )

    outputs = []
    for t, expected in ((Fraction(1, 2), (0, 36, -36)), (Fraction(3), (600, 456, 144))):
        weights = (Fraction(1), Fraction(1), t)
        face = defaultdict(Fraction)
        completion = defaultdict(Fraction)
        for i, (n1, f1) in enumerate(columns):
            for j, (n2, f2) in enumerate(columns):
                common = set(f1) & set(f2)
                if common:
                    # Both factors are squarefree, so a common prime has the
                    # exact zero local pattern (1,1) in the full A2 table.
                    continue
                require(math.gcd(n1, n2) == 1, "face_coprimality")
                coefficient = (-1) ** (len(f1) + len(f2)) * weights[i] * weights[j]
                face[n1 * n2] += coefficient
                completion[n1 * n2] += coefficient
        require(dict(face) == dict(completion), "full_completion_equals_face")
        require(len(face) == 3, "distinct_product_columns")
        energy = 6 * sum(face.values()) ** 2
        diagonal = 6 * sum(abs(value) ** 2 for value in face.values())
        centered = energy - diagonal
        require((energy, diagonal, centered) == expected, "literal_centered_witness")
        require(centered == 48 * t * (t - 2), "symbolic_centered_formula")
        outputs.append({
            "t": str(t),
            "product_coefficients": {str(n): str(z) for n, z in sorted(face.items())},
            "energy": str(energy),
            "product_diagonal": str(diagonal),
            "centered": str(centered),
        })
    print(json.dumps({
        "status": "PASS",
        "scope": "finite exact genuine coefficient controls only",
        "unit_sextic_exponents": unit_phases,
        "witnesses": outputs,
        "predicates": dict(sorted(COUNT.items())),
        "predicate_total": sum(COUNT.values()),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
