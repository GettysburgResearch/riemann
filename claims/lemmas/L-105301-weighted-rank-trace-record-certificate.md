# L-105301 — Weighted Hermite rank–trace and record certificate

Claim ID: `L-105301`
Status: **PROVED EXACT AT FINITE-POLYNOMIAL SCOPE**
Created: 2026-08-23
Depends on: `L-105300`
RH status: not assumed

## 1. Source-faithful polynomial preconditioning

Retain the assumptions and notation of `L-105300`. Let

\[
w\in\mathbb R[x]
\]

be relatively prime to `p'`. Define

\[
\mathcal B_{p,w}(u,v)
=\operatorname{Tr}_{A_p/\mathbb R}
\bigl(q_p w^2uv\bigr).
\tag{L-105301.1}
\]

Multiplication by `w` is an invertible real-linear map on `A_p`, and

\[
\mathcal B_{p,w}(u,v)=\mathcal B_p(wu,wv).
\tag{L-105301.2}
\]

Therefore `B_(p,w)` is congruent to `B_p`; its inertia is independent of `w`.
The preconditioner is sign-blind: on a real critical point it multiplies
`-rho_c` by the positive number `w(c)^2`, and on a conjugate pair it acts by
an invertible real two-dimensional congruence.

In the monomial quotient basis put

\[
H_{p,w}=\langle1\rangle\oplus B_{p,w}.
\tag{L-105301.3}
\]

Then

\[
\operatorname{sig}(H_{p,w})=r(p),
\qquad
\nu_+(H_{p,w})=\frac{n+r(p)}2.
\tag{L-105301.4}
\]

## 2. Rank–trace lower bound

For every real symmetric matrix `H`, if `P=nu_+(H)`, then

\[
(\operatorname{tr}H)_+^2
\le P\,\operatorname{tr}(H^2).
\tag{L-105301.5}
\]

Indeed, the positive trace is at most the sum of the positive eigenvalues,
and Cauchy–Schwarz bounds that sum by the square root of `P` times their
square sum.

Apply this to `H_(p,w)`. Define

\[
\boxed{
\Theta(p,w)
=\frac{(\operatorname{tr}H_{p,w})_+^2}
{n\,\operatorname{tr}(H_{p,w}^2)}.
}
\tag{L-105301.6}
\]

Then

\[
\nu_+(H_{p,w})\ge n\Theta(p,w),
\]

and (L-105301.4) gives

\[
\boxed{
\frac{r(p)}n\ge 2\Theta(p,w)-1.
}
\tag{L-105301.7}
\]

The integer refinement is

\[
\boxed{
r(p)\ge 2\left\lceil
\frac{(\operatorname{tr}H_{p,w})_+^2}
{\operatorname{tr}(H_{p,w}^2)}
\right\rceil-n.
}
\tag{L-105301.8}
\]

## 3. Exact record threshold

The frozen public Anthropic/Alpöge–Furman proportion is `0.67250`. Since

\[
\frac{1+0.67250}{2}=0.83625,
\]

any asymptotic family of source-faithful Xi window matrices satisfying

\[
\boxed{
\liminf_{T\to\infty}\Theta_T>0.83625
}
\tag{L-105301.9}
\]

would imply a critical-line proportion strictly greater than `0.67250`.

This is not a rearrangement of the same two moments used in the two-thirds
paper. The matrix `H_(p,w)` is the antiderivative/critical-value Hermite trace
form; its entries depend on the derivative quotient `-p/p''` inside the
critical algebra. The weight `w` is a genuine source-side congruence degree of
freedom.

## 4. Higher spectral certificates

The first-two-moment certificate (L-105301.7) is only the first member of an
exact hierarchy. For nonsingular `H`,

\[
\operatorname{sig}(H)
=\operatorname{tr}(\operatorname{sgn}H),
\tag{L-105301.10}
\]

and

\[
\boxed{
\operatorname{sgn}H
=\frac2\pi\int_0^\infty
H(H^2+t^2I)^{-1}\,dt.
}
\tag{L-105301.11}
\]

Consequently the exact real-root count is

\[
\boxed{
r(p)=\frac2\pi\int_0^\infty
\operatorname{tr}\!\bigl(H_{p,w}(H_{p,w}^2+t^2I)^{-1}\bigr)\,dt.
}
\tag{L-105301.12}
\]

Finite rational lower approximants to the sign function give rigorous
multi-moment or resolvent certificates beyond the rank–trace ceiling. This is
the natural place to seek a record improvement if two moments remain sharp.

## 5. Scope

The inequality is exact but conditional on constructing and estimating the
correct Xi window matrix. No such asymptotic estimate is asserted here.
