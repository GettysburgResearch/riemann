"""O-108523 proof probe: branch-splitting slopes at torsion points.

At a torsion point a0, the class-crowded spectrum point z_c is a
mu_c-fold root of M_m(z; a0). Writing z = z_c + w, a = a0 + s, the
Weierstrass/Newton data of M_m(z_c + w; a0 + s) at (0,0) decides how
the mu_c branches separate:

  transversal case: the branches are analytic with distinct slopes
  lam_1..lam_mu (w ~ lam_i s), and these slopes are the roots of the
  ASSOCIATED POLYNOMIAL  A(lam) = sum_k  c_{k, mu-k} lam^k  where
  c_{i,j} = coeff of s^i w^j in the expansion — i.e. the weighted
  diagonal of the Newton square. Then each pair contributes
  ord (z^(i) - z^(j)) = 1 and disc gains exactly mu(mu-1) from this
  class — O-108523's interior term.

This script extracts A(lam) for the a = 0 tower (M = 4, z_c = 0) and
for the other interior classes at every torsion point available in
the committed spectra (m <= 13 via disc_slice data recomputed on the
fly at b = 1), then:
  P1  checks A has degree mu and NONZERO discriminant (distinct
      slopes) and reports the slope sets;
  P2  hunts for structure in the a = 0 tower's A (closed form).
Everything exact (sympy over Q(alpha) / cyclotomic fields).
rh_established = false.
"""
import json
import sys
import time

sys.path.insert(0, '.')
import sympy as sp

sys.set_int_max_str_digits(1_000_000)

a, z, lam = sp.symbols('a z lam')


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def spectrum_M(m):
    """M_m(z; a) at b = 1 symbolically (the committed pipeline,
    small m only)."""
    from m18_spectrum_only import defect_numerator_b1, spectrum_b1
    N = defect_numerator_b1(m)
    mus, nu = spectrum_b1(N, m)
    return sum(mus[j] * z ** j for j in range(nu + 1)), nu


def associated_poly(M, z0, a0, K, mufield=None):
    """A(lam) from the Newton square of M(z0 + w; a0 + s):
    A(lam) = sum_{k=0..mu} [s^k w^(mu-k)] M * lam^k  where mu is the
    w-multiplicity at s = 0. Exact over the field of z0, a0.
    Also certifies hypothesis (T.a): every monomial s^i w^j with
    i + j < mu has ZERO coefficient (the Newton polygon touches
    nothing below the diagonal), returned as below_diag_clear."""
    w, s = sp.symbols('w s')
    E = M.subs([(z, z0 + w), (a, a0 + s)])
    E = sp.expand(E)
    P = sp.Poly(E, w, s)
    # multiplicity mu: lowest w-degree with nonzero coeff at s = 0
    mu = None
    for j in range(K + 1):
        c = P.coeff_monomial(w ** j) if j else P.coeff_monomial(1)
        if c is not None and sp.simplify(c) != 0:
            mu = j
            break
    A = sp.Integer(0)
    for k in range(mu + 1):
        mono = (w ** (mu - k) * s ** k)
        c = P.coeff_monomial(mono)
        if c is None:
            c = sp.Integer(0)
        A += sp.simplify(c) * lam ** k
    below = True
    for (j, i), c in P.terms():          # terms are ((w_exp, s_exp), c)
        if j + i < mu and sp.simplify(c) != 0:
            below = False
    return sp.Poly(sp.expand(A), lam), mu, below


def certify_cell(M, a0, cls_mults, zs):
    """Hypotheses (S) + (C) for one (point, m) cell: gcd(M, M') at
    a = a0 has degree exactly sum(mu_c - 1) and each interior class
    point z_c roots it to order exactly mu_c - 1 — so the multiple
    roots of M(.; a0) are precisely the class points with their
    crowding multiplicities and the cofactor never crowds them."""
    Ma = sp.expand(M.subs(a, a0))
    g = sp.gcd(sp.Poly(Ma, z), sp.Poly(sp.diff(Ma, z), z))
    dg = sp.degree(g, z)
    want = sum(mu - 1 for mu in cls_mults)
    per = []
    ge = g.as_expr() if hasattr(g, 'as_expr') else g
    for zc, mu in zip(zs, cls_mults):
        h = sp.expand(ge)
        k = 0
        while True:
            q, r = sp.div(h, z - zc, z)
            if sp.simplify(r) != 0:
                break
            h = sp.expand(q)
            k += 1
        per.append(k == mu - 1)
    return bool(dg == want and all(per)), int(dg), int(want)


def main():
    out = {"tower_a0": [], "other_points": [], "rh_established": False}
    # ---- the a = 0 tower (alpha = i, M = 4; single interior pair
    # {1, 3}, z_c = 0; no boundary classes at odd m) ------------------
    say("a = 0 tower: associated polynomials + full certificates")
    for m in range(5, 14, 2):
        M, nu = spectrum_M(m)
        A, mu, below = associated_poly(M, sp.Integer(0),
                                       sp.Integer(0), nu)
        dA = sp.discriminant(A.as_expr(), lam)
        degA = sp.degree(A.as_expr(), lam)
        sc, dg, want = certify_cell(M, sp.Integer(0), [mu],
                                    [sp.Integer(0)])
        say(f"  m = {m}: mu = {mu}, A = {A.as_expr()}")
        say(f"    (T): deg A = {degA} (= mu: {degA == mu}), "
            f"disc(A) = {dA} {'NONZERO' if dA != 0 else 'ZERO!'}, "
            f"below-diagonal clear: {below}")
        say(f"    (S)+(C): gcd degree {dg} == {want}: {sc}")
        out["tower_a0"].append({
            "m": m, "mu": mu, "A": str(A.as_expr()),
            "deg_A_eq_mu": bool(degA == mu),
            "disc_nonzero": bool(dA != 0),
            "below_diagonal_clear": bool(below),
            "separation_and_no_accident": bool(sc),
            "cell_fully_certified": bool(degA == mu and dA != 0
                                         and below and sc)})
    # ---- golden point (M = 10; boundary class 5 has mu <= 1 at
    # m = 11, 13, so the interior pairs are the whole cell) -----------
    say("golden point a^2 - a - 1 (M = 10), full cells at m = 11, 13:")
    from collections import Counter
    a0 = sp.Rational(1, 2) + sp.sqrt(5) / 2
    for m in (11, 13):
        M, nu = spectrum_M(m)
        th = sp.acos(a0 / 2)
        n = Counter(((2 * j - m) % 10) for j in range(m + 1))
        classes = []
        done = set()
        for c in sorted(n):
            if c in done or c == 0 or 2 * c == 10:
                continue
            done.add(c)
            done.add((-c) % 10)
            if n[c] - 1 >= 2:
                zc = sp.radsimp(sp.expand_trig(
                    sp.nsimplify(2 * sp.cos(c * th), [sp.sqrt(5)])))
                classes.append((c, n[c] - 1, zc))
        assert n[5] - 1 <= 1, "boundary crowded; cell not covered"
        recs = []
        allok = True
        for c, mu_c, zc in classes:
            A, mu, below = associated_poly(M, zc, a0, nu)
            assert mu == mu_c, (m, c, mu, mu_c)
            dA = sp.simplify(sp.discriminant(A.as_expr(), lam))
            degA = sp.degree(A.as_expr(), lam)
            ok = bool(sp.simplify(dA) != 0 and degA == mu and below)
            allok = allok and ok
            say(f"  m = {m}, class pair {{{c}, {10 - c}}}: mu = {mu}, "
                f"(T) {'OK' if ok else 'FAIL'}")
            recs.append({"m": m, "class": int(c), "mu": int(mu),
                         "T_ok": ok})
        sc, dg, want = certify_cell(M, a0,
                                    [mc for _, mc, _ in classes],
                                    [zz for _, _, zz in classes])
        say(f"    (S)+(C): gcd degree {dg} == {want}: {sc}")
        out["other_points"].append({
            "point": "a^2 - a - 1", "m": m, "classes": recs,
            "separation_and_no_accident": bool(sc),
            "cell_fully_certified": bool(allok and sc),
            "predicted_mult": int(sum(mc * (mc - 1)
                                      for _, mc, _ in classes))})
    json.dump(out, open('matrix/branch_slopes.json', 'w'), indent=1)
    say("done")


if __name__ == "__main__":
    main()
