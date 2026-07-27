from flint import arb, ctx
import math,json,sys,time

def ppowers(limit):
    f=bytearray(b'\x01')*(limit+1); f[0:2]=b'\x00\x00'
    for p in range(2,math.isqrt(limit)+1):
        if f[p]:
            st=p*p; f[st:limit+1:p]=b'\x00'*(((limit-st)//p)+1)
    out=[]
    for p in range(2,limit+1):
        if f[p]:
            n=p
            while n<=limit: out.append((n,p)); n*=p
    return sorted(out)
class Smooth:
    def __init__(self): self.k1=(arb(1)/4).digamma()-arb.pi().log(); self.C=arb.pi()**2+8*arb.const_catalan()
    def phi(self,t,M=30):
        z=(-2*t).exp(); a,zp=arb(0),arb(1)
        for m in range(M): a+=zp/((arb(m)+arb(1)/4)**2); zp*=z
        tail=zp/(((arb(M)+arb(1)/4)**2)*(1-z)); return a+tail.union(arb(0))
    def A(self,t): return 4*((t/2).exp()+(-t/2).exp()-2)+(t/2)*self.k1+(self.C-(-t/2).exp()*self.phi(t))/4
    def dA(self,t,M=30):
        a=arb(0)
        for m in range(M):
            k=4*m+1; a+=2*(-(arb(k)*t)/2).exp()/k
        k=4*M+1; tail=(-(arb(k)*t)/2).exp()/(2*(1-(-2*t).exp()))
        return 2*((t/2).exp()-(-t/2).exp())+self.k1/2+a+tail.union(arb(0))
def exact(x):
    m,e=x.man_exp(); m=int(m); e=int(e)
    if e>=0: n=m<<e; d=1
    else:
        n=m; d=1<<(-e)
        while n and n%2==0: n//=2; d//=2
    return {'n':str(n),'d':str(d),'m':str(m),'e':e}
def run(lo,hi,outfile):
    ctx.prec=128; C=10**7; pp=ppowers(C); hi=min(hi,len(pp)); sm=Smooth(); p0=p1=arb(0); tprev=arb(1)/2
    for j in range(lo):
        n,p=pp[j]; tau=arb(n).log();
        if tau>tprev: tprev=tau
        w=arb(p).log()/arb(n).sqrt(); p0+=w; p1+=w*tau
    mn=None; where=None; allpos=True; cells=0; worst=0
    def cell(a,b,p0v,p1v,dep=0):
        nonlocal worst
        s=(a+b)/2; val=sm.A(s)-p0v*s+p1v; der=sm.dA(s)-p0v
        bd=val+(der*(a-s)).min(der*(b-s))
        if bd>0 or dep>=14: worst=max(worst,dep); return bd
        return cell(a,s,p0v,p1v,dep+1).min(cell(s,b,p0v,p1v,dep+1))
    st=time.time()
    for j in range(lo,hi):
        n,p=pp[j]; tau=arb(n).log()
        if tau>tprev:
            bd=cell(tprev,tau,p0,p1); cells+=1
            if not bd>0: allpos=False
            l=bd.lower()
            if mn is None or l<mn: mn=l; where={'kind':'knot','n':n,'index':j}
            tprev=tau
        w=arb(p).log()/arb(n).sqrt(); p0+=w; p1+=w*tau
    terminal=False
    if hi==len(pp):
        terminal=True; bd=cell(tprev,arb(C).log(),p0,p1); cells+=1
        if not bd>0: allpos=False
        l=bd.lower()
        if mn is None or l<mn: mn=l; where={'kind':'terminal','n':C,'index':hi}
    res={'lo':lo,'hi':hi,'total':len(pp),'cells':cells,'allpos':allpos,'min':exact(mn),'minstr':str(mn),'where':where,'terminal':terminal,'worst':worst,'sec':time.time()-st}
    open(outfile,'w').write(json.dumps(res,indent=2)); print(json.dumps(res))
if __name__=='__main__': run(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
