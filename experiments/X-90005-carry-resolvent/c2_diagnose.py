import numpy as np

def build_B(T):
    idx = np.arange(2, T+1)
    B = np.zeros((T-1, T-1))
    for i, n in enumerate(idx):
        q = idx[:i+1]
        B[i, :i+1] = (n // q) * (q - 1 - (n % q)) / (n + 1)
    return B

def build_ratio(T):
    # deterministic ratio-kernel model g(n/q) = floor(u)(1-{u})/u, u=n/q
    idx = np.arange(2, T+1)
    B = np.zeros((T-1, T-1))
    for i, n in enumerate(idx):
        q = idx[:i+1]
        u = n / q
        fl = np.floor(u)
        B[i, :i+1] = fl * (1 - (u - fl)) / u
    return B

def build_cont(T):
    # continuous sawtooth-free comparison: replace floor(u)(1-{u})/u by its local mean 1 - 1/(2? ) :
    # E_u over unit cell of g: for u in [k,k+1): mean_u g = k*mean(1-{u})/u ~ ... use g_smooth(u)= (u - 1/2)/u? crude: 1/2*(1+1/u)?
    # honest smooth comparison: g_s(u) = integral over cell = k/u*(1/2) *? just use 0.5*(1+ (2-u) if u<2)  -- skip; use midpoint average of jumps:
    idx = np.arange(2, T+1)
    B = np.zeros((T-1, T-1))
    for i, n in enumerate(idx):
        q = idx[:i+1]
        u = n / q
        B[i, :i+1] = (u - 0.5) / u * 0.5 + 0.25  # placeholder smooth ~0.5
        B[i, i] = 1.0
    return B

print("ratio-kernel model g(n/q) (deterministic, no 1/(n+1) subtleties, no mu):")
for T in [8, 10, 12, 16, 32, 64, 256, 1024]:
    S = build_ratio(T); S = (S + S.T) / 2
    ev = np.linalg.eigvalsh(S)
    print(f"  T={T:5d} min eig={ev[0]:+.5f}  (per T: {ev[0]/T:+.5f})")

print("\ntrue matrix vs ratio model, eigvec localization at T=512:")
for name, M in [("true", build_B(512)), ("ratio", build_ratio(512))]:
    w, V = np.linalg.eigh((M + M.T) / 2)
    v = V[:, 0]; n = np.arange(2, 513)
    c = int(n[np.argmax(np.abs(v))])
    print(f"  {name}: min eig {w[0]:+.4f}, |v| peak at n={c}, mass in n<T/2: {np.sum(v[:255]**2):.3f}")

# diagonal scaling rescue attempt on true matrix, T=64: D = n^a
print("\nscaling rescue D=n^a, true T=64:")
B = build_B(64); n = np.arange(2, 65.0)
for a in [-1.0, -0.5, -0.25, 0, 0.25, 0.5, 1.0]:
    d = n**a
    S = (np.outer(d, d) * B); S = (S + S.T) / 2
    # PSD of D B D sym part; use generalized: actually congruence D S D preserves inertia of S only if same D both sides of sym -- here we scale B then symmetrize (different!)
    ev = np.linalg.eigvalsh(S)
    print(f"  a={a:+.2f}: min eig={ev[0]:+.5f}")

# congruence sanity at T=10
B = build_B(10); K = np.linalg.inv(B.T)
print("\nT=10: min eig sym(B)=", np.linalg.eigvalsh((B+B.T)/2)[0], " sym(K)=", np.linalg.eigvalsh((K+K.T)/2)[0])

# principal-submatrix location: smallest leading principal minor failure of sym(B_10)?
S = (B + B.T)/2
for m in range(1, 10):
    ev = np.linalg.eigvalsh(S[:m,:m])
    if ev[0] < 0:
        print(f"first failing leading principal section: size {m} (n=2..{m+1}), min eig {ev[0]:+.5f}")
        break
else:
    print("full T=10 matrix needed for failure (no leading principal section fails)")
