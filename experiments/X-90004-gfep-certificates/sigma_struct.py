import numpy as np, sys, math
sys.path.insert(0, "/home/user/riemann/experiments/X-90002-stress-test-artifacts")
from gfep import mobius_sieve, critical_r, sigma_first_entrance

for X in [1000, 2000, 5003]:
    r = critical_r(X)
    # (a) 2n >= X: Sigma == p*r[p] exactly (R(X)=0 kills the single far source when 2n==X)
    n = X//2
    ps, sig = sigma_first_entrance(r, X, n)
    diag = ps*r[ps[0]:ps[-1]+1]
    print(f"X={X}: n=floor(X/2)={n}, max|Sigma - p r(p)| = {np.abs(sig-diag).max():.2e}, R(X)={r[X]:.2e}")
    # global min cell exact formula
    smin = sig.min(); pmin = ps[sig.argmin()]
    formula = math.sqrt(X-1)*math.log(X/(X-1))
    print(f"   min Sigma={smin:.8e} at p={pmin}; sqrt(X-1)log(X/(X-1))={formula:.8e}  match={abs(smin-formula)<1e-12}")

# (b) one-step closed form, X/3 < n <= X/2
def sigma_closed_top_third(r, X, n):
    up = min(2*n, X+1); ps = np.arange(n, up); out = ps.astype(float)*r[n:up]
    for m in range(2*n, X+1):
        g = r[m]/2.0  # m R(m) Q(m,c) = c*mult*R(m)/2
        a2, b2 = m//2, m - m//2; a3 = -(-m//3); b3 = m - a3
        for c,mult in [(a2,1),(b2,1),(a3,1),(b3,1)]:
            if n <= c < up: out[c-n] += c*g
    return out

X = 2000; r = critical_r(X)
for n in [667, 700, 900, 1000]:
    ps, sig = sigma_first_entrance(r, X, n)
    cl = sigma_closed_top_third(r, X, n)
    print(f"X={X} n={n}: one-step closure max err = {np.abs(sig-cl).max():.2e}")

# top-third far sources are w-differences only: check U(m)=w(m) for m> X/2, and R(m)=w(m)-w(m+1)>=0 there
w = np.zeros(X+2); q = np.arange(1, X+1, dtype=float)
w[2:X+1] = np.log(X/q[1:])/np.sqrt(q[1:])
mval = np.arange(X//2+1, X+1)
print("max |R(m) - (w(m)-w(m+1))| on (X/2, X]:", np.abs(r[mval] - (w[mval]-w[np.minimum(mval+1,X+1)])).max())
