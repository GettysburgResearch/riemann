# L-34008 — Serial-exponential Mellin recurrence and the two-new-zero Hermite induction

Claim ID: `L-34008`

Status: **PROPOSED COMPLETE EXACT DIFFERENCE-EQUATION LEMMA — INDEPENDENT REVIEW REQUESTED**

Created: 2026-08-09

Dependencies: `L-34001`; elementary gamma/exponential calculus

Scope: exact `N -> N+1` recurrence for the finite raw Brownian factors and their forced negative-integer zeros; no RH-facing stability theorem and no RH claim

## 1. Resolve every Gamma(2) variable into two exponentials

Let

\[
\lambda_{2j-1}=\lambda_{2j}=j^2,
\qquad j\ge1,
\tag{L-34008.1}
\]

and let

\[
Y_m\sim\operatorname{Exp}(\lambda_m)
\]

be independent.  Since a shape-two unit-rate gamma is the sum of two independent unit-rate exponentials, scaling by `j^-2` gives exactly

\[
\boxed{
S_N
=\sum_{j=1}^N\frac{\Gamma_{2,j}}{j^2}
\overset d=
\sum_{m=1}^{2N}Y_m.
}
\tag{L-34008.2}

Put

\[
X_m=\sum_{r=1}^{m}Y_r,
\qquad
F_m(z)=\mathbb E[X_m^z].
\tag{L-34008.3}
\]

The initial domain `Re z>0` is sufficient for the calculation below; all identities then continue meromorphically/entirely through the natural moment domains.

## 2. One-exponential Mellin recurrence

Condition on `X_(m-1)=x`.  For `Y_m~Exp(lambda_m)`,

\[
I_m(z,x)
=\int_0^\infty
\lambda_m e^{-\lambda_m y}(x+y)^z\,dy.
\tag{L-34008.4}
\]

Integration by parts gives exactly

\[
\boxed{
I_m(z,x)
=x^z+\frac z{\lambda_m}I_m(z-1,x).
}
\tag{L-34008.5}

Averaging in `x` therefore yields

\[
\boxed{
F_m(z)
=F_{m-1}(z)
+\frac z{\lambda_m}F_m(z-1).
}
\tag{L-34008.6}

No asymptotic approximation is involved.

## 3. Gamma normalization removes the coefficient z

Define

\[
\boxed{
G_m(z)=\frac{F_m(z)}{\Gamma(z+1)}.
}
\tag{L-34008.7}

Since `Gamma(z+1)=z Gamma(z)`, equation (L-34008.6) becomes the constant-coefficient shift recurrence

\[
\boxed{
G_m(z)
=G_{m-1}(z)+\frac1{\lambda_m}G_m(z-1).
}
\tag{L-34008.8}

Equivalently, with the backward shift

\[
(E^{-1}f)(z)=f(z-1),
\]

\[
\boxed{
(1-\lambda_m^{-1}E^{-1})G_m=G_{m-1}.
}
\tag{L-34008.9}

This is the natural difference equation hidden by the partial-fraction formulas.

## 4. Pair the repeated Brownian rates

At the `N`-th Brownian stage the same rate `N^2` occurs twice.  Applying (L-34008.9) twice gives

\[
\boxed{
(1-N^{-2}E^{-1})^2G_{2N}=G_{2N-2}.
}
\tag{L-34008.10}

Expanding,

\[
\boxed{
G_{2N}(z)
-\frac{2}{N^2}G_{2N}(z-1)
+\frac1{N^4}G_{2N}(z-2)
=G_{2N-2}(z).
}
\tag{L-34008.11}

By `L-34001`,

\[
D_N(2z)
=\frac{\mathbb E[S_N^z]}{\Gamma(z+1)}
=G_{2N}(z).
\tag{L-34008.12}

Hence the finite Brownian raw factors themselves obey

\[
\boxed{
(1-N^{-2}E^{-1})^2D_N(2z)=D_{N-1}(2z).
}
\tag{L-34008.13}

The base case is especially simple:

\[
\boxed{D_1(2z)=z+1.}
\tag{L-34008.14}

## 5. Every new exponential forces one new negative-integer zero

The density of `X_m`, a convolution of `m` positive exponential densities, has the origin behavior

\[
f_{X_m}(x)=O(x^{m-1})
\qquad(x\downarrow0).
\tag{L-34008.15}

Consequently the negative moment `F_m(z)` is finite throughout

\[
\Re z>-m.
\tag{L-34008.16}

At every integer

\[
r=1,2,\ldots,m-1,
\]

`F_m(-r)` is finite and positive, whereas `Gamma(z+1)` has a pole at `z=-r`.  Therefore

\[
\boxed{
G_m(-r)=0,
\qquad1\le r\le m-1.
}
\tag{L-34008.17}

In particular,

\[
\boxed{
D_N(2z)=0
\quad\text{at}\quad
z=-1,-2,\ldots,-(2N-1).
}
\tag{L-34008.18}

Passing from `N-1` to `N` therefore adds exactly the two new forced interpolation zeros

\[
\boxed{z=-(2N-2),\qquad z=-(2N-1).}
\tag{L-34008.19}

These are the difference-equation counterpart of the twofold Hermite knots in `L-34003/L-34004`.

## 6. Homogeneous mode and the new reciprocal-square frequency

The homogeneous equation associated with one Brownian pair is

\[
(1-N^{-2}E^{-1})^2h=0.
\tag{L-34008.20}
\]

Its exponential-polynomial solutions have the form

\[
\boxed{
h(z)=N^{-2z}(Az+B)}
\tag{L-34008.21}
\]

(up to the usual period-one homogeneous freedom if no growth class is imposed).

Thus the `N`-th step of the difference equation introduces exactly the new frequency

\[
N^{-2z}
\]

with a linear coefficient in `z`, precisely as in the explicit numerator

\[
H_N(z)=\sum_{i=1}^NC_{N,i}i^{-2z}(z+\alpha_{N,i}).
\]

The two new negative-integer conditions (L-34008.19), together with the inherited equation, fix this new Hermite mode in the Brownian moment class.

## 7. Strategic consequence

The all-`N` raw Brownian problem now has three equivalent exact coordinates:

```text
Dirichlet mean / B-spline        L-34001/L-34003;
reciprocal Hermite interpolation L-34004;
serial-exponential difference equation  L-34008.
```

A cofinal proof need not estimate the full `N`-term exponential polynomial from scratch.  It may instead prove that the pair-addition boundary-value problem

\[
(1-N^{-2}E^{-1})^2G_N=G_{N-1}
\]

preserves the half-plane

\[
\Re z\le\frac14
\]

for all non-forced zeros in the Brownian moment/growth class.

That preservation theorem is not asserted here.

## 8. Proof boundary

Closed exactly:

1. serial exponential representation of `S_N`;
2. one-exponential Mellin recurrence;
3. gamma-normalized constant-shift recurrence;
4. exact paired-rate recurrence for `D_N`;
5. all forced negative-integer zeros;
6. the two-new-zero Hermite induction at every stage;
7. identification of the new homogeneous frequency.

Open:

1. a half-plane stability-preserver theorem for the paired difference step;
2. cofinal Brownian stability;
3. RH.
