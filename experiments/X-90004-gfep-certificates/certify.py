"""Certified interval enclosures (mpmath.iv, directed rounding) for the cell-sign
inequalities. C_N linear in L => cell sign follows from the two endpoint signs.
POS claims: N=1..4 endpoints > 0 (worst: C_4(log5) > 1/25).
NEG claims: N=5..40 endpoints < 0 (worst margin at N=6)."""
from mpmath import iv, mp
iv.dps = 60

def mobius_list(n):
    mu = [0]*(n+1); mu[1]=1
    for i in range(1, n+1):
        if mu[i]:
            for j in range(2*i, n+1, i):
                mu[j] -= mu[i]
    return mu

NMAX = 40
mu = mobius_list(NMAX+2)

def C_iv(N, Lint):
    s = iv.mpf(0)
    for k in range(1, N+1):
        if mu[k]:
            term = (1 + (Lint - iv.log(k))/2)/iv.sqrt(k)
            s += mu[k]*term
    return s

ok = True
rows = []
for N in range(1, NMAX+1):
    a = C_iv(N, iv.log(N))
    b = C_iv(N, iv.log(N+1))
    if N <= 4:
        good = (a.a > 0) and (b.a > 0)   # certified strictly positive
        rows.append((N, float(a.a), float(b.a), "POS_CERT" if good else "FAIL"))
    else:
        good = (a.b < 0) and (b.b < 0)   # certified strictly negative
        rows.append((N, float(a.b), float(b.b), "NEG_CERT" if good else "FAIL"))
    ok = ok and good

for r in rows: print(f"N={r[0]:3d}  endpointL={r[1]:+.9f} endpointR={r[2]:+.9f}  {r[3]}")
print("ALL_CERTIFIED" if ok else "CERTIFICATION_FAILED")

# the two binding constants, with certified enclosures:
c4 = C_iv(4, iv.log(5)); c6l = C_iv(6, iv.log(6)); c6r = C_iv(6, iv.log(7))
print("C_4(log5) in", c4, " > 1/25:", c4.a > 0.04)
print("C_6(log6) in", c6l, "; C_6(log7) in", c6r)
# also M_N=sum mu/sqrt k for N=5..40 all negative? (not needed for linearity argument, report)
