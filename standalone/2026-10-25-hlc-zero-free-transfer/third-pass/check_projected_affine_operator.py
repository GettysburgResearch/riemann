#!/usr/bin/env python3
"""Exact finite checks for PROJECTED_AFFINE_OPERATOR.md.

These checks do not certify an arithmetic HLC estimate or a Kloosterman
bound. All acceptance predicates remain active under python -O.
"""

from fractions import Fraction as F


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def avg(values):
    return sum(values, F(0)) / len(values)


def variance(values):
    return avg([v * v for v in values]) - avg(values) ** 2


def dist(x, p):
    x %= p
    return min(x, p - x)


affine_cases = 0
projection_error_cases = 0
negative_controls = 0
for p in [3, 5, 7, 11, 13]:
    f = [F((-1) ** x * (x + 1), p) for x in range(p)]
    g = [F((x * x + 3 * x + 1) % (2 * p) - p, p)
         for x in range(p)]
    masks = [
        [1] * p,
        [int(x % 3 != 0) for x in range(p)],
        [int(x >= p // 3) for x in range(p)],
        [int(x == 0 or dist(pow(x, -1, p), p) > 1)
         for x in range(p)],
    ]
    for P in masks:
        for Q in masks:
            pf = [P[x] * f[x] for x in range(p)]
            qg = [Q[x] * g[x] for x in range(p)]
            mqg = avg(qg)
            centered = []
            uncentered = []
            for q in range(1, p):
                for h in range(p):
                    raw = avg([pf[x] * qg[(q * x + h) % p]
                               for x in range(p)])
                    centered.append((raw - avg(pf) * mqg) ** 2)
                    uncentered.append(raw ** 2)
            expected = variance(pf) * variance(qg) / (p - 1)
            require(avg(centered) == expected,
                    "Fixed-projector centered affine identity")
            require(avg(uncentered) == expected + avg(pf) ** 2 * mqg ** 2,
                    "Uncentered affine mean term")
            if avg(pf) * mqg != 0:
                require(avg(uncentered) != expected,
                        "Negative control: centering cannot be omitted")
                negative_controls += 1
            affine_cases += 1

    mf, mg = avg(f), avg(g)
    supf, supg = max(map(abs, f)), max(map(abs, g))
    for q in range(1, p):
        for h in range(p):
            P = [int(dist((1 - q) * x - h, p) > 1)
                 for x in range(p)]
            Q = [int((x + q + h) % 5 != 0) for x in range(p)]
            pf = [P[x] * f[x] for x in range(p)]
            qg = [Q[x] * g[x] for x in range(p)]
            actual = avg([pf[x] * qg[(q * x + h) % p]
                          for x in range(p)]) - avg(pf) * avg(qg)
            base = avg([f[x] * g[(q * x + h) % p]
                        for x in range(p)]) - mf * mg
            dp, dq = 1 - avg(P), 1 - avg(Q)
            require(abs(actual - base) <= 2 * (dp + dq) * supf * supg,
                    "Pointwise projector error bound")
            projection_error_cases += 1


fibre_cases = 0
compressed_cases = 0
mean_zero_cases = 0
for p in [3, 5, 7, 11, 13]:
    N = p - 1
    for v in [(1, 0), (0, 1), (1, 2)]:
        for c in sorted({1, 2 % p, p - 1}):
            require(c != 0, "Nonzero determinant")

            def determinant(z):
                return (z[0] * v[1] - z[1] * v[0]) % p

            X = [(a, b) for a in range(p) for b in range(p)
                 if determinant((a, b)) != 0]
            Y = list(range(1, p))
            phi = {z: c * pow(determinant(z), -1, p) % p for z in X}
            fibres = {t: [z for z in X if phi[z] == t] for t in Y}
            require(len(X) == p * N, "Source cardinality")
            require(all(len(fibres[t]) == p for t in Y),
                    "Uniform determinant fibres")
            for z in X:
                t = phi[z]
                target = (t * v[0] % p, t * v[1] % p)
                require((z[0] * target[1] - z[1] * target[0]) % p == c,
                        "Exact dirty determinant and line")
                fibre_cases += 1

            source_masks = [
                set(X),
                {z for z in X if (z[0] + 2 * z[1]) % p != 0},
                {z for z in X if dist(pow(determinant(z), -1, p), p) > 1},
                {z for z in X if (z[0] + 3 * z[1]) % 4 != 0},
            ]
            target_masks = [
                set(Y),
                {t for t in Y if t % 2},
                {t for t in Y if t > N // 3},
            ]
            for A in source_masks:
                retained = {t: F(len(A.intersection(fibres[t])), p) for t in Y}
                delta = 1 - F(len(A), len(X))
                require(avg(list(retained.values())) == 1 - delta,
                        "Compressed Gram average")
                for B in target_masks:
                    if not B:
                        continue
                    alpha = F(len(B), N)
                    lower = max(F(0), 1 - delta / alpha)
                    require(max(retained[t] for t in B) >= lower,
                            "Compressed norm lower bound")
                    for s in B:
                        for t in B:
                            gram = F(sum(int(z in A and phi[z] == s
                                             and phi[z] == t) for z in X), p)
                            require(gram == (retained[t] if s == t else 0),
                                    "Exact diagonal compressed Gram matrix")
                    compressed_cases += 1
                    if len(B) >= 2:
                        top = sorted(B, key=lambda t: retained[t], reverse=True)[:2]
                        g = {t: F(int(t == top[0]) - int(t == top[1])) for t in Y}
                        require(sum(g.values()) == 0, "Mean-zero target test")
                        norm_in = avg([g[t] ** 2 for t in Y])
                        norm_out = avg([int(z in A) * g[phi[z]] ** 2 for z in X])
                        require(norm_out / norm_in
                                == (retained[top[0]] + retained[top[1]]) / 2,
                                "Centered two-fibre Rayleigh quotient")
                        require(norm_out / norm_in >= lower,
                                "Centered compressed norm lower bound")
                        mean_zero_cases += 1

require(negative_controls > 0, "Centering negative control exercised")
print("EXACT fixed-projector affine identities:", affine_cases, "PASS")
print("EXACT varying-projector errors:", projection_error_cases, "PASS")
print("EXACT dirty incidence constraints:", fibre_cases, "PASS")
print("EXACT compressed Gram cases:", compressed_cases, "PASS")
print("EXACT mean-zero lower bounds:", mean_zero_cases, "PASS")
print("NEGATIVE CONTROL: omitted centered comparison PASS")
print("No full HLC dirty-edge estimate or Möbius correlation certified.")
