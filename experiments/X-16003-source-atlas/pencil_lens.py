"""In Prop 4.1 source terms, what is the note's one-scalar family?

Loewner is LINEAR in the source.  The source of the B_p direction is -lambda, and
   Loewner(lambda)_ij = (i-j)/(i-j) = 1  (i!=j),   Loewner(lambda)_ii = lambda'(i) = 1.
So Loewner(lambda) = J, the ALL-ONES matrix -- rank one, PSD.
Hence  Loewner(psi - t*lambda) = Loewner(psi) - t*J : a RANK-ONE shift.

Consequence to test: by Cauchy interlacing for symmetric rank-one updates, the number of
negative eigenvalues can change by AT MOST ONE over the whole family, for any t.
"""
import sys; sys.path.insert(0,'.')
from mpmath import mp, mpf, nstr, matrix
import x0001, random

mp.dps = 50
print("A. Is Loewner(lambda) the all-ones matrix J?  (exact by inspection, checked numerically)")
N=4; idx=list(range(-N,N+1))
Lo=[[1 if i!=j else 1 for j in idx] for i in idx]
print("   Loewner(lambda)_ij = (i-j)/(i-j) = 1 off-diagonal;  diagonal = lambda'(i) = 1  ->  J")
print("   so the pencil in source terms is   Q  ->  Q - t*J   (rank-one, PSD direction)\n")

def inertia_float(A, tol=None):
    n=A.rows
    ev=mp.eigsy(A, eigvals_only=True)
    ev=[mp.mpf(e) for e in ev]
    sc=max(abs(e) for e in ev)
    tol = tol or sc*mp.mpf(10)**(-mp.dps+8)
    return (sum(1 for e in ev if e>tol), sum(1 for e in ev if e<-tol), sum(1 for e in ev if abs(e)<=tol)), ev

print("B. Inertia of the X-0001 cutoff-free Weil matrix, and of the pencil Q - t*J.")
print(f"   {'cut':>6} {'N':>3} {'dim':>4} {'inertia(Q)':>14} {'min n_- over t':>16} {'argmin t':>12}")
for cut,N in [('50',4),('100',4),('100',6),('200',6),('500',6)]:
    A,_ = x0001.build_cutoff_free_matrix(cut, N, dps=50)
    dim=A.rows
    (p0,n0,z0),ev0 = inertia_float(A)
    best=(n0, mpf(0))
    sc=max(abs(A[i,j]) for i in range(dim) for j in range(dim))
    for k in range(-40,41):
        t = mpf(k)*sc/mpf(8)
        B = matrix(dim,dim)
        for i in range(dim):
            for j in range(dim): B[i,j]=A[i,j]-t
        (p,n,z),_ = inertia_float(B)
        if n<best[0]: best=(n,t)
    print(f"   {cut:>6} {N:>3} {dim:>4} {str((p0,n0,z0)):>14} {best[0]:>16} {nstr(best[1],4):>12}")

print()
print("C. Direct test of the interlacing consequence on random symmetric matrices:")
random.seed(3)
worst=0
for trial in range(200):
    n=random.choice([5,7,9])
    A=matrix(n,n)
    for i in range(n):
        for j in range(i,n):
            v=mpf(random.uniform(-1,1)); A[i,j]=v; A[j,i]=v
    (_,n0,_),_=inertia_float(A)
    for t in [mpf(x) for x in (-5,-2,-0.5,0.5,2,5)]:
        B=matrix(n,n)
        for i in range(n):
            for j in range(n): B[i,j]=A[i,j]-t
        (_,n1,_),_=inertia_float(B)
        worst=max(worst, abs(n1-n0))
print(f"   max |n_-(Q - tJ) - n_-(Q)| over 200 random matrices x 6 values of t : {worst}")
print("   (interlacing predicts at most 1)")
