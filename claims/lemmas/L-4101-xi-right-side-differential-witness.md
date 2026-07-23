# L-4101 — A right-side differential witness for RH failure

Claim ID: L-4101  
Title: Certified negativity of a first differential localizer for `xi'/xi` disproves RH  
Status: PROPOSED  
Authoring agent: `gpt56-05-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: `D-3201`; the zero-resolvent expansion used in `L-3201`  
Scope: one-point finite `xi`-jet counterexample certificates  
Related counterexample candidates: none

## Statement

Let

\[
 F(s)=\frac{\xi'(s)}{\xi(s)}
\]

in the normalization of `D-3201`. At an exact point

\[
 s=\frac12+x+iT,
 \qquad x>0,
 \qquad \xi(s)\ne0,
\]

define

\[
 \mathcal D(s)
 =\operatorname{Re}F'(s)
  +\frac1x\operatorname{Re}F(s).
\]

If RH holds, then

\[
 \mathcal D(s)
 =2\sum_\gamma
 \frac{(T-\gamma)^2}
 {\left(x^2+(T-\gamma)^2\right)^2}
 \ge0,
\]

where the ordinates of the nontrivial zeros are counted with multiplicity.
Consequently, an exact rational or dyadic point with rigorous enclosures proving

\[
 0\notin\xi(s)
 \qquad\text{and}\qquad
 \mathcal D(s)<0
\]

is a finite unconditional counterexample witness to RH.

Moreover, if RH is false, then there is a nonempty open subset of
`Re(s)>1/2` on which

\[
 \operatorname{Re}F(s)>0
 \qquad\text{but}\qquad
 \mathcal D(s)<0.
\]

Thus the differential criterion is existentially complete and is not merely a
rephrasing of the scalar negative-real-part criterion `L-3201`: it detects every
off-line zero from points immediately to the **right** of that zero, where the
scalar response has a positive pole.

## Evaluation formulas

A producer may evaluate

\[
 F'(s)=\frac{\xi''(s)}{\xi(s)}-F(s)^2
\]

from a second-order `xi` jet. In the direct completion convention of `D-3201`,

\[
 F'(s)=
 -\frac1{s^2}-\frac1{(s-1)^2}
 +\frac14\psi_1(s/2)
 +\frac{\zeta''(s)}{\zeta(s)}
 -\left(\frac{\zeta'(s)}{\zeta(s)}\right)^2,
\]

where `psi_1` is the trigamma function. The direct formula is valid only when
the denominator enclosures justify every division; a direct `xi` jet avoids
separate removable cancellations.

## Motivation

`L-3201` searches for `Re F<0` immediately to the left of a right-half-plane
zero. Close to the pole, however, interval division can become difficult, and a
search limited to negative scalar values ignores the equally singular region on
the other side.

The differential expression above is nonnegative under RH but diverges to
negative infinity on the right side of an off-line symmetric zero pair. At the
same points, `Re F` diverges to positive infinity. This gives Issue #39 a second
one-point certificate with a different geometric basin and only one additional
`xi` derivative.

## Proof under RH

Assume RH. Every nontrivial zero is

\[
 \rho=\frac12+i\gamma.
\]

At `s=1/2+x+iT`, the zero-resolvent term is

\[
 \frac1{s-\rho}
 =\frac1{x+i(T-\gamma)}.
\]

Its real part is

\[
 \operatorname{Re}\frac1{s-\rho}
 =\frac{x}{x^2+(T-\gamma)^2}.
\]

Differentiating the resolvent gives

\[
 \operatorname{Re}\left(-\frac1{(s-\rho)^2}\right)
 =\frac{(T-\gamma)^2-x^2}
 {\left(x^2+(T-\gamma)^2\right)^2}.
\]

Therefore this zero's contribution to `D(s)` is

\[
 \frac{(T-\gamma)^2-x^2}
 {\left(x^2+(T-\gamma)^2\right)^2}
 +\frac1{x^2+(T-\gamma)^2}
 =\frac{2(T-\gamma)^2}
 {\left(x^2+(T-\gamma)^2\right)^2}.
\]

Every term is nonnegative. The derivative series is absolutely convergent
because it is dominated by a constant multiple of
`sum_gamma |s-rho|^-2`, and the real-part series used after division by `x` is
the absolutely convergent Poisson sum already invoked in `L-3201`. Summing the
termwise identity proves the displayed formula and nonnegativity. A directed
negative enclosure contradicts RH.

## Converse: every RH failure creates a right-side witness

Assume RH is false. By zero symmetry there is a pair, with the same positive or
negative ordinate,

\[
 \rho_+=\frac12+\delta+i\gamma,
 \qquad
 \rho_-=\frac12-\delta+i\gamma,
 \qquad \delta>0,
\]

with a common multiplicity `m>=1`. Remove both poles from `F` in a small
neighborhood of `rho_+`. Along the horizontal line through the pair,

\[
 F\!\left(\frac12+x+i\gamma\right)
 =\frac{m}{x-\delta}+\frac{m}{x+\delta}+h(x)
 =\frac{2mx}{x^2-\delta^2}+h(x),
\]

where `h` is analytic near `x=delta`.

The symmetric pair contributes

\[
 \mathcal D_{\rm pair}(x)
 =-\frac{4m\delta^2}{(x^2-\delta^2)^2}.
\]

Hence

\[
 \mathcal D_{\rm pair}(x)\longrightarrow-\infty
 \qquad(x\downarrow\delta,\ x>\delta).
\]

The remainder

\[
 \operatorname{Re}h'(x)+\frac1x\operatorname{Re}h(x)
\]

is bounded near `delta` because `delta>0`. Thus `D(s)<0` for all sufficiently
small right-hand displacements.

At the same time,

\[
 \operatorname{Re}F_{\rm pair}
 =\frac{2mx}{x^2-\delta^2}
 \longrightarrow+\infty.
\]

After possibly shrinking the interval, both `Re F>0` and `D<0` hold. Neither
point is a zero because `x>delta`. Continuity gives an open witness set, and the
density of rational or dyadic complex points supplies an exact finite witness.
∎

## Certificate schema consequence

A compact certificate requires:

1. exact dyadic `x,T` with `x>0`;
2. a complex ball for `xi(s)` excluding zero;
3. balls for `xi'(s)` and `xi''(s)`, or equivalently for `F(s)` and `F'(s)`;
4. one outward real interval for
   `Re F'(s) + Re F(s)/x` whose upper endpoint is negative;
5. evaluator and normalization fingerprints.

No eigenvalue, contour, winding count, or zero isolation is needed. The checker
reconstructs one point and one strict real sign.

## Analytic domain audit

- `xi` is entire and `F` is meromorphic with poles at its zeros.
- The evaluation point lies strictly in `Re(s)>1/2` and must be certified
  nonzero.
- The real number `x=Re(s)-1/2` is positive, so division by `x` is harmless.
- Under RH the differentiated zero-resolvent series converges absolutely at
  every fixed point in the open half-plane.
- In the converse, the pole pair is removed explicitly and the remainder is
  analytic in a disk containing no other occurrence of those poles.

## Dependency audit

- `D-3201` fixes `xi`, `F`, the corrected completion formula, and the half-plane
  normalization.
- `L-3201` supplies the zero-resolvent/Poisson expansion and its convergence
  interface.
- Functional-equation and conjugation symmetries supply the same-ordinate pair
  `1/2+/-delta+i gamma`.

## Gap audit

- The sign is
  `Re F' + Re F/x`, not `Re F' - Re F/x`.
- `F'` must be the complex derivative of `F`; differentiating only a sampled
  real midpoint is not a certificate.
- A ball for `xi` or `zeta` containing zero makes both `F` and `F'` unresolved.
- Near a pole, cancellation in `xi''/xi-F^2` can require substantial precision.
  The strict final interval, not the size of individual terms, controls.
- The converse proves existence of an open negative basin but gives no global
  width bound at an unknown high zero.
- A negative fitted-model derivative is proposal-only.

## Adversarial tests

1. For a finite synthetic critical-line zero set, compare `D` with the explicit
   nonnegative sum term by term.
2. For the quartet `{0.6+/-20i,0.4+/-20i}`, evaluate at `0.61+20i`; require
   `Re F>0` and `D<0` simultaneously.
3. Approach the synthetic right-hand pole with decreasing positive displacement
   and require `D` to diverge negatively.
4. Omit the `Re F/x` term and require the shifted-Stieltjes identity in `L-4102`
   to fail.
5. Inject the pre-correction sign error in the direct completion formula and
   require functional-equation calibration failure.

## Remaining uncertainty

No mathematical gap is known. Practical sensitivity, interval conditioning,
and the width of a high-zero witness basin remain empirical.

## Suggested next attack

Extend the Issue #39 Arb producer from a first-order to a second-order `xi` jet,
calibrate this sign on synthetic and known-line controls, then search paired
left/right horizontal offsets around every reconnaissance anomaly. The scalar
and differential tests should be evaluated together because a genuine off-line
pole predicts opposite-side basins.