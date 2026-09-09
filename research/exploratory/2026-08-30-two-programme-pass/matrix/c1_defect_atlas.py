"""C1 + C3: the defect atlas (programme #764).

Part A (symbolic, sympy, d = 2, free (a, b)): for m = 2..9 build the
power-defect numerator N_m from the PROVED coefficient formula of
T-108500 (c_r = sum_u (-1)^{r-u} e_{r-u}(Sym^m) h_u^m), certify the tail
vanishes on an independent window, verify self-duality, then extract the
DEFORMATION SPECTRUM POLYNOMIAL M_m defined by

    N_m(T) = (1 + b^{m/2} T)^eps * T^nu * M_m(b^m T + 1/T),
    eps = 1 iff m even,   nu = (m - 1 - eps)/2,   deg_z M_m = nu,

whose z-roots are (minus) the traces of self-dual rank-2 local data of
determinant b^m (m = 3: M_3 = z + 2ab recovers the cube-defect bridge's
trace-doubled deformation). Factor M_m over Q(a,b) and factor
disc_z(M_m) — the TOWER INVARIANTS D_m — and expand each D_m on the
b = 1 slice in the Chebyshev basis q_j = x^j + x^{-j} (a = x + 1/x).

Part A2 (instantiation statistics): factor N_m over Q at ~200 integer
(a,b) points for m = 5,7,9; correlate splitting with D_m squareness.

Part B (exact Fractions, stdlib core): the (m,d) grid — (2,d) d<=6,
(3,d) d<=4, (4,d) d<=3 — at generic integer instantiations: certify
deg Q = C(d+m-1, m) (denominator fullness), test the CODIMENSION-d LAW
deg N_{m,d} = C(d+m-1, m) - d, and test scaled self-duality of N.

Part C (transforms at d = 2): Rankin control (symbolic, recurrence
series), mixed cube h_A^2 h_B, shift-then-square, section defects and
composition degree tracking.

Everything exact. Writes matrix/c1_defect_atlas.json.
rh_established = false.
"""
import json
import sys
import time
from fractions import Fraction as Fr
from math import comb

import sympy as sp

sys.path.insert(0, '.')
from core.exact import minimal_rational_form

a, b, T, z, x = sp.symbols('a b T z x')
OUT = {"meta": {"arithmetic_class": "EXACT_RATIONAL/EXACT_SYMBOLIC",
                "sympy": sp.__version__, "rh_established": False}}


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


# ---------------- Part A: symbolic d=2 defect + deformation spectrum ------

def h_sequence(n):
    """h_0..h_n for 1/(1 - aT + bT^2)."""
    h = [sp.Integer(1), a]
    for k in range(2, n + 1):
        h.append(sp.expand(a * h[-1] - b * h[-2]))
    return h[:n + 1]


def q_sequence(n):
    """q_j = alpha^j + beta^j (alpha+beta=a, alpha beta=b)."""
    q = [sp.Integer(2), a]
    for j in range(2, n + 1):
        q.append(sp.expand(a * q[-1] - b * q[-2]))
    return q


def symk_power_sums(m, nmax):
    """Power sums p_j of Sym^m eigenvalues alpha^i beta^{m-i}, j<=nmax."""
    q = q_sequence(m * nmax + 1)
    ps = []
    for j in range(1, nmax + 1):
        s = sp.Integer(0)
        i = 0
        while 2 * i < m:
            s += b ** (i * j) * q[(m - 2 * i) * j]
            i += 1
        if m % 2 == 0:
            s += b ** ((m // 2) * j)
        ps.append(sp.expand(s))
    return ps


def elementary_from_ps_sym(ps, d):
    e = [sp.Integer(1)]
    for k in range(1, d + 1):
        s = sp.Integer(0)
        for i in range(1, k + 1):
            s += (-1) ** (i - 1) * e[k - i] * ps[i - 1]
        e.append(sp.expand(s / k))
    return e


def defect_numerator(m):
    """N_m via the PROVED T-108500 formula + independent tail check."""
    dim = m + 1
    e = elementary_from_ps_sym(symk_power_sums(m, dim), dim)
    h = h_sequence(m + 4)
    hm = [sp.expand(hk ** m) for hk in h]

    def c(r):
        s = sp.Integer(0)
        for u in range(0, r + 1):
            if r - u <= dim:
                s += (-1) ** (r - u) * e[r - u] * hm[u]
        return sp.expand(s)

    N = [c(r) for r in range(m)]              # proved degree m-1
    for r in range(m, m + 4):                 # independent tail window
        assert c(r) == 0, f"tail fails at m={m}, r={r}"
    return N


def check_selfdual(N, m):
    """N_m(T) = b^{m(m-1)/2} T^{m-1} N_m(1/(b^m T)) coefficientwise."""
    for r in range(m):
        lhs = N[m - 1 - r]
        rhs = sp.expand(b ** (m * (m - 1) // 2) * N[r] / b ** (m * r))
        if sp.simplify(lhs - rhs) != 0:
            return False
    return True


def spectrum_poly(N, m):
    """Extract M_m with N(T) = (1+b^{m/2}T)^eps T^nu M(b^m T + 1/T),
    nu = (m-1-eps)/2, by exact linear solve. Returns (M, eps, ok)."""
    eps = 1 if m % 2 == 0 else 0
    nu = (m - 1 - eps) // 2
    mus = sp.symbols(f'mu0:{nu + 1}')
    expr = sum(mus[j] * (b ** m * T + 1 / T) ** j for j in range(nu + 1))
    expr = sp.expand(expr * T ** nu)
    if eps:
        expr = sp.expand(expr * (1 + b ** (m // 2) * T))
    target = sum(N[r] * T ** r for r in range(m))
    diff = sp.expand(expr - target)
    eqs = [sp.Eq(sp.expand(diff.coeff(T, r)), 0) for r in range(m)]
    sol = sp.solve(eqs, mus, dict=True)
    if not sol:
        return None, eps, False
    M = sp.expand(sum(sol[0][mus[j]] * z ** j for j in range(nu + 1)))
    resid = sp.simplify(diff.subs(sol[0]))
    return M, eps, resid == 0


def chebyshev_slice(P):
    """b=1, a=x+1/x: rewrite a Laurent-symmetric expression in the basis
    q_j = x^j + x^-j; returns {j: coeff} or the raw Laurent dict if not
    symmetric."""
    ex = sp.together(sp.expand(P.subs({b: 1, a: x + 1 / x})))
    num, den = sp.fraction(ex)
    pd = sp.Poly(sp.expand(den), x)
    if len(pd.monoms()) != 1:
        return {"error": "denominator not monomial"}
    k = pd.monoms()[0][0]
    c0 = pd.coeffs()[0]
    p = sp.Poly(sp.expand(num), x)
    coeffs = {mon[0] - k: cf / c0 for mon, cf in
              zip(p.monoms(), p.coeffs())}
    out = {}
    for j, cj in coeffs.items():
        if j < 0:
            continue
        if j > 0 and sp.simplify(coeffs.get(-j, sp.Integer(0)) - cj) != 0:
            return {"not_symmetric": {str(jj): str(cc) for jj, cc
                                      in sorted(coeffs.items())}}
        out[j] = cj
    return {str(j): str(sp.nsimplify(c)) for j, c in sorted(out.items())}


def part_A():
    rows = {}
    for m in range(2, 10):
        t0 = time.time()
        N = defect_numerator(m)
        sd = check_selfdual(N, m)
        M, eps, ok = spectrum_poly(N, m)
        Mfac = sp.factor(M) if M is not None else None
        disc = None
        discfac = None
        cheb = None
        if M is not None and sp.degree(M, z) >= 2:
            disc = sp.discriminant(sp.Poly(M, z), z)
            discfac = sp.factor(disc)
            cheb = chebyshev_slice(disc)
        rows[str(m)] = {
            "deg_N": m - 1, "self_dual": sd,
            "even_factor_1_plus_b^{m/2}T": bool(eps),
            "spectrum_poly_M": str(M) if M is not None else None,
            "M_factored": str(Mfac), "M_residual_zero": ok,
            "disc_z_M_factored": str(discfac) if discfac is not None
            else None,
            "disc_chebyshev_qbasis(b=1,a=x+1/x)": cheb,
            "N_coeffs": [str(c) for c in N],
        }
        say(f"A: m={m} selfdual={sd} eps={eps} M_fac={Mfac} "
            f"disc={discfac} ({time.time()-t0:.1f}s)")
    OUT["A_deformation_spectrum"] = rows


def part_A2():
    say("A2: instantiation factor-pattern statistics (m = 5, 7, 9)")
    stats = {}
    Ns = {m: defect_numerator(m) for m in (5, 7, 9)}
    D5 = 16 * a ** 4 - 48 * a ** 2 * b + 41 * b ** 2
    pts = [(ai, bi) for ai in range(-7, 8) for bi in range(-7, 8)
           if bi != 0 and ai != 0 and ai * ai != 4 * bi][:210]
    for m in (5, 7, 9):
        pat = {}
        extra = {"n_points": 0, "n_split": 0}
        if m == 5:
            extra.update({"D5_square": 0, "D5_square_and_split": 0,
                          "split_without_D5_square": 0})
        for (ai, bi) in pts:
            vals = [int(sp.expand(cc.subs({a: ai, b: bi})))
                    for cc in Ns[m]]
            if vals[-1] == 0:
                continue                      # degeneration locus
            poly = sp.Poly(list(reversed(vals)), T)
            fl = sp.factor_list(poly)[1]
            key = tuple(sorted(sum([[f[0].degree()] * f[1]
                                    for f in fl], [])))
            pat[str(key)] = pat.get(str(key), 0) + 1
            extra["n_points"] += 1
            split = len(key) > 1
            if split:
                extra["n_split"] += 1
            if m == 5:
                v = int(D5.subs({a: ai, b: bi}))
                is_sq = v >= 0 and sp.sqrt(v).is_Integer
                if is_sq:
                    extra["D5_square"] += 1
                    if split:
                        extra["D5_square_and_split"] += 1
                elif split:
                    extra["split_without_D5_square"] += 1
        stats[str(m)] = {"patterns": pat, **extra}
        say(f"A2: m={m} patterns={pat} extra={extra}")
    OUT["A2_factor_patterns"] = stats


# ---------------- Part B: the (m,d) grid ----------------------------------

def h_seq_general(es, n):
    """h_k for 1/(1 - e1 T + e2 T^2 - ...), exact Fractions."""
    d = len(es)
    h = [Fr(1)]
    for k in range(1, n + 1):
        s = Fr(0)
        for i in range(1, min(k, d) + 1):
            s += (-1) ** (i - 1) * Fr(es[i - 1]) * h[k - i]
        h.append(s)
    return h


def selfdual_scale_test(P):
    """Is P scaled-palindromic: c_{deg-r} = s K^r c_r for rational s,K?"""
    Pt = [Fr(f) for f in P]
    dg = len(Pt) - 1
    if dg < 1 or Pt[0] == 0 or Pt[-1] == 0:
        return None
    sconst = Pt[dg] / Pt[0]
    Ks = set()
    for r in range(0, dg):
        if Pt[r + 1] != 0 and Pt[r] != 0 and Pt[dg - r] != 0 \
                and Pt[dg - r - 1] != 0:
            Ks.add((Pt[dg - r - 1] / Pt[r + 1]) / (Pt[dg - r] / Pt[r]))
    if len(Ks) != 1:
        return {"self_dual_scaled": False, "note": "no unique scale"}
    K = Ks.pop()
    ok = all(Pt[dg - r] == sconst * K ** r * Pt[r] for r in range(dg + 1))
    return {"self_dual_scaled": bool(ok), "K": str(K), "s": str(sconst)}


def part_B():
    say("B: (m,d) grid — codimension law + duality")
    import random
    rnd = random.Random(108500)
    grid = ([(2, d) for d in range(2, 7)] + [(3, d) for d in range(2, 5)]
            + [(4, d) for d in range(2, 4)])
    rows = {}
    for (m, d) in grid:
        dim = comb(d + m - 1, m)
        pred = dim - d
        need = 2 * dim + pred + 8
        recs = []
        for _ in range(5):
            es = [rnd.randint(1, 9) * rnd.choice([1, -1]) for _ in range(d)]
            h = h_seq_general(es, need)
            r = minimal_rational_form([hk ** m for hk in h])
            if r is None:
                recs.append({"es": es, "verdict": "REFUSED"})
                continue
            P, Q = r
            recs.append({"es": es, "deg_N": len(P) - 1, "deg_Q": len(Q) - 1,
                         "dual": selfdual_scale_test(P)})
        gen = [(rc["deg_N"], rc["deg_Q"]) for rc in recs if "deg_N" in rc]
        degP = max(p for (p, q) in gen)
        degQ = max(q for (p, q) in gen)
        rows[f"m{m}_d{d}"] = {
            "dim_Sym^m": dim, "deg_Q_generic": degQ,
            "denominator_full": degQ == dim,
            "deg_N_generic": degP, "codim_law_pred": pred,
            "codim_law_holds": degP == pred,
            "trials": recs,
        }
        say(f"B: (m={m},d={d}) dim={dim} degQ={degQ} degN={degP} "
            f"pred={pred} law={'OK' if degP == pred else 'FAIL'} "
            f"dual={[rc.get('dual', {}) and rc['dual'].get('self_dual_scaled') for rc in recs if 'deg_N' in rc]}")
    OUT["B_grid"] = rows


# ---------------- Part C: transforms --------------------------------------

def series_from_recurrence(numc, denc, n):
    """Exact series of num/den (den[0]=1), symbolic coefficients."""
    s = []
    for k in range(n):
        v = numc[k] if k < len(numc) else sp.Integer(0)
        for r in range(1, min(k, len(denc) - 1) + 1):
            v -= denc[r] * s[k - r]
        s.append(sp.expand(v))
    return s


def part_C():
    say("C: transform defects at d=2")
    c, dd = sp.symbols('c d')
    res = {}

    # Rankin control: sum h_k(A) h_k(B) T^k = (1 - det A det B T^2) /
    # det(1 - A x B T), verified symbolically via recurrence series
    hA = h_sequence(12)
    hB = [hh.subs({a: c, b: dd}) for hh in hA]
    qA = q_sequence(6)
    qB = [qq.subs({a: c, b: dd}) for qq in qA]
    psT = [sp.expand(qA[j] * qB[j]) for j in range(1, 5)]
    eT = elementary_from_ps_sym(psT, 4)
    denc = [sp.expand((-1) ** r * eT[r]) for r in range(5)]
    numc = [sp.Integer(1), sp.Integer(0), sp.expand(-b * dd)]
    ser = series_from_recurrence(numc, denc, 12)
    ok = all(sp.simplify(ser[k] - sp.expand(hA[k] * hB[k])) == 0
             for k in range(12))
    res["rankin_control_symbolic"] = ok
    say(f"C: Rankin control closed form {'CONFIRMED' if ok else 'FAILED'}")

    import random
    rnd = random.Random(108501)

    # mixed cube h_A^2 h_B: denominator should be Sym^2(A) x B (dim 6);
    # codimension question: deg N = 6 - 2?  duality scale?
    rows = []
    for _ in range(6):
        A = (rnd.randint(1, 9), rnd.randint(1, 9) * rnd.choice([1, -1]))
        B = (rnd.randint(1, 9), rnd.randint(1, 9) * rnd.choice([1, -1]))
        hA_ = h_seq_general(list(A), 40)
        hB_ = h_seq_general(list(B), 40)
        r = minimal_rational_form([hA_[k] ** 2 * hB_[k] for k in range(41)])
        if r is None:
            rows.append({"A": A, "B": B, "verdict": "REFUSED"})
            continue
        P, Q = r
        rows.append({"A": A, "B": B, "deg_N": len(P) - 1,
                     "deg_Q": len(Q) - 1, "dual": selfdual_scale_test(P)})
    res["mixed_cube_h2A_h1B"] = rows
    say(f"C: mixed cube (deg_N, deg_Q) = "
        f"{[(r.get('deg_N'), r.get('deg_Q')) for r in rows]}")

    # shift-then-square: g_k = h_{k+1}; same Sym^2 denominator, numerator?
    rows = []
    for _ in range(4):
        A = (rnd.randint(1, 9), rnd.randint(1, 9) * rnd.choice([1, -1]))
        h_ = h_seq_general(list(A), 30)
        r = minimal_rational_form([h_[k + 1] ** 2 for k in range(29)])
        rows.append({"A": A,
                     "deg": (len(r[0]) - 1, len(r[1]) - 1) if r
                     else "REFUSED",
                     "dual": selfdual_scale_test(r[0]) if r else None})
    res["shift_then_square"] = rows
    say(f"C: shift-then-square degs = {[r['deg'] for r in rows]}")

    # section s_k = h_{2k}: its own minimal form, then the square's.
    # (pointwise power commutes with sections; the content here is how
    # the section's NUMERATOR feeds the square's defect vs the pure
    # object of the same denominator, whose m=2 defect is 1 + e2 T)
    rows = []
    for _ in range(4):
        A = (rnd.randint(1, 9), rnd.randint(1, 9) * rnd.choice([1, -1]))
        h_ = h_seq_general(list(A), 62)
        sec = [h_[2 * k] for k in range(31)]
        r0 = minimal_rational_form(sec)
        r1 = minimal_rational_form([v ** 2 for v in sec])
        rows.append({"A": A,
                     "section_deg": (len(r0[0]) - 1, len(r0[1]) - 1)
                     if r0 else "REFUSED",
                     "section_numer": [str(v) for v in r0[0]] if r0
                     else None,
                     "square_of_section_deg": (len(r1[0]) - 1,
                                               len(r1[1]) - 1)
                     if r1 else "REFUSED",
                     "square_dual": selfdual_scale_test(r1[0]) if r1
                     else None})
    res["section_transforms"] = rows
    say(f"C: section degs = "
        f"{[(r['section_deg'], r['square_of_section_deg']) for r in rows]}")
    OUT["C_transforms"] = res


def main():
    t0 = time.time()
    part_A()
    with open("matrix/c1_defect_atlas.json", "w") as f:
        json.dump(OUT, f, indent=1)
    part_A2()
    with open("matrix/c1_defect_atlas.json", "w") as f:
        json.dump(OUT, f, indent=1)
    part_B()
    with open("matrix/c1_defect_atlas.json", "w") as f:
        json.dump(OUT, f, indent=1)
    part_C()
    with open("matrix/c1_defect_atlas.json", "w") as f:
        json.dump(OUT, f, indent=1)
    say(f"C1 atlas done in {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
