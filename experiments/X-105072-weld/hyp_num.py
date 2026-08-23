import mpmath as mp
mp.mp.dps = 30

rho1 = mp.zetazero(1)
gamma1 = mp.im(rho1)
zp1 = mp.zeta(rho1, derivative=1)
zpp1 = mp.zeta(rho1, derivative=2)
zstar = mp.mpf(1)/4 - 1j*gamma1/2
ln2 = mp.log(2)

def k(b):
    b = mp.mpc(b)
    if abs(b) < mp.mpf('0.01'):
        # entire: series k = ln2/2 - b ln2^2/6 + b^2 ln2^3/24 - ... = sum_{n>=0} (-1)^n ln2^{n+1} b^n /(n+2)!*? use exact: (1-2^{-b})/b^2/ln2 expansion
        s = mp.mpc(0)
        for n in range(0, 25):
            s += (-1)**n * ln2**(n+1) * b**n / mp.factorial(n+2)
        return 1/b - (1/b - s)  # placeholder never used in region |b|>=1/8
    return 1/b - (1 - 2**(-b))/(b**2 * ln2)

def kp(b):  # k'
    h = mp.mpf(10)**(-12)
    return (k(b+h)-k(b-h))/(2*h)

def bfun(v):
    v = mp.mpc(v)
    if abs(v-1) < mp.mpf(10)**(-9):
        return mp.mpf(1) + mp.euler/2*(v-1)
    return mp.sqrt((v-1)*mp.zeta(v))

def Z1(w):
    w = mp.mpc(w)
    if abs(w) < mp.mpf(10)**(-8):
        return zp1 + zpp1*w/2
    return mp.zeta(rho1+w)/w

def Z1p(w):
    h = mp.mpf(10)**(-10)
    return (Z1(w+h)-Z1(w-h))/(2*h)

R = []
def rec(name, val):
    R.append((name, val)); print(name, mp.nstr(val, 12))

rec('gamma1', gamma1)
rec('|zeta_p(rho1)|', abs(zp1))
rec('k(1/2)', k(mp.mpf('0.5')))
rec('kp(1/2)', kp(mp.mpf('0.5')))
rec('k(1/4)', k(mp.mpf('0.25')))

# --- K_N: sup |k| on rectangle [1/8, 5/8] x [-1/8, 1/8]  (contains the beta-stadium)
best = 0; lipk = 0
N = 120
for i in range(N+1):
    for j in range(N+1):
        b = mp.mpf('0.125') + mp.mpf('0.5')*i/N + 1j*(mp.mpf('-0.125') + mp.mpf('0.25')*j/N)
        m = abs(k(b)); best = max(best, m)
        if i % 8 == 0 and j % 8 == 0:
            lipk = max(lipk, abs(kp(b)))
h = mp.mpf('0.5')/N
K_N = best + lipk*h  # grid max + Lipschitz margin
rec('K_N(sup k on beta rect, w/ margin)', K_N)
rec('lip_k', lipk)

# K_r: max k on real [1/4,1/2]
K_r = max(abs(k(mp.mpf('0.25')+mp.mpf('0.25')*i/200)) for i in range(201))
rec('K_r(real)', K_r)

# --- b on v-rectangle [0.625, 1.125] x [-1/8, 1/8]: sup|b|, min Re((v-1)zeta(v))
bestb = 0; minre = mp.mpf(10); lipb = 0
for i in range(N+1):
    for j in range(N+1):
        v = mp.mpc(mp.mpf('0.625') + mp.mpf('0.5')*i/N, mp.mpf('-0.125') + mp.mpf('0.25')*j/N)
        if abs(v-1) < mp.mpf(10)**(-9):
            g = mp.mpc(1)
        else:
            g = (v-1)*mp.zeta(v)
        minre = min(minre, mp.re(g))
        m = abs(mp.sqrt(g)); bestb = max(bestb, m)
hh = mp.mpf(10)**(-8)
for i in range(0, N+1, 8):
    for j in range(0, N+1, 8):
        v = mp.mpf('0.625') + mp.mpf('0.5')*i/N + 1j*(mp.mpf('-0.125') + mp.mpf('0.25')*j/N)
        d = (bfun(v+hh)-bfun(v-hh))/(2*hh)
        lipb = max(lipb, abs(d))
B_N = bestb + lipb*h
rec('B_N(sup b, w/ margin)', B_N)
rec('min Re((v-1)zeta(v)) on rect', minre)
B_r = max(abs(bfun(mp.mpf('0.75')+mp.mpf('0.25')*i/200)) for i in range(201))
rec('B_r(real [3/4,1])', B_r)
rec('b_prime(1) approx (gammaE/2?)', (bfun(1+mp.mpf(10)**(-6))-bfun(1-mp.mpf(10)**(-6)))/(2*mp.mpf(10)**(-6)))

# --- Z_N: inf |Z1| on |w| <= 5/8  (min modulus on boundary circle; interior sanity)
minZ = mp.mpf(10); lipZ = 0
M = 800
for i in range(M):
    w = mp.mpf('0.625')*mp.exp(2j*mp.pi*i/M)
    m = abs(Z1(w)); minZ = min(minZ, m)
    if i % 20 == 0:
        lipZ = max(lipZ, abs(Z1p(w)))
step = 2*mp.pi*mp.mpf('0.625')/M
Z_N = minZ - lipZ*step/2
rec('Z_N(inf |Z1| disk 5/8, w/ margin)', Z_N)
# interior sanity
sanity = min(abs(Z1(mp.mpf('0.625')*r_*mp.exp(2j*mp.pi*i/40))) for r_ in [mp.mpf('0.2'),mp.mpf('0.5'),mp.mpf('0.8')] for i in range(40))
rec('Z disk interior sanity min', sanity)

# --- Z_c: inf |Z1| on rectangle boundary Re in [-1/16, 3/2], Im in [-3.2, 3.2]
pts = []
Mb = 500
for i in range(Mb+1):
    t = mp.mpf(i)/Mb
    pts.append(mp.mpf('-0.0625') + t*mp.mpf('1.5625') + 3.2j)
    pts.append(mp.mpf('-0.0625') + t*mp.mpf('1.5625') - 3.2j)
    pts.append(mp.mpf('-0.0625') + 1j*(-3.2 + t*mp.mpf('6.4')))
    pts.append(mp.mpf('1.5') + 1j*(-3.2 + t*mp.mpf('6.4')))
minZc = mp.mpf(10); lipZc = 0
for idx, w in enumerate(pts):
    m = abs(Z1(w)); minZc = min(minZc, m)
    if idx % 40 == 0:
        lipZc = max(lipZc, abs(Z1p(w)))
stepc = mp.mpf('6.4')/Mb
Z_c = minZc - lipZc*stepc/2
rec('Z_c(inf |Z1| rect bdry, w/ margin)', Z_c)
# interior sanity coarse
s2 = mp.mpf(10)
for i in range(31):
    for j in range(41):
        w = mp.mpf('-0.0625') + mp.mpf('1.5625')*i/30 + 1j*(-3.2 + mp.mpf('6.4')*j/40)
        s2 = min(s2, abs(Z1(w)))
rec('Z rect interior sanity min', s2)

# --- ratio_max for far tail: sup_{Res>=5/12} (3*Res+1.8125)/sqrt((1.5*Res-0.25)^2+6.27^2)
rmax = 0; argmax = 0
x = mp.mpf('5')/12
while x < 500:
    r_ = (3*x + mp.mpf('1.8125'))/mp.sqrt((mp.mpf('1.5')*x - mp.mpf('0.25'))**2 + mp.mpf('6.27')**2)
    if r_ > rmax: rmax = r_; argmax = x
    x *= mp.mpf('1.01')
rec('ratio_max', rmax); rec('ratio argmax Res', argmax)

# --- kappa(s0): coefficient of (s-s0)^{1/2} in R_loc
gammaE = mp.euler
A0 = k(mp.mpf('0.5'))/(zstar*zp1)
bracket = 3*kp(mp.mpf('0.5'))/k(mp.mpf('0.5')) + mp.mpf('1.5')*gammaE - mp.mpf('1.5')/zstar
kappa = mp.sqrt(3)/2 * A0 * bracket
rec('A0 = k/(z* zeta_p)', A0)
rec('|A0|', abs(A0))
rec('kappa(s0)', kappa)
rec('|kappa(s0)|', abs(kappa))

# numeric cross-check of kappa via direct derivatives
def A0s(s):
    eps = 3*(s - 1j*gamma1/3)
    return k(mp.mpf('0.5'))/((mp.mpf('0.25')-mp.mpf('1.5')*s)*Z1(eps))
hd = mp.mpf(10)**(-8)
s0 = 1j*gamma1/3
As_num = (A0s(s0+hd)-A0s(s0-hd))/(2*hd)
def Ax(x):
    return k(mp.mpf('0.5')-x)*bfun(1-x)/((zstar-x)*Z1(x))
Ax_num = (Ax(hd)-Ax(-hd))/(2*hd)
kappa2 = mp.sqrt(3)/2*(As_num - 3*Ax_num)
rec('kappa cross-check', kappa2)

# ---------------- assembly ----------------
sep_N  = gamma1/2 - mp.mpf('1.5')/24 - mp.mpf('0.125')
sep_NN = gamma1/2 - mp.mpf('0.125') - mp.mpf('0.125')
sep_0N = gamma1/2 - mp.mpf('1.5')/24
sep_F  = gamma1/2 - mp.mpf('1.5')*(mp.mpf('0.5')+mp.mpf(1)/96)
rec('sep_N', sep_N); rec('sep_NN', sep_NN); rec('sep_F', sep_F)

A_N  = K_N*B_N/(sep_N*Z_N)
A_NN = K_N*B_N/(sep_NN*Z_N)
A_0N = k(mp.mpf('0.5'))/(sep_0N*Z_N)
S_1  = k(mp.mpf('0.5'))/(sep_NN*Z_N)
A_1  = 8*S_1
M_a  = 8*A_N
M_sx = 192*A_NN
rec('A_N', A_N); rec('A_NN', A_NN); rec('A_0N', A_0N); rec('A_1', A_1)
rec('M_a', M_a); rec('M_sx', M_sx)

cB = mp.mpf('0.04782893516094')
A_F = K_r*B_r*max(1/(sep_F*Z_c), mp.mpf('1.51988')*rmax)
rec('A_F', A_F)

E1 = 3/(2*mp.pi)*M_a
E2 = 6/mp.pi*A_0N
E3 = mp.sqrt(3)/2*A_1/mp.sqrt(24)
M_R_N = E1+E2+E3
rec('E1', E1); rec('E2', E2); rec('E3', E3); rec('M_R_N', M_R_N)

M_R_F = 3/(2*mp.pi)*A_F*8*mp.sqrt(2) + cB*mp.sqrt(24)
rec('M_R_F', M_R_F)

C0 = 3/(2*mp.pi)*(M_sx + 4*A_1 + 16*A_0N)
C1 = 3*mp.sqrt(3)/4*A_1 + 4*mp.sqrt(3)/mp.pi*M_a
rec('C0', C0); rec('C1', C1)

M_R_C = 3/(2*mp.pi)*A_F*mp.mpf('13.06') + cB*mp.sqrt(32)
M_D_F = 96*M_R_C
rec('M_R_C', M_R_C); rec('M_D_F', M_D_F)

M_loc = max(M_R_N, M_R_F, C0, C1, M_D_F)
rec('M_loc = max(...)', M_loc)
# literal on |s-s0|>=d, d=1/24:
lit = max(M_R_N, M_R_F) + max(C0 + C1*mp.sqrt(24), M_D_F)
rec('M_loc_literal(d=1/24)', lit)
