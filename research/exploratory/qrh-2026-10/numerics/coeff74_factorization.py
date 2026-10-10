"""
coeff74_factorization.py -- finite check that the coefficient (7.4) of the OpenAI
"Quasi-Riemann Hypothesis" manuscript (30 Sep 2026; external, unreviewed) factors
into the local summands of the series (7.10), through (7.1), (7.9), the b_*/xi/tau
cancellation and the pair-phase cancellation of Section 7.2.

Status: FLOATING_RECONNAISSANCE.  Sextic and cubic symbols are exact (integer
arithmetic in O = Z[omega], tables validated against a2/eis.py:sym_prime).  Gauss
sums, Gamma, tau, gamma_j are ordinary double-precision sums of roots of unity; they
are NOT directed or certified.  A finite check is not a proof.

Source: paper.tex at git object pr908 (31c706bb...), path
  standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
  The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex
  sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3.
Formulas were transcribed from the TeX (the PDF text layer drops overbars).

Objects (manuscript labels; equation numbers of Section 7 in brackets)
  e(z) = exp(4 pi i Im z / sqrt 3); primary = 1 mod 3; chi_p(a) = a^{(Np-1)/6} mod p,
  chi_c = prod chi_p^{v_p(c)}, powers with exponent = 0 mod 6 mean 1[(a,c)=1].
  g_psi(c,k) = sum_{d mod c} psi(d) e(kd/c);  tau = q_{b*}^{-1/2} g_xi(b_*,1);
  Xi(a) = xi(a) chi_a(b_*);  gamma_j(c) = q_c^{-1/2} sum_v chi_c(v)^j e(v/c);
  Gamma(c) = |c|^{-1} sum_{x mod c} e(x^2/c);  G(c) = conj(chi_c(4)) Gamma(c);
  R(a,b) = r(a,b) = Gamma(ab)/(Gamma(a)Gamma(b))  (four-term formula, Lemma 4.3/4.4).
  [7.1]  F(s,A,H) = sum_{d mod s, H = b_*Ad mod s} chi_s(d) g_{xi chi_A}(b_*A, (H-b_*Ad)/s)
  [7.4]  K = F(s,A,ua^6) chi_s(b_*) / (sqrt(q_b*) tau xi(s) conj(xi(u)))
             * gamma_2(c) conj(alpha(A) G(A)) eta(A) Xi(A)^{-1} R(A,s),   A = c n^3
  [7.7]  C_p(t,k,j') = sum_{d mod p^k, p^{j'} = p^t d (p^k)} chi_p^k(d) g_{chi_p^t}(p^t,(p^{j'}-p^t d)/p^k)
  [7.9]  U_p = chi_p^{k-t}(h_p) chi_p^t(s_p) chi_p^{t-k}(A_p^o) chi_p^{t-k}(b_*)
  [7.10] summand at p (coefficient of the Dirichlet monomial):
         kappa_p = (-1)^{e0} gamma_1^{-e0} eta(p)^{e0} (a_p conj(gamma_3))^l rho^{k-t}
                   * omega_p^{tk - e0 l - l(l-1)/2} C_p(t,k,j+6m),
         a_p = conj(alpha(p))^3 eta(p)^3, rho = chi_p(u/p^j), omega_p = chi_p(-1).

Checks
  K   (main)  K_direct(c,n,s,a;u) from [7.4]+[7.1] by brute force  ==  prod_p kappa_p.
  FS  (intermediate) F(s,A,H) == sqrt(q_b*) tau xi(A) conj(xi(H/s)) prod_p U_p C_p
      (the "b_* local factor" sentence and [7.9]).
  C   [7.7] brute force == [7.8] closed form, for every (p,t,k,j') used.
  P1  [7.1] Fourier claim: sum_{m mod sb_*A} xi chi_A(m) q_s^{-1/2} g_{chi_s}(s,-m) e(Hm/(sb_*A))
      == q_s^{1/2} F(s,A,H), every H, small moduli.
  P2  F(s,A,H) = 0 when (H,S) != 1, including H = 0.
  Controls (must FAIL): wrong conjugations, dropped/wrong phases, non-primary generators,
      conjugated additive character.

Run:  nice -n 10 python3 -I coeff74_factorization.py results/coeff74_factorization.json
"""

import cmath
import json
import math
import os
import random
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "a2"))
import eis as E  # noqa: E402  (exact Z[omega] arithmetic; read-only use)

ZETA = np.exp(1j * np.pi * np.arange(6) / 3)        # zeta^k, zeta = 1 + omega
OMEGA_C = complex(-0.5, math.sqrt(3) / 2)
LUT_MAX = 2_000_000
TOL = 1e-8


def to_c(x):
    return complex(x[0] - 0.5 * x[1], x[1] * math.sqrt(3) / 2)


def epow(x, k):
    r = (1, 0)
    for _ in range(k):
        r = E.mul(r, x)
    return r


def neg(x):
    return (-x[0], -x[1])


def exact_div(z, m):
    c, d = E.mul(z, E.conj(m))
    n = E.norm(m)
    assert c % n == 0 and d % n == 0, (z, m)
    return (c // n, d // n)


def residues_np(M):
    """Same residue system as eis.residues, as numpy arrays (x, y) <-> x + y omega."""
    a1, b1 = M
    a2, b2 = E.mul(M, (0, 1))
    N = abs(a1 * b2 - a2 * b1)
    g = math.gcd(b1, b2)
    d1 = N // g
    X = np.tile(np.arange(d1, dtype=np.int64), g)
    Y = np.repeat(np.arange(g, dtype=np.int64), d1)
    return X, Y


def gamma4(c):
    """Four-term formula for Gamma(c), c odd: (1 + i^{-b} + i^a + i^{b-a})/2."""
    a, b = c
    I = [1, 1j, -1, -1j]
    return (1 + I[(-b) % 4] + I[a % 4] + I[(b - a) % 4]) / 2


def r_bichar(x, y):
    return gamma4(E.mul(x, y)) / (gamma4(x) * gamma4(y))


# ---------------------------------------------------------------------------
# exact sextic symbol tables
# ---------------------------------------------------------------------------
class Prime:
    def __init__(self, gen):
        self.gen = gen
        self.N = E.norm(gen)
        if gen[1] == 0:
            self.kind = "inert"
            q = abs(gen[0])
            self.q = q
            tab = np.empty(q * q, dtype=np.int64)
            for x in range(q):
                for y in range(q):
                    k = E.sym_prime((x, y), gen)
                    tab[x * q + y] = -1 if k is None else k
        else:
            self.kind = "split"
            P = self.N
            self.r = next(r for r in range(P) if E.divides(gen, (-r, 1)))
            tab = np.empty(P, dtype=np.int64)
            for x in range(P):
                k = E.sym_prime((x, 0), gen)
                tab[x] = -1 if k is None else k
        self.tab = tab
        self._cache = {}

    def codes(self, X, Y):
        if self.kind == "split":
            idx = np.mod(X + Y * self.r, self.N)
        else:
            idx = np.mod(X, self.q) * self.q + np.mod(Y, self.q)
        return self.tab[idx]

    def code(self, z):
        """exact (z/p)_6 as k (value zeta^k) or None."""
        key = (z[0], z[1])
        if key not in self._cache:
            self._cache[key] = E.sym_prime(z, self.gen)
        return self._cache[key]

    def val(self, z, e=1):
        """chi_p(z)^e with the zero convention."""
        k = self.code(z)
        if k is None:
            return 0j
        return complex(ZETA[(e * k) % 6])


class ModCtx:
    """Residues of O/M and additive characters e(k d / M)."""

    def __init__(self, M):
        self.M = M
        self.N = E.norm(M)
        self.X, self.Y = residues_np(M)
        assert len(self.X) == self.N
        self.cM = E.conj(M)
        self.lut = (np.exp(2j * np.pi * np.arange(self.N) / self.N)
                    if self.N <= LUT_MAX else None)

    def phases(self, k, sign=1):
        N = self.N
        kc = E.mul(k, self.cM)
        w1 = (sign * kc[1]) % N
        w2 = (sign * E.mul(kc, (0, 1))[1]) % N
        ph = (self.X * w1 + self.Y * w2) % N
        if self.lut is not None:
            return self.lut[ph]
        return np.exp(2j * np.pi * ph / N)

    def gsum(self, f, k, sign=1):
        return complex(np.dot(f, self.phases(k, sign)))


# ---------------------------------------------------------------------------
# the arithmetic world: S, b_*, xi, eta, generator normalization
# ---------------------------------------------------------------------------
class World:
    def __init__(self, maxnorm=200, bstar_unit=0, xi2_exp=1, extra_S=(), extra_xi=(),
                 gen_sign=1, eta_seed=12345, esign=1):
        self.esign = esign
        gens = E.primes_upto(maxnorm)
        # extra_S: norms of split primes put into S (both primes of that norm)
        self.S_extra = [g for g in gens if E.norm(g) in extra_S]
        good = [g for g in gens if E.norm(g) not in extra_S]
        self.primes = [Prime(g) for g in good]
        if gen_sign == -1:                      # control: non-primary generators -p
            for P in self.primes:
                P.gen = neg(P.gen)
        self.byname = {}
        for P in self.primes:
            self.byname[self.pname(P)] = P
        self.Sprimes = [Prime(g) for g in self.S_extra]
        # b_* = unit * 2 * lambda * prod(extra S primes)
        b = E.mul((2, 0), (1, 2))
        for g in self.S_extra:
            b = E.mul(b, g)
        b = E.mul(E.UNITS[bstar_unit], b)
        self.bstar = b
        self.qb = E.norm(b)
        self.xi2_exp = xi2_exp
        self.extra_xi = list(extra_xi)          # exponents of chi_p on the extra S primes
        assert len(self.extra_xi) == len(self.Sprimes)
        rng = random.Random(eta_seed)
        self.eta = {self.pname(P): cmath.exp(2j * math.pi * rng.random()) for P in self.primes}
        bctx = ModCtx(self.bstar)
        self.tau = bctx.gsum(self.xi_arr(bctx.X, bctx.Y), (1, 0), esign) / math.sqrt(self.qb)
        self.modctx = {}
        self.pdata = {}
        self.Ccache = {}
        self.Cstats = {"brute": 0, "closed_only": 0, "maxdiff": 0.0}

    @staticmethod
    def pname(P):
        return f"{P.gen[0]}{'+' if P.gen[1] >= 0 else '-'}{abs(P.gen[1])}w"

    def P(self, norm, which=0):
        L = [P for P in self.primes if P.N == norm]
        return L[which]

    # --- xi: character mod b_*, nonprincipal at each prime, order | 6 -------------
    def xi_arr(self, X, Y):
        lam = np.mod(X + Y, 3)                  # omega = 1 mod lambda
        v = np.where(lam == 0, 0.0, np.where(lam == 1, 1.0, -1.0)).astype(complex)
        x2 = np.mod(X, 2)
        y2 = np.mod(Y, 2)
        # F_4^x = <omega>: 1 -> 0, omega -> 1, 1+omega = omega^2 -> 2
        e2 = np.where((x2 == 1) & (y2 == 0), 0, np.where((x2 == 0) & (y2 == 1), 1, 2))
        v2 = np.exp(2j * np.pi * self.xi2_exp * e2 / 3)
        v2[(x2 == 0) & (y2 == 0)] = 0
        v = v * v2
        for Pq, e in zip(self.Sprimes, self.extra_xi):
            c = Pq.codes(X, Y)
            w = ZETA[(e * c) % 6]
            w[c < 0] = 0
            v = v * w
        return v

    def xi(self, z):
        return complex(self.xi_arr(np.array([z[0]], dtype=np.int64),
                                   np.array([z[1]], dtype=np.int64))[0])

    def ctx(self, M):
        key = (M[0], M[1])
        if key not in self.modctx:
            self.modctx[key] = ModCtx(M)
        return self.modctx[key]

    # --- ideals ------------------------------------------------------------------
    def ideal(self, fac):
        """fac: dict pname -> exponent; returns (generator, fac).  The generator is
        the product of the prime generators (primary unless gen_sign = -1)."""
        g = (1, 0)
        for name, e in fac.items():
            g = E.mul(g, epow(self.byname[name].gen, e))
        return g, {k: v for k, v in fac.items() if v}

    def chi_arr(self, fac, X, Y, power=1):
        s = np.zeros(len(X), dtype=np.int64)
        z = np.zeros(len(X), dtype=bool)
        for name, e in fac.items():
            c = self.byname[name].codes(X, Y)
            z |= c < 0
            s += e * power * np.where(c < 0, 0, c)
        v = ZETA[s % 6]
        v[z] = 0
        return v

    def chi(self, fac, z, power=1):
        out = 1 + 0j
        for name, e in fac.items():
            out *= self.byname[name].val(z, e * power)
        return out

    def gamma_j(self, fac, j):
        """gamma_j(c), c squarefree."""
        c, _ = self.ideal(fac)
        if not fac:
            return 1 + 0j
        cx = self.ctx(c)
        f = self.chi_arr(fac, cx.X, cx.Y, power=j)
        return cx.gsum(f, (1, 0), self.esign) / math.sqrt(cx.N)

    def Gamma_direct(self, c):
        cx = self.ctx(c)
        N = cx.N
        X = cx.X % N
        Y = cx.Y % N
        s0 = (X * X - Y * Y) % N
        s1 = (2 * X * Y - Y * Y) % N
        cc = E.conj(c)
        coord = (s0 * cc[1] + s1 * (cc[0] - cc[1])) % N
        return complex(np.sum(np.exp(2j * np.pi * self.esign * coord / N))) / math.sqrt(N)

    def G(self, fac, gen=None):
        A, _ = self.ideal(fac)
        if gen is not None:
            A = gen
        return np.conj(self.chi(fac, (4, 0))) * gamma4(A)

    # --- prime data and the local scalar -------------------------------------------
    def prime_data(self, name):
        if name not in self.pdata:
            P = self.byname[name]
            cx = self.ctx(P.gen)
            G = {0: -1.0}
            for r in range(1, 6):
                f = self.chi_arr({name: 1}, cx.X, cx.Y, power=r)
                G[r] = cx.gsum(f, (1, 0), self.esign)
            om = P.val((-1, 0))
            assert abs(om.imag) < 1e-12
            self.pdata[name] = dict(G=G, Q=P.N, omega=round(om.real),
                                    alpha=to_c(P.gen) / math.sqrt(P.N),
                                    chi4=P.val((4, 0)))
        return self.pdata[name]

    def gauss_pt(self, name, t, y):
        P = self.byname[name]
        pt = epow(P.gen, t)
        cx = self.ctx(pt)
        key = ("f", name, t)
        if key not in self.Ccache:
            self.Ccache[key] = self.chi_arr({name: 1}, cx.X, cx.Y, power=t)
        return cx.gsum(self.Ccache[key], y, self.esign)

    def C_closed(self, name, t, k, jp):
        d = self.prime_data(name)
        G, Q, om = d["G"], d["Q"], d["omega"]

        def lift(r, t, jp):
            if r % 6:
                return G[r % 6] * Q ** (t - 1) if jp == t - 1 else 0
            v = 0
            if jp >= t:
                v += Q ** t
            if jp >= t - 1:
                v -= Q ** (t - 1)
            return v
        if t == 0 and k == 0:
            return 1.0
        if t == 0:
            return 1.0 if jp == 0 else 0.0
        if k == 0:
            return lift(t, t, jp)
        if k == 1 and jp >= 1:
            return G[1] / om * lift(t - 1, t, jp - 1)
        return 0.0

    def C_p(self, name, t, k, jp, brute_cap=6e7):
        """[7.7] by brute force when Q^t * Q^k <= brute_cap, else [7.8]."""
        jpe = min(jp, t + k)                    # p^{j'} mod p^{t+k} is all that matters
        key = (name, t, k, jpe)
        if key in self.Ccache:
            return self.Ccache[key]
        P = self.byname[name]
        Q = P.N
        closed = self.C_closed(name, t, k, jp)
        if t == 0 and k == 0:
            val = 1.0 + 0j
        elif Q ** (t + k) <= brute_cap:
            ptk = epow(P.gen, t + k)
            pjp = E.reduce_mod(epow(P.gen, jpe), ptk) if jpe < t + k else (0, 0)
            pt = epow(P.gen, t)
            if k == 0:
                val = self.gauss_pt(name, t, pjp) if t > 0 else 1.0 + 0j
            else:
                pk = epow(P.gen, k)
                Xd, Yd = residues_np(pk)
                chik = self.chi_arr({name: 1}, Xd, Yd, power=k)
                val = 0j
                for i in range(len(Xd)):
                    if chik[i] == 0:
                        continue
                    d = (int(Xd[i]), int(Yd[i]))
                    diff = (pjp[0] - E.mul(pt, d)[0], pjp[1] - E.mul(pt, d)[1])
                    if not E.divides(pk, diff):
                        continue
                    y = exact_div(diff, pk)
                    g = self.gauss_pt(name, t, y) if t > 0 else 1.0
                    val += chik[i] * g
            self.Cstats["brute"] += 1
            scale = max(1.0, Q ** max(t - 0.5, 0))
            self.Cstats["maxdiff"] = max(self.Cstats["maxdiff"], abs(val - closed) / scale)
        else:
            val = complex(closed)
            self.Cstats["closed_only"] += 1
        self.Ccache[key] = val
        return val


# ---------------------------------------------------------------------------
# tuples, direct coefficient, local product
# ---------------------------------------------------------------------------
def merge(*facs):
    out = {}
    for f in facs:
        for k, v in f.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}


def scale(fac, m):
    return {k: m * v for k, v in fac.items()}


class Tuple:
    __slots__ = ("c", "n", "s", "a", "uunit", "ufac", "tag")

    def __init__(self, c, n, s, a, uunit, ufac, tag=""):
        self.c, self.n, self.s, self.a, self.uunit, self.ufac, self.tag = c, n, s, a, uunit, ufac, tag

    def key(self, W):
        q = lambda f: E.norm(W.ideal(f)[0])
        return (q(self.c) * q(self.n) ** 3 * q(self.s) * q(self.a) * q(self.ufac), self.uunit)

    def describe(self, W):
        def nm(f):
            return "*".join(f"{k}^{v}" if v > 1 else k for k, v in sorted(f.items())) or "1"
        return dict(c=nm(self.c), n=nm(self.n), s=nm(self.s), a=nm(self.a),
                    u=f"zeta^{self.uunit}*" + nm(self.ufac))


def K_direct(W, T, var=frozenset(), cacheA=None):
    """[7.4] with F from [7.1], by brute force.  var: set of control switches."""
    c, cfac = W.ideal(T.c)
    n, nfac = W.ideal(T.n)
    s, sfac = W.ideal(T.s)
    a, afac = W.ideal(T.a)
    ug, _ = W.ideal(T.ufac)
    u = E.mul(E.UNITS[T.uunit], ug)
    Afac = merge(cfac, scale(nfac, 3))
    A = E.mul(c, epow(n, 3))
    if "nonprimary_A" in var:                  # control: generator -A (c -> -c)
        c = neg(c)
        A = neg(A)
    if "nonprimary_s" in var:
        s = neg(s)
    H = E.mul(u, epow(a, 6))
    b = W.bstar
    bA = E.mul(b, A)
    # F(s, A, H)
    key = (A, "nA" in var)
    if cacheA is not None and key in cacheA:
        cxA, fA = cacheA[key]
    else:
        cxA = W.ctx(bA)
        fA = W.xi_arr(cxA.X, cxA.Y) * W.chi_arr(Afac, cxA.X, cxA.Y)
        if cacheA is not None:
            cacheA[key] = (cxA, fA)
    cxs = W.ctx(s)
    chis = W.chi_arr(sfac, cxs.X, cxs.Y)
    Hr = E.reduce_mod(H, E.mul(s, bA))
    p0, p1 = bA
    X, Y = cxs.X, cxs.Y
    z0 = Hr[0] - (p0 * X - p1 * Y)
    z1 = Hr[1] - (p0 * Y + p1 * X - p1 * Y)
    cs = E.conj(s)
    Ns = cxs.N
    w0 = z0 * cs[0] - z1 * cs[1]
    w1 = z0 * cs[1] + z1 * cs[0] - z1 * cs[1]
    ok = (w0 % Ns == 0) & (w1 % Ns == 0) & (chis != 0)
    F = 0j
    nsol = 0
    for i in np.nonzero(ok)[0]:
        k = (int(w0[i]) // Ns, int(w1[i]) // Ns)
        F += chis[i] * cxA.gsum(fA, k, W.esign)
        nsol += 1
    # prefactors
    chis_b = W.chi(sfac, b)
    if "drop_chisb" in var:
        chis_b = 1
    xs = W.xi(s)
    xu = W.xi(u)
    xu_term = xu if "xi_u_noconj" in var else np.conj(xu)
    tau = np.conj(W.tau) if "tau_conj" in var else W.tau
    g2 = W.gamma_j(cfac, 2) if "nonprimary_A" not in var else gamma_j_gen(W, c, cfac, 2)
    alA = to_c(A) / math.sqrt(E.norm(A))
    alA_term = alA if "alpha_noconj" in var else np.conj(alA)
    GA = np.conj(W.chi(Afac, (4, 0))) * gamma4(A)
    GA_term = GA if "G_noconj" in var else np.conj(GA)
    etaA = 1 + 0j
    for name, e in Afac.items():
        etaA *= W.eta[name] ** e
    Xi = W.xi(A) * (1 if "Xi_drop_chiAb" in var else W.chi(Afac, b))
    R = 1 if "drop_R" in var else r_bichar(A, s)
    K = (F * chis_b / (math.sqrt(W.qb) * tau * xs * xu_term)
         * g2 * alA_term * GA_term * etaA / Xi * R)
    info = dict(F=F, nsol=nsol, xi_s=xs, xi_u=xu, xi_A=W.xi(A), chiA_b=W.chi(Afac, b),
                chis_b=W.chi(sfac, b), R=r_bichar(A, s), H=H, u=u, A=A, s=s, Afac=Afac)
    return K, info


def gamma_j_gen(W, c, cfac, j):
    if not cfac:
        return 1 + 0j
    cx = W.ctx(c)
    f = W.chi_arr(cfac, cx.X, cx.Y, power=j)
    return cx.gsum(f, (1, 0), W.esign) / math.sqrt(cx.N)


def local_data(W, T):
    ug, _ = W.ideal(T.ufac)
    u = E.mul(E.UNITS[T.uunit], ug)
    names = set(T.c) | set(T.n) | set(T.s) | set(T.a) | set(T.ufac)
    out = []
    for name in sorted(names):
        e0 = T.c.get(name, 0)
        l = T.n.get(name, 0)
        k = T.s.get(name, 0)
        m = T.a.get(name, 0)
        j = T.ufac.get(name, 0)
        P = W.byname[name]
        u_red = u
        for _ in range(j):
            u_red = exact_div(u_red, P.gen)
        rho_k = P.code(u_red)
        assert rho_k is not None
        out.append((name, e0, l, k, m, j, rho_k))
    return out, u


def K_local(W, T, var=frozenset(), closed=False):
    loc, u = local_data(W, T)
    prod = 1 + 0j
    for (name, e0, l, k, m, j, rho_k) in loc:
        d = W.prime_data(name)
        Q = d["Q"]
        t = e0 + 3 * l
        jp = j + 6 * m
        C = W.C_closed(name, t, k, jp) if closed else W.C_p(name, t, k, jp)
        if C == 0:
            return 0j
        g1 = d["G"][1] / math.sqrt(Q)
        g3 = d["G"][3] / math.sqrt(Q)
        eta = W.eta[name]
        a_p = np.conj(d["alpha"]) ** 3 * eta ** 3
        g3t = g3 if "gamma3_noconj" in var else np.conj(g3)
        rho = complex(ZETA[rho_k])
        rexp = (t - k) if "rho_sign" in var else (k - t)
        oexp = t * k - e0 * l - l * (l - 1) // 2
        if "drop_omega_ll" in var:
            oexp += l * (l - 1) // 2
        if "drop_omega_tk" in var:
            oexp -= t * k
        g1e = g1 ** e0 if "gamma1_pos" in var else g1 ** (-e0)
        kap = ((-1) ** e0 * g1e * eta ** e0 * (a_p * g3t) ** l * rho ** rexp
               * d["omega"] ** oexp * C)
        prod *= kap
    return prod


def F_split(W, T, info):
    """FS: sqrt(q_b) tau xi(A) conj(xi(H/s)) prod_p U_p C_p(t,k,j')."""
    loc, u = local_data(W, T)
    s, sfac = W.ideal(T.s)
    A = info["A"]
    H = info["H"]
    Afac = info["Afac"]
    b = W.bstar
    val = math.sqrt(W.qb) * W.tau * W.xi(A) * np.conj(W.xi(H)) * W.xi(s)
    for (name, e0, l, k, m, j, rho_k) in loc:
        P = W.byname[name]
        t = e0 + 3 * l
        jp = j + 6 * m
        C = W.C_p(name, t, k, jp)
        if C == 0:
            return 0j
        hp = H
        for _ in range(jp):
            hp = exact_div(hp, P.gen)
        sp = s
        for _ in range(k):
            sp = exact_div(sp, P.gen)
        Ao = A
        for _ in range(t):
            Ao = exact_div(Ao, P.gen)
        U = (P.val(hp, k - t) * P.val(sp, t) * P.val(Ao, t - k) * P.val(b, t - k))
        val *= U * C
    return val


def diagnostics(W, T, info):
    """Which cancellations are exercised (value != 1) for this tuple."""
    loc, u = local_data(W, T)
    s, sfac = W.ideal(T.s)
    A = info["A"]
    Afac = info["Afac"]
    tp = {name: e0 + 3 * l for (name, e0, l, k, m, j, r) in loc}
    kp = {name: k for (name, e0, l, k, m, j, r) in loc}
    # A-s cross phases  prod_p chi_p^{t_p}(s_p) chi_p^{-k_p}(A_p^o)
    cross_As = 1 + 0j
    within_A = 1 + 0j
    diag = 1
    for name in tp:
        P = W.byname[name]
        t, k = tp[name], kp[name]
        sp = s
        for _ in range(k):
            sp = exact_div(sp, P.gen)
        Ao = A
        for _ in range(t):
            Ao = exact_div(Ao, P.gen)
        if t:
            cross_As *= P.val(sp, t)
        if k:
            cross_As *= P.val(Ao, -k)
        diag *= W.prime_data(name)["omega"] ** (t * k)
    names = [x for x in tp if tp[x]]
    for i in range(len(names)):
        for jx in range(i + 1, len(names)):
            p, r = W.byname[names[i]], W.byname[names[jx]]
            within_A *= (p.val(r.gen) * r.val(p.gen)) ** (tp[names[i]] * tp[names[jx]])
    om_ll = any(W.prime_data(nm)["omega"] == -1 and (l * (l - 1) // 2) % 2
                for (nm, e0, l, k, m, j, r) in loc)
    nontriv = lambda z: abs(z - 1) > 1e-9
    return dict(tau=nontriv(W.tau), xi_s=nontriv(info["xi_s"]), xi_u=nontriv(info["xi_u"]),
                xi_A=nontriv(info["xi_A"]), chiA_b=nontriv(info["chiA_b"]),
                chis_b=nontriv(info["chis_b"]), R_As=nontriv(info["R"]),
                cross_As=nontriv(cross_As), within_A=nontriv(within_A),
                diag_omega_tk=(diag == -1), omega_ll=bool(om_ll),
                l_pos=any(l > 0 for (_, e0, l, *_r) in loc),
                l2=any(l >= 2 for (_, e0, l, *_r) in loc),
                two_prime_A=len(names) >= 2,
                k_pos_t_pos=any(tp[x] > 0 and kp[x] > 0 for x in tp),
                m_pos=any(m > 0 for (_, e0, l, k, m, *_r) in loc),
                unit_u=T.uunit != 0)


# ---------------------------------------------------------------------------
def sf_list(W, names, maxnorm):
    """All squarefree products of the named primes with norm <= maxnorm."""
    out = [{}]
    for nm in names:
        Q = W.byname[nm].N
        out += [merge(f, {nm: 1}) for f in out
                if E.norm(W.ideal(f)[0]) * Q <= maxnorm]
    return out


def all_ideals(W, names, maxnorm):
    out = [{}]
    for nm in names:
        Q = W.byname[nm].N
        new = []
        for f in out:
            e = 1
            while E.norm(W.ideal(f)[0]) * Q ** e <= maxnorm:
                new.append(merge(f, {nm: e}))
                e += 1
        out += new
    return out


def build_tiers(W, which):
    nmsQ = lambda Q: [W.pname(P) for P in W.primes if P.N == Q]
    small = [W.pname(P) for P in W.primes if P.N <= 100]
    tuples = []
    if which == "main":
        p7, p7b = nmsQ(7)
        p13, p13b = nmsQ(13)
        p19 = nmsQ(19)[0]
        m5 = nmsQ(25)[0]
        # Tier 1 box: c sf N<=100, n=1, s all ideals N<=49, a in {1,p7,p7b}, u = 6 units x 12
        C1 = sf_list(W, small, 100)
        S1 = all_ideals(W, small, 49)
        A1 = [{}, {p7: 1}, {p7b: 1}]
        U1 = [{}, {p7: 1}, {p7: 2}, {p7: 5}, {p7b: 1}, {p7b: 4}, {p13: 1}, {p13: 3},
              {p7: 1, p13: 1}, {p7b: 1, p13b: 2}, {m5: 1}, {p19: 1}]
        for c in C1:
            for s in S1:
                for a in A1:
                    for uf in U1:
                        for un in range(6):
                            tuples.append(Tuple(c, {}, s, a, un, uf, "T1"))
        # Tier 2: cube-full A, u tailored at the primes of A (all j = 0..5)
        T2 = [  # (c, n, s-list, a-list, unit list, extra u factors)
            ({}, {p7: 1}), ({p7: 1}, {p7: 1}), ({p7b: 1}, {p7: 1}), ({p13: 1}, {p7: 1}),
            ({p7: 1, p13: 1}, {p7: 1}), ({}, {p7b: 1}), ({p7b: 1}, {p7b: 1}),
            ({}, {p13: 1}), ({p13: 1}, {p13: 1}), ({p7: 1}, {p13: 1}), ({}, {m5: 1}),
        ]
        S2 = [{}, {p7: 1}, {p7b: 1}, {p7: 2}, {p13: 1}, {p7: 1, p13: 1}, {p7: 1, p7b: 1},
              {m5: 1}, {p13: 2}]
        A2 = [{}, {p7: 1}, {p7b: 1}, {p13: 1}]
        for (c, n) in T2:
            supp = sorted(set(c) | set(n))
            # one prime: all units, u with and without an unrelated prime factor;
            # two primes: units {1, zeta, -1}, no extra factor (cost control)
            extras = ({}, {p19: 1}) if len(supp) == 1 else ({},)
            units = range(6) if len(supp) == 1 else (0, 1, 3)
            for s in S2:
                for a in A2:
                    for js in np.ndindex(*([6] * len(supp))):
                        base = {nm: int(j) for nm, j in zip(supp, js) if j}
                        for extra in extras:
                            for un in units:
                                tuples.append(Tuple(c, n, s, a, un, merge(base, extra), "T2"))
        # Tier 3: large A (l = 2 and two primes with l = 1), reduced index sets
        T3 = [({}, {p7: 2}, [{}, {p7: 1}, {p13: 1}, {p7b: 1}], [{}, {p7: 1}], [0, 1, 3]),
              ({p7: 1}, {p7: 2}, [{}, {p7: 1}, {p13: 1}], [{}, {p7: 1}], [0, 1]),
              ({}, {p7: 1, p7b: 1}, [{}, {p7: 1}, {p13: 1}], [{}, {p7: 1}], [0, 2]),
              ({p13: 1}, {p7: 1, p7b: 1}, [{}, {p7b: 1}], [{}], [0])]
        for (c, n, Ss, As, units) in T3:
            supp = sorted(set(c) | set(n))
            for s in Ss:
                for a in As:
                    for js in np.ndindex(*([6] * len(supp))):
                        base = {nm: int(j) for nm, j in zip(supp, js) if j}
                        for un in units:
                            tuples.append(Tuple(c, n, s, a, un, base, "T3"))
    elif which == "alt":
        # alternative admissible choices of b_* generator / xi: smaller box
        p7, p7b = nmsQ(7)
        p13 = nmsQ(13)[0]
        C1 = sf_list(W, small, 49)
        S1 = all_ideals(W, small, 25)
        for c in C1:
            for s in S1:
                for a in ({}, {p7: 1}):
                    for uf in ({}, {p7: 1}, {p7: 2}, {p7b: 3}, {p13: 1}):
                        for un in range(6):
                            tuples.append(Tuple(c, {}, s, a, un, uf, "alt1"))
        for (c, n) in (({}, {p7: 1}), ({p7: 1}, {p7: 1}), ({p13: 1}, {p7b: 1})):
            supp = sorted(set(c) | set(n))
            for s in ({}, {p7: 1}, {p7b: 1}, {p13: 1}):
                for a in ({}, {p7: 1}):
                    for js in np.ndindex(*([6] * len(supp))):
                        base = {nm: int(j) for nm, j in zip(supp, js) if j}
                        for un in (0, 1, 4):
                            tuples.append(Tuple(c, n, s, a, un, base, "alt2"))
    elif which == "bigS":
        # S enlarged by both primes of norm 7 (b_* of norm 588)
        p13, p13b = nmsQ(13)
        p19 = nmsQ(19)[0]
        smallE = [W.pname(P) for P in W.primes if P.N <= 100]
        C1 = sf_list(W, smallE, 100)
        S1 = all_ideals(W, smallE, 31)
        for c in C1:
            for s in S1:
                for a in ({}, {p13: 1}):
                    for uf in ({}, {p13: 1}, {p13: 2}, {p13b: 5}, {p19: 1}):
                        for un in (0, 1, 5):
                            tuples.append(Tuple(c, {}, s, a, un, uf, "bigS1"))
        for (c, n) in (({}, {p13: 1}), ({p13: 1}, {p13: 1})):
            supp = sorted(set(c) | set(n))
            for s in ({}, {p13: 1}, {p13b: 1}, {p19: 1}):
                for a in ({}, {p13: 1}):
                    for js in range(6):
                        for un in (0, 2):
                            tuples.append(Tuple(c, n, s, a, un, {p13: js} if js else {}, "bigS2"))
    return tuples


def run_tuples(W, tuples, label, fs_check=True, diag=True, log=print):
    t0 = time.time()
    cacheA = {}
    worst = dict(K=0.0, FS=0.0, Kclosed=0.0)
    nonzero = 0
    zero_both = 0
    fails = []
    flags = {}
    per_tier = {}
    for i, T in enumerate(tuples):
        Kd, info = K_direct(W, T, cacheA=cacheA)
        Kl = K_local(W, T)
        Klc = K_local(W, T, closed=True)
        sc = max(1.0, abs(Kl), abs(Kd))
        dev = abs(Kd - Kl) / sc
        devc = abs(Kd - Klc) / sc
        worst["K"] = max(worst["K"], dev)
        worst["Kclosed"] = max(worst["Kclosed"], devc)
        pt = per_tier.setdefault(T.tag, dict(n=0, nonzero=0, maxdev=0.0))
        pt["n"] += 1
        pt["maxdev"] = max(pt["maxdev"], dev)
        if fs_check:
            Fp = F_split(W, T, info)
            dfs = abs(info["F"] - Fp) / max(1.0, abs(Fp), abs(info["F"]))
            worst["FS"] = max(worst["FS"], dfs)
        if dev > TOL:
            fails.append((T.key(W), T, Kd, Kl))
        if abs(Kl) > 1e-6:
            nonzero += 1
            pt["nonzero"] += 1
            if diag:
                for kf, vf in diagnostics(W, T, info).items():
                    flags[kf] = flags.get(kf, 0) + int(vf)
        elif abs(Kd) < 1e-6:
            zero_both += 1
        if (i + 1) % 20000 == 0:
            log(f"   [{label}] {i + 1}/{len(tuples)}  maxdev={worst['K']:.2e}  "
                f"{time.time() - t0:.0f}s")
    fails.sort(key=lambda x: x[0])
    res = dict(label=label, tuples=len(tuples), nonzero=nonzero, zero_both_sides=zero_both,
               max_rel_dev_K=worst["K"], max_rel_dev_K_using_closed_C=worst["Kclosed"],
               max_rel_dev_FS=worst["FS"] if fs_check else None, failures=len(fails),
               per_tier=per_tier, exercised_on_nonzero=flags,
               seconds=round(time.time() - t0, 1))
    if fails:
        k, T, Kd, Kl = fails[0]
        res["minimal_failure"] = dict(T.describe(W), K_direct=str(Kd), K_local=str(Kl))
    return res


def run_controls(W, tuples, log=print):
    out = {}
    direct_sw = ["alpha_noconj", "G_noconj", "drop_R", "Xi_drop_chiAb", "drop_chisb",
                 "xi_u_noconj", "tau_conj", "nonprimary_s", "nonprimary_A"]
    local_sw = ["gamma3_noconj", "rho_sign", "drop_omega_ll", "drop_omega_tk", "gamma1_pos"]
    for sw in direct_sw + local_sw:
        t0 = time.time()
        var = frozenset([sw])
        worst = 0.0
        nfail = 0
        nnz = 0
        cacheA = {}
        for T in tuples:
            if sw in direct_sw:
                Kd, _ = K_direct(W, T, var=var, cacheA=cacheA if sw not in
                                 ("nonprimary_A",) else None)
                Kl = K_local(W, T)
            else:
                Kd, _ = K_direct(W, T, cacheA=cacheA)
                Kl = K_local(W, T, var=var)
            if abs(Kl) > 1e-6 or abs(Kd) > 1e-6:
                nnz += 1
            dev = abs(Kd - Kl) / max(1.0, abs(Kl), abs(Kd))
            worst = max(worst, dev)
            nfail += dev > TOL
        out[sw] = dict(max_rel_dev=worst, failing_tuples=nfail, of=len(tuples),
                       nonzero=nnz, verdict="FAILS (control OK)" if nfail else "passes (!)",
                       seconds=round(time.time() - t0, 1))
        log(f"   control {sw:16s} maxdev={worst:.3g} failing={nfail}/{len(tuples)}")
    return out


def check_P1(W, log=print):
    """[7.1]: finite Fourier transform claim, every H, small moduli."""
    nm = {P.N: W.pname(P) for P in W.primes}
    p7, p13 = nm[7], nm[13]
    p7b = [W.pname(P) for P in W.primes if P.N == 7][1]
    cases = [({}, {}), ({p7: 1}, {}), ({}, {p7: 1}), ({p7: 1}, {p7: 1}), ({p7: 1}, {p7b: 1}),
             ({p7: 2}, {}), ({}, {p13: 1}), ({p7: 1}, {p13: 1}), ({p13: 1}, {p7: 1})]
    worst = 0.0
    count = 0
    for sfac, Afac in cases:
        s, _ = W.ideal(sfac)
        A, _ = W.ideal(Afac)
        bA = E.mul(W.bstar, A)
        Mtot = E.mul(s, bA)
        cx = W.ctx(Mtot)
        X, Y = cx.X, cx.Y
        # f(m) = xi(m) chi_A(m) q_s^{-1/2} g_{chi_s}(s, -m)
        cxs = W.ctx(s)
        chis = W.chi_arr(sfac, cxs.X, cxs.Y)
        f = W.xi_arr(X, Y) * W.chi_arr(Afac, X, Y)
        gs = np.array([cxs.gsum(chis, (int(X[i]), int(Y[i])), -W.esign) for i in range(len(X))])
        f = f * gs / math.sqrt(cxs.N)
        cxA = W.ctx(bA)
        fA = W.xi_arr(cxA.X, cxA.Y) * W.chi_arr(Afac, cxA.X, cxA.Y)
        for i in range(len(X)):
            H = (int(X[i]), int(Y[i]))
            lhs = complex(np.dot(f, cx.phases(H, W.esign)))
            # F(s,A,H) directly
            Fv = 0j
            for jd in range(cxs.N):
                d = (int(cxs.X[jd]), int(cxs.Y[jd]))
                if chis[jd] == 0:
                    continue
                diff = (H[0] - E.mul(bA, d)[0], H[1] - E.mul(bA, d)[1])
                if not E.divides(s, diff):
                    continue
                Fv += chis[jd] * cxA.gsum(fA, exact_div(diff, s), W.esign)
            rhs = math.sqrt(cxs.N) * Fv
            worst = max(worst, abs(lhs - rhs) / max(1.0, abs(rhs)))
            count += 1
    log(f"   P1 Fourier claim: {count} (s,A,H) cases, max rel dev {worst:.2e}")
    return dict(cases=count, pairs=len(cases), max_rel_dev=worst)


def check_P2(W, log=print):
    """F(s,A,H) = 0 if H meets S (H = 0, lambda*..., 2*..., extra S primes)."""
    nm = [W.pname(P) for P in W.primes if P.N <= 13]
    worst = 0.0
    count = 0
    lam = (1, 2)
    bads = [(0, 0), lam, (2, 0), E.mul(lam, (3, 1)), E.mul((2, 0), (5, 3)), E.mul(lam, lam)]
    bads += [E.mul(g, (1, 3)) for g in W.S_extra]
    for sfac in ({}, {nm[0]: 1}, {nm[2]: 1}):
        for Afac in ({}, {nm[1]: 1}, {nm[0]: 3}):
            s, _ = W.ideal(sfac)
            A, _ = W.ideal(Afac)
            bA = E.mul(W.bstar, A)
            cxA = W.ctx(bA)
            fA = W.xi_arr(cxA.X, cxA.Y) * W.chi_arr(Afac, cxA.X, cxA.Y)
            cxs = W.ctx(s)
            chis = W.chi_arr(sfac, cxs.X, cxs.Y)
            for H in bads:
                Fv = 0j
                for jd in range(cxs.N):
                    d = (int(cxs.X[jd]), int(cxs.Y[jd]))
                    diff = (H[0] - E.mul(bA, d)[0], H[1] - E.mul(bA, d)[1])
                    if chis[jd] == 0 or not E.divides(s, diff):
                        continue
                    Fv += chis[jd] * cxA.gsum(fA, exact_div(diff, s), W.esign)
                worst = max(worst, abs(Fv))
                count += 1
    log(f"   P2 vanishing at S: {count} cases, max |F| = {worst:.2e}")
    return dict(cases=count, max_abs_F=worst)


def self_tests(W, log=print):
    out = {}
    # residue systems complete and distinct
    for M in [(7, 0), (2, 4), E.mul((2, 4), (3, 1)), (-5, 0), E.mul((3, 1), (3, 1))]:
        X, Y = residues_np(M)
        reps = {E.reduce_mod((int(x), int(y)), M) for x, y in zip(X, Y)}
        assert len(reps) == E.norm(M), M
    # symbol tables vs exact powmod
    rng = random.Random(7)
    bad = 0
    n = 0
    for P in W.primes[:12]:
        for _ in range(200):
            z = (rng.randrange(-500, 500), rng.randrange(-500, 500))
            k = P.codes(np.array([z[0]]), np.array([z[1]]))[0]
            ke = E.sym_prime(z, P.gen)
            bad += (k if k >= 0 else None) != ke
            n += 1
    out["symbol_table_vs_exact"] = f"{n - bad}/{n}"
    assert bad == 0
    # Gauss identities at primes (Lemma 4.2/(4.7)): gamma_2^3 = -alpha, gamma_1 gamma_2 = -alpha G
    worst = 0.0
    for P in W.primes:
        if P.N > 200:
            continue
        nmP = W.pname(P)
        d = W.prime_data(nmP)
        Q = d["Q"]
        g = {r: d["G"][r] / math.sqrt(Q) for r in range(1, 6)}
        Gp = np.conj(d["chi4"]) * gamma4(P.gen)
        worst = max(worst, abs(g[2] ** 3 + d["alpha"]), abs(g[1] * g[2] + d["alpha"] * Gp),
                    abs(gamma4(P.gen) - g[3]), abs(W.Gamma_direct(P.gen) - g[3]))
    out["prime_gauss_identities_maxdev"] = worst
    # four-term formula vs direct Gamma on composite / nonsquarefree elements
    worst = 0.0
    for fac in ({"x": 0},):
        pass
    els = []
    for P in W.primes[:6]:
        els += [P.gen, epow(P.gen, 3), epow(P.gen, 2)]
    els += [E.mul(W.primes[0].gen, W.primes[3].gen), E.mul(epow(W.primes[1].gen, 3), W.primes[2].gen)]
    for c in els:
        worst = max(worst, abs(gamma4(c) - W.Gamma_direct(c)))
    out["four_term_vs_direct_Gamma_maxdev"] = worst
    # xi is a character mod b_* of order | 6, nonprincipal at each prime of b_*
    cx = W.ctx(W.bstar)
    xv = W.xi_arr(cx.X, cx.Y)
    nz = np.abs(xv) > 0.5
    out["xi_units"] = int(nz.sum())
    out["xi_order_divides_6"] = bool(np.allclose(xv[nz] ** 6, 1))
    out["tau"] = [W.tau.real, W.tau.imag]
    out["abs_tau_minus_1"] = abs(abs(W.tau) - 1)
    log(f"   self-tests: {out}")
    return out


def main():
    outpath = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "results",
                                                                  "coeff74_factorization.json")
    logs = []

    def log(msg):
        print(msg, flush=True)
        logs.append(msg)

    t_all = time.time()
    result = {}
    log("== main world: S = {2, lambda}, b_* = 2*lambda, xi = (quadratic at lambda) x (omega at 2)")
    W = World()
    result["self_tests"] = self_tests(W, log)
    result["P1_fourier"] = check_P1(W, log)
    result["P2_vanishing"] = check_P2(W, log)
    tuples = build_tiers(W, "main")
    log(f"   main tuples: {len(tuples)}")
    res = run_tuples(W, tuples, "main", log=log)
    log(f"   main: {json.dumps(res, default=str)}")
    result["main"] = res
    result["C_brute_vs_closed"] = dict(W.Cstats)
    log(f"   C_p brute [7.7] vs closed [7.8]: {W.Cstats}")

    # controls on a subset that contains every tier
    rng = random.Random(3)
    sub = [T for T in tuples if T.tag == "T1"]
    sub = rng.sample(sub, 3000) + [T for T in tuples if T.tag == "T2"][::12] \
        + [T for T in tuples if T.tag == "T3" and not T.c and len(T.n) == 1][::4]
    # keep only tuples where the true identity is nonzero, plus some zeros
    log(f"== controls on {len(sub)} tuples")
    result["controls"] = run_controls(W, sub, log)

    # whole-world controls: primary normalization and additive character orientation
    for label, kw in (("ctrl_gen_minus_p", dict(gen_sign=-1)), ("ctrl_e_conjugate", dict(esign=-1))):
        Wc = World(**kw)
        tt = build_tiers(Wc, "alt")
        r = run_tuples(Wc, tt, label, fs_check=False, diag=False, log=log)
        r["verdict"] = "FAILS (control OK)" if r["failures"] else "passes (!)"
        log(f"   {label}: tuples={r['tuples']} maxdev={r['max_rel_dev_K']:.3g} "
            f"failures={r['failures']}")
        result[label] = r

    # alternative admissible choices (should PASS)
    for label, kw in (("alt_bstar_unit_zeta", dict(bstar_unit=1)),
                      ("alt_bstar_unit_minus", dict(bstar_unit=3)),
                      ("alt_xi2_conj", dict(xi2_exp=2)),
                      ("alt_eta_seed", dict(eta_seed=999))):
        Wa = World(**kw)
        tt = build_tiers(Wa, "alt")
        r = run_tuples(Wa, tt, label, log=log)
        log(f"   {label}: tuples={r['tuples']} nonzero={r['nonzero']} "
            f"maxdev={r['max_rel_dev_K']:.3g} FS={r['max_rel_dev_FS']:.3g} failures={r['failures']}")
        result[label] = r

    log("== enlarged S = {2, lambda, both primes of norm 7}; xi = chi^3 and chi^1 there")
    Wb = World(extra_S=(7,), extra_xi=(3, 1))
    result["bigS_self_tests"] = self_tests(Wb, log)
    result["bigS_P2"] = check_P2(Wb, log)
    tt = build_tiers(Wb, "bigS")
    r = run_tuples(Wb, tt, "bigS", log=log)
    log(f"   bigS: {json.dumps(r, default=str)}")
    result["bigS"] = r

    result["seconds_total"] = round(time.time() - t_all, 1)
    result["log"] = logs
    os.makedirs(os.path.dirname(os.path.abspath(outpath)), exist_ok=True)
    with open(outpath, "w") as fh:
        json.dump(result, fh, indent=1, default=str)
    log(f"wrote {outpath}  ({result['seconds_total']} s)")


if __name__ == "__main__":
    main()
