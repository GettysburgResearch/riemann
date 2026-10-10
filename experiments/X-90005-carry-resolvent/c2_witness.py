import numpy as np

def build_B(T):
    idx = np.arange(2, T+1)
    B = np.zeros((T-1, T-1))
    for i, n in enumerate(idx):
        q = idx[:i+1]
        B[i, :i+1] = (n // q) * (q - 1 - (n % q)) / (n + 1)
    return B

T0 = 512
B = build_B(T0)
w, V = np.linalg.eigh((B + B.T)/2)
v = V[:, 0]
n = np.arange(2, T0+1)
# characterize: sign changes, where positive/negative mass sits
sc = np.sum(np.diff(np.sign(v)) != 0)
print(f"T={T0} min-eigvec: {sc} sign changes; v[n=2..8] =", np.round(v[:7], 3))
# mass by dyadic band of x=n/T
for lo, hi in [(0, .125), (.125, .25), (.25, .375), (.375, .5), (.5, .75), (.75, 1.0)]:
    m = (n >= lo*T0) & (n < hi*T0)
    print(f"  x in [{lo},{hi}): mass {np.sum(v[m]**2):.3f}, mean sign {np.sign(np.sum(v[m])):+.0f}")
# is it orthogonal to smooth positives? correlation with constant, and with sawtooth {T/n}?
for name, f in [("const", np.ones_like(v)), ("frac(T0/n)-.5", (T0/n)%1 - .5), ("frac(n*phi)", (n*0.618034)%1 - .5)]:
    f = f/np.linalg.norm(f)
    print(f"  corr with {name}: {v@f:+.3f}")

# transferable witness: freeze profile x -> v(x), x=n/T0, interpolate at other T
from numpy import interp
x0 = n / T0
for T in [256, 512, 1024, 2048, 3072]:
    Bt = build_B(T)
    nn = np.arange(2, T+1)
    f = interp(nn/T, x0, v, left=0, right=0)
    val = f @ (Bt @ f); nrm = f @ f
    print(f"T={T:5d}: frozen-profile witness  f^T B f = {val:+.3f}, per ||f||^2 = {val/nrm:+.4f}")
