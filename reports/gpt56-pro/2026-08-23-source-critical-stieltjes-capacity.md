# Source–critical Stieltjes capacity for the Xi boundary gate

Date: 2026-08-23  
Workspace: PR #729  
Scientific status: **RH unproved**

## Exact common coordinate

Let the regularized origin ratio be

\[
\widehat m_F(z)=z\sum_{n\ge0}a_nz^{2n}.
\]

For each real nonpositive critical pair `+/-c`, define

\[
s_c=c^{-2},
\qquad
W_c=-2F(c)/(c^2F''(c)).
\]

The boundary coefficients satisfy

\[
\beta_n
=a_n-
\sum_cW_cs_c^n.
\]

Therefore, for both parity blocks,

\[
S_{k,\Omega}^{(a)}
=A_k^{(a)}-C_{k,\Omega}^{(a)}.
\]

The fixed source moment space is partitioned exactly into critical atomic
consumption and boundary residual reserve.

## Capacity theorem

When `A` is positive definite,

\[
S\succeq0
\iff
\lambda_{\max}(A^{-1/2}CA^{-1/2})\le1.
\]

For singular `A`, the exact statement uses the pseudoinverse and requires
`Ran C subset Ran A`.

The normalized critical operator is a sum of rank-one features. Its trace is a
Christoffel leverage sum

\[
\sum_cW_c\mathcal K_{k,a}(s_c).
\]

Trace at most one is a scalar sufficient condition, while the exact operator
norm at most one is the sharp finite-order capacity condition.

## Conclusion graph

The clean normative theorem is `T-105371`:

\[
\mathrm{OSCC105371}
\Longleftrightarrow
\mathrm{OASH105350}
\Longleftrightarrow
\mathrm{BRP105220}.
\]

Hence

\[
\mathrm{CRVH105330}
\wedge
\mathrm{OSCC105371}
\Longrightarrow
\mathrm{RH}.
\]

The stronger scalar lane `SCLC105371` also implies the conclusion when combined
with `CRVH105330`. None of these Xi estimates is proved.

## Order-one calibration

For odd `F`, `a_0=1`, so

\[
\beta_0
=1-
\sum_{0<c}
{-2F(c)\over c^2F''(c)}.
\]

The first boundary slope is literally the unused reciprocal-square critical
capacity.

## Exact replay

```text
PASS_X_105370_SOURCE_CRITICAL_CAPACITY
71 exact rational checks
```

The polynomial calibrations are `z^3-3z` and
`z^4-2z^2+3/4`. A three-atom synthetic source fixture checks the inverse,
trace and domination formulas exactly. The replay does not evaluate Xi or
establish any RH-bearing gate.

## Publication correction

The initial drafts `L-105371` and `T-105370` contain malformed display
delimiters and are explicitly superseded. The normative files are
`L-105372` and `T-105371`.
