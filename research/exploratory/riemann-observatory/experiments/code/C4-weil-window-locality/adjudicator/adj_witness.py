"""Adjudicator: Arb-rigorous evaluation of explicit detection witnesses in the injection models of C4.

Model functional (precise definition used here; it is a finite computation):
    W_mod(g) = A(g) + Q_{T0,delta}(g) - R(g),
  A(g)  = arithmetic side of the explicit formula for f = g*g~ (brief's normalisation)
        = int 2cosh(y/2) f(y) dy - sum_{n<e^{2L}} Lambda(n) n^{-1/2} (f(log n)+f(-log n))
          - (log 4pi + gamma_E) f(0) - int_0^inf [e^{-y/2}(f(y)+f(-y)) - 2e^{-y} f(0)]/(1-e^{-2y}) dy,
        which equals sum over ALL zeta zeros of h_g(gamma) conj h_g(conj gamma) unconditionally;
  Q     = sum_{z in {T0-i d, T0+i d, -T0+i d, -T0-i d}} h_g(z) conj h_g(conj z)   (injected quadruple);
  R     = 0 (additive model) or sum_{gamma in {+-ga, +-gb}} |h_g(gamma)|^2 (collision model: the two
          Arb-certified neighbouring ordinates ga < T0 < gb are removed).
Test function: g(x) = e^{-i T0 x} p(x) on [-L, L], p a polynomial with exact rational coefficients
obtained by rounding the float64 ground-state eigenvector of the INVESTIGATOR's model matrix
(detect_lib / weil_core) -- the eigenvector only serves to choose g; every quantity below is
recomputed from scratch in Arb (python-flint) from the definition above:
  * f(y) = e^{-i T0 y} a(y), a(y) exact in Q[i][y] (Taylor/antiderivative formula, fmpq_poly);
  * pole term: closed form int_0^{2L} e^{cy} a(y) dy = [e^{cy} sum_k (-1)^k a^(k)(y)/c^{k+1}];
  * prime sum: exact list of prime powers, Arb logs;
  * archimedean integral: acb.integral (rigorous) of an integrand rewritten without removable
    singularity: G = {e^{-y/2}[e1 b + e1' b~ - 2 T0 a0 sin(T0y/2) sinc(T0y/2)] + a0 e^{-3y/4} sinc(iy/4)}
                    / (2 e^{-y} sinc(iy)),  b = (a - a0)/y,  plus the exact tail -2 a0 artanh(e^{-2L});
  * h_g(z): exact finite integration-by-parts sum, high precision.
The output is a ball for W_mod(g)/||g||^2; if its upper end is < 0 this is a NUMERICAL-RIGOROUS proof
(modulo FLINT/Arb correctness) that the MODEL form is negative on window L.

Usage: OPENBLAS_NUM_THREADS=1 python3 adj_witness.py CASE   (CASE in coll_T1e4_d0.1, add_T1e4_d0.49, add_T7e4_d0.2, ...)
"""
import os, sys, json, time, math, hashlib, platform
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
from fractions import Fraction
CODE = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C4-weil-window-locality"
sys.path.insert(0, CODE)
sys.path.insert(0, "/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C1-detection-horizons")
import numpy as np
import flint
from flint import fmpq, fmpq_poly, arb, acb, acb_poly
RES = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/adjudicator"
ZFILES = ["/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/data/zeros_1_50000.tsv",
          "/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/data/zeros_50001_100000.tsv"]

CASES = {
    # name: (model, T_target, delta (string, exact rational), L (string, exact rational), N)
    "coll_T1e4_d0.1": ("collision", 10000.0, "1/10", "7/2", 64),
    "coll_T1e4_d0.2": ("collision", 10000.0, "1/5", "16/5", 64),
    "add_T1e4_d0.49": ("add", 10000.0, "49/100", "13/5", 64),
    "add_T7e4_d0.2": ("add", 70000.0, "1/5", "23/5", 96),
    "add_T1e3_d0.01": ("add", 1000.0, "1/100", "3", 64),
    "coll_T1e4_d0.1_L3.3": ("collision", 10000.0, "1/10", "33/10", 64),
    "coll_T1e4_d0.03_L3.67": ("collision", 10000.0, "3/100", "367/100", 96),
    "add_T7e4_d0.2_L4.5": ("add", 70000.0, "1/5", "9/2", 96),
}


def load_neighbors(Tt):
    rows = []
    for f in ZFILES:
        with open(f) as fh:
            for line in fh:
                n, m, r = line.split()
                rows.append((m, r))
    mids = np.array([float(m) for m, _ in rows])
    k = int(np.searchsorted(mids, Tt))
    return rows[k - 1], rows[k], float(mids[k - 1]), float(mids[k])


def legendre_scaled(j, Lq):
    return fmpq_poly.legendre_p(j)(fmpq_poly([0, 1 / Lq]))


def main(case):
    model, Tt, dstr, Lstr, N = CASES[case]
    t_start = time.time()
    (ma, ra), (mb, rb), ga_f, gb_f = load_neighbors(Tt)
    T0f = 0.5 * (ga_f + gb_f)                      # same T0 as the investigator (midpoint, float64)
    dq, Lq = fmpq(Fraction(dstr).numerator, Fraction(dstr).denominator), fmpq(Fraction(Lstr).numerator, Fraction(Lstr).denominator)
    d_f, L_f = float(Fraction(dstr)), float(Fraction(Lstr))
    LN = 0.5 * math.log(T0f / (2 * math.pi))

    # ---- float64 model matrix (investigator code), only to choose the test function ----
    from detect_lib import W_true
    from weil_core import quad_matrix, real_zero_matrix
    W = W_true(T0f, L_f, N, asym=False)
    Wm = W + quad_matrix(T0f, d_f, T0f, L_f, N)
    if model == "collision":
        Wm = Wm - real_zero_matrix(np.array([ga_f, gb_f]), T0f, L_f, N)
    Wm = 0.5 * (Wm + Wm.conj().T)
    ev, V = np.linalg.eigh(Wm)
    lam_float = float(ev[0])
    v = V[:, 0]
    c = np.conj(v)            # coefficient convention: W(g) = sum_jk c_j W_jk conj(c_k), so c = conj(eigvec)
    u = c * np.sqrt((2 * np.arange(N) + 1) / (2 * L_f))

    # ---- exact polynomial p = pr + i pi ----
    pr, pim = fmpq_poly([0]), fmpq_poly([0])
    for j in range(N):
        Pj = legendre_scaled(j, Lq)
        fr, fi = Fraction(float(u[j].real)), Fraction(float(u[j].imag))
        pr += fmpq(fr.numerator, fr.denominator) * Pj
        pim += fmpq(fi.numerator, fi.denominator) * Pj
    deg = max(pr.degree(), pim.degree())

    # ---- exact autocorrelation a(y) = int_{-L}^{L-y} p(u+y) conj p(u) du, 0 <= y <= 2L ----
    Ly = fmpq_poly([Lq, -1])     # L - y
    yv = fmpq_poly([0, 1])
    ar, ai = fmpq_poly([0]), fmpq_poly([0])
    dr, di = pr, pim
    fact = fmpq(1)
    for k in range(deg + 1):
        if k > 0:
            dr, di = dr.derivative(), di.derivative()
            fact = fact * k
        re_k = (dr * pr + di * pim).integral()
        im_k = (di * pr - dr * pim).integral()
        Jr = re_k(Ly) - re_k(-Lq)
        Ji = im_k(Ly) - im_k(-Lq)
        yk = yv ** k / fact
        ar += yk * Jr
        ai += yk * Ji
    a0 = ar(fmpq(0))
    assert ai(fmpq(0)) == 0

    flint.ctx.prec = 512
    j_ = acb(0, 1)
    T0 = arb(fmpq(Fraction(T0f).numerator, Fraction(T0f).denominator))
    L = arb(Lq)
    d = arb(dq)
    a0a = arb(a0)

    def to_acbpoly(Pr, Pi, shift):
        # polynomial in s = y - shift
        Pr2, Pi2 = Pr(fmpq_poly([shift, 1])), Pi(fmpq_poly([shift, 1]))
        n = max(Pr2.length(), Pi2.length())
        cr = Pr2.coeffs() + [fmpq(0)] * (n - Pr2.length())
        ci = Pi2.coeffs() + [fmpq(0)] * (n - Pi2.length())
        return acb_poly([acb(arb(x), arb(yy)) for x, yy in zip(cr, ci)])

    A_s = to_acbpoly(ar, ai, Lq)                        # a(y), in s = y - L
    br = (ar - a0).right_shift(1) if hasattr(ar, "right_shift") else None
    bi = ai.right_shift(1)
    B_s = to_acbpoly(br, bi, Lq)                        # b(y) = (a(y)-a0)/y
    Bc_s = to_acbpoly(br, -bi, Lq)                      # conj-coefficient b~

    # ---- pole term: 2 Re [I(1/2 - i T0) + I(-1/2 - i T0)], I(c) = int_0^{2L} e^{cy} a(y) dy ----
    derivs_r, derivs_i = [ar], [ai]
    for k in range(deg * 2 + 2):
        derivs_r.append(derivs_r[-1].derivative()); derivs_i.append(derivs_i[-1].derivative())

    def I_exp(cc):
        tot = acb(0)
        twoL = 2 * Lq
        for y_end, sgn in [(twoL, 1), (fmpq(0), -1)]:
            s = acb(0)
            ck = cc
            for k in range(len(derivs_r)):
                val = acb(arb(derivs_r[k](y_end)), arb(derivs_i[k](y_end)))
                s += ((-1) ** k) * val / ck
                ck = ck * cc
            tot += sgn * (cc * arb(y_end)).exp() * s
        return tot
    pole = 2 * (I_exp(acb(arb(1) / 2, -T0)) + I_exp(acb(-arb(1) / 2, -T0))).real

    # ---- prime sum ----
    X = math.exp(2 * L_f)
    pps = []
    sieve = np.ones(int(X) + 2, dtype=bool); sieve[:2] = False
    for pnum in range(2, int(X ** 0.5) + 2):
        if sieve[pnum]:
            sieve[pnum * pnum::pnum] = False
    for pnum in np.nonzero(sieve)[0]:
        pnum = int(pnum); q = pnum
        while q <= X:
            pps.append((q, pnum)); q *= pnum
    PS = arb(0)
    nterms = 0
    for (n, pnum) in pps:
        ln = arb(n).log()
        if not (ln < 2 * L):
            assert ln > 2 * L
            continue
        val = A_s(acb(ln - L))
        PS += arb(pnum).log() / arb(n).sqrt() * 2 * ((-j_ * T0 * ln).exp() * val).real
        nterms += 1

    # ---- archimedean integral ----
    def G(y, analytic):
        s = y - L
        e1 = (-j_ * T0 * y).exp()
        e2 = (j_ * T0 * y).exp()
        half = T0 * y / 2
        term = (-y / 2).exp() * (e1 * B_s(s) + e2 * Bc_s(s) - 2 * T0 * a0a * half.sin() * half.sinc()) \
            + a0a * (-3 * y / 4).exp() * (j_ * y / 4).sinc()
        return term / (2 * (-y).exp() * (j_ * y).sinc())
    t1 = time.time()
    flint.ctx.prec = 256
    Iarch = acb.integral(G, 0, 2 * L, rel_tol=arb(2) ** -80, abs_tol=arb(2) ** -90, eval_limit=10 ** 8, deg_limit=200)
    t_int = time.time() - t1
    flint.ctx.prec = 512
    tail = -2 * a0a * (-2 * L).exp().atanh()
    arch = Iarch.real + tail
    euler = arb.const_euler()
    f0term = ((4 * arb.pi()).log() + euler) * a0a
    A_g = pole - PS - f0term - arch

    # ---- h_g(z) by exact integration by parts ----
    flint.ctx.prec = 3000
    pd_r, pd_i = [pr], [pim]
    for k in range(deg + 1):
        pd_r.append(pd_r[-1].derivative()); pd_i.append(pd_i[-1].derivative())
    Pp = [acb(arb(pd_r[k](Lq)), arb(pd_i[k](Lq))) for k in range(deg + 1)]
    Pm = [acb(arb(pd_r[k](-Lq)), arb(pd_i[k](-Lq))) for k in range(deg + 1)]
    Lh = arb(Lq)

    def h(z):
        kap = j_ * (z - arb(fmpq(Fraction(T0f).numerator, Fraction(T0f).denominator)))
        eP, eM = (kap * Lh).exp(), (-kap * Lh).exp()
        s = acb(0); kk = kap
        for k in range(deg + 1):
            s += ((-1) ** k) * (eP * Pp[k] - eM * Pm[k]) / kk
            kk = kk * kap
        return s
    T0h = arb(fmpq(Fraction(T0f).numerator, Fraction(T0f).denominator))
    dh = arb(dq)
    quad = acb(0)
    for z in [acb(T0h, -dh), acb(T0h, dh), acb(-T0h, dh), acb(-T0h, -dh)]:
        quad += h(z) * h(z.conjugate()).conjugate()
    removed = arb(0)
    if model == "collision":
        for (m, r) in [(ma, ra), (mb, rb)]:
            # evaluate at the (decimal) midpoint, then widen by |h'| * radius, with the rigorous bound
            # |h'(z)| <= int |x||p(x)| dx <= L sqrt(2L) ||p||_2 for real z (Cauchy-Schwarz)
            gmid = arb(m)
            # certified enclosure of gamma from EXP-0001: [mid - rad - 5e-21, mid + rad + 5e-21]
            # (midpoints printed to 25 significant digits; see experiments/reproducibility.md)
            hp_bound = Lh * (2 * Lh).sqrt() * arb(a0).sqrt() * (arb(r) + arb("5e-21"))
            for sgn in [1, -1]:
                hv = h(acb(sgn * gmid))
                hv = acb(arb(hv.real.mid(), hv.real.rad() + hp_bound), arb(hv.imag.mid(), hv.imag.rad() + hp_bound))
                removed += (hv * hv.conjugate()).real
    flint.ctx.prec = 512
    Wmod = A_g + quad.real - removed
    ratio = Wmod / a0a
    out = {
        "case": case, "model": model, "T0": repr(T0f), "neighbors": [ma + " +- " + ra, mb + " +- " + rb],
        "delta": dstr, "L": Lstr, "L_float": L_f, "L_N": LN, "kappa=delta*log(T0/2pi)": d_f * 2 * LN, "N": N,
        "deg_p": deg, "prime_powers_used": nterms,
        "lam_min_float64_investigator_matrix": lam_float,
        "quad_imag_part": quad.imag.str(5),
        "components_over_norm2": {
            "pole": (pole / a0a).str(15), "prime_sum": (PS / a0a).str(15), "f0term": (f0term / a0a).str(15),
            "arch": (arch / a0a).str(15), "A(g)": (A_g / a0a).str(15),
            "quadruple": (quad.real / a0a).str(15), "removed_zeros": (removed / a0a).str(15)},
        "norm2_a0": arb(a0).str(15),
        "W_mod_over_norm2_ball": ratio.str(20),
        "W_mod_over_norm2_upper": float(ratio.mid() + ratio.rad()),
        "certified_negative": bool(ratio < 0),
        "arch_integral_seconds": round(t_int, 1),
        "runtime_s": round(time.time() - t_start, 1),
        "versions": {"python": platform.python_version(), "python-flint": flint.__version__, "numpy": np.__version__},
    }
    os.makedirs(RES, exist_ok=True)
    fn = os.path.join(RES, "adj_witness_%s.json" % case)
    with open(fn, "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out, indent=1))
    print("sha256", hashlib.sha256(open(fn, "rb").read()).hexdigest())


if __name__ == "__main__":
    main(sys.argv[1])
