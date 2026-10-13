"""O1 check of the 'free Moebius' identities (floating point, finite; direct Gauss sums via a2/eis.py).
(K1) gamma_{-1}(p) = -chi_p(16) G(p) gamma_2(p) / alpha(p)            at primes (coordinator note (1))
(K2) gamma_1(n)    = mu(n) alpha(n) G(n) gamma_4(n)                    at squarefree n (1-3 prime factors)
     => sextic Kubota coefficient at numerator 1 is a Moebius-weighted cubic Gauss sum times Hecke x ray.
(K3) mu(n) gamma_2(n) conj(chi_n(h))^2 = chi_n(-1) alpha(n) G(n) gamma_{-1}(-h^4... ) form:
     mu(n) gamma_2(n) conj(chi_n(h))^2 = alpha(n) G(n) * N^{-1/2} sum_x conj(chi_n(x)) e(r x / n),  r = -h^4
     i.e. the absorbed cubic-family dual is the 6-fold (inverse-cocycle) Kubota coefficient with numerator -h^4.
G(n) = conj(chi_n(4)) gamma_3(n), alpha(n) = n/|n|.  Controls: the same identities without mu fail by 2.
Usage: python3 kubota_mobius_check.py NMAX OUT.json
"""
import sys, json, math, cmath, itertools, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'a2'))
import eis
Z = [cmath.exp(1j*math.pi*k/3) for k in range(6)]
def alpha(fs):
    n = (1, 0)
    for p in fs: n = eis.mul(n, p)
    z = complex(n[0] - n[1]/2, n[1]*math.sqrt(3)/2); return z/abs(z), n
def chiv(fs, u):
    k = eis.chi(fs, u); return 0 if k is None else Z[k]
def G(fs): return chiv(fs, (4, 0)).conjugate()*eis.gamma(3, fs)
def gam_num(j, fs, r):
    n = (1, 0)
    for p in fs: n = eis.mul(n, p)
    R, N = eis.residues(n); s = 0
    for v in R:
        k = eis.chi(fs, v)
        if k is None: continue
        s += Z[(j*k) % 6]*eis.e_of(eis.mul(r, v), n)
    return s/math.sqrt(N)
def main(NMAX, out):
    P = eis.primes_upto(NMAX)
    res = {'K1': 0.0, 'K1_ctrl': 9.0, 'K2': 0.0, 'K2_ctrl': 9.0, 'K3': 0.0, 'n_primes': len(P), 'n_comp': 0, 'n_K3': 0}
    for p in P:
        fs = [p]; a, _ = alpha(fs)
        lhs = eis.gamma(-1, fs); rhs = -chiv(fs, (16, 0))*G(fs)*eis.gamma(2, fs)/a
        res['K1'] = max(res['K1'], abs(lhs - rhs)); res['K1_ctrl'] = min(res['K1_ctrl'], abs(lhs + rhs))
    sq = [[p] for p in P] + [list(c) for c in itertools.combinations(P[:14], 2)] + [list(c) for c in itertools.combinations(P[:7], 3)]
    for fs in sq:
        a, n = alpha(fs)
        if eis.norm(n) > 4000: continue
        mu = (-1)**len(fs)
        lhs = eis.gamma(1, fs); rhs = mu*a*G(fs)*eis.gamma(4, fs)
        res['K2'] = max(res['K2'], abs(lhs - rhs))
        if len(fs) == 1: res['K2_ctrl'] = min(res['K2_ctrl'], abs(lhs - rhs/mu*(-mu)))  # sign-flipped control
        if len(fs) > 1: res['n_comp'] += 1
        if eis.norm(n) <= 1500:
            for h in [(2, 1), (5, 3), (1, 4), (7, -2)]:
                if eis.chi(fs, h) is None: continue
                h4 = eis.mul(eis.mul(h, h), eis.mul(h, h)); r = (-h4[0], -h4[1])
                lhs = mu*eis.gamma(2, fs)*chiv(fs, h).conjugate()**2
                rhs = a*G(fs)*gam_num(-1, fs, r)
                res['K3'] = max(res['K3'], abs(lhs - rhs)); res['n_K3'] += 1
    json.dump(res, open(out, 'w'), indent=1); print(res)
if __name__ == '__main__':
    main(int(sys.argv[1]), sys.argv[2])
