# L-102901 — Primewise complementary temperatures form an infinite-dimensional flat gauge

Claim ID: `L-102901`  
Status: **PROVED EXACT FINITE-HORIZON SOURCE IDENTITY**  
Created: 2026-08-25  
Depends on: `L-102898`; labelled duplicate-67 convention  
RH status: **not assumed**

Work in the finite commutative labelled Euler algebra on one physical horizon.
The two labels whose physical prime is `67` remain distinct. For each active
label `ell` put

\[
x_\ell=p_\ell^{-1/2}U_\ell,
\]

and choose an arbitrary real or complex temperature vector

\[
\mathbf t=(t_\ell)_\ell.
\]

Define

\[
\boxed{
\sigma_{\mathbf t}
=\prod_\ell(1-x_\ell)(1+x_\ell)^{t_\ell}.
}
\tag{L-102901.1}
\]

Every generalized binomial series is coefficientwise finite on the declared
horizon.

## 1. Exact detector invariance

Let `1-t` denote the coordinatewise complement. At every labelled prime,

\[
(1-x)^2(1+x)^t(1+x)^{1-t}
=(1-x)^2(1+x)
=(1-x)(1-x^2).
\]

Consequently

\[
\boxed{
\sigma_{\mathbf t}*\sigma_{\mathbf1-\mathbf t}
=\Gamma_{1/2}
=\eta*\eta
=\beta*\beta^\square
}
\tag{L-102901.2}
\]

for every primewise temperature vector. Thus changing one temperature, a
finite subset of temperatures, or all of them does not change the arithmetic
source, the fixed outer detector, or any hypothetical reciprocal-zeta pole.

## 2. Coordinatewise flat connection

For one coordinate `j`, put

\[
\Lambda_j=\log(1+x_j).
\]

Then

\[
\partial_{t_j}\sigma_{\mathbf t}
=\sigma_{\mathbf t}*\Lambda_j.
\tag{L-102901.3}
\]

Differentiating (L-102901.2) in the `j`-th complementary direction gives

\[
\boxed{
(\partial_{t_j}\sigma_{\mathbf t})*
 \sigma_{\mathbf1-\mathbf t}
=
\sigma_{\mathbf t}*
(\partial_{s_j}\sigma_{\mathbf s})|_{\mathbf s=\mathbf1-\mathbf t}.
}
\tag{L-102901.4}
\]

All coordinate generators commute. Hence

\[
[\partial_{t_i}-\Lambda_i,\partial_{t_j}-\Lambda_j]=0
\]

and every mixed curvature vanishes. The scalar flat connection of `L-102898`
is the diagonal restriction `t_ell=t`.

## 3. Exact regional use

Let `P_R` be any source-owned projection or partition applied to the complete
product source after labels and provenance have been fixed. Since the product
in (L-102901.2) is independent of `t`,

\[
P_R(\sigma_{\mathbf t}*\sigma_{\mathbf1-\mathbf t})
=P_R\Gamma_{1/2}.
\]

Thus different disjoint source regions may use different primewise gauges,
provided every region is assigned once and the complementary factors are
recombined before a negative part or physical norm is taken.

Every fixed Mellin filter, common-mother factorization, owner projection,
additive phase, dyadic block, and physical observation used on PR #719 acts
after this identity and preserves it.

## Scope

The theorem removes the need to choose one global completion temperature for
all primes. It does not orient the fixed product observation: the product is
unchanged, and `R-102872` remains binding.
