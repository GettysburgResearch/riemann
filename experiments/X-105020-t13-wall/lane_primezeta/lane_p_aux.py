import numpy as np, itertools, math
from mpmath import mp, mpf, mpc, zeta, log, primezeta, zetazero, e1

mp.dps = 30
N1 = 10**7
smallp = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

sieve = np.ones(N1+1, dtype=bool); sieve[:2] = False
for p in range(2, int(N1**0.5)+1):
    if sieve[p]: sieve[p*p::p] = False
primes = np.nonzero(sieve)[0]

# ---------- semi-analytic tail-corrected k=1 check ----------
def S_of(z): return np.prod([1 - mpf(p)**(-z) for p in smallp])
def P67_mp(z): return primezeta(z) - sum(mpf(p)**(-z) for p in smallp)

rough = primes[primes >= 67].astype(np.float64)

for zz in ['1.5','1.25']:
    z = mpf(zz); zf = float(zz)
    # prefix sums of p^{-z} over rough primes
    pw = rough**(-zf)
    cs = np.concatenate([[0.0], np.cumsum(pw)])
    P67f = float(P67_mp(z))
    def tailP(X):
        # sum_{p>X, p>=67} p^{-z}
        i = np.searchsorted(rough, X, side='right')
        return P67f - cs[i]
    # enumerate all smooth squarefree m via subsets; need tailP(max(66, N/m))
    ms = [1]
    for p in smallp:
        ms = ms + [m*p for m in ms]
    ms = np.array(sorted(ms), dtype=np.float64)
    mus = np.array([(-1)**(bin(i).count('1')) for i in range(2**18)])
    # recompute properly: pair each subset with its mobius
    vals = []
    for i in range(2**18):
        pass
    # vectorized: build products and parity together
    prods = np.ones(1); pars = np.zeros(1, dtype=np.int64)
    for p in smallp:
        prods = np.concatenate([prods, prods*p]); pars = np.concatenate([pars, pars+1])
    muv = np.where(pars % 2 == 0, 1.0, -1.0)
    Xs = np.maximum(66.0, N1/prods)
    idxs = np.searchsorted(rough, Xs, side='right')
    tails = P67f - cs[idxs]
    tail_k1 = -np.sum(muv * prods**(-zf) * tails)
    # sieve LHS at N1 (recompute quickly): need mu and rough count again -- do minimal version
    print(f"z={zz}: predicted missing k=1 tail beyond 1e7 = {tail_k1:+.10e}")

# ---------- e2 algebra direct check ----------
z = 2.0
wp = primes[(primes>=67)&(primes<=100000)].astype(np.float64)
pw = wp**(-z)
tot = np.sum(pw)**2 - np.sum(wp**(-2*z))
direct_pairs = tot/2   # = sum_{p<q in window} (pq)^{-2}
# formula for window: e2_win = (U^2 - V)/2 with U,V window sums (identical algebra) -- instead compare full:
P1 = P67_mp(mpf(2)); P2 = P67_mp(mpf(4))
e2_full = (P1**2 - P2)/2
# direct full estimate: window pairs + bound on remainder
rem_bound = float(P67_mp(mpf(2)))* (float(P67_mp(mpf(2))) - np.sum(pw))  # crude
print(f"e2(2): formula = {float(e2_full):.12e}; window-pair direct = {direct_pairs:.12e}; missing-mass crude bound = {rem_bound:.2e}")

# ---------- singular behavior numerics ----------
print("\n-- near z=1: P(1+d) + log(d) should converge --")
for d in ['1e-2','1e-4','1e-6','1e-8']:
    dd = mpf(d)
    v = primezeta(1+dd) + log(dd)
    print(f" d={d}: P(1+d)+log d = {v}")

print("\n-- near z=1/2+: P(1/2+d) - (1/2)log(2d) --")
for d in ['1e-2','1e-3','1e-4','1e-5']:
    dd = mpf(d)
    v = primezeta(mpf('0.5')+dd)
    w = v - mpf('0.5')*log(2*dd)
    print(f" d={d}: P = {mpc(v)},  P-(1/2)log(2d) = {mpc(w)}")

print("\n-- near z=rho1 (first zeta zero): P(z) - log zeta(z) --")
rho1 = zetazero(1)
for d in ['0.2','0.1','0.05','0.02','0.01']:
    zpt = rho1 + mpf(d)
    try:
        v = primezeta(zpt)
        w = v - log(zeta(zpt))
        print(f" d={d}: P = {mpc(v)},  P - log zeta = {mpc(w)}")
    except Exception as ex:
        print(f" d={d}: primezeta failed: {ex}")

print("\n-- bracket B2(z)=1-P67+(P67^2-P67(2z))/2 near z=1: compare to (1/2)log(z-1)^2 --")
# first extract a67 = lim P67(z)+log(z-1)
a67 = primezeta(1+mpf('1e-12')) + log(mpf('1e-12')) - sum(mpf(p)**(-1) for p in smallp)
print(" a67 := lim_{z->1}[P67(z)+log(z-1)] =", a67)
for d in ['1e-2','1e-4','1e-6']:
    dd = mpf(d); zloc = 1+dd
    P1 = P67_mp(zloc); P2 = P67_mp(2*zloc)
    B2v = 1 - P1 + (P1**2 - P2)/2
    ell = log(dd)
    model = ell**2/2 + (1-a67)*ell
    print(f" d={d}: B2 = {B2v},  B2 - [l^2/2+(1-a67)l] = {B2v - model}")

print("\n-- closed-form F2(s) blow-up as s->1/2+ --")
def F2_closed(s):
    zloc = s + mpf('0.5')
    S = S_of(zloc); P1 = P67_mp(zloc); P2 = P67_mp(2*zloc)
    G = S*(1 - P1 + (P1**2 - P2)/2)
    return (1 - mpf(67)**(-zloc)) * (s + mpf('1.5'))/(s*(s-mpf('0.5'))) * G
for d in ['0.1','0.01','0.001']:
    s = mpf('0.5')+mpf(d)
    print(f" s=1/2+{d}: F2(s) = {F2_closed(s)}")

# compare full F(s) = (1-67^-z)(s+3/2)/(s(s-1/2) zeta(z)): finite at 1/2
def F_full(s):
    zloc = s + mpf('0.5')
    return (1 - mpf(67)**(-zloc)) * (s + mpf('1.5'))/(s*(s-mpf('0.5'))*zeta(zloc))
print(" full F(0.5+1e-6) =", F_full(mpf('0.5')+mpf('1e-6')), " (finite: zeta pole cancels)")
