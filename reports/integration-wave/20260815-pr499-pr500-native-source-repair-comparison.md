# Comparative review of PR #499 and PR #500

Review cutoff: `2026-08-15T18:32:52Z`  
Main: `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`

```text
PR #499 head  99d3983b57f82941131caa8d9c36e4947f1179a0
PR #500 head  d73c1e7a1a482cac31581211a84db43cc34c824e
```

## Executive verdict

Both proposals attempt to close review #492's missing native-source-to-realized-row arrow. Neither succeeds at its frozen head.

```text
shared native normalization and Y4 dual          VERIFIED
compact target-Hall and row-bonus algebra        VERIFIED WITH FIXES
rough first ownership and causal coefficients    VERIFIED
formal integration / one quantizer               VERIFIED CONDITIONAL
all-column and native-cost arithmetic             VERIFIED CONDITIONAL

PR #499 complete target-null Hall packet          FALSE AS WRITTEN
PR #499 full composition                          UNPROVEN / GAP
PR #499 reproducibility                           3 ADVERTISED MANIFESTS ABSENT

PR #500 abstract coupling theorem                 VERIFIED WITH FIXES
PR #500 live factor-67 coupling marginal          UNPROVEN / GAP
PR #500 current replay                            EMPIRICAL ONLY
PR #500 full composition                          UNPROVEN / GAP

Riemann Hypothesis                                UNPROVEN
```

PR #500 is the cleaner architecture: it correctly keeps signed finite/continuum comparison outside the positive source cone. It still verifies a schema rather than instantiating the live arithmetic coupling.

## Shared mathematical arrow

```text
full Möbius row
 -> exact w_X, Omega_X, J_Lambda
 -> positive Y4 dual
 -> compact factor-67 Hall
 -> Hall residual + nonnegative component-row bonus
 -> rough first-owner partition
 -> causal current and same-index child placements

 -> ONE EXPLICIT POSITIVE JOINT COUPLING
    with the actual source marginals and physical output marginal

 -> complete cells
 -> one label-blind B-spline quantizer
 -> one nonnegative finite row d_X

signed observation comparison
 + positive unused capacity
 -> Omega_X-Xi(d_X) >= 0
 -> direct Y4 price
 -> endpoint consumer
 -> RH.
```

The capitalized coupling remains open.

# PR #499

## Exact Hall score obstruction

`L-91820` correctly proves the target residual and the nonnegative component-row Hall bonus. It then promotes each edge bonus to a **complete positive target-null packet**, while also claiming exact score equality.

At the admissible fibre \(x=2\), Hall must use the edge \(o=2\to e=1\). Per unit target, the score ratio is

\[
g(z)=\frac{5z-3}{4z-3},
\qquad
g'(z)=-\frac3{(4z-3)^2}<0.
\]

Here \(z_e=\sqrt2\), \(z_o=1\), so the exact edge score is

\[
g(\sqrt2)-g(1)
=
\frac{3(1-\sqrt2)}{4\sqrt2-3}
<0.
\]

Therefore a nonzero edge cannot simultaneously be:

```text
target-null;
positive in the complete target/score/row cone;
nonnegative in every row;
exact in declared score.
```

The correct surviving statement is:

```text
target equality;
component-row equality with a nonnegative bonus;
score superordination.
```

Thus `L-91820` is **FALSE AS WRITTEN** at complete typed-packet scope. The row-only bonus remains valid.

## One-row question

The residual rows, row bonuses and positive causal colours can formally be integrated and quantized once into one uncoloured row. But the complete typed fibre claimed by `L-91820` does not exist, so `L-91821` is blocked.

`L-91822` and `L-91823` remain coherent conditional capacity/cost theorems if a valid row is independently supplied.

## Missing manifests

Remote reads at the frozen head returned `404` for all three advertised ledgers:

```text
FACTOR67_91820_SHA256SUMS
experiments/X-91820-positive-common-parent-response-complement/SHA256SUMS
standalone/2026-08-15-positive-common-parent-closure/CONTENT_SHA256SUMS
```

This is a separate reproducibility defect.

## PR #499 status

```text
L-91820 complete fibre     FALSE AS WRITTEN
L-91821 realization        UNPROVEN / BLOCKED
L-91822 complements        VERIFIED WITH FIXES / CONDITIONAL
L-91823 native cost        VERIFIED WITH FIXES / CONDITIONAL
T-91821                    UNPROVEN / GAP
```

# PR #500

## Abstract theorem

`L-91850` is a valid conditional theorem for a supplied Hall coupling, residual measure, causal kernel, positive placement kernels and label-blind Quantizer.

## Live marginal is not instantiated

`L-91851` introduces the output

\[
d_X(j)=\Gamma_X(S_X\cross A_X\cross \{T}_atex\cross\{j\})
\]

but does not construct \(\Gamma_X\) from the live arithmetic data. In particular, it does not display the actual positive physical placement of the Hall row bonus.

The current replay confirms the scope problem. It uses:

```text
hard-coded rational even/odd masses;
arbitrary rational profiles;
synthetic cells 12,...,16;
a hard-coded 1/4,1/2,1/4 quantizer;
arbitrary error and Y4 vectors;
64 randomized abstract fixtures.
```

It does not compute or load the actual Möbius atoms, target/score/component rows, Hall flow, rough monoid, endpoint density, same-index packets or B-spline state kernel. The copied frozen imports are not read.

The owner validator is also structurally wrong:

```python
len(owners) == len(set(owners.values())
```

requires owner values to be injective. First ownership is many-to-one: both \(67\) and \(67\cdot71\) are correctly owned by \(67\).

## PR #500 status

```text
L-91850 abstract coupling      VERIFIED WITH FIXES
L-91851 live Gamma_X           UNPROVEN / GAP
L-91852 interface contract     VERIFIED
L-91853 native cost            VERIFIED WITH FIXES / CONDITIONAL
X-91850                        EMPIRICAL ONLY
T-91850                        UNPROVEN / GAP
```

# Shared open theorem

A successor must construct one explicit joint measure

\[
\Gamma_X(ds,do,de,da,dt,dj)
\]

with the actual factor-67 Hall marginals, Hall-edge physical placement, first-owner causal kernel, same-index child packets, complete-cell endpoint density and actual B-spline quantizer. Its output marginal must be checked in every row, ordinary, detail, score and boundary coordinate.

The score coordinate must remain an inequality unless the negative Hall-edge score correction is retained explicitly as a signed coordinate.

## Final disposition

```text
PR #499: one FALSE load-bearing claim; composition unproved
PR #500: cleaner abstract repair; live marginal uninstantiated
RH:      unproved
```

Neither proposal closes the review #492 producer gap at its frozen head.
