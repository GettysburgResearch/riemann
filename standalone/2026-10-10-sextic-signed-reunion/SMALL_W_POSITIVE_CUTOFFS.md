# Addendum after PR #924: positive cutoffs below one and the small-w benchmark

**Scope.** This addendum qualifies the method-specific diagnosis in
`pass2_small_w_core_audit.md`, SHA256
`c0d07ccc7ed2fc1490a631c73db47044df256b7ca6f946ecacd5c735e457f9d9`.
It does not modify that frozen file or any other frozen proof. The exact
native reunion and the ambient-height two-axis adapter in its Sections 1–2
are unchanged.

The new source is PR #924 at commit
`725b2d25ab47e57500049d93985560098c7ef3fa`, with files in
`standalone/2026-10-10-sextic-moving-labels/`:

- `SIXTH_POWER_STRATIFIED_INVERSE.md`, Git blob
  `004dd4a8de2237661235a9da460b3caab432ef53`;
- `ANISOTROPIC_A2_NORM_TRANSFER.md`, Git blob
  `1e4e8a9b70fb15ee42bc41abbcdc3b217e07f215`;
- `MIXED_LABEL_COMPLETION.md`, Git blob
  `6f59a15b41cc87c64188a8037cfc3516bf962ea3`.

The completed combined theorem is `STRATIFIED_TWO_SCALAR_A2.md`, SHA256
`9b540fe779b6e0f3c64baba04deed6ee380f1d9746035afc3cf9c7fdb0cf3ad5`.

## 1. The source's positive cutoff range is genuinely larger

The anisotropic source allows every parent inverse cutoff R>0 and scales
each A2 child cutoff with its actual second-axis length. Child cutoffs below
one are essential to its norm-weight summation. They cannot be replaced by
one in all of the displayed monomials.

The source uses a sharp inverse cutoff: below one the short inverse is
empty. A smooth cutoff omega(Nt/R), with omega equal to one on [0,1] and
zero on [2,infinity), has the corresponding empty-short assertion only
for R<1/2. The remaining interval [1/2,1] has uniformly bounded nonempty
indices and causes no analytic loss. A combined theorem retaining a second
Möbius cancellation must use a smooth version and its actual threshold.
An equivalent fixed dilation is allowed. The combined theorem chooses
omega equal to one on [0,1/2] and zero on [1,infinity); its short part is
empty for R<=1, and its exact long-empty physical cap is doubled.

Accordingly, the earlier audit's R>=1 restriction is a property of its
explicitly pinned old hybrid route. It is not a restriction on PR #924 or
on future child-cutoff choices.

## 2. Exact optimization of the displayed envelope for all R>0

Retain k=2, H=D^h, w=1 and an admissible balanced residual block with

\[
Nb\asymp B,\qquad Z=D^2/B,\qquad m=M=\sqrt Z,
\qquad Y=Z^2/H.
\tag{2.1}
\]

The exact moving labels are J=B and K=B^(1/3). As in the original audit,
granting a loss-free primitive-pair/Cauchy conversion gives the optimistic
factor H/Z from a normalized positive energy to this dyadic covariance
bound. The following calculation is a benchmark for the displayed positive
envelopes, not an assertion of an unsigned replacement for the covariance.

Write kappa in (1/2,1] for the angular scalar exponent. The second short
monomial and the stratified long monomial have relative-to-target costs

\[
\mathcal A R^p\quad\hbox{and}\quad R^{-3},
\qquad
\mathcal A=\frac{D^2}{H^2}Z^{7/4+\kappa/2}.
\tag{2.2}
\]

For PR #924, p=9/2-3 kappa. In `STRATIFIED_TWO_SCALAR_A2.md`, which has
the same stratified long tail, the corresponding power is p=5/2-kappa.
Both powers are positive. For every positive A and p, exact minimization
gives

\[
\boxed{
\inf_{R>0}\max\{\mathcal A R^p,R^{-3}\}
=\mathcal A^{3/(p+3)}.
}
\tag{2.3}
\]

The minimizing cutoff is R=A^(-1/(p+3)); this formula explicitly includes
R<1. To verify (2.3), if R is above that balancing point, the first term
is at least the displayed value; if it is below, the second term is at
least that value.

Whenever the compact dual support contains a nonzero element, Y is at
least a fixed positive constant. Thus Z is at least a fixed constant times
sqrt(H), and

\[
\mathcal A\gg D^2 H^{-9/8+\kappa/4}.
\tag{2.4}
\]

For 1<h<2 and 1/2<kappa<=1, the right side exceeds a fixed power of D.
Hence the optimized right side in (2.3) still exceeds a fixed power of D.
The previously identified difficulty in this balanced family therefore
persists for the displayed six-term envelopes even after allowing all
positive cutoffs.

At kappa=11/12, (2.4) is D^2 H^(-43/48). The exponent 3/(p+3) is 12/19
for PR #924 and 36/55 for the completed two-scalar strengthening. These
are powers in a method-specific positive upper bound. They are not lower
bounds for the arithmetic energy and do not rule out cancellation before
taking positive norms.

## 3. Exact empty strata and the classical fallback remain separate

The Y times smaller-axis term retained in each boxed hybrid envelope gives
D^3 at b=w=1 after the factor H/D^2. This is independent of the parameter
R in that displayed envelope. It is not an assertion that every physical
short stratum is nonempty: a proof using exact empty-stratum information
may omit its actual short contribution. Such a refinement must then bound
the remaining terms with their true supports.

For comparison, the existing all-row classical positive raw envelope is

\[
Y+Y^{1/6}D^2+(YD^2)^{2/3}
\tag{3.1}
\]

at the leading physical rectangle D by D. Multiplication by H/D^2 and
substitution Y=D^(4-h) give the exponents

\[
2,\qquad (5h+4)/6,\qquad 2+h/3.
\tag{3.2}
\]

For 1<h<2, the last is the largest and remains greater than h. Thus even
the optimistic classical benchmark does not close the leading balanced
core in this range.

At sufficiently large b, Y can be bounded. The classical envelope can
then be diagonal-sized, and compact dual support may eventually make the
nonzero-frequency sum empty. Neither this addendum nor the original
method comparison rules out those already accessible low-conductor
endpoints. The failure diagnosis concerns the remaining balanced growing
scales when approached through the specified positive envelopes; it does
not exclude a new exact pruning argument, an averaged moving-label gain,
or cancellation within the original signed covariance.
