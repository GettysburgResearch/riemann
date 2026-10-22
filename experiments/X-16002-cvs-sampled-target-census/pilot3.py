"""Pilot 3: build P by synthetic division from Omega instead of the naive double loop.
   Omega(s) = prod_k (lambda_k - s);  prod_{k!=j}(lambda_k - s) = Omega(s)/(lambda_j - s).
   Naive build is O(N^2) polynomial multiplications; this is O(N) divisions."""
import time, sys
sys.path.insert(0,'/home/user/riemann/experiments/X-16001-finsler-cone-collapse')
from verify import p_mul, p_add, p_scale, p_trim, sturm_count_all, squarefree_part
from fractions import Fraction as F
from mpmath import mp, mpf, pi, zeta, gamma
mp.dps = 160
def Xi(z): return (mpf(1)/2*(mpf(1)/2+1j*mpf(z))*((mpf(1)/2+1j*mpf(z))-1)*pi**(-(mpf(1)/2+1j*mpf(z))/2)
                   *gamma((mpf(1)/2+1j*mpf(z))/2)*zeta(mpf(1)/2+1j*mpf(z))).real
def t(f):
    a=time.time(); r=f(); return r, time.time()-a

def build_fast(N, alpha='0.5'):
    """ascending-coefficient P, built by synthetic division from Omega."""
    xis={j: F((-1)**j)*F(mp.nstr(Xi(2*pi*mpf(alpha)*j),100,strip_zeros=False)) for j in range(-N,N+1)}
    Om=[F(1)]
    for k in range(-N,N+1): Om=p_mul(Om,[F(k),F(-1)])       # (k - s)
    P=[F(0)]
    for j in range(-N,N+1):
        # divide Om by (j - s):  synthetic division, descending is easier -> do it on reversed coeffs
        # Om(s) = (j - s) * Qj(s).  Work descending.
        Omd=Om[::-1]; n=len(Omd)
        Qd=[F(0)]*(n-1); rem=F(0)
        # (j - s) = -(s - j); Om/(j-s) = -(Om/(s-j)); synthetic division by (s-j)
        acc=F(0)
        for i in range(n-1):
            acc = Omd[i] + acc*F(j)
            Qd[i]=acc
        Qj=[-c for c in Qd[::-1]]                            # negate for (j - s)
        P=p_add(P, p_scale(Qj, xis[j]))
    return p_trim(P)

print("=== G. build P: naive double loop vs synthetic division (pure Fraction, no sympy) ===")
print(f"   {'N':>4} {'deg':>5} {'fast build (s)':>15} {'Sturm (s)':>11} {'total (s)':>10} {'#real':>7}")
prev=None
for N in [6,8,10,12,14,16,20]:
    P,tb = t(lambda: build_fast(N))
    def cnt():
        return sturm_count_all(squarefree_part(P))
    n,tc = t(cnt)
    tot=tb+tc
    r = f"  x{tot/prev:.1f}" if prev else ""
    print(f"   {N:>4} {len(P)-1:>5} {tb:>15.2f} {tc:>11.2f} {tot:>10.2f} {n:>7}{r}")
    prev=tot
