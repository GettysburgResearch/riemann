"""Exact checks for LF_THETA_THIRD.md: the F_2 ledger formula (LF) at theta = 1/3.

Status: EXPLORATION / exact symbolic and finite checks.  The symbolic part [A] is an exact
        polynomial identity in the free symbol theta (sympy); it re-derives the manuscript's
        (old-eq:2.15)-(old-eq:2.16) from its theta-free definitions (old-eq:2.7), the exponent
        table at l. 13846-13861, (old-eq:2.13) and (old-eq:2.14), with the exceptional count
        exponent theta*(m' - f) as the only theta input.  Parts [B], [C] are finite exact checks
        (Fractions, integers, exact residue symbols in Z[omega]); they are not proofs of the
        lemmas they illustrate.
Run:    python3 -I lf_theta_third_checks.py
Inputs: none (self-contained; no repository module is imported).
"""
import sys
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
import sympy as sp

RESULTS = []


def report(tag, ok, msg, control=False):
    # for a control, ok = True means the wrong rule was detected (it fails, as it must)
    RESULTS.append((tag, bool(ok), control))
    kind = 'CTRL' if control else 'CHECK'
    print(f"[{tag}] {kind} {'PASS' if ok else 'FAIL'}: {msg}")


# =============================================================================================
# [A] the ledger, theta generic (sympy)
# =============================================================================================
th = sp.Symbol('theta')
(A, m, q, c, d, R, E, Dk, w, wo, Bc, g, l, s0, eG,
 b2, c2, d2, g2, p2, t2, V, f) = sp.symbols(
    "A m q c d R E D_k w w_o B_c g ell s_0 epsilon_G b_2 c_2 d_2 g_2 p_2 t_2 V f", real=True)
SECOND = {b2, g2, p2, t2, V, f}          # second-transform symbols (F_2 side)

# theta-free definitions, transcribed from the manuscript (line numbers in LF_THETA_THIRD.md)
M = m + q                                 # total width (consistent with (2.13): M' = M + J - g - g_2 + t_2)
K0 = 2*A - c - d + R + E - m              # l. 13284
K = K0 - Dk                               # D_k := K_0 - K (l. 14459-14460)
qt = q + R + E                            # (2.3), l. 13293
a0 = A - c - w                            # l. 13417
Lam_c = a0 + qt + wo + w + Bc - s0 + eG   # (2.7), l. 13419-13423
J = d - c + Dk - 2*w + wo                 # (2.8)
mp = 2*a0 - K - g - g2 - V                # (2.13), l. 13793
qp = qt + wo + t2 + V                     # (2.13), l. 13794
Mp = mp + qp                              # (2.13), l. 13795
Dchild = b2 - p2 + w + Bc + l             # (2.14), l. 13866-13871
expo_sum = (-a0) + (K + g - a0) + (-l) + (p2 - s0) + (g2 - t2) + (a0 - b2)  # table l. 13846-13856


def LHS(kappa):
    """count exponent kappa*(m'-f) + volume a_0 - b_2 - allowance (M' + Delta_child)  [(2.15) left side]"""
    return kappa*(mp - f) + a0 - b2 - (Mp + Dchild)


def F1(t):
    return t*c + (1 - t)*(d + Dk) + 2*t*w + t*qt + wo + Bc - (1 - t)*g + l


def F2(t, fsym=f):
    return 2*b2 - (1 - t)*g2 - p2 + t2 + t*V + t*fsym


def zero(e):
    return sp.expand(e) == 0


# [A1] (2.14) is (2.7) minus the exponent table, with (2.13): theta-free
report('A1', zero((Lam_c - eG) - expo_sum - (Mp + Dchild)),
       "(old-eq:2.7) - [exponent table l.13846-13856] = M' + Delta_child exactly (no theta, no n)")
# [A2] M' = M + J - g - g_2 + t_2 (2.13), theta-free
report('A2', zero(Mp - (M + J - g - g2 + t2)), "(2.13): M' = m' + q' = M + J - g - g_2 + t_2, M = m + q")
# [A3] the manuscript's intermediate form (l. 14453-14457), theta generic
report('A3', zero(LHS(th) - (a0 - 2*b2 + p2 - w - Bc - l - (1 - th)*mp - qp - th*f)),
       "LHS(theta) = a_0 - 2b_2 + p_2 - w - B_c - ell - (1-theta)m' - q' - theta f  (l.14453-14457 at theta=1/6)")
# [A4] the identity (2.15) with theta symbolic
resid = sp.expand(LHS(th) - (A - (1 - th)*M - F1(th) - F2(th)))
report('A4', resid == 0, "LHS(theta) = A - (1-theta)M - F_1(theta) - F_2(theta) identically in theta, with "
       "F_2(theta) = 2b_2 - (1-theta)g_2 - p_2 + t_2 + theta V + theta f")
# [A5] canonical split: F_2 := the second-transform part of A - (1-theta)M - LHS; F_1 := the rest
tot = sp.expand(A - (1 - th)*M - LHS(th))
poly = sp.Poly(tot, *sorted(SECOND, key=str))
F2_canon = sum(coef*mon for mon, coef in zip([sp.Mul(*[v**e for v, e in zip(poly.gens, ms)]) for ms in poly.monoms()],
                                               poly.coeffs()) if mon != 1)
F1_canon = sp.expand(tot - F2_canon)
ok5 = zero(F2_canon - F2(th)) and zero(F1_canon - F1(th)) and not (F1_canon.free_symbols & SECOND)
report('A5', ok5, "split is forced: the b_2,g_2,p_2,t_2,V,f-part of A-(1-theta)M-LHS is exactly F_2(theta); "
       "the remainder is F_1(theta) and contains no second-transform symbol")
# [A6] theta enters only through the count coefficient
dLHS = sp.expand(sp.diff(LHS(th), th) - (mp - f))
coeffs = {str(s): sp.factor(sp.expand(F2(th)).coeff(s)) for s in (b2, g2, p2, t2, V, f)}
report('A6', dLHS == 0 and coeffs == {'b_2': 2, 'g_2': th - 1, 'p_2': -1, 't_2': 1, 'V': th, 'f': th},
       f"dLHS/dtheta = m' - f (count exponent is the only theta input); F_2 coefficients {coeffs}")
# [A7] theta = 1/6 reproduces the manuscript (2.15)-(2.16) verbatim (l. 14437-14446)
s6 = sp.Rational(1, 6)
F1_ms = c/6 + 5*(d + Dk)/6 + w/3 + qt/6 + wo + Bc - 5*g/6 + l
F2_ms = 2*b2 - sp.Rational(5, 6)*g2 - p2 + t2 + V/6 + f/6
report('A7', zero(F1(s6) - F1_ms) and zero(F2(s6) - F2_ms) and
       zero((mp - f)/6 + a0 - b2 - (Mp + Dchild) - (A - sp.Rational(5, 6)*M - F1_ms - F2_ms)),
       "theta = 1/6 gives the manuscript's (2.15)-(2.16) verbatim")
# [A8] theta = 1/3 gives (LF) and the cubic F_1 of CUBIC_N3_GAPS Sec. 3.2 item 3
s3 = sp.Rational(1, 3)
LF = 2*b2 - sp.Rational(2, 3)*g2 - p2 + t2 + V/3 + f/3
F1_cub = c/3 + 2*(d + Dk)/3 + 2*w/3 + qt/3 + wo + Bc - 2*g/3 + l
report('A8', zero(F2(s3) - LF) and zero(F1(s3) - F1_cub) and
       zero((mp - f)/3 + a0 - b2 - (Mp + Dchild) - (A - sp.Rational(2, 3)*M - F1_cub - LF)),
       "theta = 1/3 gives (LF): F_2 = 2b_2 - (2/3)g_2 - p_2 + t_2 + V/3 + f/3, and the cubic F_1")

# ---- failing controls for [A]
r1 = sp.expand((mp - f)/3 + a0 - b2 - (Mp + Dchild) - (A - sp.Rational(2, 3)*M - F1_cub - F2_ms))
report('A-CTRL1', r1 != 0, f"sextic F_2 coefficients with the cubic count do not close: residual {r1}", True)
r2 = sp.expand((mp - f)/6 + a0 - b2 - (Mp + Dchild) - (A - sp.Rational(2, 3)*M - F1_cub - LF))
report('A-CTRL2', r2 != 0, f"sextic count exponent (m'-f)/6 with the cubic F_1, F_2 does not close: residual {r2}", True)
# moving V out of q' (i.e. not counting the V primes in the moving support) changes the V coefficient
r3 = sp.expand(sp.Rational(1, 3)*(mp - f) + a0 - b2 - ((mp + qp - V) + Dchild) - (A - sp.Rational(2, 3)*M - F1_cub - LF))
report('A-CTRL3', r3 != 0, f"dropping V from q' (2.13) breaks (LF): residual {r3}", True)

# =============================================================================================
# [B] the count input: forced residue and f, with an exact Z[omega] witness
# =============================================================================================
def forced_residue(i, n):
    """residue of v_p(h') forced at a nonunit equal-multiplicity prime of multiplicity i
    (v_p(G_c V_id) = i + 1, no older moving character; Corollary 4.H(4) / l. 14349-14357)"""
    return (-(i + 1)) % n


report('B1', forced_residue(1, 6) == 4 and forced_residue(1, 3) == 1 and
       [forced_residue(i, 3) for i in range(1, 7)] == [1, 0, 2, 1, 0, 2],
       "forced residue -(i+1) mod n: n=6, i=1 -> 4 (l. 14357); n=3: i=1..6 -> 1,0,2,1,0,2")
# the f actually available from the i = 1 primes is r(1,n) * v_1 (log-norm of h_0 restricted to them)
report('B2', Fr(forced_residue(1, 6)) >= 2 and forced_residue(1, 3) == 1,
       "n=6: q_h0 >= Z^{4 v_1}; the manuscript's f = 2v_1 is a weakening (2 <= 4). "
       "n=3: q_h0 >= Z^{v_1} only, so f = v_1 and no weakening is available")


# exact cubic residue symbols on Z[omega]; elements are pairs (a, b) <-> a + b*omega
def emul(x, y):
    a, b = x; c_, d_ = y
    return (a*c_ - b*d_, a*d_ + b*c_ - b*d_)


def enorm(x):
    a, b = x
    return a*a - a*b + b*b


def epow(x, e):
    z = (1, 0)
    for _ in range(e):
        z = emul(z, x)
    return z


def units():
    u, out = (1, 0), []
    zeta = (1, 1)                      # -omega^2 = 1 + omega, a primitive 6th root of unity
    for _ in range(6):
        out.append(u); u = emul(u, zeta)
    return out


def primary(x):
    for u in units():
        y = emul(u, x)
        if y[0] % 3 == 1 and y[1] % 3 == 0:
            return y
    raise ValueError(x)


def is_prime_int(n):
    if n < 2:
        return False
    k = 2
    while k*k <= n:
        if n % k == 0:
            return False
        k += 1
    return True


def split_primes(bound):
    out = []
    for ell in range(7, bound + 1, 3):
        if ell % 3 != 1 or not is_prime_int(ell):
            continue
        seen = set()
        for a in range(-60, 61):
            for b in range(-60, 61):
                if enorm((a, b)) == ell:
                    pi = primary((a, b))
                    if pi not in seen:
                        seen.add(pi)
        for pi in sorted(seen):
            a, b = pi
            r = next(r for r in range(ell) if (r*r + r + 1) % ell == 0 and (a + b*r) % ell == 0)
            out.append((pi, ell, r))
    return out


def chi(n_data, x):
    """(x/n)_3 as exponent in Z/3 (value omega^e), None if n | x.  n = (pi, ell, r), pi | (omega - r)."""
    pi, ell, r = n_data
    red = (x[0] + x[1]*r) % ell
    if red == 0:
        return None
    v = pow(red, (ell - 1)//3, ell)
    return {1: 0, r % ell: 1, (r*r) % ell: 2}[v]


PR = split_primes(1500)
ok_b3, details, ctrl_hits = True, [], 0
for p in [next(t for t in PR if t[1] == 7), next(t for t in PR if t[1] == 13)]:
    others = [n for n in PR if n[0] != p[0]]
    exc_ks = []
    for k in range(6):
        x = epow(p[0], 2 + k)                     # row factor G_c V_id (valuation 2) times h' = p^k
        vals = {n[0]: chi(n, x) for n in others}
        principal = all(v == 0 for v in vals.values())
        # witness of non-S-support: two primary primes congruent mod 18 with different values
        bycls, wit = {}, None
        for n0, v in vals.items():
            key = (n0[0] % 18, n0[1] % 18)
            if key in bycls and bycls[key] != v:
                wit = key; break
            bycls.setdefault(key, v)
        if principal:
            exc_ks.append(k)
        ok_b3 &= principal == ((2 + k) % 3 == 0)
        ok_b3 &= principal or wit is not None
    details.append((p[1], exc_ks))
    ok_b3 &= exc_ks == [1, 4]
    # minimal exceptional row h' = p has norm q_p^1: the count must allow rows at scale q_p, i.e. f <= v_1
    if min(exc_ks) == 1:
        ctrl_hits += 1
report('B3', ok_b3, f"Z[omega], nonunit i=1 prime p (Np = 7, 13), row factor p^2: n -> chi_n(p^(2+k)) is principal "
       f"iff k = 1, 4 (k <= 5), and otherwise non-constant on two primary primes congruent mod 18 "
       f"({len(PR)} primary primes of norm <= 1500); exceptional k per Np: {details}")
report('B-CTRL1', ctrl_hits == 2, "transcribing the manuscript's f = 2v_1 to n = 3 claims q_h0 >= q_p^2 at each i=1 prime; "
       "the exceptional row h' = p (norm q_p^1) refutes it at Np = 7 and 13", True)

# =============================================================================================
# [C] per-prime tables (exact Fractions)
# =============================================================================================
def local_types(n, imax):
    """(name, c_2, d_2, g_2, p_2, t_2, V, i, j0) for every nonzero local type with i, j0 <= imax"""
    out = []
    for i in range(1, imax + 1):
        if i % n:
            out.append(('unit', i, i, i, 1, 1, 0, i, i))
            out.append(('nonunit', i, i, i, 1, 0, 1, i, i))
        else:
            out.append(('equal n|i', i, i, i, 1, 0, 0, i, i))
        for j0 in range(n, i, n):
            out.append(('unequal', i, j0, j0, 1, 0, 0, i, j0))
            out.append(('unequal', j0, i, j0, 1, 0, 0, j0, i))
    return out


def F2_local(t, ty, f_loc):
    name, c_, d_, g_, p_, t_, V_, i, j0 = ty
    b_ = Fr(c_ + d_, 2)
    return 2*b_ - (1 - t)*g_ - p_ + t_ + t*V_ + t*f_loc, b_


def f_rule(ty, n, mode):
    name, i = ty[0], ty[7]
    if name != 'nonunit' or i != 1:
        return Fr(0)
    return {'cubic': Fr(1), 'sextic_ms': Fr(2), 'none': Fr(0), 'naive2': Fr(2), 'true': Fr(forced_residue(1, n))}[mode]


# [C1] theta = 1/6, manuscript f = 2v_1: the manuscript table l. 14509-14515 verbatim, min F_2/b_2 = 2/3
t6, ok = Fr(1, 6), True
for ty in local_types(6, 48):
    F, b = F2_local(t6, ty, f_rule(ty, 6, 'sextic_ms'))
    name, i, j0 = ty[0], ty[7], ty[8]
    if name == 'unit':
        ok &= F == Fr(7*i, 6)
    elif name == 'nonunit':
        ok &= F == Fr(7*i - 5, 6) + (Fr(1, 3) if i == 1 else 0)
    elif name == 'equal n|i':
        ok &= F == Fr(7*i, 6) - 1
    elif i > j0:
        ok &= F == i + Fr(j0, 6) - 1
mn6 = min(F2_local(t6, ty, f_rule(ty, 6, 'sextic_ms'))[0] / F2_local(t6, ty, 0)[1] for ty in local_types(6, 48))
report('C1', ok and mn6 == Fr(2, 3), f"theta=1/6, f=2v_1: manuscript table l.14509-14515 reproduced (i <= 48); "
       f"min F_2/b_2 = {mn6} (= manuscript (2.17))")

# [C2] theta = 1/3, f = v_1: the 4.G table; kappa_2 = 1 with tight set {nonunit 1, nonunit 2, equal 3}
t3, ok, tight, mn3, mnmin = Fr(1, 3), True, set(), None, None
for ty in local_types(3, 60):
    F, b = F2_local(t3, ty, f_rule(ty, 3, 'cubic'))
    name, i, j0 = ty[0], ty[7], ty[8]
    if name == 'unit':
        ok &= F == Fr(4*i, 3)
    elif name == 'nonunit':
        ok &= F == Fr(4*i, 3) - Fr(2, 3) + (Fr(1, 3) if i == 1 else 0)
    elif name == 'equal n|i':
        ok &= F == Fr(4*i, 3) - 1
    elif i > j0:
        ok &= F == i + Fr(j0, 3) - 1 and F - b == Fr(3*i - j0 - 6, 6)
    ratio = F / b
    mn3 = ratio if mn3 is None else min(mn3, ratio)
    mnmin = (F - min(ty[1], ty[2])) if mnmin is None else min(mnmin, F - min(ty[1], ty[2]))
    if F == b:
        tight.add((name, i))
report('C2', ok and mn3 == 1 and mnmin == 0 and tight == {('nonunit', 1), ('nonunit', 2), ('equal n|i', 3)},
       f"theta=1/3, f=v_1: LEMMAS_4BCD_GH Sec.5 table reproduced (i <= 60); min F_2/b_2 = {mn3} (kappa_2 = 1); "
       f"min F_2 - min(c_2,d_2) = {mnmin}; tight types {sorted(tight)} (= CUBIC_ALLOCATION_LOSS)")

# [C3] side observation, generic n with the true forcing at i = 1: F_2 = b_2 at nonunit i = 1 for every n
ok = all(F2_local(Fr(1, n), ('nonunit', 1, 1, 1, 1, 0, 1, 1, 1), Fr(forced_residue(1, n)))[0] == 1
         for n in range(3, 13))
report('C3', ok, "n = 3..12, theta = 1/n, f = (n-2)v_1 (true forcing): F_2 = b_2 at nonunit i = 1; the sextic 2/3 is "
       "the manuscript's weakening f = 2v_1, not a theta effect")

# ---- failing controls for [C]
mn = min(F2_local(t3, ty, f_rule(ty, 3, 'none'))[0] / F2_local(t3, ty, 0)[1] for ty in local_types(3, 60))
report('C-CTRL1', mn == Fr(2, 3), f"theta=1/3 with f = 0: min F_2/b_2 = {mn} = 2 theta < 1 (kappa_2 = 1 needs f)", True)
F, b = F2_local(t3, ('nonunit', 1, 1, 1, 1, 0, 1, 1, 1), Fr(2))
report('C-CTRL2', F - b == Fr(1, 3), f"theta=1/3 with the naive f = 2v_1: F_2 - b_2 = {F - b} at nonunit i=1, an "
       "unearned spare (refuted by B3/B-CTRL1)", True)
# sextic unit/nonunit selection (6 does not divide i) at n = 3, i = 3: unit bound P^{i-1} vs exact P^{i-1}(P-2)
P, i = 7, 3
exact = sum(1 for x in range(P**3) if x % P and (x - 1) % P)   # F(p^3,p^3; p^3 k), k = 1, summand chi^3 = principal
report('C-CTRL3', exact == P**(i - 1)*(P - 2) and exact > P**(i - 1),
       f"sextic t_2 rule at n=3, i=3 (Np=7): exact local value {exact} = P^2(P-2) exceeds the unit bound P^2 = {P**2}", True)

# =============================================================================================
n_chk = sum(1 for _, _, c_ in RESULTS if not c_)
n_ok = sum(1 for _, ok, c_ in RESULTS if ok and not c_)
n_ctl = sum(1 for _, _, c_ in RESULTS if c_)
n_ctl_ok = sum(1 for _, ok, c_ in RESULTS if ok and c_)
print(f"SUMMARY: checks {n_ok}/{n_chk} PASS; failing controls detected {n_ctl_ok}/{n_ctl}")
sys.exit(0 if (n_ok == n_chk and n_ctl_ok == n_ctl) else 1)
