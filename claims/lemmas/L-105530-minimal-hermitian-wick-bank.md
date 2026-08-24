# L-105530 — Minimal two-channel Hermitian Wick bank

Claim ID: `L-105530`  
Status: **PROVED EXACT AT FOLDED NORMAL-SOURCE SCOPE**  
Created: 2026-08-24  
Depends on: elementary Hermitian algebra  
RH status: **not assumed**

## 1. Folded reciprocal source

For a scalar `z` with `|z|<1`, put

\[
\mathfrak r(z)
=\Re\frac1{1-z}
=\frac{2-z-\bar z}{2(1-z)(1-\bar z)}>0.
\tag{L-105530.1}
\]

This is the scalar Hermitian source which appears after a right/left
safe-line pair has already been folded.  The lemma does not assert that this
folded boundary model is the complete Xi contour compression.

## 2. A scalar channel cannot cancel Hermitian degree two

Let

\[
w(z)=1+a z+b z^2+O(z^3).
\]

The expansion of `|w(z)|^2 mathfrak r(z)` has linear coefficients
`a+1/2` and `conj(a)+1/2`.  Cancelling both forces `a=-1/2`.  The coefficient
of `z bar z` at total degree two is then

\[
|a|^2+\Re(2a) /2
=|a|^2+a
=-\frac14,
\tag{L-105530.2}
\]

independently of `b`.  Therefore no single normalized holomorphic scalar
filter can satisfy

\[
|w(z)|^2\mathfrak r(z)=1+O(|z|^3).
\tag{L-105530.3}
\]

This is the Hermitian obstruction hidden by a formal analytic square.

## 3. Minimal two-channel repair

Define

\[
\boxed{
 w_0(z)=1-\frac z2-\frac{z^2}{4},
 \qquad
 w_1(z)=\frac z2.
}
\tag{L-105530.4}
\]

The cancellation is genuinely two-boundary.  For independent variables
`z,y`, put

\[
\mathfrak r(z,y)=\frac12\left(\frac1{1-z}+\frac1{1-y}\right),
\quad
S(z,y)=w_0(z)w_0(y)+w_1(z)w_1(y),
\quad
\Lambda(z,y)=S(z,y)\mathfrak r(z,y).
\tag{L-105530.5}
\]

A direct common-denominator calculation gives

\[
\boxed{
\Lambda(z,y)-1
=\frac{\mathcal N(z,y)}{32(1-z)(1-y)},
}
\tag{L-105530.6}
\]

where

\[
\begin{aligned}
\mathcal N(z,y)={}&
 4z^3+4y^3
 -2z^3y-2zy^3-2z^2y^2\\
&-z^3y^2-z^2y^3.
\end{aligned}
\tag{L-105530.7}
\]

Every bidegree of total degree one or two vanishes even before imposing a
Hermitian relation between the two boundary variables.  On the Hermitian
slice `y=bar z`, write `Lambda(z)=Lambda(z,bar z)`.  Since
`mathfrak r(z)>0` and `w_0,w_1` never vanish simultaneously,

\[
\boxed{\Lambda(z)>0\qquad(|z|<1).}
\tag{L-105530.8}
\]

For `|z|<=r<1`,

\[
\boxed{
|\Lambda(z)-1|
\le
\varepsilon(r)
:=\frac{r^3(4+3r+r^2)}{16(1-r)^2}.
}
\tag{L-105530.9}
\]

In particular, for `r<=1/4`,

\[
\boxed{
\frac{9139}{9216}
\le\Lambda(z)\le
\frac{9293}{9216}.
}
\tag{L-105530.10}
\]

## 4. Block interpretation

Let `z(t)` be a bounded scalar multiplication source on a measure space and
let `H(t)=mathfrak r(z(t))`.  Stack the two analytic channels over one base
observation space.  The fibre matrix is

\[
H(t)
\begin{pmatrix}w_0(z(t))\\w_1(z(t))\end{pmatrix}
\begin{pmatrix}\overline{w_0(z(t))}&\overline{w_1(z(t))}\end{pmatrix}.
\tag{L-105530.11}
\]

It is PSD, has rank one in channel space, and its sole nonzero eigenvalue is
`Lambda(z(t))`.  Thus two channels do not double-count the source dimension;
they provide the minimal Hermitian spectral factor which removes the first two
source levels.

## 5. Scope

The theorem is an exact folded-boundary model.  To use it for Xi one still
must construct a holomorphic strip observation map whose two boundary values
produce this bank and retain the finite-window Cauchy-index/partial-index
ledger.  That realization is `BANKREAL105530` and is not proved here.
