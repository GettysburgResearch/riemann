import mpmath as mp
from fractions import Fraction as Fr
mp.mp.dps = 25
def sinc(t): return mp.mpf(1) if t == 0 else mp.sin(mp.pi*t)/(mp.pi*t)
th = mp.mpf(17)/20
wins = {"first":([193305, -23105, 29166, 13952, -21009, 41052], mp.mpf(607)/1000),
        "second":([122290, -45012, 16241, 1887, 2711, 3731, -5307, 2982, -5153, 5358], mp.mpf(13)/20),
        "third":([200566, 19, -9358, 9283, -6746, 8170], mp.mpf(61)/100)}
for name,(w,g0) in wins.items():
    a = [mp.mpf(x)/10**6 for x in w]
    f = lambda u: 1 + sum(aj*mp.cos(2*mp.pi*(j+1)*u) for j,aj in enumerate(a))
    g = lambda u: g0*(sinc(th*(u-mp.mpf(1)/2)) + sinc(th*(u+mp.mpf(1)/2)))**2
    m = min(g(mp.mpf(k)/20000) - f(mp.mpf(k)/20000) for k in range(0,10001))
    print(name, "min_{0<=u<=1/2} (g-f) on grid =", mp.nstr(m, 6))
# Theorem 1.5
x, b = Fr(54525,10**6), Fr(37272,10**6); C0pp = Fr(6662319,5000000); t = Fr(27,8); e0 = 2*t-t*t/4
v = (e0 - C0pp - b)/(e0 - 1 - x); print("Thm1.5 =", v, float(v), v == Fr(50652159,56956375), " 2+2x=", float(2+2*x))
