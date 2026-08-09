import numpy as np, math

NMAX = 16000
N = 4*NMAX + 8   # need arrays to 4n for Delta_4 crosscheck at small n; 2n for main scan

lam_odd = np.zeros(N)
is_c = np.zeros(N, dtype=bool)
for p in range(2, N):
    if not is_c[p]:
        if p != 2:
            lp = math.log(p); q = p
            while q < N: lam_odd[q] = lp; q *= p
        is_c[p*p::p] = True

op = np.arange(N)
while True:
    ev = (op % 2 == 0) & (op > 0)
    if not ev.any(): break
    op[ev] //= 2
g = np.zeros(N); g[1:] = np.log(op[1:])
F = np.cumsum(g); G = np.cumsum(g*g); PSO = np.cumsum(lam_odd)

def rows(n):
    j = np.arange(max(1,(n+3)//4), (3*n)//4 + 1)   # quarter-balanced cone
    k = n - j
    return j, k

def O_(n,j,k): return F[n]-F[j]-F[k]
def S_(n,j,k): return G[n]-G[j]-G[k]
def R_(n,j,k): return O_(n,j,k)**2 - S_(n,j,k)

best = (0,0,0); block = {}
diag = []
for n in range(20, NMAX+1):
    j,k = rows(n)
    I2 = PSO[2*n]-PSO[2*j]-PSO[2*k]
    d2R = R_(2*n,2*j,2*k) - 4*R_(n,j,k)
    ok = d2R > 0
    ratio = np.where(ok, I2*I2/np.where(ok, d2R, 1), -1)
    i = int(np.argmax(ratio))
    if ratio[i] > best[0]: best = (float(ratio[i]), n, int(j[i]))
    b = int(math.log2(n))
    if b not in block or ratio[i] > block[b][0]: block[b] = (float(ratio[i]), n, int(j[i]))
    if d2R.min() <= 0:
        bad = j[d2R<=0]
        if n > 200: print("NONPOS d2R at n=", n, "j=", bad[:5])
print("max ratio |I2|^2/Delta2R on quarter cone, n<=%d:" % NMAX, best)
print("dyadic-block envelope (log2 n -> max ratio, argmax):")
for b in sorted(block): print("  2^%d: %.4f at %s" % (b, block[b][0], block[b][1:]))

# reported check: n<=5000 max
best5 = (0,0,0)
for n in range(20, 5001):
    j,k = rows(n)
    I2 = PSO[2*n]-PSO[2*j]-PSO[2*k]
    d2R = R_(2*n,2*j,2*k) - 4*R_(n,j,k)
    ratio = I2*I2/d2R
    i = int(np.argmax(ratio))
    if ratio[i] > best5[0]: best5 = (float(ratio[i]), n, int(j[i]))
print("n<=5000 max:", best5, " (reported: 0.392 at (31,11))")

# Delta_4 gate crosscheck vs O-90011 numbers, n<=1200 (arrays allow 4n)
lam = np.zeros(N)
is_c2 = np.zeros(N, dtype=bool)
for p in range(2, N):
    if not is_c2[p]:
        lp = math.log(p); q = p
        while q < N: lam[q] = lp; q *= p
        is_c2[p*p::p] = True
PSI = np.cumsum(lam)
best4 = (0,0,0)
for n in range(20, 1201):
    j,k = rows(n)
    Qc = (PSI[4*n]-PSI[4*j]-PSI[4*k]) - 4*(PSI[n]-PSI[j]-PSI[k]) - 4*math.log(4)
    d4R = R_(4*n,4*j,4*k) - 16*R_(n,j,k)
    ratio = Qc*Qc/d4R
    i = int(np.argmax(ratio))
    if ratio[i] > best4[0]: best4 = (float(ratio[i]), n, int(j[i]))
print("Delta4 gate max, n<=1200:", best4, " (reported 0.53375 at (31,15), n<=5000)")

# typical (median) ratio per block: is it ~ c/log n ?
for b in [7, 9, 11, 13]:
    n = 2**b + 137
    j,k = rows(n)
    I2 = PSO[2*n]-PSO[2*j]-PSO[2*k]
    d2R = R_(2*n,2*j,2*k)-4*R_(n,j,k)
    r = I2*I2/d2R
    print("n=%d median ratio=%.5f mean=%.5f  1/log n=%.5f" % (n, float(np.median(r)), float(np.mean(r)), 1/math.log(n)))

# diagonal D(x) = psi_odd(2x)-2psi_odd(x): sqrt-normalized growth
print("diagonal D(x)/sqrt(2x) and /sqrt(2x log 2x):")
for x in [10**3, 10**4, 3*10**4, NMAX*2 - 5]:
    D = PSO[2*x]-2*PSO[x]
    print("  x=%6d D=%9.3f  D/sqrt(2x)=%7.3f  D^2/(2x log 2x)=%.4f" % (x, D, D/math.sqrt(2*x), D*D/(2*x*math.log(2*x))))
xs = np.arange(100, 2*NMAX//1)
Dv = PSO[2*xs]-2*PSO[xs]
z = Dv/np.sqrt(2*xs)
print("max |D|/sqrt(2x) over x in [100,%d]: %.4f at x=%d" % (2*NMAX-1, float(np.abs(z).max()), int(xs[np.abs(z).argmax()])))
