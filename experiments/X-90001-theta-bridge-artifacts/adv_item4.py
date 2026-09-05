import numpy as np, math, mpmath as mp
mp.mp.dps = 30

zh  = complex(mp.zeta(0.5))      # zeta(1/2)
zph = complex(mp.zeta(0.5, derivative=1))  # zeta'(1/2)

# ---------- (a0) ghat formula vs direct quadrature ----------
def ghat_formula(w):
    return -(w-0.5)**-2 + 4/(w-0.5) - 4/w

print("== ghat check ==")
for w in [mp.mpc(2,3), mp.mpc(1.5,-2), mp.mpc(0.9,0.7)]:
    direct = mp.quad(lambda u: ((mp.log(u)+4)/mp.sqrt(u) - 4)*u**(w-1), [0,1])
    f = -(w-mp.mpf(0.5))**-2 + 4/(w-mp.mpf(0.5)) - 4/w
    print(f"  w={complex(w)}  |direct-formula| = {abs(complex(direct-f)):.2e}")

# ---------- cell data ----------
M = 2_000_000
N = np.arange(1, M+1, dtype=np.float64)
S = np.cumsum(N**-0.5)                      # S_N
A = np.cumsum(np.log(N)/np.sqrt(N))         # A_N

def E_cell(theta):
    """E(theta) via cell formula, theta array in (0,1]."""
    theta = np.asarray(theta, dtype=np.float64)
    n = np.floor(1.0/theta).astype(np.int64)
    n = np.minimum(n, M)
    Sn = S[n-1]; An = A[n-1]
    return theta**-0.5*(An + (Sn+1)*np.log(theta) + 4*Sn) - 4*n

def E_raw(theta):
    th = float(theta); n = int(math.floor(1.0/th))
    k = np.arange(1, n+1, dtype=np.float64)*th
    return float(np.sum((np.log(k)+4)/np.sqrt(k) - 4)) - th**-0.5*math.log(1/th)

print("\n== cell formula vs raw E at random theta ==")
rng = np.random.default_rng(7)
ths = np.concatenate([rng.uniform(1e-4, 1, 8), [0.5, 1/3+1e-12, 0.999]])
err = max(abs(E_raw(t) - E_cell(np.array([t]))[0]) for t in ths)
print(f"  max |E_raw - E_cell| over 11 pts = {err:.2e}")

# ---------- (a) Ehat(w) via exact cell integrals + smooth tail ----------
def Ehat_cells(w, Muse):
    n = np.arange(1, Muse+1, dtype=np.float64)
    a = 1.0/(n+1); b = 1.0/n
    wm = w - 0.5
    P  = lambda t: t**wm/wm
    Q  = lambda t: t**wm*(wm*np.log(t)-1)/wm**2
    I1 = P(b)-P(a); I2 = Q(b)-Q(a); I3 = (b**w-a**w)/w
    cells = (A[:Muse]+4*S[:Muse])*I1 + (S[:Muse]+1)*I2 - 4*n*I3
    return np.sum(cells[::-1])

def Ehat_tail(w, Muse):
    # E(theta) ~ theta^{-1/2}[(1+zh)log th + (4zh - zph)] + 2*delta, delta mean 1/2
    tM = 1.0/(Muse+1); wm = w-0.5
    c1 = 1+zh; c0 = 4*zh - zph
    t1 = c1*tM**wm*(wm*np.log(tM)-1)/wm**2
    t0 = c0*tM**wm/wm
    saw = tM**w/w   # 2*mean(delta)=1 times int theta^{w-1}
    return t1+t0+saw

def Ehat_num(w, Muse=M):
    return Ehat_cells(w, Muse) + Ehat_tail(w, Muse)

def Ehat_formula(w):
    return complex(mp.zeta(w))*ghat_formula(w) - (w-0.5)**-2

print("\n== dual identity Ehat(w)=zeta(w)ghat(w)-(w-1/2)^{-2} ==")
for w in [2+3j, 2.5-5j, 3+0.7j, 1.5+11j, 0.8+2j]:
    num1 = Ehat_num(w, 1_000_000); num2 = Ehat_num(w, M)
    f = Ehat_formula(w)
    print(f"  w={w}: |num-formula|={abs(num2-f):.2e}  (M-stability {abs(num2-num1):.2e})")

print("\n== (b) Ehat(1) = int_0^1 E ==")
for Mu in (1_000_000, M):
    print(f"  M={Mu}: int_0^1 E = {Ehat_num(1.0+0j, Mu).real:.3e}")
gp1 = 2*(0.5)**-3 - 4*(0.5)**-2 + 4  # ghat'(1)
print(f"  symbolic: ghat(1) = {-(0.5)**-2 + 4/0.5 - 4}, ghat'(1) = {gp1}, so lim zeta*ghat = {gp1}, Ehat(1) = {gp1-4}")

# ---------- (c) residue at a sample zero ----------
print("\n== (c) residue check at first zero (numerical, on-line zero as proxy) ==")
rho = complex(mp.mpc(0.5, mp.zetazero(1).imag))
print(f"  Ehat(rho) formula = {Ehat_formula(rho):.6f}  vs -(rho-1/2)^-2 = {-(rho-0.5)**-2:.6f}")

# ---------- (d/e) Phi vs A_X, ramp piece ----------
def sieve(n):
    s = np.ones(n+1, dtype=bool); s[:2] = False
    for i in range(2, int(n**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

def bvals(m, X):
    m = np.asarray(m, dtype=np.float64)
    out = 2.0*np.sqrt(m)*(np.log(X/m) - 2.0*(1.0-np.sqrt(m/X)))
    out[(m<2)|(m>X)] = 0.0
    return out

def int_E(theta_low):
    """int_{theta_low}^1 E(t) dt via cell closed forms at w=1."""
    n0 = int(math.floor(1.0/theta_low))
    n = np.arange(1, n0, dtype=np.float64)   # full cells 1..n0-1: [1/(n+1),1/n]
    a = 1.0/(n+1); b = 1.0/n
    I1 = 2*(np.sqrt(b)-np.sqrt(a))
    I2 = 2*(np.sqrt(b)*(np.log(b)-2) - np.sqrt(a)*(np.log(a)-2))
    I3 = b-a
    tot = np.sum(((A[:n0-1]+4*S[:n0-1])*I1 + (S[:n0-1]+1)*I2 - 4*n*I3)[::-1])
    # partial cell [theta_low, 1/n0]
    a2, b2 = theta_low, 1.0/n0
    I1 = 2*(math.sqrt(b2)-math.sqrt(a2))
    I2 = 2*(math.sqrt(b2)*(math.log(b2)-2) - math.sqrt(a2)*(math.log(a2)-2))
    I3 = b2-a2
    tot += (A[n0-1]+4*S[n0-1])*I1 + (S[n0-1]+1)*I2 - 4*n0*I3
    return tot

print("\n== (d/e) A_X vs Phi(X), unconditional ramp piece ==")
XMAX = 100_000
primes_all = sieve(XMAX)
for X in (10_000, 30_000, 100_000):
    pr = primes_all[primes_all<=X]
    lp = np.log(pr.astype(np.float64))
    v = np.array([float(np.sum(bvals(np.arange(1, X//q+1, dtype=np.int64)*q, X)
                               - bvals(np.arange(1, X//q+1, dtype=np.int64)*q+1, X))) for q in pr])
    ramp = pr**-0.5*np.log(X/pr.astype(np.float64))
    A_X = float(np.sum(lp*(v-ramp)))
    V   = float(np.sum(lp*v))
    Rr  = float(np.sum(lp*ramp))                     # the 'ramp sum'
    # Phi(X) = X^{-1/2}[ sum_p log p E(p/X) - int_2^X E(t/X)dt ]
    Ep = E_cell(pr.astype(np.float64)/X)
    Phi = X**-0.5*(float(np.sum(lp*Ep)) - X*int_E(2.0/X))
    theta_R = 4*math.sqrt(X) - Rr
    print(f"  X={X}: A_X={A_X:+9.4f}  Phi={Phi:+9.4f}  A-Phi={A_X-Phi:+8.4f} (logX={math.log(X):.2f})"
          f"  V-4sqrtX={V-4*math.sqrt(X):+9.4f}  4sqrtX-ramp={theta_R:+9.4f}")
