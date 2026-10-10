import numpy as np, itertools, math, json, sys
from mpmath import mp, mpf, mpc, zeta, log, primezeta, e1, quad, sqrt as msqrt

mp.dps = 30
N1 = 10**7   # sieve limit for Dirichlet-identity checks
N0 = 10**6   # empirics limit

# ---------- sieve ----------
sieve = np.ones(N1+1, dtype=bool); sieve[:2] = False
for p in range(2, int(N1**0.5)+1):
    if sieve[p]: sieve[p*p::p] = False
primes = np.nonzero(sieve)[0]
print("num primes to 1e7:", len(primes))

mu = np.ones(N1+1, dtype=np.int8)
for p in primes:
    mu[p::p] *= -1
for p in primes[primes <= int(N1**0.5)]:
    mu[p*p::p*p] = 0
mu[0] = 0

# rough count: number of distinct primes >= 67 dividing n
r = np.zeros(N1+1, dtype=np.int8)
for p in primes[primes >= 67]:
    r[p::p] += 1

# sanity
assert mu[1]==1 and r[1]==0 and mu[67]==-1 and r[67]==1 and r[67*71]==2 and mu[67*71]==1
assert r[67*71*73]==3
print("sieve sanity OK")

nn = np.arange(N1+1, dtype=np.float64); nn[0] = 1.0

smallp = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

def S_of(z):
    return np.prod([1 - mpf(p)**(-z) for p in smallp])

def P67_mp(z):
    # prime zeta over p>=67 via mpmath primezeta minus small primes
    return primezeta(z) - sum(mpf(p)**(-z) for p in smallp)

def P_series(z, J=80):
    # independent check: P(z) = sum_{j} mu(j)/j log zeta(jz)
    s = mpf(0)
    mus = mobius_list(J)
    for j in range(1, J+1):
        if mus[j] != 0:
            s += mpf(mus[j])/j * log(zeta(j*z))
    return s

def mobius_list(J):
    m = [1]*(J+1)
    for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]:
        if p > J: break
        for q in range(p, J+1, p): m[q] *= -1
        for q in range(p*p, J+1, p*p): m[q] = 0
    return m

# cross-validate primezeta at test points
for z in [mpf('1.5'), mpf('1.25'), mpf('2.5'), mpf('3.0'), mpf('2.4')]:
    a = primezeta(z); b = P_series(z)
    print(f"primezeta({z}) = {a},  series diff = {abs(a-b)}")

# direct prime-sum check of P67 at z=1.5 with PNT tail estimate
z = 1.5
direct = np.sum(primes[primes>=67].astype(np.float64)**(-z))
tail_est = e1((mpf(z)-1)*log(N1))   # integral_{N1}^inf t^-z/log t dt = E1((z-1) log N1)
print("P67(1.5): mpmath =", P67_mp(mpf('1.5')))
print("          direct primes<=1e7 =", direct, " + PNT tail est", tail_est, " => ", direct + float(tail_est))

# ---------- Task 1: Dirichlet identity per depth k ----------
res = {}
for zz in ['1.5','1.25','2.5']:
    z = mpf(zz); zf = float(zz)
    w = mu.astype(np.float64) * nn**(-zf); w[0]=0.0
    S = S_of(z); P1 = P67_mp(z); P2 = P67_mp(2*z)
    e1s = P1; e2s = (P1**2 - P2)/2
    rhs = {0: S, 1: -S*e1s, 2: S*e2s}
    print(f"\n=== z = {zz} ===")
    for k in [0,1,2]:
        mask = (r == k)
        lhs_1e6 = float(np.sum(np.where(mask[:N0+1], w[:N0+1], 0.0)))
        lhs_1e7 = float(np.sum(np.where(mask, w, 0.0)))
        R = rhs[k]
        d6 = abs(lhs_1e6 - float(R)); d7 = abs(lhs_1e7 - float(R))
        dig6 = -math.log10(d6/abs(float(R))) if d6>0 else 16
        dig7 = -math.log10(d7/abs(float(R))) if d7>0 else 16
        print(f" k={k}: RHS={float(R):+.12f}  LHS(1e6)={lhs_1e6:+.12f} (diff {d6:.2e}, {dig6:.1f} digits)  LHS(1e7)={lhs_1e7:+.12f} (diff {d7:.2e}, {dig7:.1f} digits)")
        res[(zz,k)] = (float(R), lhs_1e6, lhs_1e7)

# exact k=0 check by full subset enumeration at z=1.5
z = mpf('1.5')
tot = mpf(0)
for kk in range(len(smallp)+1):
    for comb in itertools.combinations(smallp, kk):
        prod = 1
        for p in comb: prod *= p
        tot += mpf((-1)**kk) * mpf(prod)**(-z)
print("\nk=0 exact subset-enumeration sum at z=1.5:", tot, " vs S(1.5) =", S_of(z), " diff:", abs(tot - S_of(z)))

# ---------- Task 5 empirics on N0 = 1e6 ----------
c2 = np.where(r[:N0+1] <= 2, mu[:N0+1], 0).astype(np.float64)
cf = mu[:N0+1].astype(np.float64)
n0 = np.arange(N0+1, dtype=np.float64); n0[0]=1.0
A2 = np.cumsum(c2 / n0); B2 = np.cumsum(c2 / np.sqrt(n0))
Af = np.cumsum(cf / n0); Bf = np.cumsum(cf / np.sqrt(n0))
A2[0]=B2[0]=Af[0]=Bf[0]=0.0
idx = np.arange(1, N0+1)
m_r = idx // 67          # floor(x/67) at x=n (right limit)
m_l = (idx - 1) // 67    # floor((n-eps)/67)
sq = np.sqrt(idx.astype(np.float64))
s67 = math.sqrt(67.0)

def h_arrays(A, B):
    hr = 4*sq*(A[idx] - A[m_r]/67.0) - 3*(B[idx] - B[m_r]/s67)
    hl = 4*sq*(A[idx-1] - A[m_l]/67.0) - 3*(B[idx-1] - B[m_l]/s67)
    return hr, hl

h2r, h2l = h_arrays(A2, B2)
hfr, hfl = h_arrays(Af, Bf)

def minreport(hr, hl, lo=1):
    i = np.argmin(hr[lo-1:]) + lo-1
    j = np.argmin(hl[lo:]) + lo   # left limits meaningful for n>=2
    vals = [(hr[i], idx[i], 'right'), (hl[j], idx[j], 'left')]
    v = min(vals)
    return v

print("\n--- h^{(<=2)} empirics on [1, 1e6] ---")
v2 = minreport(h2r, h2l); vf = minreport(hfr, hfl)
print("min h^{<=2} :", v2)
print("min h(full) :", vf)
print("h^{<=2} negative anywhere? ", bool((h2r[0:]<0).any() or (h2l[1:]<0).any()))
neg = np.nonzero(h2r < 0)[0]
print("num integers with h2 right-limit < 0:", len(neg), neg[:20]+1 if len(neg) else "")
negf = np.nonzero(hfr < 0)[0]
print("num integers with hfull right-limit < 0:", len(negf), (negf[:20]+1) if len(negf) else "")

print("\nlog-grid table: x, h^{<=2}(x), h_full(x), Psi^{<=2}(x), Psi_full(x)")
for ex in [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6]:
    x = int(round(10**ex))
    if x > N0: x = N0
    k = x
    p2 = 4*math.sqrt(k)*A2[k] - 3*B2[k]
    pf = 4*math.sqrt(k)*Af[k] - 3*Bf[k]
    print(f" x=10^{ex:<4}: h2={h2r[k-1]:+11.4f}  hfull={hfr[k-1]:+11.4f}  Psi2={p2:+11.4f}  Psif={pf:+11.4f}")

# main-term comparison: A2(x) vs S(1)*(1-u+u^2/2), u = sum_{67<=p<=x} 1/p
S1 = float(np.prod([1-1/p for p in smallp]))
pr6 = primes[(primes>=67)&(primes<=N0)].astype(np.float64)
u = float(np.sum(1.0/pr6))
print(f"\nS(1) = {S1:.6f}, u(1e6) = sum_(67<=p<=1e6) 1/p = {u:.6f}")
print(f"A2(1e6) = {A2[N0]:.6f}  vs  S(1)*(1-u+u^2/2) = {S1*(1-u+u*u/2):.6f}")
print(f"Afull(1e6) = {Af[N0]:.6e} (should tend to 0)")
print(f"B2(1e6) = {B2[N0]:.4f},  Bfull(1e6) = {Bf[N0]:.4f}")

# ---------- Mellin identity check for F^{(<=2)}(s) ----------
# segment-exact integral of h2 * x^{-s-1} over [1, N0], breakpoints at integers
def F2_numeric(sf):
    a_n = A2[idx] - A2[m_r]/67.0    # value on [n, n+1)
    b_n = B2[idx] - B2[m_r]/s67
    x_lo = idx.astype(np.float64); x_hi = x_lo + 1.0
    t1 = 4*a_n * (x_hi**(0.5-sf) - x_lo**(0.5-sf))/(0.5-sf)
    t2 = -3*b_n * (x_hi**(-sf) - x_lo**(-sf))/(-sf)
    return float(np.sum(t1 + t2))

def F2_closed(s):
    zloc = s + mpf('0.5')
    S = S_of(zloc); P1 = P67_mp(zloc); P2 = P67_mp(2*zloc)
    G = S*(1 - P1 + (P1**2 - P2)/2)
    return (1 - mpf(67)**(-zloc)) * (s + mpf('1.5'))/(s*(s-mpf('0.5'))) * G

for sf in [1.2, 2.0]:
    fn = F2_numeric(sf); fc = F2_closed(mpf(str(sf)))
    print(f"\nF2 Mellin check at s={sf}: numeric(x<=1e6)={fn:.10f}  closed={float(fc):.10f}  diff={abs(fn-float(fc)):.2e}")

# also verify the repo kernel Mellin: int_1^inf (4 sqrt y - 3) y^{-s-1} dy = (s+3/2)/(s(s-1/2)) at s=0.8
s = mpf('0.8')
q = quad(lambda y: (4*msqrt(y)-3)*y**(-s-1), [1, mp.inf])
print("kernel Mellin at s=0.8:", q, " vs ", (s+mpf('1.5'))/(s*(s-mpf('0.5'))))
