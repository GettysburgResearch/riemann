import time, flint, sys
from flint import acb, arb
flint.ctx.prec = 64
c20 = None
def chars():
    # Kronecker characters as flint dirichlet_char, built and checked independently
    import math
    def kron(d, n):
        from math import gcd
        if gcd(abs(d), n) != 1: return 0
        res = 1
        while n % 2 == 0:
            n //= 2; res *= 1 if d % 8 in (1, 7) else -1
        a, m, j = d % n, n, 1
        while a:
            while a % 2 == 0:
                a //= 2
                if m % 8 in (3, 5): j = -j
            a, m = m, a
            if a % 4 == 3 and m % 4 == 3: j = -j
            a %= m
        return res * j if m == 1 else 0
    out = {}
    for d in (-20, -4, 5):
        q = abs(d)
        for lab in range(1, q):
            if math.gcd(lab, q) != 1: continue
            c = flint.dirichlet_char(q, lab)
            if c.order() != 2: continue
            ok = all((kron(d, n) == 0 and math.gcd(n, q) > 1) or (math.gcd(n, q) == 1 and (1 if c.chi_exponent(n) == 0 else -1) == kron(d, n)) for n in range(1, q))
            if ok: out[d] = c
    return out
C = chars()
def Z(s):
    return acb.zeta(s) * acb.dirichlet_l(s, C[-20]) + acb.dirichlet_l(s, C[-4]) * acb.dirichlet_l(s, C[5])
if __name__ == '__main__':
    for t in [148065.85, 506416.5, 3587891.15067]:
        t0 = time.time(); v = Z(acb(1.01, t)); print(t, v, round(time.time()-t0, 2))
