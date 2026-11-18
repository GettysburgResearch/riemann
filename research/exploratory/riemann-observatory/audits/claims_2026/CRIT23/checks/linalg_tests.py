# Randomised / adversarial checks of the load-bearing finite inequalities.
import numpy as np
rng = np.random.default_rng(20261117)

def herm(n, cplx=True):
    A = rng.normal(size=(n,n)) + (1j*rng.normal(size=(n,n)) if cplx else 0)
    return (A + A.conj().T)/2

def lemma32_gap(P, Q, r, b):
    S = P + Q
    hs = np.real(np.trace(S @ S.conj().T))
    return r - (2*np.real(np.trace(P)) + 4*np.real(np.trace(Q)) - 4*b - hs)

# (1) Alpoge-Furman Lemma 3.2 (rank-trace)
worst = np.inf
for it in range(20000):
    d = rng.integers(2, 9); r = rng.integers(0, d+1); b = rng.integers(0, d+1)
    X = rng.normal(size=(d, r)) + 1j*rng.normal(size=(d, r)); X *= rng.uniform(0.1, 2)
    P = X @ X.conj().T
    # Q with at most b positive eigenvalues
    U, _ = np.linalg.qr(rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d)))
    ev = -np.abs(rng.normal(size=d))*rng.uniform(0,3)
    pos = rng.choice(d, size=min(b,d), replace=False); ev[pos] = np.abs(rng.normal(size=len(pos)))*rng.uniform(0,4)
    Q = U @ np.diag(ev) @ U.conj().T
    g = lemma32_gap(P, Q, r, b); worst = min(worst, g)
print("Lemma 3.2 random: min slack =", worst, "(must be >= 0)")
# equality case P=Pi1, Q=2 Pi2
d=6; E=np.eye(d); P=E[:, :2]@E[:, :2].T; Q=2*E[:, 2:5]@E[:, 2:5].T
print("Lemma 3.2 equality case slack:", lemma32_gap(P,Q,2,3))

# (2) Knausgard Lemma 2.1: tr A^2 >= 2c trA - 2c trP + tr phi_c(P) - c^2 p
def phi(t, c): return np.where(t <= c, t*t, 2*c*t - c*c)
worst = np.inf
for it in range(20000):
    d = rng.integers(2, 9); r = rng.integers(0, d+1); p = rng.integers(0, d+1); c = rng.uniform(0, 4)
    X = rng.normal(size=(d, r)) + 1j*rng.normal(size=(d, r)); X *= rng.uniform(0.1, 2)
    P = X @ X.conj().T
    U, _ = np.linalg.qr(rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d)))
    ev = -np.abs(rng.normal(size=d))*rng.uniform(0,3)
    pos = rng.choice(d, size=min(p,d), replace=False); ev[pos] = np.abs(rng.normal(size=len(pos)))*rng.uniform(0,4)
    Q = U @ np.diag(ev) @ U.conj().T; A = P + Q
    lhs = np.real(np.trace(A@A)); pe = np.linalg.eigvalsh(P)
    rhs = 2*c*np.real(np.trace(A)) - 2*c*np.real(np.trace(P)) + phi(pe, c).sum() - c*c*p
    worst = min(worst, lhs - rhs)
print("Knausgard Lemma 2.1 random: min slack =", worst)

# (3) Lamzouri Prop 2.1 with flat eta^2 = 1_[-1/2,1/2]: K(xi) = sin(pi xi)/(pi xi) (entire)
def Kf(z):
    z = np.asarray(z, dtype=complex)
    out = np.ones_like(z)
    nz = np.abs(z) > 1e-12
    out[nz] = np.sin(np.pi*z[nz])/(np.pi*z[nz])
    return out
def build(nreal1, nreal2, npairs, spread, depth, mult_hi=3):
    pts=[]; mult=[]
    for x in rng.uniform(0, spread, nreal1): pts.append(complex(x)); mult.append(1)
    for x in rng.uniform(0, spread, nreal2): pts.append(complex(x)); mult.append(int(rng.integers(2, mult_hi+1)))
    for _ in range(npairs):
        x = rng.uniform(0, spread); y = rng.uniform(1e-3, depth); m = int(rng.integers(1, mult_hi+1))
        pts += [complex(x, y), complex(x, -y)]; mult += [m, m]
    return np.array(pts), np.array(mult)
worst = {k: np.inf for k in ("2.4","2.5","2.6","2.7")}; imagmax = 0; negS = 0
for it in range(4000):
    pts, mult = build(rng.integers(0,8), rng.integers(0,4), rng.integers(0,5), rng.uniform(0.5, 10), rng.uniform(0.01, 1.5))
    if len(pts)==0: continue
    D = pts[:,None]-pts[None,:]
    S = (mult[:,None]*mult[None,:]*Kf(D)**2).sum()
    imagmax = max(imagmax, abs(S.imag)/max(1,abs(S))); S = S.real
    if S < -1e-9: negS += 1
    Zc = mult.sum()
    real = np.abs(pts.imag) < 1e-15
    n_simple_real = int(((mult==1)&real).sum())
    n_distinct = len(pts)
    n_simple = int((mult==1).sum()); n_real_mult = int(mult[real].sum())
    n_simple_or_real = int(mult[(mult==1)|real].sum())
    worst["2.4"] = min(worst["2.4"], n_simple_real - (2*Zc - S))
    worst["2.5"] = min(worst["2.5"], n_distinct - (1.5*Zc - 0.5*S))
    worst["2.6"] = min(worst["2.6"], n_simple + n_real_mult - (3*Zc - S))
    A = S/Zc
    if 1 <= A < 2:
        worst["2.7"] = min(worst["2.7"], n_simple_or_real - (5+2*np.sqrt(2)-2*A)/(3+2*np.sqrt(2))*Zc)
print("Lamzouri Prop 2.1 random (flat kernel): min slacks", worst, " max rel imag", imagmax, " #negative S", negS)
