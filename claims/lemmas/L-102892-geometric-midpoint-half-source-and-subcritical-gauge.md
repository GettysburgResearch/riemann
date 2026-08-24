# L-102892 — The native/squared geometric midpoint is an eventually positive half-source

Claim ID: `L-102892`  
Status: **PROVED EXACT SOURCE FACTORIZATION AND UNCONDITIONAL TAIL SIGN**  
Created: 2026-08-24  
Depends on: `L-102700`, `L-102891`  
RH status: **not assumed**

Let

\[
\beta=(\delta_1-\delta_{67})*\mu
\]

be the native duplicate-67 source and let \(\beta^\square\) denote its square
lift.  Let \(\lambda\) be the formal half-divisor source of `L-102700`, so
that

\[
\lambda*\lambda=\beta,
\qquad
\lambda^\square*\lambda^\square=\beta^\square.
\]

Define the geometric-midpoint source

\[
\boxed{
\eta=\lambda*\lambda^\square.
}
\tag{L-102892.1}
\]

Then

\[
\boxed{
\eta*\eta=\beta*\beta^\square.
}
\tag{L-102892.2}
\]

No analytic branch choice enters this coefficient identity; it holds in every
finite commutative labelled Euler algebra before physical collapse.

## 1. Dirichlet multiplier

If

\[
E(z)=\sum_n\eta(n)n^{-z},
\]

then

\[
\boxed{
E(z)^2
=
\frac{(1-67^{-z})(1-67^{-2z})}
{\zeta(z)\zeta(2z)}.
}
\tag{L-102892.3}
\]

Taking the branch positive on the real half-line \(z>1\),

\[
\boxed{
E(z)=\zeta(z)^{-1/2}G_\eta(z),
}
\tag{L-102892.4}
\]

where

\[
\boxed{
G_\eta(z)
=
\left[
\frac{(1-67^{-z})(1-67^{-2z})}{\zeta(2z)}
\right]^{1/2}
}
\tag{L-102892.5}
\]

is analytic and nonzero in a neighborhood of \(\Re z\ge1\), with

\[
G_\eta(1)
=
\left[
\frac{(1-67^{-1})(1-67^{-2})}{\zeta(2)}
\right]^{1/2}>0.
\tag{L-102892.6}
\]

At one ordinary labelled prime, the local factor is

\[
\boxed{
(1-x)\sqrt{1+x}
=
\sqrt{(1-x)(1-x^2)}.
}
\tag{L-102892.7}
\]

Thus \(\eta\) is literally the geometric midpoint between the native and
squared Euler factors.

## 2. Eventual positivity in the fixed outer observation

Define

\[
H_\eta(X)
=
\sum_n\frac{\eta(n)}{\sqrt n}R_L(X/n).
\]

Applying the kernelized Selberg–Delange calculation of `L-102891` with
exponent \(-1/2\) gives

\[
\boxed{
H_\eta(X)
=
\frac{\widehat R_L(1/2)G_\eta(1)}{\Gamma(-1/2)}
\frac{\sqrt X}{(\log X)^{3/2}}
\left(1+O\!\left(\frac1{\log X}\right)\right).
}
\tag{L-102892.8}
\]

Since

\[
\widehat R_L(1/2)<0,
\qquad
\Gamma(-1/2)=-2\sqrt\pi<0,
\]

one has

\[
\boxed{H_\eta(X)>0\quad\text{eventually}.}
\tag{L-102892.9}
\]

This is an unconditional positive half-source whose exact arithmetic square
contains the native detector.

## 3. Relation to the arithmetic midpoint completion

Let \(B_{1/2}(z)\) be the source of `L-102891` with \(c=1/2\).  At one label,

\[
f_{1/2}(x)=(1-x)(1+x/2).
\]

The exact local identity

\[
\boxed{
\frac{f_{1/2}(x)^2}{(1-x)(1-x^2)}
=
\frac{(1+x/2)^2}{1+x}
=
1+\frac{x^2}{4(1+x)}
}
\tag{L-102892.10}
\]

shows that

\[
\boxed{
B_{1/2}(z)^2
=E(z)^2G_{\rm mid}(z),
}
\tag{L-102892.11}
\]

where \(G_{\rm mid}\) is the labelled Euler product of the last local factor.
Both \(G_{\rm mid}\) and its inverse begin at squared activity and have
finite-horizon source \(\ell^1\) norm bounded by a power of \(\log Y\).

Thus the arithmetic midpoint and geometric midpoint are related by a
subcritical two-sided gauge.  This statement concerns source/energy norms; the
gauge is signed and is not claimed to preserve one-sided negative mass.

## Exact boundary

The eventual positivity of \(H_\eta\) is a first-order half-source theorem.
The detector-bearing object is its arithmetic source square
\(\eta*\eta\), not the pointwise square of the scalar field
\(H_\eta\).  The exact positive inverse from that source square to the native
source is constructed in `L-102893`.
