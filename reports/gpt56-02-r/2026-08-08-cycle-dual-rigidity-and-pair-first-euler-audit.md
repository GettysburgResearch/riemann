# Cycle-Debt continuation: global dual rigidity, harmless floor atoms, and the pair-first Euler obstruction

Date: 2026-08-08  
Agent: `gpt56-02-r`  
Branch: `agent/gpt56-02-r/262-half-pole-boundary-spline`  
Status: **NEW EXACT THEOREMS + EXACT REFUTATION; RH REMAINS UNPROVED**

## 1. What is now pushed

This continuation adds:

```text
L-27901  global square-root rigidity of Cycle Debt duals;
L-27902  the complete floor-atomic capacity cone is nonobstructing;
R-27901  feasible defects need not be monotone or completely monotone;
X-27901  exact standard-library mutation replay.
```

The live PR #272 factor-one-half dyadic recurrence remains the preferred carry
consumer.  Its sole native hinge is the paired odd-commutator debt `DCD`.

## 2. Global duals are rigid

Every global feasible potential satisfies

\[
 F(n)=an-D_F(n),
 \qquad
 0\le D_F(n)\le D_{\mathcal G}(n)\le4\sqrt n,
\]

where `D_F` and `D_mathcalG-D_F` are balanced subadditive and

\[
 D_{\mathcal G}(n)
 =\sum_{q\ge2}{\{n/q\}\over\sqrt q}.
\]

The linear part vanishes against the size-zero Möbius divergence.  Hence a
global dual obstruction is one square-root-sized capacity defect, not an
arbitrary high-dimensional potential.

Finite duals are pointwise compact after normalization.  Any cofinal
obstruction must therefore be either:

1. a genuine global defect inside `D_mathcalG`; or
2. a moving endpoint shell escaping every fixed-coordinate limit.

## 3. Every literal floor atom is harmless

For `0<=theta_q<=1`, the atomwise defect

\[
 D_\theta(n)=\sum_q\theta_q{\{n/q\}\over\sqrt q}
\]

is feasible.  Its exact Möbius-target pairing is

\[
 \left\langle r_X,D_\theta\right\rangle
 =-\sum_{q\le X}{\theta_q\over\sqrt q}w_X(q)\le0.
\]

Thus no positive Cycle Debt can be produced by assigning the capacity
independently among the carry columns.  A real obstruction must be a non-atomic
compatible splitting or a moving endpoint shell.

## 4. Generic complete monotonicity is false

The legal `q=2` floor atom has defect

```text
D(2m)=0,
D(2m+1)=1/(2 sqrt(2)).
```

Its dyadic curvature alternates forever.  Therefore the balanced constraints do
not imply monotonicity, complete monotonicity, a positive Laplace mixture, or an
automatic move from `1/zeta(s+1/2)` to the Euler-product half-plane.

This disposes of the speculative complete-monotonicity shortcut without
weakening DCD itself.

## 5. Exact audit of PR #301

The corrected full proposal on PR #301 pairs the shifted-even and
unshifted-odd cutoff legs and obtains

\[
 D_k=(2kq-1)^{-s}-((2k+1)q)^{-s}>0.
\]

The pairwise Hausdorff representation is valid.  However, after pairing, the
actual source is the ordinary positive series

\[
 \sum_{k\ge K}D_k
 =\int {y^K\over1-y}\,d\sigma(y).
\]

The branch then invokes the alternating Euler remainder

\[
 \sum_{k\ge K}(-1)^{k-K}\Delta^mD_k
 =\int {y^K(1-y)^m\over1+y}\,d\sigma(y).
\]

These are different series.  Pairing destroys the alternation which supplies
the `1/(1+y)` denominator and the `2^-M` Euler compression.

Retaining the original interleaved alternation does not restore coefficientwise
positivity: at `q=2,s=1`, one exact second jet is

\[
 {1\over6}-{2\over7}+{1\over10}=-{2\over105}.
\]

This is recorded on the proposal branch as `R-29803`.  It blocks the claimed
positive finite source compression and therefore the current derivation of DCD.
It does not refute the pairwise Hausdorff identity or RH.

## 6. Correct replacement frontier

A valid continuation must choose one ordering and keep its consequences:

```text
pair first:
    ordinary positive Hausdorff resolvent y^K/(1-y),
    but no alternating Euler damping;

Euler first:
    exact 2^-M compression,
    but a signed finite jet bank.
```

The most credible replacement is now the second:

1. retain the true interleaved Euler identity;
2. emit every signed finite jet at the strict half-scale;
3. realize those jets immediately through the canonical balanced-tree/Pascal
   cycle basis;
4. prove their total capacity injection is polylogarithmic under the `6/7`
   analytic bulk contraction;
5. feed that bound into PR #272's exact factor-one-half debt recurrence.

This is a source-specific signed boundary theorem.  No generic positive kernel
or complete-monotonicity claim is available.

## 7. Exact boundary

```text
global dual square-root rigidity             PROPOSED EXACT
floor-atomic dual cone harmless               PROPOSED EXACT
complete-monotonicity shortcut                REFUTED
pairwise Hausdorff source identity            RETAIN
pair-first positive Euler compression         REFUTED
signed interleaved boundary-jet recurrence    OPEN
DCD / Cycle Debt                              OPEN
Riemann Hypothesis                            UNPROVED
```
