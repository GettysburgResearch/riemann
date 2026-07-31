# L-15620 — Berezin-clipped symbol capacity

Claim ID: `L-15620`  
Title: The dangerous clipped operator trace is bounded by the symbol deficit at the desired floor, independently of the auxiliary level `G`  
Status: `PROPOSED — COMPLETE ABSTRACT PROOF`  
Authoring agent: `gpt56-pro-09-f`  
Created: 2026-07-31  
Dependencies: `L-15618`; Plancherel; scalar Jensen inequality; the diagonal of the time-limiting reproducing kernel  
Scope: proof-facing arithmetic form of the exact clipped saturation gate  
Related counterexample candidates: none

## 1. Localization operator

Let `I` be a bounded interval of length `|I|`. Extend vectors in `L^2(I)` by
zero and use

\[
 \|f\|_2^2
 =\frac1{2\pi}\int_\mathbb R|\widehat f(\xi)|^2d\xi.
 \tag{L-15620.1}
\]

For a measurable nonnegative symbol `w`, define

\[
 D_w=P_I\mathcal F^{-1}M_w\mathcal FP_I.
 \tag{L-15620.2}
\]

Assume the right side below is finite.

## 2. Convex trace inequality

Let `Phi:[0,infinity)->[0,infinity)` be convex with `Phi(0)=0`. Then

\[
 \boxed{
 \operatorname{Tr}\Phi(D_w)
 \le
 \frac{|I|}{2\pi}
 \int_\mathbb R\Phi(w(\xi))d\xi.}
 \tag{L-15620.3}
\]

### Proof

Let `lambda_n` be the positive eigenvalues of `D_w` and choose orthonormal
eigenfunctions `u_n`. Plancherel gives

\[
 \lambda_n
 =\frac1{2\pi}
 \int_\mathbb Rw(\xi)|\widehat u_n(\xi)|^2d\xi,
 \tag{L-15620.4}
\]

while

\[
 \frac1{2\pi}\int|\widehat u_n|^2=1.
\]

Scalar Jensen therefore gives

\[
 \Phi(\lambda_n)
 \le\frac1{2\pi}
 \int\Phi(w(\xi))|\widehat u_n(\xi)|^2d\xi.
 \tag{L-15620.5}
\]

Sum over the complete orthonormal eigenbasis, adding a basis of the kernel when
necessary. For each fixed `xi`, Parseval applied to the time-limited plane wave
gives

\[
 \sum_n|\widehat u_n(\xi)|^2=|I|.
 \tag{L-15620.6}
\]

Tonelli's theorem then proves (L-15620.3). QED.

## 3. Exact clipping identity

Take

\[
 \Phi_\theta(x)=(x-\theta)_+.
 \tag{L-15620.7}
\]

Then

\[
 \boxed{
 \operatorname{Tr}(D_w-\theta I)_+
 \le\frac{|I|}{2\pi}
 \int_\mathbb R(w(\xi)-\theta)_+d\xi.}
 \tag{L-15620.8}
\]

Now let a real lower symbol `s` and an auxiliary level `G` define

\[
 w_G(\xi)=(G-s(\xi))_+,
 \qquad
 D_G=D_{w_G}.
 \tag{L-15620.9}
\]

For any `Gamma<=G`, put

\[
 \theta=G-\Gamma.
\]

The scalar identity

\[
 \boxed{
 \bigl((G-s)_+-(G-\Gamma)\bigr)_+
 =(\Gamma-s)_+}
 \tag{L-15620.10}
\]

holds pointwise. Hence

\[
 \boxed{
 \operatorname{Tr}
 \bigl(D_G-(G-\Gamma)I\bigr)_+
 \le
 \frac{|I|}{2\pi}
 \int_\mathbb R(\Gamma-s(\xi))_+d\xi.}
 \tag{L-15620.11}
\]

The auxiliary level `G` has disappeared from the arithmetic quantity.

## 4. Exact scalar saturation theorem

Suppose the same localized operator satisfies

\[
 A\succeq GI-D_G,
 \tag{L-15620.12}
\]

and a `d`-dimensional packet `L` satisfies

\[
 A|_L\preceq\alpha I_L,
 \qquad
 \alpha<\Gamma\le G.
 \tag{L-15620.13}
\]

If

\[
 \boxed{
 \frac{|I|}{2\pi}
 \int_\mathbb R(\Gamma-s(\xi))_+d\xi
 \le d(\Gamma-\alpha),}
 \tag{L-15620.14}
\]

then

\[
 \boxed{A|_{L^\perp}\succeq\Gamma I.}
 \tag{L-15620.15}
\]

### Proof

Equation (L-15620.11) and (L-15620.14) give

\[
 \operatorname{Tr}
 \bigl(D_G-(G-\Gamma)I\bigr)_+
 \le d(\Gamma-\alpha).
\]

This is exactly the danger-threshold condition (L-15618.17). Apply
`L-15618`. QED.

On the scaled Suzuki interval `I=[-1,1]`, the proof-facing condition is

\[
 \boxed{
 \frac1\pi
 \int_\mathbb R(\Gamma-s_a(\xi))_+d\xi
 \le d_a(\Gamma-\alpha_a).}
 \tag{L-15620.16}
\]

## 5. Layer-cake sublevel-set form

The phase-space deficit is

\[
 \boxed{
 \int_\mathbb R(\Gamma-s(\xi))_+d\xi
 =\int_{-\infty}^{\Gamma}
 |\{\xi:s(\xi)<u\}|du.}
 \tag{L-15620.17}
\]

Therefore the complete scalar gate can be certified from directed sublevel-set
measure bounds at levels below `Gamma`. It is not necessary to integrate the
full depth `G-s`, nor to charge symbol cells whose deficit is too shallow to
cross the target floor.

## 6. Relation to the requested full-trace inequality

The originally requested condition

\[
 \operatorname{Tr}D_G-d(G-\alpha)\le G-\Gamma
 \tag{L-15620.18}
\]

also proves the floor, by `L-15612`, but is not sharp. It charges all shallow
eigenvalues of `D_G` and retains a spurious dependence on `G`.

Equations (L-15620.14)--(L-15620.16) are a strict structural improvement:

- the operator is clipped at the exact crossing threshold;
- the symbol is evaluated directly at `Gamma`;
- the auxiliary construction level cancels;
- modern bad-set/plunge estimates enter through the layer-cake measure;
- the finite example of `L-15618` passes (L-15620.14) while failing the full
  trace condition by an arbitrarily large amount.

## 7. Exact finite and directed interface

A production certificate needs only:

1. a directed complete lower symbol `s_lower` for the same operator;
2. a rational target floor `Gamma`;
3. a directed finite-cell enclosure of
   \[
   \int(\Gamma-s_lower)_+;
   \]
4. exact packet rank `d`;
5. a directed packet compression endpoint `alpha<Gamma`;
6. a rational verification of (L-15620.14).

Every symbol or assembly radius is inserted into `s_lower` before taking the
positive part. No packet Fourier leverage or principal angle is required.

## 8. Cofinal consequence

If an unbounded support sequence satisfies

\[
 \frac{|I_j|}{2\pi}
 \int(\Gamma_j-s_j)_+
 \le d_j(\Gamma_j-\alpha_j)
 \tag{L-15620.19}
\]

and the near-radical residual rates of `L-15617` or `L-15619`, then exact
low-index saturation holds at every retained level. The inverse-Ritz lower
floor of `T-15602` tends to zero, and the existing cofinal lower-envelope theorem
implies RH.

## 9. Proof boundary

- The convex trace theorem and clipping identity are exact.
- The remaining zeta-specific statement is the cofinal directed phase-space
  inequality (L-15620.19).
- A midpoint symbol scan or a finite support ladder does not prove it.
- The theorem removes the unnecessary full-trace burden but does not establish
  the arithmetic sublevel integral.
- No proof of RH is claimed.
