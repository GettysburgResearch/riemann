"""CORRECTED.  The source is ODD, so the representing measure is symmetric under mu -> -mu
and ALL ODD MOMENTS VANISH IDENTICALLY.  My first Hankel test divided by max|v| on each
antidiagonal, so on the odd antidiagonals it computed 0/0 and returned O(1) noise, which I
misread as a failure.  Only the EVEN antidiagonals carry information.

Same bug affects L-16006 sec 4's orthogonality residual: P_xi is even and the atoms come in
+-mu pairs, so <P_xi, s^k>_nu vanishes term-by-term for odd k.  Redo it over EVEN k only.

Then: extract the Christoffel weights W_i of the form's own Gauss rule and compute the
IMPLIED RESIDUE  a_i = W_i * Omega(r_i)^2 .  If the pure pole model psi_W = sum_rho 1/(s-rho)
held, a_i would be 1 at every recovered zero.  That is the sharp test.
"""
import sys; sys.path.insert(0,'.')
import mpmath as mp
from mpmath import mpf, nstr, matrix, lu_solve, polyroots
import x0001

GAM=[mpf(v) for v in ['14.134725141734693790','21.022039638771554993','25.010857580145688763',
                      '30.424876125859513210','32.935061587739189691','37.586178158825671257',
                      '40.918719012147495187','43.327073280914999519']]

def run(cut,N,dps):
    mp.mp.dps=dps
    A,_=x0001.build_cutoff_free_matrix(cut,N,dps=dps)
    d=2*N+1; nodes=[mpf(k) for k in range(-N,N+1)]
    w=[]
    for j in range(d):
        p=mpf(1)
        for k in range(d):
            if k!=j: p*=(nodes[k]-nodes[j])
        w.append(1/p)
    Qt=[[w[i]*A[i,j]*w[j] for j in range(d)] for i in range(d)]
    V=[[nodes[i]**a for a in range(d)] for i in range(d)]
    M=[[sum(V[i][a]*Qt[i][j]*V[j][b] for i in range(d) for j in range(d)) for b in range(d)] for a in range(d)]
    print(f"=== cutoff {cut}, N={N}, dim={d}, dps={dps} ===")
    ev=[];od=[]
    mus=[]
    for k in range(2*d-1):
        vals=[M[a][k-a] for a in range(max(0,k-d+1),min(d-1,k)+1)]
        m=sum(vals)/len(vals); mus.append(m)
        if len(vals)<2: continue
        sc=max(abs(v) for v in vals)
        r=(max(abs(v-m) for v in vals)/sc) if sc>0 else mpf(0)
        (ev if k%2==0 else od).append((k,r,sc))
    print(f"  EVEN antidiagonals: worst relative Hankel defect {nstr(max(r for _,r,_ in ev),4)}")
    print(f"  ODD  antidiagonals: worst scale max|M_ab| = {nstr(max(sc for _,_,sc in od),4)}"
          f"   vs even scale {nstr(max(sc for _,_,sc in ev),4)}  -> odd moments vanish")
    print(f"    [even defect at working precision => the form IS a moment functional]")
    # kernel vector, polynomial, Gauss nodes
    x=lu_solve(A,matrix([1]*d)); ts=1/sum(x[i] for i in range(d)); xi=[x[i]*ts for i in range(d)]
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
    rts=polyroots(P[::-1],maxsteps=600,extraprec=25*dps)
    nds=sorted([mp.re(r) for r in rts if abs(mp.im(r))<mpf(10)**(-20)*max(1,abs(mp.re(r)))])
    n=len(nds)
    VA=matrix(n,n); rhs=matrix(n,1)
    for k in range(n):
        for i in range(n): VA[k,i]=nds[i]**k
        rhs[k]=mus[k]
    W=lu_solve(VA,rhs)
    L=mp.log(mpf(cut))
    print(f"  Gauss nodes / Christoffel weights / IMPLIED RESIDUE a_i = W_i * Omega(r_i)^2")
    print(f"    {'w = 2 pi r/L':>16} {'rel. err vs gamma':>18} {'Christoffel W_i':>18} {'implied a_i':>16}")
    for i in range(n//2,n):
        ww=2*mp.pi*nds[i]/L
        near=min(GAM,key=lambda g:abs(g-ww))
        rel=abs(ww-near)/near
        ai=W[i]*pev(Om,nds[i])**2
        print(f"    {nstr(ww,12):>16} {nstr(rel,3):>18} {nstr(W[i],6):>18} {nstr(ai,8):>16}")
    # corrected sec 4 orthogonality: EVEN k only, against nu_zeta with unit residues
    Delta=L/(2*mp.pi)
    atoms=[]
    for g in GAM+[mpf(v) for v in ['48.005150881167159727','49.773832477672302182',
                                   '52.970321477714460644','56.446247697063394805']]:
        m=g*Delta
        for mm in (m,-m): atoms.append((mm,1/pev(Om,mm)**2))
    res=[]
    for k in range(0,2*N,2):
        s=sum(wt*pev(P,m)*m**k for m,wt in atoms)
        nrm=sum(abs(wt)*abs(pev(P,m))*abs(m)**k for m,wt in atoms)
        res.append(abs(s)/nrm if nrm>0 else mpf(0))
    print(f"  L-16006 sec4 residual REDONE over EVEN k only, vs unit-residue nu_zeta: "
          f"{nstr(max(res),4)}   (was reported as ~0.5-0.8 including the vacuous odd k)")
    print()

for cut,N,dps in [('2000',4,120),('2000',6,160),('2000',8,220),('500',6,160)]:
    run(cut,N,dps)
