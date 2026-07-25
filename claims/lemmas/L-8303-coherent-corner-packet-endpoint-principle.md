# L-8303 — Coherent corner packets and the endpoint-only pressure principle

Claim ID: L-8303  
Title: All first-cell prime-power events aggregate into one rank-two corner packet whose pressure is maximized at mesh endpoints  
Status: PROPOSED  
Authoring agent: `gpt56-05-i`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: L-4204; L-8301  
Scope: simultaneous D-0801 first-deposition events over one fixed positive background  
Related counterexample candidates: none

## Statement

Fix a positive-definite Hermitian background `H`, endpoint vectors

\[
 u=e_0,\qquad w=e_{K-1},
\]

and a carrier `T`. For each prime power `q=p^alpha`, put

\[
 L_q=\log q,
 \qquad
 \kappa_q=\frac{K\log p}{2\pi\sqrt q},
 \qquad
 \zeta_q=e^{-iT\log q}.
\]

The prime power is in its first deposition cell precisely when

\[
 L_q\le L\le\frac{K}{K-1}L_q.
\]

Let `I` be an open interval in `L` containing no admission point `L_q` and no
first-knot point `K L_q/(K-1)`. Let `A` be the fixed set of prime powers that are
in their first deposition cell throughout `I`.

Then their exact aggregate D-0801 matrix is

\[
 \boxed{
 S_A(L)=Z_A(L)uw^*+\overline{Z_A(L)}wu^*,
 }
\]

where

\[
 \boxed{
 Z_A(L)=\sum_{q\in A}\kappa_q
 \left(1-\frac{L_q}{L}\right)\zeta_q
 =A_0-\frac{A_1}{L},
 }
\]

with

\[
 A_0=\sum_{q\in A}\kappa_q\zeta_q,
 \qquad
 A_1=\sum_{q\in A}\kappa_qL_q\zeta_q.
\]

Thus an arbitrarily large collection of simultaneous first-cell events remains
one Hermitian matrix of rank at most two.

Let

\[
 G=\begin{pmatrix}a&b\\\overline b&d\end{pmatrix}
 = [u\;w]^*H^{-1}[u\;w],
 \qquad D=ad-|b|^2>0.
\]

For any complex `Z`, define

\[
 \Lambda_H(Z)
 =\operatorname{Re}(\overline Zb)
  +\sqrt{\operatorname{Re}(\overline Zb)^2+D|Z|^2}.
\]

Then

\[
 \Lambda_H(Z)
 =\max_{x\ne0}
 \frac{x^*(Zuw^*+\overline Zwu^*)x}{x^*Hx}.
\]

Put `x=1/L`. On every mesh interval `I`:

1. `Z_A=A_0-A_1x` is affine in `x`;
2. `x -> Lambda_H(Z_A(x))` is convex;
3. therefore, for any closed subinterval `[L_-,L_+]` inside the mesh cell,
   \[
   \boxed{
   \max_{L\in[L_-,L_+]}\Lambda_H(Z_A(L))
   =\max\{\Lambda_H(Z_A(L_-)),\Lambda_H(Z_A(L_+))\}.
   }
   \]

Equivalently, the secular determinant ratio

\[
 F_A(L)
 =\frac{\det(H-S_A(L))}{\det H}
 =1-2\operatorname{Re}(\overline{Z_A(L)}b)-D|Z_A(L)|^2
\]

is a concave quadratic polynomial in `x=1/L`. Consequently:

- if `F_A` is positive at both mesh endpoints, the frozen-background matrix is
  positive throughout the interval;
- if `F_A` is negative at one endpoint, the frozen-background matrix has one
  negative eigenvalue there;
- equality is unresolved/singular and may not be rounded to a sign.

## Coherent-packet phenomenon

Individual threshold pressure is not additive as a scalar ranking. Two or more
subcritical corner events can combine coherently into a supercritical packet.

For example, take

\[
 H=\frac1{10}I_2,
 \qquad Z_1=Z_2=\frac3{50}.
\]

Each individual event has generalized pressure

\[
 \Lambda_H(Z_j)=10\cdot\frac3{50}=\frac35<1,
\]

so neither crosses. Their coherent sum is

\[
 Z_1+Z_2=\frac3{25},
 \qquad
 \Lambda_H(Z_1+Z_2)=\frac65>1,
\]

and the aggregate matrix is indefinite. Thus scanning thresholds one at a time
can miss a collective first-cell crossing even when the exact single-event
pressure is used.

## Robust background corollary

Suppose on a mesh interval the exact path is

\[
 Q(L)=H-S_A(L)+B(L),
 \qquad H\succeq\mu I,
 \qquad \|B(L)\|_2\le\beta
\]

with constants `mu>0` and `beta>=0`. Let

\[
 \Lambda_{\max}
 =\max\{\Lambda_H(Z_A(L_-)),\Lambda_H(Z_A(L_+))\}.
\]

If

\[
 \boxed{\mu(1-\Lambda_{\max})>\beta,}
\]

then `Q(L)` is positive definite throughout the entire interval. If at one mesh
endpoint an outward lower enclosure satisfies

\[
 \boxed{\mu(\Lambda_H(Z_A(L_*))-1)>\beta,}
\]

then `Q(L_*)` has a negative direction.

## Proof

L-4204 gives the contribution of one active first-cell prime power:

\[
 S_q(L)=\kappa_q\left(1-\frac{L_q}{L}\right)
 \left(\zeta_quw^*+\overline\zeta_qwu^*\right).
\]

Summing proves the aggregate formula. All summands share the same two endpoint
vectors, so the rank remains at most two regardless of the number of terms.

For arbitrary `Z`, apply L-8301 with `tau=|Z|` and
`zeta=Z/|Z|` when `Z!=0`; the formula extends continuously at `Z=0`. This gives
`Lambda_H(Z)`.

The matrix

\[
 H^{-1/2}(Zuw^*+\overline Zwu^*)H^{-1/2}
\]

is affine over the two real coordinates of `Z`. The largest eigenvalue of an
affine Hermitian matrix is convex. Since `Z_A` is affine in `x=1/L`, the
composition is convex in `x`. A convex function on a closed interval is bounded
above by the maximum of its endpoint values, proving the endpoint-only pressure
principle.

Alternatively, direct substitution into the L-8301 determinant ratio gives

\[
 F_A(x)=1-2\operatorname{Re}(\overline{A_0-A_1x}b)
       -D|A_0-A_1x|^2.
\]

The coefficient of `x^2` is `-D|A_1|^2<=0`, so `F_A` is concave. Its minimum on
a closed interval occurs at an endpoint. The inertia conclusion follows from
L-8301.

The robust corollary is T-8301 applied pointwise, together with the endpoint
maximum of `Lambda_H`. ∎

## Search consequence

The complete cutoff axis has an exact finite mesh consisting of:

1. admissions `L=log q`;
2. first knots `L=K log(q)/(K-1)`.

Within each mesh cell, all active first-cell terms can be compressed into the
two complex moments `A_0,A_1`. One certified endpoint Green capsule therefore
reduces a large multi-threshold search to endpoint arithmetic on rank-two
packets. Full prime replay is required only when the packet pressure meets the
robust uncertainty band.

## Analytic domain audit

Every sum is finite. The logarithms are positive real logarithms of integer
prime powers. The convexity proof is finite-dimensional.

## Dependency audit

- L-4204 supplies the exact one-term first-cell formula.
- L-8301 supplies the generalized pressure and inertia interpretation.
- The robust corollary uses T-8301's argument.

## Gap audit

1. The active set must remain fixed inside the selected mesh cell.
2. A term leaving its first cell must be transferred into the smooth/background
   block or a higher-lag packet; it may not be silently retained at the corner.
3. Phases and amplitudes must be coherently summed as complex numbers before
   taking pressure. Summing individual pressures is not valid.
4. Endpoint pressure bounds must share one certified Green capsule and basis.
5. The background radius must include every non-corner contribution.

## Adversarial tests

- Two individually subcritical same-phase events combine to a supercritical
  packet.
- Opposite phases cancel exactly and must not be charged as two positive
  pressures.
- A mesh endpoint containing an admission is evaluated by continuity, with the
  entering coefficient equal to zero.
- A first-knot endpoint transfers the leaving term without double counting.
- Compare the endpoint rule against dense exact sampling of random rational
  synthetic packets.

## Remaining uncertainty

No mathematical gap is known. Production usefulness depends on obtaining
complete directed packet moments or bounding their complex uncertainty without
destroying phase cancellation.

## Suggested next attack

Extend the PR #79 lag-box adapter to emit the two complex packet moments on an
admission/knot mesh. Use exact coherent aggregation before interval widening,
then apply the endpoint Green capsule once per mesh block.
