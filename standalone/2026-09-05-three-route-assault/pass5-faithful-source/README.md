# Fifth continuation: faithful growing-degree arithmetic

**PROPOSED COMPLETE COMPONENT PROOFS; independent review required. RH, the
all-degree signed energy bound, and all-order matrix positivity remain open.**

Parent: PR #793 at `6ebbe5efe6430584736649b87495af2be073f693`.
Directory: `standalone/2026-09-05-three-route-assault/pass5-faithful-source/`.
Both fourth-pass contributions are preserved: the raw prime-cutoff study and
the separately imported signed-energy packet. No inherited file is changed.

## What this pass completes

### A uniform, faithful Mobius cutoff

For EVERY |b(k)|<=1, simultaneously through degree N,

    |sum_(k>2^(11N)) b(k)k^(-3/2)L_n(2log k)|
      <= (544/195)2^(-7N/34),       0<=n<=N.

This removes the previously exhibited false convergence caused by dropping
a growing-degree arithmetic tail. The squared energy of the resulting
finite Mobius sum has the same exponential growth rate as the full source.
The sharp universal absolute-tail slope is C_*=7.177988363... for cutoffs
exp(CN); its exact definition and rational enclosure are supplied. Near
this threshold the lower bound already holds for the fixed positive
squarefree source, not a degree-dependent adversarial vector.

See [SHARP_ARITHMETIC_CUTOFF.md](SHARP_ARITHMETIC_CUTOFF.md).

### A short source computation that keeps the infinite tail

The large raw cutoff need NOT be enumerated to compute the actual
coefficients. At fixed safe Cayley disks, retain an integer sum only through

    K-1=2N+2ceil(B/4)+10,

add M=N+ceil(B/4)+4 Euler--Maclaurin terms, and retain the proved analytic
remainder. The entire required disk has remainder <=4/36^M. Cauchy and a
zero-free SAFE-half-plane denominator bound then certify every Mobius
coefficient through N with analytic error <2^(-N-B-13).

The same construction supplies completed-xi logarithmic-derivative jets
with explicit errors. These feed both the invariant moment matrices and
the fixed Hardy matrices; no zeta-zero data is used. This is a quantitative
specialization of classical Euler--Maclaurin and Cauchy methods, not a new
claimed special-function algorithm or a linear-time claim.

See [SOURCE_COMPILER.md](SOURCE_COMPILER.md).

## Actual finite certificates executed

The standard-library-only producer [compile_source.py](compile_source.py)
reconstructs [SOURCE_RESULTS.json](SOURCE_RESULTS.json):

- a_0,...,a_12 for literal 67-free Mobius, with N=12,B=96,M=40,K=83;
  the retained integer sum has 82 terms. The infinite analytic tail is paid.
- Ten invariant log moments at s=2. Both five-by-five moment matrices have
  five strictly positive rational interval LDL pivots. This gives positive
  five-node resolvent quadrature matching ten moments, NOT a rank-five
  ordinary determinant.
- The full eight-by-eight Hardy compression in the parent's fixed Laguerre
  basis has eight strictly positive interval LDL pivots. Its final pivot is
  approximately 2.4623564e-21.

These eighteen signs concern those stated FINITE matrices. They do not imply
positivity at an unbounded rank. The generic source compiler is an accurate
way to pose that problem, not a solution of its sign.

## Route status

Route 1 retains the fixed unshifted Hankel endpoint. This pass supplies ten
certified moments and the five-node positive resolvent, without imposing
integer weights prematurely.

Route 2 gains a faithful cofinal finite-arithmetic target, an optimal
universal tail cost, and an efficient alternative source evaluation. The
actual assembled energy is NOT proved subexponential at all degrees.

Route 3 gains the same certified safe-source engine and an explicit
4d*eps operator-error budget from d scalar coefficient errors. Full-source
8-by-8 positivity is certified; the all-rank lower bound remains open.

No route is dropped. Raw-cutoff impossibility does not mean that retaining
a rigorously bounded analytic tail is impossible: this packet implements
the latter distinction rather than repeating the false truncation.

## Replay and trust boundary

From this directory:

```sh
python compile_source.py --check SOURCE_RESULTS.json
python -O compile_source.py --check SOURCE_RESULTS.json
python -m unittest -v test_source
python -O -m unittest -v test_source
sha256sum -c SHA256SUMS
```

All fourteen tests and both fresh source reconstructions pass. The latter
outputs are byte-identical. Two deliberate saved-result corruptions are
rejected, one in each Python mode. The analytic proof is not machine-proved
by these controls. A separate optional [regression.py](regression.py) checks
seven Mobius coefficients, three moments and three Hardy source coefficients
using 110-digit mpmath. It is explicitly non-directed and not a proof input.

The source and review ledger, failed continuation step, resource caps, and
scope of the optional numerical check are in
[REVIEW_AND_VALIDATION.md](REVIEW_AND_VALIDATION.md). No Lean build, broad
prime/zero scan, independent referee acceptance, or remote CI success is
claimed. Finite positivity and an accurate coefficient algorithm are not RH.
