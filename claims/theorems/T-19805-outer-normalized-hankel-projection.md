# T-19805 — Outer-normalized Hankel projection criterion

Claim ID: `T-19805`  
Title: After removing the unconditional minimum-phase factor, every zero to the right of a vertical line contributes an exact projection-valued Hardy defect  
Status: `PROPOSED — COMPLETE HARDY-FACTORIZATION PROOF; COFINAL PRIME-SIDE BOUND OPEN`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Dependencies: canonical factorization in `H^2(C_+)`; Toeplitz–Hankel algebra; `L-19809`  
Scope: strip-sensitive self-adjoint/contour replacement for the beta-cell sign blocker

## 1. A zero-preserving Hardy transfer

Fix

\[
0<\omega<\frac12,
\qquad
\sigma_\omega=\frac12+\omega,
\qquad
s_\omega(z)=\sigma_\omega-iz.
\tag{T-19805.1}
\]

Remove the zeta pole, but no zero, by setting

\[
\boxed{
F_\omega(z)=\bigl(s_\omega(z)-1\bigr)\zeta(s_\omega(z)).}
\tag{T-19805.2}
\]

The function is entire in `z`. Its zeros in the upper half-plane are exactly

\[
\boxed{
p_\rho=-\Im\rho+i(\Re\rho-\sigma_\omega),
\qquad
\zeta(\rho)=0,\quad \Re\rho>\sigma_\omega,}
\tag{T-19805.3}
\]

with multiplicity. Trivial zeros never occur in this half-plane.

Standard polynomial bounds for zeta on `Re s>=sigma_omega` imply that, for a
sufficiently large integer `M`,

\[
G_{\omega,M}(z)=(z+i)^{-M}F_\omega(z)
\tag{T-19805.4}
\]

belongs to `H^2(C_+)`. The damping factor is zero-free and outer, so it changes
neither the zero set nor the inner factor.

## 2. Canonical factorization has only one possible defect

Factor

\[
\boxed{G_{\omega,M}=B_\omega O_{\omega,M}.}
\tag{T-19805.5}
\]

Here `B_omega` is the Blaschke product of the points (T-19805.3), and
`O_(omega,M)` is outer. There is no singular inner factor because
`G_(omega,M)` extends meromorphically—and in fact holomorphically after the
explicit lower-half-plane damping pole—through every real point. There is no
exponential inner factor because its upper-half-plane mean type is zero.

Changing `M` multiplies `O_(omega,M)` by another zero-free outer factor and
leaves `B_omega` unchanged.

## 3. Outer-normalized all-pass symbol

For real `t`, use the boundary reflection notation

\[
G^\#(t)=\overline{G(t)},
\qquad
O^\#(t)=\overline{O(t)}.
\]

Define the unimodular boundary symbol

\[
\boxed{
\mathfrak a_\omega(t)
=
{G_{\omega,M}^\#(t)\over G_{\omega,M}(t)}
{O_{\omega,M}(t)\over O_{\omega,M}^\#(t)}.}
\tag{T-19805.6}
\]

The damping and every outer amplitude cancel. Equation (T-19805.5) gives

\[
\boxed{
\mathfrak a_\omega(t)
={\overline{B_\omega(t)}\over B_\omega(t)}
=\overline{B_\omega(t)}^{\,2}}
\quad\text{a.e.}
\tag{T-19805.7}
\]

Thus `mathfrak a_omega` is the exact non-minimum-phase component of the zeta
transfer. It is independent of the auxiliary damping exponent.

The reversible operator of `L-19809` determines the boundary amplitude. The
outer factor is the unique minimum-phase reconstruction of that amplitude. The
symbol (T-19805.6) is precisely what amplitude/self-adjointness cannot see.

## 4. Projection-valued Hankel defect

Let

\[
\mathsf H_\omega
=P_-M_{\mathfrak a_\omega}|_{H^2(\mathbb C_+)},
\qquad
T_\omega
=P_+M_{\mathfrak a_\omega}|_{H^2(\mathbb C_+)}.
\tag{T-19805.8}
\]

Put

\[
I_\omega=B_\omega^2.
\tag{T-19805.9}
\]

Since `I_omega` is inner and `mathfrak a_omega=overline(I_omega)`, the standard
model-space identity gives

\[
\boxed{
\mathsf H_\omega^*\mathsf H_\omega
=P_{K_{I_\omega}},
\qquad
K_{I_\omega}=H^2\ominus I_\omega H^2.}
\tag{T-19805.10}
\]

Consequently

\[
\boxed{
I-T_\omega^*T_\omega
=P_{K_{I_\omega}}.}
\tag{T-19805.11}
\]

This is stronger than an ordinary positive defect: it is an orthogonal
projection. Therefore

\[
\boxed{
\|\mathsf H_\omega\|
\in\{0,1\}.}
\tag{T-19805.12}
\]

More explicitly,

\[
\boxed{
\begin{aligned}
\|\mathsf H_\omega\|=0
&\iff B_\omega\equiv1\\
&\iff \zeta(s)\ne0\quad(\Re s>\tfrac12+\omega),
\end{aligned}}
\tag{T-19805.13}
\]

whereas the existence of even one zero to the right gives

\[
\boxed{
\|\mathsf H_\omega\|=1,
\qquad
\inf_{\|f\|=1}\|T_\omega f\|=0.}
\tag{T-19805.14}
\]

The off-line defect cannot be small after outer normalization.

## 5. Quantized strict-moat theorem

Any one of the following unconditional inequalities at one offset proves the
corresponding zero-free half-plane:

\[
\boxed{
\|\mathsf H_\omega\|<1,}
\tag{T-19805.15}
\]

\[
\boxed{
\mathsf H_\omega^*\mathsf H_\omega\preceq\kappa I
\quad\text{for some }\kappa<1,}
\tag{T-19805.16}
\]

or

\[
\boxed{
T_\omega^*T_\omega\succeq cI
\quad\text{for some }c>0.}
\tag{T-19805.17}
\]

Unlike the raw Suzuki scattering symbol, no uniform moat over an unknown pole
crossing is needed: the outer-normalized defect is already quantized at every
fixed offset.

If (T-19805.15), (T-19805.16), or (T-19805.17) is proved for a sequence
`omega_j downarrow 0`, then RH follows.

## 6. Finite-zero specialization

If only finitely many zeros lie to the right of the line, with total
multiplicity `N_omega`, then

\[
\boxed{
\operatorname{rank}
(\mathsf H_\omega^*\mathsf H_\omega)
=2N_\omega.}
\tag{T-19805.18}
\]

The factor two comes from the square `I_omega=B_omega^2`. Thus the projection
rank is an exact right-of-line zero count. For infinitely many zeros, the model
space is infinite-dimensional and the norm conclusion remains unchanged.

## 7. Proof-producing contour interface

The outer factor is determined by the boundary modulus through the Poisson
integral of `log|G_(omega,M)|`. Hence a directed certificate does not need zero
ordinates. It may consist of:

1. a directed boundary producer for `F_omega`;
2. a directed Poisson/Hilbert reconstruction of its outer factor;
3. a causal/anti-causal decomposition of `mathfrak a_omega`;
4. one strict Hankel norm upper bound below one, or one positive Toeplitz floor.

A finite coefficient truncation requires a complete anti-causal tail radius.
Because the true defect is a projection, any strict completed bound is decisive.

## 8. Exact remaining obstruction

The theorem constructs a genuinely strip-sensitive, positivity-preserving
operator that excludes every fixed off-line mode. It does not yet prove the
strict bound (T-19805.15).

The smallest remaining statement is now:

\[
\boxed{
\text{for a cofinal sequence }\omega_j\downarrow0,
\quad
\|P_-M_{\mathfrak a_{\omega_j}}P_+\|<1.}
\tag{T-19805.19}
\]

Because of projection quantization, this is exactly a minimum-phase theorem for
one explicitly outer-normalized zeta transfer; it is no longer a small-tail,
packet-capture, or moving-frequency estimate.

## 9. Proof boundary

- Canonical factorization and the projection identity are exact.
- Polynomial growth and the harmless outer damping must be bound in a production
  normalization, but they carry no zero information.
- Boundary zeros may be treated by a limiting line displacement; any positive
  Toeplitz floor automatically excludes them as well.
- No strict prime-side Hankel bound has yet been proved, so RH is not claimed.