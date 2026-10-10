"""lemma18_local.py -- EMPIRICAL exact-symbol spot check of the prime-power Fourier sums
(Lemma lem:prime-power-fourier, eq:gauss-local, paper.tex l. 7056-7079) used by the two finite
Poisson transforms in the proof of Lemma 18.1, and of the local correlation factor
(eq:correlation-local, l. 7110-7126) at one prime.  Floating point; not a proof.

  G(a,k) = q_a^{-1/2} sum_{x mod a} chi_a(x) e(kx/a),  chi_{p^a} = chi_p^a (zero-extended)
  |G(p^a,k)| = P^{(a-1)/2} 1_{v_p(k)=a-1}            (6 !| a)
   G(p^a,k)  = P^{a/2} 1_{p^a | k} - P^{a/2-1} 1_{p^{a-1} | k}   (6 | a)

Split primes only (O/pi^a = Z/p^a); k ranges over a sample of elements.
Run: python3 -I lemma18_local.py
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "numerics"))
import eisenstein as E  # noqa: E402


def vp(k, pi, amax=20):
    v = 0
    while v < amax and E.divides_exact(pi, k):
        k = E.mul(k, E.conj(pi))
        k = (k[0] // E.norm(pi), k[1] // E.norm(pi))
        v += 1
    return v


def G(P, a, k):
    p = P.p
    mod = p ** a
    pa = E.power(P.gen, a)
    # z = k * x * conj(pi^a) / N ; omega-coefficient of k*conj(pi^a) is d0, so e(.) = exp(2 pi i x d0 / p^a)
    d0 = E.mul(k, E.conj(pa))[1]
    x = np.arange(mod, dtype=np.int64)
    codes = P.codes(x, np.zeros_like(x))
    zero = codes == E.ZERO
    val = np.where(zero, 0.0, E.ZETA[(np.where(zero, 0, codes).astype(np.int64) * a) % 6])
    s = (val * np.exp(2j * np.pi * ((x * d0) % mod) / mod)).sum()
    return s / p ** (a / 2.0)


def main():
    primes = [P for P in E.prime_ideals(40) if P.kind == "split"][:3]     # norms 7, 7, 13
    rng = np.random.default_rng(3)
    nchk, maxdev = 0, 0.0
    for P in primes:
        amax = 7 if P.p == 7 else 4
        for a in range(1, amax + 1):
            ks = []
            for v in range(0, a + 2):
                for _ in range(3):
                    u = (int(rng.integers(-50, 50)), int(rng.integers(-50, 50)))
                    if u == (0, 0) or E.divides_exact(P.gen, u):
                        continue
                    ks.append(E.mul(u, E.power(P.gen, v)))
            ks.append((0, 0))
            for k in ks:
                g = G(P, a, k)
                v = 10 ** 9 if k == (0, 0) else vp(k, P.gen)
                Pn = P.p
                if a % 6:
                    pred_abs = Pn ** ((a - 1) / 2.0) if v == a - 1 else 0.0
                    dev = abs(abs(g) - pred_abs)
                else:
                    pred = (Pn ** (a / 2.0) if v >= a else 0.0) - (Pn ** (a / 2.0 - 1) if v >= a - 1 else 0.0)
                    dev = abs(g - pred)
                maxdev = max(maxdev, dev / max(1.0, Pn ** (a / 2.0)))
                nchk += 1
    print("gauss-local: %d checks, max relative deviation %.2e" % (nchk, maxdev))
    assert maxdev < 1e-8


if __name__ == "__main__":
    main()
