import mpmath as mp
mp.mp.dps = 20
rho = mp.mpc(mp.mpf('0.5'), mp.im(mp.zetazero(1)))
zp  = mp.zeta(rho, derivative=1); zst=(rho-1)/2; r=mp.mpf('0.125')
b1,z1=mp.mpf('0.3'),mp.mpf('0.2')
c_p = -mp.power(2,-zst)/(zst*zp)
sqpi = mp.sqrt(mp.pi)

# B2 standalone: D^{1/2}[(s-a)^{-1/2}] = (1/sqrt(pi))(s-a)^{-1}
a0 = mp.mpc(0.3,1.1)
for sv in [a0+mp.mpc('0.02','0.01'), a0+mp.mpc('1e-3','-2e-3')]:
    Fp = lambda t: -mp.mpf('0.5')*mp.power(t-a0,mp.mpf('-1.5'))
    G  = -(1/sqpi)*2*mp.quad(lambda xi: Fp(sv+xi**2), [0, mp.sqrt(abs(sv-a0)), 1, mp.inf])
    pred = (1/sqpi)/(sv-a0)
    print("[N2a] B2 check s-a=%s: |G/pred - 1| = %s" % (mp.nstr(sv-a0,3), mp.nstr(abs(G/pred-1),3)))

# model F' (analytic differentiation of the collapsed representation)
def a_amp(x,s):
    zb=(s-1)/2; eps=s-rho
    return (mp.power(2,-(zb+x))/(zb+x))*(1+b1*(1-x-1))/(zp*(1+z1*(eps+x)))
def dlog_a(x,s):
    zb=(s-1)/2; eps=s-rho
    return -mp.log(2)/2 - mp.mpf('0.5')/(zb+x) - z1/(1+z1*(eps+x))
def Fp_col(s):
    eps=s-rho
    integ = lambda xi: a_amp(xi**2,s)*( dlog_a(xi**2,s)/(xi**2+eps) - 1/(xi**2+eps)**2 )
    return -(2/mp.pi)*mp.quad(integ,[0,mp.sqrt(abs(eps)),mp.sqrt(2*r)])

# sanity: Fp_col vs numeric diff of F_col
def F_col(s):
    eps=s-rho
    return -(2/mp.pi)*mp.quad(lambda xi: a_amp(xi**2,s)/(xi**2+eps),[0,mp.sqrt(abs(eps)),mp.sqrt(2*r)])
s0=rho+mp.mpc('1e-2','3e-3'); dd=mp.mpf('1e-7')
nd=(F_col(s0+dd)-F_col(s0-dd))/(2*dd)
print("[N2b] Fp_col vs numeric diff: rel = %s" % mp.nstr(abs(Fp_col(s0)-nd)/abs(nd),3))

# Theorem B composition: G = D^{1/2}F_col -> (c_p/sqrt(pi)) eps^{-1}
def G_weyl(s):
    eps=s-rho
    return -(1/sqpi)*2*mp.quad(lambda xi: Fp_col(s+xi**2),
                               [0, mp.sqrt(abs(eps)), mp.sqrt(r), 1, 3, mp.inf])
print("[N2c] full-pole restoration: ratio := G*eps/(c_p/sqrt(pi)); expect 1+O(eps log):")
for ev in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpc('1e-3','1e-3'), mp.mpf('1e-4'),
           mp.mpc('5e-5','-5e-5')]:
    s=rho+ev
    ratio=G_weyl(s)*ev/(c_p/sqpi)
    print("  eps=%-18s ratio-1 = %s" % (mp.nstr(ev,3), mp.nstr(ratio-1,4)))
