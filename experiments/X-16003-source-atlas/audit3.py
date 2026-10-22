"""Where exactly does the Loewner-Hankel identity hold?

Contour derivation: for psi analytic, psi[x,y] = (1/2 pi i) oint psi(t)/((t-x)(t-y)) dt, and for
a <= n (= 2N) one has  sum_i w_i lam_i^a/(t-lam_i) = t^a / Omega~(t),  Omega~(t) = prod_k(t-lam_k).
Hence
        M_ab = (1/2 pi i) oint psi(t) t^{a+b} / Omega~(t)^2 dt
which depends only on a+b -- HANKEL -- PROVIDED the contour at infinity vanishes.  The
integrand decays like psi(t) t^{a+b-(4N+2)}, and a+b reaches 4N, so the condition is
        psi(t) / t^2 -> 0.
Prediction: Hankel for psi of growth < t^2, FAILING from psi ~ t^3 upward.  Test it."""
import sys; sys.path.insert(0,'.')
import mpmath as mp
from mpmath import mpf, nstr
import blinddet2 as B
mp.mp.dps = 80

def hankel_defect(psi,dpsi,N,dps=80):
    mp.mp.dps=dps
    d=2*N+1; nodes=[mpf(j) for j in range(-N,N+1)]
    w=[]
    for j in range(d):
        p=mpf(1)
        for k in range(d):
            if k!=j: p*=(nodes[k]-nodes[j])
        w.append(1/p)
    Q=[[dpsi(nodes[i]) if i==j else (psi(nodes[i])-psi(nodes[j]))/(nodes[i]-nodes[j])
        for j in range(d)] for i in range(d)]
    Qt=[[w[i]*Q[i][j]*w[j] for j in range(d)] for i in range(d)]
    V=[[nodes[i]**a for a in range(d)] for i in range(d)]
    M=[[sum(V[i][a]*Qt[i][j]*V[j][b] for i in range(d) for j in range(d)) for b in range(d)] for a in range(d)]
    worst=mpf(0); worst_ab=None
    for a in range(d-1):
        for b in range(d-1):
            sc=max(abs(M[a+1][b]),abs(M[a][b+1]))
            if sc>0:
                v=abs(M[a+1][b]-M[a][b+1])/sc
                if v>worst: worst,worst_ab=v,(a+1,b)
    return worst,worst_ab

print("Monomial sources psi(x) = x^m -- where does Hankel break?")
print(f"{'m':>3} {'N=3':>14} {'N=5':>14}   predicted (growth < t^2 => Hankel)")
print("-"*70)
for m in range(1,7):
    r3,_=hankel_defect(lambda x,m=m:x**m, lambda x,m=m:m*x**(m-1),3)
    r5,ab=hankel_defect(lambda x,m=m:x**m, lambda x,m=m:m*x**(m-1),5)
    pred = "HANKEL" if m<3 else "fails"
    print(f"{m:>3} {nstr(r3,5):>14} {nstr(r5,5):>14}   {pred}")
print()
print("Bounded / decaying sources (the class psi_W belongs to):")
for name,p,dp in [
   ("1/(x-30.5)", lambda x:1/(x-mpf('30.5')), lambda x:-1/(x-mpf('30.5'))**2),
   ("atan(x/20)", lambda x:mp.atan(x/20), lambda x:(mpf(1)/20)/(1+(x/20)**2)),
   ("x/(1+x^2)",  lambda x:x/(1+x**2), lambda x:(1-x**2)/(1+x**2)**2),
   ("log(x+40)",  lambda x:mp.log(x+40), lambda x:1/(x+40))]:
    r,_=hankel_defect(p,dp,5)
    print(f"   {name:14s} N=5 worst defect {nstr(r,5)}")
print()
print("=> The identity is universal ONLY within the growth class psi(t)/t^2 -> 0.")
print("   It is NOT universal for all Loewner sources: x^3, x^5, sin all break it.")
print("   psi_W is bounded, so the identity DOES apply -- the reviewer's conclusion for")
print("   the arithmetic case stands, but the stated generality is too broad.")
print()
print("="*90)
print("Re-run L-16004's SCOPE-CAUTION table with the CORRECT (2x2-capable) inertia routine")
print("="*90)
def loewner_poles(poles,N):
    d=2*N+1; nodes=[mpf(j) for j in range(-N,N+1)]
    Q=[[mpf(0)]*d for _ in range(d)]
    for m,wt in poles:
        ell=[1/(nodes[j]-m) for j in range(d)]
        for i in range(d):
            for j in range(d): Q[i][j]+=mp.re(wt*ell[i]*ell[j])
    return Q
mp.mp.dps=120
print(f"{'N':>3} {'mu_*':>9} {'mu_*/N':>7} {'d':>7} {'buggy':>12} {'CORRECT':>12}  agree?")
for N,star_k in [(4,5),(4,20),(6,8),(8,20)]:
    for dd in (mpf('0.1'), mpf(1), mpf(10)):
        M=20; poles=[]
        for k in range(1,M+1):
            m=k*mp.pi/2
            if k==star_k:
                for sg in (1,-1):
                    for s2 in (1,-1):
                        poles.append((sg*m+s2*mp.mpc(0,1)*dd, mpf(1)/2))
            else:
                poles.append((m,mpf(1))); poles.append((-m,mpf(1)))
        Q=loewner_poles(poles,N)
        import audit1 as A1
        old=A1.buggy_1x1(Q); new=B.inertia(Q)
        print(f"{N:>3} {nstr(star_k*mp.pi/2,6):>9} {float(star_k*mp.pi/2/N):>7.2f} {nstr(dd,3):>7} "
              f"{str(old):>12} {str(new):>12}  {old==new}")
