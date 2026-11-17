# Check A-F Lemma 2.1 (Poisson-Gabor identity): sum_k phihat(z-a_k) phihat(z'-a_k) = L * (phi^2)^(z-z'), a_k = T + 2 pi k / L
import mpmath as mp
mp.mp.dps = 30
L = mp.mpf(6); T = mp.mpf('3.7'); h = 2*mp.pi/L
def S(x, a):  # int_{-L/2}^{L/2} e^{-i u x} ... helper: 2 sin(xL/2)/x
    return L if abs(x) < mp.mpf('1e-25') else 2*mp.sin(x*L/2)/x
def phihat(xi):   # phi(u) = cos^2(pi u / L) on [-L/2, L/2]
    w = 2*mp.pi/L
    return S(xi,0)/2 + (S(xi-w,0) + S(xi+w,0))/4
def phi2hat(z):
    return mp.quad(lambda u: mp.cos(mp.pi*u/L)**4*mp.exp(-1j*u*z), [-L/2, 0, L/2])
for (z, zp) in ((mp.mpc(4.1, 0.3), mp.mpc(5.3, -0.2)), (mp.mpc(2.0, 0.45), mp.mpc(2.0, -0.45)), (mp.mpc(7.7,0), mp.mpc(7.7,0))):
    M = 4000
    lhs = mp.fsum(phihat(z - (T + k*h))*phihat(zp - (T + k*h)) for k in range(-M, M+1))
    rhs = L*phi2hat(z - zp)
    print("z=",z," z'=",zp," lhs=", mp.nstr(lhs,12), " rhs=", mp.nstr(rhs,12), " |diff|=", mp.nstr(abs(lhs-rhs),3))
