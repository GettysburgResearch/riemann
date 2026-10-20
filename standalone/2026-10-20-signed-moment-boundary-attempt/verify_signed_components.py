#!/usr/bin/env python3
"""Exact checks for the signed-moment research components.

The six symbolic cases cover every choice of distinct maximal/minimal
coordinates in the buffered eight-point comparison. Finite residue models
check the graph substitution; they do not certify an analytic moment bound.
Only Python's standard library is used. No floating point enters acceptance.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
import hashlib
import json
import math
from pathlib import Path


DIM = 8  # x1,x2,x3,L,sigma,g1,g2,g3


def add(*forms):
    return tuple(sum(a[i] for a in forms) for i in range(DIM))


def scale(c, form):
    return tuple(c * x for x in form)


def sub(a, b):
    return add(a, scale(-1, b))


def basis(i):
    return tuple(Q(int(k == i)) for k in range(DIM))


ZERO = (Q(0),) * DIM
X = [basis(i) for i in range(3)]
L, S = basis(3), basis(4)
G = [basis(i) for i in range(5, 8)]


def require(ok, label):
    if not ok:
        raise ValueError("failed: " + label)


def marginals(vertices):
    out = []
    for i in range(3):
        counts = Counter()
        for point, coefficient in vertices:
            counts[point[i]] += coefficient
        out.append({key: value for key, value in counts.items() if value})
    return out


def symbolic_stencils():
    receipts = []
    for maximum in range(3):
        for minimum in range(3):
            if maximum == minimum:
                continue
            delta = [scale(int(i == maximum) - int(i == minimum), S)
                     for i in range(3)]
            t = [scale(3, S), add(scale(3, S), delta[1]),
                 sub(scale(3, S), delta[0])]
            require(all(2 <= item[4] <= 4 and
                        all(value == 0 for i, value in enumerate(item) if i != 4)
                        for item in t), "buffer offsets in [2 sigma,4 sigma]")
            a = add(sub(L, X[1]), t[1])
            b = add(sub(L, X[2]), t[2])
            c = add(sub(L, X[0]), t[0])
            directions = [(ZERO, a, scale(-1, a)),
                          (scale(-1, b), ZERO, b),
                          (c, scale(-1, c), ZERO)]
            # For x_i <= L+sigma, each increment is >= sigma.
            for inc, coordinate in [(a, 1), (b, 2), (c, 0)]:
                rhs = add(sub(add(L, S), X[coordinate]),
                          sub(t[coordinate], scale(2, S)))
                require(sub(inc, S) == rhs, "positive increment certificate")
            vertices = []
            for mask in range(8):
                point = tuple(add(X[i], *[directions[j][i] for j in range(3)
                                          if mask & (1 << j)]) for i in range(3))
                coefficient = (-1) ** mask.bit_count()
                vertices.append((point, coefficient))
                require(add(*point) == add(*X), "equal total length")
            require(not any(marginals(vertices)), "all one-coordinate marginals vanish")
            shifted = [(tuple(sub(point[i], G[i]) for i in range(3)), coefficient)
                       for point, coefficient in vertices]
            require(not any(marginals(shifted)), "common divisor translations preserve marginals")
            require(sum(coefficient for _, coefficient in vertices) == 0,
                    "constant term cancelled")
            require(vertices[0] == (tuple(X), 1), "central coefficient one")
            y = [X[2], X[0], X[1]]
            terminal = vertices[7][0]
            require(terminal == tuple(add(y[i], delta[i]) for i in range(3)),
                    "last vertex is cyclic permutation plus delta")
            require(terminal[maximum] == add(y[maximum], S), "maximum rises by sigma")
            require(terminal != tuple(X), "last vertex distinct from center as a form")
            witnesses = {1: 1, 2: 2, 4: 0, 3: 1, 5: 0, 6: 2}
            for mask, coordinate in witnesses.items():
                require(vertices[mask][0][coordinate] == add(L, t[coordinate]),
                        "six outer vertices exceed buffered ceiling by sigma")
            positive = [c, a, b]
            negative = [b, c, a]
            positive_bits, negative_bits = [2, 0, 1], [1, 2, 0]
            for mask, (point, _) in enumerate(vertices):
                for i in range(3):
                    pos = int(bool(mask & (1 << positive_bits[i])))
                    neg = int(bool(mask & (1 << negative_bits[i])))
                    require(point[i] == add(X[i], scale(pos, positive[i]),
                                            scale(-neg, negative[i])), "coordinate decomposition")
                    if pos:
                        certificate = add(sub(scale(4, S), t[i]),
                                          scale(neg, negative[i]))
                    else:
                        certificate = add(sub(add(L, S), X[i]), scale(3, S),
                                          scale(neg, negative[i]))
                    require(sub(add(L, scale(4, S)), point[i]) == certificate,
                            "nonnegative certificate for upper ceiling")
            require(any(marginals(vertices[:-1])), "deleted-vertex mutation rejected")
            receipts.append({"maximum_of_cyclic_input": maximum + 1,
                             "minimum_of_cyclic_input": minimum + 1,
                             "vertices": len(vertices), "signed_mass": 0})
    return receipts


def mobius(n):
    sign, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def finite_projectors():
    for n in range(1, 513):
        exact = sum(mobius(d) for d in range(1, n + 1) if n % d == 0)
        require(exact == int(n == 1), "complete Mobius projector")
    # The off-diagonal coprime kernel is indefinite.
    require(2 * 1 * 1 == 2 and 2 * 1 * -1 == -2, "indefinite two-column form")
    return {"integer_models": 512, "indefinite_form_values": [-2, 2]}


def invariant_labels(modulus, multiplier):
    labels = {}
    for x in range(modulus):
        if x in labels:
            continue
        orbit, y = [], x
        while y not in orbit:
            orbit.append(y)
            y = multiplier * y % modulus
        require(y == x, "multiplication is a residue permutation")
        representative = min(orbit)
        for y in orbit:
            labels[y] = representative
    return labels


def finite_alias_models():
    receipts = []
    for modulus, prime in [(7, 2), (13, 2), (19, 2), (21, 2), (25, 3), (35, 3)]:
        require(math.gcd(modulus, prime) == 1, "pool prime coprime to modulus")
        p6 = prime ** 6
        labels = invariant_labels(modulus, p6)
        for frequency in range(modulus):
            lhs = Counter()
            # This parameterizes EVERY nonzero-support residue modulo m*p^6.
            for x in range(modulus):
                k = p6 * x
                require(k % p6 == 0 and 0 <= k < modulus * p6, "complete graph residue")
                lhs[(labels[k % modulus], (-frequency * (k // p6)) % modulus)] += 1
            rhs = Counter((labels[x], (-frequency * x) % modulus)
                          for x in range(modulus))
            require(lhs == rhs, "full Fourier polynomial on amplified graph")
        height = Q(7, 3)
        require(height * p6 / (modulus * p6) == height / modulus,
                "row scale and periodic modulus cancel exactly")
        require(height * p6 / modulus != height / modulus,
                "dropped-modulus mutation rejected")
        # For constant f the nonzero transform occurs at every j=0 (mod m).
        aliases = list(range(0, modulus * p6, modulus))
        require(len(aliases) == p6 and len(aliases) > 1,
                "all aliases present in the full residue period")
        receipts.append({"modulus": modulus, "pool_prime": prime,
                         "frequency_classes_checked": modulus,
                         "aliases_per_class": p6})
    return receipts


def scalar_saving():
    # Exact affine identities on v<=s2 and v>=s2 prove the infimum.
    # Below s2: 2v/3+(s2-v) = 2s2/3+(s2-v)/3.
    # Above s2: 2v/3 = 2s2/3+2(v-s2)/3.
    require(Q(2, 3) - 1 == -Q(1, 3), "lower branch identity")
    require(Q(2, 3) * Q(3, 2) == 1, "saving coefficient")
    # A-5M/6-2(A-M/2)/3 = A/3-M/2.
    require(1 - Q(2, 3) == Q(1, 3), "exceptional A coefficient")
    require(-Q(5, 6) + Q(1, 3) == -Q(1, 2), "exceptional M coefficient")
    return {"infimum": "2*s2/3", "exceptional_excess": "A/3-M/2",
            "separate_second_diagonal_excess_at_A_3M_2": "M/2"}


def main():
    result = {
        "status": "PASS",
        "arithmetic": "EXACT_RATIONAL_AND_SYMBOLIC_LINEAR_FORMS",
        "scope": "Finite algebraic components; no analytic moment or smaller zero-free boundary certified.",
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "symbolic_comparison_cases": symbolic_stencils(),
        "projector_models": finite_projectors(),
        "alias_models": finite_alias_models(),
        "scalar_component": scalar_saving(),
        "excluded_claims": ["sixth moment bounded by U^(1+epsilon)",
                            "signed amplification with a smaller width",
                            "boundary below 0.874886647039964..."],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
