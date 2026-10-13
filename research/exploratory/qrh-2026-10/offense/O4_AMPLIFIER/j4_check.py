"""
j4_check.py -- finite checks for README section 7 (the j = 4 amplifier).  Floating point and exact
integer arithmetic in Z[omega], finite; imports ../../a2/eis.py unchanged (read, not modified).

J1 (twist exponent of the e = 1 amplifier):  gamma_2(l n) / (gamma_2(l) gamma_2(n)) == chi_n(l)^4,
    i.e. the Oct 5 eq:crt-a factor that the plain prime amplifier chi_l(u) puts on the dual n-sum.
    Since chi_n(l)^4 = chi_n(l)^{j} with j = 4, this is the j = 4 case of the R3 law.
    Also records gamma_{-1}(l n)/(gamma_{-1}(l) gamma_{-1}(n)) against chi_n(l)^a, a = 0..5.
J2 (finite-field local factor):  sum_{v mod p, p | v excluded} chi_p(v)^{j+2} e(x v / p)
    equals -1 + N(p) 1_{p | x} for j = 4 (Ramanujan sum, no character) and has modulus sqrt(N p)
    times |chi_p(x)| for j != 4 (a character of x survives); all x mod p, split and inert p.
J3 (the surviving row phase):  for fixed amplifier prime l, the post-reflection phase of the
    reindexed term is chi_l(k) * chi_k(l)^3 (outer Poisson/CRT phase times reindexing phase).
    Checks that its cube is a ray-class sign and that it is NOT constant in k: it takes >= 3
    values, i.e. a cubic character of the row k mod l survives.
Usage: python3 -I j4_check.py OUT.json
"""
import cmath
import itertools
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..", "a2")))
import eis  # noqa: E402
from eis import ZETA, gamma, mul, norm, primes_upto, residues, sym_prime, e_of, divides  # noqa: E402


def chi_val(u, p):
    k = sym_prime(u, p)
    return 0 if k is None else ZETA[k]


def main(out):
    res = {}
    P = [p for p in primes_upto(200)]
    split = [p for p in P if norm(p) % 3 == 1 and norm(p) < 120]
    # J1
    pairs = [(a, b) for a, b in itertools.combinations(P[:14], 2) if norm(a) * norm(b) <= 2600]
    maxdev4, maxdev_other, cnt = 0.0, [], 0
    expo_m1 = {}
    for l, n in pairs:
        g2 = gamma(2, [l, n]) / (gamma(2, [l]) * gamma(2, [n]))
        c = chi_val(l, n)                      # chi_n(l)
        maxdev4 = max(maxdev4, abs(g2 - c ** 4))
        # gamma_{-1}: find exponent a with ratio == chi_n(l)^a (up to sign/ray-class unit)
        gm = gamma(-1, [l, n]) / (gamma(-1, [l]) * gamma(-1, [n]))
        best = min(range(6), key=lambda a: abs(gm - c ** a))
        expo_m1[best] = expo_m1.get(best, 0) + 1
        cnt += 1
    res["J1"] = dict(pairs=cnt, max_dev_gamma2_vs_chi4=maxdev4, gamma_m1_best_exponent_counts=expo_m1)
    print(f"J1: {cnt} pairs, max |gamma2(ln)/(gamma2 gamma2) - chi_n(l)^4| = {maxdev4:.2e}; "
          f"gamma_-1 ratio best exponent counts {expo_m1}")
    # J2
    rows = []
    for p in P[:10]:
        R, N = residues(p)
        for j in range(6):
            m = (j + 2) % 6
            worst = 0.0
            for x in R:
                s = 0
                for v in R:
                    k = sym_prime(v, p)
                    if k is None:
                        continue
                    s += ZETA[(m * k) % 6] * e_of(mul(x, v), p)
                if j == 4:
                    target = -1 + (N if divides(p, x) else 0)
                    worst = max(worst, abs(s - target))
                else:
                    kx = sym_prime(x, p)
                    target_abs = math.sqrt(N) if kx is not None else 0.0
                    worst = max(worst, abs(abs(s) - target_abs))
            rows.append(dict(p=list(p), N=N, j=j, worst=worst))
    wj4 = max(r["worst"] for r in rows if r["j"] == 4)
    wother = max(r["worst"] for r in rows if r["j"] != 4)
    res["J2"] = dict(primes=len(P[:10]), worst_j4=wj4, worst_other=wother)
    print(f"J2: {len(P[:10])} primes (split and inert), j=4 Ramanujan identity max dev {wj4:.2e}; "
          f"j!=4 |sum| = sqrt(N)|chi(x)| max dev {wother:.2e}")
    # J3
    J3 = []
    for l in split[:8]:
        vals, cubes = set(), set()
        for k in P[:60]:
            if k == l:
                continue
            a = sym_prime(k, l)        # chi_l(k) = (k/l)_6
            b = sym_prime(l, k)        # chi_k(l) = (l/k)_6
            if a is None or b is None:
                continue
            ph = (a + 3 * b) % 6
            vals.add(ph)
            cubes.add((3 * ph) % 6)
        # J3b: phase / chi_l(k)^4 = (chi_k(l)/chi_l(k))^3 is a sign; test that it depends only on k mod 4
        cls, consistent = {}, True
        for k in P[:60]:
            if k == l:
                continue
            a = sym_prime(k, l); b = sym_prime(l, k)
            if a is None or b is None:
                continue
            sign = (3 * (b - a)) % 6
            key = eis.reduce_mod(k, (4, 0))
            if key in cls and cls[key] != sign:
                consistent = False
            cls[key] = sign
        J3.append(dict(l=list(l), N=norm(l), phase_values=sorted(vals), cube_values=sorted(cubes),
                       sign_is_function_of_k_mod_4=consistent, n_classes=len(cls)))
        print(f"J3b: l={l}: phase = chi_l(k)^4 * sign, sign a function of k mod 4: {consistent} ({len(cls)} classes)")
        print(f"J3: l={l} N={norm(l)}: phase chi_l(k)chi_k(l)^3 takes exponents {sorted(vals)} "
              f"(cube exponents {sorted(cubes)})")
    res["J3"] = J3
    with open(out, "w") as fh:
        json.dump(dict(note="finite checks, floating point and exact symbols; see j4_check.py", **res), fh, indent=1)


if __name__ == "__main__":
    main(sys.argv[1])
