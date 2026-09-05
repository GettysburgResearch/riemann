import numpy as np, math, json
# Stage 5: (a) pointwise |F(-1/2+h+i g1)| exponents (mission item 2, feasible-h window);
# (b) pipeline validation on synthetic half/full-pole densities.
D=json.load(open('stage1_big.json'))
rows=np.array(D['rows']); u=rows[:,0]; W=rows[:,2]; V=rows[:,3]; msamp=rows[:,4]
L=np.log(u); dL=np.gradient(L)
g1=14.134725141734695
hs=np.array([0.6,0.45,0.35,0.27,0.2,0.15,0.11,0.08])
def F(A,h):  # F(s)=int A_u u^{1/2-h} e^{-i g1 lnu} dlnu  with A=u^{1/2}X convention: pass X*u^{1/2}?
    return abs(np.sum(A*np.exp((-h)*L)*np.exp(-1j*g1*L)*dL))
res={}
print('(a) pointwise |F_X(-1/2+h+i*g1)|, X in {W,V,m}; local slope dln|F|/dln h (full pole -> -1, half -> -0.5)')
for name,X in [('W',np.sqrt(u)*W),('V',np.sqrt(u)*V),('m',np.sqrt(u)*msamp)]:
    vals=np.array([F(X,h) for h in hs])
    sl=np.diff(np.log(vals))/np.diff(np.log(hs))
    res[name]=[list(map(float,vals)),list(map(float,sl))]
    print(' %s |F|: '%name, ' '.join('%.4f'%v for v in vals))
    print('   local exp:', ' '.join('%+.2f'%s for s in sl), ' (h pairs %.2f..%.2f; trunc-floor when h*lnT<~1: lnT=%.1f)'%(hs[0],hs[-1],L[-1]))
# (b) synthetic validation on same grid/pipeline
def proj_beta(A,width=2.0,step=0.25,cmin=3.0):
    ph=np.exp(-1j*g1*L); cs=[];amps=[]
    c=L[0]+width/2
    while c+width/2<=L[-1]+1e-9:
        w=(L>=c-width/2)&(L<c+width/2)
        if w.sum()>10:
            cs.append(c); amps.append(abs(np.sum(A[w]*ph[w]*dL[w])/np.sum(dL[w])))
        c+=step
    cs=np.array(cs);amps=np.array(amps)
    sel=cs>=cmin
    x=np.log(cs[sel]);y=np.log(amps[sel])
    M=np.vstack([np.ones_like(x),x]).T
    coef,_,_,_=np.linalg.lstsq(M,y,rcond=None)
    return -coef[1]
half=np.cos(g1*L)/np.sqrt(L)          # half-pole density (model of .6)
full=np.cos(g1*L)                     # restored
b1=proj_beta(half); b2=proj_beta(full); b3=proj_beta(half*np.sqrt(2*L))  # sqrt(lnN)=sqrt(2 lnu)
print('(b) synthetic: beta(half)=%.3f (truth .5), beta(full)=%.3f (0), beta(half*sqrt(lnN))=%.3f (0)'%(b1,b2,b3))
res['synthetic']=[float(b1),float(b2),float(b3)]
json.dump(res,open('stage5.json','w'))
print('wrote stage5.json')
