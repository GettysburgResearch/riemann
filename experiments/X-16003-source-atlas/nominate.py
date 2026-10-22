"""If Q_W is positive definite and the pencil is Q - t*J with J = eta eta^T (rank one), then by the
Sherman-Morrison determinant identity
        det(Q - t eta eta^T) = det(Q) (1 - t * eta^T Q^{-1} eta),
so the family becomes singular at exactly ONE scalar
        t* = 1 / (eta^T Q^{-1} eta),
and there the kernel is one-dimensional, spanned by
        xi  ∝  Q^{-1} eta.
i.e. the ARITHMETIC form nominates its own target, rather than the target being chosen.
Test: compute t*, the nominated xi, and ask whether its interpolation polynomial is real-rooted
(which is the CvS gate)."""
import sys; sys.path.insert(0,'.')
from mpmath import mp, mpf, nstr, matrix, lu_solve, mpc, polyroots
import x0001

mp.dps = 60
print(f"{'cut':>6} {'N':>3} {'dim':>4} {'t* = 1/(eta^T Q^-1 eta)':>26} {'xi even?':>10} {'inertia(Q-t*J)':>16}")
print("-"*84)
data={}
for cut,N in [('50',4),('100',4),('100',6),('200',6),('500',6),('200',8)]:
    A,_ = x0001.build_cutoff_free_matrix(cut, N, dps=60)
    dim=A.rows
    eta = matrix([1]*dim)
    x = lu_solve(A, eta)                      # Q^{-1} eta
    denom = sum(x[i] for i in range(dim))     # eta^T Q^{-1} eta
    tstar = 1/denom
    xi = [x[i]*tstar for i in range(dim)]     # normalised so eta^T xi = 1
    evenness = max(abs(xi[i]-xi[dim-1-i]) for i in range(dim))/max(abs(v) for v in xi)
    B = matrix(dim,dim)
    for i in range(dim):
        for j in range(dim): B[i,j]=A[i,j]-tstar
    ev = [mp.mpf(e) for e in mp.eigsy(B, eigvals_only=True)]
    sc = max(abs(e) for e in ev); tol=sc*mp.mpf(10)**(-mp.dps+12)
    ine = (sum(1 for e in ev if e>tol), sum(1 for e in ev if e<-tol), sum(1 for e in ev if abs(e)<=tol))
    data[(cut,N)]=(tstar,xi)
    print(f"{cut:>6} {N:>3} {dim:>4} {nstr(tstar,16):>26} {nstr(evenness,3):>10} {str(ine):>16}")

print()
print("Now the CvS gate on the NOMINATED target: roots of P(s) = sum_j xi_j prod_{k!=j}(k-s).")
print(f"{'cut':>6} {'N':>3} {'deg':>4} {'#real':>6} {'#nonreal':>9}   roots (real parts)")
print("-"*100)
for (cut,N),(tstar,xi) in data.items():
    dim=2*N+1; idx=list(range(-N,N+1))
    # build P by convolution in mpf
    Om=[mpf(1)]
    for k in idx:
        Om=[ (Om[i-1] if i>0 else mpf(0))*(-1) + (Om[i]*mpf(k) if i<len(Om) else mpf(0)) for i in range(len(Om)+1)]
    P=[mpf(0)]*(dim)
    for a,j in enumerate(idx):
        Q1=[mpf(0)]*(dim)      # Om/(j - s), synthetic division, ascending
        Omd=Om[::-1]; acc=mpf(0); Qd=[]
        for i in range(len(Omd)-1):
            acc=Omd[i]+acc*mpf(j); Qd.append(acc)
        Qj=[-c for c in Qd[::-1]]
        for i in range(len(Qj)): P[i]+= xi[a]*Qj[i]
    coeffs=[P[i] for i in range(len(P))][::-1]
    try:
        rts=polyroots(coeffs, maxsteps=300, extraprec=2000)
    except Exception as e:
        print(f"{cut:>6} {N:>3} {len(P)-1:>4}  polyroots failed: {e}"); continue
    nre=[r for r in rts if abs(mp.im(r))<=mpf(10)**(-25)*max(1,abs(mp.re(r)))]
    nnr=[r for r in rts if r not in nre]
    print(f"{cut:>6} {N:>3} {len(P)-1:>4} {len(nre):>6} {len(nnr):>9}   {[nstr(mp.re(r),6) for r in sorted(nre,key=lambda z: mp.re(z))][:8]}")
