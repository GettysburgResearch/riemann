# L-102706 — Euler completion and half-divisor homotopies are subcritically gauge-equivalent

Claim ID: `L-102706`  
Status: **PROVED EXACT WITH POLYLOGARITHMIC TRANSFER**  
Created: 2026-08-22  
Depends on: PR #718 `L-102600--L-102603`; PR #719 `L-102700`  
RH status: **not assumed**

Work on a finite labelled horizon, so every multiplicative shift is nilpotent.
For one labelled prime put

\[
x=p^{-1/2}e^{-i\vartheta}U_p.
\]

The two copies of `67` remain distinct labels.

## 1. Euler path

Orient the positive-completion path from the squared source to the native
source:

\[
\boxed{
 e_\tau(x)
 =(1-x)(1+(1-\tau)x)
 =1-\tau x-(1-\tau)x^2,
 \qquad 0\le\tau\le1.
}
\tag{L-102706.1}
\]

Thus

\[
e_0(x)=1-x^2,
\qquad
e_1(x)=1-x.
\]

Its first-order term is exactly the owner/transfer current of PR #718.

## 2. Half-divisor path

Put

\[
\ell_\tau(x)
 =\tau\sqrt{1-x}+(1-\tau)\sqrt{1-x^2}
\]

and

\[
\boxed{h_\tau(x)=\ell_\tau(x)^2.}
\tag{L-102706.2}
\]

Since

\[
\sqrt{1-x^2}=\sqrt{1-x}\sqrt{1+x},
\]

one has

\[
 h_\tau(x)
 =(1-x)[\tau+(1-\tau)\sqrt{1+x}]^2.
\tag{L-102706.3}
\]

Again

\[
h_0(x)=1-x^2,
\qquad
h_1(x)=1-x.
\]

The two paths therefore have identical endpoints.

## 3. Exact gauge ratio

Their local ratio is

\[
\boxed{
 g_\tau(x)
 =\frac{h_\tau(x)}{e_\tau(x)}
 =\frac{[\tau+(1-\tau)\sqrt{1+x}]^2}
 {1+(1-\tau)x}.
}
\tag{L-102706.4}
\]

The denominator is nonzero for `|x|<=2^(-1/2)`.  Direct expansion gives

\[
\boxed{g_\tau(x)=1+O(x^2),}
\qquad
\boxed{g_\tau(x)^{-1}=1+O(x^2),}
\tag{L-102706.5}
\]

uniformly for `0<=tau<=1` and every labelled prime.  In particular there is
no critical `p^(-1/2)` term in the gauge transfer.

Equivalently,

\[
 h_\tau(x)-e_\tau(x)
 =\tau(1-\tau)
 \left[2(1-x)\sqrt{1+x}-2+x+x^2\right],
\tag{L-102706.6}
\]

whose Taylor series begins with `-x^2/4`.

## 4. Global transfer

For a finite label set define

\[
E_\tau=\prod_\ell e_\tau(x_\ell),
\qquad
H_\tau=\prod_\ell h_\tau(x_\ell),
\qquad
G_\tau=\prod_\ell g_\tau(x_\ell).
\]

Then

\[
\boxed{H_\tau=G_\tau E_\tau.}
\tag{L-102706.7}
\]

Because every nonconstant local coefficient of `g_tau` and `g_tau^(-1)` starts
at activity `p^(-1)`, absolute coefficient majorants give, on a horizon `Y`,

\[
\boxed{
 \|G_\tau\|+\|G_\tau^{-1}\|
 \ll (\log(2Y))^C
}
\tag{L-102706.8}
\]

for one absolute `C`, uniformly in `tau`.  This follows from

\[
\prod_{p\le Y}(1+C/p)\ll(\log(2Y))^C.
\]

The extra labelled `67` changes only the implied constant.

## 5. Meaning

The Euler path is adapted to exact greatest-owner and moving-completion
cancellation.  The half-divisor path is adapted to root-free Hilbert
factorization.  Equation (L-102706.7) proves that these are two gauges of the
same source path, connected by a subcritical, polylogarithmically invertible
multiplier.

Consequently collaborators may use Euler coordinates in owner/activation
regions and half-divisor coordinates in balanced/occupancy regions without
introducing another critical source.  The gauge transfer must still occur
before regional absolute values.

This theorem does not prove the remaining cross-owner arithmetic estimate.