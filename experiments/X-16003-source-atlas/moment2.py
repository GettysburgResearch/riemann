"""Validate the Hankel test on a case where the answer MUST be 0, then report the
arithmetic defect antidiagonal by antidiagonal rather than as a single worst number."""
import sys; sys.path.insert(0,'.')
import mpmath as mp
from mpmath import mpf, nstr, matrix
import x0001

def hankel_profile(Qmat, N, label):
    d = 2*N+1
    nodes=[mpf(k) for k in range(-N,N+1)]
    w=[]
    for j in range(d):
        p=mpf(1)
        for k in range(d):
            if k!=j: p*=(nodes[k]-nodes[j])
        w.append(1/p)
    Qt=[[w[i]*Qmat[i][j]*w[j] for j in range(d)] for i in range(d)]
    V=[[nodes[i]**a for a in range(d)] for i in range(d)]
    M=[[sum(V[i][a]*Qt[i][j]*V[j][b] for i in range(d) for j in range(d)) for b in range(d)] for a in range(d)]
    print(f"  {label}")
    out=[]
    for k in range(2*d-1):
        vals=[M[a][k-a] for a in range(max(0,k-d+1),min(d-1,k)+1)]
        if len(vals)<2: continue
        m=sum(vals)/len(vals); sc=max(abs(v) for v in vals)
        out.append((k, float(max(abs(v-m) for v in vals)/sc) if sc>0 else 0.0))
    print("    a+b :  " + " ".join(f"{k:>9d}" for k,_ in out[:14]))
    print("    defect: " + " ".join(f"{v:>9.2e}" for _,v in out[:14]))
    if len(out)>14:
        print("    a+b :  " + " ".join(f"{k:>9d}" for k,_ in out[14:]))
        print("    defect: " + " ".join(f"{v:>9.2e}" for _,v in out[14:]))

def pole_loewner(poles,weights,N):
    d=2*N+1; nodes=[mpf(k) for k in range(-N,N+1)]
    allp=[(m,a) for m,a in zip(poles,weights)]+[(-m,a) for m,a in zip(poles,weights)]
    Q=[[mpf(0)]*d for _ in range(d)]
    for m,a in allp:
        ell=[1/(nodes[j]-m) for j in range(d)]
        for i in range(d):
            for j in range(d): Q[i][j]+=a*ell[i]*ell[j]
    return Q

mp.mp.dps=160
print("VALIDATION -- pole-sum source. L-16006(c) says the form IS L^2(nu), so the defect must be ~0.")
hankel_profile(pole_loewner([mpf(v) for v in [11,19,27,35,43,51,63,71,88,97]],[mpf(1)]*10,4),
               4,"10 pole pairs at 11..97, N=4 (over-determined)")
hankel_profile(pole_loewner([mpf(v) for v in [11,19,27,35,43,51,63,71,88,97,113,127,141,155,169,183,199,211,227,241]],
                            [mpf(1)]*20,6), 6,"20 pole pairs, N=6")
print()
print("Same profile PLUS a linear term c*lambda (Loewner(lambda) = eta eta^T), which is what")
print("the CvS pencil adds.  It should stay Hankel: eta eta^T contributes only at (2N,2N).")
d=9
Qp=pole_loewner([mpf(v) for v in [11,19,27,35,43,51,63,71,88,97]],[mpf(1)]*10,4)
Qj=[[Qp[i][j]-mpf('0.001') for j in range(d)] for i in range(d)]
hankel_profile(Qj,4,"same, minus 0.001 * eta eta^T")
print()
print("ARITHMETIC Weil form, same profile:")
for cut,N,dps in [('2000',4,120),('2000',6,160)]:
    mp.mp.dps=dps
    A,_=x0001.build_cutoff_free_matrix(cut,N,dps=dps)
    Q=[[A[i,j] for j in range(2*N+1)] for i in range(2*N+1)]
    hankel_profile(Q,N,f"cutoff {cut}, N={N}, dps={dps}")
