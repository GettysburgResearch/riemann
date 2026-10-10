import numpy as np
from math import log, floor, lgamma
from sympy import mobius, factorint

NMAX = 4100  # supports rows up to n=1000 with 4e = 4000, plus chain checks

# --- basic arithmetic arrays ---
mu = np.zeros(NMAX+1, dtype=np.int64)
for n in range(1, NMAX+1):
    mu[n] = int(mobius(n))
Lam = np.zeros(NMAX+1)          # von Mangoldt
Lam_odd = np.zeros(NMAX+1)
for p in range(2, NMAX+1):
    # prime powers
    pass
def is_prime(n):
    if n < 2: return False
    i = 2
    while i*i <= n:
        if n % i == 0: return False
        i += 1
    return True
primes = [p for p in range(2, NMAX+1) if is_prime(p)]
for p in primes:
    pk = p
    while pk <= NMAX:
        Lam[pk] = log(p)
        if p != 2: Lam_odd[pk] = log(p)
        pk *= p

def v2(n):
    v = 0
    while n % 2 == 0:
        n //= 2; v += 1
    return v

# chi_{n,d}(j)
def chi(n, d, j):
    return n//d - j//d - (n-j)//d

def Lrow(f, n, j):
    return sum(f[d]*chi(n,d,j) for d in range(2, n+1) if f[d] != 0.0)

# --- 1. Y_odd checks ---
def C2(x):
    if x < 1: return 0
    return 1 + floor(np.log2(x)+1e-12)
def Y_odd_formula(n, j): return C2(n)-C2(j)-C2(n-j)
b_odd = np.array([0.0]*(NMAX+1))
for n in range(1, NMAX+1):
    if n % 2 == 1: b_odd[n] = mu[n]
# row of b_odd via carry transform
def Y_odd_row(n, j): return Lrow(b_odd, n, j)
print("Y_odd(10,3): formula", Y_odd_formula(10,3), " row", Y_odd_row(10,3),
      " old-claim sum chi_{10,2^r}(3):", chi(10,2,3)+chi(10,4,3)+chi(10,8,3))
bad = [(n,j) for n in range(3,200) for j in range(1,n) if abs(Y_odd_formula(n,j)-Y_odd_row(n,j))>1e-9]
print("Y_odd formula==row mismatches (n<200):", len(bad))
# scaling law
sc = [(n,j) for n in range(3,150) for j in range(1,n) if Y_odd_formula(2*n,2*j) != Y_odd_formula(n,j)-1]
print("Y(2e)=Y(e)-1 violations:", len(sc))
# mu row = -1
muarr = mu.astype(float)
mrow = [(n,j) for n in range(3,150) for j in range(1,n) if abs(Lrow(muarr,n,j)+1)>1e-9]
print("L_e(mu)=-1 violations:", len(mrow))

# --- 2. S_odd two definitions agree? ---
C_odd_seq = np.zeros(NMAX+1)
for d in range(2, NMAX+1):
    C_odd_seq[d] = Lam_odd[d]*log(d)
# Lam_odd * Lam_odd
supp = [d for d in range(2,NMAX+1) if Lam_odd[d]>0]
for a in supp:
    for b in supp:
        if a*b <= NMAX: C_odd_seq[a*b] += Lam_odd[a]*Lam_odd[b]
g = np.zeros(NMAX+1)
for n in range(1,NMAX+1): g[n] = log(n) - v2(n)*log(2)
Gpref = np.cumsum(g**2)  # Gpref[x] = sum_{m<=x} g^2 ... careful index
Gp = np.zeros(NMAX+1); Gp[1:] = np.cumsum((g**2)[1:])
def S_prefix(n,j): return Gp[n]-Gp[j]-Gp[n-j]
def S_row(n,j): return Lrow(C_odd_seq,n,j)
errs = max(abs(S_prefix(n,j)-S_row(n,j)) for n in range(3,120) for j in range(1,n))
print("max |S_prefix - S_row| (n<120):", errs)

# --- 3. reserve, innovation, target ratio ---
Fp = np.zeros(NMAX+1); Fp[1:] = np.cumsum(g[1:])
def O_row(n,j): return Fp[n]-Fp[j]-Fp[n-j]
def R_odd(n,j): return O_row(n,j)**2 - S_prefix(n,j)
def D2R(n,j): return R_odd(2*n,2*j) - 4*R_odd(n,j)
q_odd = np.zeros(NMAX+1)
for n in range(1,NMAX+1):
    if n%2==1 and mu[n]!=0: q_odd[n] = -mu[n]*log(n)
# prefix of 1*q_odd for speed: Cq(x) = sum_{m<=x} (1*q_odd)(m) = sum_{d<=x} q_odd(d) floor(x/d)
def Cq(x): return sum(q_odd[d]*(x//d) for d in range(1,x+1) if q_odd[d]!=0)
CqA = np.zeros(NMAX+1)
conv = np.zeros(NMAX+1)
for d in range(1,NMAX+1):
    if q_odd[d]!=0.0:
        conv[d::d] += q_odd[d]
CqA[1:] = np.cumsum(conv[1:])
def Q_odd(n,j): return CqA[n]-CqA[j]-CqA[n-j]
def I2(n,j): return Q_odd(2*n,2*j)-Q_odd(n,j)

best = (0,None)
worst_pos = 0
for n in range(20, 1001):
    for j in range(int(np.ceil(n/4)), n//2+1):
        d = D2R(n,j)
        if d <= 0:
            worst_pos += 1
            continue
        r = I2(n,j)**2/d
        if r > best[0]: best = (r,(n,j))
print("max |I2|^2/D2R on quarter-balanced n<=1000:", round(best[0],4), "at", best[1], "; rows with D2R<=0:", worst_pos)

# E2 identity check
from math import comb
def E2_direct(n,j): return O_row(2*n,2*j)-2*O_row(n,j)
def E2_formula(n,j):
    v = v2(comb(n,j))
    return log(comb(2*n,2*j)) - 2*log(comb(n,j)) + v*log(2)
e2err = max(abs(E2_direct(n,j)-E2_formula(n,j)) for n in range(3,80) for j in range(1,n))
v2err = sum(1 for n in range(3,200) for j in range(1,n) if v2(comb(2*n,2*j))!=v2(comb(n,j)))
print("E2 identity max err:", e2err, "; v2 doubling invariance violations:", v2err)

# D2R = Theta(n log n)? ratios on balanced diag j~n/2
print("D2R/(n log n) at j=floor(n/2):", [round(D2R(n,n//2)/(n*log(n)),3) for n in [50,100,200,400,800,1000,1500,2000]])

# --- 4. Q_circ and the aligned-chain identity ---
psi = np.zeros(NMAX+1); psi[1:] = np.cumsum(Lam[1:])
def Cqc(x):
    v = psi[x] - 4*psi[x//4]
    if x >= 4: v += 4*log(4)
    return v
def Q_circ(n,j): return Cqc(n)-Cqc(j)-Cqc(n-j)
# independent def via b_circ = mu - 4 delta_4 * mu ; q_circ = -b_circ log
b_circ = np.zeros(NMAX+1)
for n in range(1,NMAX+1):
    b_circ[n] += mu[n]
    if n % 4 == 0: b_circ[n] -= 4*mu[n//4]
qc2 = np.zeros(NMAX+1)
for n in range(2,NMAX+1): qc2[n] = -b_circ[n]*log(n)
conv2 = np.zeros(NMAX+1)
for d in range(2,NMAX+1):
    if qc2[d]!=0.0: conv2[d::d] += qc2[d]
Cqc2 = np.zeros(NMAX+1); Cqc2[1:] = np.cumsum(conv2[1:])
def Q_circ2(n,j): return Cqc2[n]-Cqc2[j]-Cqc2[n-j]
qq = max(abs(Q_circ(n,j)-Q_circ2(n,j)) for n in range(3,150) for j in range(1,n))
print("Q_circ two-defs max err (n<150):", qq)

# chain identity: e_r=(2^r n, 2^r j), Q_o(e_r) = I_r - 4 I_{r-2} - log2*(3 Y_r + 19), r>=3
def chain_check(n0, j0, rmax):
    out = []
    for r in range(3, rmax+1):
        n, j = (2**r)*n0, (2**r)*j0
        if n > NMAX: break
        Qr  = Q_odd(n, j)
        Qr1 = Q_odd(n//2, j//2)
        Qr2 = Q_odd(n//4, j//4)
        Qr3 = Q_odd(n//8, j//8)
        Ir  = Qr - Qr1
        Ir2 = Qr2 - Qr3
        Yr  = Y_odd_formula(n, j)
        rhs = Ir - 4*Ir2 - log(2)*(3*Yr + 19)
        lhs = Q_circ(n, j)
        out.append(abs(lhs-rhs))
    return max(out) if out else None
print("chain identity max errs:", [chain_check(n0,j0,9) for (n0,j0) in [(3,1),(5,2),(7,3),(11,5),(25,12)]])

# --- 5. O-90011 gate ratio ---
def D4R(n,j): return R_odd(4*n,4*j)-16*R_odd(n,j)
best4 = (0,None)
for n in range(20, 1001):
    for j in range(int(np.ceil(n/4)), 3*n//4+1):
        d = D4R(n,j)
        if d<=0: continue
        r = Q_circ(4*n,4*j)**2/d
        if r>best4[0]: best4=(r,(n,j))
print("max |Qcirc(4e)|^2/D4R_odd quarter-balanced n<=1000:", round(best4[0],4), "at", best4[1])
# L-90010.19 identity
id19 = max(abs(D4R(n,j)-(D2R(2*n,2*j)+4*D2R(n,j))) for n in range(10,200) for j in range(1,n))
print("D4R = D2R(2e)+4 D2R(e) max err:", id19)
