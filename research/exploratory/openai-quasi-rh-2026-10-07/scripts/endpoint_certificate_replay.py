# Replays OpenAI 7/8 paper Lemma 20.2 (compensated endpoint certificate): -E_* >= 49/440640 on
# 0<=delta<=5/6, 0<=x<=1/2, with h=13/16, alpha=5/6, E_* = C0 + (2/3)d + q/6 - h(1-R_*), q = x d.
from fractions import Fraction as Fr
import itertools
h=Fr(13,16); al=Fr(5,6); C0=Fr(-1,48)
def negE(d,x):
    Dx=3-Fr(17,9)*x; Px=(2-Fr(8,9)*x)*(1-x)
    J=(al-d)*Dx+d*Px
    if J<=0: return None
    one_minus_R=d-(al-d)*d*Px/(2*J)
    E=C0+Fr(2,3)*d+x*d/6-h*one_minus_R
    return -E
best=None
N=400
for i in range(N+1):
    for j in range(N+1):
        d=al*Fr(i,N); x=Fr(j,2*N)
        v=negE(d,x)
        if v is not None and (best is None or v<best[0]): best=(v,d,x)
v,d,x=best
print("grid min of -E_*: %.10f at delta=%s x=%s ; claimed bound 49/440640=%.10f"%(float(v),d,x,49/440640))
# refine with local exact search around minimizer
for N2 in [10**4]:
    loc=min(((negE(d+al*Fr(a,N2*10),x+Fr(b,N2*20)),d+al*Fr(a,N2*10),x+Fr(b,N2*20))
            for a in range(-50,51) for b in range(-50,51)
            if 0<=d+al*Fr(a,N2*10)<=al and 0<=x+Fr(b,N2*20)<=Fr(1,2) and negE(d+al*Fr(a,N2*10),x+Fr(b,N2*20)) is not None),key=lambda t:t[0])
    print("refined min: %.10f at delta=%.6f x=%.6f"%(float(loc[0]),float(loc[1]),float(loc[2])))
