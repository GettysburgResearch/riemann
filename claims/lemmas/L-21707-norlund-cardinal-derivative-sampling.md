# L-21707 — Exact cardinal derivative sampling behind the Nörlund approximants

Claim ID: `L-21707`  
Title: The logarithmic Brownian–Nörlund Dirichlet spline is a derivative sample of one positive-definite binomial-cardinal kernel  
Status: **PROPOSED COMPLETE EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-21705`, `L-21706`; elementary gamma differentiation and the beta integral  
Scope: finite exact structure; no zero-location or RH conclusion

## 1. Continuous binomial-cardinal functions

For an integer `K>=1`, define

\[
R_K(x)
=\frac{\Gamma(K+1)^2}
       {\Gamma(K+1-x)\Gamma(K+1+x)}.
\tag{L-21707.1}
\]

At an integer `0<=n<=K`,

\[
\boxed{
R_K(n)
=\frac{\binom{2K}{K-n}}{\binom{2K}{K}}.}
\tag{L-21707.2}
\]

At every integer `n>K`, `R_K` has a simple zero. Hence `R_K(x)^2` has a double zero there.

The finite Brownian coefficient of `L-21705` is exactly

\[
\boxed{C_{K,n}=4R_K(n)^2.}
\tag{L-21707.3}
\]

## 2. One positive continuous kernel

Put

\[
\boxed{
B_N(x)
=\frac{2}{H_N}
  \sum_{K=1}^N\frac{R_K(x)^2}{K}.}
\tag{L-21707.4}
\]

Let

\[
\overline D_N(s)
=\sum_{n=1}^N(\alpha_{N,n}+s\beta_{N,n})n^{-s}
\tag{L-21707.5}
\]

be the Nörlund Dirichlet spline from `L-21706`. Then

\[
\boxed{\beta_{N,n}=B_N(n).}
\tag{L-21707.6}
\]

Differentiate (L-21707.1):

\[
\frac{R_K'(x)}{R_K(x)}
=\psi(K+1-x)-\psi(K+1+x).
\tag{L-21707.7}
\]

At an active integer `1<=n<=K`, this is

\[
\frac{R_K'(n)}{R_K(n)}
=-(H_{K+n}-H_{K-n}).
\tag{L-21707.8}
\]

Consequently the complete constant coefficient is the sampled product derivative

\[
\boxed{
\alpha_{N,n}
=-\left.\frac{d}{dx}\bigl[xB_N(x)\bigr]\right|_{x=n}.}
\tag{L-21707.9}
\]

Indeed, for one endpoint `K`,

\[
-\frac{d}{dx}\left[2xR_K(x)^2\right]_{x=n}
=4R_K(n)^2
 \left[n(H_{K+n}-H_{K-n})-\frac12\right],
\]

which is precisely the raw coefficient in `L-21705`; logarithmic averaging preserves the identity.

## 3. Exact derivative-sampling normal form

Equations (L-21707.6) and (L-21707.9) give

\[
\boxed{
\begin{aligned}
\overline D_N(s)
&=\sum_{n=1}^{\infty}
 \left[(s-1)B_N(n)-nB_N'(n)\right]n^{-s}\\
&=-\sum_{n=1}^{\infty}
 \left.\frac{d}{dx}
 \left[x^{1-s}B_N(x)\right]\right|_{x=n}.
\end{aligned}}
\tag{L-21707.10}
\]

The sums are actually finite. For every integer `n>N`, every summand in (L-21707.4) has a double zero, so both `B_N(n)` and `B_N'(n)` vanish.

This is the first proof-facing form in which the linear coefficient in `s` and the harmonic constant term are not independent data: they are the value and derivative of the same positive kernel.

## 4. Positive-definite Fourier representation

The beta integral gives, for real `x`,

\[
\boxed{
R_K(x)
=\frac{\displaystyle
 \int_{-\pi}^{\pi}
 \cos^{2K}(\theta/2)e^{ix\theta}\,d\theta}
 {\displaystyle
 \int_{-\pi}^{\pi}
 \cos^{2K}(\theta/2)\,d\theta}.}
\tag{L-21707.11}
\]

Thus `R_K` is the characteristic function of one explicit symmetric probability law on `[-pi,pi]`. Its square is the characteristic function of the sum of two independent copies. Therefore

\[
\boxed{\frac12B_N(x)}
\tag{L-21707.12}
\]

is a convex mixture of characteristic functions, hence is positive definite. In addition,

\[
B_N(x)\ge0\quad(x\in\mathbb R),
\qquad
B_N(0)=2.
\tag{L-21707.13}
\]

The nonnegativity is stronger than ordinary positive definiteness and comes from the literal squares in (L-21707.4).

## 5. Limit to the zeta source

For every fixed complex `x`, the gamma ratio gives

\[
R_K(x)\longrightarrow1.
\]

Logarithmic Cesàro averaging therefore gives

\[
B_N(x)\longrightarrow2
\tag{L-21707.14}
\]

at each fixed `x`. Consistently, `L-21706` yields locally uniformly in the open critical strip

\[
\boxed{
\overline D_N(s)
\longrightarrow
2(s-1)\zeta(s).}
\tag{L-21707.15}
\]

To see the normalization directly, divide
`overline m_N(s)->2 xi(s)` by

\[
\pi^{-s/2}\Gamma(1+s/2)
=\frac{s}{2}\pi^{-s/2}\Gamma(s/2).
\]

## 6. New proof interface

The exact finite stability problem is now:

```text
positive-definite nonnegative cardinal kernel B_N
-> derivative samples -d[x^(1-s)B_N(x)] at the integers
-> exponential polynomial Dbar_N(s)
-> prove no zero with Re(s)>1/2.
```

This formulation exposes three possible production mechanisms:

1. a Hermite–Biehler theorem for the derivative-sampled cardinal kernel;
2. a positive inverse-Laplace resolvent for `1/Dbar_N(1/2+z)`;
3. a variation-diminishing theorem using the beta-angle representation (L-21707.11).

None of these stability theorems is asserted in this lemma.

## 7. Proof boundary

Closed exactly:

- the continuous gamma/cardinal extension;
- the binomial coefficient identity;
- the coefficient/product-derivative identity;
- the finite derivative-sampling formula;
- the positive-definite Fourier representation;
- compatibility with the zeta limit.

Open:

- right-half-plane stability of `overline D_N`;
- reciprocal complete monotonicity;
- RH.
