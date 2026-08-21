"""Does  a(gamma) = (log c / pi^2) sin^2(gamma log c / 2)  hold for EVERY zero, not just gamma_1?
Higher zeros are less resolved, so push N up and watch the agreement improve."""
import sys; sys.path.insert(0,'.')
import mpmath as mp
from mpmath import mpf,nstr,matrix,lu_solve,polyroots
import x0001
GAM=[mpf(v) for v in ['14.134725141734693790','21.022039638771554993','25.010857580145688763',
                      '30.424876125859513210','32.935061587739189691','37.586178158825671257',
                      '40.918719012147495187','43.327073280914999519']]
def run(cut,N,dps):
    mp.mp.dps=dps
    A,_=x0001.build_cutoff_free_matrix(cut,N,dps=dps)
    d=2*N+1;nodes=[mpf(k) for k in range(-N,N+1)]
    w=[]
    for j in range(d):
        p=mpf(1)
        for k in range(d):
            if k!=j: p*=(nodes[k]-nodes[j])
        w.append(1/p)
    Qt=[[w[i]*A[i,j]*w[j] for j in range(d)] for i in range(d)]
    V=[[nodes[i]**a for a in range(d)] for i in range(d)]
    mus=[]
    for k in range(2*d-1):
        vals=[sum(V[i][a]*Qt[i][j]*V[j][k-a] for i in range(d) for j in range(d))
              for a in range(max(0,k-d+1),min(d-1,k)+1)]
        mus.append(sum(vals)/len(vals))
    x=lu_solve(A,matrix([1]*d));ts=1/sum(x[i] for i in range(d));xi=[x[i]*ts for i in range(d)]
    Om=[mpf(1)]
    for k in nodes:
        Om=[(Om[i-1] if i>0 else mpf(0))*(-1)+(Om[i]*k if i<len(Om) else mpf(0)) for i in range(len(Om)+1)]
    P=[mpf(0)]*d
    for a,lj in enumerate(nodes):
        Omd=Om[::-1];acc=mpf(0);Qd=[]
        for i in range(len(Omd)-1):
            acc=Omd[i]+acc*lj;Qd.append(acc)
        Qj=[-c for c in Qd[::-1]]
        for i in range(len(Qj)): P[i]+=xi[a]*Qj[i]
    def pev(C,s):
        acc=mpf(0)*s
        for c in reversed(C): acc=acc*s+c
        return acc
    rts=polyroots(P[::-1],maxsteps=800,extraprec=25*dps)
    nds=sorted([mp.re(r) for r in rts if abs(mp.im(r))<mpf(10)**(-20)*max(1,abs(mp.re(r)))])
    n=len(nds)
    VA=matrix(n,n);rhs=matrix(n,1)
    for k in range(n):
        for i in range(n): VA[k,i]=nds[i]**k
        rhs[k]=mus[k]
    W=lu_solve(VA,rhs)
    L=mp.log(mpf(cut))
    out=[]
    for i in range(n//2,n):
        ai=W[i]*pev(Om,nds[i])**2
        ww=2*mp.pi*nds[i]/L
        g=min(GAM,key=lambda t:abs(t-ww))
        pred=(L/mp.pi**2)*mp.sin(g*L/2)**2
        out.append((ww,g,ai,pred,abs(ww-g)/g))
    return out,L

for cut in ['2000','20000']:
    for N in (6,8,10):
        dps=60+20*N
        try:
            out,L=run(cut,N,dps)
            mp.mp.dps=30
            print(f"=== cutoff {cut} (L={nstr(L,8)}), N={N}, dps={dps} ===")
            print(f"    {'zero':>8} {'node rel.err':>13} {'a measured':>16} {'(L/pi^2)sin^2(gL/2)':>21} {'ratio':>11}")
            for ww,g,ai,pred,rel in out[:6]:
                idx=GAM.index(g)+1
                print(f"    gamma_{idx:<2} {nstr(rel,3):>13} {nstr(ai,10):>16} {nstr(pred,10):>21} "
                      f"{nstr(ai/pred,9):>11}")
            print()
        except Exception as e:
            print(f"cutoff {cut} N={N}: failed {type(e).__name__}: {e}")
        sys.stdout.flush()
