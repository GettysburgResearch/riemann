# Generalized 2k-th plain-moment dial, corrected to the paper's detector structure (Prop 8.3):
# row split (r, m) with r in [t-1/2, min(t,1)], m = t - r <= 1/2; count = 1 - delta*max(F_I(r), F_S(m)); worst r.
# F_I(r) = r + 2x cI (1-r)  [Lemma 17.1 + zM=(1-r)/2];  rows with r>1: long count L(t)=1-delta+(alpha-delta)(t-1).
# F_S(m) = max over k in kP with k m <= 1 of [k m + 2 x c (1 - k m)],  c = 1/(6 kappa)   (k=2 is Lemma 18.1).
import numpy as np
from math import sqrt
def Rstar(delta, x, kappa=0.75, alpha=5/6, cI=0.5, cP=6.0, tmax=1.5, kP=(2,), ngrid=400):
    c = 1.0/(cP*kappa)
    best = np.inf
    for t in np.linspace(1.0, tmax, 101):
        rs = np.linspace(t-0.5, min(t,1.0), ngrid); ms = t - rs
        FI = rs + 2*x*cI*(1-rs)
        FS = np.zeros_like(ms)
        for k in kP:
            ok = k*ms <= 1 + 1e-12
            FS = np.where(ok, np.maximum(FS, k*ms + 2*x*c*(1-k*ms)), FS)
        cnt = 1 - delta*np.maximum(FI, FS)
        short = np.max(cnt)
        long_ = 1 - delta + (alpha-delta)*(t-1)
        best = min(best, max(short, long_))
    RN = 1 - 2*alpha*delta/(3*alpha-delta)
    return min(best, RN)
def E(b, l, delta, x, R):
    h = (1+b+3*l)/2
    return -0.25 + b/6 + 5*l/4 + (0.5+l)*delta + l*x*delta - h*(1-R)
def Blow(l, b): return 11/12 - l/4 + max(0, 8*b+3*l-3)/12 + max(0, 5*l-1)/8
def side_ok(l, b, dmax, d0=0.02):
    h=(1+b+3*l)/2; ly=(1+b-l)/2; lx=(1-b-l)/2
    if not (b>0 and lx>l and ly>l and 5*l-h>0 and l/h>7/37): return False
    if not (ly/2 - 13*h/75 - 0.02 > 0): return False
    if not (-(-0.25+b/6+5*l/4) - (0.5+1.5*l)*d0 > 0): return False
    for d in (d0, dmax):
        if (225*l+50-75*b)*d + 78*l-49*b-73 >= 0: return False
    return True
def best_B(kappa=0.75, dmax=0.75, nd=60, nx=11, **kw):
    dgrid=np.linspace(0.02, dmax, nd); xgrid=np.linspace(0,0.5,nx)
    Rtab=np.array([[Rstar(d,x,kappa,**kw) for x in xgrid] for d in dgrid])
    def feas(l):
        best=(np.inf,None,None)
        for b in np.linspace(0.002,0.35,120):
            if not side_ok(l,b,dmax): continue
            Ev = np.array([[E(b,l,d,x,Rtab[i,j]) for j,x in enumerate(xgrid)] for i,d in enumerate(dgrid)])
            i,j = np.unravel_index(np.argmax(Ev), Ev.shape)
            if Ev[i,j]<best[0]: best=(Ev[i,j],b,(dgrid[i],xgrid[j],Rtab[i,j]))
        return best
    lo,hi=0.164,0.26
    if feas(lo)[0]>0: return None
    for _ in range(24):
        mid=(lo+hi)/2
        if feas(mid)[0]<=0: lo=mid
        else: hi=mid
    w,b,arg=feas(lo)
    return Blow(lo,b), lo, b, arg
if __name__=="__main__":
    dc=(49-sqrt(921))/48
    print("check R*(dc,1/2)=%.5f (target 2/3)"%Rstar(dc,0.5))
    for lab,kw in [("baseline plain k=2",{}),("plain k in {2,3}",{"kP":(2,3)}),("plain k in {2,3,4}",{"kP":(2,3,4)}),
                   ("plain k in {2..8}",{"kP":tuple(range(2,9))}),("plain k in {2..40}",{"kP":tuple(range(2,41))}),
                   ("k in {2..40} and alpha=0.75",{"kP":tuple(range(2,41)),"alpha":0.75}),
                   ("k in {2..40} and cI=0.75",{"kP":tuple(range(2,41)),"cI":0.75})]:
        res=best_B(**kw)
        print(" %-32s B=%.6f l=%.5f b=%.4f crit delta=%.3f x=%.2f R*=%.4f"%((lab,res[0],res[1],res[2])+res[3]) if res else lab+" infeasible", flush=True)
