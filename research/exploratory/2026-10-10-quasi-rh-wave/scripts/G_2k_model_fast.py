import numpy as np, sys
from math import sqrt
sys.path.insert(0,'.')
from stage3_closed import E, Blow, side_ok
ALPHA=5/6
TS=np.linspace(1.0,1.5,26); SS=np.linspace(0,0.5,11); RS=np.linspace(0,1.5,151)
def Rstar(delta,x,kappa,mode):
    best=np.inf
    for t in TS:
        r=RS[(RS>=t-0.5-1e-9)&(RS<=t+1e-9)]
        R,S=np.meshgrid(r,SS,indexing='ij'); M=t+S-R
        ok=(M>=-1e-9)&(M<=0.5+1e-9); M=np.clip(M,0,0.5)
        cnt=np.where(R<=1, 1-delta*R-x*delta*(1-R), 1-ALPHA+(ALPHA-delta)*R)
        cnt=np.minimum(cnt, 1-2*delta*M-2*x*delta*np.maximum(0,1-2*M)/(6*kappa))
        if mode.get('huxley'): cnt=np.minimum(cnt, np.maximum(R-delta*R, 1+R-3*delta*R))
        if mode.get('hybrid') is not None:
            cnt=np.where(R+M<=mode['hybrid']+1e-9, np.minimum(cnt,1-delta*(R+M)), cnt)
        if mode.get('ideal'): cnt=np.minimum(cnt,1-delta)
        worst=np.max(np.where(ok,cnt,-np.inf))
        best=min(best, max(worst, 1-delta+(ALPHA-delta)*(t-1)))
    return min(best, 1-2*ALPHA*delta/(3*ALPHA-delta))
def best_B(kappa,dmax,mode,d0=0.02,nd=60,nx=21):
    dg=np.linspace(d0,dmax,nd); xg=np.linspace(0,0.5,nx)
    Rt=np.array([[Rstar(d,x,kappa,mode) for x in xg] for d in dg])
    D,X=np.meshgrid(dg,xg,indexing='ij')
    def feas(l):
        best=(np.inf,None,None)
        for b in np.linspace(0.002,0.35,350):
            if not side_ok(l,b,dmax,d0): continue
            h=(1+b+3*l)/2; Ev=-0.25+b/6+5*l/4+(0.5+l)*D+l*X*D-h*(1-Rt)
            i=np.unravel_index(np.argmax(Ev),Ev.shape); w=Ev[i]
            if w<best[0]: best=(w,b,(dg[i[0]],xg[i[1]],Rt[i]))
        return best
    lo,hi=0.164,0.30
    if feas(lo)[0]>0: return None
    for _ in range(30):
        mid=(lo+hi)/2
        if feas(mid)[0]<=0: lo=mid
        else: hi=mid
    w,b,arg=feas(lo); return Blow(lo,b),lo,b,arg
if __name__=="__main__":
    dc=(49-sqrt(921))/48
    for name,mode in [("baseline",{}),("Huxley large values M_r",{'huxley':True}),("hybrid r+m<=1",{'hybrid':1.0}),
                      ("hybrid r+m<=1.125",{'hybrid':1.125}),("hybrid r+m<=1.25",{'hybrid':1.25}),("hybrid r+m<=1.5",{'hybrid':1.5}),("ideal 1-delta",{'ideal':True})]:
        print("%-28s R*(crit)=%.4f"%(name,Rstar(dc,0.5,0.75,mode)), end='  ')
        res=best_B(0.75,0.75,mode)
        print("B=%.6f l=%.5f b=%.4f crit=(%.3f,%.3f,%.4f)"%((res[0],res[1],res[2])+res[3]) if res else "infeasible", flush=True)
