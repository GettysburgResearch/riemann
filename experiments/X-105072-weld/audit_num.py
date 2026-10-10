import mpmath as mp
mp.mp.dps = 30

rho1 = mp.zetazero(1); g1 = mp.im(rho1)
zp1 = mp.zeta(rho1, derivative=1)
zstar = mp.mpf(1)/4 - 1j*g1/2
ln2 = mp.log(2)
s0 = 1j*g1/3

def k(b):
    b = mp.mpc(b)
    return 1/b - (1 - 2**(-b))/(b**2 * ln2)

# --- A5: constants to 20 digits
print("gamma1      =", mp.nstr(g1, 20))
print("k(1/2)      =", mp.nstr(k(mp.mpf('0.5')), 20))
print("k closed    =", mp.nstr(2 - 4*(1-1/mp.sqrt(2))/ln2, 20))
print("|z*|        =", mp.nstr(abs(zstar), 20))
print("zeta'(rho1) =", mp.nstr(zp1, 20))
print("|zeta'|     =", mp.nstr(abs(zp1), 20))
cB = mp.sqrt(3)/2 * k(mp.mpf('0.5'))/(zstar*zp1)
print("|c_B|       =", mp.nstr(abs(cB), 20))
print("c_0'        =", mp.nstr(4/(3*mp.pi)*abs(cB)**2, 20))
print("gamma2-gamma1 =", mp.nstr(mp.im(mp.zetazero(2))-g1, 15))

# --- kappa closed form + direct
def kp(b, h=mp.mpf(10)**-10):
    return (k(b+h)-k(b-h))/(2*h)
A0 = k(mp.mpf('0.5'))/(zstar*zp1)
br = 3*kp(mp.mpf('0.5'))/k(mp.mpf('0.5')) + mp.mpf('1.5')*mp.euler - mp.mpf('1.5')/zstar
kap = mp.sqrt(3)/2*A0*br
print("kappa closed =", mp.nstr(kap, 15), " |kappa|=", mp.nstr(abs(kap), 12))

# --- independent kappa via R_loc fit (tests c_B sign/omega AND kappa)
def bfun(v):
    v = mp.mpc(v)
    if abs(v-1) < mp.mpf(10)**-12: return mp.mpf(1)
    return mp.sqrt((v-1)*mp.zeta(v))
def Z1(w):
    w = mp.mpc(w)
    if abs(w) < mp.mpf(10)**-12: return zp1
    return mp.zeta(rho1+w)/w
def A(x, s):
    return k(mp.mpf('0.5')-x)*bfun(1-x)/((mp.mpf('0.25')-mp.mpf('1.5')*s - x)*Z1(3*(s-s0)+x))
def Zloc(s):
    eps = 3*(s-s0)
    f = lambda u: 2*A(u**2, s)/(u**2+eps)   # x=u^2
    return 3/(2*mp.pi)*mp.quad(f, [0, mp.mpf('0.5')])
def Rloc(s):
    return Zloc(s) - mp.sqrt(3)/2*A0*(s-s0)**mp.mpf('-0.5')
for th in [0, mp.pi/4]:
    e = mp.exp(1j*th)
    t1, t2 = mp.mpf(10)**-4, mp.mpf(10)**-6
    est = (Rloc(s0+t1*e)-Rloc(s0+t2*e))/((mp.sqrt(t1)-mp.sqrt(t2))*mp.exp(1j*th/2))
    print("kappa fit (arg %s) =" % mp.nstr(th,3), mp.nstr(est, 10))

# residual size check: |Rloc| small near s0 (row 10 sanity)
print("|Rloc(s0+1e-4)| =", mp.nstr(abs(Rloc(s0+mp.mpf(10)**-4)), 8))
print("|Rloc(0.2+i Im s0)| =", mp.nstr(abs(Rloc(mp.mpf('0.2')+1j*g1/3)), 8))

# --- deformation identity numeric test at anchor s
s = mp.mpf('0.23') + 1j*(g1/3 + mp.mpf('0.3'))
a = mp.mpf('0.75') + mp.mpf('1.5')*s
zb = 1 - a
mub = mp.im(zb)
# branch scan: does (v-1)zeta(v) hit (-inf,0] on v-image [3/4,1.19]x[-2,2]?
minre_pathological = False; worst = mp.mpf(10)
for i in range(25):
    for j in range(41):
        v = mp.mpf('0.75') + mp.mpf('0.44')*i/24 + 1j*(-2 + mp.mpf('4')*j/40)
        gv = (v-1)*mp.zeta(v)
        if mp.re(gv) <= 0 and abs(mp.im(gv)) < mp.mpf('0.05'): minre_pathological = True
        worst = min(worst, mp.re(gv))
print("v-image min Re((v-1)zeta) =", mp.nstr(worst, 8), " near-neg-axis:", minre_pathological)

def Psi(z):
    z = mp.mpc(z)
    return mp.mpf('1.5')*k(mp.mpf('0.25')+mp.mpf('1.5')*s+z)*(z-zb)**mp.mpf('-0.5')*bfun(a+z)/(z*mp.zeta(a-z))
Y = 2; r2 = mp.mpf('0.25')  # 2r
c = mp.mpf('0.0625')
# S: vertical segment
IS = mp.quad(lambda y: Psi(c+1j*y)*1j, [mub-Y, mub, mub+Y])
# B_out: horizontal then vertical (lower side)
xL = mp.re(zb) - r2
I1 = mp.quad(lambda x: Psi(x+1j*(mub-Y)), [c, xL]) * (-1)  # left dir: integrate c->xL means dz=dx negative dir; do explicit
I1 = mp.quad(lambda x: Psi(x+1j*(mub-Y)), [xL, c]); I1 = -I1
I2 = mp.quad(lambda y: Psi(xL+1j*y)*1j, [mub-Y, mub])
# H hug with delta cap
delta = mp.mpf(10)**-4
low = mp.quad(lambda x: -Psi(zb - x - 1j*mp.mpf(10)**-25), [delta, r2])*(-1)  # param x: r2->delta, dz=-dx
low = mp.quad(lambda x: Psi(zb - x - 1j*mp.mpf(10)**-25), [delta, r2]); low = low  # x r2->delta: int = -int_{delta}^{r2}(-dx)... compute directly:
# lower edge z=zb-x-i0, x from r2 to delta: integral = int_{r2}^{delta} Psi*(-dx) = int_{delta}^{r2} Psi dx
Ilow = mp.quad(lambda x: Psi(zb - x - 1j*mp.mpf(10)**-20), [delta, r2])
# cap: z = zb + delta e^{i th}, th from -pi to +pi (ccw passing right)
Icap = mp.quad(lambda th: Psi(zb + delta*mp.exp(1j*th))*1j*delta*mp.exp(1j*th), [-mp.pi+mp.mpf(10)**-12, mp.pi-mp.mpf(10)**-12])
# upper edge z=zb-x+i0, x from delta to r2: integral = int Psi*(-dx) = -int_{delta}^{r2}
Iup = -mp.quad(lambda x: Psi(zb - x + 1j*mp.mpf(10)**-20), [delta, r2])
I3 = mp.quad(lambda y: Psi(xL+1j*y)*1j, [mub, mub+Y])
I4 = mp.quad(lambda x: Psi(x+1j*(mub+Y)), [xL, c])
tot = I1 + I2 + Ilow + Icap + Iup + I3 + I4
print("deform: |S - deformed| =", mp.nstr(abs(IS-tot), 8), " |S|=", mp.nstr(abs(IS),8))
# also hug-only vs collapsed (Z) at this s
hug = (Ilow + Icap + Iup)/(2j*mp.pi)
print("hug/(2pi i) vs Zloc(s):", mp.nstr(abs(hug - Zloc(s)), 8), " |Zloc|=", mp.nstr(abs(Zloc(s)),8))

# --- independent grid re-checks (coarser, different offsets)
KN = 0
for i in range(81):
    for j in range(33):
        b = mp.mpf('0.125') + mp.mpf('0.5')*i/80 + 1j*(-mp.mpf('0.125')+mp.mpf('0.25')*j/32)
        KN = max(KN, abs(k(b)))
print("K_N regrid =", mp.nstr(KN, 8))
BN = 0; mre = mp.mpf(10)
for i in range(81):
    for j in range(33):
        v = mp.mpf('0.625') + mp.mpf('0.5')*i/80 + 1j*(-mp.mpf('0.125')+mp.mpf('0.25')*j/32)
        gv = mp.mpc(1) if abs(v-1)<mp.mpf(10)**-12 else (v-1)*mp.zeta(v)
        mre = min(mre, mp.re(gv)); BN = max(BN, abs(mp.sqrt(gv)))
print("B_N regrid =", mp.nstr(BN,8), " minRe regrid =", mp.nstr(mre,8))
ZN = mp.mpf(10)
for i in range(1200):
    w = mp.mpf('0.625')*mp.exp(2j*mp.pi*(i+mp.mpf('0.5'))/1200)
    ZN = min(ZN, abs(Z1(w)))
print("Z_N regrid(1200 bdry, offset) =", mp.nstr(ZN,8))
Zc = mp.mpf(10)
for i in range(701):
    t = mp.mpf(i)/700
    for w in [mp.mpf('-0.0625')+t*mp.mpf('1.5625')+mp.mpf('3.2')*1j,
              mp.mpf('-0.0625')+t*mp.mpf('1.5625')-mp.mpf('3.2')*1j,
              mp.mpf('-0.0625')+1j*(-mp.mpf('3.2')+t*mp.mpf('6.4')),
              mp.mpf('1.5')+1j*(-mp.mpf('3.2')+t*mp.mpf('6.4'))]:
        Zc = min(Zc, abs(Z1(w)))
print("Z_c regrid =", mp.nstr(Zc,8))
# rmax recheck
rmax = 0
x = mp.mpf('5')/12
while x < 3000:
    r_ = (3*x+mp.mpf('1.8125'))/mp.sqrt((mp.mpf('1.5')*x-mp.mpf('0.25'))**2+mp.mpf('6.27')**2)
    rmax = max(rmax, r_); x *= mp.mpf('1.005')
print("rmax regrid =", mp.nstr(rmax,8), " zeta2/zeta4 =", mp.nstr(mp.zeta(2)/mp.zeta(4),8))
# E2 kernel bound worst case at |Im z|=40, Im beta shift 8.6
w1 = 1/mp.mpf('31.4') + (1+2**mp.mpf('-0.3125'))/(ln2*mp.mpf('31.4')**2)
print("E2 worst |k| at ImZ=40 (shifted) =", mp.nstr(w1,6), " vs 2/40 =", 0.05)
