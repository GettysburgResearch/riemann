import numpy as np
from math import sqrt
# Closed-form row-count exponent. cI: inverse capacity z<=cI(1-r) (paper: 1/2); cP: plain capacity z<=(1-2m)/(cP*kappa) (paper cP=6)
def Rstar(delta, x, kappa, alpha=5/6, cI=0.5, cP=6.0, tmax=1.5):
    ck = 1.0/(cP*kappa)
    # F_I = r + 2x cI (1-r) ; F_S = 2m + 2x ck (1-2m), m=t-r  (uncapped branches; caps never bind here)
    aI = 2*x*cI; bI = 1-2*x*cI            # F_I = aI + bI r
    aS = 2*x*ck; bS = 2-4*x*ck            # F_S = aS + bS (t-r)
    # crossing: aI + bI r = aS + bS t - bS r  => r = (aS - aI + bS t)/(bI + bS)
    # saving S(t) = aI + bI r*(t) = S0 + S1 t
    S1 = bI*bS/(bI+bS); S0 = aI + bI*(aS-aI)/(bI+bS)
    def short(t):
        r = (aS - aI + bS*t)/(bI+bS)
        if r > 1: r = 1.0
        if r < t-0.5: r = t-0.5
        return 1 - delta*max(aI+bI*r, aS+bS*(t-r))
    def long_(t): return 1 - delta + (alpha-delta)*(t-1)
    tstar = (alpha - delta*S0)/(delta*S1 + alpha - delta) if (delta*S1+alpha-delta)>0 else tmax
    ts = [1.0, tmax, min(max(tstar,1.0),tmax)]
    vals = [max(short(t), long_(t)) for t in ts]
    RN = 1 - 2*alpha*delta/(3*alpha-delta)
    return min(min(vals), RN)

def E(b, l, delta, x, R):
    h = (1+b+3*l)/2
    return -0.25 + b/6 + 5*l/4 + (0.5+l)*delta + l*x*delta - h*(1-R)
def Blow(l, b): return 11/12 - l/4 + max(0, 8*b+3*l-3)/12 + max(0, 5*l-1)/8
def side_ok(l, b, dmax, d0=0.02):
    h=(1+b+3*l)/2; ly=(1+b-l)/2; lx=(1-b-l)/2
    if not (b>0 and lx>l and ly>l and 5*l-h>0 and l/h>7/37): return False
    if not (ly/2 - 13*h/75 - 0.02 > 0): return False
    if not (-(-0.25+b/6+5*l/4) - (0.5+1.5*l)*d0 > 0): return False      # floor bin, R=1, q<=d0/2
    for d in (d0, dmax):
        if (225*l+50-75*b)*d + 78*l-49*b-73 >= 0: return False            # intermediate rows d=1/2
    return True

def best_B(kappa, dmax, alpha=5/6, cI=0.5, cP=6.0, tmax=1.5, Rshift=0.0, d0=0.02, nd=120, nx=41):
    dgrid=np.linspace(d0, dmax, nd); xgrid=np.linspace(0,0.5,nx)
    Rtab=np.array([[Rstar(d,x,kappa,alpha,cI,cP,tmax)-Rshift for x in xgrid] for d in dgrid])
    def feas(l):
        best=(np.inf,None,None)
        for b in np.linspace(0.002,0.35,350):
            if not side_ok(l,b,dmax,d0): continue
            w=-np.inf; arg=None
            for i,d in enumerate(dgrid):
                for j,x in enumerate(xgrid):
                    e=E(b,l,d,x,Rtab[i,j])
                    if e>w: w,arg=e,(d,x,Rtab[i,j])
            if w<best[0]: best=(w,b,arg)
        return best
    lo,hi=0.164,0.26
    if feas(lo)[0]>0: return None
    for _ in range(36):
        mid=(lo+hi)/2
        if feas(mid)[0]<=0: lo=mid
        else: hi=mid
    w,b,arg=feas(lo)
    return Blow(lo,b), lo, b, arg

if __name__=="__main__":
    dc=(49-sqrt(921))/48
    print("check R*(dc,1/2;3/4)=%.6f (should be 2/3)"%Rstar(dc,0.5,0.75))
    base=best_B(0.75,5/6)
    print("Liu setting kappa=3/4, dmax=5/6: B=%.7f l=%.6f b=%.5f crit=%s"%base)
    print("\n== stage-3 iteration from B1=7/8 (kappa=dmax=2B1-1) ==")
    B=0.875
    for it in range(4):
        k=2*B-1; res=best_B(k,k); print(" iter %d: B1=%.8f -> Phi=%.8f  (l=%.6f b=%.5f crit delta=%.4f x=%.3f R*=%.4f)"%((it,B,res[0],res[1],res[2])+res[3])); B=res[0]
    print("\n== hypothetical: Lemma 18.1 unchanged down to kappa=1/2 (beta*=3/4 input) ==")
    for k in (0.7,0.6,0.5):
        res=best_B(k,k); print(" kappa=%.2f: B=%.7f (l=%.6f b=%.5f crit delta=%.4f x=%.3f R*=%.4f)"%((k,res[0],res[1],res[2])+res[3]))
    print("\n== sensitivities at kappa=3/4, dmax=3/4 (7/8 input) ==")
    for lab,kw in [("baseline",{}),("alpha=0.80",{"alpha":0.80}),("alpha=0.75",{"alpha":0.75}),("alpha=0.70",{"alpha":0.70}),
                   ("inverse cap cI=0.6",{"cI":0.6}),("inverse cap cI=0.75",{"cI":0.75}),("inverse cap cI=1.0",{"cI":1.0}),
                   ("plain cap cP=4",{"cP":4.0}),("plain cap cP=2",{"cP":2.0}),("tmax=2",{"tmax":2.0}),
                   ("R* - 0.02 all classes",{"Rshift":0.02}),("R* - 0.05",{"Rshift":0.05}),("R* - 0.10",{"Rshift":0.10}),("R* - 0.2",{"Rshift":0.2}),
                   ("floor d0=0.002",{"d0":0.002})]:
        res=best_B(0.75,0.75,**kw)
        print(" %-24s B=%.7f l=%.6f b=%.5f crit delta=%.4f x=%.3f R*=%.4f"%((lab,res[0],res[1],res[2])+res[3]) if res else lab+" infeasible")
