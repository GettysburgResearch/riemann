import mpmath as mp
mp.mp.dps = 20
rho = mp.mpc(mp.mpf('0.5'), mp.im(mp.zetazero(1)))
gam = mp.im(rho); zp = mp.zeta(rho, derivative=1)
zst=(rho-1)/2; r=mp.mpf('0.125'); s1=rho-1
b1,z1=mp.mpf('0.3'),mp.mpf('0.2')
c_p = -mp.power(2,-zst)/(zst*zp)
c0p = (4/mp.pi)*abs(c_p)**2
print("|c_p| =", mp.nstr(abs(c_p),8), "  c0' = (4/pi)|c_p|^2 =", mp.nstr(c0p,6))
gform = 16*mp.sqrt(2)/(mp.pi*(mp.mpf('0.25')+gam**2)*abs(zp)**2)
print("closed form 16 sqrt2/(pi(1/4+g^2)|zp|^2) =", mp.nstr(gform,6))

def a_amp(x):   # frozen amplitude a(x, rho)
    return (mp.power(2,-(zst+x))/(zst+x))*(1-b1*x)/(zp*(1+z1*x))

# Amp(L) and the density dictionary check
def Amp(L):
    return -(2/mp.pi)*mp.quad(lambda xi: a_amp(xi**2)*mp.e**(-L*xi**2),[0,mp.sqrt(2*r)])
print("[N3a] density dictionary Amp(L)*sqrt(pi L)/c_p -> 1:")
for L in [20,100,1000,10000]:
    print("  L=%-6d ratio-1 = %s" % (L, mp.nstr(Amp(L)*mp.sqrt(mp.pi*L)/c_p - 1, 3)))

# Q_W(T)/log T -> c0'
def uW2(L):   # u W_u^2 at L=log u  (= (u^{1/2}W)^2), W=sqrt(2L)*2 Re lambda_m
    lam = Amp(L)*mp.exp(1j*gam*L)      # u^{s1} -> u^{-1/2} e^{i gam L}; u^{1/2}lam = Amp e^{igL}
    return 2*L*(2*mp.re(lam))**2
print("[N3b] Q_W(T)/log T vs c0' (expect -> 1 with O(1/log T)):")
for LT in [50, 200, 800, 3200]:
    per = 2*mp.pi/gam
    Q = mp.quad(uW2, mp.linspace(1, LT, max(60,int(LT/per)+1)))
    Q1 = mp.quad(uW2, mp.linspace(0, 1, 8))
    print("  logT=%-5d (Q/logT)/c0' = %s" % (LT, mp.nstr((Q+Q1)/LT/c0p, 6)))

# window integral: F_W on probe line, closed forms
G32 = mp.gamma(mp.mpf('1.5'))
def Gfun(sp):
    eps = sp - s1
    return -(G32/mp.pi)*(2)*mp.quad(lambda xi: a_amp(xi**2)*mp.power(xi**2+eps,mp.mpf('-1.5')),
                                    [0,mp.sqrt(2*r)])
def Gcfun(sp):
    eps = sp - mp.conj(s1)
    return -(G32/mp.pi)*(2)*mp.quad(lambda xi: mp.conj(a_amp(xi**2))*mp.power(xi**2+eps,mp.mpf('-1.5')),
                                    [0,mp.sqrt(2*r)])
def FW(sp): return mp.sqrt(2)*(Gfun(sp)+Gcfun(sp))
# sanity: G pole constant
for ev in [mp.mpf('1e-3'), mp.mpc('1e-4','1e-4')]:
    print("[N3c] G*eps/(c_p/sqrt(pi)) - 1 =", mp.nstr(Gfun(s1+ev)*ev/(c_p/mp.sqrt(mp.pi))-1, 3))
print("[N3d] window law: h-scaled window integral / prediction -> 1:")
r0 = mp.mpf('0.5')
for h in [mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')]:
    I = mp.quad(lambda t: abs(FW(mp.mpc(-0.5,0)+h+1j*t))**2, mp.linspace(gam-r0, gam+r0, 41))
    pred = (2*abs(c_p)**2/mp.pi)*(2/h)*mp.atan(r0/h)
    print("  h=%s  I/pred = %s" % (mp.nstr(h,2), mp.nstr(I/pred, 6)))
