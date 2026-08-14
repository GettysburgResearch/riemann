# `T-91656` final hostile-reconstruction handoff

## Frozen predecessor and repair

```text
repository:                 gfreund123/riemann
proposal PR:                #455
review predecessor:         PR #457
review head:                e136fcf42fbab1195fc193e64ce4039d1a1d416c
reviewed false proposal:    9dba11b2f1130c0aa8dba5846ec3c2e658326474
base branch:                research/gpt56-pro/91663-direct-root-review-response
base SHA:                   f41797c91497dc462f549a127d8494bbe4ccde2f
normative content commit:   6b56f65f4970be887d1b9567455594b8be6ca96d
manifest commit:            cd01edfcdd11c6f52cf00dc885f187ef55a63f7f
manifest blob:              f591f627c1a0734c0750b591324cd0439b08264a
connector audit commit:     940998db3f53a4060f346f2a7ed2b1af31c20fcc
connector audit blob:       4a5995f0e8ba726e614df14f17ae4c72edc251c9
```

The final self-excluding lock is written after this handoff and must be read
with the dependency manifest.

## Review disposition

PR #457's factor-three counterexample is accepted exactly. Historical
`L-91668`, `L-91669`, and `T-91655` are rejected or superseded on the live
branch.

The replacement is:

\[
w_\Psi=3w_{4/3},
\qquad
\mathcal H_{\Psi,j}(Y)=\frac{Q_Y(j)}{4\sqrt Y-3},
\]

so one source atom realizes exactly one native component row atom.

## Normative chain

```text
R-91659  exact factor-three refutation
L-91670  one-copy single-SHARP source/target/score/row normalization
L-91671  exact finite-seed bridge, one physical row, equality-deficit recurrence
L-91666  fixed-67 literal entropy theorem
T-91656  final conclusion-producing proposal
```

The controlling packet front door is:

```text
standalone/2026-08-14-full-direct-row-closure/README.md
standalone/2026-08-14-full-direct-row-closure/CLAIM_STATUS.md
standalone/2026-08-14-full-direct-row-closure/FINAL_REVIEW_SPECIFICATION.md
```

## Required review order

1. Reproduce `R-91659`; verify that the old two-channel row multiplier is `3`.
2. Reconstruct `L-91670`, including its internalized `a=4/3` normalized-row
   monotonicity and exact least-prime source recursion.
3. Verify the finite equality-seed Fubini identity and
   `R[b_X^star]=c_X` in `L-91671`.
4. Reconstruct the finite-window continuum endpoint realization, quantization,
   collar, mismatch, top, terminal, and corrected port exactly once.
5. Verify the one-prime target/row-budgeted-score/row cocycle and frozen Hall
   cells.
6. Verify source-disjoint stopping leaves and measurable leafwise Hall Fubini.
7. Verify the same-index arbitrary-child ordinary/detail inequalities in every
   physical integer column.
8. Rerun `L-91666/X-91666` and `X-91670`.
9. Derive the equality-deficit identity before inequalities and verify the
   current constant is independent of `X` and leaf count.
10. Convert equality deficit to native loss using
    `J_Lambda(X)<4sqrt(X)+4log(X)`; do not identify `P_Lambda` with `4sqrt(X)`.
11. Reconstruct the finite dual, prime-square drift, Mellin pole, Landau sign,
    and functional equation.

## Exact one-row and score rules

The sole physical row is

\[
d_X=R_X^{\rm par}-R_X^{\rm ch}+d_K.
\]

The recursive identity is for the equality deficit:

\[
\mathcal D_X(d_X)
=
[J_X^{\rm eq}-J_K^{\rm eq,ch}
-\mathcal S(R_X^{\rm par}-R_X^{\rm ch})]
+
\mathcal D_K^{\rm ch}(d_K).
\]

Only afterward is the native loss formed:

\[
\mathfrak L_X(d_X)
=[J_\Lambda(X)-4\sqrt X]+\mathcal D_X(d_X).
\]

## Replays and freeze validation

```text
X-91666:
  PASS_FULL_DIRECT_ROW_CLOSURE_ALGEBRA

X-91670:
  PASS_SINGLE_SHARP_NORMALIZATION_HARDENING
  a5b07f68367447da089ef8d8fa84adf2ea2615b4fcbb8f038d7f23cf5dc49dda

X-91671 connector audit:
  PASS_T91656_FINAL_SINGLE_SHARP_LOCK_CONNECTOR_AUDIT
  4ee8bc90ee634def1c4c4a0005be2d11d02fb9fb01ab588e287552a895f7759e
```

The connector audit validates the declared repository freeze. It explicitly
does not validate the mathematics or establish RH. The local checkout validator
is deposited but was not executed in this runtime because DNS could not resolve
GitHub for a checkout.

## Immediate falsifiers

```text
old balanced/reserve row normalization used;
single-SHARP row multiplier not equal to one;
source atom duplicated;
global positivity of L_* assumed;
finite and continuum equality seeds misnormalized;
P_Lambda identified with 4sqrt(X);
current packet appended twice or copied to child;
ordinary/detail column overdraw;
L-91666 failure;
C_reset depends on X or leaf count;
equality-deficit coefficient differs from one;
endpoint sign or pole cancellation wrong.
```

## Status

```text
factor-three review objection              accepted and repaired
single-SHARP normalization                 exact
typed finite/continuum bridge              explicit
source/Hall/current finite inputs           frozen / reconstruct
same-index child replacement               exact
fixed-67 theorem                           proved
full theorem                               complete proposal / review required
Riemann Hypothesis                         unproved pending review
```
