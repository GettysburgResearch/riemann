"""
check_identities.py -- EMPIRICAL check of Lemma lem:arithmetic in
"The Quasi-Riemann Hypothesis" (OpenAI, Oct 2026), for all squarefree
primary n prime to 6 with N(n) <= BOUND.

Usage:  python3 -I check_identities.py [BOUND] [PAIR_BOUND] [OUT_JSON]

Every Gauss sum is computed directly from its definition,
    gamma_j(n) = N(n)^{-1/2} sum_{x mod n} chi_n(x)^j e(x/n),
over an explicit complete residue system mod n, with chi_n the product of
the sextic symbols of the prime factors (no CRT shortcut is used).
Conventions are those of eisenstein.py.  Checked:

 (a) gamma_2(n)^3            = mu(n) alpha(n)
 (b) gamma_1(n) gamma_2(n)   = mu(n) alpha(n) G(n),  G(n) = conj(chi_n(4)) gamma_3(n)
 (c) gamma_1(n) gamma_{-1}(n) = chi_n(-1)
 (d) mu(n) gamma_{-1}(n)     = chi_n(-1) G(n)^{-1} conj(alpha(n)) gamma_2(n)
 (e) chi_b(a) = R(a,b) chi_a(b) with R = +-1 for coprime squarefree primary
     a, b; R depends only on (a mod 4, b mod 4) and equals the paper's
     bicharacter (-1)^{eh+fg+fh} on square classes (-1)^e lambda^f;
     G(ab) = G(a) G(b) R(a,b);  a(ab) = a(a) a(b) chi_b(a)^4 (eq:crt-a,
     xi = 1);  G(n) depends only on n mod m (smallest m searched);
     closed forms gamma_3(c) = (1 + i^{-b} + i^a + i^{b-a})/2 (c = a + b w)
     and chi_c(4) = (c mod 2) in {1, w, w^2}.
"""

import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402

import eisenstein as E  # noqa: E402


def codes_of(primes, facs, x, y):
    s = np.zeros(np.shape(x), dtype=np.uint8)
    for i in facs:
        s += primes[i].codes(x, y)
    return s


def chi_value(primes, facs, u):
    x = np.array([u[0]], dtype=np.int64)
    y = np.array([u[1]], dtype=np.int64)
    return E.VALUE[codes_of(primes, facs, x, y)[0]]


def gauss_sums(primes, gen, N, facs, js=(1, 2, 3, -1)):
    """gamma_j(n) for the listed j, by direct summation over x mod n."""
    a, b = gen
    g = math.gcd(a, b)
    # complete residue system: c + d*omega, 0 <= c < N/g, 0 <= d < g
    c = np.tile(np.arange(N // g, dtype=np.int64), g)
    d = np.repeat(np.arange(g, dtype=np.int64), N // g)
    s = codes_of(primes, facs, c, d)
    ok = s < E.ZERO
    k = (s % 6).astype(np.int64)
    # e(x/n) = e(x * conj(n) / N); omega-coordinate of x*conj(n)
    nb = E.conj(gen)
    dprime = c * nb[1] + d * nb[0] - d * nb[1]
    phase = np.exp(2j * np.pi * np.mod(dprime, N) / N)
    out = {}
    for j in js:
        out[j] = np.sum(np.where(ok, E.ZETA[(j * k) % 6], 0) * phase) / math.sqrt(N)
    return out


def gamma_quad_closed(c):
    a, b = c
    i = 1j
    return (1 + i ** (-b % 4) + i ** (a % 4) + i ** ((b - a) % 4)) / 2


def mod2_cube_root_code(c):
    """Code of the cube root of unity congruent to c mod 2 (1, w, w^2)."""
    a, b = c[0] % 2, c[1] % 2
    return {(1, 0): 0, (0, 1): 2, (1, 1): 4}[(a, b)]


def square_class(c):
    """(e, f) with c = (-1)^e lambda^f * square in (O/4)^x."""
    t = (c[0] % 4, c[1] % 4)
    t3 = E.mul(E.mul(t, t), t)
    t3 = (t3[0] % 4, t3[1] % 4)
    return {(1, 0): (0, 0), (3, 0): (1, 0), (1, 2): (0, 1), (3, 2): (1, 1)}[t3]


def bichar(c1, c2):
    e, f = square_class(c1)
    g, h = square_class(c2)
    return (-1) ** (e * h + f * g + f * h)


def main():
    bound = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    pair_bound = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
    out_json = sys.argv[3] if len(sys.argv) > 3 else "identities.json"
    t0 = time.time()
    primes = E.prime_ideals(bound)
    n_selftest = E.self_test(primes)
    ns = E.squarefree_primary(primes, bound)
    print(f"bound={bound}: {len(primes)} prime ideals, {len(ns)} squarefree n; "
          f"table self-test {n_selftest} exact checks passed ({time.time()-t0:.1f}s)")

    rec = {}
    err = {k: 0.0 for k in ["a", "b", "c", "d", "absG", "gamma3_closed", "chi4_mod2"]}
    worst = {}
    n_split = n_inert_involved = n_composite = 0
    for gen, N, facs in ns:
        gs = gauss_sums(primes, gen, N, facs)
        mu = (-1) ** len(facs)
        alpha = E.to_complex(gen) / math.sqrt(N)
        chi4 = chi_value(primes, facs, (4, 0))
        chim1 = chi_value(primes, facs, (-1, 0))
        G = np.conj(chi4) * gs[3]
        vals = {
            "a": abs(gs[2] ** 3 - mu * alpha),
            "b": abs(gs[1] * gs[2] - mu * alpha * G),
            "c": abs(gs[1] * gs[-1] - chim1),
            "d": abs(mu * gs[-1] - chim1 / G * np.conj(alpha) * gs[2]),
            "absG": abs(abs(G) - 1),
            "gamma3_closed": abs(gs[3] - gamma_quad_closed(gen)),
            "chi4_mod2": abs(chi4 - E.ZETA[mod2_cube_root_code(gen)]),
        }
        for k, v in vals.items():
            if v > err[k]:
                err[k] = v
                worst[k] = (gen, N)
        rec[gen] = dict(N=N, facs=facs, mu=mu, alpha=alpha, g1=gs[1], g2=gs[2],
                        g3=gs[3], gm1=gs[-1], chi4=chi4, chim1=chim1, G=G)
        n_composite += len(facs) > 1
        n_split += all(primes[i].kind == "split" for i in facs)
        n_inert_involved += any(primes[i].kind == "inert" for i in facs)
    t1 = time.time()
    print(f"Gauss sums for {len(ns)} n done ({t1-t0:.1f}s); "
          f"{n_composite} composite, {n_inert_involved} involve an inert prime")
    for k in err:
        print(f"  max error {k:14s}: {err[k]:.3e}   (worst n = {worst.get(k)})")

    # ---- (e) reciprocity on coprime pairs -------------------------------
    small = [(g, N, f) for g, N, f in ns if N <= pair_bound]
    R_err = 0.0
    R_classes = {}
    R_formula_mismatch = 0
    R_gammaquad_err = 0.0
    G_mult_err = 0.0
    crt_err = 0.0
    n_pairs = n_mult = 0
    for ga, Na, fa in small:
        for gb, Nb, fb in small:
            if set(fa) & set(fb):
                continue
            n_pairs += 1
            x_ba = chi_value(primes, fb, ga)            # chi_b(a)
            x_ab = chi_value(primes, fa, gb)            # chi_a(b)
            R = x_ba / x_ab
            Rr = round(R.real)
            R_err = max(R_err, abs(R - Rr))
            key = ((ga[0] % 4, ga[1] % 4), (gb[0] % 4, gb[1] % 4))
            R_classes.setdefault(key, set()).add(Rr)
            if Rr != bichar(ga, gb):
                R_formula_mismatch += 1
            gq = gamma_quad_closed(E.mul(ga, gb)) / (
                gamma_quad_closed(ga) * gamma_quad_closed(gb))
            R_gammaquad_err = max(R_gammaquad_err, abs(gq - Rr))
            gab = E.mul(ga, gb)
            if gab in rec:
                n_mult += 1
                ra, rb, rab = rec[ga], rec[gb], rec[gab]
                G_mult_err = max(G_mult_err, abs(rab["G"] - ra["G"] * rb["G"] * Rr))
                aa = np.conj(ra["alpha"]) * ra["g2"]
                ab = np.conj(rb["alpha"]) * rb["g2"]
                aab = np.conj(rab["alpha"]) * rab["g2"]
                crt_err = max(crt_err, abs(aab - aa * ab * x_ba ** 4))
    R_inconsistent = sum(len(v) > 1 for v in R_classes.values())
    print(f"(e) {n_pairs} coprime ordered pairs with N <= {pair_bound}: "
          f"max |R - round(R)| = {R_err:.2e}; R values {sorted(set().union(*R_classes.values()))}; "
          f"(a mod 4, b mod 4) classes: {len(R_classes)}, inconsistent: {R_inconsistent}; "
          f"mismatches with (-1)^(eh+fg+fh): {R_formula_mismatch}; "
          f"max |R - Gq(ab)/(Gq(a)Gq(b))| = {R_gammaquad_err:.2e}")
    print(f"    G(ab)=G(a)G(b)R(a,b): {n_mult} pairs with N(ab)<={bound}, max err {G_mult_err:.2e};"
          f" eq:crt-a max err {crt_err:.2e}")

    # ---- dependence of G (and pieces) on n mod m ------------------------
    moddep = {}
    for m in [2, 3, 4, 6, 8, 12, 24, 36, 72]:
        res = {}
        for name in ["G", "g3", "chi4", "chim1"]:
            groups = {}
            for gen, r in rec.items():
                groups.setdefault((gen[0] % m, gen[1] % m), []).append(r[name])
            spread = max(max(abs(v - vs[0]) for v in vs) for vs in groups.values())
            res[name] = (len(groups), spread)
        moddep[m] = res
        print(f"  mod {m:2d}: " + "; ".join(
            f"{k}: {c} classes, max spread {s:.2e}" for k, (c, s) in res.items()))
    const_moduli = [m for m in moddep if moddep[m]["G"][1] < 1e-8]
    # table of G on classes mod 4
    Gtab = {}
    for gen, r in rec.items():
        key = (gen[0] % 4, gen[1] % 4)
        Gtab.setdefault(key, (complex(r["G"]), complex(r["chim1"]),
                              square_class(gen)))
    print("  G on classes n mod 4 (a mod 4, b mod 4) -> G, chi_n(-1), square class (e,f):")
    for key in sorted(Gtab):
        G, cm1, sc = Gtab[key]
        print(f"    {key}: G = {G.real:+.4f}{G.imag:+.4f}i   chi(-1) = {cm1.real:+.0f}"
              f"   class {sc}   R(c,c)={bichar(key, key):+d}")
    chim1_vs_Rcc = max(abs(r["chim1"] - bichar(g, g)) for g, r in rec.items())
    print(f"  max |chi_n(-1) - R(n,n)| = {chim1_vs_Rcc:.2e}")
    # class-level identities on (O/4)^x: G(ab) = G(a)G(b)R(a,b) for ALL class
    # pairs, and eq:quotient's G(a^{-1}) = chi_a(-1) conj(G(a)).
    cls = sorted(Gtab)
    red = lambda z: (z[0] % 4, z[1] % 4)  # noqa: E731
    cls_mult_err = max(abs(Gtab[red(E.mul(c1, c2))][0] - Gtab[c1][0] * Gtab[c2][0] * bichar(c1, c2))
                       for c1 in cls for c2 in cls)
    inv = {c1: next(c2 for c2 in cls if red(E.mul(c1, c2)) == (1, 0)) for c1 in cls}
    cls_inv_err = max(abs(Gtab[inv[c]][0] - Gtab[c][1] * np.conj(Gtab[c][0])) for c in cls)
    print(f"  class level: max |G(ab)-G(a)G(b)R(a,b)| over all 144 class pairs = {cls_mult_err:.2e};"
          f" max |G(a^-1) - chi_a(-1) conj G(a)| = {cls_inv_err:.2e}")

    summary = dict(
        bound=bound, n_tested=len(ns), n_composite=n_composite,
        n_with_inert_factor=n_inert_involved, table_selftest_checks=n_selftest,
        max_errors={k: float(v) for k, v in err.items()},
        worst_n={k: list(map(list, [v[0]])) + [v[1]] for k, v in worst.items()},
        reciprocity=dict(pair_bound=pair_bound, n_pairs=n_pairs, max_R_err=R_err,
                         n_class_pairs=len(R_classes), inconsistent_class_pairs=R_inconsistent,
                         mismatches_with_bicharacter_formula=R_formula_mismatch,
                         max_err_R_vs_gamma_quad_ratio=R_gammaquad_err,
                         G_multiplicativity_pairs=n_mult, G_multiplicativity_max_err=G_mult_err,
                         crt_a_max_err=crt_err),
        G_mod_dependence={str(m): {k: [c, float(s)] for k, (c, s) in v.items()}
                          for m, v in moddep.items()},
        moduli_where_G_constant=const_moduli,
        G_table_mod4={f"{k}": [Gtab[k][0].real, Gtab[k][0].imag, Gtab[k][1].real]
                      for k in sorted(Gtab)},
        max_err_chi_minus1_vs_R_nn=float(chim1_vs_Rcc),
        class_level_G_mult_err=float(cls_mult_err),
        class_level_G_inverse_err=float(cls_inv_err),
        seconds=time.time() - t0,
    )
    with open(out_json, "w") as fh:
        json.dump(summary, fh, indent=1)
    print(f"wrote {out_json} ({time.time()-t0:.1f}s total)")


if __name__ == "__main__":
    main()
