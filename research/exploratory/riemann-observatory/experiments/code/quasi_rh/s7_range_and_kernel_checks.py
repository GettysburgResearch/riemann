# s7_range_and_kernel_checks.py -- Level-2 audit of Section 7 of "The Quasi-Riemann Hypothesis"
# (paper2.tex l.2217-2685). Written from scratch; no code from the OpenAI repository is used or run.
#
# Checks the INEQUALITY layer of Section 7 (the identities are checked in s7_transfer_identities.py):
#   R1  Lemma 7.1, y-range domination (l.2330-2333): every row (C,t,d,f,h) in the displayed ranges
#       has N(h f^2) <= Y_{C,d}, using c_I >= 4 C_Phi v^2 and LF <= Sigma.
#   R2  Lemma 7.3, support and child-scale bookkeeping (l.2541-2621, eq:child-column-lower-bound):
#       for random admissible (H,L,F,Sigma) and random (r,f',k',j) in the support,
#         N(k') <= HL/(Sigma F N(r)^2), H' >= F' >= 1, X'/N(j) >= 1, F'N(j) >= 1, 1 <= X'/X'_0 < 4,
#         H'/Sigma' <= H/Sigma, Sigma' <= L, H' <= HL/(Sigma F), Sigma' >= 1,
#       and the rescaled kernel support [u/(2 rho), 2v/rho] lies in [u/8, 2v], inside int[u/16, 4v].
#       Exact rational arithmetic (fractions.Fraction); random and boundary samples.
#   R3  Kernel smoothness (l.2316-2325, l.2603-2614): the Euler-operator identity
#         (x1 d/dx1)^a (x2 d/dx2)^b hatPhi(A/(x1 x2)) = (-1)^(a+b) [(t d/dt)^(a+b) hatPhi](A/(x1 x2)),
#       checked symbolically (sympy, generic hatPhi) for a+b <= 6. Since supp hatPhi is in [0,C_Phi],
#       the right side is bounded by max_{k<=a+b} sup_{[0,C_Phi]} |(t d/dt)^k hatPhi|, uniformly in A >= 0.
#   R4  Zero-frequency sums (l.2282-2284, l.2416, l.2656-2662): ideal-counting constants for
#       #{g squarefree, prime to 30 : N g <= x} <= c x and sum_{N t <= x} 1/N t << log x, tabulated.
# Run:  python3 -I s7_range_and_kernel_checks.py
import sys, os, math, random, itertools
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

random.seed(7)
fails = 0; tests = 0
def check(cond, msg):
    global fails, tests
    tests += 1
    if not cond:
        fails += 1
        if fails < 20: print("FAIL:", msg)

def rand_fr(lo, hi, den=97):
    return Fr(random.randint(int(lo * den), int(hi * den)), den)

# ---------------------------------------------------------------- R1
for trial in range(20000):
    v = rand_fr(Fr(1, 2), 5); CPhi = rand_fr(Fr(1, 10), 4)
    cI = max(Fr(1), 4 * CPhi * v * v)
    L = rand_fr(1, 300); F = rand_fr(1, 50)
    Sigma = L * F * rand_fr(1, 20)           # LF <= Sigma
    H = rand_fr(1, Sigma)                    # H <= Sigma
    NC = random.choice([1, 7, 13, 49, 91, 19 * 7, 37])
    Nd = random.choice([d for d in [1, 7, 13, 19, 37, 49, 91, 133] if NC % d == 0])
    Nf = rand_fr(F, 2 * F - Fr(1, 97))
    Nh_max = CPhi * v * v * L * L * Nd / (H * NC * NC)
    Nh = rand_fr(0, Nh_max) if Nh_max > 0 else Fr(0)
    Ny = Nh * Nf * Nf
    Y = cI * Sigma * L * F * Nd / (H * NC * NC)
    check(Ny <= 4 * CPhi * v * v * L * L * F * F * Nd / (H * NC * NC), "R1 first inequality")
    check(Ny <= Y, "R1 N(y) <= Y_{C,d}: %s" % ((v, CPhi, L, F, Sigma, H, NC, Nd),))
print("R1 done: tests so far", tests, "failures", fails)

# ---------------------------------------------------------------- R2
def r2_sample(boundary=False):
    v = rand_fr(Fr(1, 2), 5); u = rand_fr(Fr(1, 10), v); CPhi = rand_fr(Fr(1, 10), 4)
    cI = max(Fr(1), 4 * CPhi * v * v)
    L = rand_fr(1, 10 ** 4); F = rand_fr(1, 100)
    Sigma = max(L * F, rand_fr(1, 10 ** 6)) * (1 if boundary else rand_fr(1, 3))
    H = Sigma if boundary else rand_fr(1, Sigma)
    # dyadic R, F' and an r, f' in them
    R = Fr(2) ** random.randint(0, 8); Fp = Fr(2) ** random.randint(0, 8)
    Nr = R if boundary else rand_fr(R, 2 * R - Fr(1, 97))
    Nfp = Fp if boundary else rand_fr(Fp, 2 * Fp - Fr(1, 97))
    # supports: N(r)N(f') <= 2vL ; N(k') <= (4 C_Phi v^2/c_I) HL/(Sigma F N(r)^2), f' | k'  => N(k') >= N(f')
    if Nr * Nfp > 2 * v * L: return None
    kmax = (4 * CPhi * v * v / cI) * H * L / (Sigma * F * Nr * Nr)
    if kmax < Nfp: return None                  # no nonzero term: r not retained
    Nk = Nfp * (1 if boundary else rand_fr(1, kmax / Nfp))
    Nj = Nr if boundary else rand_fr(1, Nr)     # j | r
    return dict(v=v, u=u, CPhi=CPhi, cI=cI, L=L, F=F, Sigma=Sigma, H=H, R=R, Fp=Fp, Nr=Nr, Nfp=Nfp, Nk=Nk, Nj=Nj)

n_ok = 0
for trial in range(400000):
    s = r2_sample(boundary=(trial % 10 == 0))
    if s is None: continue
    n_ok += 1
    v, u, L, F, Sigma, H, R, Fp, Nr, Nfp, Nk, Nj = (s[k] for k in ["v", "u", "L", "F", "Sigma", "H", "R", "Fp", "Nr", "Nfp", "Nk", "Nj"])
    Xp = L / (R * Fp); Sp = Xp * Fp; Hp = H * L / (Sigma * F * R * R); X0 = L / (Nr * Nfp)
    check(Nk <= H * L / (Sigma * F * Nr * Nr), "R2 N(k') bound")
    check(Fp <= Nfp <= Nk <= Hp, "R2 F' <= N(k') <= H'")
    check(Hp >= 1, "R2 H' >= 1")
    check(Xp / Nj >= Sigma * F * Nr * Nr / (H * R * Nj) >= F * Sigma / H >= 1, "R2 child column bound %s" % s)
    check(Fp * Nj >= 1, "R2 F'N(j) >= 1")
    rho = Xp / X0
    check(1 <= rho < 4, "R2 X'/X'_0 in [1,4)")
    check(Hp / Sp == H / (Sigma * F * R) and Hp / Sp <= H / Sigma, "R2 H'/Sigma'")
    check(Sp <= L and Sp >= 1, "R2 1 <= Sigma' <= L")
    check(Hp <= H * L / (Sigma * F), "R2 H' <= HL/(Sigma F)")
    lo, hi = u / 2 / rho, 2 * v / rho        # support of x -> U0(rho x), U0 supported in [u/2, 2v]
    check(u / 8 < lo and hi <= 2 * v, "R2 rescaled support in [u/8, 2v]")
    check(u / 16 < u / 8 and 2 * v < 4 * v, "R2 [u/8,2v] in int[u/16,4v]")
print("R2 done: admissible samples", n_ok, " tests so far", tests, "failures", fails)

# ---------------------------------------------------------------- R3
import sympy as sp
x1, x2, A, t = sp.symbols('x1 x2 A t', positive=True)
hp = sp.Function('hatPhi')
for a in range(0, 4):
    for b in range(0, 4):
        if a + b > 6: continue
        expr = hp(A / (x1 * x2))
        for _ in range(a): expr = x1 * sp.diff(expr, x1)
        for _ in range(b): expr = x2 * sp.diff(expr, x2)
        rhs = hp(t)
        for _ in range(a + b): rhs = t * sp.diff(rhs, t)
        rhs = (-1) ** (a + b) * rhs.subs(t, A / (x1 * x2))
        ok = sp.simplify(sp.expand(expr - rhs.doit())) == 0
        check(ok, "R3 Euler identity a=%d b=%d" % (a, b))
print("R3 done: tests so far", tests, "failures", fails)

# ---------------------------------------------------------------- R4
from s4_zw import eisenstein_primes, squarefree_products, nm
P = [p for p in eisenstein_primes(3000) if p.q != 25]
cols = squarefree_products(P, 3000)
Ns = sorted(nm(c) for c in cols)
worst = max(sum(1 for N in Ns if N <= x) / x for x in range(1, 3001))
harm = [(x, sum(1 / N for N in Ns if N <= x) / math.log(2 * x)) for x in (10, 100, 1000, 3000)]
print("R4  max_x #{g sqfree prime to 30, N g <= x}/x for x<=3000: %.3f" % worst)
print("R4  sum_{N t <= x} 1/N t  /  log(2x):", ", ".join("x=%d: %.3f" % h for h in harm))
check(worst < 2, "R4 counting constant")

print("TOTAL tests %d failures %d" % (tests, fails))
