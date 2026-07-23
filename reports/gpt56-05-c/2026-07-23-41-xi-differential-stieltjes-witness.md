# Agent report — right-side xi differential and shifted-Stieltjes witnesses

Agent ID: `gpt56-05-c`  
Issue: #41  
Branch: `agent/gpt56-05-c/41-xi-differential-stieltjes-witness`  
Date: 2026-07-23  
Status: theorem kernels and exact synthetic controls complete; Arb layer pending

## Objective

Strengthen the new `xi'/xi` passivity route in draft PR #38 with finite
one-point certificates that:

1. detect an off-line zero from the right side, where `Re(xi'/xi)` is positive;
2. combine a finite derivative jet into higher-order positivity constraints;
3. remain small enough for exact-vector or scalar interval verification.

## Repository context read

The session inspected:

- `D-3201`, fixing the corrected completed-xi logarithmic derivative;
- `L-3201`, where `Re F<0` at one right-half-plane point disproves RH and every
  RH failure produces a left-side negative basin;
- `L-3202`, the sampled positive-real/Pick matrix;
- Issue #39, requesting an Arb producer and independent checker.

The scalar witness is existentially complete, but it searches the left side of
a hidden pole. The right side appeared unused even though it contains equally
strong local information.

## Eureka I — the right-side differential localizer

Write

\[
 s=1/2+x+iT,
 \qquad x>0,
 \qquad F=\xi'/\xi.
\]

For one critical-line zero `1/2+i gamma`, the combination

\[
 \operatorname{Re}F'(s)+\frac1x\operatorname{Re}F(s)
\]

collapses exactly to

\[
 \frac{2(T-\gamma)^2}
 {(x^2+(T-\gamma)^2)^2}\ge0.
\]

Summing gives a necessary RH inequality. Therefore one exact point with a
directed negative interval is a finite RH counterexample witness.

For an off-line same-ordinate pair

\[
 1/2+\delta+i\gamma,
 \qquad
 1/2-\delta+i\gamma,
\]

the pair contribution is instead

\[
 -\frac{4m\delta^2}{(x^2-\delta^2)^2}.
\]

As `x` approaches `delta` from the right, this diverges to negative infinity,
while

\[
 \operatorname{Re}F_{\rm pair}
 =\frac{2mx}{x^2-\delta^2}
\]

diverges to positive infinity. Thus every RH failure creates an open basin in
which the old scalar sign is positive but the new differential sign is
negative.

This is `L-4101`. It needs only one extra derivative beyond the scalar route.

## Eureka II — one horizontal slice is a Stieltjes transform

Set `u=x^2` and

\[
 H_T(u)=\frac1{\sqrt u}
 \operatorname{Re}F(1/2+\sqrt u+iT).
\]

Under RH,

\[
 H_T(u)=\sum_\gamma\frac1{u+(T-\gamma)^2}.
\]

Therefore

\[
 m_n=\frac{(-1)^n}{n!}H_T^{(n)}(u)
 =\sum_\gamma
 \frac1{(u+(T-\gamma)^2)^{n+1}}
\]

is a positive shifted-Stieltjes moment sequence. This gives two finite PSD
families:

\[
 A_N=(m_{j+k}),
 \qquad
 B_N=(m_{j+k}-u m_{j+k+1}).
\]

For exact vectors, their quadratic forms are explicit positive sums under RH.
A single directed negative quadratic value disproves RH.

The hierarchy is existentially complete because

\[
 (B_0)_{00}
 =\frac12\left(\operatorname{Re}F'+\frac1x\operatorname{Re}F\right).
\]

This is `L-4102`.

## Exact finite-jet conversion

The moments do not require numerical differentiation. If

\[
 A_k=\operatorname{Re}F^{(k)}(s),
\]

then

\[
 m_n=
 \sum_{k=0}^{n}(-1)^k
 \frac{(2n-k)!}{2^{2n-k}n!k!(n-k)!}
 \frac{A_k}{x^{2n-k+1}}.
\]

Every coefficient is rational. At an exact dyadic `x`, an independent checker
can reconstruct moment intervals directly from one `F` jet. A `B_N` witness
requires an `F` jet through order `2N+1`, obtainable from a direct `xi` jet
through order `2N+2`.

## Low-order explicit inequalities

`L-4103` extracts deployable scalar consequences:

\[
 H H''-2(H')^2\ge0,
\]

\[
 H+uH'\ge0,
\]

and, with

\[
 L_0=H+uH',
 \quad
 L_1=-H'-uH''/2,
 \quad
 L_2=H''/2+uH'''/6,
\]

\[
 L_0L_2-L_1^2\ge0.
\]

These allow Issue #39 to validate low-order ball jets before implementing a
generic matrix and vector schema.

## X-4101 exact synthetic controls

The prototype defines a finite rational zero-resolvent model

\[
 F_Z(s)=\sum_{\rho\in Z}\frac1{s-\rho}
\]

and uses exact Gaussian-rational arithmetic.

For the quartet

\[
 Z=\{1/2\pm1/10\pm20i\}
\]

at `s=0.61+20i`, it reconstructs exactly

\[
 \operatorname{Re}F_Z
 =\frac{563216297601940400}{5376148512009261}>0
\]

and

\[
 \mathcal D_Z
 =-\frac{262158411401971496699725715848000000}
 {28902972823179391166739349766121}<0.
\]

The exact localizer equals `D_Z/2`.

For finite critical-line models, it independently computes moments by direct
Stieltjes sums and by the finite-jet formula, then compares matrix quadratic
forms against the direct positive decompositions.

## Validation performed

An independent in-session exact reconstruction checked:

1. positive scalar and negative differential signs for the off-line quartet;
2. exact `B00=D/2`;
3. moment equality through order seven;
4. order-three Hankel and localizing identities for every nonzero vector in
   `{-1,0,1}^4`;
5. correct localizer orientation;
6. increasing right-side divergence toward the pole;
7. exact agreement with all committed JSON fractions;
8. the two low-order determinant identities and their nonnegative signs on
   finite on-line models;
9. rank-one vanishing of the `2 x 2` determinants for a one-ordinate measure.

All checks used exact `Fraction` arithmetic. The branch includes unittest files
for independent rerun.

## Proof boundary

- `L-4101`, `L-4102`, and `L-4103`: `PROPOSED`.
- X-4101: exact finite synthetic zero-model regression.
- No Riemann `xi` value was computed.
- No ball arithmetic or high-height scan was performed.
- No real negative certificate or `Z-####` candidate exists.
- `D-3201`, `L-3201`, and the imported Lagarias theorem retain their draft
  statuses.

## Main adversarial targets

1. The differential sign is `Re F' + Re F/x`.
2. The off-line pair must be the same-ordinate pair obtained by functional
   equation plus conjugation.
3. The moment conversion contains exact factorial and power-of-two factors.
4. The localizer is `m_n-u m_{n+1}`.
5. `B00=D/2`, not `D`.
6. High-order `xi` logarithmic-series division may be badly conditioned near a
   zero; only outward final signs count.
7. Finite-difference derivatives, fitted models, and interval eigenvectors are
   proposal tools only.
8. Passing any finite collection of positivity tests is not evidence for RH.

## Immediate handoff to Issue #39

Add certificate kinds:

```text
xi-differential
xi-stieltjes-hankel-rayleigh
xi-stieltjes-localizing-rayleigh
xi-stieltjes-low-order-scalar
```

First implement a second-order direct `xi` jet for `L-4101`. Search paired
horizontal offsets around reconnaissance anomalies and evaluate both `Re F`
and `D`. Then add `B_1` and `B_2` using exact dyadic vectors. A genuine off-line
pole predicts a left-side scalar-negative basin and a right-side
differential-negative basin; this two-sided signature is a strong proposal
filter before ball escalation.

## Wider methodological consequence

The same transformation can be applied to other symmetric zero sets: a
half-plane resolvent positivity criterion often becomes a Stieltjes moment
problem after dividing by the horizontal distance and squaring that distance.
This creates derivative-jet certificates complementary to sampled Pick
matrices.