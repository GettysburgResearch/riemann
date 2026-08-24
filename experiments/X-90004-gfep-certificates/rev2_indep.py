"""FINAL-PASS independent reviewer checks (implementations written from scratch where feasible).
A. Exact boundary term: tau(theta) - 4m(1/theta) == -sqrt(th)[(4+L)M_K - A_K], K=floor(1/th).
B. Independent quadrature of tau(theta) over N-cells (no per-k closed form).
C. Leak accounting: loss during first-entrance descent comes ONLY from a3-children of
   strip parents m in [2n, 3n-3]; per-parent leak weight <= 1/6 + 1/(3m); survival >= 5/6.
D. Split consistency: POS+NEG+ADV in-flows + diagonal == independent sigma_first_entrance.
E. Sources: M_N, A_N to 2^21; C_N growth; VK-bound slackness.
F. Octave race at X=1e5: per-octave Phi ratios and cumulative |neg|/pos at argmin p.
G. tau(theta) vs X^{-1/2} suffix sum at X=1e5.
"""
import numpy as np, math, sys
sys.path.insert(0, "/home/user/riemann/experiments/X-90002-stress-test-artifacts")
from gfep import mobius_sieve, critical_r, sigma_first_entrance

# ---------- A + B ----------
def mob(n):
    mu = [0]*(n+1); mu[1] = 1
    for i in range(1, n+1):
        if mu[i]:
            for j in range(2*i, n+1, i): mu[j] -= mu[i]
    return mu

def tau_closed(theta):
    K = int(1/theta); mu = mob(K+1); tot = 0.0
    for k in range(1, K+1):
        if not mu[k]: continue
        F = lambda t: 2*math.sqrt(t)*(1-math.log(k)/2) + math.sqrt(t)*(math.log(1/t)+2)
        tot += mu[k]/math.sqrt(k)*(F(1.0/k)-F(theta))
    return tot

def tau_quad(theta, pts=48):
    """Gauss-Legendre on each cell (1/(N+1),1/N] intersect [theta,1]; C via prefix sums."""
    K = int(1/theta); mu = mob(K+2)
    Ms = np.cumsum([mu[k]/math.sqrt(k) if k else 0 for k in range(K+2)])
    As = np.cumsum([mu[k]*math.log(k)/math.sqrt(k) if k >= 2 else 0 for k in range(K+2)])
    x, w = np.polynomial.legendre.leggauss(pts)
    tot = 0.0
    for N in range(1, K+1):
        a, b = max(theta, 1.0/(N+1)), 1.0/N
        if b <= a: continue
        t = (b-a)/2*x + (b+a)/2; ww = (b-a)/2*w
        L = -np.log(t)
        C = (1 + L/2)*Ms[N] - As[N]/2
        tot += float(np.sum(ww * C / np.sqrt(t)))
    return tot

print("== A/B: exact boundary term and independent quadrature ==")
for theta in [1e-2, 1e-3, 1e-4]:
    K = int(1/theta); mu = mob(K+1)
    MK = sum(mu[k]/math.sqrt(k) for k in range(1, K+1))
    AK = sum(mu[k]*math.log(k)/math.sqrt(k) for k in range(2, K+1))
    mK = sum(mu[k]/k for k in range(1, K+1))
    L = math.log(1/theta)
    B_exact = -math.sqrt(theta)*((4+L)*MK - AK)
    tc = tau_closed(theta); tq = tau_quad(theta)
    print(f" th=1e{int(math.log10(theta)):+d}: tau_closed={tc:+.6f} tau_quad={tq:+.6f} "
          f"diff={abs(tc-tq):.2e} | 4m+Bexact={4*mK+B_exact:+.6f} resid={tc-4*mK-B_exact:+.2e} "
          f"| M_K={MK:+.4f} A_K={AK:+.4f}")

# ---------- C: leak accounting ----------
def descend_track(seed, X, n):
    far = seed.astype(float).copy(); far[:2*n] = 0.0
    entrance = np.zeros(2*n); lost = 0.0; strip_a3_loss = 0.0; other_loss = 0.0
    hi = X
    while hi >= 2*n:
        lo = max(2*n, (2*hi)//3 + 1)
        M = np.arange(lo, hi+1); fm = far[lo:hi+1]; g = fm/(2.0*M)
        a2 = M//2; b2 = M-a2; a3 = (M+2)//3; b3 = M-a3
        for idx, wts in ((a2, a2*g), (b2, b2*g), (a3, a3*g), (b3, b3*g)):
            below = idx < n
            amt = wts[below].sum()
            if amt:
                inside = (M[below] >= 2*n) & (M[below] <= 3*n-3)
                assert inside.all() or not amt, "loss from outside strip!"
            if idx is a3: strip_a3_loss += amt
            else: other_loss += amt
            buf = np.bincount(idx, weights=wts, minlength=hi)
            if len(buf) > 2*n: far[2*n:len(buf)] += buf[2*n:]
            entrance[n:] += buf[n:2*n]
        hi = lo - 1
    return entrance[n:], strip_a3_loss, other_loss

print("\n== C: leak accounting (uniform positive seed on [2n,X]) ==")
X = 30000
for n in [100, 1500]:
    seed = np.zeros(X+2); seed[2*n:X+1] = 1.0
    e, sl, ol = descend_track(seed, X, n)
    tot = float(seed[2*n:X+1].sum())
    print(f" n={n}: survival={e.sum()/tot:.4f} (>=5/6={5/6:.4f}: {e.sum()/tot >= 5/6}) "
          f"a3-strip loss={sl/tot:.4f} non-a3/out-of-strip loss={ol/tot:.2e}")
mmax = 0.0
for m in range(2*100, 3*100-2):
    a3 = (m+2)//3
    if a3 < 100: mmax = max(mmax, a3/(2*m))
print(f" max strip leak weight (n=100): {mmax:.6f} <= 1/6+1/(6n)={1/6+1/600:.6f}: {mmax <= 1/6+1/600}")

# ---------- D + F ----------
print("\n== D: split consistency at X=30000, n in (100, 1500) ==")
mu30 = mobius_sieve(X); r30 = critical_r(X, mu30)
m_all = np.arange(0, X+1); src = m_all*r30[:X+1]
Nof = np.zeros(X+1, dtype=int); Nof[1:] = X // m_all[1:]
def dsc(seed, n):
    from gfep import sigma_first_entrance as _
    far = np.zeros(X+2); far[:X+1] = seed
    e, *_r = descend_track(far, X, n)
    return e
for n in [100, 1500]:
    POS = Nof <= 4; NEG = (Nof >= 5) & (Nof <= 40); ADV = (Nof >= 41) & (m_all >= 2)
    parts = [dsc(np.where(msk, src, 0.0), n) for msk in (POS, NEG, ADV)]
    ps, sig = sigma_first_entrance(r30, X, n)
    tot = parts[0][:len(ps)] + parts[1][:len(ps)] + parts[2][:len(ps)] + src[ps]
    print(f" n={n}: max|split-sum - sigma_first_entrance| = {np.abs(tot-sig).max():.2e}")

print("\n== E: sources to 2^21 ==")
NN = 1 << 21
muN = mobius_sieve(NN).astype(float)
k = np.arange(NN+1, dtype=float); k[0] = 1
Mp = np.cumsum(muN/np.sqrt(k)); lg = np.zeros(NN+1); lg[2:] = np.log(k[2:])
Ap = np.cumsum(muN*lg/np.sqrt(k))
chk = [2**j for j in range(4, 22)]
Ms = [Mp[c] for c in chk]; As_ = [Ap[c] for c in chk]
print(f" M_N range over N=2^4..2^21: [{min(Ms):+.3f},{max(Ms):+.3f}]; A_N range: [{min(As_):+.3f},{max(As_):+.3f}]")
CN = [(1+math.log(c)/2)*Mp[c]-Ap[c]/2 for c in chk]
print(" |C_N(log N)|/log N at N=2^10,2^15,2^21:",
      ", ".join(f"{abs((1+math.log(c)/2)*Mp[c]-Ap[c]/2)/math.log(c):.3f}" for c in (2**10, 2**15, 2**21)))
c_vk = 0.2098  # Ford-shape constant, illustrative
N0 = 2**21
vk = math.sqrt(N0)*math.exp(-c_vk*(math.log(math.sqrt(N0)))**(3/5))
print(f" VK-style bound at N=2^21 ~ {vk:.1f} vs actual |M_N|={abs(Mp[N0]):.2f} (slack x{vk/abs(Mp[N0]):.0f})")

print("\n== F: octave race, X=1e5 (independent split-by-octave descent) ==")
X = 100000
muX = mobius_sieve(X); rX = critical_r(X, muX)
m_all = np.arange(0, X+1); srcX = m_all*rX[:X+1]
NofX = np.zeros(X+1, dtype=int); NofX[1:] = X // m_all[1:]
lab = np.zeros(X+1, dtype=int)
big = NofX >= 5
lab[big] = np.floor(np.log2(NofX[big])).astype(int) + 1
lab[NofX == 4] = 2; lab[(NofX == 2) | (NofX == 3)] = 1; lab[NofX == 1] = 0
for n in [317, 47]:
    ps, sig = sigma_first_entrance(rX, X, n)
    j = int(sig.argmin()); pstar = int(ps[j]); sx = math.sqrt(X)
    flows = []
    for g in range(int(lab.max())+1):
        seed = np.zeros(X+2); msk = lab == g
        seed[:X+1][msk] = srcX[msk]
        far = seed.copy(); far[:2*n] = 0.0
        e, *_ = descend_track(far, X, n)
        phi = e[j] + (srcX[pstar] if lab[pstar] == g else 0.0)
        flows.append(phi*sx)
    tot = sum(flows)
    pos = sum(flows[:3]); neg = sum(flows[3:])
    rats = [abs(flows[i+1]/flows[i]) for i in range(3, len(flows)-1) if abs(flows[i]) > 1e-12]
    print(f" n={n}: sqrtX*minSigma={sx*sig[j]:+.4f} (recon {tot:+.4f}); pos(N<=4)={pos:+.3f} "
          f"negSum={neg:+.3f} |neg|/pos={abs(neg)/pos:.4f}")
    print(f"   per-octave |Phi_(g+1)/Phi_g| (g>=3): " + " ".join(f"{r:.2f}" for r in rats))

print("\n== G: tau vs suffix aggregate at X=1e5 ==")
suf = np.cumsum(srcX[::-1])[::-1]
for theta in [1e-2, 1e-3, 3.17e-3]:
    Mth = int(theta*X)
    print(f" theta={theta:g}: t(M)={suf[Mth]/math.sqrt(X):+.5f} vs tau={tau_closed(theta):+.5f}")
