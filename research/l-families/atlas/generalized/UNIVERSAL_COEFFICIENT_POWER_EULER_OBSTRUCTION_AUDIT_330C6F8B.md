# Independent audit of the universal coefficient-power Euler packet

Audited mathematical source: **`330c6f8b85fa1923f2d4914ce3ab1775b0e56c75`**.

Source note: `UNIVERSAL_COEFFICIENT_POWER_EULER_OBSTRUCTION.md`, with its
producer, canonical JSON, source manifest, and eleven original unit tests.
The audit used a separate worktree; the frozen source and main were not edited.

Verdict: **the four local mathematical statements pass in their stated
scope; release metadata and lint require the separate repair accompanying
this report.** No universal or global conclusion is inferred from finite
tests. RH and GRH remain unproved.

## 1. Mathematical findings

| statement | exact audit result |
|---|---|
| universal finite virtual-representation obstruction | PASS for `n>=2,k>=2`; at the identity, first degree forces virtual dimension `n^k`, while either the pole order or the positive second-jet defect contradicts the proposed Euler factor |
| Zariski-dense extension | PASS for algebraic representations of `GL_n`; every formal coefficient is regular on that group, so dense equality reaches the identity |
| multiset-Eulerian numerator | PASS, including empty alphabet and zero multiplicity; the stable-sort map and its inverse preserve precisely the required strict increases |
| exact numerator degree | PASS: strictly decreasing runs give at least `n-1` runs, and repeated descending alphabet blocks attain `(k-1)(n-1)` descents |
| balanced power-trace exponential | PASS: `End(V)^tensor_m` is a genuine algebraic representation; its invariant trace pairing, determinant one, scalar-twist blindness, and formal logarithmic determinant identity are exact |
| degree versus recurrence order | PASS with the compact-unitary dense-orbit hypothesis for the absolute-trace scalar sequence; the Euler denominator retains all `n^(2m)` multiplicities even at collisions |

The no-go permits arbitrary finite virtual differences, not just actual
representations or tensor powers. Negative virtual dimensions cannot evade
the first coefficient at the identity. The decomposition of
`Sym^2(V^tensor_k)` into even numbers of exterior-square factors correctly
explains the positive defect but is not needed to exclude other candidates.

All excluded chambers are genuine exceptions. For `k=0`, the operation is
the polynomial constant one, including when a complete symmetric coefficient
vanishes. For `k=1` it is the standard Euler factor. For `n=1` it is the
character `z -> z^k`. The stable-sort proof also handles `k=0`, `n=1`, and
the resulting single empty word without using a negative degree formula.

The constructive result changes the coordinate being transformed: it uses
power traces and their formal exponential, not the coefficientwise power of
the original determinant inverse. Unitarity is essential for replacing the
algebraic trace pair by an absolute value. The self-duality is a bilinear
representation-theoretic statement and does not assume every complex matrix
is unitary.

## 2. Release findings and separate repair

The original frozen producer and all eleven original tests passed in normal
and optimized Python. The original Ruff run failed on five diagnostics:
`UP033`, `TRY004`, `RUF007`, and two instances of `SIM117`.

Its arithmetic-class value `EXACT_INTEGER_AND_RATIONAL` was not one of the
repository's accepted classes. The repair uses `MIXED`, with explicit
`CERTIFIED_INTEGER_COVERAGE` and `EXACT_RATIONAL` components and a no-rounding
contract. This changes taxonomy, not the computed arithmetic.

The repair also makes **compact unitary torus** explicit in the imported
absolute-trace recurrence sentence. The frozen source note already defines
that domain, and the original packet's unitarity firewall was correct; this
is clarification, not a strengthening or correction of its algebraic
power-trace theorem.

Lint repairs, formatting, and regenerated content hashes accompany these
changes. No mathematical formula, parameter rectangle, resource ceiling,
source commit, or source manifest is relaxed. The repair has its own Git
identity and does not rewrite the reviewed source.

## 3. Additional independent exact controls

Three new tests bring the packet to fourteen tests:

1. Explicitly enumerate weak-list systems, perform stable sorting, invert
   the map, and count every observed word's admissible value sequences.
   Cases include zero multiplicity and an empty alphabet.
2. Use the invertible matrix `diag(1,-1)`, whose odd complete symmetric
   coefficients vanish, to check the polynomial zero-power convention.
3. Construct non-diagonal `End` matrices directly, independently of the
   producer's weight expansion. The inputs are a unipotent Jordan matrix,
   `[[2,1],[1,1]]`, and the unitary rotation `[[0,-1],[1,0]]`.

The matrix test checks the invariant trace-pairing Gram matrix, exact scalar
twists, power traces through the full dimensions four and sixteen, and all
Newton determinant coefficients. The top coefficient remains one. The
unipotent case gives `(1-T)^N`. The finite unitary orbit gives
`(1-T^2)^(N/2)`, while its scalar trace sequence has recurrence order two.
This directly tests why a nondense scalar recurrence degree must not be
substituted for the representation's Euler degree.

All these tests use integers and `Fraction`, with no floating point, random
sampling, or symbolic external engine. Their finite success does not replace
the unbounded proofs in the note.

## 4. Source, resource, and literature checks

The manifest checksum and all three frozen Git blobs are authenticated,
including byte-content hashes and working-tree equality. The fixture binds
the producer, note, tests, row payloads, and complete payload. The strict
resource-cap refusals and hard parameter maxima pass under `-O`; the stated
work bounds count the declared primary algebraic loops, not all bit
operations, memory use, hashing, or wall-clock time. No stronger resource
claim is warranted.

Primary publication records were checked for the three literature pointers.
[Morales](https://arxiv.org/abs/1306.6910v2) explicitly identifies Segre
Hilbert numerators with Simon Newcomb numbers;
[Deligeorgaki--Han--Solus](https://arxiv.org/abs/2407.12076v2) supplies the
multiset-Eulerian context. The bibliographic record for
[Jacquet--Piatetskii-Shapiro--Shalika](https://www.math.columbia.edu/~hj/Rankin%20Selberg%20convolutions.pdf)
matches the stated Rankin--Selberg reference. These checks do not constitute
an exhaustive novelty search or a new global automorphy theorem. The local
algebraic proofs are self-contained, and the external references remain
explicitly non-machine-authenticated literature boundaries.

## 5. Replay

```text
python -B -m unittest tests.test_universal_coefficient_power_euler_obstruction
python -B -O -m unittest tests.test_universal_coefficient_power_euler_obstruction
python -B research/l-families/atlas/generalized/universal_coefficient_power_euler_obstruction.py --check
python -B -O research/l-families/atlas/generalized/universal_coefficient_power_euler_obstruction.py --check
python -B -m ruff check research/l-families/atlas/generalized/universal_coefficient_power_euler_obstruction.py tests/test_universal_coefficient_power_euler_obstruction.py
python -B -m ruff format --check research/l-families/atlas/generalized/universal_coefficient_power_euler_obstruction.py tests/test_universal_coefficient_power_euler_obstruction.py
```

This audit accepts no prime-indexed family, ramification, functional equation,
automorphy, motive, complex-rank interpolation, or RH/GRH consequence. The
smallest retained obstruction is already the exact identity two-jet at
`n=k=2`: the target second coefficient is nine, not ten.
