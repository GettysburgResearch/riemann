import itertools
from mpmath import iv, mp

iv.prec = 250  # bits, interval arithmetic

PRIMES61 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

def mobius_sf(fac_count):
    return 1 if fac_count % 2 == 0 else -1

# enumerate squarefree d | P_61 with d <= bound
def smooth_divisors(bound):
    out = [(1, 1)]  # (d, mu)
    for p in PRIMES61:
        new = []
        for d, mu in out:
            nd = d * p
            if nd <= bound:
                new.append((nd, -mu))
        out += new
    return sorted(out)

def T_iv(u):
    # u: iv.mpf interval, assumed >= 1 checked outside
    return 4 * iv.sqrt(u) - 3

def leaf_deficit(base, p, y):
    """t_d = d^{-1/2}[T(base/d) - p^{-1/2} T(y/d)], active d <= base.
       returns (sum mu(d) t_d as interval, active count)"""
    divs = smooth_divisors(base)
    total = iv.mpf(0)
    count = 0
    rp = 1 / iv.sqrt(iv.mpf(p))
    for d, mu in divs:
        if d > base:
            continue
        count += 1
        sd = iv.sqrt(iv.mpf(d))
        val = T_iv(iv.mpf(base) / d)
        if d <= y:
            val = val - rp * T_iv(iv.mpf(y) / d)
        t_d = val / sd
        total += mu * t_d
    return total, count

tot, cnt = leaf_deficit(923, 71, 13)
mp.dps = 30
print("active divisor count (d<=923):", cnt)
print("E_T - O_T interval lower:", mp.nstr(tot.a, 25))
print("E_T - O_T interval upper:", mp.nstr(tot.b, 25))
print("width:", mp.nstr(tot.delta, 5))
print("E_T - O_T > 17 :", tot.a > 17)
print("E_T - O_T > 18 :", tot.a > 18)
