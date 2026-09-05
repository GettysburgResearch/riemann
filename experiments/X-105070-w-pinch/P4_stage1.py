import numpy as np, math, json, sys, time
# Stage 1: compute Lambda(u), W_u on log grid via prefix-sum trick; validate vs brute force.
NMAX = int(sys.argv[1]) if len(sys.argv)>1 else 4*10**6
OUT  = sys.argv[2] if len(sys.argv)>2 else 'stage1_test.json'
t0=time.time()
umax = int(math.isqrt(NMAX))
# ---- mobius sieve up to NMAX (int8) using primes<=sqrt(NMAX) + large-prime fix
mu = np.ones(NMAX+1, dtype=np.int8); mu[0]=0
P  = np.ones(NMAX+1, dtype=np.float64)
sieve = np.ones(umax+1, dtype=bool); sieve[:2]=False
for p in range(2,int(umax**0.5)+1):
    if sieve[p]: sieve[p*p::p]=False
primes = np.nonzero(sieve)[0]
for p in primes:
    p=int(p)
    mu[p::p] *= -1
    mu[p*p::p*p] = 0
    pk=p
    while pk<=NMAX:
        P[pk::pk]*=p; pk*=p
n_ar = np.arange(NMAX+1, dtype=np.float64)
big = (P < n_ar) & (mu!=0)   # remaining single large prime factor
mu[big] = -mu[big]
del P, big
print('sieve done', time.time()-t0)
# ---- eta up to umax
K=30
eta_k=np.ones(K)
for k in range(1,K): eta_k[k]=eta_k[k-1]*(2*k-1)/(2*k)
eta=np.ones(umax+1); eta[0]=0
for p in primes:
    p=int(p); pk=p; k=1
    while pk<=umax:
        eta[pk::pk]*=eta_k[k]/max(eta_k[k-1],1e-300); pk*=p; k+=1
# fix: above multiplies ratio at p^k for all multiples of p^k => net eta_k[k] at exact power k. ok
# ---- prefix sums Phi0=cumsum(mu(d)/sqrt(d)), Phi1=cumsum(mu(d) ln d/sqrt(d)), mprefix=cumsum(mu/n)
sq = np.sqrt(n_ar[1:])
lg = np.log(n_ar[1:])
mud = mu[1:].astype(np.float64)
Phi0 = np.concatenate([[0.0], np.cumsum(mud/sq)])
Phi1 = np.concatenate([[0.0], np.cumsum(mud*lg/sq)])
mpre = np.concatenate([[0.0], np.cumsum(mud/n_ar[1:])])   # m(u)=mpre[u]
del sq, lg, mud
print('prefix done', time.time()-t0)
ln2=math.log(2)
def Lambda_fast(u):
    N=u*u
    emax=N//(u+1)
    e=np.arange(1,emax+1)
    hi=N//e
    lo=np.maximum(u, N//(2*e))
    good=hi>lo
    e=e[good]; hi=hi[good]; lo=lo[good]
    d0=Phi0[hi]-Phi0[lo]; d1=Phi1[hi]-Phi1[lo]
    c = np.log(2.0*e/N)
    return float(np.sum(eta[e]/np.sqrt(e)*(d1 + c*d0))/ln2)
def Lambda_brute(u):
    N=u*u
    h=np.zeros(N+1)
    for d in range(u+1,N+1):
        md=mu[d]
        if md:
            q=N//d
            h[d::d]+=md*eta[1:q+1]
    idx=np.arange(N//2+1,N+1)
    return float(np.sum(h[idx]/np.sqrt(idx)*np.log(2*idx/N)/ln2))
# validation on small u
val={}
for u in [50,101,200,316]:
    if u*u<=NMAX and u*u<=4*10**5:
        a=Lambda_fast(u); b=Lambda_brute(u)
        val[u]=(a,b)
        print('validate u=%d fast=%.6f brute=%.6f diff=%.2e'%(u,a,b,abs(a-b)))
# ---- grid
grid=[]
lnu=math.log(20)
uprev=0
while True:
    u=int(round(math.exp(lnu)))
    if u*u>NMAX: break
    if u>uprev: grid.append(u); uprev=u
    lnu+=0.02
res=[]
for u in grid:
    lam=Lambda_fast(u)
    N=u*u
    W=lam*math.sqrt(math.log(N))/u
    V=lam/u
    res.append((u,lam,W,V,float(mpre[u])))
print('grid done', len(grid), time.time()-t0)
json.dump({'NMAX':NMAX,'validate':val,'cols':'u,Lambda,W,V,m(u)','rows':res}, open(OUT,'w'))
print('wrote',OUT)
