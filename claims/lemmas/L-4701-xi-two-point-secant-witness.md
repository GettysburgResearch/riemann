# L-4701 — A two-point value-only xi secant witness

Claim ID: L-4701  
Title: Two values of `xi'/xi` can certify the right-side RH failure detected by L-4101  
Status: PROPOSED  
Authoring agent: `gpt56-05-d`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-3201; the critical-line logarithmic-derivative expansion used in L-3201/L-4101  
Scope: derivative-free finite point certificates in `Re(s)>1/2`  
Related counterexample candidates: none

## Statement

Use the D-3201 normalization

\[
 F(s)=\frac{\xi'(s)}{\xi(s)}.
\]

For real `T`, positive `x`, and a point

\[
 s_x=\frac12+x+iT
\]

at which `xi` is nonzero, put

\[
 R_T(x)=\operatorname{Re}F(s_x),
 \qquad
 J_T(x^2)=xR_T(x).
\]

Let `0<x_1<x_2`, write `u_j=x_j^2`, and define the value-only secant

\[
 \mathcal S_T(x_1,x_2)
 =\frac{x_2R_T(x_2)-x_1R_T(x_1)}{x_2^2-x_1^2}
 =\frac{J_T(u_2)-J_T(u_1)}{u_2-u_1}.
\]

If RH holds, then

\[
 \mathcal S_T(x_1,x_2)
 =\sum_\gamma
 \frac{(T-\gamma)^2}
 {(x_1^2+(T-\gamma)^2)(x_2^2+(T-\gamma)^2)}
 \ge0.
\]

Consequently, exact rational or dyadic `T,x_1,x_2`, rigorous nonzero
certificates for both xi values, and a directed enclosure

\[
 \mathcal S_T(x_1,x_2)<0
\]

form a finite unconditional counterexample witness to RH.

Conversely, if RH is false, then there is a nonempty open set of triples
`(T,x_1,x_2)` with

\[
 0<x_1<x_2,
 \qquad R_T(x_1)>0,
 \qquad R_T(x_2)>0,
 \qquad \mathcal S_T(x_1,x_2)<0.
\]

In particular, rational or dyadic triples of this type exist. Thus the
value-only two-point criterion is existentially complete: every RH failure
creates such a certificate, even though locating it may be difficult.

Finally, the confluent limit is the L-4101 differential localizer:

\[
 \lim_{x_2\to x_1=x}\mathcal S_T(x_1,x_2)
 =\frac12\left(
   \operatorname{Re}F'(s_x)+\frac1x\operatorname{Re}F(s_x)
 \right).
\]

## Motivation

L-4101 turns a negative first-order xi jet into a compact RH-disproof witness.
The present lemma removes the derivative entirely. A producer needs only two
independently enclosed values of `F`, exact multiplication by the horizontal
offsets, and one exact rational division.

This is valuable near enormous heights, where a derivative jet may be much more
expensive or ill-conditioned than two nearby simultaneous zeta evaluations.
It also gives an immediate finite-difference calibration of every future
L-4101 implementation.

## Proof under RH

Assume RH. Every nontrivial zero, with multiplicity, has the form

\[
 \rho=\frac12+i\gamma.
\]

The conjugate-paired logarithmic-derivative expansion used in L-3201 gives, for
`x>0`,

\[
 R_T(x)=\sum_\gamma
 \frac{x}{x^2+(T-\gamma)^2}.
\]

The series is absolutely convergent at every fixed right-half-plane point.
Multiplying by `x` and writing `u=x^2` gives

\[
 J_T(u)=\sum_\gamma\frac{u}{u+a_\gamma},
 \qquad a_\gamma=(T-\gamma)^2\ge0.
\]

For every `a>=0` and `u_1<u_2`,

\[
 \frac{u_2/(u_2+a)-u_1/(u_1+a)}{u_2-u_1}
 =\frac{a}{(u_1+a)(u_2+a)}\ge0.
\]

Summing gives the displayed secant formula. The secant series converges
absolutely because its summand is `O((T-gamma)^-2)` for large ordinates, and the
standard zero-counting growth makes the corresponding zero sum convergent.
A rigorous negative enclosure contradicts the RH consequence.

For the confluent identity, differentiate `J_T(u)=xR_T(x)` with `u=x^2`:

\[
 \frac{dJ_T}{du}
 =\frac1{2x}\frac{d}{dx}\{xR_T(x)\}
 =\frac12\left(R_T'(x)+\frac{R_T(x)}x\right).
\]

Horizontal differentiation gives
`R_T'(x)=Re F'(1/2+x+iT)`, proving the limit.

## Converse and right-side geometry

Assume RH is false. Zero symmetry supplies a zero

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad \delta>0,
\]

of multiplicity `m>=1`, together with the same-ordinate reflected zero

\[
 1-\overline\rho=\frac12-\delta+i\gamma
\]

of the same multiplicity. In a sufficiently small horizontal neighborhood of
`x=delta`, subtract these two poles and write

\[
 F\left(\frac12+x+i\gamma\right)
 =\frac{m}{x-\delta}+\frac{m}{x+\delta}+h(x),
\]

where `h` is analytic in that neighborhood.

The pole pair contributes

\[
 R_{\rm pair}(x)=\frac{2mx}{x^2-\delta^2},
 \qquad
 J_{\rm pair}(u)=\frac{2mu}{u-\delta^2}.
\]

For `delta^2<u_1<u_2`, its exact secant is

\[
 \frac{J_{\rm pair}(u_2)-J_{\rm pair}(u_1)}{u_2-u_1}
 =-\frac{2m\delta^2}
 {(u_1-\delta^2)(u_2-\delta^2)}.
\]

This tends to negative infinity as both nodes approach `delta^2` from the
right. The background

\[
 J_h(u)=\sqrt u\,\operatorname{Re}h(\sqrt u)
\]

is continuously differentiable there, so its nearby secants are bounded.
Hence sufficiently close right-side nodes give a negative total secant.
Meanwhile `R_pair(x)` tends to positive infinity from the right, so the two
scalar real parts are both positive after the nodes are chosen close enough.

All inequalities are strict and the evaluation points avoid the pole.
Continuity therefore preserves them under small perturbations of `T,x_1,x_2`.
Density supplies exact rational or dyadic triples in that open set.

## Proof-oriented certificate

A certificate needs only:

1. exact dyadic `T,x_1,x_2` with `0<x_1<x_2`;
2. complex balls for `xi(s_1),xi(s_2)` excluding zero, or audited zeta balls
   with all completion factors;
3. real balls for `Re F(s_1),Re F(s_2)`;
4. exact interval propagation through
   \[
   \frac{x_2\operatorname{Re}F(s_2)-x_1\operatorname{Re}F(s_1)}
        {x_2^2-x_1^2};
   \]
5. a final upper endpoint strictly below zero;
6. a producer fingerprint and deterministic serialization.

The checker does not differentiate, fit, interpolate, or locate a zero.

## Analytic domain audit

- Every evaluation point lies strictly in `Re(s)>1/2`.
- `F` is meromorphic and division is licensed only after the exact point is
  proved not to be a zero of `xi`.
- Under RH the right half-plane is zero-free and the resolvent formula applies.
- The converse works in a zero-free punctured neighborhood to the right of an
  isolated off-line zero.
- All square roots use the positive real branch because `u=x^2>0`.
- No complex logarithm or contour deformation occurs.

## Dependency audit

- D-3201 fixes `xi`, `F`, the functional equation, and the corrected completion
  convention.
- The zero-resolvent expansion is the same imported interface used by L-3201,
  L-3202, and L-4101.
- The converse uses only the local principal part of a meromorphic logarithmic
  derivative plus the standard xi zero symmetries.

## Gap audit

1. Two negative floating midpoints are not a certificate; the final secant
   interval must have negative upper endpoint.
2. The denominator is `x_2^2-x_1^2`, not `x_2-x_1`.
3. Each xi or zeta denominator ball must exclude zero independently.
4. Evaluating extremely close to a pole can make both `F` balls useless; the
   search must balance pole dominance against interval division width.
5. A negative secant of a fitted rational surrogate is proposal-only.
6. Lower-height synthetic or calibration witnesses are not Riemann
   counterexamples.
7. The imported logarithmic-derivative normalization remains PROPOSED until
   independently reconstructed.

## Adversarial tests

1. For a finite critical-line zero multiset, evaluate the exact secant and
   compare with the positive resolvent formula.
2. For the symmetric off-line pair `1/2+-delta+i gamma`, verify the exact
   negative expression above to the right of the pole.
3. Add a large positive critical-line background and confirm that sufficiently
   near-pole right-side nodes still become negative.
4. Swap `x_1,x_2`; the quotient must remain unchanged, while malformed node
   ordering in the certificate must be rejected rather than silently repaired.
5. Let the nodes coalesce numerically and compare with the separately evaluated
   L-4101 differential expression.
6. Widen either `F` ball until the secant interval reaches zero and require
   `UNRESOLVED`.

## Remaining uncertainty

The elementary secant and local-pole arguments appear complete. The practical
width of the negative two-point region for an actual high off-line zero is
unknown, and a rigorous high-height value-only producer has not yet been built.

## Suggested next attack

Extend Issue #39's planned Arb evaluator to accept pairs of exact dyadic
horizontal offsets at one height. Search scalar passivity on the left and the
present secant on the right in one shared zeta-evaluation batch. Escalate only
strictly separated negative intervals to candidate review.
