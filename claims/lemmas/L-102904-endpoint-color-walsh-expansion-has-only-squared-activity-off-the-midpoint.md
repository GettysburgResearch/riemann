# L-102904 — Endpoint-color Walsh expansion has only squared activity off the arithmetic midpoint

Claim ID: `L-102904`  
Status: **PROVED EXACT WALSH/SUBCRITICAL-GAUGE IDENTITY**  
Created: 2026-08-25  
Depends on: `L-102901--L-102903`; `L-102892`  
RH status: **not assumed**

At one labelled prime retain

\[
E=1-x,
\qquad C=1-x^2.
\]

Define the arithmetic midpoint and endpoint fluctuation

\[
\boxed{
M=\frac{E+C}{2}=1-\frac x2-\frac{x^2}{2},
\qquad
D=\frac{E-C}{2}=\frac{-x+x^2}{2}.
}
\tag{L-102904.1}

Then

\[
E=M+D,
\qquad C=M-D,
\]

and therefore

\[
\boxed{
EC=M^2-D^2.
}
\tag{L-102904.2}

The arithmetic midpoint `M` is exactly the local factor

\[
(1-x)(1+x/2)
\]

of the strict partial-completion source at parameter `c=1/2`.

## 1. Independent endpoint colors

Let `epsilon_p` be independent signs in `{+1,-1}`. Put

\[
L_\epsilon=\bigotimes_p(M_p+\epsilon_pD_p),
\qquad
R_\epsilon=\bigotimes_p(M_p-\epsilon_pD_p).
\]

For every color realization, arithmetic convolution gives the same fixed
product source:

\[
\operatorname{conv}(L_\epsilon\otimes R_\epsilon)
=\prod_p(M_p^2-D_p^2)
=\Gamma_{1/2}.
\]

Averaging in the free labelled tensor algebra removes every mixed midpoint /
fluctuation term:

\[
\boxed{
\mathbb E_\epsilon
[L_\epsilon\otimes R_\epsilon]
=
\bigotimes_p
(M_p\otimes M_p-D_p\otimes D_p).
}
\tag{L-102904.3}

## 2. Every variance coordinate is subcritical

The fluctuation square is

\[
\boxed{
D_p^2
=\frac14x_p^2(1-x_p)^2.
}
\tag{L-102904.4}

It has no root or first-chaos term and begins at activity

\[
x_p^2=p^{-1}U_{p^2}.
\]

Equivalently,

\[
\boxed{
\frac{E_pC_p}{M_p^2}
=1-\frac14x_p^2+rac14x_p^3-rac3{16}x_p^4+\cdots,
}
\tag{L-102904.5}

with zero linear coefficient. Therefore the two-sided transfer between the
arithmetic midpoint square and the geometric/native midpoint product begins
at squared activity and has finite-horizon source norm bounded by a power of
`log Y`.

This recovers, in endpoint-color coordinates, the subcritical arithmetic /
geometric midpoint gauge of `L-102892`.

## 3. Exact remaining mean coordinate

All nonempty Walsh fluctuations are contained in the squared and
higher-prime-power ledger. The only critical tensor coordinate is the mean
term

\[
\bigotimes_p M_p\otimes M_p.
\]

Thus endpoint randomization does not create a new critical source. It moves all
color variance into subcritical square activity and leaves one arithmetic
midpoint-square orientation problem.

## Scope

The fixed physical observation is signed. Neither (L-102904.3) nor the
subcritical variance bound makes the mean arithmetic square pointwise
nonnegative. The surviving mean coordinate is gauge-equivalent to
`GMBC102893` and remains RH-bearing.
