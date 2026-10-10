"""
check_kintali_phase.py -- finite checks of the "finite phase correction" eq. (1) of the
Kintali QRH manuscript (and its Appendix A.1 statements), read from the rendered PDF:

    Gamma_q(c) = (1 + i^{-b} + i^a + i^{b-a})/2   for odd c = a + b w,
    G(c) = conj(chi_c(4)) Gamma_q(c)               (primary c prime to 6),
    R(v, w) = Gamma_q(vw) / (Gamma_q(v) Gamma_q(w))  (all odd v, w).
  Claims: |G| = 1; R is a symmetric sign-valued bicharacter; on primary arguments G, R
  descend to the ray class group T mod 36 O; Gamma_q(c) = |c|^{-1} sum_{x mod c} e(x^2/c)
  for EVERY odd nonzero c (incl. nonsquarefree); (A.1) G(vw) = G(v)G(w)R(v,w),
  G(p^3) = gamma_3(p), R(p,p) = gamma_3(p)^2 = chi_p(-1); (A.2) chi_v(w) = R(v,w) chi_w(v)
  for coprime primary v, w prime to S (incl. nonsquarefree).

Labels per part:
  K1 FLOATING_RECONNAISSANCE  Gauss-sum evaluation of Gamma_q for all odd c, N(c) <= X1
  K2 EXACT                    exhaustive residue-class algebra mod 36 (and mod 4)
  K3 EXACT                    G(p^3) = Gamma_q(p), G(v^2) = chi_v(4), R(p,p) = chi_p(-1) via symbols
  K4 EXACT                    (A.2) for all coprime primary pairs, incl. nonsquarefree, N <= X4
Coverage NOT repeated here (see w5copg numerics/RESULTS.md): gamma_3(n) = Gamma_q(n) and
(a)-(e) of the Gauss identities for squarefree primary n with N(n) <= 50000.

Run:  python3 -I check_kintali_phase.py results/kintali_phase.json
"""

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import eisenstein as E  # noqa: E402

I_POW = [1, 1j, -1, -1j]


def two_gamma(a, b):
    """2 * Gamma_q(a + b w), exact Gaussian integer (as a Python complex with int parts)."""
    return 1 + I_POW[(-b) % 4] + I_POW[a % 4] + I_POW[(b - a) % 4]


def is_odd(a, b):
    return not (a % 2 == 0 and b % 2 == 0)


def cube_root_mod2(a, b):
    """The cube root of unity congruent to c mod 2 (c odd), as a zeta-code (0, 2 or 4)."""
    # O/2 = F_4: units 1 = (1,0), w = (0,1), w^2 = -1-w = (1,1) mod 2
    r = (a % 2, b % 2)
    return {(1, 0): 0, (0, 1): 2, (1, 1): 4}[r]


ZETA = np.exp(1j * np.pi * np.arange(6) / 3)


def G_exact(a, b):
    """G(c) = conj(chi_c(4)) Gamma_q(c), using chi_c(4) = cube root of unity = c mod 2."""
    k = cube_root_mod2(a, b)
    return ZETA[(-k) % 6] * two_gamma(a, b) / 2


# ---------------------------------------------------------------------------
def part_K1(X1, out):
    print(f"== K1: Gamma_q(c) vs |c|^-1 sum_x e(x^2/c), all odd c with N(c) <= {X1} ==", flush=True)
    worst = 0.0
    n = n_nonprimary = n_lambda = n_nonsqfree = 0
    bmax = int(2 * math.sqrt(X1 / 3)) + 2
    for b in range(-bmax, bmax + 1):
        disc = X1 - 0.75 * b * b
        if disc < 0:
            continue
        for a in range(int(math.floor(b / 2 - math.sqrt(disc))) - 1,
                       int(math.ceil(b / 2 + math.sqrt(disc))) + 2):
            N = a * a - a * b + b * b
            if N == 0 or N > X1 or not is_odd(a, b):
                continue
            g = math.gcd(a, b)
            xs = np.arange(N // g, dtype=np.int64)
            ys = np.arange(g, dtype=np.int64)
            X, Y = np.meshgrid(xs, ys, indexing="ij")
            X = X.ravel()
            Y = Y.ravel()
            # x^2 for x = X + Y w:  (X^2 - Y^2, 2XY - Y^2)
            sa = X * X - Y * Y
            sb = 2 * X * Y - Y * Y
            ca, cb = a - b, -b                        # conj(c)
            coord = (sa * cb + sb * ca - sb * cb) % N  # omega-coordinate of x^2 conj(c)
            val = np.exp(2j * np.pi * coord / N).sum() / math.sqrt(N)
            worst = max(worst, abs(val - two_gamma(a, b) / 2))
            n += 1
            n_nonprimary += not (a % 3 == 1 and b % 3 == 0)
            n_lambda += (a + b) % 3 == 0          # lambda | c  <=>  a + b = 0 mod 3
            # crude nonsquarefree flag: divisible by a rational square or by lambda^2 = -3
            n_nonsqfree += (a % 3 == 0 and b % 3 == 0)
    out["K1"] = dict(label="FLOATING_RECONNAISSANCE", X=X1, odd_elements=n,
                     non_primary=n_nonprimary, divisible_by_lambda=n_lambda,
                     divisible_by_3=n_nonsqfree, max_abs_dev=worst)
    print(f"  {n} odd c ({n_nonprimary} non-primary, {n_lambda} divisible by lambda, "
          f"{n_nonsqfree} divisible by 3): max |dev| = {worst:.2e}")


def part_K2(out):
    print("== K2: exhaustive class algebra (EXACT) ==", flush=True)
    res = {}
    # all odd residues mod 36 and the primary ones prime to 6
    odd36 = [(a, b) for a in range(36) for b in range(36) if is_odd(a, b)]
    prim36 = [(a, b) for (a, b) in odd36 if a % 3 == 1 and b % 3 == 0]
    res["odd_classes_mod36"] = len(odd36)
    res["primary_classes_mod36_prime_to_6"] = len(prim36)
    # Gamma_q is a function mod 4 (periodicity of i^k) -- check by lifting each class
    bad_period = 0
    for (a, b) in odd36:
        base = two_gamma(a, b)
        for s, t in [(36, 0), (0, 36), (4, 0), (0, 4), (-36, 72)]:
            bad_period += two_gamma(a + s, b + t) != base
    res["Gamma_q_not_periodic"] = bad_period
    # |Gamma_q| = 1 on all odd classes
    res["max_abs_absGamma_minus_1"] = max(abs(abs(two_gamma(a, b)) - 2) for a, b in odd36) / 2

    def mul36(x, y, m=36):
        p = E.mul(x, y)
        return (p[0] % m, p[1] % m)

    def R(v, w):
        vw = E.mul(v, w)
        # |Gamma| = 1 exactly, so 1/Gamma = conj(Gamma); exact in dyadic rationals
        return (two_gamma(*vw) * two_gamma(*v).conjugate() * two_gamma(*w).conjugate()) / 8

    # R on all odd classes mod 4 (12 classes; Gamma_q depends only on c mod 4)
    odd4 = [(a, b) for a in range(4) for b in range(4) if is_odd(a, b)]
    vals = {}
    nonsign = asym = nonbichar = 0
    for v in odd4:
        for w in odd4:
            r = R(v, w)
            vals[(v, w)] = r
            nonsign += r not in (1, -1)
            asym += r != R(w, v)
    for v1 in odd4:
        for v2 in odd4:
            for w in odd4:
                v12 = E.mul(v1, v2)
                nonbichar += R(v12, w) != R(v1, w) * R(v2, w)
    res["mod4"] = dict(classes=len(odd4), R_not_sign=nonsign, R_asymmetric=asym,
                       bicharacter_failures=nonbichar, triples=len(odd4) ** 3)

    # square-class formula of OpenAI (4.4): r((-1)^e lam^f, (-1)^g lam^h) = (-1)^{eh+fg+fh}
    lam = (1, 2)
    reps = {}
    for e in (0, 1):
        for f in (0, 1):
            x = E.power(lam, f)
            if e:
                x = (-x[0], -x[1])
            reps[(e, f)] = x
    table_fail = 0
    for (e, f), x in reps.items():
        for (g, h), y in reps.items():
            table_fail += R(x, y) != (-1) ** (e * h + f * g + f * h)
    res["square_class_table_failures"] = table_fail
    res["Gamma_on_reps"] = {str(k): str(two_gamma(*v) / 2) for k, v in reps.items()}

    # primary classes mod 36: |G| = 1, G(vw) = G(v)G(w)R(v,w), R well defined mod 36, bichar
    Gv = {c: G_exact(*c) for c in prim36}
    res["max_abs_absG_minus_1"] = max(abs(abs(g) - 1) for g in Gv.values())
    idx = {c: i for i, c in enumerate(prim36)}
    n36 = len(prim36)
    Rm = np.zeros((n36, n36))
    prod_idx = np.zeros((n36, n36), dtype=np.int64)
    g_fail = 0.0
    r_lift_fail = 0
    for i, v in enumerate(prim36):
        for j, w in enumerate(prim36):
            vw = mul36(v, w)
            prod_idx[i, j] = idx[vw]
            r = R(v, w)
            Rm[i, j] = r.real
            assert r.imag == 0
            # R computed from other lifts of the same classes mod 36
            r2 = R((v[0] + 36, v[1] - 72), (w[0] - 36, w[1] + 108))
            r_lift_fail += r2 != r
            g_fail = max(g_fail, abs(Gv[vw] - Gv[v] * Gv[w] * r))
    bichar36 = 0
    for i in range(n36):
        # R(v_i v_k, w_j) = R(v_i, w_j) R(v_k, w_j) for all i, k, j
        lhs = Rm[prod_idx[i, :], :]                    # rows: k, cols: j
        rhs = Rm[i, :][None, :] * Rm
        bichar36 += int(np.sum(lhs != rhs))
    res["mod36_primary"] = dict(classes=n36, R_not_sign=int(np.sum(np.abs(Rm) != 1)),
                                R_asymmetric=int(np.sum(Rm != Rm.T)),
                                R_lift_dependence=r_lift_fail,
                                bicharacter_failures=bichar36, triples=n36 ** 3,
                                max_abs_G_multiplicativity_dev=g_fail)
    # G constant on classes mod 4 (ray classes mod 12) and NOT mod 2
    by4, by2 = {}, {}
    for c, g in Gv.items():
        by4.setdefault((c[0] % 4, c[1] % 4), set()).add(complex(round(g.real, 12), round(g.imag, 12)))
        by2.setdefault((c[0] % 2, c[1] % 2), set()).add(complex(round(g.real, 12), round(g.imag, 12)))
    res["G_values_per_class_mod4_max"] = max(len(s) for s in by4.values())
    res["G_values_per_class_mod2_max"] = max(len(s) for s in by2.values())
    out["K2"] = dict(label="EXACT", **res)
    for k, v in res.items():
        if k != "Gamma_on_reps":
            print(f"  {k}: {v}")
    print(f"  Gamma_q on 1, lam, -1, -lam: {res['Gamma_on_reps']}")


def ideals_upto(primes, X):
    """All ideals prime to 6 with norm <= X: (primary generator, norm, {prime index: exp})."""
    out = [((1, 0), 1, {})]

    def rec(start, gen, n, fac):
        for i in range(start, len(primes)):
            P = primes[i]
            if n * P.N > X:
                break
            g, m, e = gen, n, 0
            while m * P.N <= X:
                g, m, e = E.mul(g, P.gen), m * P.N, e + 1
                f2 = dict(fac)
                f2[i] = e
                out.append((g, m, f2))
                rec(i + 1, g, m, f2)

    rec(0, (1, 0), 1, {})
    return out


def chi_code(primes, fac, u):
    """code of chi_c(u) = prod chi_p(u)^e (ZERO if not coprime)."""
    tot = 0
    for i, e in fac.items():
        c = int(primes[i].codes(np.array([u[0]], dtype=np.int64), np.array([u[1]], dtype=np.int64))[0])
        if c == E.ZERO:
            return E.ZERO
        tot += e * c
    return tot % 6


def part_K3_K4(X3, X4, out):
    print(f"== K3/K4: symbols (EXACT): primes N<={X3}; coprime primary pairs N<={X4} ==", flush=True)
    primes = E.prime_ideals(max(X3, X4))
    # K3: G(p^3) = Gamma_q(p) (exact class arithmetic), R(p,p) = chi_p(-1), G(v^2) = chi_v(4)
    f_g3 = f_rpp = f_gv2 = f_chi4 = 0
    nP = 0
    for i, P in enumerate(primes):
        if P.N > X3:
            continue
        nP += 1
        p = P.gen
        p3 = E.power(p, 3)
        f_g3 += abs(G_exact(*p3) - two_gamma(*p) / 2) > 1e-12
        rpp = (two_gamma(*E.mul(p, p)) * two_gamma(*p).conjugate() ** 2) / 8
        cm1 = chi_code(primes, {i: 1}, (-1, 0))
        f_rpp += rpp != (1 if cm1 == 0 else -1) or cm1 not in (0, 3)
        c4 = chi_code(primes, {i: 1}, (4, 0))
        f_chi4 += c4 != cube_root_mod2(*p)
        # G(v^2) = chi_v(4)
        f_gv2 += abs(G_exact(*E.mul(p, p)) - ZETA[c4]) > 1e-12
    out["K3"] = dict(label="EXACT (symbols) + exact class arithmetic", primes=nP,
                     G_p3_ne_Gamma_p=f_g3, R_pp_ne_chi_p_minus1=f_rpp,
                     chi_p4_ne_cube_root_mod2=f_chi4, G_p2_ne_chi_p4=f_gv2)
    print(f"  K3 over {nP} primes: G(p^3)!=Gamma_q(p): {f_g3}; R(p,p)!=chi_p(-1): {f_rpp}; "
          f"chi_p(4)!=(p mod 2): {f_chi4}; G(p^2)!=chi_p(4): {f_gv2}")
    # K4: (A.2) for coprime primary v, w (all ideals, incl. prime powers), N <= X4
    ids = [x for x in ideals_upto(primes, X4) if x[1] > 1]
    nonsq = sum(any(e > 1 for e in f.values()) for _, _, f in ids)
    # cache chi_p(u) codes: for each ideal, codes of chi_v(w) for all w
    fails = pairs = 0
    fails_n1 = 0
    for (v, Nv, fv) in ids:
        for (w, Nw, fw) in ids:
            if set(fv) & set(fw):
                continue
            pairs += 1
            cvw = chi_code(primes, fv, w)
            cwv = chi_code(primes, fw, v)
            r = (two_gamma(*E.mul(v, w)) * two_gamma(*v).conjugate() * two_gamma(*w).conjugate()) / 8
            ok = (cvw - cwv) % 6 == (0 if r == 1 else 3) and r in (1, -1)
            fails += not ok
        # chi_n(-1) = R(n, n)
        cm1 = chi_code(primes, fv, (-1, 0))
        rnn = (two_gamma(*E.mul(v, v)) * two_gamma(*v).conjugate() ** 2) / 8
        fails_n1 += rnn != (1 if cm1 == 0 else -1)
    out["K4"] = dict(label="EXACT", X=X4, ideals=len(ids), nonsquarefree_ideals=nonsq,
                     coprime_ordered_pairs=pairs, sextic_reciprocity_failures=fails,
                     chi_n_minus1_ne_R_nn=fails_n1)
    print(f"  K4: {len(ids)} primary ideals ({nonsq} nonsquarefree), {pairs} coprime ordered pairs: "
          f"(A.2) failures {fails}; chi_n(-1)!=R(n,n): {fails_n1}")


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "kintali_phase.json"
    X1 = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
    t0 = time.time()
    out = {"source": "Kintali QRH manuscript eq. (1) and Appendix A.1 (read from rendered PDF); "
                     "OpenAI QRH Lemma 4.3/4.4"}
    part_K1(X1, out)
    part_K2(out)
    part_K3_K4(20000, 2000, out)
    out["runtime_s"] = time.time() - t0
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(f"done in {out['runtime_s']:.1f} s -> {out_path}")


if __name__ == "__main__":
    main()
