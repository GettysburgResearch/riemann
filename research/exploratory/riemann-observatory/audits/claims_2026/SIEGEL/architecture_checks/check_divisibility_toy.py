"""Exact toy replay of the OpenAI/Banks determinant construction (our own code).

For small N and a quadratic field Q(sqrt d), d != 1,2 squarefree, we
  * build the rows R_alpha = (theta_n^a1 sigma(theta_n)^a2 sigma tau(theta_n)^a3)_n,
    n in {0..N-1}^4, theta_n = n1 + n2 a + n3 b + n4 ab, a^2=d, b^2=2;
  * run the greedy weighted selection (weight a1 + H a2 + H a3) over K
    (K-independence <=> Q-independence of the 4 Q-multiples of each row);
  * compute Norm_{K/Q}(Delta) exactly as the determinant of the 4M x 4M integer
    regular-representation matrix;
  * check the paper's divisibility claim v_p(N(Delta)) >= 4 E_p,
    E_p = sum floor(a1/p), for every admissible p (p odd, p>H, p !| q, chi(p)=-1);
  * as controls: Frobenius-identity primes (chi(p)=1,(2/p)=1) where all three
    coordinates can be reduced, and Frobenius-tau primes, where no divisibility
    is predicted;
  * check the weight bound 96 H^{2/3} N^{4/3} and the box of Corollary 3.
Run: python3 -I check_divisibility_toy.py
"""
import itertools, math, sys
import flint

def kron_d_p(d, p):
    # Legendre symbol (d/p) for odd prime p
    r = pow(d % p, (p - 1) // 2, p)
    return 0 if r == 0 else (1 if r == 1 else -1)

def fund_disc(d):
    return d if d % 4 == 1 else 4 * d

def mul(x, y, d):
    x1, x2, x3, x4 = x; y1, y2, y3, y4 = y
    return (x1*y1 + d*x2*y2 + 2*x3*y3 + 2*d*x4*y4,
            x1*y2 + x2*y1 + 2*x3*y4 + 2*x4*y3,
            x1*y3 + x3*y1 + d*x2*y4 + d*x4*y2,
            x1*y4 + x4*y1 + x2*y3 + x3*y2)

def regmat(z, d):
    # columns: z*1, z*a, z*b, z*ab
    cols = [mul(z, e, d) for e in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]]
    return [[cols[j][i] for j in range(4)] for i in range(4)]

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b'\x00\x00'
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]

def vp(n, p):
    n = abs(int(n)); v = 0
    while n % p == 0: n //= p; v += 1
    return v

def run(d, N, H, verbose=True):
    q = abs(fund_disc(d))
    pts = list(itertools.product(range(N), repeat=4))
    M = N**4
    th = [(n[0], n[1], n[2], n[3]) for n in pts]
    sg = [(n[0], -n[1], n[2], -n[3]) for n in pts]
    st = [(n[0], -n[1], -n[2], n[3]) for n in pts]
    powcache = {}
    def pw(vecs, key, k):
        if (key, k) in powcache: return powcache[(key, k)]
        if k == 0: res = [(1,0,0,0)] * M
        else:
            prev = pw(vecs, key, k - 1)
            res = [mul(prev[i], vecs[i], d) for i in range(M)]
        powcache[(key, k)] = res
        return res
    def row(alpha):
        A = pw(th, 't', alpha[0]); B = pw(sg, 's', alpha[1]); C = pw(st, 'u', alpha[2])
        return [mul(mul(A[i], B[i], d), C[i], d) for i in range(M)]
    # enumerate indices by weight, tie-break (a2,a3)
    def indices():
        w = 0
        while True:
            for a2 in range(w // H + 1):
                for a3 in range((w - H*a2) // H + 1):
                    a1 = w - H*a2 - H*a3
                    yield (a1, a2, a3)
            w += 1
    P1, P2 = (1 << 61) - 1, (1 << 59) - 55  # two large primes for greedy rank tests
    retained, qrows = [], []
    for alpha in indices():
        r = row(alpha)
        # the 4 Q-multiples of the row (by 1, a, b, ab) as integer vectors in Z^{4M}
        new = []
        for e in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]:
            v = []
            for z in r: v.extend(mul(z, e, d))
            new.append(v)
        cand = qrows + new
        rk1 = flint.nmod_mat(cand, P1).rank(); rk2 = flint.nmod_mat(cand, P2).rank()
        assert rk1 == rk2, "mod-p rank disagreement"
        if rk1 == len(cand):
            retained.append(alpha); qrows = cand
            if len(retained) == M: break
    # exact norm of Delta via regular representation
    big = [[0]*(4*M) for _ in range(4*M)]
    for i, alpha in enumerate(retained):
        r = row(alpha)
        for j in range(M):
            m4 = regmat(r[j], d)
            for a in range(4):
                for b_ in range(4):
                    big[4*i + a][4*j + b_] = m4[a][b_]
    normD = flint.fmpz_mat(big).det()
    assert normD != 0
    S1 = sum(a[0] for a in retained); S2 = sum(a[1] + a[2] for a in retained)
    maxw = max(a[0] + H*a[1] + H*a[2] for a in retained)
    U = N**(4/3)
    out = {'d': d, 'q': q, 'N': N, 'H': H, 'M': M, 'S1': S1, 'S2': S2,
           'max_weight': maxw, 'weight_bound_96H^(2/3)U': 96*H**(2/3)*U,
           'max_a1': max(a[0] for a in retained),
           'log|N(Delta)|/4': float(math.log(abs(int(normD))))/4 if normD != 0 else None}
    fails = []; checks = []
    for p in primes_upto(max(a[0] for a in retained) + 2):
        if p == 2 or q % p == 0: continue
        chi = kron_d_p(d, p); two = 1 if p % 8 in (1, 7) else -1
        v = vp(normD, p)
        if chi == -1 and p > H:
            Ep = sum(a[0] // p for a in retained)
            checks.append(('admissible', p, v, 4*Ep))
            if v < 4*Ep: fails.append(('admissible', p, v, 4*Ep))
        elif chi == 1 and two == 1:
            Ep = sum(a[0] // p + a[1] // p + a[2] // p for a in retained)
            checks.append(('frob=1 (control, all 3 coords)', p, v, 4*Ep))
            if v < 4*Ep: fails.append(('frob1', p, v, 4*Ep))
        elif chi == 1 and two == -1:
            Ep = sum(a[1] // p + a[2] // p for a in retained)  # sigma*theta^p = sigma tau theta etc.
            checks.append(('frob=tau (control, coords 2,3 only)', p, v, 4*Ep))
            if v < 4*Ep: fails.append(('frobtau', p, v, 4*Ep))
    out['checks'] = checks; out['fails'] = fails
    if verbose:
        print({k: out[k] for k in out if k not in ('checks',)})
        for c in checks: print('   ', c)
    return out

if __name__ == '__main__':
    total_fail = 0
    for (d, N, H) in [(-163, 2, 1), (-163, 2, 2), (5, 2, 2), (13, 2, 1), (-7, 2, 2), (-163, 3, 2), (5, 3, 3)]:
        o = run(d, N, H)
        total_fail += len(o['fails'])
    print('TOTAL FAILURES:', total_fail)
