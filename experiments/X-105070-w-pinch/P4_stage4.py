import numpy as np, math, json
# Stage 4: (a) within-U-cell N-sweep of Lambda; (b) frequency scan of W-projection around gamma_1.
# Rebuild small sieve up to 9e6 (u<=3000) for cell sweeps.
NM=9*10**6
sv=np.ones(int(NM**0.5)+1,dtype=bool); sv[:2]=False
for p in range(2,int(len(sv)**0.5)+1):
    if sv[p]: sv[p*p::p]=False
primes=np.nonzero(sv)[0]
mu=np.ones(NM+1,dtype=np.int8); mu[0]=0
P=np.ones(NM+1)
for p in primes:
    p=int(p); mu[p::p]*=-1; mu[p*p::p*p]=0
    pk=p
    while pk<=NM: P[pk::pk]*=p; pk*=p
nn=np.arange(NM+1,dtype=float)
big=(P<nn)&(mu!=0); mu[big]=-mu[big]
del P
mud=mu[1:].astype(float)
Phi0=np.concatenate([[0.],np.cumsum(mud/np.sqrt(nn[1:]))])
Phi1=np.concatenate([[0.],np.cumsum(mud*np.log(nn[1:])/np.sqrt(nn[1:]))])
umax=3000
K=30; eta_k=np.ones(K)
for k in range(1,K): eta_k[k]=eta_k[k-1]*(2*k-1)/(2*k)
eta=np.ones(umax+1); eta[0]=0
for p in primes:
    p=int(p)
    if p>umax: break
    pk=p;k=1
    while pk<=umax:
        eta[pk::pk]*=eta_k[k]/eta_k[k-1]; pk*=p; k+=1
ln2=math.log(2)
def Lam(U,N):
    emax=N//(U+1)
    e=np.arange(1,emax+1)
    hi=N//e; lo=np.maximum(U,N//(2*e))
    g=hi>lo; e=e[g];hi=hi[g];lo=lo[g]
    return float(np.sum(eta[e]/np.sqrt(e)*((Phi1[hi]-Phi1[lo])+np.log(2.0*e/N)*(Phi0[hi]-Phi0[lo])))/ln2)
print('(a) within-cell sweep: u, W_anchor(N=u^2), mean W over N in [u^2,u^2+3u], rms, min, max')
cell={}
for u in [300,700,1500,2500]:
    Ns=np.arange(u*u,u*u+3*u+1, max(1,(3*u)//60))
    Ws=np.array([Lam(u,int(N))*math.sqrt(math.log(N))/u for N in Ns])
    cell[u]=[float(Ws[0]),float(Ws.mean()),float(np.sqrt((Ws**2).mean())),float(Ws.min()),float(Ws.max())]
    print(' u=%d  anchor=%.5f mean=%.5f rms=%.5f min=%.5f max=%.5f'%(u,Ws[0],Ws.mean(),np.sqrt((Ws**2).mean()),Ws.min(),Ws.max()))
# (b) frequency scan using stage1_big grid
D=json.load(open('stage1_big.json'))
rows=np.array(D['rows']); u=rows[:,0]; W=rows[:,2]
L=np.log(u); dL=np.gradient(L)
A=np.sqrt(u)*W
sel=L>=3.0
freqs=np.arange(8.0,22.01,0.25)
g1=14.134725141734695
freqs=np.sort(np.concatenate([freqs,[g1,21.022039639]]))  # gamma_2=21.0220
amps=[abs(np.sum(A[sel]*np.exp(-1j*f*L[sel])*dL[sel])/np.sum(dL[sel])) for f in freqs]
print('(b) global projection |a(f)| of sqrt(u)W_u, f in [8,22]:')
for f,a in zip(freqs,amps): print('   f=%.3f  %.5f'%(f,a))
json.dump({'cell':cell,'freq':[list(map(float,freqs)),list(map(float,amps))]},open('stage4.json','w'))
print('wrote stage4.json')
