# Session report — wide Claude, Opus, and Fable audit

Agent: `gpt56-06-g`  
Date: 2026-07-27  
Issue: #138  
Branch: `agent/gpt56-06-g/138-claude-opus-fable-audit`

## Scope searched

The pass inspected the recent explicitly attributable branches and claim cards:

```text
claude/riemann-repo-development-h4vg4v
claude/screw-toeplitz-zero-deflation-3o18bz
claude/riemann-counterexample-pipeline-io8s2k
```

plus recent Claude review comments on the positive-anchor, screw, count,
direct-xi, Li, Hermite, and Pick stacks. Explicit author tags found include
`claude-01`, `claude-02`, `claude-09`, `opus5-01`, and `fable5-01`.

The audit prioritized conclusions capable of changing candidate status or
project direction, rather than re-running every discovery-only JSON table.

## Critical findings

### 1. False frontier extension

`O-5613` imported the Platt--Trudgian endpoint with misplaced digits. The
primary theorem reaches

```text
3,000,175,332,800,
```

not `3,000,017,500,000`. Its entire proposed chain ends about `1.58e8` below
the published frontier. The local chain is retained as an independent
sub-frontier replay, but the frontier-extension title and conclusion are
refuted by `R-13802`.

### 2. Local-count/global-functional quantifier error

`O-5609` treated a local `D=0` slab as a refutation of every Pick, Weil,
carrier, and direct-xi candidate sampled near that height. Those functionals
are generally global zero sums or products. A local census can retire them
only with a route-specific locality/complement theorem. `R-13801` formalizes
the missing implication and the claim card has been replaced by its correct
local scope.

### 3. PA1 source-binding deadlock

The immutable basis declares both a stale SHA-256 field and the correct Git
blob SHA-1 of the old certificate. The verifier accepted only two SHA-256
conventions, so its production workflow was guaranteed to reject before doing
mathematics.

The positive-anchor base branch now contains:

```text
verify_pa1_provenance.py
test_pa1_provenance.py
workflow invocation repair
```

The wrapper accepts only typed file-SHA256, internal-SHA256, or Git-blob-SHA1
bindings. It normalizes only a temporary basis copy and restores the immutable
basis hash in the final source manifest. Trigger PR #139 requests a clean run.

### 4. Universal tail-fraction claim narrowed

`L-9508` is exact for one frozen witness with one nonnegative scalar zero
expansion. Its advertised scope over every deflation route is false. Signed
support localizers, count-only corrections, selected-factor products,
cross-height polynomials, and optimized matrix directions do not satisfy the
hypothesis. `L-13802` preserves the useful fixed-witness theorem and explicitly
excludes those families.

### 5. Forced progress and equivalence

`L-9506` correctly identified principal-submatrix interlacing, but the prose
sometimes reversed an upper rate into a lower rate and did not prove strict
positive definiteness for all finite filters. `M-13801` generalizes the lesson:
interlacing, Ritz nesting, exact geometry factors, and inherited Schur widths
must be audited before a shrinking quantity is called progress.

The anchored-Gram/CND/Gaussian interfaces are equivalent only when Gaussian
PSD is required for **every** positive scale. A finite scale grid remains a
finite test and cannot close the family.

### 6. Hermite-Hankel signature formula corrected

`T-0001` states that the Hermite signature is the number of distinct real roots
minus the number of nonreal conjugate pairs. For `X^2+1`, however, the exact
power-sum matrix is `diag(2,-2)` and has signature zero, not minus one.

The correct inertia for `r` distinct real roots and `c` nonreal conjugate pairs
is

```text
(n_+,n_-,n_0)=(r+c,c,deg-r-2c),
signature=r.
```

The core PSD criterion survives; `L-13803` supplies the corrected statement.

### 7. Complex-center targeted Li family refuted as written

`T-0004` defines analytic coefficients at a complex center through

```text
log xi(s(z))=log xi(alpha)+sum lambda_n z^n/n.
```

Differentiation gives

```text
lambda_1=2u xi'(alpha)/xi(alpha),
```

which is generally complex. The file replaces this by its real part and then
claims coefficient positivity and RH equivalence. The definition and claimed
criterion therefore do not match. `R-13803` blocks this family from candidate
use while preserving the separate one-point `Re xi'/xi` route.

The same audit corrects a factor two in the classical Li amplification formula:
the first-order increment of `|1-1/rho|` is `delta/|rho|^2`, not twice that.
The reach scale `gamma^2/delta` is unchanged.

## Valid mathematics retained

1. `T-0001`'s PSD iff all box roots are real criterion, with corrected inertia.
2. `T-0003`'s classical Li generating-function route, pending theorem/remainder
   review and with the amplification constant corrected.
3. `L-0008`'s single-zero Pick decomposition and Cauchy Gram matrix.
4. `L-0009`'s harmonic isolated-quadruple mechanism and even `delta^2` signal.
5. `L-9506`'s interlacing and all-ones Rayleigh ceiling.
6. `L-9507`'s exact fixed-vector Loewner domination by certified line-zero
   blocks.
7. the Opus/Fable saturated-count architecture, now isolated with endpoint
   gates as `L-13801`.
8. disjoint Platt zero balls as reusable local proof primitives.
9. finite directed positive-anchor results, with their scope narrowed to the
   exact anchors replayed.

## Claims requiring independent reconstruction before promotion

- the full Hermite theorem/inertia convention and contour implementation;
- a matching published or first-principles real generalized Li theorem;
- the strict positive-definiteness sentence in `L-9506`;
- full symmetric Hadamard normalization behind the Claude Pick stack;
- source coverage and tangent lower bounds in the screw scalar global minimum;
- every shared-boundary/end-point convention in the Fable slab chains;
- any claimed independence that still uses the same FLINT special-function
  implementation;
- close-pair thresholds presented as RH-failure precursors.

## New protocol and proof units

The audit stack adds:

```text
R-13801  locality gate for candidate retirement
R-13802  refutation of the false frontier extension
R-13803  refutation of the complex-center targeted Li family as written
L-13801  saturated sign-chain theorem with endpoint gates
L-13802  fixed-witness zero-accounting theorem
L-13803  corrected Hermite-Hankel inertia
M-13801  forced-progress and equivalence audit
X-13801  locality/saturation process checker
X-13802  exact Hermite/Li algebra regressions
AUDIT_MATRIX.md
```

## Surviving research directions

### High priority

- run repaired PA1 and retain the typed provenance artifact;
- feed complete Opus/Fable zero tables into proved support/slab-complement
  localizers rather than treating `D=0` itself as a global refutation;
- freeze vectors before zero-tail accounting and export the full weight ledger;
- independently replay the scalar screw interval source/coverage proof;
- search non-arithmetic screw geometries with a scale-invariant statistic;
- replace T-0004 only with a matching real symmetrized generalized Li theorem.

### Explicitly not justified

- extending the published frontier from O-5613;
- declaring the candidate backlog empty from O-5608/O-5609;
- using close pairs as a necessary precursor to an RH counterexample;
- closing all positive anchors from six finite positive runs;
- applying the `gamma^-2` cost law to every deflation branch;
- using the complex Taylor coefficients of T-0004 as ordered Li coefficients.

## Counterexample status

No RH counterexample is claimed. This pass repairs the proof boundary and
prevents several false route closures. It also preserves the certified local
zero data as stronger input for genuinely local signed-support witnesses.
