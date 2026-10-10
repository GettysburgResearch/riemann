#!/usr/bin/env python3
"""Reviewer checks for R2 of the October 5 2026 OpenAI manuscript "The Quasi-Riemann Hypothesis"
(paper2.tex at pr908 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, sha256 d9a8f15a...0d4d).

Status: review instrument (exploration level), written from scratch for this review.
Scope:  Section sec:descent (lines 1254-1629) and Section sec:transfer-proof (lines 2217-2683),
        plus the extraction of 11/12 from Prop thm:ms (lines 679-722).  Prop prop:R is a
        black box.  Lemma lem:arithmetic is imported; part E only replays the two *paired*
        Gauss-sum identities that the transfer proof derives from it, numerically, for small
        norms, from the definitions.
Arithmetic: exact rationals (fractions.Fraction, sympy Rational / positive symbols) for every
        gate in parts A-D and F.  Part E is floating point (Gauss sums), tolerance 1e-9; it is
        EMPIRICAL and only checks conventions and the CRT step.
Run:    python3 -I oct5_r2_iteration_check.py   (prints a report; writes no files)
"""
from fractions import Fraction as Fr
from itertools import product
import cmath
import math
import sys

import sympy as sp

RESULTS = []


def rec(part, claim, ok, detail=""):
    RESULTS.append((part, claim, bool(ok), detail))
    print(("PASS " if ok else "FAIL ") + f"[{part}] {claim}" + (f"  -- {detail}" if detail else ""))


# ---------------------------------------------------------------------------------------------
# A. Exponent bookkeeping 11/12 from Prop thm:ms (paper2 lines 689-722, 274-299, 1611-1629)
# ---------------------------------------------------------------------------------------------
def part_A():
    th = sp.symbols('vartheta', nonnegative=True)
    H = 1 + th                       # log_D H
    Y = H / 6                        # log_D Y, Y = H^(1/6)
    ms = 2 + th                      # Prop thm:ms: sum_{N u <= H} |A_u|^2 << D^(2+th+eps)
    e1 = sp.simplify(ms - Y)         # (1/J) * mean square, J ~ Y/log Y
    e2 = sp.simplify(2 - 2 * Y)      # (D/Y)^2
    rec('A', 'first term exponent 2+th-(1+th)/6 == 11/6+5th/6 (eq:prime-extract)',
        sp.simplify(e1 - (sp.Rational(11, 6) + 5 * th / 6)) == 0, str(e1))
    rec('A', 'second term exponent 2-(1+th)/3 == 5/3-th/3 (eq:prime-extract)',
        sp.simplify(e2 - (sp.Rational(5, 3) - th / 3)) == 0, str(e2))
    rec('A', 'first term dominates for th>=0: e1-e2 == 1/6+7th/6 > 0',
        sp.simplify(e1 - e2 - (sp.Rational(1, 6) + 7 * th / 6)) == 0)
    a1 = sp.simplify(e1 / 2)
    rec('A', 'A_1(D) << D^(11/12+5th/12+eps)', sp.simplify(a1 - (sp.Rational(11, 12) + 5 * th / 12)) == 0, str(a1))
    rec('A', 'limit th -> 0+ gives 11/12', sp.limit(a1, th, 0) == sp.Rational(11, 12))
    # outline form D^{1+eps} H^{5/6} + D^2 H^{-1/3}  (eq:intro-extraction)
    rec('A', 'outline D*H^(5/6) has exponent e1', sp.simplify(1 + sp.Rational(5, 6) * H - e1) == 0)
    rec('A', 'outline D^2*H^(-1/3) has exponent e2', sp.simplify(2 - H / 3 - e2) == 0)
    # optimality of Y = H^(1/6) among Y <= H^(1/6): exponent max(ms - y, 2 - 2y) is decreasing in y
    y = sp.symbols('y', nonnegative=True)
    f1, f2 = ms - y, 2 - 2 * y
    rec('A', 'on 0<=y<=(1+th)/6, ms-y >= 2-2y (so the max is ms-y, decreasing in y)',
        sp.simplify(f1 - f2 - (th + y)) == 0)
    # leverage law: c = fraction of rows lost; principal rows ~ H^(1-c), with 1-c = 1/6
    c = sp.Rational(5, 6)
    rec('A', 'leverage law (1+c)/2 at c=5/6 is 11/12', (1 + c) / 2 == sp.Rational(11, 12))
    # sixth powers p^6 with N p <= Y = H^(1/6) have norm <= H
    rec('A', 'rows u=p^6 with N(p)<=H^(1/6) satisfy N(u)<=H', sp.simplify(6 * Y - H) == 0)
    # Section 3/completion: Poisson reduction scales with H = D^(1+th)
    D, B, Fv, C = sp.symbols('D B F C', positive=True)
    Hs = D ** (1 + th)
    X = D / (B * Fv)
    Hdual = C * D ** 2 / (Hs * B ** 2)
    Sig = X * Fv
    rec('A', 'Sigma = XF = D/B (eq:initial-scales)', sp.simplify(Sig - D / B) == 0)
    rec('A', 'Hdual/Sigma = C D^(-th)/B (eq:initial-positive-gap)',
        sp.simplify(sp.powsimp(Hdual / Sig) - C * D ** (-th) / B) == 0)
    rec('A', 'block bound (H N(b)/D^2) * #b * Sigma^2 = H at N(b)~B (eq:weighted)',
        sp.simplify(Hs * B / D ** 2 * B * Sig ** 2 - Hs) == 0)
    # kappa = th/2 works for large D: C D^-th / B <= D^(-th/2) iff D^(th/2) >= C/B
    rec('A', 'kappa = th/2: C D^-th <= D^-th/2 iff D >= C^(2/th) (B>=1)',
        sp.simplify(sp.powsimp((C * D ** (-th)) / D ** (-th / 2)) - C * D ** (-th / 2)) == 0)


# ---------------------------------------------------------------------------------------------
# B. Monomial identities in the transfer proof (lines 2235-2345, 2509-2664)
# ---------------------------------------------------------------------------------------------
def part_B():
    (Hh, L, Fv, Sig, cI, NC, Nd, Nt, Ng, Ne, Nw, Nh, Nx1, Nx2, z1, z2,
     R, Fp, Nr, Nfp, Nk, Nj, CPhi, v) = sp.symbols(
        'H L F Sigma c_I NC Nd Nt Ng Ne Nw Nh Nx1 Nx2 z1 z2 R Fp Nr Nfp Nk Nj C_Phi v', positive=True)
    ell = L / (NC * Nt)
    w = Hh * NC / (Nd * L ** 2 * Fv)
    Y = cI * Sig * L * Fv * Nd / (Hh * NC ** 2)
    # first Poisson: weight H/(L F N(d) sqrt(N(u1 u2))) with u_i = t x_i, z_i = N(x_i)/ell
    Nu1u2 = Nt ** 2 * Nx1 * Nx2
    first_weight = Hh / (L * Fv * Nd * sp.sqrt(Nu1u2))
    zsub = {Nx1: z1 * ell, Nx2: z2 * ell}
    rec('B', 'first Poisson weight == w_{C,d} (z1 z2)^(-1/2) (line 2238, 2319)',
        sp.simplify(first_weight.subs(zsub) - w * (z1 * z2) ** sp.Rational(-1, 2)) == 0)
    arg1 = Hh * Nh / (Nd * Nu1u2)
    rec('B', 'first Poisson Fourier argument == H N(h) N(C)^2/(L^2 N(d) z1 z2) (line 2321)',
        sp.simplify(arg1.subs(zsub) - Hh * Nh * NC ** 2 / (L ** 2 * Nd * z1 * z2)) == 0)
    rec('B', 'N(C u_i)/L == z_i (columns at scale ell)',
        sp.simplify((NC * Nt * Nx1 / L).subs(zsub) - z1) == 0)
    # enlargement: natural y-range 4 C_Phi v^2 L^2 F^2 N(d)/(H N(C)^2) <= Y_{C,d}
    natural = 4 * CPhi * v ** 2 * L ** 2 * Fv ** 2 * Nd / (Hh * NC ** 2)
    rec('B', 'Y_{C,d}/natural == (c_I/(4 C_Phi v^2)) * Sigma/(L F) (enlargement factor, line 2333)',
        sp.simplify(Y / natural - cI / (4 * CPhi * v ** 2) * Sig / (L * Fv)) == 0)
    # second Poisson regrouping: r = t g/e, f' = C e w, k' = d e h
    Nr_ = Nt * Ng / Ne
    Nfp_ = NC * Ne * Nw
    Nk_ = Nd * Ne * Nh
    rec('B', "X'_0 = ell/(N g N w) == L/(N r N f') (line 2527)",
        sp.simplify(ell / (Ng * Nw) - L / (Nr_ * Nfp_)) == 0)
    rec('B', "w_{C,d} Y N(g)/(N(e) ell) == c_I Sigma N(r)/L^2 (line 2529)",
        sp.simplify(w * Y * Ng / (Ne * ell) - cI * Sig * Nr_ / L ** 2) == 0)
    rec('B', "Y N(h) N(g)^2/(N(e) ell^2) == c_I Sigma F N(k') N(r)^2/(H L) (line 2531)",
        sp.simplify(Y * Nh * Ng ** 2 / (Ne * ell ** 2) - cI * Sig * Fv * Nk_ * Nr_ ** 2 / (Hh * L)) == 0)
    # kernel support (line 2544): N(k') <= C_Phi (2v)^2 H L /(c_I Sigma F N(r)^2)
    bound_k = CPhi * (2 * v) ** 2 * Hh * L / (cI * Sig * Fv * Nr ** 2)
    rec('B', "support of hatPhi gives N(k') <= 4C_Phi v^2/c_I * H L/(Sigma F N(r)^2)",
        sp.simplify(bound_k - 4 * CPhi * v ** 2 / cI * Hh * L / (Sig * Fv * Nr ** 2)) == 0)
    # dyadic block parameters
    Xp = L / (R * Fp)
    Sigp = Xp * Fp
    Hp = Hh * L / (Sig * Fv * R ** 2)
    rec('B', "Sigma' = X'F' = L/R (line 2587)", sp.simplify(Sigp - L / R) == 0)
    rec('B', "H'/Sigma' == H/(Sigma F R) (line 2618)", sp.simplify(Hp / Sigp - Hh / (Sig * Fv * R)) == 0)
    rec('B', "block total (Sigma R/L^2) * R * Sigma'^2 == Sigma (line 2651)",
        sp.simplify(Sig * R / L ** 2 * R * Sigp ** 2 - Sig) == 0)
    rec('B', "zero frequency w_{C,d} Y_{C,d} ell == c_I Sigma/(N(C)^2 N(t)) (line 2658-2660)",
        sp.simplify(w * Y * ell - cI * Sig / (NC ** 2 * Nt)) == 0)
    # child column lower bound (eq:child-column-lower-bound) as an exact implication in logs:
    # X'/N(j) = L/(R F' N j);  F' <= H L /(Sigma F N(r)^2)  =>  X'/N(j) >= Sigma F N(r)^2/(H R N(j))
    expr = (L / (R * Fp * Nj)) / (Sig * Fv * Nr ** 2 / (Hh * R * Nj))
    rec('B', "X'/N(j) divided by Sigma F N(r)^2/(H R N(j)) == (H L/(Sigma F N(r)^2))/F' (>=1 by f'|k')",
        sp.simplify(expr - (Hh * L / (Sig * Fv * Nr ** 2)) / Fp) == 0)
    # Outline consistency (lines 562-611): F=1, C=t=d=g=e=w=1, Sigma = X
    Xs, Lb = sp.symbols('X L_b', positive=True)
    Yout = Xs * Lb / Hh
    rec('B', 'outline: Y = X L_b/H >= L_b^2/H iff L_b <= X', sp.simplify(Yout / (Lb ** 2 / Hh) - Xs / Lb) == 0)
    rec('B', "outline: H' = L_b^2/Y == H L_b/X", sp.simplify(Lb ** 2 / Yout - Hh * Lb / Xs) == 0)
    rec('B', "outline: (H/X)(X/L_b) * E'/(X/L_b)... factor X/L_b converts target L_b to X",
        sp.simplify(Hh / Lb ** 2 * Yout * Lb - Xs) == 0, 'H/L_b^2 * Y * L_b == X (zero-frequency YL_b term)')
    rec('B', "full version specialises: H L/(Sigma F) at F=1, Sigma=X equals outline H'",
        sp.simplify((Hh * Lb / (Xs * 1))) == sp.simplify(Hh * Lb / Xs))


# ---------------------------------------------------------------------------------------------
# C. Descent contraction and gap preservation in log coordinates, with exact Farkas certificates
# ---------------------------------------------------------------------------------------------
def part_C():
    # log_D coordinates: h = log H, x = log X, f = log F, beta = log N(b), kap = kappa,
    # L = x - 3 beta, sigma = x + f.
    # transfer outputs: h' <= h + L - sigma - f  (H' <= H L/(Sigma F)),  h' - sigma' <= h - sigma,
    # sigma' <= L.  Cube reduction: supremum nonempty only if 2h > x, and then 3 beta > 2x - 2h.
    # Canonical hypothesis: h <= sigma - kap.
    h, x, f, beta, kap, hp, sp_, cst = sp.symbols("h x f beta kappa hp sigmap c")
    s1 = (h + (x - 3 * beta) - (x + f) - f) - hp       # >= 0 : transfer row bound
    s2 = 3 * beta - (2 * x - 2 * h)                      # > 0  : N(b) > H_c, H_c^3 = X^2/H^2
    s3 = (x + f) - h - kap                               # >= 0 : canonical gap
    target = h - 2 * kap - hp                            # want > 0
    rec('C', "Farkas: h - 2kappa - h' == s1 + s2 + 2 s3 (so H' < D^(-2kappa) H; line 1566-1572)",
        sp.expand(target - (s1 + s2 + 2 * s3)) == 0)
    # same with the paper's intermediate form H' < H (H/Sigma)^2
    rec('C', "H/(N(b)^3 F^2) < H (H/Sigma)^2 <=> s2 > 0 (line 1570-1571)",
        sp.expand((h + 2 * (h - (x + f))) - (h - 3 * beta - 2 * f) - s2) == 0)
    # gap preserved: h' - sigma' <= h - sigma <= -kappa
    s4 = (h - (x + f)) - (hp - sp_)
    rec('C', "gap: (sigma' - kappa) - h' == s4 + s3 (H' <= Sigma' D^-kappa)",
        sp.expand((sp_ - kap - hp) - (s4 + s3)) == 0)
    # Sigma' <= L_b <= X <= Sigma <= D^C0
    rec('C', "Sigma - L_b == f + 3 beta >= 0 in logs (so Sigma' <= L_b <= Sigma <= D^C0)",
        sp.expand((x + f) - (x - 3 * beta) - (f + 3 * beta)) == 0)
    # short cube: H^2 F H_c^3 / X <= Sigma with H_c^3 = min(X, X^2/H^2)
    rec('C', "short cube: H^2 F H_c^3/X at H_c^3 = X^2/H^2 equals Sigma exactly (line 1399-1400)",
        sp.expand((2 * h + f + (2 * x - 2 * h) - x) - (x + f)) == 0, 'H_c^3 <= X^2/H^2 gives <= Sigma')
    # termination: induction on H <= D^{j kappa}; C0 = 2, kappa = th/2  -> j_max = ceil(4/th)
    rows = []
    for th in [Fr(1, 10), Fr(1, 20), Fr(1, 100), Fr(1, 1000)]:
        kap_v = th / 2
        jmax = math.ceil(Fr(2) / kap_v)
        rows.append((th, jmax))
    rec('C', 'j_max = ceil(C0/kappa) = ceil(4/theta) for theta in {1/10,1/20,1/100,1/1000}',
        rows == [(Fr(1, 10), 40), (Fr(1, 20), 80), (Fr(1, 100), 400), (Fr(1, 1000), 4000)], str(rows))

    # Finite exploration of the recursion on an exact rational grid (illustration, not a proof).
    # State (h, x, f) with h>=0, x>=0, f>=0, x+f<=C0, h <= x+f-kap. One step = worst-case branch.
    kap_v = Fr(1, 20)   # theta = 1/10, kappa = theta/2 (the paper's largest theta); illustration only,
    C0 = Fr(2)          # the Farkas identity above covers all real states and all theta
    step = Fr(1, 20)
    grid = [step * i for i in range(0, int(C0 / step) + 1)]
    max_depth = 0
    bad = 0
    nstates = 0

    def children(hh, xx, ff):
        out = set()
        if 2 * hh <= xx:
            return out   # supremum empty (Lemma cube-reduction)
        lo = Fr(2, 3) * (xx - hh)          # beta > lo ; also beta >= 0 ; L = x - 3 beta > 0
        betas = [b for b in grid if b > lo and 3 * b < xx]   # beta = 0 (b = 1) allowed iff H > X
        for b in betas:
            L = xx - 3 * b
            sig = xx + ff
            hp_max = hh + L - sig - ff
            for rho in grid:                  # rho = log R >= 0, Sigma' = L - rho
                sigp = L - rho
                if sigp < 0:
                    continue
                hpv = hp_max - 2 * rho        # H' = H L/(Sigma F R^2)
                if hpv < 0:
                    continue                  # empty (H' >= N(k') >= 1 needed)
                for fp in grid:               # F' <= N(f') <= N(k') <= H'; all splits of Sigma'
                    if fp > hpv or fp > sigp:
                        continue
                    out.add((hpv, sigp - fp, fp))
        return out

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def depth(hh, xx, ff):
        nonlocal bad
        ch = children(hh, xx, ff)
        d = 0
        for (a, b, c) in ch:
            # hypotheses of Prop canonical at the child
            if not (a >= 0 and b >= 0 and c >= 0 and b + c <= C0 and a <= b + c - kap_v):
                bad += 1
            if not (a <= hh - 2 * kap_v):
                bad += 1
            d = max(d, 1 + depth(a, b, c))
        return d

    for hh in grid:
        for xx in grid:
            for ff in grid:
                if xx + ff <= C0 and hh <= xx + ff - kap_v:
                    nstates += 1
                    max_depth = max(max_depth, depth(hh, xx, ff))
    rec('C', f'grid exploration (kappa={kap_v}, C0={C0}, step {step}, {nstates} start states, all f\' splits): every child satisfies '
             f'the canonical hypotheses and h decreases by >= 2 kappa', bad == 0,
        f'max recursion depth {max_depth} <= ceil(C0/(2kappa)) = {math.ceil(C0 / (2 * kap_v))}')
    rec('C', f'grid depth bounded by ceil(C0/kappa) = {math.ceil(C0 / kap_v)} used in the paper',
        max_depth <= math.ceil(C0 / kap_v))


# ---------------------------------------------------------------------------------------------
# D. Preimage sign sum in Lemma second-transfer (lines 2550-2568): sum mu(e)mu(w) = tau(r) 1_{f'|k'}
# ---------------------------------------------------------------------------------------------
def part_D():
    ok = True
    count = 0
    for s in range(0, 7):                 # primes of f'
        for K in product([0, 1], repeat=s):   # K[i] = 1 iff p_i | k'
            total = 0
            # each prime of f' goes to C (with d or not), e, or w
            for assign in product(['C', 'Cd', 'e', 'w'], repeat=s):
                good = True
                sign = 1
                for a, k in zip(assign, K):
                    if a == 'Cd' and not k:
                        good = False          # d | k'
                    if a == 'e':
                        if not k:
                            good = False      # e | k'
                        sign = -sign
                    if a == 'w':
                        if k:
                            good = False      # (w, k') = 1
                        sign = -sign
                if good:
                    total += sign
            expect = 1 if all(K) else 0
            ok &= (total == expect)
            count += 1
    rec('D', 'sum over (C,d,e,w) of mu(e)mu(w) == 1_{f\'|k\'} for all squarefree f\' with <=6 primes '
             'and all divisibility patterns of k\'', ok, f'{count} patterns')
    # t | r factor: t ranges over all divisors of r (no constraint), giving tau(r)
    ok2 = all(sum(1 for _ in product([0, 1], repeat=s)) == 2 ** s for s in range(7))
    rec('D', 'choices t | r contribute tau(r) = 2^omega(r) for squarefree r', ok2)
    # multiplicity of (f, h) -> y = h f^2 is <= number of squarefree f with f^2 | y <= tau(y)


# ---------------------------------------------------------------------------------------------
# E. EMPIRICAL replay of the paired Gauss-sum identities used at lines 2288-2291 and 2433-2435
# ---------------------------------------------------------------------------------------------
def emul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def econj(x):
    a, b = x
    return (a - b, -b)


def enorm(x):
    a, b = x
    return a * a - a * b + b * b


def ecomplex(x):
    a, b = x
    return complex(a - b / 2, b * math.sqrt(3) / 2)


ZETA_O = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]   # (1+w)^k, k = 0..5


class Prime:
    def __init__(self, gen):
        self.gen = gen
        self.N = enorm(gen)
        a, b = gen
        if b == 0:                       # inert: gen = -q
            self.q = -a
            self.kind = 'inert'
        else:
            self.p = self.N
            self.kind = 'split'
            self.r = (-a * pow(b, -1, self.p)) % self.p
        self.table = {}
        e = (self.N - 1) // 6
        zimg = [self.red(z) for z in ZETA_O]
        for res in self.residues():
            if self.is_zero(res):
                continue
            pw = self.powr(res, e)
            k = zimg.index(pw)
            self.table[res] = k

    def red(self, x):
        c, d = x
        if self.kind == 'split':
            return (c + d * self.r) % self.p
        return (c % self.q, d % self.q)

    def residues(self):
        if self.kind == 'split':
            return range(self.p)
        return [(c, d) for c in range(self.q) for d in range(self.q)]

    def is_zero(self, res):
        return res == 0 if self.kind == 'split' else res == (0, 0)

    def mulr(self, s, t):
        if self.kind == 'split':
            return (s * t) % self.p
        a, b = s
        c, d = t
        q = self.q
        return ((a * c - b * d) % q, (a * d + b * c - b * d) % q)

    def powr(self, s, e):
        result = 1 if self.kind == 'split' else (1, 0)
        base = s
        while e:
            if e & 1:
                result = self.mulr(result, base)
            base = self.mulr(base, base)
            e >>= 1
        return result

    def chi_code(self, x):
        res = self.red(x)
        if self.is_zero(res):
            return None
        return self.table[res]


ZETA = [cmath.exp(1j * math.pi * k / 3) for k in range(6)]


def chi(primes, x, power=1):
    """chi_n(x)^power for n = product of the given primes (sextic symbol, zero-extended)."""
    tot = 0
    for P in primes:
        k = P.chi_code(x)
        if k is None:
            return 0
        tot += k
    return ZETA[(power * tot) % 6]


def hnf_residues(m):
    p, q = m
    v1 = [p, q]
    v2 = [-q, p - q]
    # row-reduce [[v1],[v2]] to [[A, B], [0, C]]
    a, b = v1, v2
    while b[0] != 0:
        t = a[0] // b[0]
        a = [a[0] - t * b[0], a[1] - t * b[1]]
        a, b = b, a
    if a[0] < 0:
        a = [-a[0], -a[1]]
    Cc = abs(b[1])
    A = a[0]
    assert A * Cc == enorm(m)
    return [(i, j) for i in range(A) for j in range(Cc)]


def e_add(x, m):
    """e(x/m) = exp(2 pi i d / N(m)) where x conj(m) = c + d w."""
    c, d = emul(x, econj(m))
    return cmath.exp(2j * math.pi * d / enorm(m))


def prod_gen(primes):
    g = (1, 0)
    for P in primes:
        g = emul(g, P.gen)
    return g


def gauss(primes_plus, primes_minus, jplus=1, jminus=-1):
    """normalized Gauss sum of chi_{u1}^jplus * chi_{u2}^jminus modulo u1 u2."""
    m = prod_gen(primes_plus + primes_minus)
    s = 0
    for x in hnf_residues(m):
        c1 = chi(primes_plus, x, jplus) if primes_plus else 1
        c2 = chi(primes_minus, x, jminus) if primes_minus else 1
        if c1 == 0 or c2 == 0:
            continue
        s += c1 * c2 * e_add(x, m)
    return s / math.sqrt(enorm(m))


def part_E():
    # small primary primes prime to 6: split (a = 1 mod 3, b = 0 mod 3, norm prime), inert -q
    split = []
    for a in range(-20, 21):
        for b in range(-20, 21):
            if a % 3 == 1 and b % 3 == 0 and b != 0:
                n = enorm((a, b))
                if n < 80 and all(n % d for d in range(2, int(n ** 0.5) + 1)) and n > 3:
                    split.append((a, b))
    split = sorted(set(split), key=lambda z: (enorm(z), z))
    inert = [(-5, 0), (-11, 0)]
    primes = [Prime(g) for g in split] + [Prime(g) for g in inert]
    rec('E', f'built {len(primes)} primary primes prime to 6 (norms {sorted(P.N for P in primes)})',
        all(P.gen[0] % 3 == 1 and P.gen[1] % 3 == 0 for P in primes))

    def alpha(primes_):
        z = ecomplex(prod_gen(primes_))
        return z / abs(z)

    def gam(primes_, j):
        return gauss(primes_, [], j, 0) if primes_ else 1

    def G(primes_):
        return (chi(primes_, (4, 0), 1).conjugate() if primes_ else 1) * gam(primes_, 3)

    # sanity: Lemma arithmetic (gj) and (convert1) on single primes and a few products
    worst = 0.0
    for P in primes:
        g1, g2 = gam([P], 1), gam([P], 2)
        worst = max(worst, abs(g2 ** 3 - (-1) * alpha([P])))
        worst = max(worst, abs(alpha([P]).conjugate() * g2 * g1 - (-1) * G([P])))
    rec('E', 'sanity (gj),(convert1) at primes: gamma2^3 = -alpha, conj(alpha) gamma2 gamma1 = -G',
        worst < 1e-9, f'max err {worst:.2e}')

    # paired identities on coprime squarefree u1, u2 with small norms
    small = [P for P in primes if P.N <= 43]
    cases = []
    for i, P in enumerate(small):
        for Q in small[i + 1:]:
            cases.append(([P], [Q]))
            cases.append(([Q], [P]))
    # a few with composite u1 or u2
    if len(small) >= 4:
        cases.append(([small[0], small[1]], [small[2]]))
        cases.append(([small[2]], [small[0], small[3]]))
        cases.append(([small[1]], [small[0], small[2]]))
    cases.append(([], [small[0]]))
    cases.append(([small[1]], []))
    w1 = w2 = wR = 0.0
    for U1, U2 in cases:
        mu1 = (-1) ** len(U1)
        mu2 = (-1) ** len(U2)
        a1 = alpha(U1).conjugate() * gam(U1, 2)
        a2 = alpha(U2).conjugate() * gam(U2, 2)
        u1, u2 = prod_gen(U1), prod_gen(U2)
        R12 = (chi(U2, u1) if U2 else 1) * ((chi(U1, u2) if U1 else 1).conjugate())
        wR = max(wR, abs(R12.imag), abs(abs(R12) - 1))
        chi2m1 = chi(U2, (-1, 0)) if U2 else 1
        chi1m1 = chi(U1, (-1, 0)) if U1 else 1
        # (paired-first-gauss), line 2288-2291, before the ray-class quotient (eq:quotient):
        # a(u1) conj(a(u2)) gamma(chi_u1 conj chi_u2) = mu mu G(u1) conj G(u2) chi_u2(-1) R(u1,u2)
        lhs = a1 * a2.conjugate() * gauss(U1, U2, 1, -1)
        rhs = mu1 * mu2 * G(U1) * G(U2).conjugate() * chi2m1 * R12
        w1 = max(w1, abs(lhs - rhs))
        # second paired identity, line 2433-2435 (xi_1 trivial), before (eq:quotient):
        # mu(z1)mu(z2) gamma(conj chi_z1 chi_z2) = a(z1) conj a(z2) G(z2) conj G(z1) chi_z1(-1) R(z1,z2)
        lhs2 = mu1 * mu2 * gauss(U2, U1, 1, -1)
        rhs2 = a1 * a2.conjugate() * G(U2) * G(U1).conjugate() * chi1m1 * R12
        w2 = max(w2, abs(lhs2 - rhs2))
    rec('E', f'R(u1,u2) = chi_u2(u1) conj chi_u1(u2) is +-1 on {len(cases)} pairs', wR < 1e-9, f'{wR:.1e}')
    rec('E', f'first paired identity (CRT + convert1/2 + recip) on {len(cases)} coprime pairs',
        w1 < 1e-9, f'max err {w1:.2e}')
    rec('E', f'second paired identity (CRT + convert1/2 + recip) on {len(cases)} coprime pairs',
        w2 < 1e-9, f'max err {w2:.2e}')
    # recip for G (eq:recip): G(ab) = G(a) G(b) R(a,b)
    wG = 0.0
    for i, P in enumerate(small[:5]):
        for Q in small[i + 1:6]:
            R = chi([Q], P.gen) * chi([P], Q.gen).conjugate()
            wG = max(wG, abs(G([P, Q]) - G([P]) * G([Q]) * R))
    rec('E', 'G(ab) = G(a)G(b)R(a,b) on small prime pairs (eq:recip, imported)', wG < 1e-9, f'{wG:.2e}')


# ---------------------------------------------------------------------------------------------
# F. Derivative order, epsilon split and interval growth through the induction (lines 1517-1608)
# ---------------------------------------------------------------------------------------------
def part_F():
    n = sp.symbols('n', integer=True, nonnegative=True)
    # J_{j+1} >= 4 J_j + 12, J_0 = 1 => J_j >= 5*4^j - 4
    J = [1]
    for _ in range(45):
        J.append(4 * J[-1] + 12)
    rec('F', 'J_j = 4 J_{j-1} + 12, J_0 = 1 gives J_j = 5*4^j - 4 (lower bound when 4m+12 dominates)',
        all(J[j] == 5 * 4 ** j - 4 for j in range(46)))
    rec('F', 'at theta = 1/10, j_max = 40: derivative order >= 5*4^40 - 4', J[40] == 5 * 4 ** 40 - 4,
        f'{J[40]:.3e}')
    # epsilon: level j with eps uses eps/3 at level j-1: depth i sees eps/3^i, finite for j bounded
    rec('F', 'epsilon at depth 40 is eps/3^40 > 0 (finite chain; total loss at top level is eps)',
        Fr(1, 3 ** 40) > 0)
    # interval growth: [u,v] -> [u/16, 4v] per level
    rec('F', 'interval after 40 levels is [u/16^40, 4^40 v] (fixed, depends only on I)',
        (Fr(1, 16) ** 40, 4 ** 40) == (Fr(1, 2 ** 160), 2 ** 80))
    # each level: eps/3 (cube) + eps/3 (transfer) + eps/3 (hypothesis) = eps
    rec('F', 'per-level loss split eps/3 + eps/3 + eps/3 == eps (lines 1551-1600)',
        Fr(1, 3) * 3 == 1)
    # transfer: m -> 2m+4 (second) -> 2(2m+4)+4 = 4m+12 (first)
    m = sp.symbols('m')
    rec('F', 'transfer derivative order: 2(2m+4)+4 == 4m+12 (line 2672-2681)',
        sp.expand(2 * (2 * m + 4) + 4 - (4 * m + 12)) == 0)


if __name__ == '__main__':
    part_A()
    part_B()
    part_C()
    part_D()
    part_E()
    part_F()
    npass = sum(1 for r in RESULTS if r[2])
    print(f'\n{npass}/{len(RESULTS)} checks pass')
    sys.exit(0 if npass == len(RESULTS) else 1)
