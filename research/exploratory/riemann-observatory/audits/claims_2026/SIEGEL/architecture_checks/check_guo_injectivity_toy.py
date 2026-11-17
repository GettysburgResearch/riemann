"""Small exact instances of Guo (arXiv:2610.30476) Lemma 3.3 and (3.10) (our own code).

iota: V = span_Z{z^r w^s : r<p0, s<s0} -> Z^{2 m(m-1) s0},
f -> two integer coefficients of rho((d/dz)^j f (u+vt, u-vt)) mod t^2-d,
0<=u<m, 1<=v<m, 0<=j<s0, m = ceil(sqrt p0).
Checks: (i) iota injective (Lemma 3.3);  (ii) for every odd p<=p0 with chi(p)=-1,
v_p(gcd of maximal minors) >= H_p = sum_{r,s} min(floor(r/p), s0-1-s)  ((3.10) + basis change);
(iii) the counting inequality of Lemma 3.2, H <= n log n + sum log w_i, with w_i the actual
column sup-norms.  The paper's size constraints (p0>=10000, p0>=4q, s0=floor(p0/30)) are NOT
imposed; injectivity only needs 2m(m-1)>p0, s0<p0, chi(p0)=-1.
Run: python3 -I check_guo_injectivity_toy.py
"""
import math, flint

def leg(d, p):
    r = pow(d % p, (p - 1)//2, p); return 0 if r == 0 else (1 if r == 1 else -1)

def mulq(x, y, d):  # (a+bt)(c+et) mod t^2-d
    return (x[0]*y[0] + d*x[1]*y[1], x[0]*y[1] + x[1]*y[0])

def powq(x, k, d):
    r = (1, 0)
    for _ in range(k): r = mulq(r, x, d)
    return r

def falling(r, j):
    out = 1
    for i in range(j): out *= (r - i)
    return out

def primes_upto(n):
    return [p for p in range(2, n+1) if all(p % k for k in range(2, int(p**.5)+1))]

def vp(n, p):
    n = abs(int(n)); v = 0
    while n and n % p == 0: n //= p; v += 1
    return v

def run(d, p0, s0):
    assert leg(d, p0) == -1 and s0 < p0
    m = math.isqrt(p0); m = m if m*m >= p0 else m + 1
    assert 2*m*(m-1) > p0
    cols = [(r, s) for r in range(p0) for s in range(s0)]
    rows = []
    grid = [(u, v) for u in range(m) for v in range(1, m)]
    for (u, v) in grid:
        zp = [powq((u, v), k, d) for k in range(p0)]
        wp = [powq((u, -v), k, d) for k in range(s0)]
        for j in range(s0):
            r1, r2 = [], []
            for (r, s) in cols:
                if j > r: r1.append(0); r2.append(0); continue
                c = falling(r, j)
                val = mulq(zp[r-j], wp[s], d)
                r1.append(c*val[0]); r2.append(c*val[1])
            rows.append(r1); rows.append(r2)
    A = flint.fmpz_mat(rows)
    n = len(cols)
    rank = A.rank()
    snf = A.snf()
    gcdminors = 1
    for i in range(n): gcdminors *= int(snf[i, i])
    res = {'d': d, 'p0': p0, 's0': s0, 'm': m, 'n': n, 'rows': len(rows), 'rank': rank, 'injective': rank == n}
    fails = []
    Htot = 0.0
    for p in primes_upto(p0):
        if p == 2 or leg(d, p) != -1: continue
        Hp = sum(min(r // p, s0 - 1 - s) for (r, s) in cols)
        v = vp(gcdminors, p)
        if v < Hp: fails.append((p, v, Hp))
        res.setdefault('vp_vs_Hp', []).append((p, v, Hp))
        Htot += Hp * math.log(p)
    w = [max(abs(int(A[i, k])) for i in range(A.nrows())) for k in range(n)]
    rhs = n*math.log(n) + sum(math.log(x) for x in w)
    res['H'] = round(Htot, 2); res['nlogn+sum log w'] = round(rhs, 2)
    res['log gcd of maximal minors'] = round(math.log(gcdminors), 2)
    res['fails'] = fails
    print(res)
    return len(fails) + (0 if rank == n else 1) + (0 if Htot <= rhs else 1)

if __name__ == '__main__':
    tot = 0
    for (d, p0, s0) in [(-163, 37, 3), (-163, 23, 4), (5, 17, 4), (-7, 19, 3), (13, 31, 3)]:
        tot += run(d, p0, s0)
    print('TOTAL FAILURES:', tot)
