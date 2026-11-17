import mpmath as mp
from fractions import Fraction as Fr
mp.mp.dps = 30
w1 = [193305, -23105, 29166, 13952, -21009, 41052]
w2 = [122290, -45012, 16241, 1887, 2711, 3731, -5307, 2982, -5153, 5358]
w3 = [200566, 19, -9358, 9283, -6746, 8170]
def mk(a):
    a = [mp.mpf(x)/10**6 for x in a]
    f = lambda u: 1 + sum(aj*mp.cos(2*mp.pi*(j+1)*u) for j,aj in enumerate(a))
    return a, f
def C(f):
    I2 = mp.quad(lambda x: f(x)**2, [-0.5, 0, 0.5])
    inner = lambda x: mp.quad(lambda y: abs(x-y)*f(y), [-0.5, x, 0.5])
    I3 = mp.quad(lambda x: f(x)*inner(x), [-0.5, 0, 0.5])
    return I2 + I3, mp.quad(f, [-0.5,0.5])
def sinc(t): return mp.mpf(1) if t == 0 else mp.sin(mp.pi*t)/(mp.pi*t)
def K(a, t):
    return sinc(t) + sum(aj/2*(sinc(t-(j+1))+sinc(t+(j+1))) for j,aj in enumerate(a))
for name, w, Cbound in (("first", w1, Fr(266541,200000)), ("second", w2, Fr(6639737,5000000)), ("third", w3, Fr(6662319,5000000))):
    a, f = mk(w)
    c, mass = C(f)
    fmin = min(f(mp.mpf(k)/2000) for k in range(-1000,1001))
    print(name, "C(f)=", mp.nstr(c, 12), " mass=", mp.nstr(mass, 8), " C< bound", c < mp.mpf(Cbound.numerator)/Cbound.denominator, " min f=", mp.nstr(fmin,6), " f(1/2)=", mp.nstr(f(mp.mpf(0.5)),6))
    th = mp.mpf(17)/20
    kmin = min(K(a, th*k/4000)**2 for k in range(0,4001))
    print("   min K^2 on [0,17/20] (grid)=", mp.nstr(kmin, 8))
# Lambda of majorant
th = mp.mpf(17)/20
for g0, claim in ((mp.mpf(607)/1000, "1.67105"), (mp.mpf(13)/20, "1.78942"), (mp.mpf(61)/100, "1.67931")):
    print("Lambda gamma0=",g0, mp.nstr(2*g0/th*(1+sinc(th)),8), "claimed", claim)
# Final rationals
x1,x2,b = Fr(54350,10**6),Fr(69433,10**6),Fr(37314,10**6)
C0 = Fr(266541,200000)
q = (3-C0+x2-x1-b)/(2-2*x1+x2); print("q =", q, float(q), " claimed 1645064/1960733", q==Fr(1645064,1960733), " 2q-1=", 2*q-1)
c = Fr(67,20)
mu = 2-2*x1+x2; nu = 2*c-3+x1-x2; rh = 6*c-7-c*c+x1-2*x2; rk = 4*c-2-c*c-2*x1
print(" mu,nu,rh,rk =", float(mu), float(nu), float(rh), float(rk))
x, b2 = Fr(8722,10**6), Fr(4389,10**6); C0p = Fr(6639737,5000000)
s0 = (2-C0p-b2)/(1-x); print("s0 =", s0, float(s0), s0==Fr(1669159,2478195), " (1+s0)/2=", (1+s0)/2, (1+s0)/2==Fr(2073677,2478195))
t = Fr(27,8); e0 = 2*t - t*t/4; print(" 4t-t^2=", float(4*t-t*t), " 2+2x1=", float(2+2*x1), " e0=", e0)
v = (e0-C0-b)/(e0-1-x1); print(" Thm1.4b =", v, float(v), v==Fr(3376433,3797325))
# Theorem 1.5: certificate (x,b)=(54525,37272)e-6 third window; t = 27/8? check later lines
