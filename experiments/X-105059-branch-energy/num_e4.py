import numpy as np, math
# Lambda functional sanity: measured vs branch model prediction, coupled U=isqrt(N)
NP=2*10**6
pr=np.ones(NP+1,dtype=bool); pr[:2]=False
for p in range(2,int(NP**0.5)+1):
    if pr[p]: pr[p*p::p]=False
prm=np.nonzero(pr)[0]
K=25
eta_k=np.ones(K)
for k in range(1,K): eta_k[k]=eta_k[k-1]*(2*k-1)/(2*k)
eta=np.ones(NP+1); eta[0]=0
mu=np.ones(NP+1); mu[0]=0
for p in prm:
    pl=int(p); eta[pl::pl]*=eta_k[1]; mu[pl::pl]*=-1
    pk=pl*pl;k=2
    while pk<=NP:
        eta[pk::pk]*=eta_k[k]/eta_k[k-1]
        if k==2: mu[pk::pk]=0
        pk*=pl;k+=1
nn=np.arange(NP+1,dtype=np.float64); nn[0]=1
m=np.cumsum(mu/nn)
def h_arr(N,U):
    g=mu.copy()  # placeholder; build h = (mu 1_{>U})*eta directly
    h=np.zeros(N+1)
    # h = g_full - sum_{d<=U} mu(d) eta(n/d), g_full = mu*eta = g coefficients of zeta^{-1/2}
    # build g quickly: g multiplicative; use recursion g = mu*eta via full conv too slow; use:
    # h(n) = sum_{d|n, d>U} mu(d) eta(n/d) computed by sieve over d>U
    for d in range(U+1, N+1):
        md=mu[d]
        if md:
            h[d::d]+=md*eta[:N//d+1][1:len(h[d::d])+1]
    return h
ln2=math.log(2)
print('U    N       Lambda_meas   Lambda_pred(K=-sqrt2 m)  ratio')
for N in [10**5, 3*10**5, 10**6, 2*10**6]:
    U=int(math.isqrt(N))
    h=h_arr(N,U)
    ns=np.arange(1,N+1,dtype=np.float64)
    idx=np.arange(N//2+1,N+1)
    lam=np.sum(h[idx]/np.sqrt(idx)*np.log(2*idx/N)/ln2)
    mU=m[U]; Kp=-math.sqrt(2)*mU
    kap=-2*Kp/math.sqrt(math.pi*math.log(N))
    pred=0.15466*kap*math.sqrt(N)   # 1-(2/ln2)(1-1/sqrt2)
    print(U,N,round(lam,4),round(pred,4),round(lam/pred,3) if pred else '-')
