import numpy as np, json, math
from mpmath import mp, quad, mpf, sqrt as msqrt, log as mlog, exp as mexp, pi as mpi
mp.dps = 30
out={}
# 1) I_w exact identity check: I_w = int_R w/(1+4g^2) dg vs 2*pi*(3 ln2 - 2)
ln2=mlog(2)
def w_of(g):
    s=1j*g
    v=(1-mexp(-s*ln2))*(1-msqrt(2)*mexp(-s*ln2))/s
    return abs(v)**2
Iw = 2*quad(lambda g: w_of(g)/(1+4*g*g), [mpf('1e-8'),1,10,100,1000,10000,mp.inf])
pred = 2*mpi*(3*ln2-2)
out['I_w_quad']=float(Iw); out['I_w_closed_form_2pi(3ln2-2)']=float(pred)
out['I_w_reldiff']=float(abs(Iw-pred)/pred)
# 2) mu sieve to 1.1e6 ; m(u); dyadic block masses of u m(u)^2 in du/u ~ sum m(n)^2
NP=1100000
mu=np.ones(NP+1,dtype=np.int64); mu[0]=0
pr=np.ones(NP+1,dtype=bool); pr[:2]=False
for p in range(2,int(NP**0.5)+1):
    if pr[p]:
        pr[p*p::p]=False
        mu[p::p]*=-1; mu[p*p::p*p]=0
# fix: need mu via factor counting; redo properly
mu=np.ones(NP+1,dtype=np.float64); mu[0]=0
for p in range(2,int(NP**0.5)+1):
    if pr[p]: mu[p::p]*=-1; mu[p*p::p*p]=0
# primes > sqrt(NP) handled: numbers with a large prime factor p>sqrt get *-1 automatically? No.
# safer: standard linear count of prime factors
mu=np.ones(NP+1,dtype=np.float64); mu[0]=0
prm=np.nonzero(pr)[0]
big=np.arange(NP+1,dtype=np.int64)
for p in prm:
    mu[p::p]*=-1
    mu[p*p::p*p]=0
    big[p::p]//=p; big[p*p::p*p]=1  # crude; big track only for full division once... skip
# numbers n whose largest prime factor > sqrt(NP): p appears once; loop above covers ALL primes<=NP? prm only <=NP.
# pr sieve was only marked composite for p<=sqrt: primes up to NP are correctly in prm? pr[p*p::p] for p<=sqrt marks all composites. yes prm=all primes<=NP.
nn=np.arange(NP+1,dtype=np.float64); nn[0]=1
m=np.cumsum(mu/nn)
out['m_check']= {'m(100)':float(m[100]),'m(10000)':float(m[10000]),'m(1000000)':float(m[1000000])}
# dyadic blocks j: int_{2^j}^{2^{j+1}} u m^2 du/u ~= sum_{2^j<n<=2^{j+1}} m(n)^2
c0=0.0158924; ln2f=math.log(2)
blocks={}
Q=np.cumsum(m**2)
for j in range(7,20):
    hi=min(2**(j+1),NP)
    blocks[j]=float(Q[hi]-Q[2**j])
out['blocks_um2']={str(j):round(v,5) for j,v in blocks.items()}
out['c0_log2']=round(c0*ln2f,5)
json.dump(out,open('num1.json','w'),indent=1)
print(json.dumps(out,indent=1))
