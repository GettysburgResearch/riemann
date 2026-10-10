import numpy as np, math, json, sys
# Stage 2: masses, gamma_1 projections, beta fits, h-scan. Input: stage1 json.
IN  = sys.argv[1] if len(sys.argv)>1 else 'stage1_test.json'
OUT = sys.argv[2] if len(sys.argv)>2 else 'stage2_test.json'
D=json.load(open(IN))
rows=np.array(D['rows'])   # u, Lambda, W, V, m(u)
u=rows[:,0]; W=rows[:,2]; V=rows[:,3]
L=np.log(u)
g1=14.134725141734695
# dense m up to max u
UM=int(u[-1])+2
mu=np.ones(UM+1,dtype=np.int8); mu[0]=0
for p in range(2,int(UM**0.5)+1):
    if mu[p]==1 or mu[p]==-1:
        # p prime iff untouched by smaller primes? use simple prime sieve instead
        pass
sv=np.ones(UM+1,dtype=bool); sv[:2]=False
for p in range(2,int(UM**0.5)+1):
    if sv[p]: sv[p*p::p]=False
for p in np.nonzero(sv)[0]:
    p=int(p); mu[p::p]*=-1; mu[p*p::p*p]=0
Pp=np.ones(UM+1)
for p in np.nonzero(sv)[0]:
    p=int(p); pk=p
    while pk<=UM: Pp[pk::pk]*=p; pk*=p
nn=np.arange(UM+1,dtype=float)
big=(Pp<nn)&(mu!=0); mu[big]=-mu[big]
m=np.concatenate([[0.],np.cumsum(mu[1:]/nn[1:])])
# trapezoid weights on the (uneven-int) log grid
dL=np.gradient(L)
def massW(X):   # (1/lnT) int u X^2 du/u cumulative on grid
    integ=np.cumsum(u*X*X*dL)
    return integ/L
MW=massW(W); MV=massW(V)
# m mass dense: Q(T)=sum_{n<T} m(n)^2 (m const on [n,n+1))
n_=np.arange(1,UM)
Qm=np.concatenate([[0.],np.cumsum(m[1:UM]**2)])  # Qm[k]=int_1^{k+1} m^2 du
def Mm_at(T):
    k=int(T)-1
    return (Qm[k]+ (T-int(T))*m[int(T)]**2)/math.log(T)
# decade table
Ts=[t for t in [100,316,1000,3162,10000,12600] if t<=u[-1]]
tab=[(T, float(MW[np.searchsorted(u,T,side='right')-1]),
        float(MV[np.searchsorted(u,T,side='right')-1]), Mm_at(T)) for T in Ts]
print('T      massW     massV     mass_m   ratio W/m')
for T,a,b,c in tab: print('%6d  %.5f  %.5f  %.5f   %.3f'%(T,a,b,c,a/c if c else 0))
# sliding-window gamma_1 projection
def proj(A, width=2.0, step=0.25):
    cs=[]; amps=[]
    Lmin,Lmax=L[0],L[-1]
    c=Lmin+width/2
    ph=np.exp(-1j*g1*L)
    while c+width/2<=Lmax+1e-9:
        w=(L>=c-width/2)&(L<c+width/2)
        if w.sum()>10:
            a=np.sum(A[w]*ph[w]*dL[w])/np.sum(dL[w])
            cs.append(c); amps.append(abs(a))
        c+=step
    return np.array(cs), np.array(amps)
def proj_m(width=2.0, step=0.25):
    # exact stepwise integral of sqrt(u) m(u) u^{-i g1} dln u = m(n) int_n^{n+1} u^{-1/2-i g1} du
    ex=0.5-1j*g1
    upow=(nn[2:UM+1]**ex - nn[1:UM]**ex)/ex   # int_n^{n+1} u^{-1/2-ig1} du for n=1..UM-1
    ln_n=np.log(nn[1:UM])
    cs=[]; amps=[]
    c=math.log(20)+width/2
    while c+width/2<=math.log(UM-1):
        lo,hi=math.exp(c-width/2),math.exp(c+width/2)
        wsel=(nn[1:UM]>=lo)&(nn[1:UM]<hi)
        a=np.sum(m[1:UM][wsel]*upow[wsel])/(math.log(hi)-math.log(lo))
        cs.append(c); amps.append(abs(a))
        c+=step
    return np.array(cs), np.array(amps)
cW,aW=proj(np.sqrt(u)*W); cV,aV=proj(np.sqrt(u)*V); cm,am=proj_m()
def beta_fit(cs,amps,cmin=3.5):
    sel=(cs>=cmin)&(amps>0)
    x=np.log(cs[sel]); y=np.log(amps[sel])
    A=np.vstack([np.ones_like(x),x]).T
    coef,res,_,_=np.linalg.lstsq(A,y,rcond=None)
    yhat=A@coef; sd=float(np.std(y-yhat))
    n=len(x); se=sd/math.sqrt(max(n,2))/np.std(x) if np.std(x)>0 else 0
    return float(-coef[1]), float(se), float(math.exp(coef[0]))
bW=beta_fit(cW,aW); bV=beta_fit(cV,aV); bm=beta_fit(cm,am)
print('beta (amp ~ (ln u)^-beta):  W: %.3f+-%.3f  V: %.3f+-%.3f  m: %.3f+-%.3f'%(bW[0],bW[1],bV[0],bV[1],bm[0],bm[1]))
# h-scan J(h): grid version for W,V; dense for m
hs=[0.5,0.35,0.25,0.18,0.125,0.09,0.0625,0.044]
Jm=[float(np.sum(m[1:UM]**2 * nn[1:UM]**(-2*h))) for h in hs]
JW=[float(np.sum(u*W*W*np.exp(-2*h*L)*dL)) for h in hs]
JV=[float(np.sum(u*V*V*np.exp(-2*h*L)*dL)) for h in hs]
print('h      h*J_W    h*J_V    h*J_m    J_W/ln(1/h)')
for i,h in enumerate(hs):
    print('%.4f  %.4f  %.4f  %.4f  %.4f'%(h,h*JW[i],h*JV[i],h*Jm[i],JW[i]/math.log(1/h)))
# tracking: corr sqrt(u)W vs sqrt(u)m on grid
sm=np.array([m[int(x)] for x in u])
X1=np.sqrt(u)*W; X2=np.sqrt(u)*sm
cc=float(np.corrcoef(X1,X2)[0,1])
sl=float(np.sum(X1*X2)/np.sum(X2*X2))
print('corr(sqrt(u)W, sqrt(u)m)=%.4f  regression slope=%.4f'%(cc,sl))
json.dump({'mass_table':tab,'beta':{'W':bW,'V':bV,'m':bm},
 'proj_W':[list(map(float,cW)),list(map(float,aW))],
 'proj_V':[list(map(float,cV)),list(map(float,aV))],
 'proj_m':[list(map(float,cm)),list(map(float,am))],
 'hscan':{'h':hs,'JW':JW,'JV':JV,'Jm':Jm},
 'corr':cc,'slope':sl},open(OUT,'w'))
print('wrote',OUT)
