"""The implied residue a_1 = W_1 * Omega(r_1)^2 at the recovered gamma_1 came out
N-INDEPENDENT (0.072265 / 0.0722332 / 0.072233228 at N = 4/6/8, cutoff 2000) but strongly
cutoff-dependent (0.0023715 at cutoff 500).  Map it.  If the pure pole model psi_W ~
sum_rho 1/(s-rho) held, a_1 would be 1."""
import sys; sys.path.insert(0,'.')
import mpmath as mp
from mpmath import mpf,nstr,matrix,lu_solve,polyroots
import x0001
G1=mpf('14.134725141734693790')
print(f"{'cut':>8} {'L':>9} {'N':>3} {'a_1':>18} {'a_2':>14} {'a_1 * L^17':>13} {'a_1/(1/L^2)':>13}")
print("-"*84)
for cut in ['50','200','500','1000','2000','5000','20000']:
    for N in (5,6,7):
        dps=60+18*N
        mp.mp.dps=dps
        try:
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
            L=mp.log(mpf(cut))
            a1=W[n//2]*pev(Om,nds[n//2])**2
            a2=W[n//2+1]*pev(Om,nds[n//2+1])**2
            mp.mp.dps=25
            print(f"{cut:>8} {nstr(L,7):>9} {N:>3} {nstr(a1,12):>18} {nstr(a2,8):>14} "
                  f"{nstr(a1*L**17,6):>13} {nstr(a1*L**2,6):>13}")
        except Exception as e:
            print(f"{cut:>8} {'':>9} {N:>3}   failed {type(e).__name__}")
        sys.stdout.flush()
