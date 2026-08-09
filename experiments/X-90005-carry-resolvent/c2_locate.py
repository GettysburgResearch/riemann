import numpy as np
from fractions import Fraction

def build_B(T):
    idx = np.arange(2, T+1)
    B = np.zeros((T-1, T-1))
    for i, n in enumerate(idx):
        q = idx[:i+1]
        B[i, :i+1] = (n // q) * (q - 1 - (n % q)) / (n + 1)
    return B

# exact first failing T
prev = None
for T in range(3, 20):
    B = build_B(T)
    ev = np.linalg.eigvalsh((B + B.T) / 2)
    print(f"T={T:3d} min eig={ev[0]:+.8f}")
    if ev[0] < 0 and prev is None:
        prev = T
print("first negative T =", prev)

# eigenvector at first failure and at T=64
for T in [prev, 64, 512]:
    B = build_B(T)
    w, V = np.linalg.eigh((B + B.T) / 2)
    v = V[:, 0]
    n = np.arange(2, T+1)
    # top components
    ordidx = np.argsort(-np.abs(v))[:8]
    print(f"\nT={T}: min eig {w[0]:+.5f}; top |v| at n =", [(int(n[i]), round(float(v[i]),3)) for i in ordidx])
    # correlation with smooth profiles
    for name, f in [("1/sqrt(n)", 1/np.sqrt(n)), ("(-1)^n", (-1.0)**n), ("(-1)^n/sqrt n", (-1.0)**n/np.sqrt(n))]:
        f = f/np.linalg.norm(f)
        print(f"   corr with {name:14s}: {abs(v@f):.3f}")

# smooth (residue-averaged, floor-free) model: bbar = (n/q - 1)*... use k=(n-q/2)/q approx? Use exact expectation over r: E[q-1-r]=(q-1)/2, k ~ n/q
def build_smooth(T):
    idx = np.arange(2, T+1)
    B = np.zeros((T-1, T-1))
    for i, n in enumerate(idx):
        q = idx[:i+1].astype(float)
        B[i, :i+1] = (n/q) * (q-1)/2 / (n+1)
        B[i, i] = (n-1)/(n+1)   # keep exact diagonal
    return B

print("\nsmooth (floor-free, residue-averaged) model:")
for T in [12, 64, 256, 1024]:
    ev = np.linalg.eigvalsh((build_smooth(T)+build_smooth(T).T)/2)
    print(f"T={T:5d} min eig smooth={ev[0]:+.5f}")

# scaling law of true min eig
for T in [256, 512, 1024, 2048]:
    ev = np.linalg.eigvalsh((build_B(T)+build_B(T).T)/2)
    print(f"T={T:5d} mineig/T = {ev[0]/T:+.6f}")
