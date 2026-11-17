#!/usr/bin/env python3
"""Adjudication of SIEGEL audit item U4 (OAI Lean development not replayed).

Our own code. Run with `python3 -I`. It READS third-party files as text and never executes, builds or
imports anything from them. Nothing here compiles Lean.

Inputs (positional, all optional):
  1. OAI lean root      (default /home/user/openai/math/lean, read-only clone @ 4eaee875)
  2. Kimura vendor list (lean/vendor/SHA256SUMS of github.com/iwaokimura/cln-imq-2k @ e66ab86, downloaded as data)
  3. Kimura challenge   (lean/Challenge/B4ZeroGap.lean @ e66ab86, downloaded as data)
  4. Mathlib dir        (three Mathlib files @ d13f23b, downloaded as data, '/' replaced by '_')

Sections:
  (1) PNT+ patch: text extraction of the files the OAI lakefile ADDS to PrimeNumberTheoremAnd.
  (2) Static import closure of the comparator solution module and of the two proof chains.
  (3) Comment-stripped token scan of the whole closure (sorry/axiom/native_decide/...).
  (4) Statement checks: challenge vs solution statements, comparator config, Mathlib definitions.
  (5) Kimura v2 cross-check: vendored file hashes vs 4eaee875, vendored set vs closures, uncovered modules.
  (6) Exact arithmetic: Cor 4 budget, H, 18818, master-bound constants of the Lean statement vs paper.
  (7) Toy certificates (mod p, rigorous lower bound on rank over K) for the Lean form of Cor 4
      (`actual_biquadratic_rectangle_span`) and for the Vandermonde span; minimal scale kappa* vs 32.
  (8) The duality identity behind `uniform_rectangular_multiplicity`: (D^alpha x^n)(1) = (A n)^alpha.
"""
import os, re, sys, json, hashlib, collections, itertools, time
from fractions import Fraction as Fr

T0 = time.time()
ARGS = sys.argv[1:]
OAI = ARGS[0] if len(ARGS) > 0 else '/home/user/openai/math/lean'
SCR = '/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/audit2026'
KSUMS = ARGS[1] if len(ARGS) > 1 else SCR + '/adj_U4_kimura_repo/lean_vendor_SHA256SUMS'
KCHAL = ARGS[2] if len(ARGS) > 2 else SCR + '/adj_U4_kimura_repo/lean_Challenge_B4ZeroGap.lean'
MLIB = ARGS[3] if len(ARGS) > 3 else SCR + '/adj_U4_mathlib_d13f23b'

RESULTS = []
def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ''))

def sha(b): return hashlib.sha256(b).hexdigest()

def strip_comments(src):
    out = []; i = 0; depth = 0; n = len(src)
    while i < n:
        if depth == 0 and src.startswith('--', i):
            j = src.find('\n', i); i = n if j < 0 else j; continue
        if src.startswith('/-', i): depth += 1; i += 2; continue
        if depth > 0 and src.startswith('-/', i): depth -= 1; i += 2; continue
        if depth == 0: out.append(src[i])
        elif src[i] == '\n': out.append('\n')
        i += 1
    return ''.join(out)

# ---------------------------------------------------------------- (1) PNT+ patch-added files
print('== (1) PNT+ compatibility patch: files added under PrimeNumberTheoremAnd/SiegelZeros/')
patch_path = os.path.join(OAI, 'patches', 'PrimeNumberTheoremAnd-lean4341.patch')
patch_bytes = open(patch_path, 'rb').read()
print('patch sha256', sha(patch_bytes))
files = {}; cur = None
for L in patch_bytes.decode('utf-8').split('\n'):
    if L.startswith('diff --git '):
        cur = re.match(r'diff --git a/(\S+) b/(\S+)', L).group(2)
        files[cur] = {'new': False, 'plus': [], 'minus': 0}
    elif cur is None: continue
    elif L.startswith('new file mode'): files[cur]['new'] = True
    elif L.startswith('+++') or L.startswith('---') or L.startswith('@@') or L.startswith('index '): pass
    elif L.startswith('+'): files[cur]['plus'].append(L[1:])
    elif L.startswith('-'): files[cur]['minus'] += 1
PNT = {}   # module name -> text
for f, d in sorted(files.items()):
    if f.startswith('PrimeNumberTheoremAnd/SiegelZeros/') and f.endswith('.lean'):
        assert d['new'] and d['minus'] == 0, f
        PNT[f[:-5].replace('/', '.')] = '\n'.join(d['plus']) + '\n'
pnt_lines = sum(t.count('\n') for t in PNT.values()) - len(PNT)  # trailing newline added above
print('patch-added PNT+ SiegelZeros modules:', len(PNT), ' lines:', pnt_lines)
check('PNT+ SiegelZeros files are all new files (patch adds, does not modify)', len(PNT) == 12)

# ---------------------------------------------------------------- (2) import closures
print('\n== (2) static import closures')
def src_of(mod):
    p = os.path.join(OAI, *mod.split('.')) + '.lean'
    if os.path.exists(p): return open(p, 'rb').read()
    if mod in PNT: return PNT[mod].encode('utf-8')
    return None
def imports(text):
    toks = strip_comments(text).split(); res = []; i = 0
    while i < len(toks):
        t = toks[i]
        if t in ('module', 'prelude'): i += 1; continue
        if t == 'public' and i + 1 < len(toks) and toks[i + 1] == 'import': i += 1; continue
        if t == 'import': res.append(toks[i + 1]); i += 2; continue
        break
    return res
def closure(start):
    seen, ext, order, stack = set(), collections.defaultdict(set), [], [start]
    while stack:
        m = stack.pop()
        if m in seen: continue
        seen.add(m); b = src_of(m)
        if b is None: ext[m.split('.')[0]].add(m); continue
        order.append(m); stack.extend(imports(b.decode('utf-8')))
    return sorted(order), ext
def lines_of(mods):
    tot = 0
    for m in mods:
        b = src_of(m); tot += b.count(b'\n') if m not in PNT else PNT[m].count('\n') - 1
    return tot
SZ = 'OAI.NumberTheory.SiegelZeros.'
cl_main, ext_main = closure(SZ + 'Main')
cl_thm, _ = closure(SZ + 'Conclusions.Theorem')
cl_drzb, _ = closure(SZ + 'Characters.DirichletRealZeroBoundProof')
oai_main = [m for m in cl_main if m.startswith('OAI.')]
pnt_main = [m for m in cl_main if m.startswith('PrimeNumberTheoremAnd.')]
man = hashlib.sha256()
for m in cl_main: man.update(m.encode() + b'\0' + sha(src_of(m)).encode() + b'\n')
print(f'solution module closure: {len(oai_main)} OAI modules ({lines_of(oai_main)} lines) + '
      f'{len(pnt_main)} patch-added PNT+ modules ({lines_of(pnt_main)} lines); manifest sha256 {man.hexdigest()}')
print('external roots:', {k: len(v) for k, v in ext_main.items()}, ' non-Mathlib externals:',
      sorted(x for k, v in ext_main.items() if k != 'Mathlib' for x in v))
all_sz = []
for d, _, fs in os.walk(os.path.join(OAI, 'OAI', 'NumberTheory', 'SiegelZeros')):
    for f in fs:
        if f.endswith('.lean'):
            rel = os.path.relpath(os.path.join(d, f), OAI)[:-5].replace(os.sep, '.')
            all_sz.append(rel)
check('closure of OAI.NumberTheory.SiegelZeros.Main = every file of the SiegelZeros directory (306)',
      set(oai_main) == set(all_sz) and len(all_sz) == 306, f'{len(oai_main)} vs {len(all_sz)}')
check('only externals are Mathlib, Lean core (omega) and the 12 patch-added PNT+ modules',
      set(ext_main) <= {'Mathlib', 'Lean'} and len(pnt_main) == 12)
o_thm = {m for m in cl_thm if m.startswith('OAI.')}; o_drzb = {m for m in cl_drzb if m.startswith('OAI.')}
print(f'chain A (Conclusions.Theorem -> exists_absolute_real_zero_gap): {len(o_thm)} OAI modules, '
      f'{lines_of(sorted(o_thm))} lines, PNT+ used: {any(m.startswith("Prime") for m in cl_thm)}')
print(f'chain B (DirichletRealZeroBoundProof -> dirichletRealZeroBound_proof): {len(o_drzb)} OAI modules, '
      f'{lines_of(sorted(o_drzb))} lines, PNT+ used: {any(m.startswith("Prime") for m in cl_drzb)}')
check('the two challenge theorems are proved by module-disjoint chains', not (o_thm & o_drzb),
      f'intersection {len(o_thm & o_drzb)}')

# ---------------------------------------------------------------- (3) token scan
print('\n== (3) comment-stripped token scan of the full closure (318 files)')
TOK = {
    'sorry': r'\bsorry\b', 'admit': r'\badmit\b', 'axiom': r'\baxiom\b',
    'native_decide': r'\bnative_decide\b', 'ofReduceBool/trustCompiler': r'ofReduceBool|trustCompiler',
    'implemented_by': r'implemented_by', '@[extern': r'@\[\s*extern', 'unsafe': r'\bunsafe\b',
    'opaque': r'\bopaque\b', 'skipKernelTC': r'skipKernelTC', 'debug options': r'set_option\s+debug',
    'macro': r'^\s*(?:local\s+|scoped\s+)?macro\b', 'elab': r'^\s*(?:local\s+|scoped\s+)?elab\b',
    'syntax': r'^\s*(?:local\s+|scoped\s+)?syntax\b', 'run_cmd/run_tac/#eval/#exit': r'\brun_cmd\b|\brun_tac\b|#eval\b|#exit\b',
    'initialize': r'^\s*(?:builtin_)?initialize\b', 'open Lean': r'\bopen\s+(?:[A-Za-z.]+\s+)*Lean\b',
    'Lean.Meta/Environment/addDecl': r'\bLean\.(?:Meta|Environment|addDecl)\b', '@[csimp': r'@\[\s*csimp',
}
cnt = collections.Counter(); setopts = collections.Counter()
for m in cl_main:
    s = strip_comments(src_of(m).decode('utf-8'))
    for k, rx in TOK.items(): cnt[k] += len(re.findall(rx, s, re.M))
    for mm in re.finditer(r'set_option\s+(\S+)', s): setopts[mm.group(1)] += 1
print('counts:', dict((k, cnt[k]) for k in TOK))
print('set_option names used:', dict(setopts))
check('no soundness-relevant token in 306 OAI + 12 PNT+ files', sum(cnt.values()) == 0)
check('set_option uses only resource/elaboration limits', set(setopts) <= {'maxHeartbeats', 'maxRecDepth', 'synthInstance.maxHeartbeats', 'linter.unusedVariables', 'linter.style.longLine', 'autoImplicit', 'linter.unusedSectionVars', 'synthInstance.maxSize', 'linter.unusedTactic', 'linter.unnecessarySimpa', 'linter.flexible', 'linter.style.multiGoal', 'linter.style.setOption', 'pp.proofs', 'linter.style.cases', 'linter.style.refine', 'linter.style.induction', 'linter.style.nativeDecide', 'linter.hashCommand', 'linter.style.maxHeartbeats', 'exponentiation.threshold', 'linter.style.emptyLine', 'linter.deprecated', 'backward.isDefEq.lazyWhnfCore', 'linter.unusedSimpArgs', 'backward.isDefEq.lazyProjDelta', 'linter.style.show', 'linter.style.openClassical'}, str(sorted(setopts)))

# ---------------------------------------------------------------- (4) statements
print('\n== (4) statement checks')
def norm(s): return re.sub(r'\s+', ' ', s).strip()
chal = open(os.path.join(OAI, 'ComparatorChallenges', 'SiegelZeros.lean')).read()
cfg = json.load(open(os.path.join(OAI, 'ComparatorChallenges', 'SiegelZeros.json')))
print('challenge sha256', sha(chal.encode()), ' config', json.dumps(cfg, sort_keys=True))
check('challenge imports only Mathlib', imports(chal) == ['Mathlib'])
check('comparator: permitted axioms exactly {propext, Classical.choice, Quot.sound}',
      set(cfg['permitted_axioms']) == {'propext', 'Classical.choice', 'Quot.sound'})
check('comparator: solution module is OAI.NumberTheory.SiegelZeros.Main', cfg['solution_module'] == SZ + 'Main')
print('comparator: enable_nanoda =', cfg['enable_nanoda'], '(no second kernel in the OAI config)')
def body_after(text, head, stop):
    i = text.index(head) + len(head); j = text.index(stop, i); return norm(text[i:j])
c1 = body_after(chal, 'theorem exists_absolute_real_zero_gap :', ':= by')
c2 = body_after(chal, 'theorem WeightedTorusJets.dirichletRealZeroBound_proof :', ':= by')
model = open(os.path.join(OAI, 'OAI/NumberTheory/SiegelZeros/Model.lean')).read()
m1 = body_after(model, 'def UniformSiegelZeroExclusion : Prop :=', '\nend')
t1 = body_after(open(os.path.join(OAI, 'OAI/NumberTheory/SiegelZeros/Conclusions/Theorem.lean')).read(),
                'theorem exists_absolute_real_zero_gap :', ':= by')
p2 = open(os.path.join(OAI, 'OAI/NumberTheory/SiegelZeros/Characters/DirichletRealZeroBoundProof.lean')).read()
s2 = body_after(p2, 'theorem WeightedTorusJets.dirichletRealZeroBound_proof :', ':= by')
check('solution statement 1 is verbatim the challenge statement 1', t1 == c1)
check('Model.UniformSiegelZeroExclusion body is verbatim challenge statement 1 (so `exact` is syntactic)', m1 == c1)
check('solution statement 2 is verbatim the challenge statement 2', s2 == c2)
print('statement 1 (normalized):', c1)
# Mathlib definitions at d13f23b (downloaded files, read as text)
def mfile(p):
    q = os.path.join(MLIB, p.replace('/', '_'))
    return open(q).read() if os.path.exists(q) else None
dc = mfile('Mathlib/NumberTheory/LSeries/DirichletContinuation.lean')
db = mfile('Mathlib/NumberTheory/DirichletCharacter/Basic.lean')
if dc and db:
    print('Mathlib DirichletContinuation sha256', sha(dc.encode()), ' DirichletCharacter/Basic sha256', sha(db.encode()))
    check('Mathlib: LFunction χ s := ZMod.LFunction χ s', 'noncomputable def LFunction (χ : DirichletCharacter ℂ N) (s : ℂ) : ℂ := ZMod.LFunction χ s' in dc)
    check('Mathlib: LFunction = LSeries for 1 < re s, and differentiable on ℂ when χ ≠ 1',
          'lemma LFunction_eq_LSeries (χ : DirichletCharacter ℂ N) {s : ℂ} (hs : 1 < re s)' in dc and
          'lemma differentiable_LFunction {χ : DirichletCharacter ℂ N} (hχ : χ ≠ 1)' in dc)
    check('Mathlib: IsPrimitive := conductor χ = n', 'def IsPrimitive : Prop := conductor χ = n' in db)
else:
    print('Mathlib files not supplied; definitions not checked here')
if os.path.exists(KCHAL):
    k = open(KCHAL).read(); print('Kimura challenge B4ZeroGap.lean sha256', sha(k.encode()))
    kz = norm(k[k.index('theorem zero_gap_all'):k.index(':= by', k.index('theorem zero_gap_all'))])
    need = ['(q : ℕ) [NeZero q] (hq : 3 ≤ q) (χ : DirichletCharacter ℂ q)', '(hreal : ∀ x : ZMod q, (χ x).im = 0)',
            '(hprim : χ.IsPrimitive) (hne : χ ≠ 1) (β : ℝ) (hβ0 : 0 < β)', '(hβ1 : β < 1) (hzero : DirichletCharacter.LFunction χ (β : ℂ) = 0)',
            '(5811/10000000 : ℝ) ≤ (1 - β) * Real.log q']
    check("Kimura's zero_gap_all has the OAI hypotheses with c = 5811/10^7 (hence implies OAI statement 1)",
          all(norm(x) in kz for x in need) and imports(k) == ['Mathlib'])

# ---------------------------------------------------------------- (5) Kimura vendor comparison
print('\n== (5) Kimura v2 (cln-imq-2k v1.4) vendored upstream files vs openai/math @ 4eaee875')
if os.path.exists(KSUMS):
    rows = [l.split(None, 1) for l in open(KSUMS) if l.strip()]
    print('SHA256SUMS sha256', sha(open(KSUMS, 'rb').read()), ' entries', len(rows))
    vend = set(); same = diff = 0; others = collections.Counter()
    for h, rel in rows:
        rel = rel.strip().lstrip('*'); pkg, sub = rel.split('/', 1)
        if pkg == 'openai-math':
            mod = sub[:-5].replace('/', '.'); vend.add(mod); b = src_of(mod)
        elif pkg == 'PrimeNumberTheoremAnd' and sub.startswith('PrimeNumberTheoremAnd/SiegelZeros/'):
            mod = sub[:-5].replace('/', '.'); b = PNT[mod].encode('utf-8') if mod in PNT else None
        else:
            others[pkg] += 1; continue
        if b is not None and sha(b) == h: same += 1
        else: diff += 1
    print(f'compared {same + diff}: identical {same}, different/missing {diff}; not compared (other libraries) {dict(others)}')
    check('all 254 vendored OAI files and 12 PNT+ SiegelZeros files are byte-identical at 4eaee875',
          same == 266 and diff == 0)
    ka, _ = closure(SZ + 'Characters.UnconditionalPrimeBias'); kb, _ = closure(SZ + 'EntireFunctions.RealZeroUniformMasterBound')
    union = {m for m in ka + kb if m.startswith('OAI.')}
    check('vendored OAI set = import closure of {UnconditionalPrimeBias, RealZeroUniformMasterBound}', union == vend,
          f'{len(union)} vs {len(vend)}')
    unc = sorted(set(oai_main) - vend)
    print(f'solution-closure modules outside Kimura\'s checks: {len(unc)} ({lines_of(unc)} lines), e.g.',
          [m.replace(SZ, '') for m in unc if any(x in m for x in ('Main', 'Model', 'Conclusions', 'BezoutBoundary',
                                                                  'GeometricBoundary', 'DirichletRealZeroBound', 'ContrarySequence', 'BoundedConductor'))])
    check('the deep arithmetic core (multiplicity estimate, rectangle span, pivot and master bounds) is vendored',
          all(SZ + x in vend for x in ['Differentials.TorusQuotientDimensionPosCotangentFinrankThree',
                                       'Structure.InvariantJetLinearMap', 'Selection.GlobalRectanglePivotBounds',
                                       'Characters.CharacterGlobalGreedyDeterminantMasterBounds',
                                       'EntireFunctions.RealZeroUniformMasterBound']))
    check('the final assembly modules are NOT vendored (Kimura does not use the OAI final theorem)',
          all(SZ + x not in vend for x in ['Main', 'Model', 'Conclusions.Theorem', 'Characters.DirichletRealZeroBound',
                                           'Characters.DirichletRealZeroBoundProof', 'Estimates.GeometricBoundary']))
else:
    print('Kimura SHA256SUMS not supplied; section skipped')

# ---------------------------------------------------------------- (6) exact arithmetic
print('\n== (6) exact arithmetic: Cor 4 budget, H, thresholds, Lean master-bound constants vs paper (master)')
c0 = Fr(1, 4 * 97 ** 2); C0 = 192
H = 86713344
check('H = 12*C0/c0 = 9216*97^2 = 86713344, i.e. (C0/c0)/H = 1/12 exactly', Fr(C0) / c0 / H == Fr(1, 12) and H == 9216 * 97 ** 2)
check('18818 = 2*97^2 (Kimura: Lemma 6 needs H^(2/3) U >= 2*97^2)', 18818 == 2 * 97 ** 2)
# Cor 4: T1 T2 T3 = 32^3 N^4 ; prod(T_j - 3(N-1)) >= T1T2T3/8 needs T_j >= 6(N-1) (true since T_j >= 32N)
check('Cor 4: 32^3/8 = 4096 and 4096 N^4 > (4N-3)^4 for N = 1..10^5 (and 4096 > 4^4 for all N)',
      32 ** 3 // 8 == 4096 and all(4096 * N ** 4 > (4 * N - 3) ** 4 for N in range(1, 100001)))
r = Fr(1, 12)                         # S2/S1 <= 1/12
check('13/16 = (3/4)(1+1/12)', Fr(3, 4) * (1 + r) == Fr(13, 16))
check('13/24 = (1/2)(1+1/12)  [coefficient of l/log U]', Fr(1, 2) * (1 + r) == Fr(13, 24))
check('13/12 = 1+1/12  [coefficient of log 8 / log U]', 1 + r == Fr(13, 12))
check('13/16 + 1/16 = 7/8 < 1 (the contradiction of the paper and of the Lean master bound)', Fr(13, 16) + Fr(1, 16) == Fr(7, 8))
# last terms: (C M U + 1/2 M log M)/(S1 log U) with S1 >= M D U, D = H^{2/3}/(4*97^2), log M = 3 log U
import sympy as sp
Ms, Us, Ds, Cs, Ls = sp.symbols('M U D C L', positive=True)
S1 = Ms * Ds * Us
lhs = (Cs * Ms * Us + sp.Rational(1, 2) * Ms * 3 * Ls) / (S1 * Ls)
check('(C M U + (1/2) M log M)/(S1 log U) = C/(D log U) + 3/(2 D U) at S1 = M D U, log M = 3 log U',
      sp.simplify(lhs - (Cs / (Ds * Ls) + sp.Rational(3, 2) / (Ds * Us))) == 0)

# ---------------------------------------------------------------- (7) toy certificates (mod p)
print('\n== (7) toy certificates for the Lean form of Cor 4 (rank mod p <= rank over K, so full rank mod p certifies span)')
import numpy as np
def is_prime(n):
    if n < 2: return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0: return n == q
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True
def split_prime(d, start=2_000_000_000):
    p = start
    while True:
        p -= 1
        if p % 8 == 7 and is_prime(p) and pow(d % p, (p - 1) // 2, p) == 1:
            return p
def rank_mod_p(Mx, p):
    A = Mx.copy() % p; rows, cols = A.shape; r = 0
    for c in range(cols):
        piv = None
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0: continue
        piv = r + nz[0]
        if piv != r: A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        f = A[:, c].copy(); f[r] = 0
        nzr = np.nonzero(f)[0]
        if len(nzr):
            A[nzr] = (A[nzr] - (f[nzr, None] * A[r][None, :]) % p) % p
        r += 1
        if r == rows: break
    return r
def theta_mod(d, N, p):
    sd = pow(d % p, (p + 1) // 4, p); s2 = pow(2, (p + 1) // 4, p)
    assert sd * sd % p == d % p and s2 * s2 % p == 2
    pts = list(itertools.product(range(N), repeat=4))
    th = np.array([(n0 + n1 * sd + n2 * s2 + n3 * sd * s2) % p for n0, n1, n2, n3 in pts], dtype=np.int64)
    sg = np.array([(n0 - n1 * sd + n2 * s2 - n3 * sd * s2) % p for n0, n1, n2, n3 in pts], dtype=np.int64)   # sigma: a->-a
    st = np.array([(n0 - n1 * sd - n2 * s2 + n3 * sd * s2) % p for n0, n1, n2, n3 in pts], dtype=np.int64)   # sigma tau: a->-a, b->-b
    return th, sg, st
def powtab(v, m, p):
    T = np.ones((m + 1, len(v)), dtype=np.int64)
    for e in range(1, m + 1): T[e] = (T[e - 1] * v) % p
    return T
def rect_rows(th, sg, st, a0, a1, a2, p):
    P0, P1, P2 = powtab(th, a0, p), powtab(sg, a1, p), powtab(st, a2, p)
    out = []
    for i in range(a0 + 1):
        for j in range(a1 + 1):
            pj = (P0[i] * P1[j]) % p
            for k in range(a2 + 1): out.append((pj * P2[k]) % p)
    return np.array(out, dtype=np.int64)
toy_ok = True; kappa_rows = []
for d in (-1, 5):
    p = split_prime(d)
    for N in (2, 3, 4):
        th, sg, st = theta_mod(d, N, p)
        M = N ** 4
        distinct = len(set(th.tolist())) == M
        vand = rank_mod_p(powtab(th, M - 1, p), p) == M if distinct else False
        toy_ok &= vand
        for Hh in range(1, N + 1):
            u = N ** (4 / 3)
            def spans(kap):
                a0 = int(kap * Hh ** (2 / 3) * u); a12 = int(kap * Hh ** (-1 / 3) * u)
                if (a0 + 1) * (a12 + 1) ** 2 < M: return False
                return rank_mod_p(rect_rows(th, sg, st, a0, a12, a12, p), p) == M
            # the Lean thresholds themselves (kappa = 32): certified via the Vandermonde sub-block when T1 >= M-1,
            # otherwise by direct rank
            T1 = 32 * Hh ** (2 / 3) * u
            lean_ok = vand if T1 >= M - 1 else spans(32.0)
            toy_ok &= lean_ok
            lo, hi = 0.0, 32.0
            for _ in range(14):
                mid = (lo + hi) / 2
                if spans(mid): hi = mid
                else: lo = mid
            kappa_rows.append((d, N, Hh, p, lean_ok, round(hi, 3)))
print(' d   N  H  p           Lean-rectangle spans   kappa* (upper bound, mod p)')
for row in kappa_rows: print('%3d %3d %2d  %d  %-22s %s' % row)
check('Lean-form Cor 4 rectangles (kappa = 32) span for d in {-1,5}, N <= 4, 1 <= H <= N; Vandermonde rows span', toy_ok)
check('minimal scale kappa* <= 4 in every toy case (32 has a factor >= 8 of slack there)', max(r_[5] for r_ in kappa_rows) <= 4,
      f'max kappa* = {max(r_[5] for r_ in kappa_rows)}')

# ---------------------------------------------------------------- (8) duality identity
print('\n== (8) (D1^a1 D2^a2 D3^a3 x^n)(1,1,1,1) = (A n)^alpha for D_j = sum_i A_ji x_i d/dx_i')
xs = sp.symbols('x0:4'); A = sp.Matrix([[1, 2, -1, 3], [0, 1, 4, -2], [5, -1, 1, 1]])
def Dj(j, f): return sp.expand(sum(A[j, i] * xs[i] * sp.diff(f, xs[i]) for i in range(4)))
ok = True
for n in [(0, 0, 0, 0), (1, 0, 2, 1), (2, 1, 0, 3), (3, 3, 1, 2)]:
    mono = sp.Mul(*[xs[i] ** n[i] for i in range(4)])
    An = [sum(A[j, i] * n[i] for i in range(4)) for j in range(3)]
    for al in [(0, 0, 0), (1, 0, 0), (0, 2, 1), (2, 1, 3), (1, 1, 1)]:
        f = mono
        for j in (2, 1, 0):
            for _ in range(al[j]): f = Dj(j, f)
        ok &= (f.subs({x: 1 for x in xs}) == An[0] ** al[0] * An[1] ** al[1] * An[2] ** al[2])
check('duality identity on 20 (n, alpha) pairs (exact, sympy)', ok)

print('\nSUMMARY: %d PASS / %d FAIL, %.1f s' % (sum(o for _, o in RESULTS), sum(not o for _, o in RESULTS), time.time() - T0))
