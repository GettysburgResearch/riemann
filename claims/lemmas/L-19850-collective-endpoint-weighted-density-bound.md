# L-19850 — Collective endpoint weighted-density bound

Claim ID: `L-19850`  
Status: **PROPOSED ENDPOINT OPERATOR LEMMA**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Scope: supplies the endpoint weighted-density and variation inputs of `L-19843`

## 1. Endpoint model

After exact endpoint-jet extraction, the leading normalized endpoint channel of
one packet vector has the form

\[
 \mathcal H_0(v)
 =C_R(v)
 \sum_{k\ge1}\frac{e^{ik\vartheta_R(v)}}k,
 \tag{L-19850.1}
\]

where `C_R(v)` is an operator-valued coefficient with

\[
 \|C_R\|+\|\partial_vC_R\|+
 R\|\partial_RC_R\|
 \le(\log R)^C.
 \tag{L-19850.2}
\]

All higher jets have coefficients `1/k^(a+1)`, `a>=1`, and are absolutely
summable. The phase is piecewise monotone with finitely many nondegenerate
pieces; constant pieces are combined algebraically before taking a norm.

## 2. Exact collective sum

For `theta notin 2pi Z`,

\[
 \sum_{k\ge1}\frac{e^{ik\theta}}k
 =-\log(1-e^{i\theta}).
 \tag{L-19850.3}
\]

The logarithmic singularity is square integrable:

\[
 \int_0^{2\pi}
 |\log(1-e^{i\theta})|^2d\theta
 =2\pi\sum_{k\ge1}\frac1{k^2}<\infty.
 \tag{L-19850.4}
\]

More generally, insertion of one logarithmic density weight gives

\[
 \int_0^{2\pi}
 \left|
 \sum_{k\ge2}\frac{\log k}{k}e^{ik\theta}
 \right|^2d\theta
 =2\pi\sum_{k\ge2}\frac{(\log k)^2}{k^2}<\infty.
 \tag{L-19850.5}
\]

Thus endpoint density weights do not create a new divergence.

## 3. Pullback to the radial variable

On every monotone phase piece, change variables from `v` to
`theta=vartheta_R(v)`. The exact radial action gives upper and lower Jacobian
bounds away from the already isolated Airy fold. The fold interval has length
`O(R^(-2/3)polylog(R))` and is bounded directly.

Equations (L-19850.2)--(L-19850.5) yield

\[
 \int
 \|\mathcal H_0(v)\|^2dv
 \le(\log R)^C,
 \tag{L-19850.6}
\]

and, with the local zero-density correction `log v+c_0`,

\[
 \int
 (1+|\log v|)
 \|\mathcal H_0(v)\|^2dv
 \le(\log R)^C.
 \tag{L-19850.7}
\]

In first-alias-normalized coordinates the coefficient bound is uniform, and the
complete endpoint self-energy is part of `D_R`. Consequently the weighted
endpoint density form `C_R^(end)` obeys the relative estimate

\[
 \boxed{
 \|D_R^{-1/2}C_R^{\rm end}D_R^{-1/2}\|
 \le C.}
 \tag{L-19850.8}
\]

A weaker `O(log log R)` bound also suffices, but no logarithmic loss is forced by
the `1/k` channel itself.

## 4. One support derivative

Differentiate the aggregate, not the individual series:

\[
 R\partial_R\log(1-e^{i\vartheta_R})
 =-
 \frac{iR\vartheta_R'e^{i\vartheta_R}}
      {1-e^{i\vartheta_R}}.
 \tag{L-19850.9}
\]

On the endpoint-good set of `L-19845`,

\[
 |1-e^{i\vartheta_R}|\gg(\log R)^{-A},
 \tag{L-19850.10}
\]

so the derivative aggregate is polynomial in `log R`. Its square is integrable
on each good phase piece, and the excluded support set has relative measure
`o(1)`. Hence

\[
 \int
 \left(
 \|\mathcal H_0(v)\|^2+
 \|R\partial_R\mathcal H_0(v)\|^2
 \right)dv
 \le(\log R)^C.
 \tag{L-19850.11}
\]

## 5. Higher jets and remainder

For `a>=1`,

\[
 \sum_{k\ge1}k^{-a-1}<\infty.
 \tag{L-19850.12}
\]

The post-jet remainder has an additional `k^{-p-1}` factor for fixed `p>=3`.
Therefore all higher endpoint channels, their density-weighted forms, and one
scaled support derivative are absolutely summable with a polylogarithmic
operator bound.

## 6. Consequence for local Weyl

The endpoint contribution to

\[
 A_R-(\log R)D_R
 \tag{L-19850.13}
\]

has:

1. bounded relative smooth-density correction by (L-19850.8);
2. polylogarithmic amplitude and scaled support derivative by
   (L-19850.11);
3. an oscillatory first/rest cross controlled by the support large sieve;
4. positive self-energy retained inside `D_R`.

This supplies the endpoint inputs (L-19843.9) and (L-19843.11).

## 7. Proof boundary

The Fourier-series identities and weighted `l2` sums are exact. The only
profile-specific input is the finite piecewise-monotone phase/Jacobian ledger,
which is part of the corrected mode-dependent endpoint theorem `L-19844`.
No absolute sum of the leading `1/k` norms is used.
