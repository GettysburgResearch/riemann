"""STAGE 2 GATE numerics: shell decomposition validation + supply/demand measurement.

Objects (T-90001 SS0): b_X, v_q, r_X, s_X, T^s(2); profile E, differenced E_c, moat H, H_c.
Checks:
 (V1) exact T^s_X(2) vs prime-sum form F(X)=X^{-1/2} sum_p (log p) E_c(p/X); residual <= floor 10.3(2+log X)
 (V2) sqrt(X) H_c(2/X) -> -2*sqrt(2)*(1+zeta(1/2))*log 2 = -0.9025 (deterministic budget at z=2 is O(1))
 (V3) Mobius coordinates: sum_k mu(k) c_X(k) = X^{-1/2} sum_n Lambda(n) E_c(n/X) = F(X) + prime-power term O(log X)
 (V4) dyadic-block decomposition of the fluctuation; block_i vs R(t)/sqrt(t) sensitivity
 (V5) random completely multiplicative f: shell_f = sum_k f(k) c_X(k); empirical size + exact E[shell^2]
 (V6) demand vs supply curves at each X
"""
import numpy as np, math, sys, time

t0=time.time()

def sieve(X):
    pr = np.ones(X+1, bool); pr[:2]=False
    for i in range(2,int(X**.5)+1):
        if pr[i]: pr[i*i::i]=False
    return np.nonzero(pr)[0]

def spf_sieve(X):
    spf = np.zeros(X+1, np.int64)
    for i in range(2,X+1):
        if spf[i]==0: spf[i::i][spf[i::i]==0]=i
    return spf

def mobius(X, spf):
    mu = np.ones(X+1, np.int64)
    for n in range(2,X+1):
        p = spf[n]; m = n//p
        mu[n] = 0 if m % p == 0 else -mu[m]
    return mu

def profile_tables(Nmax):
    k = np.arange(Nmax+1, dtype=float); k[0]=1
    t1 = k**-0.5; t1[0]=0.0
    t2 = (k**-0.5)*np.log(k); t2[0]=0.0
    S = np.cumsum(t1); A = np.cumsum(t2)
    return S, A

def E_at(n, Z, S, A):
    """E(theta) at theta=n/Z (n integer array, 1<=n<=Z)."""
    n = np.asarray(n, np.int64)
    N = Z//n
    th = n/Z
    return th**-0.5*(A[N]+(S[N]+1)*np.log(th)+4*S[N])-4*N

def H_at(n, Z, S, A):
    """H(theta)=int_theta^1 E at theta=n/Z (closed form, T-90001 SS2)."""
    n = np.asarray(n, np.int64); N = Z//n; th = n/Z
    return -2*np.sqrt(th)*(A[N]+(S[N]+1)*np.log(th)+2*S[N]-2)+4*N*th-4

def bX(m, X):
    """b_X on [2,X], zero outside (m array of ints)."""
    m = np.asarray(m, float)
    v = 2*np.sqrt(m)*(np.log(X/m)-2*(1-np.sqrt(m/X)))
    return np.where((m>=2)&(m<=X), v, 0.0)

def v_q(q, X):
    k = np.arange(1, X//q+1, dtype=np.int64)
    return float(np.sum(bX(k*q, X)-bX(k*q+1, X)))

def exact_Ts2(X, primes):
    Y = X//2
    tot = 0.0
    for p in primes[primes<=X]:
        r = v_q(int(p), X) - p**-0.5*math.log(X/p)
        if p<=Y:
            r -= v_q(int(p), Y) - p**-0.5*math.log(Y/p)
        tot += math.log(p)*r
    return tot

def run(X, primes, spf, mu, do_exact=True, nrand=0, do_var=False, blocks=False):
    Y = X//2; c = Y/X
    S, A = profile_tables(X+2)
    n_all = np.arange(1, X+1)
    E_X = E_at(n_all, X, S, A)                       # E(n/X)
    Ec = E_X.copy()
    nY = np.arange(1, Y+1)
    Ec[:Y] -= (X/Y)**0.5 * E_at(nY, Y, S, A)         # E_c(n/X), n<=Y
    Ec_all = np.concatenate(([0.0], Ec))             # index by n
    lg = np.log(np.arange(0, X+1, dtype=float)); lg[0]=0
    pr = primes[primes<=X]
    F = X**-0.5*float(np.sum(np.log(pr)*Ec_all[pr]))         # prime-sum form (theta-form)
    # Lambda-form
    FL = F
    for p in pr[pr<=int(X**0.5)+1]:
        pj = p*p
        while pj<=X:
            FL += X**-0.5*math.log(p)*Ec_all[pj]; pj*=p
    # moat constant at z=2
    HX2 = float(H_at(np.array([2]), X, S, A)[0])
    HY2 = float(H_at(np.array([2]), Y, S, A)[0])
    moat2 = X**0.5*(HX2 - c**0.5*HY2)
    floor = 10.3*(2+math.log(X))
    out = dict(X=X, F=F, FL=FL, moat2=moat2, floor=floor)
    out['C0'] = float(np.max(np.abs(np.sqrt(n_all/X)*Ec)))   # sup |sqrt(th) E_c|
    out['mass'] = X**-0.5*float(np.sum(np.log(pr)*np.abs(Ec_all[pr])))  # trivial prime mass
    if do_exact:
        Ts2 = exact_Ts2(X, primes); out['Ts2']=Ts2; out['resid']=Ts2-F
    if blocks:
        th_v = np.sort(np.concatenate((pr.astype(float), [2.0, float(X)])))
        Hc_at = lambda n,Zn: None
        bl=[]
        R = lambda t: float(np.sum(np.log(pr[pr<=t]))) - t   # R = theta(t)-t
        for i in range(0, int(math.log2(X))-1):
            a, b = max(2, X>>(i+1)), X>>i
            pp = pr[(pr>a)&(pr<=b)]
            Ssum = X**-0.5*float(np.sum(np.log(pp)*Ec_all[pp]))
            # deterministic part: sqrt X [H_c(a/X)-H_c(b/X)]
            def Hc(nn):
                v = float(H_at(np.array([nn]), X, S, A)[0])
                if nn<=Y: v -= c**0.5*float(H_at(np.array([nn]), Y, S, A)[0])
                return v
            det = X**0.5*(Hc(a)-Hc(b))
            fl_i = Ssum-det
            sens = max(abs(R(a)),abs(R(b)))/math.sqrt(a)
            bl.append((i, a, b, fl_i, R(b), sens))
        out['blocks']=bl
    if nrand>0:
        # kernel c_X(k) = X^{-1/2} sum_{m<=X/k} log m * E_c(km/X)
        cker = np.zeros(X+1)
        for k in range(1, X+1):
            M = X//k
            if M==0: break
            m = np.arange(1, M+1)
            cker[k] = np.dot(lg[1:M+1], Ec_all[k*m])
        cker *= X**-0.5
        out['ck_mass'] = float(np.sum(np.abs(cker)))
        out['ck_env'] = float(np.max(np.abs(cker[1:])*np.arange(1,X+1)/(np.log(2*X/np.arange(1,X+1))*X**0.5)))
        shell_mu = float(np.dot(mu[:X+1], cker))     # = Lambda-form identity check
        out['shell_mu'] = shell_mu
        rng = np.random.default_rng(90001)
        f = np.ones(X+1, np.int64)
        vals=[]
        for s_i in range(nrand):
            eps = {int(p): int(rng.integers(0,2)*2-1) for p in pr}
            for n in range(2, X+1):
                f[n] = eps[int(spf[n])]*f[n//spf[n]]
            vals.append(float(np.dot(f[:X+1], cker)))
        vals=np.array(vals)
        out['rand_mean_abs']=float(np.mean(np.abs(vals)))
        out['rand_q90']=float(np.quantile(np.abs(vals),0.9))
        out['rand_max']=float(np.max(np.abs(vals)))
        if do_var:
            # exact E[shell^2] = sum_{d squarefree} ( sum_{a: d a^2 <= X} c(d a^2) )^2
            tot=0.0
            for d in range(1, X+1):
                if mu[d]==0: continue
                s_in=0.0; a=1
                while d*a*a<=X:
                    s_in+=cker[d*a*a]; a+=1
                tot+=s_in*s_in
            out['var_exact']=tot
    return out

def curves(X):
    LL=math.log(math.log(X)); L=math.log(X)
    return dict(
        demand_floor=10.3*(2+L),
        demand_eps01=X**0.1,
        hal_mu=0.66*X**0.5*(1+LL)/L,             # (1+M)e^-M at mu's M ~ loglog X
        hal_ceiling=0.66*X**0.5*(1+2*LL)/L**2,   # M at structural cap 2loglog X
        hal_secondary=0.66*X**0.5*LL/L,          # sharp class secondary term
        vk=X**0.5*math.exp(-0.2098*L**0.6/LL**0.2),
        trivial=0.66*X**0.5)

if __name__=='__main__':
    which = sys.argv[1] if len(sys.argv)>1 else 'small'
    if which=='small':
        Xs=[10**4]; nrand=200; do_var=True
    elif which=='mid':
        Xs=[10**5]; nrand=60; do_var=True
    else:
        Xs=[10**6]; nrand=10; do_var=False
    for X in Xs:
        primes = sieve(X); spf = spf_sieve(X); mu = mobius(X, spf)
        r = run(X, primes, spf, mu, do_exact=True, nrand=nrand, do_var=do_var, blocks=True)
        print(f"\n=== X={X:.0e}  (t={time.time()-t0:.0f}s) ===")
        print(f"exact T^s(2) = {r['Ts2']:+.4f}   F(prime-sum form) = {r['F']:+.4f}   resid = {r['resid']:+.4f}  (floor {r['floor']:.1f})")
        print(f"Lambda-form FL = {r['FL']:+.4f}  (FL-F = {r['FL']-r['F']:+.4f}, pred ~0.165 log X = {0.165*math.log(X):.2f})")
        print(f"sqrt(X) H_c(2/X) = {r['moat2']:+.5f}   (limit -0.90250)")
        print(f"C0 = sup|sqrt(th)E_c| = {r['C0']:.4f}    prime abs mass X^-.5 sum logp|E_c| = {r['mass']:.2f}  ( /sqrt X = {r['mass']/X**0.5:.4f})")
        print(f"shell_mu (sum mu(k)c_k) = {r['shell_mu']:+.4f}  vs FL = {r['FL']:+.4f}  (identity gap {r['shell_mu']-r['FL']:+.2e})")
        print(f"kernel: sum|c_k| = {r['ck_mass']:.1f} = {r['ck_mass']/(X**0.5*math.log(X)**2):.4f}*sqrt(X)log^2X ; env sup k|c_k|/(sqrtX log(2X/k)) = {r['ck_env']:.4f}")
        print(f"random f ({nrand} samples): mean|shell| = {r['rand_mean_abs']:.2f}  q90 = {r['rand_q90']:.2f}  max = {r['rand_max']:.2f}")
        if 'var_exact' in r:
            print(f"exact sqrt(E shell^2) = {r['var_exact']**0.5:.2f}   ( /sqrt X = {r['var_exact']**0.5/X**0.5:.4f}, /(sqrtX loglogX/logX) = {r['var_exact']**0.5/(X**0.5*math.log(math.log(X))/math.log(X)):.3f})")
        cv=curves(X)
        print("curves: " + "  ".join(f"{k}={v:.3g}" for k,v in cv.items()))
        print("blocks (i, a, b, fluct_i, R(b), sens=|R|/sqrt(a)):")
        for b in r['blocks'][:9]:
            print(f"   i={b[0]:2d} ({b[1]:>8d},{b[2]:>8d}]  fl={b[3]:+8.4f}  R(b)={b[4]:+9.2f}  sens={b[5]:8.4f}")
