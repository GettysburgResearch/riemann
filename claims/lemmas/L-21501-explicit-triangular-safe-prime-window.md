# L-21501 — Explicit triangular safe prime window

Claim ID: `L-21501`  
Title: A finite piecewise-linear window cancels the zeta pole and has no Laplace zeros in the open counterexample strip  
Status: `PROPOSED — COMPLETE ELEMENTARY CONSTRUCTION`  
Authoring agent: `gpt56-pro-17`  
Created: 2026-08-07  
Issue: #215  
Dependencies: elementary convolution and Laplace-transform algebra  
Scope: the fixed raw-prime signal in `T-21501`

## 1. Triangular base

Let

\[
 b(u)=\mathbf1_{[0,1]}(u)
\]

and put

\[
 \phi=b*b.
\]

Explicitly,

\[
 \phi(u)=
 \begin{cases}
 u,&0\le u\le1,\\
 2-u,&1\le u\le2,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{L-21501.1}
\]

Use the bilateral Laplace convention

\[
 \widehat f(z)=\int_{\mathbb R}f(u)e^{-zu}\,du.
\]

Then

\[
 \widehat b(z)=\frac{1-e^{-z}}{z}
\]

with the removable value `1` at `z=0`, and

\[
 \widehat\phi(z)=\left(\frac{1-e^{-z}}{z}\right)^2.
 \tag{L-21501.2}
\]

## 2. Pole-annihilating difference

Put

\[
 h=\log4,
 \qquad a=1,
\]

and define

\[
 \boxed{
 G(u)=\phi(u-a)-2\phi(u-a-h).}
 \tag{L-21501.3}
\]

Thus `G` is a real continuous piecewise-linear function supported in

\[
 [1,3+\log4].
\]

Its transform is exactly

\[
 \boxed{
 \widehat G(z)
 =e^{-z}
  \left(\frac{1-e^{-z}}{z}\right)^2
  \left(1-2\,4^{-z}\right).}
 \tag{L-21501.4}
\]

At the shifted zeta pole,

\[
 \widehat G(1/2)=0
\]

because

\[
 2\,4^{-1/2}=1.
\]

## 3. Exact zero set

The exponential factor has no zeros. The triangular factor has zeros

\[
 z=2\pi i k,
 \qquad k\in\mathbb Z\setminus\{0\},
\]

all on `Re z=0`, each with multiplicity two.

The pole-annihilation factor vanishes when

\[
 4^{-z}=\frac12.
\]

Hence its zero set is

\[
 \boxed{
 z=\frac12-\frac{\pi i k}{\log2},
 \qquad k\in\mathbb Z,}
 \tag{L-21501.5}
\]

all on `Re z=1/2`.

Therefore

\[
 \boxed{
 \widehat G(z)\ne0
 \qquad\left(0<\operatorname{Re}z<\frac12\right).}
 \tag{L-21501.6}
\]

The construction is finite. No infinite convolution, limiting spline, or
numerical zero search is needed.

## 4. Vertical decay

For `sigma` in a fixed bounded interval,

\[
 |1-e^{-\sigma-it}|\le1+e^{-\sigma},
\]

and the final factor is bounded on the same strip. Thus

\[
 \boxed{
 |\widehat G(\sigma+it)|
 \le C_\sigma(1+|t|)^{-2}.}
 \tag{L-21501.7}
\]

Two powers are enough for the Hardy-energy argument because the zeta logarithmic
derivative has at most polylogarithmic growth on every fixed zero-free
half-plane.

## 5. Explicit autocorrelation

Let

\[
 C_\phi(t)=\int_{\mathbb R}\phi(u)\phi(u+t)\,du.
\]

It is the centered cubic cardinal B-spline

\[
 \boxed{
 C_\phi(t)
 =\frac16\sum_{j=0}^{4}(-1)^j\binom4j(t+2-j)_+^3.}
 \tag{L-21501.8}
\]

In particular, `C_phi` is even, supported on `[-2,2]`, nonnegative, and

\[
 C_\phi(0)=\frac23.
\]

The shift `a` disappears from the autocorrelation of `G`, giving

\[
 \boxed{
 C_G(t)
 =5C_\phi(t)-2C_\phi(t-h)-2C_\phi(t+h),
 \qquad h=\log4.}
 \tag{L-21501.9}
\]

Although `C_G` may change sign pointwise, every finite matrix

\[
 (C_G(u_i-u_j))_{i,j}
\]

is positive semidefinite because it is a Gram matrix of translates of `G`.
This piecewise-cubic formula is the exact interior kernel in the finite
prime-pair energy of `L-21502`.

## 6. Relation to earlier safe-window work

The universal smooth window of the terminal-prime programme is valuable for
arbitrary-order zero-tail estimates. The present construction serves a
different purpose: it is the smallest explicit finite window needed for a
Hardy `H^2` global-growth criterion.

Its advantages are:

- exact finite support and coefficients;
- exact boundary-line zero set;
- sufficient vertical decay;
- an explicit piecewise-cubic autocorrelation;
- direct finite prime-pair energy production.

It does not supersede smoother windows when high derivative order is needed.

## 7. Proof boundary

All assertions are elementary consequences of (L-21501.4). This lemma supplies
the safe filter; it does not prove the subexponential prime-energy estimate of
`T-21501`.
