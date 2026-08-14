# Final hardening pass: single-SHARP normalization and typed root ledger

## Executive result

The pass found an exact factor-three error in the reviewed PR #455 root-entry
theorem. The balanced/reserve target identity is correct, but applying each
channel's normalized component profile and then restoring the positive channel
coefficients produces three native rows.

That route is rejected.

The replacement uses one SHARP channel:

\[
w_\Psi=3w_{4/3},
\qquad
\mathcal H_{\Psi,j}(Y)=Q_Y(j)/(4\sqrt Y-3).
\]

This produces one native row atom exactly and preserves the native target,
row-budgeted score, row monotonicity, least-prime recursion, and one-prime Hall
interfaces.

The pass also replaces the vague continuum-to-finite statement by the exact
seed identity

\[
b_X^\star=\overline b_X^\star+E_X,
\qquad
\mathcal R[b_X^\star]=c_X,
\]

and states one physical row, one child, one current ownership table, and one
coefficient-one loss identity.

## Exact correction

Old:

\[
(1+\kappa_*)w_{a_*}\mathcal Q_{a_*}
+(2-\kappa_*)w_1\mathcal Q_1
=3Q/\sqrt n.
\]

New:

\[
w_\Psi\frac{Q_Y}{4\sqrt Y-3}=Q_Y/\sqrt n.
\]

## New review target

```text
R-91659
L-91670
L-91671
T-91656
X-91670
FINAL_REVIEW_SPECIFICATION.md
CLAIM_STATUS.md
```

Historical `L-91668`, `L-91669`, and `T-91655` are explicitly rejected or
superseded on the live branch.

## Verification

The new exact replay returns

```text
PASS_SINGLE_SHARP_NORMALIZATION_HARDENING
a5b07f68367447da089ef8d8fa84adf2ea2615b4fcbb8f038d7f23cf5dc49dda
```

It explicitly detects the old multiplier `3`, verifies the replacement
multiplier `1`, checks 60 exact finite-seed Fubini identities, 1,008 formal
prime-log score-convolution identities, source-tree coefficient identities,
and the coefficient-one loss normal form.

## Status

```text
old PR #455 native-row theorem     false
single-SHARP normalization         exact
fixed-67 theorem                   retained
finite/continuum typed bridge      explicit
one-use typed ledger               proposed complete
full successor theorem             complete proposal
RH                                 unproved pending review
```
