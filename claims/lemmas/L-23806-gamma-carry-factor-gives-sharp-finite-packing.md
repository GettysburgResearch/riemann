# L-23806 — Gamma–carry factorization gives a sharp finite carry packing

Claim ID: `L-23806`  
Title: A nonnegative Gamma–carry residual produces explicit finite packing coefficients with entropy mass `4 sqrt(X)-X^{o(1)}`  
Status: **PROPOSED COMPLETE CONDITIONAL THEOREM — EXACTLY CONDITIONAL ON GCF**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `L-23801`, `L-23804`, `L-23805`  
Scope: exact finite bridge from the continuum factor to the prime ramp

## 1. The continuum packing identity

Assume GCF from `L-23805`, and let `a(t)>=0` be its probability density. Put

\[
 \kappa(t)=e^{-t/2}K(e^t),
 \qquad t\ge0,
 \tag{L-23806.1}
\]

where `K` is the carry kernel of `L-23804`, and define

\[
 c(t)=8e^{t/2}a(t).
 \tag{L-23806.2}
\]

The Laplace transforms are

\[
 \widehat\kappa(s)
 ={(s-\tfrac12)\zeta(s+\tfrac12)
   \over(s+\tfrac12)(s+\tfrac32)},
 \tag{L-23806.3}
\]

and, by (L-23805.4),

\[
 \widehat c(s)=8A(s-\tfrac12)
 ={(s+\tfrac12)(s+\tfrac32)
   \over s^2(s-\tfrac12)\zeta(s+\tfrac12)}.
 \tag{L-23806.4}
\]

Therefore

\[
 \widehat c(s)\widehat\kappa(s)={1\over s^2}.
\]

Laplace uniqueness gives the exact convolution identity

\[
 \boxed{
 (c*\kappa)(t)=t,
 \qquad t\ge0.}
 \tag{L-23806.5}
\]

## 2. Explicit finite coefficients

For an integer `X>=3`, define

\[
 \boxed{
 d_X(n)=8\sqrt X
 \int_n^{n+1}y^{-2}
 a\!\left(\log{X\over y}\right)dy,}
 \tag{L-23806.6}
\]

for `2<=n<=X-1`, and put `d_X(X)=0`. These coefficients are nonnegative.

Let

\[
 w_X(q)=q^{-1/2}\log(X/q).
\]

Then

\[
 \boxed{
 \sum_{n=q}^{X}d_X(n)\beta_{nq}
 \le w_X(q)
 \qquad(2\le q\le X).}
 \tag{L-23806.7}
\]

### Proof

By `L-23804.3`, for `y in [n,n+1]`,

\[
 \beta_{nq}\le K(y/q).
\]

Hence the left side of (L-23806.7) is at most

\[
 8\sqrt X\int_q^X
 y^{-2}a(\log(X/y))K(y/q)dy.
 \tag{L-23806.8}
\]

Put

\[
 t=\log(X/q),
 \qquad s=\log(X/y).
\]

Then (L-23806.8) becomes

\[
 q^{-1/2}(c*\kappa)(t).
\]

Equation (L-23806.5) makes this exactly

\[
 q^{-1/2}t=w_X(q).
\]

Thus `d_X` is an exact nonnegative packing beneath the complete finite carry
matrix. QED.

## 3. Entropy mass

Let `S` be the random variable with density `a`. For every fixed

\[
 0<\eta<1/2,
\]

GCF and (L-23805.4) give the finite exponential moment

\[
 \boxed{
 \mathbb E[e^{\eta S}]=A(-\eta)<\infty.}
 \tag{L-23806.9}
\]

Using `n>=y-1` on `[n,n+1]`,

\[
 \begin{aligned}
 {1\over2}\sum_{n=2}^{X-1}n d_X(n)
 &\ge4\sqrt X\int_2^X
 (y-1)y^{-2}a(\log(X/y))dy\\
 &=4\sqrt X\left[
 \int_0^{\log(X/2)}a(s)ds
 -{1\over X}
  \int_0^{\log(X/2)}e^sa(s)ds
 \right].
 \end{aligned}
 \tag{L-23806.10}
\]

Markov's inequality with (L-23806.9) bounds both losses inside the brackets by

\[
 O_\eta(X^{-\eta}).
\]

Consequently

\[
 \boxed{
 {1\over2}\sum_{n=2}^{X-1}n d_X(n)
 \ge4\sqrt X-O_\eta(X^{1/2-\eta}).}
 \tag{L-23806.11}
\]

The same calculation without the factor `n` gives

\[
 \sum_{n=2}^{X-1}d_X(n)
 =O_\eta(X^{1/2-\eta}).
 \tag{L-23806.12}
\]

Now use the entropy estimate of `L-23801`,

\[
 G_n\ge{n\over2}-C\log(n+1).
\]

Equations (L-23806.11)--(L-23806.12) yield, for every `epsilon>0`,

\[
 \boxed{
 \sum_{n=2}^{X}d_X(n)G_n
 \ge4\sqrt X-O_\epsilon(X^\epsilon).}
 \tag{L-23806.13}
\]

Here one first chooses `eta` arbitrarily close to `1/2`, then absorbs the
logarithmic factor into a slightly larger `epsilon`.

## 4. Prime-ramp consequence

The packing implication of `L-23801` gives

\[
 \boxed{
 \mathcal P(X)
 :=\sum_{q=p^k\le X}{\Lambda(q)\over\sqrt q}
 \log{X\over q}
 \ge4\sqrt X-O_\epsilon(X^\epsilon).}
 \tag{L-23806.14}
\]

No prime-number theorem, zero-free region, or asymptotic replacement of the
finite carry matrix is used. Every prime power is retained with its exact
nonnegative von Mangoldt coefficient.

## 5. Why the construction is sharp

The constant `4` is not fitted. It is the product of:

1. the exact carry mass
   \[
   \int_1^\infty K(x)x^{-2}dx=1/2;
   \]
2. the gamma normalization in `L-23805`;
3. the entropy main term `G_n~n/2`.

The finite coefficients (L-23806.6) are a positive cell average of the exact
Gamma–carry residual. They are not the potentially signed triangular inverse
`c_X` of `L-23802`.

## 6. Proof boundary

Everything in this file is proved from GCF. The only unproved input is the
nonnegativity of the density `a` in `L-23805.8`.

In particular, once GCF is verified, no further carry positivity, LP optimum,
Möbius negative-mass estimate, or discretization theorem remains.
