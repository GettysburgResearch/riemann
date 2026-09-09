"""Lane 4, stage 2 — PROVED complex off-critical-line zero at an exact
rational modulus adjacent to the C8 archipelago.

Modulus: z* = x* + i y*, x* = 4341/50000, y* = 3731/2500 (the theta80
dirty probe point of island_probe.json rounded to exact rationals; the
off-line zero pair persists there). Form Q(m,n) = |m + n z*|^2 / y*.

CLAIM CERTIFIED: Lambda(s) = pi^{-s} Gamma(s) Z_Q(s) has EXACTLY ONE
zero (counted with multiplicity, via a rigorous winding number = 1)
inside the rectangle

    Re s in [83/100, 99/100],  Im s in [1221/100, 1238/100],

whose left edge is strictly right of the critical line: an off-line
zero with Re rho >= 0.83 (float location ~ 0.90837 + 12.29624 i).

Method (everything interval-rigorous, mpmath.iv directed rounding):
  1. Lambda via the incomplete-gamma representation (theta self-dual,
     Q* = Q o swap; same derivation as the rectangular certificate),
     evaluated at complex points with:
       - Spouge's approximation (a = 41) for Gamma(s), Gamma(1-s),
         with Spouge's explicit error bound (IMPORTED_THEOREM,
         Spouge 1994: |eps| <= a^{-1/2} (2 pi)^{-(a+1/2)}, Re z >= 0),
       - the lower-gamma series (x < 35) or the integration-by-parts
         asymptotic with remainder |R_n| <= |prod (s-i)| x^{sigma-n-1}
         e^{-x} (x >= 35),
       - lattice cutoff Q <= 14 with the proved tail bound
         sum_{Q>X} 2 e^{-pi Q}/(pi Q) <= (2/(pi X)) e^{-pi X/2}
         * [2(1+A')(1+2B') - 1]-style theta bound (exact geometric
         domination via the identity Q = (m+nx)^2/y + y n^2).
  2. A REALISTIC rigorous sup bound B for |Lambda| on the r-enlarged
     rectangle (r = 1/10) via the classical Chowla-Selberg/Epstein
     Fourier expansion (IMPORTED classical; float cross-validated to
     ~1e-40 in wall_certificate.py):
       |Lambda| <= 2 pi^{-sigma} UB|Gamma(s)| zeta(2 sigma) y^sigma
                 + 2 sqrt(pi) pi^{-sigma} UB|Gamma(s-1/2)|
                   * ZB|zeta(2s-1)| y^{1-sigma}
                 + 8 sqrt(y) sum_n n^{sigma+1/2}
                   e^{-mu theta} K_a(2 pi n y cos theta) + tail,
     with three inline-proved lemmas:
       (L1) |Gamma(a+it)|^2 = Gamma(a)^2 / prod_{k>=0}(1+t^2/(a+k)^2)
            (Weierstrass), upper-bounded by truncating the product
            (six a-subintervals against dependency loss);
       (L2) |zeta(s')| <= sum_{n<=N} n^{-sigma'} + N^{1-sigma'}/|s'-1|
            + |s'| N^{-sigma'}/sigma'   (two-line Euler-Maclaurin);
       (L3) |K_{a+i mu}(x)| <= e^{-mu theta} K_a(x cos theta) for
            0 < theta < pi/2 (rotate the integration contour of
            K_nu = (1/2) INT e^{-x cosh u - nu u} du by -i theta),
            and K_a(c) <= e^{-c} sqrt(pi/(2c)) e^{a^2/(2c)}.
  3. Rigorous winding number: walk the contour with adaptive steps
     h_j <= 0.8 * ell_j / M, M = B/r (Cauchy). Then the image of each
     segment lies in the disc D(Lambda(s_j), ell_j) which excludes 0,
     so the continuous argument change per segment equals the
     principal Arg of the ratio of consecutive enclosures (proved:
     the ratio path stays in D(1,1) subset {Re > 0}); the interval
     sum of iv.atan2 arguments must pin 2 pi * (winding).

rh_established = false. Epstein zeta != Riemann zeta.
"""
import json
import time

import mpmath as mp

iv = mp.iv
iv.dps = 30
mp.mp.dps = 30

XN, XD = 4341, 50000          # x* = XN/XD
YN, YD = 3731, 2500           # y* = YN/YD
SLO = (62, 100)               # rectangle (second zero, t ~ 18.95)
SHI = (77, 100)
TLO = (1886, 100)
THI = (1904, 100)
RENL = (1, 25)                # Cauchy enlargement r = 0.04
X_CUT = 28                    # lattice cutoff on Q: at t ~ 19 the
                              # function scale is ~1e-13 and the walk
                              # is ~20000 steps, so the tail box must
                              # be ~1e-18
SP_A = 41                     # Spouge parameter


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def rat(p, q):
    return iv.mpf(p) / iv.mpf(q)


# ---------------- complex rectangles over iv ------------------------

class C:
    __slots__ = ("re", "im")

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, o):
        return C(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return C(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return C(self.re * o.re - self.im * o.im,
                 self.re * o.im + self.im * o.re)

    def rmul(self, r):
        return C(self.re * r, self.im * r)

    def conj(self):
        return C(self.re, -self.im)

    def abs2(self):
        return self.re * self.re + self.im * self.im

    def abs_lo(self):
        a2 = self.abs2()
        lo = mp.mpf(a2.a)
        return mp.sqrt(lo) if lo > 0 else mp.mpf(0)

    def abs_hi(self):
        return mp.sqrt(mp.mpf(self.abs2().b))


def cdiv(a, b):
    n = b.abs2()
    num = a * b.conj()
    return C(num.re / n, num.im / n)


def cexp(a):
    e = iv.exp(a.re)
    return C(e * iv.cos(a.im), e * iv.sin(a.im))


def cbox(r):
    """complex interval box of radius r (an mpf upper bound) around 0."""
    return C(iv.mpf([-r, r]), iv.mpf([-r, r]))


CONE = C(iv.mpf(1), iv.mpf(0))


def cfromint(n):
    return C(iv.mpf(n), iv.mpf(0))


def clog(a):
    """log of complex interval with Re > 0."""
    assert mp.mpf(a.re.a) > 0
    return C(iv.log(a.abs2()) / 2, iv.atan2(a.im, a.re))


# ---------------- Spouge complex gamma ------------------------------

SP_C = None
SP_EPS = None


def spouge_init():
    global SP_C, SP_EPS
    a = iv.mpf(SP_A)
    SP_C = [iv.sqrt(2 * iv.pi)]
    fact = 1
    for k in range(1, SP_A):
        if k > 1:
            fact *= (k - 1)
        ak = iv.mpf(SP_A - k)
        ck = (iv.exp((iv.mpf(2 * k - 1) / 2) * iv.log(ak) + ak)
              / iv.mpf(fact))
        SP_C.append(ck if k % 2 == 1 else -ck)
    SP_EPS = mp.mpf((iv.exp(-(a + iv.mpf(1) / 2) * iv.log(2 * iv.pi))
                     / iv.sqrt(a)).b)


def gamma_c(s):
    """Gamma(s) for 0 < Re s < 2 (complex), via Gamma(s+2)/(s(s+1));
    Spouge (z = s+1, Re z >= 1: Gamma(z+1) form, Re z >= 0 holds)."""
    z = s + CONE
    acc = C(SP_C[0], iv.mpf(0))
    for k in range(1, SP_A):
        acc = acc + cdiv(C(SP_C[k], iv.mpf(0)), z + cfromint(k))
    acc = acc + cbox(SP_EPS)
    za = z + cfromint(SP_A)
    pref = cexp((z + C(rat(1, 2), iv.mpf(0))) * clog(za) - za)
    g2 = pref * acc                       # Gamma(s+2)
    return cdiv(g2, s * (s + CONE))


# ---------------- incomplete gamma (complex s, real interval x) -----

S_ABS_HI = 20.0    # |s| and |1-s| stay below this on our rectangle


def gamma_upper_c(s, x, gamma_s, lnx):
    xb = mp.mpf(x.b)
    if xb < 45:
        # lower-gamma series
        K = 2 * int(mp.ceil(xb)) + 50
        term = cdiv(cexp(s.rmul(lnx) - C(x, iv.mpf(0))), s)
        tot = term
        for k in range(1, K + 1):
            term = cdiv(term.rmul(x), s + cfromint(k))
            tot = tot + term
        ratio = xb / (K + 1 - S_ABS_HI)
        assert 0 < ratio < 0.6
        tot = tot + cbox(term.abs_hi() * ratio / (1 - ratio))
        return gamma_s - tot
    # integration-by-parts asymptotic, n = 20
    n = 20
    u = CONE
    tot = CONE
    for j in range(1, n):
        u = cdiv((s - cfromint(j)) * u, C(x, iv.mpf(0)))
        tot = tot + u
    pref = cexp((s - CONE).rmul(lnx) - C(x, iv.mpf(0)))
    main = pref * tot
    # |R_n| <= prod_{i<=n}|s-i| * x^{sigma-n-1} e^{-x}
    pb = mp.mpf(1)
    for i in range(1, n + 1):
        pb *= (S_ABS_HI + i)
    sig_hi = mp.mpf(s.re.b)
    rb = pb * mp.mpf((iv.exp((iv.mpf(mp.nstr(sig_hi - n - 1, 20))
                              * iv.log(x)) - x)).b)
    return main + cbox(rb)


# ---------------- the lattice and Lambda ----------------------------

from fractions import Fraction as Fr

VECS = None
TAILB = None


def lattice_init():
    global VECS, TAILB
    x = Fr(XN, XD)
    y = Fr(YN, YD)
    zz = x * x + y * y
    vecs = []
    M = 9
    N = 5
    for m in range(-M, M + 1):
        for n in range(-N, N + 1):
            if m == 0 and n == 0:
                continue
            Q = Fr(m * m) + 2 * x * m * n + zz * n * n
            Q = Q / y
            if Q <= X_CUT:
                vecs.append(Q)
    VECS = []
    for Q in vecs:
        Qiv = rat(Q.numerator, Q.denominator)
        xiv = iv.pi * Qiv
        VECS.append((xiv, iv.log(xiv)))
    say(f"lattice: {len(VECS)} vectors with Q <= {X_CUT}")
    # tail bound: sum_{Q>X} 2 e^{-pi Q}/(pi Q)
    #   <= (2/(pi X)) e^{-pi X/2} sum'_v e^{-pi Q(v)/2}
    # and sum'_v e^{-pi Q/2} <= (1+2B') * 2(1+A') - 1  via
    # Q = (m+nx)^2/y + y n^2 exactly.
    yiv = rat(YN, YD)
    q1 = iv.exp(-iv.pi / (2 * yiv))
    Ap = q1 / (1 - q1)
    q2 = iv.exp(-iv.pi * yiv / 2)
    Bp = q2 / (1 - q2)
    theta_half = (1 + 2 * Bp) * 2 * (1 + Ap) - 1
    t = (2 / (iv.pi * iv.mpf(X_CUT)) * iv.exp(-iv.pi * iv.mpf(X_CUT) / 2)
         * theta_half)
    TAILB = mp.mpf(t.b)
    say(f"lattice tail bound: {mp.nstr(TAILB, 4)}")


def lam_c(s):
    gs = gamma_c(s)
    g1s = gamma_c(CONE - s)
    tot = cdiv(CONE, s - CONE) - cdiv(CONE, s)
    for (x, lnx) in VECS:
        t1 = cexp(s.rmul(-lnx)) * gamma_upper_c(s, x, gs, lnx)
        t2 = cexp((s - CONE).rmul(lnx)) * gamma_upper_c(CONE - s, x,
                                                        g1s, lnx)
        tot = tot + t1 + t2
    return tot + cbox(TAILB)


# ---------------- the B bound on the enlarged box -------------------

def ub_gamma_abs(alo, ahi, tlo):
    """sup over a in [alo,ahi], t >= tlo of |Gamma(a+it)| via L1,
    six a-subintervals; product truncated at K (tail >= 1 helps)."""
    K = 300
    best = mp.mpf(0)
    for j in range(6):
        a1 = alo + (ahi - alo) * j / 6
        a2 = alo + (ahi - alo) * (j + 1) / 6
        A = iv.mpf([mp.nstr(a1, 25), mp.nstr(a2, 25)])
        T = iv.mpf(mp.nstr(tlo, 25))
        prod = iv.mpf(1)
        for k in range(K):
            prod = prod * (1 + (T / (A + k)) ** 2)
        ub = mp.mpf((iv.gamma(A) / iv.sqrt(prod)).b)
        if ub > best:
            best = ub
    return best


def zeta_abs_bound(splo, sphi, tpabs_lo, tpabs_hi):
    """Second-order Euler-Maclaurin bound for |zeta(s')|,
    sigma' in [splo, sphi] > 0, |Im s'| in [tpabs_lo, tpabs_hi]:
    zeta(s) = sum_{n<=N} n^{-s} + N^{1-s}/(s-1) - N^{-s}/2
              + s N^{-s-1}/12 + R,
    |R| <= |s||s+1| N^{-sigma-1} / (12 (sigma+1))
    (one more integration by parts than the first-order form;
    |B~2| <= 1/6)."""
    N = 60
    Alo = iv.mpf(mp.nstr(splo, 25))
    S = iv.mpf(0)
    for n in range(1, N + 1):
        S = S + iv.exp(-Alo * iv.log(iv.mpf(n)))
    S = S + iv.exp((1 - Alo) * iv.log(iv.mpf(N))) / iv.mpf(
        mp.nstr(tpabs_lo, 25))
    S = S + iv.exp(-Alo * iv.log(iv.mpf(N))) / 2
    sabs = iv.sqrt(iv.mpf(mp.nstr(sphi, 25)) ** 2
                   + iv.mpf(mp.nstr(tpabs_hi, 25)) ** 2)
    S = S + sabs * iv.exp(-(Alo + 1) * iv.log(iv.mpf(N))) / 12
    S = S + (sabs * (sabs + 1)
             * iv.exp(-(Alo + 1) * iv.log(iv.mpf(N)))
             / (12 * (Alo + 1)))
    return mp.mpf(S.b)


def k_bessel_bound(a_hi, mu_lo, x, theta):
    """L3: |K_{a+i mu}(x)| <= e^{-mu theta} K_a(x cos theta)
    <= e^{-mu theta} e^{-c} sqrt(pi/(2c)) e^{a^2/(2c)}, c = x cos th."""
    c = x * iv.cos(theta)
    kb = iv.exp(-c) * iv.sqrt(iv.pi / (2 * c)) * iv.exp(
        iv.mpf(mp.nstr(a_hi, 25)) ** 2 / (2 * c))
    return mp.mpf((iv.exp(-iv.mpf(mp.nstr(mu_lo, 25)) * theta) * kb).b)


def compute_B():
    r = mp.mpf(RENL[0]) / RENL[1]
    slo = mp.mpf(SLO[0]) / SLO[1] - r
    shi = mp.mpf(SHI[0]) / SHI[1] + r
    tlo = mp.mpf(TLO[0]) / TLO[1] - r
    thi = mp.mpf(THI[0]) / THI[1] + r
    y = mp.mpf(YN) / YD
    yiv = rat(YN, YD)
    # A1 = 2 pi^{-s} Gamma(s) zeta(2s) y^s
    ubg1 = ub_gamma_abs(slo, shi, tlo)
    z2s = zeta_abs_bound(2 * slo, 2 * shi, 2 * tlo, 2 * thi)  # sigma>1: fine
    A1 = mp.mpf((2 * iv.exp(-iv.mpf(mp.nstr(slo, 25)) * iv.log(iv.pi))
                 * iv.mpf(mp.nstr(ubg1, 25)) * iv.mpf(mp.nstr(z2s, 25))
                 * iv.exp(iv.mpf(mp.nstr(shi, 25)) * iv.log(yiv))).b)
    # A2 = 2 sqrt(pi) pi^{-s} Gamma(s-1/2) zeta(2s-1) y^{1-s}
    ubg2 = ub_gamma_abs(slo - mp.mpf('0.5'), shi - mp.mpf('0.5'), tlo)
    z2s1 = zeta_abs_bound(2 * slo - 1, 2 * shi - 1, 2 * tlo, 2 * thi)
    A2 = mp.mpf((2 * iv.sqrt(iv.pi)
                 * iv.exp(-iv.mpf(mp.nstr(slo, 25)) * iv.log(iv.pi))
                 * iv.mpf(mp.nstr(ubg2, 25)) * iv.mpf(mp.nstr(z2s1, 25))
                 * iv.exp((1 - iv.mpf(mp.nstr(slo, 25))) * iv.log(yiv))).b)
    # K block: 8 sqrt(y) sum_n n^{sigma+1/2} e^{-mu theta} K_a(..)
    theta = rat(27, 20)
    a_hi = max(abs(slo - mp.mpf('0.5')), abs(shi - mp.mpf('0.5')))
    KB = mp.mpf(0)
    last = None
    for n in range(1, 9):
        kb = k_bessel_bound(a_hi, tlo, 2 * iv.pi * yiv * n, theta)
        term = mp.mpf((8 * iv.sqrt(yiv)
                       * iv.exp(iv.mpf(mp.nstr(shi + mp.mpf('0.5'), 25))
                                * iv.log(iv.mpf(n)))).b) * kb
        KB += term
        last = term
    ratio = mp.mpf((iv.exp(iv.mpf(mp.nstr(shi + mp.mpf('0.5'), 25))
                           * iv.log(iv.mpf(9) / 8))
                    * iv.exp(-2 * iv.pi * yiv * iv.cos(theta))).b)
    assert ratio < 1
    KB += last * ratio / (1 - ratio)
    B = A1 + A2 + KB
    say(f"B bound: A1={mp.nstr(A1,3)} A2={mp.nstr(A2,3)} "
        f"K={mp.nstr(KB,3)} -> B={mp.nstr(B,4)}")
    return B, r


# ---------------- winding walk --------------------------------------

def walk(edge_only=None):
    """Full contour (edge_only None) or a single edge k in 0..3.

    Edge-parallel soundness: the winding number is (1/2pi) times the
    sum over ALL steps of the true arg increments, each of which lies
    in its step's iv.atan2 enclosure (exact-step lemma, per step).
    Splitting the step set at the exact rational corners is
    associativity of that same sum: each edge worker starts from
    lam_c(corner_e) and ends at lam_c(corner_{e+1}) — deterministic
    interval boxes, identical across processes — so the four per-edge
    interval sums add to an enclosure of the full loop's total. (The
    sequential version's zero-length closing term encloses 0 and is
    simply omitted.) Interval endpoints cross processes as 40-digit
    decimal strings and are outward-padded by 1e-30 in the combiner,
    dwarfing any decimal-representation rounding at these dps."""
    B, r = compute_B()
    M = B / r
    say(f"Lipschitz M = {mp.nstr(M, 4)}")
    corners = [(Fr(SLO[0], SLO[1]), Fr(TLO[0], TLO[1])),
               (Fr(SHI[0], SHI[1]), Fr(TLO[0], TLO[1])),
               (Fr(SHI[0], SHI[1]), Fr(THI[0], THI[1])),
               (Fr(SLO[0], SLO[1]), Fr(THI[0], THI[1]))]

    def cpt(fs, ft):
        return C(rat(fs.numerator, fs.denominator),
                 rat(ft.numerator, ft.denominator))

    total = iv.mpf(0)
    nsteps = 0
    min_ell = mp.inf
    t_start = time.time()
    cur = corners[edge_only if edge_only is not None else 0]
    Wcur = lam_c(cpt(*cur))
    W0 = Wcur
    for edge in ([edge_only] if edge_only is not None else range(4)):
        tgt = corners[(edge + 1) % 4]
        dx = tgt[0] - cur[0]
        dy = tgt[1] - cur[1]
        elen = Fr(abs(dx) + abs(dy))          # one of them is 0
        pos = Fr(0)
        while pos < elen:
            ell = Wcur.abs_lo()
            assert ell > 0, "enclosure touches 0"
            if ell < min_ell:
                min_ell = ell
            h = mp.mpf('0.8') * ell / M
            hf = Fr(mp.nstr(h, 12)).limit_denominator(10 ** 12)
            if hf <= 0:
                hf = Fr(1, 10 ** 12)
            if pos + hf > elen:
                hf = elen - pos
            pos += hf
            u = pos / elen
            nxt = (cur[0] + dx * u, cur[1] + dy * u)
            Wnxt = lam_c(cpt(*nxt))
            ratio = cdiv(Wnxt, Wcur)
            assert mp.mpf(ratio.re.a) > 0, "ratio not in right half-plane"
            total = total + iv.atan2(ratio.im, ratio.re)
            Wcur = Wnxt
            nsteps += 1
            if nsteps % 200 == 0:
                say(f"  step {nsteps}: edge {edge}, pos {float(u):.3f}, "
                    f"ell~{mp.nstr(ell, 3)}, "
                    f"{(time.time()-t_start):.0f}s")
        cur = tgt
    if edge_only is not None:
        e = edge_only
        start = corners[e]
        out = {"edge": e,
               "start": [str(start[0]), str(start[1])],
               "end": [str(cur[0]), str(cur[1])],
               "sum_lo": mp.nstr(mp.mpf(total.a), 40),
               "sum_hi": mp.nstr(mp.mpf(total.b), 40),
               "steps": nsteps,
               "min_ell": mp.nstr(min_ell, 8),
               "rh_established": False}
        json.dump(out, open(f'epstein/wall_complex2_edge{e}.json', 'w'),
                  indent=1)
        say(f"steps: {nsteps}; min ell: {mp.nstr(min_ell, 4)}")
        say(f"EDGE {e} DONE")
        return None
    # close the loop: last Wcur is at corner 0 again (pos wrapped)
    ratio = cdiv(W0, Wcur)
    assert mp.mpf(ratio.re.a) > 0
    total = total + iv.atan2(ratio.im, ratio.re)
    w = total / (2 * iv.pi)
    say(f"steps: {nsteps}; min ell: {mp.nstr(min_ell, 4)}")
    say(f"winding interval: [{mp.nstr(mp.mpf(w.a), 10)}, "
        f"{mp.nstr(mp.mpf(w.b), 10)}]")
    lo, hi = mp.mpf(w.a), mp.mpf(w.b)
    k = int(mp.nint(lo))
    pinned = (abs(lo - k) < mp.mpf('0.4') and abs(hi - k) < mp.mpf('0.4')
              and k == int(mp.nint(hi)))
    return k, pinned, nsteps, min_ell, (str(lo), str(hi))


# ---------------- validations and main ------------------------------

def validate():
    say("validations:")
    spouge_init()
    # Spouge vs mp.gamma
    for zz in [mp.mpf('0.7'), mp.mpc('0.9', '12.3')]:
        g = gamma_c(C(iv.mpf(mp.nstr(mp.re(zz), 25)),
                      iv.mpf(mp.nstr(mp.im(zz), 25))))
        ref = mp.gamma(zz)
        err = abs(mp.mpc(mp.mpf(g.re.mid), mp.mpf(g.im.mid)) - ref)
        say(f"  Spouge vs gamma at {zz}: |diff| = {mp.nstr(err, 3)}")
        assert err < mp.mpf('1e-20')
    # incomplete gamma vs mp.gammainc (both branches)
    for (sr, si, xx) in [(0.9, 12.3, 2.1), (0.9, 12.3, 40.0),
                         (0.1, -12.3, 5.0)]:
        s = C(iv.mpf(mp.nstr(mp.mpf(sr), 25)),
              iv.mpf(mp.nstr(mp.mpf(si), 25)))
        xiv = iv.mpf(mp.nstr(mp.mpf(xx), 25))
        gs = gamma_c(s)
        g = gamma_upper_c(s, xiv, gs, iv.log(xiv))
        ref = mp.gammainc(mp.mpc(sr, si), mp.mpf(xx))
        err = abs(mp.mpc(mp.mpf(g.re.mid), mp.mpf(g.im.mid)) - ref)
        say(f"  Gamma(s,x) at ({sr}+{si}i, {xx}): |diff| = "
            f"{mp.nstr(err, 3)}")
        assert err < mp.mpf('1e-20')
    # Lambda midpoint vs float route
    lattice_init()
    s0 = C(rat(9, 10), rat(123, 10))
    L = lam_c(s0)
    x = mp.mpf(XN) / XD
    y = mp.mpf(YN) / YD
    ss = mp.mpc('0.9', '12.3')
    tot = 1 / (ss - 1) - 1 / ss
    zz = x * x + y * y
    for m in range(-25, 26):
        for n in range(-5, 6):
            if m == 0 and n == 0:
                continue
            Q = (m * m + 2 * x * m * n + zz * n * n) / y
            xxv = mp.pi * Q
            if xxv > 110:
                continue
            tot += (xxv ** -ss * mp.gammainc(ss, xxv)
                    + xxv ** (ss - 1) * mp.gammainc(1 - ss, xxv))
    err = abs(mp.mpc(mp.mpf(L.re.mid), mp.mpf(L.im.mid)) - tot)
    say(f"  Lambda(0.9+12.3i) iv-mid vs float: |diff| = "
        f"{mp.nstr(err, 3)} (tail bound {mp.nstr(TAILB, 3)})")
    assert err < 100 * TAILB + mp.mpf('1e-25')


def main():
    validate()
    k, pinned, nsteps, min_ell, wint = walk()
    ok = pinned and k >= 1
    out = {
        "modulus": {"x": f"{XN}/{XD}", "y": f"{YN}/{YD}",
                    "context": "theta80 dirty probe of the C8 "
                               "archipelago campaign, exact-rationalized"},
        "rectangle": {"re": [f"{SLO[0]}/{SLO[1]}", f"{SHI[0]}/{SHI[1]}"],
                      "im": [f"{TLO[0]}/{TLO[1]}", f"{THI[0]}/{THI[1]}"]},
        "winding_interval": list(wint),
        "winding": k, "pinned": pinned, "steps": nsteps,
        "min_contour_enclosure_lower": mp.nstr(min_ell, 8),
        "lattice_tail_bound": mp.nstr(TAILB, 4),
        "float_zero_location": "0.6940279890724 + 18.9467935267590 i",
        "conclusion": (f"Z_Q has {k} zero(s) in the rectangle; its left "
                       "edge Re s = 62/100 > 1/2: a PROVED complex "
                       "off-critical-line zero at an exact archipelago-"
                       "adjacent modulus." if ok else "NOT ESTABLISHED"),
        "verified": bool(ok),
        "rh_established": False,
    }
    json.dump(out, open('epstein/wall_complex2.json', 'w'), indent=1)
    say("VERIFIED winding = " + str(k) if ok else "NOT VERIFIED")
    return 0 if ok else 1


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:          # single-edge worker mode
        validate()
        walk(int(sys.argv[1]))
        raise SystemExit(0)
    raise SystemExit(main())
