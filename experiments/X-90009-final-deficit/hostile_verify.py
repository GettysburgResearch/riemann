"""HOSTILE VERIFIER — independent re-derivation from definitions only (no campaign code imported)."""
import numpy as np, math, sys

def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.flatnonzero(s)

def mobius_upto(n):
    mu = np.ones(n + 1, dtype=np.int64)
    for p in primes_upto(n):
        mu[p::p] *= -1
        mu[p*p::p*p] = 0
    return mu

# ---------- PART 1: lambda-slice identity + ramp values ----------
def ramp_T(X):
    dmax = X // 2
    T = np.zeros(dmax + 1)
    lX = math.log(X)
    for d in range(1, dmax + 1):
        m = np.arange(2, X // d + 1, dtype=float)
        if m.size == 0: continue
        md = m * d
        T[d] = float(np.sum(np.log(m) * md**-0.5 * (lX - np.log(md))))
    return T

def lambda_ramp_direct(X):
    tot = 0.0
    for p in primes_upto(X):
        pk = p
        while pk <= X:
            tot += math.log(p) * pk**-0.5 * math.log(X / pk)
            pk *= p
    return tot

def part1(X):
    T = ramp_T(X); mu = mobius_upto(X // 2)
    ramp_mu = float(sum(mu[d] * T[d] for d in range(1, X // 2 + 1)))
    direct = lambda_ramp_direct(X)
    print(f"[P1] X={X}: |sum mu(d)T(d) - sum Lambda w| = {abs(ramp_mu - direct):.2e}   "
          f"Ramp_lambda - 4sqrtX = {ramp_mu - 4*math.sqrt(X):+.4f}   (-(2logX+4) = {-(2*math.log(X)+4):+.2f})")
    return T, mu

# ---------- PART 2: exhaustive class-H minimization at X=200 (2^25 members), X=120 (2^17) ----------
def popcount(a):
    if hasattr(np, 'bitwise_count'): return np.bitwise_count(a)
    a = a - ((a >> 1) & 0x55555555)
    a = (a & 0x33333333) + ((a >> 2) & 0x33333333)
    return (((a + (a >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24

def part2(X):
    dmax = X // 2
    T = ramp_T(X); mu = mobius_upto(dmax)
    P = [int(p) for p in primes_upto(dmax)]
    np_ = len(P); pidx = {p: i for i, p in enumerate(P)}
    ds, masks = [], []
    for d in range(2, dmax + 1):
        if mu[d] == 0: continue
        m, dd = 0, d
        for p in P:
            if dd % p == 0: m |= 1 << pidx[p]; dd //= p
        ds.append(d); masks.append(m)
    lam_val = T[1] + float(sum(mu[d] * T[d] for d in ds))
    free_min = T[1] - float(sum(T[d] for d in ds))  # f(1)=+1 fixed, all other signs free
    Nf = 1 << np_
    gmin, gargs, chunk = np.inf, None, 1 << 22
    Td = np.array([T[d] for d in ds]); mk = np.array(masks, dtype=np.uint32)
    for lo in range(0, Nf, chunk):
        F = np.arange(lo, min(lo + chunk, Nf), dtype=np.uint32)
        acc = np.full(F.size, T[1])
        for Tdi, m in zip(Td, mk):
            acc += Tdi * (1.0 - 2.0 * (popcount(F & m) & np.uint32(1)))
        i = int(np.argmin(acc))
        if acc[i] < gmin: gmin, gargs = float(acc[i]), int(F[i])
    allminus = (1 << np_) - 1
    print(f"[P2] X={X}: EXHAUSTIVE over 2^{np_} f in H: min = {gmin:+.6f}  lambda-value = {lam_val:+.6f}  "
          f"equal={abs(gmin-lam_val)<1e-9}  argmin==all-minus(lambda)={gargs==allminus}")
    print(f"     min_H - 4sqrtX = {gmin-4*math.sqrt(X):+.4f}   FREE-SIGN min - 4sqrtX = {free_min-4*math.sqrt(X):+.2f}"
          f"   (free/H ratio of deficits: free is power-scale, H is log-scale)")

# ---------- PART 3: raw shells from T-90001 SS0 definitions ----------
def A_of(X):
    """A_X = T^r_X(2) = sum_{p<=X} log p * (v_p - p^{-1/2} log(X/p)); v_q from b-differences."""
    n = np.arange(0, X + 2, dtype=float)
    B = np.zeros(X + 2)
    mm = n[2:]
    B[2:] = 2*np.sqrt(mm)*(np.log(X/mm) - 2*(1 - np.sqrt(mm/X)))  # formula incl. extension at X+1
    A = 0.0
    for p in primes_upto(X):
        idx = np.arange(p, X + 1, p)
        v = float((B[idx] - B[idx + 1]).sum())
        A += math.log(p) * (v - p**-0.5 * math.log(X / p))
    return A

def part3():
    # (a) shells at X=1e4, 1e5 with Y=floor(X/2): claimed -1.159 / -1.603
    for X, claim in [(10**4, -1.159), (10**5, -1.603)]:
        s = A_of(X) - A_of(X // 2)
        print(f"[P3a] T^s_{{{X}}}(2) = {s:+.4f}   (claimed {claim:+.3f})")
    # (b) dyadic chain 2^17 -> 2^7: shells, signs, telescope
    Avals = {j: A_of(2**j) for j in range(7, 18)}
    shells = [Avals[j] - Avals[j-1] for j in range(17, 7, -1)]
    tot = sum(shells)
    print(f"[P3b] chain 2^17->2^7 shells: {[f'{s:+.3f}' for s in shells]}")
    print(f"      all negative: {all(s < 0 for s in shells)}   sum[shell]_+ = {sum(max(s,0) for s in shells):.4f}")
    print(f"      telescope: sum shells = {tot:+.6f}  vs A(2^17)-A(2^7) = {Avals[17]-Avals[7]:+.6f}  gap {abs(tot-(Avals[17]-Avals[7])):.2e}")
    # (c) radical bridge A4: A_X vs 4 sqrt X - R_prime(X)
    for X in [10**4, 10**5]:
        Rp = float(sum(math.log(p) * p**-0.5 * math.log(X/p) for p in primes_upto(X)))
        bridge = 4*math.sqrt(X) - Rp
        print(f"[P3c] X={X}: A_X = {A_of(X):+.3f}   4sqrtX - R_prime = {bridge:+.3f}   diff = {A_of(X)-bridge:+.3f}   log^2 X = {math.log(X)**2:.0f}")

# ---------- PART 4: deficit arithmetic ----------
def part4():
    for X in [10**6, 10**40]:
        LL = math.log(math.log(X))
        avail = 2*LL
        # needed M: (1+M)e^{-M} = X^{-1/2} (RH-grade shell)
        M = 1.0
        for _ in range(200): M = -math.log(X**-0.5 / (1+M))
        print(f"[P4] X=1e{int(math.log10(X))}: available M <= 2loglogX = {avail:.2f}   needed (RH-grade) = {M:.1f}   (1/2)logX = {0.5*math.log(X):.1f}")
    X = 10**6
    LL, L = math.log(math.log(X)), math.log(X)
    sec = LL / L  # GHS secondary term — floor even at maximal distance
    print(f"[P4] X=1e6: GHS secondary-term floor sqrtX*LL/logX = {math.sqrt(X)*sec:.0f}  vs demand X^0.1 = {X**0.1:.1f}"
          f"   ratio = {math.sqrt(X)*sec/X**0.1:.0f}  (claimed ~45)")
    eps = 0.1
    print(f"[P4] assembly constant (1-2^-eps)^-1 at eps=0.1 = {1/(1-2**-eps):.2f}; "
          f"Hall floor exponent 2*kappa = {2*0.32867416320:.4f}")
    z = -1.4603545088  # zeta(1/2)
    print(f"[P4] moat closed form 2*sqrt2*(1+zeta(1/2))*log2 = {2*math.sqrt(2)*(1+z)*math.log(2):+.5f}  (docs print a leading minus AND -0.90250: sign typo in prose, value correct)")

if __name__ == '__main__':
    part1(2000)
    part2(120)
    part2(200)
    part3()
    part4()
