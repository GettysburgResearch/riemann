import numpy as np

def build_B(T):
    # rows n=2..T, cols q=2..n ; beta_{nq} = floor(n/q)(q-1-(n mod q))/(n+1)
    idx = np.arange(2, T+1)
    B = np.zeros((T-1, T-1))
    for i, n in enumerate(idx):
        q = idx[:i+1]
        k = n // q
        r = n % q
        B[i, :i+1] = k * (q - 1 - r) / (n + 1)
    return B

# --- 1. Congruence check + P test: min eig of sym(B_T) and sym(K_T) small T
for T in [4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 768, 1024]:
    B = build_B(T)
    S = (B + B.T) / 2
    ev = np.linalg.eigvalsh(S)
    K = np.linalg.inv(B.T)
    evK = np.linalg.eigvalsh((K + K.T) / 2)
    print(f"T={T:5d}  min eig sym(B)={ev[0]:+.6f}  max={ev[-1]:.3f}   min eig sym(K)={evK[0]:+.6f}")
