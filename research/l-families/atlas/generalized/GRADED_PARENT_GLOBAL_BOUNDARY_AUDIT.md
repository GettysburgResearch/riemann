# Independent review: graded parents and global analytic boundaries

Reviewed scientific source: 334bec3b0ddd20dfc42218bcfe5603890b381195.

Reviewer: /root/completion_rigidity_scout, independent of the packet author.
Review branch: codex/graded-parent-global-boundary-audit, based on that exact
scientific source. The five source files and main branches were not edited.

Verdict: PASS in the stated identity-Satake scalar, fixed-parameter, and
ordinary finite-gamma same-center scopes. No scientific repair is required.
The infinite statements were reconstructed from their written proofs and
declared classical inputs; the bounded computations do not certify them.

## 1. Exact source identity

The complete mathematical note, producer, tests, source manifest, and both
declared parent notes were read. The whole JSON fixture was parsed and compared
against a complete authenticated rebuild, not sampled or checked only by hash.
The following Git blobs and LF-normalized SHA-256 values were independently
obtained from the frozen Git source and compared with the current source bytes.

All paths below except the test are under
research/l-families/atlas/generalized/.

| File | Frozen Git blob | SHA-256 after LF normalization |
|---|---|---|
| GRADED_PARENT_GLOBAL_BOUNDARY.md | 1a49f7075b590e16c8367c7b2ef8b8d5b77c9819 | c545339d97aead843ed6591a8a2b8dadc27e0518607fa03b4d7d68b088ec1eef |
| graded_parent_global_boundary.py | 17ff46a48fc1fb4bbb0d4e42a4af46605eb598e7 | 716c25f10f86ac10d759d7464e2c0d58b31642db42b5b0c15a8569c78976c9ca |
| graded_parent_global_boundary.json | 4770ab91560e779c8f5972a71bcc62c953e80ca9 | d8a705c624c52eecd8221d066a737cdbca5377bf95b4159fb4ca7b5318332e01 |
| graded_parent_global_boundary.sources.json | 2526528722b7247e43dbbf33a81539a7deb03dff | 7a18134dd183398954b49f7f12e8cc822006af8341805b055e707e0ce0e448d8 |
| tests/test_graded_parent_global_boundary.py | fa53727f771220104e7faed31423a2fe23fd9d30 | 19adc76da6f5500aa30f15816a42cf3a8ef36dea53b90b9b4db66b4408a58b52 |

The exact fixture payload is
030c2d17778cf29e7ac459b8330424caa8b5bc08fe0a5ea139578fe98dd8d1b2.

The parent source is e2f469142cd55086e74751293877ab533001e786. Its proof
FINITE_GRADED_VIRTUAL_PARENT_CLASSIFICATION.md has blob
3932273279d43ffa34d929247152cb43b932fa1d and LF SHA-256
50daa223c5b6d0f061d771f24775a0a7a2d470f9185a1d6304f3b49e9fc799bc.
Its independent review has blob c6a9b701f6c4cd410e7dd6b67d6d7d22431f6ce3
and LF SHA-256
a67a1a901cc33f8c42059351325ffc5c8358bb8b2acf2433944676bab45e50d7.
The producer authenticates these frozen blobs and their unchanged current
bytes before accepting a rebuilt fixture.

Issue #764 and overlapping open PRs were inspected read-only before the
review. No issue, PR, or remote branch was changed.

## 2. Independent mathematical reconstruction

The frozen parent gives a self-contained strict interlacing induction.
Applying (T d/dT+j)/j to H/(1-T)^d produces the numerator

    ([j+(d-j)T]H + T(1-T)H')/j.

At every later step the new leading coefficient is positive. The alternating
nonzero values at the old negative roots, the positive constant coefficient,
and the sign at negative infinity produce every required new negative root.
The degree count exhausts the roots and proves simplicity. Thus the global
packet legitimately uses distinct positive reciprocal-root magnitudes B_i;
it is not extrapolating a Sturm census.

The actual local divisor coefficients grow polynomially in the exponent at
a fixed prime. Their local tails are uniformly O(p^(-sigma)) on every real
half-line sigma>=sigma_0>1. Positivity, multiplicativity, and absolute
convergence give the ordinary Dirichlet series and Euler product on Re s>1.
This conclusion supplies no zero-free region.

With a=n-1, the first-coefficient excess is

    h_1-2q=(a+1)^k-(3k-2)a-1.

At k=2 it is a(a-2), and at a=1,k=3 it is zero. Its increment in k is
a((a+1)^k-3)>0 in the remaining stated ranges. Equality is exactly at
(3,2) and (2,3). There are at least two distinct B_i outside (2,2), so
A=max B_i exceeds their average and is strictly greater than two.

The one-variable Estermann theorem therefore applies to H in Z[T],
H(0)=1, with reciprocal parameters -B_i. It gives meromorphic continuation
to Re s>0 and prohibits meromorphic extension at every point of Re s=0.
Dividing a hypothetical continuation by a nonzero meromorphic germ of
zeta(s)^d, or of an allowed completion multiplier, is legitimate even at
zeros or poles of that germ. An ordinary same-center functional equation
on the overlapping critical strip would glue the known right-half-plane
function to its reflected continuation across Re s=0. Thus it is excluded;
this implication does not require assuming global continuation in advance.

For D_(2,2), the halving proof is sound. Every nontrivial zero reaches a
terminal zero rho with zeta(rho/2) nonzero, since otherwise zeros accumulate
at zero where zeta is nonzero. If the set of terminals were finite, every
zero would be 2^j times a terminal, and positivity of its real part would
bound j separately for each terminal. This contradicts infinitude of the
nontrivial zeros. Hence infinitely many genuine poles of D_(2,2) lie in
0<Re s<1/2, whereas the open right half-strip is holomorphic.

A nonzero multiplier with only finitely many zeros and poles in the open
critical strip preserves this infinite/finite pole asymmetry. A finite
ordinary gamma quotient with real nonzero slopes has only finitely many
divisor points there, including when its shifts are complex. Neither
conjugate reflection nor plain reflection can hold. No RH, simplicity,
zero-counting asymptotic, or assumption that every scaled zero survives is
used. Arbitrary meromorphic multipliers are not covered: the arithmetic
factor zeta(2s) really can cancel the obstructing denominator.

The logarithmic derivative and Mobius inversion give

    b_m=d+(-1)^(m+1) sum_i B_i^m,
    m w_m=sum_(r|m) mu(r)b_(m/r).

For m>1 the constant d cancels. Separating the dominant root and the divisor
r=1 yields the stated error with beta=max(1,B_2)<A; every proper divisor
exponent is at most m/2. Consequently the eventual alternating sign and
exponential dimension growth follow for each fixed pair. They do not imply
effectivity of a positive-dimensional virtual representation.

For |T|<1 the chosen local logarithms have leading term T^m. On |T|=1/A
the absolute grade terms are asymptotic to 1/m. Their complex harmonic main
term converges except at T=-1/A; at that point it tends to minus infinity,
and the corresponding positive partial products tend to zero. This is a
boundary of a logarithmic expansion, not of the rational local function.

On the real global half-line, log zeta(m sigma)=2^(-m sigma)+O(3^(-m sigma)).
The real endpoint sigma_*=log_2 A has an alternating harmonic main term and
an absolutely summable remainder, so convergence there is conditional.
Uniform control from above gives exactly log D(sigma_*), not merely some
unspecified boundary value. Below this endpoint but above one the terms
fail the necessary zero-limit test. The prime-two complex zeros are also
valid: at the listed points its argument is -1/A, all larger-prime arguments
have smaller modulus, and their remaining product is nonzero.

The centered-grade control changes the arithmetic object. Reflection of
ds+c forces c=(1-d)/2. Using the usual completed zeta then gives the stated
meromorphic functional equation for zeta(s)^4/zeta(2s-1/2), with multiplier

    pi^(-s-1/4) Gamma(s/2)^4 / Gamma(s-1/4).

Its coefficient at p^2 is 10-sqrt(p), not nine. Dividing its absolute value
by p^(2 epsilon) tends to infinity for every 0<epsilon<1/4. An exact
functional equation for this changed meromorphic toy does not establish
Ramanujan, positivity, automorphy, or membership in the Selberg class.

## 3. Primary inputs checked

The exact one-variable statement in
[Delabarre, Section 1.2, printed p.227](https://www.numdam.org/item/10.24033/bsmf.2647.pdf)
was inspected: integer polynomial, constant coefficient one, continuation
to Re s>0, and every-point meromorphic natural boundary unless every
reciprocal parameter has modulus one. No multivariable regularity or
nondegenerate-face hypothesis is imported.

[Dahlquist's original paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/6867-11512_2007_Article_BF02591361.pdf)
was read at printed pp.534-537. The warning about the unmodified zeta product
is in Section 1.2 p.534; the elementary local factorization and Mobius
transform are on p.535, and the small-prime separation leading to Lemma 2.1
appears on pp.536-537. This is established prior art, not a novelty claim.
The PDF was downloaded into memory only after the browser fetch failed.

The zeta zero and pole facts were checked against
[DLMF 25.10](https://dlmf.nist.gov/25.10),
[25.6.1](https://dlmf.nist.gov/25.6.E1), and
[25.2](https://dlmf.nist.gov/25.2).
Gamma divisor locations agree with [DLMF 5.2](https://dlmf.nist.gov/5.2).
The centered completion agrees with [DLMF 25.4](https://dlmf.nist.gov/25.4);
the factor s(s-1)/2 distinguishing xi from Lambda is itself reflection
invariant. These external facts were checked by the reviewer, not
machine-proved or authenticated by downloaded-byte hashes.

## 4. Exact replay and independent finite checks

In the isolated audit worktree, all four commands below passed at the
scientific source. Both checkers returned the exact payload above; each
unit-test run passed all 25 tests.

    python -B research/l-families/atlas/generalized/graded_parent_global_boundary.py --check
    python -B -O research/l-families/atlas/generalized/graded_parent_global_boundary.py --check
    python -B -m unittest discover -s tests -p test_graded_parent_global_boundary.py
    python -B -O -m unittest discover -s tests -p test_graded_parent_global_boundary.py

These also passed:

    python -m ruff check research/l-families/atlas/generalized/graded_parent_global_boundary.py tests/test_graded_parent_global_boundary.py
    python -m ruff format --check research/l-families/atlas/generalized/graded_parent_global_boundary.py tests/test_graded_parent_global_boundary.py
    git diff --check

The independent in-memory script in the appendix passed under python -B -
and python -B -O -. It uses explicit failure checks, not assert. Its results:

- 30 complete rows at grade 32: 990 direct series coefficients and 960
  reciprocal-root power sums and graded dimensions each.
- Numerators reconstructed by the differential operator, not the producer's
  finite differences; divisor coefficients by repeated prefix sums.
- Power sums computed as traces of powers of the reciprocal-root companion
  matrix, not Newton's recurrence. Mobius values and divisors come separately
  from SymPy. Full direct graded products reconstruct the original series.
- 125 signed-grade panels, each through grade 20, checked against both
  producer extraction algorithms.
- 125 arbitrary integer cubics, including sign changes, repeated roots,
  nonreal roots, constants after trimming, and zero coefficients, checked
  against companion-matrix traces through order 16.
- 21 hostile input/cap rejections and five source-mismatch rejections.
  The maximal work score is 21572200; equality to the cap is rejected,
  while its successor is accepted.

The source mismatch controls independently reject a wrong Git blob, oversized
frozen blob, wrong frozen bytes, wrong current bytes, and promotion of an
external theorem to machine-proved metadata. Input controls include Boolean,
float, nonintegral type, oversized integer/rational, raw trailing malformed
coefficient, duplicate point/key, nonfinite JSON, and typed JSON mismatches.
An overflowing JSON exponent is rejected by canonical comparison even
though the JSON parser itself represents it as infinity.

The score is a declared bounded-work preflight, not an elapsed-time or RAM
certificate. Hard parameter, byte, bit, and degree limits remain separately
enforced. Exact source/algebra replay must not be confused with verification
of analytic continuation or actual zeta-zero data.

## 5. Review boundary

This review accepts the scalar identity specialization and its explicit
completion class. It does not classify nonidentity Satake families, arbitrary
dual Euler products, arbitrary arithmetic multipliers, or infinite regularized
completions. It does not prove RH, GRH, an automorphic realization, a new
L-function, or unexplored mathematical priority.

The proof and control source files remain unchanged. This separate review
adds only its own audit note. The author may import the reviewed source and
this review with their distinct identities; the review must not be silently
attached to any later repair.

## Appendix: independent in-memory replay

Run the following Python block from the audit worktree root, supplying it on
standard input to python -B - and again to python -B -O -. It reads the five
frozen files, invokes Git read-only, and uses in-memory mocks; it writes no
files. SymPy is used only for exact integer Mobius values and divisors.

```python
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from math import prod
from unittest import mock
import hashlib, importlib.util, json, subprocess
import sympy as sp

root = Path.cwd()
path = root / "research/l-families/atlas/generalized/graded_parent_global_boundary.py"
spec = importlib.util.spec_from_file_location("reviewed_global", path)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def ck(value, label):
    if not value:
        raise RuntimeError(label)

def fails(call, label):
    try:
        call()
    except (ValueError, subprocess.CalledProcessError):
        return
    raise RuntimeError("accepted " + label)

def trim(h):
    while len(h) > 1 and h[-1] == 0:
        h.pop()
    return tuple(h)

def differential(n, k):
    h, d = [Q(1)], 1
    for _ in range(k):
        for j in range(1, n):
            extended = h + [Q(0)]
            out = []
            for r in range(len(extended)):
                previous = extended[r-1] if r else Q(0)
                out.append(((j+r)*extended[r]+(d-j-r+1)*previous)/j)
            h, d = list(trim(out)), d+1
    ck(all(x.denominator == 1 for x in h), "integer differential numerator")
    return tuple(int(x) for x in h), d

def prefix_coefficients(n, k, order):
    f = [1]*(order+1)
    for _ in range(n-1):
        for j in range(1, order+1):
            f[j] += f[j-1]
    return tuple(x**k for x in f)

def companion_traces(raw, order):
    h = trim(list(raw))
    q = len(h)-1
    if not q:
        return (0,)*order
    last = [-((-1)**(q-i))*h[q-i] for i in range(q)]
    power = [[int(i == j) for j in range(q)] for i in range(q)]
    traces = []
    for _ in range(order):
        power = [[(power[i-1][j] if i else 0)+last[i]*power[q-1][j]
                  for j in range(q)] for i in range(q)]
        traces.append(sum(power[i][i] for i in range(q)))
    return tuple(traces)

def direct_product(weights, order):
    values = [1]+[0]*order
    for grade, weight in enumerate(weights, 1):
        factor = [1]
        for j in range(1, order//grade+1):
            top = factor[-1]*(weight+j-1)
            ck(top % j == 0, "factor integrality")
            factor.append(top//j)
        values = [sum(values[t-j*grade]*factor[j]
                      for j in range(t//grade+1))
                  for t in range(order+1)]
    return tuple(values)

rows = 0
for n in range(1, 6):
    for k in range(6):
        h, d = differential(n, k)
        row = m.row_control(n, k, 32)
        ck(h == row["H"] and d == row["denominator_power"], "differential versus finite differences")
        f = prefix_coefficients(n, k, 32)
        ck(f == row["coefficients"], "prefix series")
        sums = companion_traces(h, 32)
        ck(sums == row["reciprocal_root_power_sums"], "companion traces")
        b = [d+(-1)**(j+1)*sums[j-1] for j in range(1, 33)]
        weights = []
        for j in range(1, 33):
            total = sum(int(sp.mobius(r))*b[j//r-1] for r in sp.divisors(j))
            ck(total % j == 0, "Mobius integrality")
            weights.append(total//j)
        ck(tuple(weights) == row["formal_graded_dimensions"], "independent Mobius weights")
        ck(direct_product(weights, 32) == f, "direct product reconstruction")
        rows += 1

signed = 0
for a, b, c in product(range(-2, 3), repeat=3):
    weights = (a, 0, b, 0, 0, c)+(0,)*14
    f = direct_product(weights, 20)
    ck(m.euler_weights(f) == weights, "signed Euler")
    ck(m.triangular_weights(f) == weights, "signed triangular")
    signed += 1

polys = 0
for a, b, c in product(range(-2, 3), repeat=3):
    h = (1, a, b, c)
    ck(m.newton_sums(h, 16) == companion_traces(h, 16), "non-root-restricted Newton")
    polys += 1

hostile = [
    lambda: m.numerator(False, 3), lambda: m.coefficients(3, Q(2), 5),
    lambda: m.row_control(5, 6, 32), lambda: m.newton_sums((1, -1, False), 0),
    lambda: m.newton_sums((1, 0, Q(0)), 4),
    lambda: m.polynomial([1]+[0]*16+[False]),
    lambda: m.series([1]+[0]*31+[1 << 128]),
    lambda: m.triangular_weights((1, -(1 << 128))),
    lambda: m.arithmetic(-(1 << 4096)),
    lambda: m.rational(Q(1, 1 << 128)),
    lambda: m.centered_grade(Q(2)),
    lambda: m.halving_forest(((Q(1, 3), 1), (Q(1, 3), 1))),
    lambda: m.halving_forest(((Q(1, 1 << 128), 1),)),
    lambda: m.pole_order(1, Q(0)),
    lambda: m.strict_json(b'{"x":1,"x":false}'),
    lambda: m.strict_json(b'{"x":NaN}'),
    lambda: m.strict_json(b" "*(m.MAX_BYTES+1)),
    lambda: m.same_json(m.strict_json(b'{"x":1e999}'), {"x":1}),
    lambda: m.same_json({"x":1}, {"x":True}),
    lambda: m.same_json({"x":1}, {"x":1.0}),
]
for j, call in enumerate(hostile):
    fails(call, "hostile " + str(j))
score = m.preflight(5, 5, 32)
fails(lambda: m.preflight(5, 5, 32, score), "cap equality")
ck(m.preflight(5, 5, 32, score+1) == score, "cap successor")

realrun = m.subprocess.run
mutations = {"rev-parse": b"0"*40+b"\n",
             "cat-file": str(m.MAX_BYTES+1).encode()+b"\n",
             "show": b"wrong frozen bytes"}
for command, replacement in mutations.items():
    def altered(args, *args2, command=command, replacement=replacement, **kwargs):
        if args[1] == command:
            return subprocess.CompletedProcess(args, 0, stdout=replacement, stderr=b"")
        return realrun(args, *args2, **kwargs)
    with mock.patch.object(m.subprocess, "run", side_effect=altered):
        fails(m.source_locks, "source " + command)

realread = m.bounded_bytes
livepath = root / m.SOURCE_ROWS[0][0]
def changed_live(p):
    raw = realread(p)
    return raw+b"changed" if p == livepath else raw
with mock.patch.object(m, "bounded_bytes", side_effect=changed_live):
    fails(m.source_locks, "source current bytes")
manifest = m.expected_manifest()
manifest["external_theorems_machine_proved"] = True
with mock.patch.object(m, "bounded_bytes", return_value=m.canonical(manifest)):
    fails(m.source_locks, "external theorem promotion")

source = "334bec3b0ddd20dfc42218bcfe5603890b381195"
paths = [
    "research/l-families/atlas/generalized/GRADED_PARENT_GLOBAL_BOUNDARY.md",
    "research/l-families/atlas/generalized/graded_parent_global_boundary.py",
    "research/l-families/atlas/generalized/graded_parent_global_boundary.json",
    "research/l-families/atlas/generalized/graded_parent_global_boundary.sources.json",
    "tests/test_graded_parent_global_boundary.py",
]
identities = {}
for p in paths:
    raw = subprocess.check_output(["git", "show", source+":"+p], cwd=root)
    live = (root/p).read_bytes()
    normalize = lambda data: data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    ck(normalize(live) == normalize(raw), "frozen file " + p)
    identities[p] = {
        "blob": subprocess.check_output(["git", "rev-parse", source+":"+p], cwd=root).decode().strip(),
        "sha256_lf": hashlib.sha256(normalize(raw)).hexdigest(),
    }
report = m.build_report()
payload = report["payload_sha256"]
ck(payload == "030c2d17778cf29e7ac459b8330424caa8b5bc08fe0a5ea139578fe98dd8d1b2", "payload identity")
print(json.dumps({"status":"PASS", "rows_order32":rows,
 "direct_series_cells":rows*33, "newton_and_grade_cells_each":rows*32,
 "signed_grade_panels":signed, "general_integer_polynomials":polys,
 "hostile_input_rejections":len(hostile)+1, "source_mismatch_rejections":5,
 "max_work_score":score, "payload":payload, "identities":identities},
 sort_keys=True, indent=2))
```
