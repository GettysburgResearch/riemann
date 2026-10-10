"""Finite checks for LEMMA_4I.md (cubic Gauss-row zero, n = 3 transfer of paper.tex l. 13572-13594).

Status: EXPLORATION / finite checks; none of these is a proof of Lemma 4.I.
Run:    python3 -I lemma_4i_checks.py
Arithmetic: exact integer / Z[omega] arithmetic for [I1], [I1b], [I2], [I3] and all controls.
[I4] uses floating point for square roots and is labelled as such.
Imports ../../a2/eis.py read-only (no bytecode written).
"""
import sys, os, itertools, math
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', '..', 'a2')))
import eis  # noqa: E402
from eis import mul, norm, divides, powmod, primary, conj

RESULTS = []
def report(tag, ok, msg, control=False):
    # for a control, "ok" means "the wrong rule was detected (it fails)"
    RESULTS.append((tag, ok, control))
    kind = 'CTRL' if control else 'CHECK'
    print(f"[{tag}] {kind} {'PASS' if ok else 'FAIL'}: {msg}")

CUBE_ROOTS = [(1, 0), (0, 1), (-1, -1)]          # 1, w, w^2  (w = omega)

def chi3_prime(x, p):
    """(x/p)_3 as exponent e (value w^e) via x^{(Np-1)/3} mod p; None if p | x.  Any prime p prime to 3."""
    if divides(p, x): return None
    t = powmod(x, (norm(p) - 1)//3, p)
    for e, z in enumerate(CUBE_ROOTS):
        if divides(p, (t[0] - z[0], t[1] - z[1])): return e
    raise RuntimeError((x, p))

def elt(fac):
    z = (1, 0)
    for p, a in fac:
        for _ in range(a): z = mul(z, p)
    return z

def residues(m):
    """complete residue system of O/mO (Hermite basis of the lattice mO in the basis 1, omega)."""
    a1, b1 = m; a2, b2 = mul(m, (0, 1))
    N = abs(a1*b2 - a2*b1)
    g = math.gcd(b1, b2)
    return [(i, j) for j in range(g) for i in range(N // g)], N

# test primes: inert 2 (norm 4; outside the manuscript's good set if S contains 2, kept as a
# Fact-0 test only), split 7, 13, 19, inert 5 (norm 25).  All primary (= 1 mod 3).
P2 = primary((2, 0)); P5 = primary((5, 0))
P7a = primary((3, 1)); P7b = primary(conj((3, 1)))
P13a = primary((4, 1)); P13b = primary(conj((4, 1)))
P19a = primary((5, 2))
PR = [P2, P7a, P7b, P13a, P13b, P19a, P5]
for p in PR:
    assert eis.is_primary(p) and norm(p) in (4, 7, 13, 19, 25), p
assert norm(P7a) == 7 and not divides(P7a, P7b)

# consistency with the sextic symbol of eis.py at split primes: (x/p)_3 = ((x/p)_6)^2
bad = 0
for p in [P7a, P7b, P13a, P19a]:
    for x in residues(p)[0]:
        k = eis.sym_prime(x, p); e = chi3_prime(x, p)
        if (k is None) != (e is None) or (k is not None and k % 3 != e): bad += 1
report('I0', bad == 0, "direct cubic symbol x^{(Np-1)/3} agrees with (eis sextic symbol)^2 at Np = 7, 7, 13, 19")

# ------------------------------------------------------------------ [I1] G(u,0) brute force
def S0(fac):
    """sum_{x mod u} chi_u(x) as exact count vector [c0, c1, c2] (value c0 + c1 w + c2 w^2)."""
    u = elt(fac); res, N = residues(u)
    V = [0, 0, 0]
    for x in res:
        s = 0
        for p, a in fac:
            e = chi3_prime(x, p)
            if e is None: s = None; break
            s += a*e
        if s is not None: V[s % 3] += 1
    return V, N

def phi(fac):
    r = 1
    for p, a in fac:
        P = norm(p); r *= P**(a - 1)*(P - 1)
    return r

def all_moduli(maxN):
    """all factorisations prod p^a over PR with norm <= maxN (exponents >= 0, not all zero)."""
    out = []
    def rec(i, cur, n):
        if i == len(PR):
            if cur: out.append(list(cur))
            return
        P = norm(PR[i]); a = 0; nn = n
        while nn <= maxN:
            rec(i + 1, cur + ([(PR[i], a)] if a else []), nn)
            a += 1; nn *= P
    rec(0, [], 1)
    return out

MAXN = 2500
mods = all_moduli(MAXN)
# extra cube and near-cube moduli above MAXN
mods += [[(P2, 3), (P7a, 3)], [(P13a, 3)], [(P7a, 3), (P7b, 1)], [(P19a, 3)], [(P2, 3), (P13a, 3)],
         [(P5, 3)] if 25**3 <= 16000 else [(P7b, 3), (P2, 3)]]
n_cube = n_noncube = 0; fails = []
sext_rule_fails = []                     # control: sextic vanishing rule "S0 = 0 unless 6 | every a"
for fac in mods:
    V, N = S0(fac)
    cube = all(a % 3 == 0 for _, a in fac)
    val = (V[0] - V[2], V[1] - V[2])   # reduce by 1 + w + w^2 = 0
    want = (phi(fac), 0) if cube else (0, 0)
    if val != want: fails.append((fac, val, want))
    n_cube += cube; n_noncube += (not cube)
    sext_zero = not all(a % 6 == 0 for _, a in fac)
    if sext_zero and val != (0, 0): sext_rule_fails.append([(norm(p), a) for p, a in fac])
report('I1', not fails,
       f"q_u^(1/2) G(u,0) = sum_x chi_u(x) equals phi(u) 1[u a cube ideal] exactly, for all {len(mods)} moduli "
       f"over {{N=4,7,7,13,13,19,25}} with norm <= {MAXN} plus 6 larger ({n_cube} cubes, {n_noncube} non-cubes)")
report('I1-CTRL', len(sext_rule_fails) > 0,
       f"sextic rule 'G(u,0)=0 unless u is a sixth power' is FALSE at n = 3: {len(sext_rule_fails)} counterexamples, "
       f"first {sext_rule_fails[0]}", control=True)

# [I1b] |G(u,0)| <= q_u^(1/2), exact: phi(u)^2 <= q_u^2 * q_u^... i.e. (phi(u)/q_u^(1/2))^2 <= q_u  <=>  phi(u)^2 <= q_u^2
ok = all((phi(f)**2 <= (math.prod(norm(p)**a for p, a in f))**2) for f in mods if all(a % 3 == 0 for _, a in f))
report('I1b', ok, "on cubes |G(u,0)|^2 = phi(u)^2/q_u <= q_u (exact integer comparison)")

# ------------------------------------------------------------------ [I2] counting cube moduli
# prime ideals of Z[omega] prime to 3, by norm, up to X (split p = 1 mod 3: two ideals; inert p = 2 mod 3: norm p^2)
def prime_ideal_norms(X):
    sieve = [True]*(X + 1); sieve[0] = sieve[1] = False
    for i in range(2, int(X**0.5) + 1):
        if sieve[i]: sieve[i*i::i] = [False]*len(sieve[i*i::i])
    out = []
    for p in range(2, X + 1):
        if not sieve[p] or p == 3: continue
        if p % 3 == 1: out += [(p, 'a'), (p, 'b')]
        elif p*p <= X: out.append((p*p, 'i'))
    return sorted(out)

def ideals_upto(X, plist):
    """list of (norm, frozenset of prime-ideal indices dividing, prod(1-1/P) as Fraction) for all ideals of norm <= X."""
    out = []
    def rec(i, n, supp, eul):
        out.append((n, supp, eul))
        for k in range(i, len(plist)):
            P = plist[k][0]
            if n*P > X: break
            nn = n*P
            while nn <= X:
                rec(k + 1, nn, supp | {k}, eul*Fr(P - 1, P))
                nn *= P
    rec(0, 1, frozenset(), Fr(1))
    return out

XV = 20000                                  # N(v) <= XV  <=>  N(u) = N(v)^3 <= 8e12
PL = prime_ideal_norms(XV)
IDS = ideals_upto(XV, PL)
idx = {pl: k for k, pl in enumerate(PL)}
S_LIST = {'1': [], '(2)': [idx[(4, 'i')]], 'p7': [idx[(7, 'a')]], 'p7 p7bar': [idx[(7, 'a')], idx[(7, 'b')]],
          '(2) p7 p13': [idx[(4, 'i')], idx[(7, 'a')], idx[(13, 'a')]],
          'p7 p13 p19 p31': [idx[(7, 'a')], idx[(13, 'a')], idx[(19, 'a')], idx[(31, 'a')]]}
worst_ratio = Fr(0); viol_crude = 0; tested = 0
for sname, sidx in S_LIST.items():
    qs = math.prod(PL[k][0] for k in sidx)
    for Yv in [10, 30, 100, 300, 1000, 3000, 10000, 20000]:
        cnt = 0
        for n, supp, _ in IDS:
            if n <= Yv and all(k in supp for k in sidx):
                cnt += 1; tested += 1
                if qs**3 > n**3: viol_crude += 1        # crude step: s | u = v^3, s squarefree => q_s^3 <= q_u
        if Yv >= qs:
            worst_ratio = max(worst_ratio, Fr(cnt*qs, Yv))
report('I2', viol_crude == 0 and worst_ratio <= 2,
       f"cube ideals u = v^3 prime to 3 with N(u) <= Y = Yv^3 (Yv <= {XV}) and s | u, s squarefree "
       f"(6 choices): q_s^3 <= q_u in all {tested} cases; max #{{u}} q_s / Y^(1/3) = {float(worst_ratio):.4f} "
       f"(<= 2; the asymptotic constant is pi/(3 sqrt 3) * 2/3 * residue factor)")
# control: non-squarefree s breaks the crude step q_s^3 <= q_u
p7 = PL[idx[(7, 'a')]][0]
report('I2-CTRL', (p7**3)**3 > p7**3,
       "with s = p^3 (not squarefree; l. 13067 says s is squarefree) and u = p^3 a cube: s | u but "
       "q_s^3 = 7^9 > q_u = 7^3, so the crude bound s_0 <= (a_0+theta)/3 needs squarefree s", control=True)

# ------------------------------------------------------------------ [I3] exact exponent algebra
def grid():
    for th in [Fr(0), Fr(1, 100), Fr(1, 10), Fr(1, 3)]:
        for a in [-th] + [Fr(k, 12) for k in range(0, 49)]:
            if a < -th: continue
            for t in range(0, 13):
                yield th, a, t
ok_ref = ok_crude = ok_sext = True; eq_crude = 0; n = 0
for th, a, t in grid():
    s3 = (a + th)/3*Fr(t, 12)            # 0 <= s_0 <= (a_0+theta)/3  (cubic, squarefree s)
    s6 = (a + th)/6*Fr(t, 12)            # 0 <= s_0 <= (a_0+theta)/6  (sextic)
    allow3, allow6 = a - s3 + 2*th, a - s6 + 2*th
    refined = 2*a/3 - 2*s3 + 5*th/3      # count Y^{1/3}/q_s
    crude = 2*a/3 + 5*th/3               # count Y^{1/3}
    sext = a/3 + 4*th/3                  # manuscript l. 13584
    ok_ref &= refined <= allow3 and allow3 - refined == (a + th)/3 + s3
    ok_crude &= crude <= allow3 and allow3 - crude == (a + th)/3 - s3
    eq_crude += (crude == allow3)
    ok_sext &= sext <= allow6
    n += 1
report('I3', ok_ref and ok_crude and ok_sext,
       f"exact on {n} grid points (theta_N in {{0,1/100,1/10,1/3}}, a_0 >= -theta_N, 0 <= s_0 <= (a_0+theta_N)/3): "
       f"refined slack = (a_0+theta_N)/3 + s_0 >= 0; crude slack = (a_0+theta_N)/3 - s_0 >= 0 "
       f"(equality at s_0 = (a_0+theta_N)/3, {eq_crude} points); sextic l. 13584 inequality reproduced")
# controls
c2 = (lambda a, s, th: (a + 2*th) <= (a - s + 2*th))(Fr(1), Fr(1, 4), Fr(0))
report('I3-CTRL-n2', not c2,
       "n = 2 analogue with the crude count (squares: Z^{-a_0}(Y^{1/2} Y^{1/2})^2 = Z^{a_0+2theta}) exceeds the "
       "allowance a_0 - s_0 + 2theta at a_0 = 1, s_0 = 1/4", control=True)
th = Fr(1, 10); a = Fr(1); s = (a + th)/3
c3 = (2*a/3 + 5*th/3) <= (a - s + 2*th - th/100)
report('I3-CTRL-theta', not c3,
       "cubic crude count with support correction 2theta_N - theta_N/100 (instead of 2theta_N) fails at "
       "s_0 = (a_0+theta_N)/3: the crude route uses the whole 2theta_N", control=True)
# control: using the sextic count Y^{1/6} for cubic moduli (i.e. ignoring the cubes that are not sixth powers)
# would under-count; the brute-force I1-CTRL already shows the true support is the cubes.

# ------------------------------------------------------------------ [I4] the whole row-zero term (floating point)
# sup over |B(u)| <= 1 of Z^{-a_0}|sum_u B(u) G(u,0)|^2 = Y^{-1}(sum_{u cube, s|u, N u <= Y} |G(u,0)|)^2,
# with Z^{a_0} = Y (theta_N = 0 normalisation), |G(v^3,0)| = N(v)^{3/2} prod_{p|v}(1-1/P) (exact by I1).
worst_ref = 0.0; worst_allow = 0.0
for sname, sidx in S_LIST.items():
    qs = math.prod(PL[k][0] for k in sidx)
    for Yv in [100, 1000, 5000, 20000]:
        if Yv < qs: continue
        Y = Yv**3
        tot = sum(n**1.5*float(eul) for n, supp, eul in IDS if n <= Yv and all(k in supp for k in sidx))
        Q = tot*tot/Y
        worst_ref = max(worst_ref, Q/(Y**(2/3)/qs**2))
        worst_allow = max(worst_allow, Q/(Y/qs))
report('I4', worst_ref <= 4 and worst_allow <= 4,
       f"(floating point) max Q/(Y^(2/3)/q_s^2) = {worst_ref:.4f}, max Q/(Y/q_s) = {worst_allow:.4f} over 6 s and "
       f"Y = Yv^3, Yv in {{1e2,1e3,5e3,2e4}}: bounded, consistent with the refined bound (a finite check, not a proof)")

nc = sum(1 for t, o, c in RESULTS if not c); npass = sum(1 for t, o, c in RESULTS if not c and o)
ncc = sum(1 for t, o, c in RESULTS if c); ncp = sum(1 for t, o, c in RESULTS if c and o)
print(f"\nSUMMARY: checks {npass}/{nc} PASS; failing controls detected {ncp}/{ncc}")
