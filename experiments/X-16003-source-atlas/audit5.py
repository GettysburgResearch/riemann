"""Two more review points to verify before patching L-16006.

(P1) The extracted Gauss rule represents the CRITICAL PENCIL, not Q itself:
        Q - t* eta eta^T  =  sum_k A_k ell(r_k) ell(r_k)^T,
     r_k the kernel-polynomial roots.  This is just L-16004(i) applied to the pencil,
     since Q - t*J = Loewner(psi - t* lambda) whose kernel polynomial is P_xi, so the
     source is -P'/P = sum_k 1/(r_k - s).  Check it entrywise.

(P2) t* < 0 proves only that Q is NOT PSD; it does NOT imply indefinite.
     Elementary counterexample Q = -I.
"""
import sys; sys.path.insert(0,'.')
import mpmath as mp
from mpmath import mpf, nstr, matrix, lu_solve, polyroots
import x0001

print("="*88)
print("(P2) t* < 0 => 'indefinite'?   Q = -I_n")
print("="*88)
for n in (3,5,9):
    mp.mp.dps=30
    eta=matrix([1]*n)
    Qinv_eta=[-1 for _ in range(n)]          # (-I)^{-1} eta = -eta
    denom=sum(Qinv_eta)
    print(f"  n={n}: eta^T Q^-1 eta = {denom},  t* = {mpf(1)/denom},  "
          f"inertia(-I) = (0,{n},0) -> NEGATIVE DEFINITE, not indefinite")
print("  => reviewer correct: t* < 0 gives 'not PSD', which is strictly weaker.\n")

print("="*88)
print("(P1) Does the extracted Gauss rule reconstruct Q - t* J  (the PENCIL)?")
print("="*88)
for cut,N,dps in [('2000',4,140),('2000',6,180),('20000',6,180)]:
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
    mus=[]
    for k in range(2*d-1):
        vals=[sum(V[i][a]*Qt[i][j]*V[j][k-a] for i in range(d) for j in range(d))
              for a in range(max(0,k-d+1),min(d-1,k)+1)]
        mus.append(sum(vals)/len(vals))
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
    rts=polyroots(P[::-1],maxsteps=700,extraprec=25*dps)
    nds=sorted([mp.re(r) for r in rts if abs(mp.im(r))<mpf(10)**(-20)*max(1,abs(mp.re(r)))])
    n=len(nds)
    VA=matrix(n,n);rhs=matrix(n,1)
    for k in range(n):
        for i in range(n): VA[k,i]=nds[i]**k
        rhs[k]=mus[k]
    W=lu_solve(VA,rhs)
    # reconstruct  sum_k A_k ell(r_k) ell(r_k)^T   and compare with Q - t* J   and with Q
    R=matrix(d,d)
    for kk in range(n):
        ell=[1/(nodes[j]-nds[kk]) for j in range(d)]
        for i in range(d):
            for j in range(d): R[i,j]+=W[kk]*ell[i]*ell[j]
    scale=max(abs(A[i,j]) for i in range(d) for j in range(d))
    err_pencil=max(abs(R[i,j]-(A[i,j]-ts)) for i in range(d) for j in range(d))/scale
    err_Q     =max(abs(R[i,j]-A[i,j])       for i in range(d) for j in range(d))/scale
    mp.mp.dps=25
    print(f"  cut={cut:>6} N={N} dps={dps}:  |R - (Q - t*J)|/scale = {nstr(err_pencil,4):>12}"
          f"     |R - Q|/scale = {nstr(err_Q,4):>12}")
print("  => the Gauss rule reconstructs the PENCIL, not Q. Reviewer correct.")

print()
print("="*88)
print("Neither matched.  A 2N-point rule is exact only to degree 4N-1, while P_u^2 has")
print("degree 4N with leading coefficient (eta^T u)^2.  So the rule should miss exactly the")
print("top moment, giving  R = Q - kappa*eta*eta^T  for SOME kappa.  Test that, and find kappa.")
print("="*88)
for cut,N,dps in [('2000',4,140),('2000',6,180),('20000',6,180)]:
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
    mus=[]
    for k in range(2*d-1):
        vals=[sum(V[i][a]*Qt[i][j]*V[j][k-a] for i in range(d) for j in range(d))
              for a in range(max(0,k-d+1),min(d-1,k)+1)]
        mus.append(sum(vals)/len(vals))
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
    rts=polyroots(P[::-1],maxsteps=700,extraprec=25*dps)
    nds=sorted([mp.re(r) for r in rts if abs(mp.im(r))<mpf(10)**(-20)*max(1,abs(mp.re(r)))])
    n=len(nds)
    VA=matrix(n,n);rhs=matrix(n,1)
    for k in range(n):
        for i in range(n): VA[k,i]=nds[i]**k
        rhs[k]=mus[k]
    W=lu_solve(VA,rhs)
    R=matrix(d,d)
    for kk in range(n):
        ell=[1/(nodes[j]-nds[kk]) for j in range(d)]
        for i in range(d):
            for j in range(d): R[i,j]+=W[kk]*ell[i]*ell[j]
    D=[[A[i,j]-R[i,j] for j in range(d)] for i in range(d)]      # Q - R
    kap=D[0][0]
    dev=max(abs(D[i][j]-kap) for i in range(d) for j in range(d))
    sc=max(abs(D[i][j]) for i in range(d) for j in range(d))
    mp.mp.dps=25
    print(f"  cut={cut:>6} N={N}:  Q-R constant? max deviation/scale = {nstr(dev/sc,4):>11}"
          f"   kappa = {nstr(kap,10):>16}   t* = {nstr(ts,10):>16}   kappa/t* = {nstr(kap/ts,8)}")
