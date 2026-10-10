uHome = "/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad/GRAND/progA2/laneM"
import numpy as np, math, json
h2 = math.log(2); s2 = math.sqrt(2)
def R(v):
    v = abs(v)
    if v <= h2: return 3*h2-(3+s2)*v
    if v <= 2*h2: return -s2*(2*h2-v)
    return 0.0

def build(N):
    spf = np.zeros(N+1, dtype=np.int64)
    for i in range(2, int(N**0.5)+1):
        if spf[i] == 0:
            sl = spf[i*i::i]; sl[sl == 0] = i
    eta = np.zeros(N+1); mu = np.zeros(N+1, dtype=np.int64)
    eta[1] = 1.0; mu[1] = 1
    ek = [1.0]
    for k in range(1, 40): ek.append(ek[-1]*(2*k-1)/(2.0*k))
    for n in range(2, N+1):
        p = spf[n] if spf[n] else n
        m, a = n, 0
        while m % p == 0: m //= p; a += 1
        eta[n] = eta[m]*ek[a]
        mu[n] = 0 if a > 1 else -mu[m]
    return eta, mu

def hU(N, U):
    eta, mu = build(N)
    h = np.zeros(N+1)
    for d in range(U+1, N+1):
        if mu[d]:
            for e in range(1, N//d+1):
                h[d*e] += mu[d]*eta[e]
    return h

def Ah(h, N, a, b):  # sum_q h(qa)h(qb)/q over qa,qb <= N
    Qm = N//max(a, b)
    q = np.arange(1, Qm+1)
    return float(np.sum(h[q*a]*h[q*b]/q))

cases = [(10**3, 10), (10**4, 21), (10**5, 46), (10**6, 100)]
pairs = [(2,1),(3,1),(3,2),(4,1),(4,3),(5,2),(8,3),(9,2),(6,1),(12,7)]
rho1 = {"2,1": -0.41292, "3,1": -0.44063, "3,2": 0.18195, "4,1": -0.09550,
        "4,3": 0.04208, "5,2": 0.19146, "8,3": 0.02015, "9,2": 0.04336,
        "6,1": 0.18195, "12,7": -0.01994}
import math as m
out = {}
for X, U in cases:
    N = X//U
    h = hU(N, U)
    A11 = float(np.sum(h[1:]**2/np.arange(1, N+1)))
    D = 3*h2*A11
    print(f"\nX={X:.0e} U={U} N={N}  D={D:.4f}  A11_h={A11:.4f}")
    row = {"D": D, "A11": A11, "ratios": {}}
    print("  skeleton  Ah/A11    rho(1)_g")
    for (a, b) in pairs:
        r = Ah(h, N, a, b)/A11
        row["ratios"][f"{a},{b}"] = r
        print(f"  ({a:2d},{b:2d})  {r:+.4f}   {rho1[f'{a},{b}']:+.4f}")
    # O^hi(P) by skeletons, signed
    Ohi = {}
    S = 0.0
    Pl = [2,4,8,16,32,64]
    for M in range(2, 65):
        for c in range(max(1, M//4+1), M):
            if m.gcd(M, c) == 1 and math.log(M/c) < 2*h2:
                S += 2*R(math.log(M/c))/math.sqrt(M*c)*Ah(h, N, M, c)
        if M in Pl: Ohi[M] = S
    row["Ohi"] = Ohi
    print("  O^hi(P): ", {k: round(v, 4) for k, v in Ohi.items()})
    out[str(X)] = row
json.dump(out, open(uHome+"/trunc_results.json", "w"), indent=1)
