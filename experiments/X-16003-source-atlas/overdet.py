"""
[!] WARNING (added after PR #173 review): the inertia routine in this file uses 1x1
    diagonal pivots only and returns (0,0,2) on [[0,1],[1,0]], whose true inertia is
    (1,1,0) -- it cannot see a hyperbolic negative direction.  Use inertia_correct.py
    instead.  Re-running this file's published tables with the correct routine
    reproduced them identically, but do not reuse the routine below.
"""
"""Independent check of the caution raised against L-16004(ii).

L-16004(ii) is stated for EXACTLY 2N poles in dimension 2N+1, where a rank count forces a
negative eigenvalue for each nonreal conjugate pair.  The claim under test is that the
SENTENCE "each nonreal pair forces a negative eigenvalue and Q is not PSD" is FALSE once the
form is OVER-DETERMINED (many more poles than nodes) -- which is the regime psi_W is in.

Build Q = sum over M real pole pairs + ONE nonreal quadruple at +-mu_* +- i*d, and read the
inertia.  If some rows come out (dim,0,0) with d > 0, the caution stands.
"""
import mpmath as mp
from mpmath import mpf, mpc, nstr

def loewner_poles(poles, N):
    """poles: list of (complex mu, weight).  Q = sum w * Re(ell(mu) ell(mu)^T), real symmetric."""
    d = 2*N+1
    nodes = [mpf(k) for k in range(-N, N+1)]
    Q = [[mpf(0)]*d for _ in range(d)]
    for mu, wt in poles:
        ell = [1/(nodes[j]-mu) for j in range(d)]
        for i in range(d):
            for j in range(d):
                Q[i][j] += mp.re(wt*ell[i]*ell[j])
    return Q

def inertia(Q):
    n=len(Q); A=[r[:] for r in Q]; piv=[]
    for k in range(n):
        b=max(range(k,n),key=lambda t:abs(A[t][t]))
        if b!=k:
            A[k],A[b]=A[b],A[k]
            for r in range(n): A[r][k],A[r][b]=A[r][b],A[r][k]
        dd=A[k][k]; piv.append(dd)
        if dd==0: continue
        for i in range(k+1,n):
            f=A[i][k]/dd
            for j in range(k,n): A[i][j]-=f*A[k][j]
            for j in range(k,n): A[j][i]=A[i][j]
    tol=max(abs(p) for p in piv)*mpf(10)**(-mp.mp.dps+12)
    return (sum(1 for p in piv if p>tol),sum(1 for p in piv if p<-tol),
            sum(1 for p in piv if abs(p)<=tol)), min(piv)

mp.mp.dps=120
print("Uniform ladder of real poles mu_k = k*pi/2, k=1..M (never on an integer node),")
print("plus ONE nonreal quadruple at +-mu_* +- i d, weight split so total weight is unchanged.")
print(f"{'N':>3} {'dim':>4} {'M':>4} {'mu_*':>9} {'mu_*/N':>7} {'d':>9} {'inertia':>12} {'min pivot':>14}")
print("-"*76)
for N in (4,6,8):
    d_=2*N+1
    for star_k in (1,5,8,20):
        mus=star_k*mp.pi/2
        for dd in (mpf(0), mpf('0.1'), mpf(1), mpf(10)):
            M=20
            poles=[]
            for k in range(1,M+1):
                m=k*mp.pi/2
                if k==star_k and dd>0:
                    for sg in (1,-1):
                        for s2 in (1,-1):
                            poles.append((sg*m+s2*mpc(0,1)*dd, mpf(1)/2))
                else:
                    poles.append((m,mpf(1))); poles.append((-m,mpf(1)))
            Q=loewner_poles(poles,N)
            ine,mp_=inertia(Q)
            print(f"{N:>3} {d_:>4} {M:>4} {nstr(mus,6):>9} {float(mus/N):>7.2f} {nstr(dd,4):>9} "
                  f"{str(ine):>12} {nstr(mp_,6):>14}"
                  f"{'   <-- nonreal pair present, still PD' if (dd>0 and ine[1]==0) else ''}")
    print()
