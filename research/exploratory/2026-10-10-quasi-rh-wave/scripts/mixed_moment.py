# Boundary B under modified inverse capacity (r + z/cI <= 1) and under Target Lemma M
# (mixed second moment sum|M_r S_m|^2 << U^{1+eps} for r+m<=1, which counts every class at R = 1-delta).
# Based on moment2k_v2.py (paper's detector structure, Prop 8.3; Liu/main geometry).
import numpy as np, sys
from math import sqrt
def Rstar(delta, x, kappa=0.75, alpha=5/6, cI=0.5, cP=6.0, tmax=1.5, kP=(2,), lemmaM=False, ngrid=400):
    c = 1.0/(cP*kappa)
    best = np.inf
    for t in np.linspace(1.0, tmax, 101):
        rs = np.linspace(t-0.5, min(t,1.0), ngrid); ms = t - rs
        FI = rs + 2*x*cI*(1-rs)
        FS = np.zeros_like(ms)
        for k in kP:
            ok = k*ms <= 1 + 1e-12
            FS = np.where(ok, np.maximum(FS, k*ms + 2*x*c*(1-k*ms)), FS)
        F = np.maximum(FI, FS)
        if lemmaM:
            # mixed moment counts the split directly with exponent r+m = t when r+m<=1 (t=1 only)
            FM = np.where(rs+ms <= 1+1e-9, rs+ms, 0.0)
            F = np.maximum(F, FM)
        cnt = 1 - delta*F
        short = np.max(cnt)
        long_ = 1 - delta + (alpha-delta)*(t-1)
        best = min(best, max(short, long_))
    RN = 1 - 2*alpha*delta/(3*alpha-delta)
    return min(best, RN)
def E(b, l, delta, x, R):
    h = (1+b+3*l)/2
    return -0.25 + b/6 + 5*l/4 + (0.5+l)*delta + l*x*delta - h*(1-R)
def Blow(l, b): return 11/12 - l/4 + max(0, 8*b+3*l-3)/12 + max(0, 5*l-1)/8
def side_ok(l, b, dmax, d0=0.02, int_lemmaM=False):
    h=(1+b+3*l)/2; ly=(1+b-l)/2; lx=(1-b-l)/2
    if not (b>0 and lx>l and ly>l and 5*l-h>0 and l/h>7/37): return False
    if not (ly/2 - 13*h/75 - 0.02 > 0): return False
    if not (-(-0.25+b/6+5*l/4) - (0.5+1.5*l)*d0 > 0): return False   # floor bin, R=1
    if int_lemmaM:
        # intermediate rows d in [d0,1/2], no primes, counted with R = 1-delta (Lemma M at t=1) instead of 76/75-2delta/3
        # E0(d) = a + h(z0-1/6) - a*ly - l/2 + d(R + delta/2 - z0), a=(1+delta)/2, z0=17/50; need E0 <= B ... use Liu form:
        # E_int(d) = -1/4 + b/6 + 5l/4 + (1/2+l)delta*(d/h)?? -- keep paper's affine form but with R=1-delta: use generic E at d
        for d in (d0, 0.5):
            for delta in (d0, dmax):
                z0=17/50; a=(1+delta)/2
                E0 = a + h*(z0-1/6) - a*ly - l/2 + d*((1-delta) + delta/2 - z0)
                if E0 - Blow(l,b) >= 0: return False
    else:
        for d in (d0, dmax):
            if (225*l+50-75*b)*d + 78*l-49*b-73 >= 0: return False
    return True
def best_B(kappa=0.75, dmax=0.75, nd=60, nx=11, int_lemmaM=False, **kw):
    dgrid=np.linspace(0.02, dmax, nd); xgrid=np.linspace(0,0.5,nx)
    Rtab=np.array([[Rstar(d,x,kappa,**kw) for x in xgrid] for d in dgrid])
    def feas(l):
        best=(np.inf,None,None)
        for b in np.linspace(0.002,0.35,120):
            if not side_ok(l,b,dmax,int_lemmaM=int_lemmaM): continue
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
    print("check R*(dc,1/2)=%.5f (target 2/3); with Lemma M: %.5f (target %.5f)"%(Rstar(dc,0.5),Rstar(dc,0.5,lemmaM=True),1-dc))
    runs=[("baseline (cI=1/2)",{}),
          ("cI=0.6",{"cI":0.6}),("cI=0.75",{"cI":0.75}),("cI=1.0 (r+z<=1)",{"cI":1.0}),
          ("Target Lemma M (R=1-delta all classes, d=h only)",{"lemmaM":True}),
          ("Target Lemma M + intermediate rows at R=1-delta",{"lemmaM":True,"int_lemmaM":True}),
          ("cI=1.0 + intermediate rows at R=1-delta",{"cI":1.0,"int_lemmaM":True}),
          ("Lemma M + cI=1 + cP ideal (2m+z<=1) + int rows",{"lemmaM":True,"cI":1.0,"cP":1/0.75,"int_lemmaM":True}),
          ]
    for lab,kw in runs:
        res=best_B(**kw)
        print(" %-52s B=%.6f l=%.5f b=%.4f crit delta=%.3f x=%.2f R*=%.4f"%((lab,res[0],res[1],res[2])+res[3]) if res else lab+" infeasible", flush=True)
