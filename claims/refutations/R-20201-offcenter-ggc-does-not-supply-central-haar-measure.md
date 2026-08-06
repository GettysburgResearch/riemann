# R-20201 — Off-center GGC structure does not supply the central Haar measure by analytic continuation

Claim ID: `R-20201`  
Title: Positive reciprocal-xi representations to the right of one do not prove the central complete-monotonicity criterion  
Status: `PROPOSED SCOPE CORRECTION — PENDING INDEPENDENT LITERATURE REVIEW`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Scope: the probability-law shortcut suggested by the real-axis criterion `T-20202`  
Related counterexample candidates: none

## 1. What is available unconditionally

For a fixed real `alpha>1`, Euler's product, the gamma integral, and the rational
completion terms give positive Lévy/Thorin-type representations for ratios of
the form

\[
 {\xi(\alpha)\over\xi(\alpha+s)}.
\]

The prime contribution is positive because the Dirichlet series is absolutely
convergent and contains the positive measure

\[
 \sum_{n\ge2}{\Lambda(n)\over\log n}\,\delta_{\log n}.
\]

This is a genuine and useful off-center probability structure. It explains why
all derivatives needed by the `T-20202` real-axis packet are accessible without
Riemann--Siegel evaluation.

## 2. The central representation is RH-bearing

At the central point, a GGC representation of

\[
 {\xi(1/2)\over\xi(1/2+\sqrt u)}
\]

would give a zero-free analytic continuation in the slit `u`-plane. Under the
map `u=(s-1/2)^2`, this excludes every zero off the critical line; functional
equation symmetry then gives RH.

Under RH the canonical product indeed yields the Thorin measure

\[
 \sum_{\gamma>0}m_\gamma\,\delta_{\gamma^2},
\]

so the central GGC statement is equivalent to the missing zero-location
information, not an unconditional input.

Likewise, `T-20202` asks for the positive measure

\[
 \mathcal D_2(t)e^{-y_0t}\,dt.
\]

Producing that measure is exactly the all-order positivity theorem.

## 3. Why analytic continuation is insufficient

An analytic identity may be continued while any of the following properties are
lost:

- complete monotonicity on a real ray;
- positivity of a Lévy or Thorin measure;
- absence of zeros in the slit plane;
- the Laplace-transform interpretation of the continued expression.

The off-center formulas contain an `alpha`-dependent positive measure and an
`alpha`-dependent drift. Substituting complex arguments and using the functional
equation gives a meromorphic identity, but it does not prove that the resulting
central exponent is the Laplace exponent of a positive measure.

In particular, writing an off-center completely monotone density schematically
as

\[
 \nu_\alpha(t)=\int e^{-tx}\,U_\alpha(dx),
 \qquad U_\alpha\ge0,
\]

does not justify a central decomposition

\[
 \nu_{1/2}(t)=\sum_{\gamma>0}e^{-\gamma^2t}
\]

until the zeros `gamma` are already known to be real. That last step is the RH
content.

## 4. Consequence for the Haar attack

The valid literature interfaces are:

1. off-center positive probability representations for numerical and analytic
   control at `Re(s)>1`;
2. central infinitely-divisible/GGC criteria as equivalent reformulations of
   RH;
3. the Nakamura--Suzuki screw characteristic-function criterion, again
   RH-equivalent.

None supplies the positive representing measure required by `T-20202` for free.
A proof must still establish one of:

\[
 \mathcal D_2(t)\ge0,
\]

an explicit positive measure for `mathcal L_2`, an all-positive Stieltjes
continued fraction, or the complete Hankel hierarchy.

The off-center formulas may help construct such a proof, but only through an
additional order-preserving theorem for their measures. Mere analytic
continuation is not order preserving.

## 5. Literature positioning

This scope correction is consistent with:

- Biane--Pitman--Yor's probability laws attached to theta/zeta integrals;
- Nakamura's complete zeta distributions and quasi-infinite divisibility away
  from the center;
- Nakamura--Suzuki's modern statement that an infinitely divisible screw
  characteristic function is equivalent to RH;
- proposed central GGC factorizations, whose central positive measure must be
  treated as the theorem to prove rather than an imported lemma.

## 6. Proof boundary

- This file does not reject the valid off-center GGC formulas.
- It does not provide a counterexample to a fully specified central
  factorization.
- It blocks only the inference that positivity of the representing measure
  survives analytic continuation automatically.
- A detailed publication claim about any named paper requires an independent
  line-by-line source review; the present conclusion is a proof-interface scope
  rule for this repository.