#!/usr/bin/env python3
"""U3 adjudication, independent pass: (a) Banks's delta0 arithmetic in ball arithmetic;
(b) LZZ's pivotal constant phi (Thm 6.3) from its displayed closed form, for the four Table 1 rows;
(c) the margins used in Banks's all-q deduction; (d) properties of the hardest adversarial d of pass 1.
Our own code; python-flint arb (rigorous for (a),(b),(c) given the transcribed formulas)."""
from flint import arb, ctx
import math
ctx.prec = 200
e32 = arb(1.5).exp()
C1 = 2 * e32 / 9
C2 = e32 / 4
w = 8 * (C2 + arb(8) / 5)
print("(a) C1 =", C1.str(12), " C2 =", C2.str(12), " 8(C2+8/5) =", w.str(12))
omega = 22
assert w > 21 and w < 22, "ceil must be 22"
d0 = arb(9) / (128 * (omega + 1) * C1)
d0b = arb(81) / (5888 * e32)
print("    omega = 22, delta0 = 9/(128*23*C1) =", d0.str(15), " = 81/(5888 e^1.5):", d0b.str(15),
      " overlap:", d0.overlaps(d0b))
print("    delta0 - 3.0e-3 =", (d0 - arb(3) / 1000).str(6), "(> 0:", d0 > arb(3) / 1000, ")")
print("(c) LZZ gives (1-beta) log q > 1/5 = 0.2 for q <= 1e10;  0.2/3.0e-3 =", (arb(1) / 5 / (arb(3) / 1000)).str(6))
print("    Guo Thm 1.1: 1/100 > 3.0e-3:", arb(1) / 100 > arb(3) / 1000)
print("    1 - 1/(5 log 3) =", (1 - 1 / (5 * arb(3).log())).str(8), "> 1/2 (so Platt's sigma>0 range suffices)")
print("    1 - 3.0e-3/log(1e10) =", (1 - (arb(3) / 1000) / (10 * arb(10).log())).str(10))
# (b) phi
for lam in ("1.6", "1.3", "1.2", "1.1", "1.4", "1.0"):
    r = arb(lam) / (10 * arb(10).log())
    r1 = r + arb(7) / 8
    th = [arb.pi() / 2] + [((r + arb(x)) / r1).acos() for x in ("0.125", "0.25", "0.5", "0.75")] + [arb(0)]
    A = lambda n, m: th[m].sin() - th[n].sin()
    B = lambda n, m: (th[n] - th[m]) / 2 + (th[n].sin() * th[n].cos() - th[m].sin() * th[m].cos()) / 2
    phi = r * A(1, 5) / (arb.pi() * r1) + B(0, 1) / (arb.pi() * (8 * r + 1)) + B(1, 5) / arb.pi()
    print(f"(b) lam={lam}: r={r.str(10)}  phi={phi.str(12)}")
r = arb("1e-30"); r1 = r + arb(7) / 8
th = [arb.pi() / 2] + [((r + arb(x)) / r1).acos() for x in ("0.125", "0.25", "0.5", "0.75")] + [arb(0)]
A = lambda n, m: th[m].sin() - th[n].sin()
B = lambda n, m: (th[n] - th[m]) / 2 + (th[n].sin() * th[n].cos() - th[m].sin() * th[m].cos()) / 2
print("    phi(r=1e-30) =", (r * A(1, 5) / (arb.pi() * r1) + B(0, 1) / (arb.pi() * (8 * r + 1)) + B(1, 5) / arb.pi()).str(12), "(LZZ: phi(0)=1/4)")
# (d) the hardest adversarial discriminant reported by pass 1
d = 9447241877
def sqfree(m):
    p = 2
    while p * p <= m:
        if m % (p * p) == 0:
            return False
        p += 1 if p == 2 else 2
    return True
primes = [p for p in range(3, 200) if all(p % k for k in range(2, int(p ** 0.5) + 1))]
leg = {p: (0 if d % p == 0 else (1 if pow(d % p, (p - 1) // 2, p) == 1 else -1)) for p in primes}
chi2 = 1 if d % 8 in (1, 7) else -1
allm1 = [2] if chi2 == -1 else []
for p in primes:
    if leg[p] == -1 and (not allm1 or allm1[-1] == max(x for x in [2] + primes if x < p)):
        allm1.append(p)
    else:
        break
print(f"(d) d={d}: d mod 8 = {d % 8}, squarefree = {sqfree(d)}, chi(2) = {chi2},"
      f" chi(p) = -1 for all primes p <= {allm1[-1]}; next prime chi = {leg[primes[len(allm1) - 1]]}"
      f" at p = {primes[len(allm1) - 1]}")
