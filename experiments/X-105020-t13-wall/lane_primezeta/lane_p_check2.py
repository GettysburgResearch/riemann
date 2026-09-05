import numpy as np, math
from mpmath import mp, mpf, zeta, log, primezeta

mp.dps = 30
N1 = 10**7; N0 = 10**6
smallp = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

sieve = np.ones(N1+1, dtype=bool); sieve[:2] = False
for p in range(2, int(N1**0.5)+1):
    if sieve[p]: sieve[p*p::p] = False
primes = np.nonzero(sieve)[0]
rough = primes[primes >= 67]

# smooth squarefree subset products with mobius
prods = np.ones(1); pars = np.zeros(1, dtype=np.int64)
for p in smallp:
    prods = np.concatenate([prods, prods*p]); pars = np.concatenate([pars, pars+1])
muv = np.where(pars % 2 == 0, 1.0, -1.0)
order = np.argsort(prods); prods = prods[order]; muv = muv[order]

# sieve reference values from run 1
sieve_vals = {
 ('1.5',1,N0): -0.016743071347, ('1.5',1,N1): -0.016752130236,
 ('1.25',1,N0): -0.051922273061, ('1.25',1,N1): -0.052289410088,
 ('1.5',2,N0): +0.000329702091, ('1.5',2,N1): +0.000341147366,
 ('1.25',2,N0): +0.004123997373, ('1.25',2,N1): +0.004592536759,
 ('1.5',0,N1): +0.399207360358, ('1.25',0,N1): +0.265438183435,
}

for zz in ['1.5','1.25']:
    zf = float(zz)
    rw = rough.astype(np.float64)**(-zf)
    cs1 = np.concatenate([[0.0], np.cumsum(rw)])   # prefix sums over rough primes

    # pair products pq <= N1, 67 <= p < q
    pp = []; ww = []
    for p in rough[rough <= int(N1**0.5)]:
        qmax = N1 // p
        j0 = np.searchsorted(rough, p, side='right'); j1 = np.searchsorted(rough, qmax, side='right')
        if j1 > j0:
            qs = rough[j0:j1].astype(np.float64)
            pp.append(p * qs); ww.append((p*qs)**(-zf))
    pp = np.concatenate(pp); ww = np.concatenate(ww)
    o = np.argsort(pp); pp = pp[o]; cs2 = np.concatenate([[0.0], np.cumsum(ww[o])])
    print(f"z={zz}: number of rough pairs pq<=1e7: {len(pp)}")

    for N in [N0, N1]:
        # k=0: subset products <= N
        k0 = float(np.sum(np.where(prods <= N, muv * prods**(-zf), 0.0)))
        # k=1: sum_m mu(m) m^-z * sum_{67<=p<=N/m} p^-z
        Xs = N / prods
        i1 = np.searchsorted(rough, Xs, side='right')
        k1 = -float(np.sum(muv * prods**(-zf) * cs1[i1]))
        # k=2: sum_m mu(m) m^-z * E2(N/m)
        i2 = np.searchsorted(pp, Xs, side='right')
        k2 = float(np.sum(muv * prods**(-zf) * cs2[i2]))
        for k, val in [(0,k0),(1,k1),(2,k2)]:
            key = (zz,k,N)
            if key in sieve_vals:
                sv = sieve_vals[key]
                print(f"  N={N:>8} k={k}: pair/subset-enum = {val:+.12f}  sieve = {sv:+.12f}  diff = {abs(val-sv):.2e}")

# ---------- A2 growth decomposition ----------
mu = np.ones(N1+1, dtype=np.int8)
for p in primes: mu[p::p] *= -1
for p in primes[primes <= int(N1**0.5)]: mu[p*p::p*p] = 0
mu[0] = 0
r = np.zeros(N1+1, dtype=np.int8)
for p in rough: r[p::p] += 1

nn = np.arange(N1+1, dtype=np.float64); nn[0]=1.0
winv = mu.astype(np.float64)/nn; winv[0]=0.0
print("\nA2 decomposition: x, Sig0, Sig1, Sig2, A2, Afull, u(x), V(x)=sum_{pq<=x}1/pq")
for ex in [3,4,5,6,7]:
    X = 10**ex
    m0 = float(np.sum(np.where(r[:X+1]==0, winv[:X+1], 0)))
    m1 = float(np.sum(np.where(r[:X+1]==1, winv[:X+1], 0)))
    m2 = float(np.sum(np.where(r[:X+1]==2, winv[:X+1], 0)))
    mf = float(np.sum(winv[:X+1]))
    ux = float(np.sum(1.0/rough[rough<=X]))
    print(f" x=1e{ex}: S0={m0:+.6f} S1={m1:+.6f} S2={m2:+.6f} A2={m0+m1+m2:+.6f} Afull={mf:+.6e} u={ux:.4f}")

# ---------- refined h min report on [1,1e6] ----------
c2 = np.where(r[:N0+1] <= 2, mu[:N0+1], 0).astype(np.float64)
cf = mu[:N0+1].astype(np.float64)
n0 = np.arange(N0+1, dtype=np.float64); n0[0]=1.0
A2c = np.cumsum(c2/n0); B2c = np.cumsum(c2/np.sqrt(n0)); A2c[0]=B2c[0]=0
Afc = np.cumsum(cf/n0); Bfc = np.cumsum(cf/np.sqrt(n0)); Afc[0]=Bfc[0]=0
idx = np.arange(1, N0+1); m_r = idx//67; m_l = (idx-1)//67
sq = np.sqrt(idx.astype(np.float64)); s67 = math.sqrt(67.0)
def h_arrays(A,B):
    hr = 4*sq*(A[idx]-A[m_r]/67.0) - 3*(B[idx]-B[m_r]/s67)
    hl = 4*sq*(A[idx-1]-A[m_l]/67.0) - 3*(B[idx-1]-B[m_l]/s67)
    return hr, hl
h2r,h2l = h_arrays(A2c,B2c); hfr,hfl = h_arrays(Afc,Bfc)
for lo in [1,2,100,10**5]:
    both2 = min(h2r[lo-1:].min(), h2l[max(lo-1,1):].min())
    bothf = min(hfr[lo-1:].min(), hfl[max(lo-1,1):].min())
    i2 = int(np.argmin(np.minimum(h2r[lo-1:], np.concatenate([[np.inf]*(1 if lo==1 else 0), h2l[max(lo-1,1):]])[:len(h2r[lo-1:])]))) + lo
    print(f" x>={lo}: min h2 = {both2:.6f}, min hfull = {bothf:.6f}")
d = h2r - hfr
first = np.nonzero(d != 0)[0]
print("first x where h2 != hfull:", (first[0]+1) if len(first) else None, " (67*71*73 =", 67*71*73, ")")
print("max (h2-hfull) on [1,1e6]:", d.max(), "at x=", int(np.argmax(d))+1, "; min:", d.min())

# ---------- bracket positivity on real axis ----------
def P67m(z): return primezeta(z) - sum(mpf(p)**(-z) for p in smallp)
print("\nbracket B2(z)=1-P67+(P67^2-P67(2z))/2 on real z:")
vals = []
for zv in [0.501,0.51,0.55,0.6,0.7,0.8,0.9,0.95,0.99,1.01,1.1,1.5,2,3,5]:
    z = mpf(str(zv))
    P1 = P67m(z); P2 = P67m(2*z)
    B2v = 1 - P1 + (P1**2 - P2)/2
    vals.append((zv, complex(B2v)))
for zv, b in vals:
    print(f"  z={zv}: B2 = {b.real:+.6f} {b.imag:+.2e}j")
