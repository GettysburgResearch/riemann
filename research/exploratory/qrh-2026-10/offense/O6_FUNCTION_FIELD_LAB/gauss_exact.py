"""gauss_exact.py -- EXACT checks (integer arithmetic in Z[zeta_N]) of the Gauss-sum identities
behind the Oct 5 absorption step, in the function-field lab F_q[T].

For monic squarefree n of degree d, chi_n(x) = chi0(Res(n,x)) (= (x/n)_r, chi0 of order r on F_q^*),
additive character e(x/n) = zeta_p^{res(x/n)}, res(x/n) = coefficient of T^{d-1} in x (n monic).
  g_n(j)   = sum_{x mod n} chi_n(x)^j e(x/n)
  g_j      = sum_{a in F_q^*} chi0(a)^j zeta_p^a          (Gauss sum over F_q)
Identities checked (each as LHS - RHS = 0 in Z[zeta_N], reduced mod Phi_N):
  (HD)  g_n(j) = mu(n) (-g_j)^d chi0^j(Res(n, n'))          [Hasse-Davenport + trace form]
  (gj)  g_n(1) g_n(2) = mu(n) (-J)^d conj(chi_n(4)) g_n(3), J = J(chi0^2, chi0^2)  [sextic, Oct 5 eq:gj]
  (S6)  mu(n) g_n(2) * g_m(5) = mu(m) g_m(2) * g_n(5)  for deg n = deg m   [cubic family: mu*cubic = f(d)*sextic]
  (Q)   mu(n) g_n(1) * conj g_m(1) = mu(m) g_m(1) * conj g_n(1), quartic chi0, deg n = deg m
  controls: the same identities with mu removed must fail.
Usage: python3 gauss_exact.py q order dmax [sample_per_degree]
"""
import sys
import random
from math import gcd
from ffcommon import monics, resultant, deriv, dlog_table, primes_upto, mobius, deg, trim, allpolys_below

try:
    import sympy
except ImportError:
    sympy = None


def cyclo(N):
    x = sympy.symbols('x')
    c = sympy.Poly(sympy.cyclotomic_poly(N, x), x).all_coeffs()[::-1]
    return [int(t) for t in c]


class ZN:
    """Z[zeta_N] elements as length-N integer vectors (powers of zeta_N), reduce mod Phi_N to compare."""
    def __init__(self, N):
        self.N = N
        self.phi = cyclo(N)

    def zero(self):
        return [0] * self.N

    def mono(self, e, c=1):
        v = [0] * self.N
        v[e % self.N] += c
        return v

    def add(self, a, b, s=1):
        return [x + s * y for x, y in zip(a, b)]

    def mul(self, a, b):
        N = self.N
        r = [0] * N
        nz = [(i, x) for i, x in enumerate(a) if x]
        for j, y in enumerate(b):
            if y:
                for i, x in nz:
                    r[(i + j) % N] += x * y
        return r

    def pw(self, a, k):
        r = self.mono(0)
        for _ in range(k):
            r = self.mul(r, a)
        return r

    def conj(self, a):
        N = self.N
        r = [0] * N
        for i, x in enumerate(a):
            r[(-i) % N] += x
        return r

    def is_zero(self, a):
        # reduce polynomial a(x) modulo Phi_N(x)
        a = list(a)
        dphi = len(self.phi) - 1
        for i in range(len(a) - 1, dphi - 1, -1):
            f = a[i]
            if f:
                for j in range(dphi + 1):
                    a[i - dphi + j] -= f * self.phi[j]
        return all(x == 0 for x in a[:dphi])


def main():
    q, r, dmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    samp = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 9
    assert (q - 1) % r == 0
    N = r * q // gcd(r, q)
    Z = ZN(N)
    g, dl = dlog_table(q)
    primes = primes_upto(dmax, q)
    rng = random.Random(1)

    def chi0(a, j):  # as exponent of zeta_N, or None
        a %= q
        if a == 0:
            return None
        return (dl[a] * j % r) * (N // r)

    def addc(a):
        return (a % q) * (N // q)

    gj = {}
    for j in range(0, r):
        v = Z.zero()
        for a in range(1, q):
            v[(chi0(a, j) + addc(a)) % N] += 1
        gj[j] = v
    # Jacobi sum J(chi0^2, chi0^2) (only meaningful for r = 6)
    J = Z.zero()
    if r == 6:
        for a in range(2, q):
            e1, e2 = chi0(a, 2), chi0(1 - a, 2)
            if e1 is not None and e2 is not None:
                J[(e1 + e2) % N] += 1

    def gauss_n(n, j):
        d = deg(n)
        v = Z.zero()
        for x in allpolys_below(d, q):
            if not x:
                continue
            rr = resultant(n, x, q)
            if rr == 0:
                continue
            top = x[d - 1] if len(x) == d else 0
            v[(chi0(rr, j) + addc(top)) % N] += 1
        return v

    stats = {}

    def rec(key, ok):
        a, b = stats.get(key, (0, 0))
        stats[key] = (a + int(ok), b + 1)

    for d in range(1, dmax + 1):
        ns = [n for n in monics(d, q) if mobius(n, q, primes) != 0]
        if len(ns) > samp:
            ns = rng.sample(ns, samp)
        ref = None
        for n in ns:
            mu = mobius(n, q, primes)
            D = resultant(n, deriv(n, q), q)
            G = {j: gauss_n(n, j) for j in range(1, r)}
            # (HD)
            for j in range(1, r):
                rhs = Z.mul(Z.pw([-x for x in gj[j]], d), Z.mono(chi0(D, j)))
                rhs = [mu * x for x in rhs]
                rec(f'HD j={j}', Z.is_zero(Z.add(G[j], rhs, -1)))
                if mu == -1: rec(f'HD j={j} control(no mu; mu=-1 only)', not Z.is_zero(Z.add(G[j], [mu * x for x in rhs], -1)))
            if r == 6:
                c4 = chi0(resultant(n, (4 % q,), q), 1)  # chi_n(4) as exponent
                lhs = Z.mul(G[1], G[2])
                rhs = Z.mul(Z.mul(Z.pw([-x for x in J], d), Z.mono(-c4)), G[3])
                rec('gj: g(1)g(2) = mu (-J)^d conj(chi_n(4)) g(3)', Z.is_zero(Z.add(lhs, [mu * x for x in rhs], -1)))
                if mu == -1: rec('gj control (no mu; mu=-1 only)', not Z.is_zero(Z.add(lhs, rhs, -1)))
            if ref is None:
                ref = (n, mu, G)
            else:
                n0, mu0, G0 = ref
                if r == 6:
                    lhs = Z.mul([mu * x for x in G[2]], G0[5])
                    rhs = Z.mul([mu0 * x for x in G0[2]], G[5])
                    rec('S6: mu g(2)/g(5) depends on d only', Z.is_zero(Z.add(lhs, rhs, -1)))
                    if mu != mu0: rec('S6 control (no mu; mu!=mu0 only)', not Z.is_zero(Z.add(Z.mul(G[2], G0[5]), Z.mul(G0[2], G[5]), -1)))
                if r == 4:
                    lhs = Z.mul([mu * x for x in G[1]], Z.conj(G0[1]))
                    rhs = Z.mul([mu0 * x for x in G0[1]], Z.conj(G[1]))
                    rec('Q: mu g(chi4)/conj g(chi4) depends on d only', Z.is_zero(Z.add(lhs, rhs, -1)))
                    if mu != mu0: rec('Q control (no mu; mu!=mu0 only)', not Z.is_zero(Z.add(Z.mul(G[1], Z.conj(G0[1])), Z.mul(G0[1], Z.conj(G[1])), -1)))
        print(f'd={d}: {len(ns)} squarefree n checked', flush=True)
    print(f'q={q} r={r} N={N} g={g}')
    for k, (a, b) in stats.items():
        print(f'  {k}: {a}/{b}')


if __name__ == '__main__':
    main()
