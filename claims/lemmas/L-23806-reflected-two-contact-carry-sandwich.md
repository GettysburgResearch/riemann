# L-23806 — Reflected two-contact carry sandwich

Claim ID: `L-23806`  
Title: Reflected Selberg recombination contracts both carry-packing slack and carry-cover excess through two-contact scalar faces  
Status: **FULL-PROOF HINGE — PROPOSED PENDING SYMBOLIC FACE ENUMERATION**  
Authoring agents: `gpt56-pro`, `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `D-23801`, `L-23801`--`L-23803`; PR #226 `L-9516`; PR #233 finite Möbius resolvent; PR #158 high-order Euler closure  
Scope: source-specific carry sandwich; no arbitrary-vector BTP claim

## 1. Two carry deficits

Let `mathfrak L(X)` and `mathfrak U(X)` be the nonnegative packing and covering
values of `L-23802`. Define

\[
 \Delta_X^-
 =\bigl(4\sqrt X-\mathfrak L(X)\bigr)_+,
 \qquad
 \Delta_X^+
 =\bigl(\mathfrak U(X)-4\sqrt X\bigr)_+,
 \tag{L-23806.1}
\]

and

\[
 \Delta_X=1+\Delta_X^-+\Delta_X^+.
 \tag{L-23806.2}
\]

Fix one reserve `0<delta<1/3`. The proposed theorem is: for every sufficiently
large fixed packet order `K`,

\[
 \boxed{
 \Delta_X
 \le
 X^{2/K+o_K(1)}
 \left[
 1+
 \max_{2\le Y\le X^{1-\delta}e^{O_K(1)}}
 \Delta_Y
 \right].}
 \tag{L-23806.3}
\]

This is stronger than the one-sided greedy-mass target and weaker than exact
Carry Saturation. The packing and covering certificates may be different.

## 2. Möbius-curvature coordinates

For the target ramp `w_X`, define

\[
 u_X(m)=\sum_{k\le X/m}\mu(k)w_X(mk),
 \qquad
 F_X(j)=\frac1{j-1}\sum_{m=j}^Xu_X(m).
 \tag{L-23806.4}
\]

The exact inverse is

\[
 c_X(j)=(j+1)\Delta^2F_X(j).
 \tag{L-23806.5}
\]

A nonnegative packing is a convex profile whose reconstructed residual is
nonnegative. A nonnegative cover is a convex profile whose reconstructed
residual is nonpositive. Thus the carry sandwich is a pair of scalar convex
obstacles around the same signed Möbius profile.

This representation retains the first-cell Mertens mode and forbids unsigned
termwise estimates.

## 3. Exact finite reflected packet

Put

\[
 V=\lceil X^{1/K}\rceil,
 \quad
 \mu_V=\mu\mathbf1_{n\le V},
 \quad
 r_V=\varepsilon-\mathbf1*\mu_V.
 \tag{L-23806.6}
\]

For `n<=X`,

\[
 \mu(n)=\sum_{j=0}^{K-1}(\mu_V*r_V^{*j})(n).
 \tag{L-23806.7}
\]

Apply this exact finite resolvent in both polarized obstacle factors. Equal
arithmetic destinations are recombined before taking a norm, positive part, or
negative part. There is no analytic inverse-zeta remainder below `X`.

## 4. Complete first-crossing partition

The fully recombined packet is divided into:

1. **free-variable rows:** one unrestricted lattice variable carries a fixed
   fraction of `log X`; PR #158's arbitrarily high Euler theorem makes these
   exponentially small;
2. **strict-scale rows:** the exposed product is at most
   `X^(1-delta)e^(O_K(1))` and is charged to `Delta_Y`;
3. **same-scale obstacle rows:** these are retained and treated by the reflected
   scalar obstacle.

The balanced class is not removed by `L-23203` or by assuming `BTP(K)`.

## 5. Reflected Hermitian energy

PR #226 supplies the exact reflected Selberg identity

\[
 C_\times-C_+-C_-=2\Lambda_+*\Lambda_-.
 \tag{L-23806.8}
\]

After the safe-window twist integral, the right side is the positive Hermitian
energy of the complete same-scale obstacle residual. The diagonal is retained;
it is never bounded entrywise. High-order null moments remove the recombined
interior polynomial and pole-model densities.

The packing slack and covering excess are evaluated together. An excursion
which obstructs the lower envelope creates usable excess in the upper envelope,
and conversely. This is the carry analogue of pairing the two reflected
Selberg factors before taking signs.

## 6. Two-contact terminal geometry

After all frozen divisor coordinates and strict lower-scale contacts are fixed,
a scalar terminal face is one maximal interval on which its convex profile is
affine. Its curvature/contact measure is therefore supported at the two ends:

\[
 \nu_{a,b}=A\delta_a+B\delta_b.
 \tag{L-23806.9}
\]

The proposed structural assertion is

\[
 \boxed{
 \#\{\text{free same-scale divisor/contact coordinates}\}\le2}
 \tag{L-23806.10}
\]

for every completely recombined terminal face, in both the packing and covering
obstacles.

Each free endpoint coordinate is at most

\[
 V^{1+o(1)}=X^{1/K+o_K(1)}.
 \tag{L-23806.11}
\]

Hence the same-scale ledger costs at most

\[
 X^{2/K+o_K(1)},
 \tag{L-23806.12}
\]

which gives (L-23806.3).

## 7. Mandatory first-cell mutation

The packet must reproduce the exact fixed-ratio Mertens increment of PR #229.
The packing and covering mutations must enclose the same scalar coefficient from
opposite sides with the exponent `2/K+o_K(1)`. A face dictionary which deletes
or unsigned-bounds that coordinate is invalid.

## 8. Decisive review

The theorem is rejected by any one of:

1. a genuine same-scale recombined face with three free contacts;
2. a balanced row discharged only by a previously assumed BTP induction;
3. an interior row not killed by the declared null quotient;
4. a reflected diagonal estimated by absolute values;
5. an omitted transition or cutoff surface;
6. failure of the first-cell Mertens mutation;
7. different packing and covering packet maps whose errors cannot be paired.

Conversely, a complete `K=6`, `K=8`, and symbolic-`K` face dictionary proving
(L-23806.10) establishes the closing recurrence.

## 9. Proof boundary

Exact/imported:

- carry/Legendre algebra and finite LPs;
- Möbius-curvature transform;
- finite double resolvent;
- reflected Selberg coefficient identity;
- high-order free-variable Euler theorem;
- scale-contraction deduction.

New RH-bearing hinge:

- exact packet-to-two-sided-obstacle identification;
- uniform two-contact terminal-face theorem.

No accepted proof of RH is claimed before independent verification of this
symbolic dictionary.
