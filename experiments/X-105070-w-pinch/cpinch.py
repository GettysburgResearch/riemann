from mpmath import mp, mpf, mpc, zeta, zetazero, sqrt, ln, pi, fabs, diff, mpmathify
mp.dps = 50
# zero
rho1 = zetazero(1); g1 = rho1.imag
# zeta'(rho1)
zp = zeta(rho1, derivative=1)
# k(beta) = 1/beta - (1-2^{-beta})/(beta^2 ln2), at beta=1/2
def k(beta): return 1/beta - (1 - mpf(2)**(-beta))/(beta**2*ln(2))
k12 = k(mpf(1)/2)
# closed form check: k(1/2) = 2 - 4(1-1/sqrt2)/ln2 = 2(1-(2/ln2)(1-1/sqrt2))
k12b = 2 - 4*(1-1/sqrt(2))/ln(2)
zstar = mpc(mpf(1)/4, -g1/2)
absz = fabs(zstar)
cB_mod = (mpf(3)/2)*fabs(k12)/(sqrt(3)*absz*fabs(zp))
# full complex value with the branch factor omega=1 convention (phase reported separately)
cB = (sqrt(3)/2) * k12 / (zstar * zp)
c0p = 4/(3*pi)*cB_mod**2
print("gamma1      =", mp.nstr(g1, 20))
print("zeta'(rho1) =", mp.nstr(zp, 20))
print("|zeta'(rho1)|=", mp.nstr(fabs(zp), 20))
print("k(1/2)      =", mp.nstr(k12, 20), " check:", mp.nstr(k12b, 20), " diff:", mp.nstr(fabs(k12-k12b), 3))
print("z*          =", mp.nstr(zstar, 20), " |z*| =", mp.nstr(absz, 20))
print("|c_B|       =", mp.nstr(cB_mod, 20))
print("c_B (omega=1)=", mp.nstr(cB, 20))
print("c_0'        =", mp.nstr(c0p, 20))
# stability check at higher precision
mp.dps = 80
rho1h = zetazero(1); zph = zeta(rho1h, derivative=1)
cBh = (mpf(3)/2)*fabs(k(mpf(1)/2))/(sqrt(3)*fabs(mpc(mpf(1)/4,-rho1h.imag/2))*fabs(zph))
mp.dps = 50
print("dps80 |c_B| =", mp.nstr(cBh, 20), " reldiff:", mp.nstr(fabs(cBh-cB_mod)/cB_mod, 3))
# rigorous-radius ingredients: verify zeta(rho1)=0 residual and local disc data
mp.dps = 50
print("|zeta(rho1)| =", mp.nstr(fabs(zeta(rho1)), 3))
# second derivative for Taylor radius argument
z2 = zeta(rho1, derivative=2)
print("|zeta''(rho1)| =", mp.nstr(fabs(z2), 10))
# max |zeta| on circle |w-rho1|=1/2 (for L-105058.5-style fallback constant)
import math
mx = 0
for j in range(240):
    th = 2*math.pi*j/240
    v = fabs(zeta(rho1 + mpf(1)/2*mpc(math.cos(th), math.sin(th))))
    mx = max(mx, v)
print("max_{|w-rho1|=1/2}|zeta| =", mp.nstr(mx, 10))
