import mpmath as mp
mp.mp.dps = 30

# genuine first-zero data for the model constants
rho = mp.mpc(mp.mpf('0.5'), mp.im(mp.zetazero(1)))
gam = mp.im(rho)
zp  = mp.zeta(rho, derivative=1)          # zeta'(rho1), simplicity constant
zst = (rho - 1)/2
r   = mp.mpf('0.125')

b1, z1 = mp.mpf('0.3'), mp.mpf('0.2')     # non-constant test amplitudes
def bfun(v):  return 1 + b1*(v - 1)
def Zfun(v):  return zp*(1 + z1*(v - rho))

def zb(s):    return (s - 1)/2
def w_of(s):  return (1 + s)/2

def Psi(z, s):
    w = w_of(s)
    return (mp.power(2, -z)/z) * bfun(w - z) * mp.power(-(z - zb(s)), mp.mpf('-0.5')) \
           / ((w + z - rho) * Zfun(w + z))

def F_loop(s, delta=None):
    eps = s - rho
    zbs = zb(s)
    if delta is None:
        delta = min(abs(eps), r/10)/10
    # lower edge: x from 2r down to delta at -i delta
    f1 = mp.quad(lambda x: Psi(zbs + x - 1j*delta, s), [2*r, delta])
    # cap: theta from -pi/2 to -3pi/2 (leftward around zb, avoids the cut)
    f2 = mp.quad(lambda th: Psi(zbs + delta*mp.exp(1j*th), s)*1j*delta*mp.exp(1j*th),
                 [-mp.pi/2, -mp.pi, -3*mp.pi/2])
    # upper edge: x from delta to 2r at +i delta
    f3 = mp.quad(lambda x: Psi(zbs + x + 1j*delta, s), [delta, 2*r])
    return (f1 + f2 + f3)/(2j*mp.pi)

def a_amp(x, s):
    eps = s - rho
    return (mp.power(2, -(zb(s) + x))/(zb(s) + x)) * bfun(1 - x) / Zfun(rho + eps + x)

def F_col(s):
    eps = s - rho
    # x = xi^2 substitution kills the endpoint singularity
    return -(2/mp.pi)*mp.quad(lambda xi: a_amp(xi**2, s)/(xi**2 + eps),
                              [0, mp.sqrt(2*r)])

c_p = -mp.power(2, -zst)/(zst*zp)
print("gamma1 =", mp.nstr(gam, 12), " zeta'(rho1) =", mp.nstr(zp, 10))
print("z_* =", mp.nstr(zst, 10), " c_p =", mp.nstr(c_p, 10), " |c_p| =", mp.nstr(abs(c_p), 8))

print("\n[N1a] loop vs collapse (validates collapse identity incl. sign/branch):")
for epsv in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpc('1e-3','5e-4'), mp.mpc('2e-3','-1e-3')]:
    s = rho + epsv
    fl, fc = F_loop(s), F_col(s)
    print("  eps=%-22s |loop-col|/|col| = %s" % (mp.nstr(epsv,3), mp.nstr(abs(fl-fc)/abs(fc), 3)))

print("\n[N1b] pinch asymptotics: ratio := F_col * eps^{1/2} / c_p  (expect 1 + O(sqrt eps)):")
for k in [2,3,4,5,6,8]:
    for th in [0, mp.pi/4, -mp.pi/4, mp.pi/2*mp.mpf('0.99')]:
        epsv = mp.mpf(10)**(-k) * mp.exp(1j*th)
        s = rho + epsv
        ratio = F_col(s)*mp.sqrt(epsv)/c_p
        print("  |eps|=1e-%d th=%5.2f  ratio-1 = %s" % (k, float(th), mp.nstr(ratio-1, 4)))

print("\n[N1c] slope check: (ratio-1)/sqrt|eps| should stabilize (kappa=1/2):")
for k in [3,4,5,6,7,8]:
    epsv = mp.mpf(10)**(-k)
    ratio = F_col(rho+epsv)*mp.sqrt(epsv)/c_p
    print("  1e-%d : (ratio-1)/sqrt(eps) = %s" % (k, mp.nstr((ratio-1)/mp.sqrt(epsv), 5)))
