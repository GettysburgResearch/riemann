import numpy as np
import mpmath as mp
mp.mp.dps = 25
rho_m = mp.mpc(mp.mpf('0.5'), mp.im(mp.zetazero(1)))
gam = float(mp.im(rho_m)); zp = complex(mp.zeta(rho_m, derivative=1))
rho = 0.5 + 1j*gam; zst = (rho-1)/2; r = 0.125; s1 = rho - 1
b1, z1 = 0.3, 0.2
c_p = -2**(-zst)/(zst*zp)
c0p = (4/np.pi)*abs(c_p)**2

xi, wq = np.polynomial.legendre.leggauss(240)
XI = 0.5*np.sqrt(2*r)*(xi+1); WQ = 0.5*np.sqrt(2*r)*wq   # nodes on [0, sqrt(2r)]
X = XI**2
AX = (2.0**(-(zst+X))/(zst+X))*(1-b1*X)/(zp*(1+z1*X))    # a(x) at nodes

def Amp_vec(L):      # L array -> Amp(L)
    return -(2/np.pi)*np.einsum('j,ij->i', AX*WQ, np.exp(-np.outer(L, X)))

print("[N3b] Q_W(T)/log T vs c0' (numpy):")
per = 2*np.pi/gam
for LT in [50, 200, 800, 3200, 12800]:
    n = int(LT/per*60)
    L = np.linspace(1e-9, LT, n)
    A = Amp_vec(L)
    integ = 2*L*(2*np.real(A*np.exp(1j*gam*L)))**2
    Q = np.trapezoid(integ, L)
    print("  logT=%-6d (Q/logT)/c0' = %.5f" % (LT, Q/LT/c0p))

def Gfun(eps_arr):   # -(Gamma(3/2)/pi) int a(x) x^{-1/2}(x+eps)^{-3/2} dx , xi-subst
    K = (XI[None,:]**2 + eps_arr[:,None])**(-1.5)
    return -(0.8862269254527580/np.pi)*2*np.einsum('j,ij->i', AX*WQ, K)
def Gcfun(eps_arr):
    K = (XI[None,:]**2 + eps_arr[:,None])**(-1.5)
    return -(0.8862269254527580/np.pi)*2*np.einsum('j,ij->i', np.conj(AX)*WQ, K)

print("[N3d] window law (tan substitution, 4000 nodes):")
r0 = 0.5
th, wth = np.polynomial.legendre.leggauss(4000)
for h in [1e-2, 1e-3, 1e-4, 1e-5]:
    T0 = np.arctan(r0/h)
    TH = T0*th; WTH = T0*wth
    tau = h*np.tan(TH)                     # t - gam
    sp = (-0.5+h) + 1j*(gam + tau)         # s' on probe line
    FW = np.sqrt(2)*(Gfun(sp - s1) + Gcfun(sp - np.conj(s1)))
    I = np.sum(np.abs(FW)**2 * h/np.cos(TH)**2 * WTH)
    pred = (2*abs(c_p)**2/np.pi)*(2/h)*np.arctan(r0/h)
    print("  h=%-7g I/pred = %.5f   h*I = %.5f (2|c_p|^2=%.5f)" % (h, I/pred, h*I, 2*abs(c_p)**2))
