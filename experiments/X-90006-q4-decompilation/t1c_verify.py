import numpy as np, math

N = 40001  # arrays up to 4*n for small chain checks; main scan uses 2*nmax
NM = 20000 # max n for identity spot checks

# --- sieve Lambda, Lambda_odd, mu ---
def sieve(N):
    lam = np.zeros(N); lam_odd = np.zeros(N)
    mu = np.ones(N, dtype=np.int64)
    primes = []
    is_c = np.zeros(N, dtype=bool)
    for p in range(2, N):
        if not is_c[p]:
            primes.append(p)
            lp = math.log(p)
            q = p
            while q < N:
                lam[q] = lp
                if p != 2: lam_odd[q] = lp
                q *= p
            is_c[p*p::p] = True
    # mobius
    mu = np.ones(N, dtype=np.int64)
    pr = np.array(primes)
    mmu = np.ones(N, dtype=np.int64)
    for p in primes:
        mmu[p::p] *= -1
        if p*p < N: mmu[p*p::p*p] = 0
    mmu[0] = 0
    return lam, lam_odd, mmu, primes

lam, lam_odd, mu, primes = sieve(N)

# g(m) = log odd(m) ; prefix F, G ; psi_odd prefix ; psi prefix ; psi_* prefix
oddpart = np.arange(N)
op = oddpart.copy()
while True:
    ev = (op % 2 == 0) & (op > 0)
    if not ev.any(): break
    op[ev] //= 2
g = np.zeros(N); g[1:] = np.log(op[1:])
F = np.cumsum(g)                    # F(x)=sum_{m<=x} log odd(m)
G = np.cumsum(g*g)                  # G(x)=sum g^2
psi = np.cumsum(lam)                # psi(x)
psi_odd = np.cumsum(lam_odd)        # psi_odd(x)
# psi_*(x) = sum_{a>=0} psi_odd(x/2^a)  (floor)
def psistar(x):
    s = 0.0; a = 0
    while (x >> a) >= 1:
        s += psi_odd[x >> a]; a += 1
    return s
# mu_odd log prefix of L_e: direct T_e sum for verification
def T(n, j, m):
    k = n - j
    return n//m - j//m - k//m

def Q_direct(n, j):
    k = n - j; s = 0.0
    for m in range(3, n+1, 2):
        if mu[m]:
            t = T(n, j, m)
            if t: s -= mu[m]*math.log(m)*t
    return s

def O_row(n, j): return F[n]-F[j]-F[n-j]
def S_row(n, j): return G[n]-G[j]-G[n-j]
def R_row(n, j): return O_row(n,j)**2 - S_row(n,j)

def Q_closed(n, j): return psistar(n)-psistar(j)-psistar(n-j)
def P_row(n, j):    return psi_odd[n]-psi_odd[j]-psi_odd[n-j]  # 3-pt psi_odd at the row itself

# --- 1. verify Q closed form and I_2 closed form ---
import random
random.seed(7)
bad = 0
for _ in range(60):
    n = random.randint(8, 3000); j = random.randint(1, n-1)
    qd = Q_direct(n, j); qc = Q_closed(n, j)
    if abs(qd-qc) > 1e-7: bad += 1; print("Q mismatch", n, j, qd, qc)
    i2c = Q_closed(2*n,2*j) - Q_closed(n,j)
    i2p = P_row(2*n, 2*j)
    if abs(i2c-i2p) > 1e-7: bad += 1; print("I2 mismatch", n, j, i2c, i2p)
print("closed-form checks: failures =", bad)

# --- 2. verify L-90010.15 expansion and Delta2R ---
for (n,j) in [(31,11),(100,37),(555,200)]:
    E2 = O_row(2*n,2*j) - 2*O_row(n,j)
    lhs = R_row(2*n,2*j) - 4*R_row(n,j)
    rhs = E2*(4*O_row(n,j)+E2) - (S_row(2*n,2*j)-4*S_row(n,j))
    v2b = 0  # v2 of binom via Kummer: carries adding j,k base2
    j_,k_,c,cnt = j, n-j, 0, 0
    x,y,carry = j_,k_,0
    while x>0 or y>0 or carry:
        s = (x&1)+(y&1)+carry
        carry = s>>1; cnt += carry; x>>=1; y>>=1
    print(f"L-90010.15 check ({n},{j}): lhs={lhs:.6f} rhs={rhs:.6f} ; E2={E2:.4f} v2binom={cnt}")

# --- 3. Y_odd and the aligned-chain recurrence L-90010.36 ---
def C2(x): return 0 if x < 1 else 1 + int(math.floor(math.log2(x)))
def Y_odd(n, j): return C2(n)-C2(j)-C2(n-j)
print("Y_odd(10,3) =", Y_odd(10,3))
# bare charge check: L_e(b_odd) computed directly
def bare_direct(n, j):
    s = 0
    for m in range(1, n+1, 2):
        if mu[m]: s += mu[m]*T(n,j,m)
    return s
for (n,j) in [(10,3),(31,11),(100,37)]:
    print("bare charge direct vs C2-formula:", (n,j), bare_direct(n,j), Y_odd(n,j))
# mu carry at doubled row = -1
def mu_carry(n, j):
    s = 0
    for m in range(1, n+1):
        if mu[m]: s += mu[m]*T(n,j,m)
    return s
print("L_2e(mu) at (62,22),(200,74):", mu_carry(62,22), mu_carry(200,74))

# Q_circ via O-90011.2 vs chain formula L-90010.36
def Qcirc_row4(n, j):  # Q_circ(4n,4j)
    k = n-j
    return (psi[4*n]-psi[4*j]-psi[4*k]) - 4*(psi[n]-psi[j]-psi[k]) - 4*math.log(4)
# direct coefficient check of q_circ: B_circ = (1-4^{1-s})/zeta ; q_circ = B_circ'
# 1*q_circ <-> zeta*B_circ' ; B_circ' = [(-log4)*(-4^{1-s}... ] do numerically via coefficients:
# b_circ = mu - 4*delta_4*mu (dirichlet), q_circ = -b_circ log
def Qcirc_direct(n, j):
    s = 0.0
    for m in range(2, n+1):
        bm = mu[m] - (4*mu[m//4] if m % 4 == 0 else 0)
        if bm: s -= bm*math.log(m if m%4 else m/4 if False else m)*T(n,j,m)
    return s
# careful: b_circ(m) = mu(m) - 4*mu(m/4) [m div by 4]; q_circ(m) = -b_circ(m) log m
def Qcirc_direct2(n, j):
    s = 0.0
    for m in range(2, n+1):
        bm = mu[m] + (-4*mu[m//4] if m % 4 == 0 else 0)
        if bm: s -= bm*math.log(m)*T(n,j,m)
    return s
for (n,j) in [(20,7),(31,11)]:
    print("Qcirc row4 psi-form vs direct:", Qcirc_row4(n,j), Qcirc_direct2(4*n,4*j))

def chain_check(n, j, r):
    Qs = [Q_closed((2**t)*n, (2**t)*j) for t in range(r+1)]
    I = [None]+[Qs[t]-Qs[t-1] for t in range(1, r+1)]
    Yr = Y_odd((2**r)*n, (2**r)*j)
    rhs = I[r] - 4*I[r-2] - math.log(2)*(3*Yr+19)
    er_n, er_j = (2**r)*n, (2**r)*j
    lhs = Qcirc_direct2(er_n, er_j)
    return lhs, rhs
for (n,j,r) in [(20,7,3),(31,11,3),(13,5,4)]:
    l, rr = chain_check(n,j,r)
    print(f"chain L-90010.36 ({n},{j},r={r}): direct={l:.6f} formula={rr:.6f}")
