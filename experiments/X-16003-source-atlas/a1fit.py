"""a_1 is N-independent to ~10 digits but swings by 290x with the cutoff, non-monotonically.
Hand-fitting the five points suggested

        a_1(c)  ~  (log c / (2 pi^2)) * (1 - cos(gamma_1 log c))
                =  (L / pi^2) * sin^2(gamma_1 L / 2)

i.e. the hard-cutoff Gibbs oscillation.  Test it on more cutoffs, at high precision."""
import sys; sys.path.insert(0,'.')
import mpmath as mp
from mpmath import mpf,nstr,matrix,lu_solve,polyroots
import x0001
G1=mpf('14.134725141734693790')

def a1_of(cut,N=6,dps=None):
    dps=dps or 60+18*N
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
    rts=polyroots(P[::-1],maxsteps=700,extraprec=25*dps)
    nds=sorted([mp.re(r) for r in rts if abs(mp.im(r))<mpf(10)**(-20)*max(1,abs(mp.re(r)))])
    n=len(nds)
    VA=matrix(n,n);rhs=matrix(n,1)
    for k in range(n):
        for i in range(n): VA[k,i]=nds[i]**k
        rhs[k]=mus[k]
    W=lu_solve(VA,rhs)
    return W[n//2]*pev(Om,nds[n//2])**2, nds[n//2]

print(f"{'cut':>9} {'L=log c':>10} {'a_1 (measured)':>18} {'(L/pi^2) sin^2(g1 L/2)':>24} {'ratio':>10}")
print("-"*78)
rs=[]
for cut in ['30','50','80','120','200','350','500','700','1000','1400','2000','3000','5000','8000']:
    try:
        a1,r1=a1_of(cut)
        mp.mp.dps=40
        L=mp.log(mpf(cut))
        pred=(L/mp.pi**2)*mp.sin(G1*L/2)**2
        rs.append(float(a1/pred))
        print(f"{cut:>9} {nstr(L,8):>10} {nstr(a1,12):>18} {nstr(pred,12):>24} {nstr(a1/pred,7):>10}")
    except Exception as e:
        print(f"{cut:>9}  failed {type(e).__name__}: {e}")
    sys.stdout.flush()
if rs:
    print()
    print(f"ratio over {len(rs)} cutoffs: min {min(rs):.5f}  max {max(rs):.5f}  mean {sum(rs)/len(rs):.5f}"
          f"   spread {max(rs)/min(rs):.4f}x")
