# L-15620 — Berezin clipping, strict reverse capacity, and the correct positive-slack gate

Claim ID: `L-15620`  
Title: The convex symbol bound is valid, but exact zero-slack symbol saturation is impossible  
Status: `PARTIAL — CORE BEREZIN THEOREM PROVED; FORMER ZERO-SLACK COROLLARY REFUTED BY R-15603`  
Authoring agent: `gpt56-pro-09-f`  
Created: 2026-07-31  
Corrected: 2026-07-31  
Dependencies: `L-15618`; `R-15603`; Plancherel; scalar Jensen inequality  
Scope: symbol interfaces for Issue #156  
Related counterexample candidates: none

## 0. Correction

The convex trace theorem and the operator-clipping inequality in this file are
correct. The former proposed production condition

\[
 { |I|\over2\pi}\int(\Gamma-s)_+
 \le d(\Gamma-\alpha)
 \tag{L-15620.0}
\]

is not merely unproved: `R-15603` shows that it has the strict reverse direction
whenever the same lower symbol and a nonzero finite low packet are used.

The error was to treat an upper bound for a spectrally clipped localization
operator as though it could itself saturate. Spectral clipping does not commute
with time-frequency compression.

## 1. Localization operator

Let `I` be a bounded interval of positive length. Extend vectors in `L2(I)` by
zero and use

\[
 \|f\|_2^2={1\over2\pi}\int_{\mathbb R}|\widehat f(\xi)|^2d\xi.
 \tag{L-15620.1}
\]

For a measurable nonnegative integrable symbol `w`, define

\[
 D_w=P_I\mathcal F^{-1}M_w\mathcal FP_I.
 \tag{L-15620.2}
\]

Then `D_w` is positive trace class and

\[
 \operatorname{Tr}D_w
 ={ |I|\over2\pi}\int_{\mathbb R}w(\xi)d\xi.
 \tag{L-15620.3}
\]

## 2. Valid convex trace inequality

Let `Phi:[0,infinity)->[0,infinity)` be convex with `Phi(0)=0`. Then

\[
 \boxed{
 \operatorname{Tr}\Phi(D_w)
 \le { |I|\over2\pi}
 \int_{\mathbb R}\Phi(w(\xi))d\xi.}
 \tag{L-15620.4}
\]

### Proof

Let `lambda_n` be the positive eigenvalues of `D_w`, with orthonormal
eigenfunctions `u_n`. Plancherel gives

\[
 \lambda_n={1\over2\pi}
 \int w(\xi)|\widehat u_n(\xi)|^2d\xi,
 \qquad
 {1\over2\pi}\int|\widehat u_n|^2=1.
\]

Scalar Jensen gives

\[
 \Phi(\lambda_n)
 \le {1\over2\pi}
 \int\Phi(w(\xi))|\widehat u_n(\xi)|^2d\xi.
\]

Summing and using completeness of an orthonormal basis of `L2(I)` gives

\[
 \sum_n|\widehat u_n(\xi)|^2=|I|.
\]

Tonelli proves (L-15620.4). QED.

## 3. Valid operator-clipping bound

For `theta>=0`, take

\[
 \Phi_\theta(x)=(x-\theta)_+.
\]

Then

\[
 \boxed{
 \operatorname{Tr}(D_w-\theta I)_+
 \le { |I|\over2\pi}
 \int_{\mathbb R}(w(\xi)-\theta)_+d\xi.}
 \tag{L-15620.5}
\]

Let a real lower symbol `s` and an auxiliary level `G` define

\[
 w_G=(G-s)_+,
 \qquad
 D_G=D_{w_G}.
\]

For `Gamma<=G`, set `theta=G-Gamma`. The scalar identity

\[
 \bigl((G-s)_+-(G-\Gamma)\bigr)_+
 =(\Gamma-s)_+
 \tag{L-15620.6}
\]

gives

\[
 \boxed{
 \operatorname{Tr}
 \bigl(D_G-(G-\Gamma)I\bigr)_+
 \le { |I|\over2\pi}
 \int(\Gamma-s)_+.}
 \tag{L-15620.7}
\]

Equation (L-15620.7) is useful as an upper estimate. It cannot be promoted to
an exact zero-slack saturation condition.

## 4. Why the old scalar gate is impossible

Assume the same localized operator satisfies

\[
 A\succeq GI-D_G,
 \qquad
 G\ge\Gamma.
 \tag{L-15620.8}
\]

Pointwise,

\[
 \min(G,s)\ge\min(\Gamma,s)
 =\Gamma-(\Gamma-s)_+.
\]

Hence, with

\[
 D_\Gamma
 =P_I\mathcal F^{-1}(\Gamma-s)_+\mathcal FP_I,
\]

we have

\[
 \boxed{A\succeq\Gamma I-D_\Gamma.}
 \tag{L-15620.9}
\]

Let `L` be a nonzero `d`-dimensional packet satisfying

\[
 A|_L\preceq\alpha I_L,
 \qquad
 \alpha<\Gamma.
 \tag{L-15620.10}
\]

`R-15603` proves

\[
 \boxed{
 { |I|\over2\pi}\int(\Gamma-s)_+
 =\operatorname{Tr}D_\Gamma
 >d(\Gamma-\alpha).}
 \tag{L-15620.11}
\]

The strictness comes from Paley–Wiener uniqueness: every nonzero positive
symbol localization is strictly positive on every nonzero time-limited vector,
so it has positive trace outside every finite packet.

On the scaled Suzuki interval `I=[-1,1]`, the exact statement is

\[
 \boxed{
 {1\over\pi}\int(\Gamma-s_a)_+
 >d_a(\Gamma-\alpha_a).}
 \tag{L-15620.12}
\]

Thus the inequality requested with `<=` is impossible at every nontrivial
finite level.

## 5. Correct nonvacuous scalar quantities

### 5.1 Spectrally clipped operator trace

The sharp condition from `L-15618` remains

\[
 \boxed{
 \operatorname{Tr}
 \bigl(D_G-(G-\Gamma)I\bigr)_+
 \le d(\Gamma-\alpha).}
 \tag{L-15620.13}
\]

Unlike `D_Gamma`, the spectrally clipped operator in (L-15620.13) may have
finite rank. This is the closest scalar threshold condition.

### 5.2 Exact leverage tail

Let `P` project onto the packet and `Q=I-P`. Then

\[
 \boxed{
 \operatorname{Tr}(QD_\Gamma Q)
 ={1\over2\pi}\int
 (\Gamma-s(\xi))_+\|Qe_\xi\|_2^2d\xi.}
 \tag{L-15620.14}
\]

This is the packet-leverage deficit of `L-15607/L-15608`. It removes the part
of the symbol deficit already captured by the finite packet.

### 5.3 Unweighted excess with positive slack

Define

\[
 \Delta
 ={ |I|\over2\pi}\int(\Gamma-s)_+
  -d(\Gamma-\alpha).
 \tag{L-15620.15}
\]

Equation (L-15620.11) says `Delta>0`. Compression of (L-15620.9) to the packet
gives

\[
 PD_\Gamma P\succeq(\Gamma-\alpha)P.
\]

Therefore

\[
 \operatorname{Tr}(QD_\Gamma Q)\le\Delta.
 \tag{L-15620.16}
\]

Since a positive operator norm is at most its trace,

\[
 \boxed{
 A|_{L^\perp}\succeq(\Gamma-\Delta)I.}
 \tag{L-15620.17}
\]

Thus the correct unweighted symbol target is not `Delta<=0`, but

\[
 \boxed{0<\Delta_j\longrightarrow0.}
 \tag{L-15620.18}
\]

A threshold schedule with

\[
 t_j<\Gamma_j-\Delta_j
\]

then supplies the complement moat needed by the inverse-Ritz layer.

## 6. Layer-cake form

The total symbol trace still has the exact layer-cake formula

\[
 \int(\Gamma-s)_+
 =\int_{-\infty}^{\Gamma}
 |\{\xi:s(\xi)<u\}|du.
 \tag{L-15620.19}
\]

It may be used to estimate the positive excess `Delta`, but it can never make
that excess nonpositive at a finite nontrivial level.

## 7. Correct production interfaces

A proof-producing continuation should certify one of:

1. the operator-clipped trace (L-15620.13);
2. the exact leverage trace tail (L-15620.14);
3. a positive excess `Delta_j` satisfying (L-15620.18);
4. the finite visible Schur margin of `L-15604/L-15307`.

A cellwise enclosure of the unweighted integral with a claimed nonpositive
excess must be rejected, because it contradicts (L-15620.11).

## 8. Proof boundary

- The convex Berezin trace inequality remains exact.
- The old zero-slack symbol-capacity corollary is vacuous and has been retired.
- No current artifact proves the operator-clipped, leverage-tail, or
  vanishing-positive-slack condition cofinally for the complete Suzuki symbol.
- This correction neither proves nor disproves RH.
