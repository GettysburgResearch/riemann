import numpy as np, math

N = 2**21  # sieve limit for prefix arrays (2^21 ~ 2.1e6); rows up to n<=3000 need prefix up to 8n
LIM = 60000  # prefix arrays up to LIM cover rows n<=7500 (need 8n for Delta_4 gate)

# Lambda sieve
lam = np.zeros(LIM+1)
is_comp = np.zeros(LIM+1, bool)
for p in range(2, LIM+1):
    if not is_comp[p]:
        for q in range(2*p, LIM+1, p): is_comp[q] = True
        pk = p
        while pk <= LIM:
            lam[pk] = math.log(p); pk *= p
lam_odd = lam.copy();
for r in range(1, 22):
    if 2**r <= LIM: lam_odd[2**r] = 0.0

psi = np.cumsum(lam)          # psi[x] = psi(x)
psi_odd = np.cumsum(lam_odd)

# g(m) = log oddpart(m); F, G prefixes
m = np.arange(LIM+1); v2 = np.zeros(LIM+1, int)
mm = m.copy();
for r in range(1, 22):
    v2[(m % 2**r == 0) & (m>0)] = r
oddpart = m // (2**v2.clip(0))
g = np.zeros(LIM+1); g[1:] = np.log(oddpart[1:])
F = np.cumsum(g); G = np.cumsum(g*g)

def C2(x): return 0 if x < 1 else 1 + int(math.floor(math.log2(x)))
def Y(n,j): return C2(n)-C2(j)-C2(n-j)
def O_(n,j): return F[n]-F[j]-F[n-j]
def S_(n,j): return G[n]-G[j]-G[n-j]
def R_(n,j): return O_(n,j)**2 - S_(n,j)
def D2R(n,j): return R_(2*n,2*j)-4*R_(n,j)
def D4R(n,j): return R_(4*n,4*j)-16*R_(n,j)
def I2(n,j): return psi_odd[2*n]-psi_odd[2*j]-psi_odd[2*(n-j)]  # T1c closed form
def Qc4(n,j):  # O-90011.2
    k=n-j
    return (psi[4*n]-psi[4*j]-psi[4*k]) - 4*(psi[n]-psi[j]-psi[k]) - 4*math.log(4)

# --- 1. verify I_2 closed form against DIRECT carry-sum definition ---
def mu_sieve(N):
    mu = np.ones(N+1, int); prim=np.ones(N+1,bool); prim[:2]=False
    for p in range(2,N+1):
        if prim[p]:
            prim[2*p::p]=False
            mu[p::p]*= -1
            mu[p*p::p*p] = 0
    return mu
MU = mu_sieve(LIM)
def q_odd(d):
    if d%2==0: return 0.0
    return -MU[d]*math.log(d) if d>1 else 0.0
def chi(n,d,j): return n//d - j//d - (n-j)//d
def Q_direct(n,j):
    return sum(q_odd(d)*chi(n,d,j) for d in range(3,n+1,2))
err1 = 0.0
import random; random.seed(7)
for _ in range(40):
    n = random.randint(8, 700); j = random.randint(1, n-1)
    direct = Q_direct(2*n,2*j) - Q_direct(n,j)
    err1 = max(err1, abs(direct - I2(n,j)))
# T1b psi-form reconciliation
err1b = 0.0
for _ in range(40):
    n = random.randint(8, 700); j = random.randint(1, n-1); k=n-j
    t1b = (psi[2*n]-psi[2*j]-psi[2*k]) - math.log(2)*Y(n,j)
    err1b = max(err1b, abs(t1b - I2(n,j)))
print("I2 closed-form vs direct carry-sum, max err:", err1)
print("T1b psi-form vs T1c psi_odd-form,  max err:", err1b)
print("Y(10,3) =", Y(10,3), " Y(2e)-[Y(e)-1] checks:", all(Y(2*n,2*j)==Y(n,j)-1 for n in range(4,60) for j in range(1,n)))
print("Y on diagonal (2m,m), m=64,1024:", Y(128,64), Y(2048,1024), " (claims of bounded Y on cone -> FALSE, = -log2 m)")

# --- 2. Selberg seam S = L_e(C_odd) vs G-3pt (direct conv) ---
def C_odd_arr(N):
    c = np.zeros(N+1)
    for a in range(1,N+1):
        if lam_odd[a]>0:
            c[a] += lam_odd[a]*math.log(a)
            for b in range(1, N//a+1):
                if lam_odd[b]>0:
                    if a*b<=N: c[a*b]+=lam_odd[a]*lam_odd[b]
    return c
CO = C_odd_arr(3000)
def S_direct(n,j): return sum(CO[d]*chi(n,d,j) for d in range(2,n+1))
err2 = max(abs(S_direct(n,j)-S_(n,j)) for n in (50,97,128,300) for j in range(1,n,7))
print("Selberg seam max err:", err2)

# --- 3. ratio scans ---
best2=(0,0,0); best2_20=(0,0,0); best4=(0,0,0)
dyadic={}
for n in range(8, 4000):
    lo, hi = (n+3)//4, (3*n)//4
    for j in range(lo, hi+1):
        d2 = D2R(n,j)
        if d2<=0: print("NONPOS D2R at",n,j); continue
        r = I2(n,j)**2/d2
        if r>best2[0]: best2=(r,n,j)
        if n>=20 and r>best2_20[0]: best2_20=(r,n,j)
        b = int(math.log2(n)); dyadic[b]=max(dyadic.get(b,0),r)
        if n<=1500:
            d4 = D4R(n,j)
            r4 = Qc4(n,j)**2/d4
            if r4>best4[0]: best4=(r4,n,j)
print("max |I2|^2/D2R (n>=8):", best2, " (n>=20):", best2_20)
print("ratio at (16,8):", I2(16,8)**2/D2R(16,8), "  at (31,11):", I2(31,11)**2/D2R(31,11))
print("max Qc4^2/D4R n<=1500:", best4, " at (31,15):", Qc4(31,15)**2/D4R(31,15), "(31,16):", Qc4(31,16)**2/D4R(31,16))
print("dyadic block maxima:", {k:round(v,3) for k,v in sorted(dyadic.items())})

# --- 4. reserve leading constant at j=n/2: compare 4H vs 6H+carry ---
H = math.log(2)
print("\nD2R/(n ln n) at j=n/2 with prediction 6H + 4ln2*v2*H/ln n  (4H=%.3f, 6H=%.3f):"%(4*H,6*H))
for n in (256, 1000, 4096, 10000, 14000):
    j=n//2; v=v2[math.comb(n,j)%2**60] if False else None
    # v2 of binom via s2
    s2=lambda x: bin(x).count('1'); vv = s2(j)+s2(n-j)-s2(n)
    pred = 6*H + 4*math.log(2)*vv*H/math.log(n)
    print(f"  n={n}: D2R/(n ln n)={D2R(n,j)/(n*math.log(n)):.3f}  v2={vv} pred={pred:.3f}")

# --- 5. chain recurrence L-90010.36 spot check r=3,4 ---
def psi_star(x):
    t=0.0; a=0
    while x>>a >= 1: t += psi_odd[x>>a] if x>>a<=LIM else None; a+=1
    return t
def Q_(n,j): return psi_star(n)-psi_star(j)-psi_star(n-j)
def qc_direct(n,j):
    # q_circ = coefficients of B_circ'; use 1*q_circ = Lambda -4 delta_4*Lambda + 4log4 delta_4 prefix law
    Cq = lambda x: psi[x] - 4*psi[x//4] + 4*math.log(4)*(x//4 >= 1)*C4(x)
    return None
def C4(x): return 0 if x<1 else 1+int(math.floor(math.log(x,4))) if x>=1 else 0
def Qc_row(n,j):
    k=n-j
    Cq = lambda x: psi[x] - 4*psi[x//4] + 4*math.log(4)*(C4(x)-1 if x>=1 else 0)
    # careful: prefix of delta_4*Lambda at x = psi(x/4); prefix of (1*)(4log4 delta_4) sum_{m<=x} coeff: delta_4 means at 4^1? B_circ: 1-4^{1-s} -> 1*q_circ = Lambda - 4 delta_4*Lambda + 4 log4 delta_4 where delta_4 = indicator of m=4
    Cq = lambda x: psi[x] - 4*psi[x//4] + 4*math.log(4)*(1 if x>=4 else 0)
    return Cq(n)-Cq(j)-Cq(k)
ok36=[]
for (n0,j0) in [(5,2),(7,3),(9,4),(11,5)]:
    for r in (3,4):
        n,j = (2**r)*n0, (2**r)*j0
        lhs = Qc_row(n,j)
        Ir  = Q_(n,j)-Q_(n//2,j//2)
        Ir2 = Q_(n//4,j//4)-Q_(n//8,j//8)
        rhs = Ir - 4*Ir2 - math.log(2)*(3*Y(n,j)+19)
        ok36.append(abs(lhs-rhs))
print("\nL-90010.36 recurrence max err (r=3,4, four chains):", max(ok36))
print("Qc_row(4e) vs O-90011.2 form err:", max(abs(Qc_row(4*n,4*j)-Qc4(n,j)) for n in (31,50,97) for j in range(1,n,5)))
