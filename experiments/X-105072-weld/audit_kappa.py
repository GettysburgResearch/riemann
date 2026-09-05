import mpmath as mp
mp.mp.dps = 40
rho1 = mp.zetazero(1); g1 = mp.im(rho1)
zp1 = mp.zeta(rho1, derivative=1)
zstar = mp.mpf(1)/4 - 1j*g1/2
ln2 = mp.log(2); s0 = 1j*g1/3
def k(b):
    b = mp.mpc(b); return 1/b - (1-2**(-b))/(b**2*ln2)
def bfun(v):
    v = mp.mpc(v)
    if abs(v-1) < mp.mpf(10)**-15: return mp.mpf(1)
    return mp.sqrt((v-1)*mp.zeta(v))
def Z1(w):
    w = mp.mpc(w)
    if abs(w) < mp.mpf(10)**-15: return zp1
    return mp.zeta(rho1+w)/w
A0 = k(mp.mpf('0.5'))/(zstar*zp1)
def A(x, s):
    return k(mp.mpf('0.5')-x)*bfun(1-x)/((mp.mpf('0.25')-mp.mpf('1.5')*s-x)*Z1(3*(s-s0)+x))
def Rloc(s):
    eps = 3*(s-s0)
    f = lambda u: 2*A(u**2, s)/(u**2+eps)
    return 3/(2*mp.pi)*mp.quad(f, [0, mp.mpf('0.5')]) - mp.sqrt(3)/2*A0*(s-s0)**mp.mpf('-0.5')
# 3-point fit R(t)=R0+kap*sqrt(t)e^{i th/2}+C t e^{i th} on ray arg=th
th = mp.pi/6; e = mp.exp(1j*th)
ts = [mp.mpf(10)**-5, mp.mpf(10)**-7, mp.mpf(10)**-9]
Rs = [Rloc(s0+t*e) for t in ts]
import itertools
# solve linear system in (R0, kap', C') with kap'=kap e^{i th/2}, C'=C e^{i th}
M = mp.matrix([[1, mp.sqrt(t), t] for t in ts])
b = mp.matrix(Rs)
sol = mp.lu_solve(M, b)
kap_fit = sol[1]/mp.exp(1j*th/2)
def kp(bb, h): return (k(bb+h)-k(bb-h))/(2*h)
br = 3*kp(mp.mpf('0.5'), mp.mpf(10)**-12)/k(mp.mpf('0.5')) + mp.mpf('1.5')*mp.euler - mp.mpf('1.5')/zstar
kap_cl = mp.sqrt(3)/2*A0*br
print("kappa closed  =", mp.nstr(kap_cl, 14))
print("kappa 3ptfit  =", mp.nstr(kap_fit, 14))
print("rel diff      =", mp.nstr(abs(kap_fit-kap_cl)/abs(kap_cl), 6))
# direct derivative cross-check, Richardson two step sizes
def A0s(s): return k(mp.mpf('0.5'))/((mp.mpf('0.25')-mp.mpf('1.5')*s)*Z1(3*(s-s0)))
def Ax(x): return k(mp.mpf('0.5')-x)*bfun(1-x)/((zstar-x)*Z1(x))
out = []
for hd in [mp.mpf(10)**-10, mp.mpf(10)**-12]:
    As_n = (A0s(s0+hd)-A0s(s0-hd))/(2*hd)
    Ax_n = (Ax(hd)-Ax(-hd))/(2*hd)
    out.append(mp.sqrt(3)/2*(As_n-3*Ax_n))
print("kappa direct h=1e-10 =", mp.nstr(out[0], 14))
print("kappa direct h=1e-12 =", mp.nstr(out[1], 14))
print("closed-vs-direct rel =", mp.nstr(abs(out[1]-kap_cl)/abs(kap_cl), 6))
