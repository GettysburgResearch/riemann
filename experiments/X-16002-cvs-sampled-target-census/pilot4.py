"""Pilot 4: END-TO-END cost of the two routes to the same information.
Route S: build P -> exact Sturm -> #real roots.
Route L: build P -> P,P',P'' at nodes -> Loewner matrix of -P'/P -> exact inertia -> #nonreal pairs.
By L-16004 these carry the same information (#neg eigenvalues = #nonreal conjugate pairs)."""
import time, sys, math
sys.path.insert(0,'/home/user/riemann/experiments/X-16001-finsler-cone-collapse')
from verify import p_mul, p_add, p_scale, p_trim, sturm_count_all, squarefree_part, inertia
from fractions import Fraction as F
from mpmath import mp, mpf, pi, zeta, gamma
mp.dps = 160
def Xi(z): return (mpf(1)/2*(mpf(1)/2+1j*mpf(z))*((mpf(1)/2+1j*mpf(z))-1)*pi**(-(mpf(1)/2+1j*mpf(z))/2)
                   *gamma((mpf(1)/2+1j*mpf(z))/2)*zeta(mpf(1)/2+1j*mpf(z))).real
def t(f):
    a=time.time(); r=f(); return r, time.time()-a
def build_fast(N, alpha):
    xis={j: F((-1)**j)*F(mp.nstr(Xi(2*pi*mpf(alpha)*j),100,strip_zeros=False)) for j in range(-N,N+1)}
    Om=[F(1)]
    for k in range(-N,N+1): Om=p_mul(Om,[F(k),F(-1)])
    P=[F(0)]
    for j in range(-N,N+1):
        Omd=Om[::-1]; acc=F(0); Qd=[]
        for i in range(len(Omd)-1):
            acc=Omd[i]+acc*F(j); Qd.append(acc)
        P=p_add(P, p_scale([-c for c in Qd[::-1]], xis[j]))
    return p_trim(P)
def ev(c,x):
    r=F(0)
    for a in reversed(c): r=r*x+a
    return r
def loewner_inertia(P,N):
    d1=[P[i]*i for i in range(1,len(P))]; d2=[d1[i]*i for i in range(1,len(d1))] if len(d1)>1 else [F(0)]
    d1=[F(0)] if not d1 else d1
    b={}; a={}
    for i in range(-N,N+1):
        Pi=ev(P,F(i))
        if Pi==0: return None
        b[i]=-ev(d1,F(i))/Pi
        a[i]=(ev(d1,F(i))**2 - Pi*ev(d2,F(i)))/(Pi*Pi)
    idx=list(range(-N,N+1))
    Q=[[a[i] if i==j else (b[i]-b[j])/F(i-j) for j in idx] for i in idx]
    return inertia(Q)

print("END-TO-END, alpha=0.5, single core.  Route S = Sturm.  Route L = Loewner inertia (L-16004).")
print(f"   {'N':>4} {'deg':>5} {'build':>7} {'S:Sturm':>9} {'S total':>9} {'L:inertia':>11} {'L total':>9} {'#real':>6} {'inertia(+,-,0)':>16} {'consistent?':>12}")
for N in [8,12,16,20,24]:
    P,tb = t(lambda: build_fast(N,'0.5'))
    nre,ts = t(lambda: sturm_count_all(squarefree_part(P)))
    ine,tl = t(lambda: loewner_inertia(P,N))
    deg=len(P)-1
    consistent = (ine is not None) and (deg - nre == 2*ine[1])
    print(f"   {N:>4} {deg:>5} {tb:>7.2f} {ts:>9.2f} {tb+ts:>9.2f} {tl:>11.2f} {tb+tl:>9.2f} {nre:>6} {str(ine):>16} {str(consistent):>12}")
