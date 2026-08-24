import numpy as np
import mpmath as mp
mp.mp.dps = 25

# G(sbar, s) = sum_{j>=2} j^{-sbar} E_j(s)/(j(j-1)),
# E_j(s) = -2 sum_{d=1}^{j-1} d^{-s} + (j+2)(j-1) j^{-s} - j(j-1)(j+1)^{-s}
def E(j, s):
    return -2*sum(mp.power(d, -s) for d in range(1, j)) + (j+2)*(j-1)*mp.power(j, -s) - j*(j-1)*mp.power(j+1, -s)

def G(sb, s, J=4000):
    # E_j(s) = -2 Z_{j-1}(s) + ..., accumulate partial zeta sum incrementally
    tot = mp.mpc(0); Z = mp.mpc(0)  # Z = sum_{d=1}^{j-1} d^{-s}
    for j in range(2, J+1):
        Z += mp.power(j-1, -s)
        Ej = -2*Z + (j+2)*(j-1)*mp.power(j, -s) - j*(j-1)*mp.power(j+1, -s)
        tot += mp.power(j, -sb) * Ej / (j*(j-1))
    return tot

# sanity: E_2, E_3 match L-32701
s = mp.mpc(0.7, 2.3)
print("E2 check:", E(2, s) - (-2 + 4*2**-s - 2*3**-s))
print("E3 check:", E(3, s) - (-2 - 2*2**-s + 10*3**-s - 6*4**-s))

# zero-response at first three zeta zeros: residue coefficient r = G(rho_bar, rho)/zeta'(rho)
for k in [1, 2, 3]:
    rho = mp.zetazero(k)
    g1 = G(mp.conj(rho), rho, 4000); g2 = G(mp.conj(rho), rho, 8000)
    r = g2 / mp.zeta(rho, derivative=1)
    print(f"rho_{k}: G(rho_bar,rho) = {mp.nstr(g2,8)} (tail drift {mp.nstr(abs(g2-g1),2)}), residue coeff = {mp.nstr(r,6)}, |r| = {mp.nstr(abs(r),6)}")

# validate response formula: finite form x* K x vs Phi(s) = G/zeta + 2*sum j^{-sbar}/(j(j-1)) at s = 1.2+3i
def build_B(T):
    idx = np.arange(2, T+1)
    B = np.zeros((T-1, T-1))
    for i, n in enumerate(idx):
        q = idx[:i+1]
        B[i, :i+1] = (n // q) * (q - 1 - (n % q)) / (n + 1)
    return B

s = mp.mpc(1.2, 3.0); sb = mp.conj(s)
elem = sum(mp.power(j, -sb)/(j*(j-1)) for j in range(2, 20000))
Phi = G(sb, s, 8000)/mp.zeta(s) + 2*elem
print("\npredicted Phi(1.2+3i) =", mp.nstr(Phi, 8))
for T in [200, 500, 1000, 2000]:
    B = build_B(T)
    K = np.linalg.inv(B.T)
    q = np.arange(2, T+1, dtype=float)
    x = q**(-complex(1.2, 3.0))
    val = np.conj(x) @ (K @ x)
    print(f"  T={T:5d}: x*Kx = {val:.6f}")

# explicit witness certificate: hat function around 0.30T, true matrix
print("\nexplicit hat witness f_n = max(0, 1-|n-0.3T|/(0.12T)):")
for T in [64, 128, 256, 512, 1024, 2048]:
    B = build_B(T)
    n = np.arange(2, T+1, dtype=float)
    f = np.maximum(0, 1 - np.abs(n - 0.3*T)/(0.12*T))
    val = f @ (B @ f)  # = f^T sym(B) f
    print(f"  T={T:5d}: f^T B f = {val:+.4f}   (per T^2: {val/T**2:+.6f}) ||f||^2={f@f:.1f}  ratio val/||f||^2 = {val/(f@f):+.4f}")
