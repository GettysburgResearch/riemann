# Special audit — rejected and refuted claim reclassification

**Agent:** `gpt56-pro`  
**Date:** 2026-08-07  
**Repository:** `gfreund123/riemann`  
**Branch:** `agent/review-verdict-reclassification`  
**Global status:** **RH remains unproved. No rejected proof is revived by this audit.**

## Executive result

I audited the repository’s rejection/refutation trail with a different question
from an ordinary proof review:

> Does the negative evidence contradict the exact frozen statement, or only a
> proof step, stronger surrogate, special construction, or lifecycle object?

The result is an 18-entry scope overlay.

```text
3   genuine verdict-type/category errors in the integrated ledger
15  theorem-level scope propagations that should be narrowed
5   tempting refutations-of-refutations checked and rejected
0   proofs of RH recovered
0   exact counterexamples overturned
```

The most important finding is not that the primary refutation files are
careless. Many are admirably precise. The error occurs when their verdicts are
propagated into PR titles, cross-PR summaries, aggregate counts, or route-level
shorthand. The recurring invalid substitutions are

```text
failed derivation                 -> false theorem
false generic operator bound      -> false source-specific scalar estimate
false unsigned/monotone surrogate -> false signed transport theorem
failed test-function construction -> false abstract conditional criterion
obsolete trigger branch           -> rejected mathematics
```

The machine-readable overlay is

```text
audits/gpt56-pro/2026-08-07-refutation-scope-overlay.tsv
```

The governing status rule is recorded in `M-26001`.

## Method

For each candidate I recorded:

1. the exact target PR and commit;
2. the negative claim or review record;
3. the hypotheses actually tested by the counterexample;
4. the conclusion actually contradicted;
5. the strongest statement that survives without being promoted to verified.

A theorem was classified `CLAIM_REFUTED` only when the witness satisfies the
exact hypotheses and contradicts the exact conclusion. “Not refuted” is not
“verified.” A surviving statement remains at its prior status, usually
`PROPOSED`, `OPEN`, or conditional.

## I. Three integrated `REJECTED` rows are not rejected mathematics

The frozen 2026-08-01 ledger reports three source PRs as `REJECTED`. All three
are lifecycle dispositions.

### 1. PR #59 — matched-pole Arb trigger branch

Frozen ref: `401e843f3c4c1e0021487537a512aab9413cd15f`.

The ledger’s own reason is “obsolete trigger/integration unit.” No theorem is
contradicted. Correct classification:

```text
LIFECYCLE_REJECTED / TRIGGER-ONLY / NO MATHEMATICAL VERDICT
```

### 2. PR #63 — fifty-shard workflow trigger

Frozen ref: `a379b14d4d8cbfd39529206617e28ebafefa353b`.

Again the object is trigger-only. Missing or obsolete workflow orchestration is
not a false mathematical claim. Correct classification:

```text
LIFECYCLE_REJECTED / TRIGGER-ONLY / NO MATHEMATICAL VERDICT
```

### 3. PR #135 — PA1 trigger with obsolete provenance contract

Frozen ref: `fb3085e4aca61592ef1c86f36ba3581415ba665d`.

The rejected object is an obsolete provenance contract; a corrected typed
workflow is a separate object. Correct classification:

```text
LIFECYCLE_REJECTED / OBSOLETE PROVENANCE / NO MATHEMATICAL VERDICT
```

### Aggregate correction

The historical ledger must remain frozen, but future summaries should not say
that the review wave found “three rejected mathematical claims.” It found

```text
mathematical REJECTED: 0
lifecycle REJECTED:    3
```

within that aggregate category. This does not alter any frozen-commit review.
It corrects the type of the aggregate.

## II. Failed derivations whose theorem statements remain open

### 4. PR #165 / `R-15407` — frozen Farey proof

Frozen target: `2e16425d5865789db113ff37709a9565f022f881`.

The refutation is exact and stands:

```text
true step in av-bq=r: (q/g,v/g), g=(q,v)
old step:             (q,v)
odd-odd residue:      nonzero cotangent difference
```

This rejects `L-15448` as a derivation and `T-15414` as a proof of RH. It does
not supply a counterexample to the critical analytic-totient local
second-moment estimate. That estimate remains RH-bearing and open.

Correct propagation:

```text
frozen Farey derivation       REJECTED
critical second-moment claim  OPEN / NOT DISPROVED
```

“Farey proof refuted” is acceptable frozen-object shorthand. “Farey
second-moment theorem refuted” is not.

### 5. PR #243 / `R-9510` — carry conditional-Hankel proof

Frozen target: `225c5e3d231ac23b6f487cd43e0dc89d48d3db1c`.

`R-9510` computes the negative local determinant

\[
 f''(0)f''''(0)-f'''(0)^2=-233/64.
\]

This is a genuine obstruction to the claimed conditional-Hankel square, not
merely to unconstrained Hankel positivity. `L-26001` supplies the missing
compatibility argument: conditional positivity of `f(x+y)` on every zero-mass
measure forces positive semidefiniteness of `f''(x+y)` by applying the form to
finite differences

\[
\mu_h=h^{-1}\sum_i a_i(\delta_{x_i+h}-\delta_{x_i}).
\]

Therefore the review’s local determinant stands and the proposed proof is
rejected. But the review explicitly does not produce a value `y` for which the
carry profile is negative. Correct propagation:

```text
positive-Bernstein / conditional-Hankel derivation  REFUTED
pointwise carry-profile positivity C(y)>=0           OPEN / NOT DISPROVED
```

A title such as “carry-Hankel refutation” must not become “carry positivity
refuted.”

### 6. PR #231 / `R-22802` — uniform Farey-cluster operator

Head: `f32aae44411ec1b635b32490f2836efde58e4466`.

The row-norm counterexample exactly refutes a uniform arbitrary-vector
subpower operator bound: a fixed positive cell contains a row of norm at least
`c_k sqrt(D)`. It does not contradict the scalar estimate on the actual
Möbius-coupled coefficient vector.

Correct propagation:

```text
uniform generic cluster bound                 REFUTED
specific signed Mobius critical-cell estimate OPEN / RH-BEARING
```

Cauchy–Schwarz cannot close the route, but the arithmetic statement has not
been shown false.

## III. Conditional criteria and abstract mechanisms that survive failed instances

### 7. PR #219 / `R-21903` — `SH(L)`

Head: `4a472026d140c3c2d8fdd80da12a36fdb4151d48`.

The positive-Hankel decay theorem rules out the proposed cellwise interpolation
of the stop-loss ramp with vanishing local residual. It does not refute the
conditional implication

```text
SH(L) => RH.
```

Correct propagation:

```text
globally positive-Hankel construction of SH(L)  BLOCKED
conditional theorem SH(L)=>RH                    RETAINED AT PRIOR SCOPE
```

The remaining work is to prove `SH(L)` by a different construction or replace
it with a valid differenced/conditional theorem.

### 8. PR #229 — compact stop-loss adjoint versus `L-23004`

Head: `2fc74c11b9929f694d8c13d060c9d55b99dc9621`.

`R-23001` shows that the exact compact stop-loss adjoint has a negative terminal
atom and therefore fails both global and zero-mass conditional Hankel cones.
The elementary abstract criterion `L-23004` remains sound under its stated
hypothesis

\[
f''(u)=\int e^{-su}\,d\rho(s),\qquad \rho\ge0.
\]

Correct propagation:

```text
specific compact stop-loss adjoint  REFUTED AS AN INSTANCE
zero-mass conditional-Hankel lemma   SURVIVES
```

The instance fails the criterion; the criterion is not refuted.

### 9. PR #199 / `R-19701` — Schur correction

Head: `4158e0d3e7f91829a6c545308605ea8177023aa3`.

The exact inequality

\[
B_K-Z^*C^{-1}Z\le B_K
\]

shows that eliminating a positive complement cannot repair an already negative
kernel direction. This does not refute Schur analysis. It identifies the
Schur-corrected kernel floor as the final RH-equivalent sign target.

Correct propagation:

```text
Schur correction as an automatic rescue mechanism  REFUTED
Schur-corrected kernel criterion/equivalence        RETAINED AT PRIOR SCOPE
```

## IV. Generic or unsigned surrogates that do not refute source-specific signed targets

### 10. PR #239 / `R-23702` — bounded-rank Bohr contagion

Head: `556e45a02d437a96c06d991bf140cb184dcf1803`.

The same-sign Möbius hypercubes refute the claimed absolute face-rank ceiling
and the resulting `C_0/K` enumeration loss. The counterfamily is exact and the
refutation stands.

It does not refute every source-specific signed contraction. In particular, it
does not show that cancellation between complete opposite-parity families is
impossible.

Correct propagation:

```text
absolute bounded-rank BCT(K)             REFUTED
source-specific signed balanced theorem  OPEN
```

### 11. PR #254 / `R-25301` — divisibility cover

Head: `058c95c04a24e3bc7d2bd6bb9a94568187199f30`.

The von-Mangoldt dual lower bound proves that every nonnegative monotone cover
of the proposed form costs `Omega(sqrt X)`, contradicting the desired
`O(log^2 X)` cost. That exact refutation stands.

The same branch exhibits positive defect and negative slack of the same
macroscopic order. A signed flow that transports defect into slack is outside
the hypotheses of the monotone-cover lower bound.

Correct propagation:

```text
nonnegative monotone Divisibility Cover  REFUTED
signed constraint-dipole transport       OPEN
```

### 12. PR #163 / `R-15601` — dimension-only capacity comparison

Head: `c3ebadec228d79b802af89c8a01759c3290c32bf`.

The two-dimensional counterexample refutes a dimension-only threshold-index
comparison when the source packet and weighted deficit operator live in
unrelated directions. It does not refute the leverage-weighted trace-tail
criterion

\[
D_L(G)=\operatorname{Tr}((I-P_L)T_G)
\]

or the finite visible Schur gate.

Correct propagation:

```text
dimension-only unrelated-packet shortcut  REFUTED
weighted trace-tail capacity target        PROPOSED / OPEN
```

### 13. PR #206 / `R-20501` — absolute Möbius-tail smallness

Head: `ff659984de0ab0c397ebefad393bc585c9007bc2`.

The positive-residual control shows that a residual may have very large
absolute norm while its negative endpoint is zero. Thus absolute tail
smallness is sufficient but not necessary.

The load-bearing quantity is the negative part of the joint Schur-corrected
residual. Correct propagation:

```text
absolute residual/tail -> 0 as a necessary condition  REFUTED
joint corrected-residual negative-part criterion       RETAINED AT PRIOR SCOPE
```

## V. Transfer or selection shortcuts that fail while exact component results survive

### 14. PR #173 / `R-16001` — sampled surrogate versus CvS coefficients

Head: `7085396b3c7e033d50ac4c031c5acdbe9b7814a6`.

The original unsatisfiability claim was already withdrawn. The hard-window
sampled-`Xi` target is not the CvS coefficient target, its tail is dominated by
cutoff artifacts, and the finite ladder does not prove cofinal incompatibility.

Correct propagation:

```text
sampled hard-window surrogate obstruction  PARTIAL / EMPIRICAL
actual CvS Fourier-coefficient problem      OPEN
programme unsatisfiable                     FALSE OVERREACH
```

### 15. PR #87 / `R-5602` — counting exclusivity

Head: `a374379b7adcac44f16462b9f75238c81a45b11d`.

The review correctly refutes uniqueness of counting as a displacement detector,
quadratic response from differentiability alone, and Hardy-`Z` sign-change
deficit as an RH disproof.

Those points do not refute the exact finite slab predicate

\[
D(a,b)=N(a,b)-N_0(a,b)>0,
\]

nor the gap-or-collision completeness dichotomy. Correct propagation:

```text
counting-exclusivity and sign-change shortcut  REFUTED
exact total-minus-line multiplicity criterion  PROPOSED / UNREFUTED
```

### 16. PR #192 / `R-18901` — unaugmented complement capture

Head: `6c1a3a73de6b020aabaf1dff6cda9b8c7129af3f`.

The finite control shows that the old packet `U_0` need not leave a positive
complement. The same spectral model identifies the canonical high-deficit
finite augmentation required to obtain the declared complement floor.

Correct propagation:

```text
unaugmented U0 complement floor             REFUTED
canonical finite deficit augmentation       PROPOSED CLOSED AT FIXED SUPPORT
finite enlarged packet sign                 STILL OPEN
```

### 17. PR #208 / `R-20701` — support averaging

Head: `8a573d0245411313326223d8afb792e95eeef073`.

Concavity prevents positivity of an averaged matrix from selecting a positive
individual support. That selection shortcut is false. The exact centered-prime
convolution and square-screw principal-coordinate identity are not affected.

Correct propagation:

```text
average positivity => positive support  REFUTED
centered-prime factorization             RETAINED AT PRIOR SCOPE
square-support principal coordinate      RETAINED AT PRIOR SCOPE
```

### 18. PR #183 / `R-17201` — Bohr limit versus finite block

Head: `ceebb12b121695f2125152b8963238b1a9f0008e`.

A limiting Bohr variance is not automatically an upper bound for one finite
mean-square block. The transfer fails without explicit sinc/Gram residual
budgets. This does not refute the limiting identity or the separately certified
finite notch moats.

Correct propagation:

```text
Bohr-limit value used directly as finite-block bound  REFUTED
finite sinc/Gram methodology and notch moats           SURVIVE AT DECLARED SCOPE
```

## VI. Tempting reviewer reversals that do not survive audit

A special pass should be adversarial in both directions. I therefore attempted
to overturn the strongest recent refutations. Five stand.

### `R-9510` stands

The zero-mass constraint does not rescue PR #243. `L-26001` proves that
conditional positivity forces derivative-kernel PSD; the negative local
Hankel determinant is fatal to the claimed square.

### `R-15407` stands

The gcd-reduced solution step and nonzero cotangent residue directly contradict
the frozen Farey enumeration and telescoping claims.

### `R-22802` stands

The fixed-cell `a=1` row genuinely has Euclidean norm `Omega(sqrt D)`, so the
stated unweighted arbitrary-vector operator norm cannot be `D^{o(1)}`.

### `R-23702` stands

The multiplicative hypercube has exact affine rank `K`, common Möbius sign, and
one fixed-ratio shell. It refutes the absolute bounded-rank theorem as stated.

### `R-25301` stands

The dual identity applies to every nonnegative monotone cover satisfying the
stated constraints and yields the square-root lower bound. Signed transport is
a different theorem, not a repair of the monotone claim.

## VII. Required repository changes

### 1. Split status dimensions

Future ledgers should record separately:

```text
mathematical_status
review_status
lifecycle_status
counterexample_hypothesis_match
surviving_scope
```

### 2. Reserve `REFUTED`

Use `REFUTED` only for an exact hypothesis-compatible counterexample. Use

```text
DERIVATION REJECTED / STATEMENT OPEN
SURROGATE REFUTED / SOURCE-SPECIFIC STATEMENT OPEN
INSTANCE REFUTED / ABSTRACT CRITERION SURVIVES
CONSTRUCTION BLOCKED / CONDITIONAL IMPLICATION SURVIVES
LIFECYCLE REJECTED / NO MATHEMATICAL VERDICT
```

when those are the actual conclusions.

### 3. Keep frozen records immutable

The 2026-08-01 ledger and every frozen review remain historical evidence. This
audit is an append-only overlay. It does not silently rewrite past reviews.

### 4. Cross-PR summaries must carry surviving scope

Every sentence of the form “PR #X refutes route Y” should identify the exact
object refuted and name the strongest surviving statement. A bare route-level
label is too lossy for an active polymath repository.

## Final status

This pass restores no proof of RH. It does restore precision to the research
map:

- three `REJECTED` ledger entries are lifecycle objects, not false mathematics;
- several exact counterexamples remain fully valid but attack only derivations,
  generic surrogates, or special constructions;
- the corresponding source-specific signed, weighted, conditional, or
  RH-bearing statements remain open rather than refuted;
- no surviving open statement is promoted to verified.

That distinction matters. A false proof must stay rejected, but an unrefuted
load-bearing theorem must not be accidentally buried with it.
