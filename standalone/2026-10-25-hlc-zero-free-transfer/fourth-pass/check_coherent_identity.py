#!/usr/bin/env python3
"""Finite algebra and exact exponent checks for COHERENT_IDENTITY.md.

No analytic premise or unproved corner bound is tested by this program.
All predicates are explicit and remain active under python -O.
"""

from fractions import Fraction as Q
from itertools import product
from math import gcd, isqrt
import json

COUNTS = {}


def require(condition, label):
    if not condition:
        raise RuntimeError(label)
    COUNTS[label.split(":", 1)[0]] = COUNTS.get(label.split(":", 1)[0], 0) + 1


def mu(n):
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -sign if n > 1 else sign


def cutoff(x):
    if x <= 1:
        return Q(1)
    if x >= 2:
        return Q(0)
    return 2 - x


def symbolic_local_shift():
    # Exact polynomials over Q in x,y,v,q^{-1}; no sampled substitution.
    one = {(0, 0, 0, 0): Q(1)}

    def variable(i):
        e = [0, 0, 0, 0]
        e[i] = 1
        return {tuple(e): Q(1)}

    def scale(p, c):
        return {e: a * c for e, a in p.items() if a * c}

    def add(*ps):
        out = {}
        for p in ps:
            for e, a in p.items():
                out[e] = out.get(e, Q(0)) + a
        return {e: a for e, a in out.items() if a}

    def mul(*ps):
        out = one
        for p in ps:
            new = {}
            for e, a in out.items():
                for f, b in p.items():
                    g = tuple(e[j] + f[j] for j in range(4))
                    new[g] = new.get(g, Q(0)) + a * b
            out = {e: a for e, a in new.items() if a}
        return out

    x, y, v, qi = (variable(j) for j in range(4))
    X, Y = mul(x, v), mul(y, v)
    delta = mul(add(one, scale(mul(X, qi), -1)),
                add(one, scale(mul(Y, qi), -1)))
    shifted = [delta, add(scale(X, -1), scale(Y, -1), mul(X, Y, qi)),
               mul(X, Y)]
    direct = [
        add(one, scale(mul(add(x, y), v, qi), -1), mul(x, y, v, v, qi, qi)),
        mul(v, add(scale(x, -1), scale(y, -1), mul(x, y, v, qi))),
        mul(v, v, x, y),
    ]
    for j in range(3):
        require(direct[j] == shifted[j],
                "symbolic_mellin_local_shift:" + str(j))
    # Deliberately omit the repeated-prime term in the p coefficient.
    require(add(scale(X, -1), scale(Y, -1)) != shifted[1],
            "negative_control_repeated_prime")


def finite_harmonic_euler():
    primes = (2, 3, 5)
    sf = list(product((0, 1), repeat=3))
    af = list(product((0, 1, 2), repeat=3))
    for trial in range(1, 5):
        xs = [Q(p + trial, p + trial + 2) for p in primes]
        ys = [Q(p + 2 * trial, p + 2 * trial + 3) for p in primes]
        vs = [Q(p + 1, p) for p in primes]
        for mask in sf:
            factor = Q(1)
            for j, p in enumerate(primes):
                if not mask[j]:
                    factor *= (1 - xs[j] * vs[j] / p) * (1 - ys[j] * vs[j] / p)
            for ae in af:
                if any(mask[j] and ae[j] for j in range(3)):
                    continue
                norm_a = 1
                for j, p in enumerate(primes):
                    norm_a *= p ** ae[j]
                direct = Q(0)
                for le in sf:
                    for re in sf:
                        if any(le[j] + re[j] < ae[j] for j in range(3)):
                            continue
                        if any(mask[j] and le[j] + re[j] for j in range(3)):
                            continue
                        value = Q(norm_a * (-1) ** (sum(le) + sum(re)))
                        for j, p in enumerate(primes):
                            value *= ((xs[j] ** le[j]) * (ys[j] ** re[j])
                                      * vs[j] ** (le[j] + re[j])
                                      / p ** (le[j] + re[j]))
                        direct += value
                bcoef = Q(1)
                for j, p in enumerate(primes):
                    if ae[j] == 0:
                        continue
                    X, Y = xs[j] * vs[j], ys[j] * vs[j]
                    delta = (1 - X / p) * (1 - Y / p)
                    bcoef *= (-(X + Y - X * Y / p) / delta
                              if ae[j] == 1 else X * Y / delta)
                require(direct == factor * bcoef,
                        "finite_masked_harmonic_euler")


def coeffs(y1, y2):
    out = {}
    for h1 in range(1, 2 * y1):
        c1 = mu(h1) * cutoff(Q(h1, y1))
        if not c1:
            continue
        for h2 in range(1, 2 * y2):
            value = c1 * mu(h2) * cutoff(Q(h2, y2))
            if value:
                out[h1 * h2] = out.get(h1 * h2, Q(0)) + value
    return {n: a for n, a in out.items() if a}


def primitive(n):
    residue = n % 5
    return 0 if residue == 0 else (1 if residue in (1, 4) else -1)


def natural(n, puncture):
    return primitive(n) if gcd(n, puncture) == 1 else 0


def phi(x):
    if x <= Q(1, 3) or x >= 2:
        return Q(0)
    return x * (2 - x) * (3 * x - 1)


def finite_reflected_model(y1, y2, threshold, low, puncture):
    acoef = coeffs(y1, y2)
    Rmax = max(acoef)
    P = 5 * puncture
    names = ("full", "H", "G", "KG", "corner")
    direct = dict.fromkeys(names, Q(0))
    grouped = dict.fromkeys(names, Q(0))
    grouped_bad_mask = dict.fromkeys(names, Q(0))

    def factors(a, r):
        H = cutoff(Q(a, 2 * threshold))
        K = cutoff(Q(a, low))
        G = 1 - cutoff(Q(r, threshold))
        require((1 - H) * (1 - G) == 0, "termwise_support_cover")
        require(0 <= K <= H <= 1, "nested_ratio_selectors")
        values = {"full": Q(1), "H": H, "G": G,
                  "KG": K * G, "corner": (H - K) * G}
        require(values["full"] == values["H"] + values["G"]
                - values["KG"] - values["corner"],
                "termwise_exact_corner_identity")
        return values

    for r, ar in acoef.items():
        pr = natural(r, puncture)
        if not pr:
            continue
        for n in range(1, 2 * r):
            ch = primitive(n)
            if not ch:
                continue
            kernel = phi(Q(n, r))
            if not kernel:
                continue
            a = r // gcd(r, n)
            f = factors(a, r)
            v = ar * pr * ch * kernel / r
            for name in names:
                direct[name] += v * f[name]

    for a in range(1, Rmax + 1):
        pa = natural(a, puncture)
        if not pa:
            continue
        dual = sum((primitive(b) * phi(Q(b, a))
                    for b in range(1, 2 * a) if gcd(a, b) == 1), Q(0))
        if not dual:
            continue
        for d in range(1, Rmax // a + 1):
            r = a * d
            ar = acoef.get(r, Q(0))
            if not ar:
                continue
            f = factors(a, r)
            v = ar * pa * dual / (a * d)
            for name in names:
                grouped_bad_mask[name] += v * f[name]
                if gcd(d, P) == 1:
                    grouped[name] += v * f[name]

    for name in names:
        require(direct[name] == grouped[name], "exact_masked_gcd_grouping:" + name)
    require(direct["full"] == direct["H"] + direct["G"]
            - direct["KG"] - direct["corner"], "coherent_exact_corner_identity")

    C_all, C_far = {}, {}
    for a in range(1, Rmax + 1):
        if gcd(a, P) != 1:
            continue
        C_all[a] = sum((acoef.get(a * d, Q(0)) / d
                        for d in range(1, Rmax // a + 1)
                        if gcd(d, P) == 1), Q(0))
        C_far[a] = sum((acoef.get(a * d, Q(0)) / d
                        * (1 - cutoff(Q(a * d, threshold)))
                        for d in range(1, Rmax // a + 1)
                        if gcd(d, P) == 1), Q(0))
    for m in C_all:
        D_full = D_far = D_H = D_KG = D_corner = Q(0)
        for k in range(1, Rmax // m + 1):
            if gcd(k, P) != 1:
                continue
            a = k * m
            H = cutoff(Q(a, 2 * threshold))
            K = cutoff(Q(a, low))
            weight = Q(mu(k), k)
            D_full += weight * C_all[a]
            D_far += weight * C_far[a]
            D_H += weight * C_all[a] * H
            D_KG += weight * C_far[a] * K
            D_corner += weight * C_far[a] * (H - K)
        am = acoef.get(m, Q(0))
        require(D_full == am, "full_divisibility_return")
        require(D_far == am * (1 - cutoff(Q(m, threshold))),
                "far_divisibility_return")
        require(D_corner == D_H - D_KG - am * cutoff(Q(m, threshold)),
                "exact_corner_coefficient_return")
    return direct, grouped_bad_mask


def exponent_certificate():
    lo, hi = Q(29, 25), Q(117, 100)
    require(Q(2, 3) <= lo <= hi <= Q(200, 147), "radical_branch_interval")
    require(hi < Q(3, 2), "increasing_gap_interval")
    require(Q(58, 3) < Q(9, 2) ** 2, "envelope_floor_lower_bound")
    require(Q(167, 30) - Q(9, 2) == Q(16, 15), "envelope_floor_identity")
    require(Q(16, 15) > 1 + hi / 50, "printed_floor_dominated")
    require(Q(211, 48) + Q(1, 1000) == Q(26381, 6000), "gap_radical_threshold")
    require(Q(58, 3) - Q(26381, 6000) ** 2 == Q(42839, 36000000),
            "positive_exact_squared_margin")
    require(Q(42839, 36000000) > 0, "strict_consumer_margin")
    require((1 - Q(17, 20)) / 4 == Q(3, 80), "overlap_cutoff_gain")
    require((lo - 1) / 4 == Q(1, 25) > Q(3, 80), "head_stronger_than_overlap")
    require((lo - 1) * Q(3, 25) == Q(12, 625) > Q(1, 60),
            "full_head_coefficient_error")
    require((1 - Q(17, 20)) * Q(3, 25) == Q(9, 500) > Q(1, 60),
            "overlap_coefficient_error")
    # A tempting stronger .002 saving fails already at the lower endpoint.
    require(Q(58, 3) < (Q(211, 48) + Q(1, 500)) ** 2,
            "negative_control_excess_saving")
    # Numerically displayed values are isolated rationally, not assumed.
    low_sqrt = Q(isqrt(58 * 10**36 // 3), 10**18)
    require(low_sqrt**2 <= Q(58, 3) < (low_sqrt + Q(1, 10**18))**2,
            "rational_radical_isolation")
    return {
        "minimum_overlap_gain_interval": [str(low_sqrt - Q(211, 48)),
                                           str(low_sqrt + Q(1, 10**18) - Q(211, 48))],
        "exact_squared_margin_over_1_over_1000": "42839/36000000",
    }


def main():
    symbolic_local_shift()
    finite_harmonic_euler()
    overlap_mutations = 0
    mask_mutations = 0
    examples = []
    for args in ((2, 5, 3, 1, 3), (3, 7, 5, 2, 3),
                 (3, 8, 6, 3, 2), (4, 9, 7, 3, 3)):
        exact, bad_mask = finite_reflected_model(*args)
        overlap_mutations += exact["KG"] != 0
        mask_mutations += any(exact[k] != bad_mask[k] for k in exact)
        examples.append({"parameters": list(args),
                         "overlap_nonzero": exact["KG"] != 0,
                         "corner_nonzero": exact["corner"] != 0})
    require(overlap_mutations > 0, "negative_control_deleted_overlap")
    require(mask_mutations > 0, "negative_control_deleted_gcd_mask")
    certificate = exponent_certificate()
    print(json.dumps({
        "status": "pass",
        "counts": COUNTS,
        "models": examples,
        "certificate": certificate,
        "limits": "Finite algebra and exact scalar comparisons only; analytic premises and the remaining corner are not proved by this checker.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
