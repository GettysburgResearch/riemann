#!/usr/bin/env python3
"""T1b steps 3-4: ratio scans via I_2 = E(2n)-E(2j)-E(2k) - log2*Y_odd, and zero injection."""
import numpy as np, math, sys

NMAX = 1_000_000          # rows up to n = 1e6, sieve to 2e6
S = 2*NMAX

# --- linear sieve for Lambda via smallest prime factor exponent trick ---
lam = np.zeros(S+1)
spf = np.zeros(S+1, dtype=np.int32)
for p in range(2, S+1):
    if spf[p] == 0:
        spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
print("spf done", flush=True)
# lam[q]=log p iff q=p^k
for p in range(2, S+1):
    if spf[p] == p:
        lp = math.log(p)
        q = p
        while q <= S:
            lam[q] = lp
            q *= p
print("lam done", flush=True)
psi = np.cumsum(lam)
x = np.arange(S+1, dtype=np.float64)
E = psi - x; E[0] = 0.0

# F,G for R_odd: g(m) = log(odd(m)) = log m - v2(m) log2
v2 = np.zeros(S+1, dtype=np.int64)
m = np.arange(S+1)
mm = m.copy()
while True:
    even = (mm > 0) & (mm % 2 == 0)
    if not even.any(): break
    v2[even] += 1
    mm[even] //= 2
g = np.zeros(S+1)
g[1:] = np.log(m[1:]) - v2[1:]*math.log(2)
F = np.cumsum(g)
G = np.cumsum(g*g)
print("F,G done", flush=True)

log2 = math.log(2)
C2v = np.zeros(S+1, dtype=np.int64)
C2v[1:] = np.floor(np.log2(m[1:])).astype(np.int64) + 1
# fix float edge cases at powers of two
p = 1
while p <= S:
    C2v[p] = int(p).bit_length()
    if p+1 <= S: C2v[p+1] = int(p+1).bit_length()
    if p-1 >= 1: C2v[p-1] = int(p-1).bit_length()
    p *= 2

def scan(nlist, Earr, label):
    """for each n, max over balanced j of ratio; returns global max info"""
    best = (0.0, None)
    hist = []
    for n in nlist:
        lo = (n+3)//4; hi = (3*n)//4
        j = np.arange(lo, hi+1)
        k = n - j
        # I2
        I2 = Earr[2*n] - Earr[2*j] - Earr[2*k] - log2*(C2v[n]-C2v[j]-C2v[k])
        # Delta2 R
        O1 = F[n]-F[j]-F[k]; S1 = G[n]-G[j]-G[k]; R1 = O1*O1-S1
        O2 = F[2*n]-F[2*j]-F[2*k]; S2 = G[2*n]-G[2*j]-G[2*k]; R2 = O2*O2-S2
        D2 = R2 - 4*R1
        if (D2 <= 0).any():
            iz = np.where(D2 <= 0)[0]
            print(f"  [{label}] NONPOSITIVE D2 at n={n} j={j[iz[0]]}")
        ratio = I2*I2/D2
        i = int(np.argmax(ratio))
        if ratio[i] > best[0]:
            best = (float(ratio[i]), (n, int(j[i])))
        hist.append((n, float(ratio[i]), float(D2.min()/(n*math.log(n))), float(np.abs(I2).max())))
    return best, hist

# ---- full scan n<=5000 (reproduce claim), then n<=20000 ----
b1, _ = scan(range(8, 5001), E, "n<=5000")
print("max ratio n<=5000:", b1, flush=True)
b2, _ = scan(range(5001, 20001), E, "5000<n<=20000")
print("max ratio 5000<n<=20000:", b2, flush=True)

# ---- geometric sample up to 1e6, all balanced j each ----
ns = sorted(set(int(round(1.05**t)) for t in range(int(math.log(20000)/math.log(1.05)), int(math.log(NMAX)/math.log(1.05))+1)))
ns = [n for n in ns if 20000 < n <= NMAX]
b3, hist3 = scan(ns, E, "sampled<=1e6")
print("max ratio sampled 2e4..1e6:", b3, flush=True)
print("sampled trajectory (n, max_ratio, min D2/(n ln n), max|I2|):")
for h in hist3[::6]: print("   ", h)

# ---- decade trend of max ratio ----
print("decade maxima:")
for a, b in [(8,100),(100,1000),(1000,5000),(5000,20000)]:
    bb, _ = scan(range(a, b+1), E, "dec")
    print(f"   n in [{a},{b}]: {bb}")

# ---- zero injection: E_inj = E + A*x^beta*cos(gamma log x - phase) ----
def inject(beta, gamma, A):
    xs = x.copy(); xs[0] = 1
    return E + A*np.power(xs, beta)*np.cos(gamma*np.log(xs))

for (beta, gamma, A, lab) in [(0.5, 14.134725, 1.0, "on-line beta=1/2 (RH-true type)"),
                              (0.65, 14.134725, 1.0, "OFF-LINE beta=0.65"),
                              (0.6, 100.0, 1.0, "OFF-LINE beta=0.60 high gamma")]:
    Ei = inject(beta, gamma, A)
    bi, hi = scan(ns[::3], Ei, lab)
    traj = [(h[0], round(h[1],3)) for h in hi[::8]]
    print(f"injection {lab}: max ratio {bi}")
    print("   trajectory:", traj, flush=True)
