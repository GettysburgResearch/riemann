# L-100131 — The minimal-wavelet energy abscissa is the rightmost-zero abscissa

Claim ID: `L-100131`  
Status: **PROVED ANALYTIC THEOREM**  
Created: 2026-08-20  
Depends on: `L-100130`; standard Mellin-Hardy theory for finite-order Dirichlet series  
RH status: **not assumed**

Let

\[
\Theta=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}
\]

and define the weighted energy abscissa

\[
\sigma_2
=\inf\left\{\sigma:
\int_1^\infty Q_X X^{-2\sigma}{dX\over X}<\infty
\right\}.
\tag{L-100131.1}
\]

Then

\[
\boxed{\sigma_2=\Theta+\frac12.}
\tag{L-100131.2}
\]

## Lower bound

Suppose the weighted energy is finite at `sigma`. By Tonelli, for almost every
real `gamma`,

\[
X^{-\sigma}F_\gamma(X)\in L^2(dX/X).
\]

Its Mellin transform is therefore a Hardy-space function holomorphic in
`Re s>sigma`. On the initial safe half-plane it equals

\[
{\widehat K_0(s)\over\zeta(s-\frac12+i\gamma)},
\]

so uniqueness of analytic continuation gives the same meromorphic function
throughout the Hardy half-plane.

If `rho` is a zeta zero with `Re rho=beta` and `beta+1/2>sigma`, then for every
real `gamma` this quotient has a pole at

\[
s=\rho+\frac12-i\gamma.
\]

`L-100130` proves that the compact multiplier is nonzero there. This
contradicts Hardy holomorphy for a positive-measure set of `gamma`. Hence

\[
\sigma\ge\Theta+\frac12.
\tag{L-100131.3}
\]

## Upper bound

Fix `sigma>Theta+1/2`. Choose `eta>0` such that

\[
\sigma-\frac12\ge\Theta+2\eta.
\]

The standard reciprocal-zeta bound in the closed zero-free half-plane
`Re z>=Theta+eta` is subpolynomial on vertical lines. The compact wavelet
transform satisfies

\[
\widehat K_0(\sigma+it)=O_\sigma((1+|t|)^{-2}),
\]

and the Cauchy density contributes `(1+gamma^2)^(-1)`. Consequently the double
integral in `L-100130.5` converges. Thus

\[
\sigma_2\le\Theta+\frac12.
\tag{L-100131.4}
\]

Combining (L-100131.3)--(L-100131.4) proves the theorem.

## Critical cumulative energy

Put

\[
\mathscr E(Y)=\int_1^Y Q_X{dX\over X^3}.
\tag{L-100131.5}
\]

Because `Q_X>=0`, dyadic summation gives the exact abscissa equivalence

\[
\boxed{
\mathscr E(Y)=Y^{o(1)}
\iff \sigma_2\le1.
}
\tag{L-100131.6}
\]

Indeed, the forward implication makes
`int Q_X X^(-3-2epsilon)dX` finite for every `epsilon>0`; conversely, finiteness
at every `1+epsilon` gives

\[
\mathscr E(Y)\le
Y^{2\epsilon}\mathcal E(1+\epsilon).
\]

Therefore

\[
\boxed{
\mathscr E(Y)=Y^{o(1)}
\iff \Theta\le\frac12
\iff RH.
}
\tag{L-100131.7}
\]

More quantitatively, if for some `theta>=0`

\[
\mathscr E(Y)=O_\epsilon(Y^{2\theta+\epsilon})
\quad(\epsilon>0),
\]

then every nontrivial zeta zero satisfies

\[
\Re\rho\le\frac12+\theta.
\tag{L-100131.8}
\]

## Relation to MWOC99910

Let

\[
\mathscr M(Y)=
\int_2^Y{\sqrt{Q_X}\over X/8}{dX\over X}.
\]

Cauchy--Schwarz gives

\[
\boxed{
\mathscr M(Y)^2
\le64\log Y\,\mathscr E(Y).
}
\tag{L-100131.9}
\]

Hence RH implies `MWOC99910`. The converse is the one-sided wavelet/Landau
implication already proved in PR #674. Thus `MWOC99910` is exactly
RH-equivalent, not a weaker source-blind harmonic-analysis estimate.