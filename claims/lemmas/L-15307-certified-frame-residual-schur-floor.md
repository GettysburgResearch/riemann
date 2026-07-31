# L-15307 — Certified-frame residual Schur floor

Claim ID: `L-15307`  
Title: One positive zero frame and one residual operator envelope certify the visible Schur block  
Status: `PROPOSED`  
Authoring agent: `gpt56-03-k`  
Created: 2026-07-31  
Dependencies: positive-metric Schur complements; `L-15305`; `L-15306`; the certified-zero frame construction of `L-14319`  
Scope: the visible/ambient gate in the three-block positive route

## 1. Setup

Let `V` and `E` be finite-dimensional real or complex Hilbert spaces with
declared positive metrics

\[
G_V\succ0,\qquad M\succ0.
\]

Write one Hermitian block as

\[
\mathcal A=
\begin{pmatrix}
B_V&Z^*\\
Z&C
\end{pmatrix}.
\tag{L-15307.1}
\]

Suppose a proof-grade positive form `J` has been separated from the exact
operator and is supported on `V`:

\[
\mathcal A=
\begin{pmatrix}J&0\\0&0\end{pmatrix}
+
\begin{pmatrix}R_V&Z^*\\Z&C\end{pmatrix}.
\tag{L-15307.2}
\]

For the zeta application, `J` may be the contribution of finitely many
independently certified critical-line zeros after whitening their restricted
exponential Gram. Choosing `E` inside the kernel of those selected evaluations
makes the zero-frame block diagonal exactly; no interval estimate is used for
that zero cross.

Assume

\[
\boxed{J\succeq\sigma^2G_V,}
\tag{L-15307.3}
\]

\[
\boxed{R_V\succeq-\rho G_V,}
\tag{L-15307.4}
\]

\[
\boxed{C\succeq hM,\qquad h>0,}
\tag{L-15307.5}
\]

and

\[
\boxed{Z^*M^{-1}Z\preceq\zeta^2G_V.}
\tag{L-15307.6}
\]

Here `rho,zeta>=0`. Every quantity is relative to one declared metric.

## 2. Main theorem

The Schur-corrected visible block satisfies

\[
\boxed{
B_V-h^{-1}Z^*M^{-1}Z
\succeq
\left(\sigma^2-\rho-\frac{\zeta^2}{h}\right)G_V.}
\tag{L-15307.7}
\]

Consequently, if

\[
\boxed{
\beta:=
\sigma^2-\rho-\frac{\zeta^2}{h}>0,}
\tag{L-15307.8}
\]

then the exact visible gate required by `L-15306` holds:

\[
\boxed{
B_V-h^{-1}Z^*M^{-1}Z\succeq\beta G_V\succ0.}
\tag{L-15307.9}
\]

### Proof

Equations (L-15307.2)--(L-15307.4) give

\[
B_V=J+R_V\succeq(\sigma^2-\rho)G_V.
\]

Equation (L-15307.6) gives

\[
h^{-1}Z^*M^{-1}Z\preceq(\zeta^2/h)G_V.
\]

Subtracting proves (L-15307.7), and strict positivity of the scalar in
(L-15307.8) proves (L-15307.9). QED.

## 3. One residual-envelope corollary

Let

\[
\mathcal G_{VE}=\operatorname{diag}(G_V,M)
\]

and suppose the residual block

\[
\mathcal R=
\begin{pmatrix}R_V&Z^*\\Z&R_E\end{pmatrix}
\]

has the relative operator enclosure

\[
\boxed{
-\omega\mathcal G_{VE}
\preceq\mathcal R
\preceq\omega\mathcal G_{VE}.}
\tag{L-15307.10}
\]

Whitening by `mathcal G_(VE)` shows

\[
R_V\succeq-\omega G_V
\]

and

\[
\|M^{-1/2}ZG_V^{-1/2}\|\le\omega.
\]

Therefore (L-15307.7) gives the single-radius certificate

\[
\boxed{
B_V-h^{-1}Z^*M^{-1}Z
\succeq
\left(\sigma^2-\omega-\frac{\omega^2}{h}\right)G_V.}
\tag{L-15307.11}
\]

This is the cleanest proof-facing version when one analytic zero-tail or symbol
remainder theorem controls the complete residual block rather than separate
entries.

## 4. Relation to `L-15305`

`L-15305` proves, on a finite packet, a raw visible lower bound

\[
B_V\succeq(\sigma_T^2-B_T)G_V
\tag{L-15307.12}
\]

from a complete certified-zero Gram and an absolute omitted-zero budget. This
may be inserted into (L-15307.7) in either of two equivalent ways:

1. put `sigma^2=sigma_T^2`, `rho=B_T`, and certify the cross bound separately;
2. treat the entire omitted-zero/symbol remainder as the block `mathcal R` in
   (L-15307.10).

The second form is stronger because correlations between the visible diagonal
and the visible/ambient cross are retained until the final relative operator
bound.

The high-zero cutoff budget and any archimedean matrix cutoff are distinct.
They may enter `omega` only after their source conventions and Loewner
directions have been composed without double counting.

## 5. Canonical zero-frame decomposition

For certified centered ordinates `Z={gamma_1,...,gamma_m}`, let

\[
V_Zf=(\widehat f(\gamma_1),\ldots,\widehat f(\gamma_m))
\]

and

\[
P_Z=V_Z^*(V_ZV_Z^*)^{-1}V_Z.
\]

Then `P_Z` is the orthogonal projection onto the restricted zero-exponential
representer space. Taking

\[
V=\operatorname{Ran}P_Z,\qquad E=\ker P_Z
\]

makes every selected-zero rank-one form supported on `V`, so the zero-frame
cross in (L-15307.2) vanishes identically. This is the invariant form of the
visible split; an unwhitened evaluation SVD is not a substitute.

In a larger radical/visible/ambient decomposition, first remove the radical-like
near-kernel, then apply the same construction to its orthogonal complement.
Every direction not covered by the selected frame remains in the residual
operator and must be paid for in `rho,zeta`, or in the single radius `omega`.

## 6. Cofinal rate form

At support `lambda`, it is enough to exhibit source-bound quantities satisfying

\[
\liminf_{\lambda\to\infty}\sigma_\lambda^2>0,
\tag{L-15307.13}
\]

\[
\rho_\lambda\longrightarrow0,
\qquad
\frac{\zeta_\lambda^2}{h_\lambda}\longrightarrow0.
\tag{L-15307.14}
\]

More generally, no individual term must vanish: it is enough that

\[
\liminf_{\lambda\to\infty}
\left(
\sigma_\lambda^2-\rho_\lambda-\frac{\zeta_\lambda^2}{h_\lambda}
\right)>0.
\tag{L-15307.15}
\]

Under the one-radius adapter, the corresponding target is

\[
\liminf_{\lambda\to\infty}
\left(
\sigma_\lambda^2-\omega_\lambda-\frac{\omega_\lambda^2}{h_\lambda}
\right)>0.
\tag{L-15307.16}
\]

## 7. Exact trust boundary

A proof object must bind:

1. the support, packet bases, and metrics;
2. the certified critical-line ordinates and multiplicities;
3. the whitened positive-frame Gram `J`;
4. a lower Loewner enclosure for `J-sigma^2 G_V`;
5. either separate lower/cross residual bounds or one complete relative
   residual block radius;
6. the outer coercivity `C>=hM`;
7. every analytic and numerical assembly radius.

A positive raw visible matrix is insufficient if its cross map is not charged.

## 8. Proof boundary

- The theorem closes the finite visible Schur algebra exactly.
- It does not prove a zeta-specific cofinal residual radius.
- A finite set of line zeros alone does not control omitted off-line zeros;
  they must remain in the source-bound residual envelope.
- The theorem is compatible with the local-Weyl tail scalarization of
  `L-16209`, but that theorem still requires a production uniform boundary
  profile and a cross-to-complement estimate.
- No RH conclusion follows until the cofinal rates and the radical-row gate of
  `L-15306` are both supplied.
