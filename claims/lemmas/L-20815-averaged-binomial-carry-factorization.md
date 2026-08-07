# L-20815 — Averaged binomial carry factorization

Claim ID: `L-20815`  
Title: The positive square-cutoff prime ramp is a nonnegative linear image of averaged logarithmic binomial coefficients  
Status: `PROPOSED — COMPLETE FINITE IDENTITIES AND CONTINUUM ENTROPY DUAL`  
Authoring agent: `gpt56-03-x`  
Created: 2026-08-07  
Dependencies: Legendre's factorial valuation formula; elementary binary entropy  
Scope: exact finite arithmetic factorization behind `T-20804`

## 1. One carry at one prime-power scale

For integers `n>=2`, `0<=j<=n`, and `q>=2`, define

\[
 b_{n,j}(q)
 =\left\lfloor{n\over q}\right\rfloor
 -\left\lfloor{j\over q}\right\rfloor
 -\left\lfloor{n-j\over q}\right\rfloor.
 \tag{L-20815.1}
\]

Since the sum of the last two real arguments is `n/q`, one has

\[
 \boxed{b_{n,j}(q)\in\{0,1\}.}
 \tag{L-20815.2}
\]

For a prime power `q=p^k`, Legendre's formula gives

\[
 v_p\binom nj
 =\sum_{k\ge1}b_{n,j}(p^k).
 \tag{L-20815.3}
\]

Multiplying by `log p` and summing over primes yields the exact finite identity

\[
 \boxed{
 \log\binom nj
 =\sum_{q=p^k\le n}\Lambda(q)b_{n,j}(q).}
 \tag{L-20815.4}
\]

No prime theorem or asymptotic estimate is involved.

## 2. Exact averaged carry coefficient

Average over every binomial position:

\[
 \beta_{nq}={1\over n+1}\sum_{j=0}^n b_{n,j}(q).
 \tag{L-20815.5}
\]

Write

\[
 n=a q+r,
 \qquad a=\left\lfloor{n\over q}\right\rfloor,
 \qquad0\le r<q.
 \tag{L-20815.6}
\]

Then a direct floor summation gives

\[
 \boxed{
 \beta_{nq}
 ={a(q-1-r)\over n+1}
 \quad(2\le q\le n).}
 \tag{L-20815.7}
\]

In particular,

\[
 0\le\beta_{nq}<1,
 \qquad
 \beta_{nn}={n-1\over n+1}>0.
 \tag{L-20815.8}
\]

### Proof of (L-20815.7)

The two floor sums in (L-20815.1) have the same total under `j -> n-j`, so

\[
 (n+1)\beta_{nq}
 =(n+1)a-2\sum_{j=0}^n\left\lfloor{j\over q}\right\rfloor.
 \tag{L-20815.9}
\]

There are `q` occurrences of each quotient `0,...,a-1` and `r+1`
occurrences of quotient `a`. Hence

\[
 \sum_{j=0}^n\left\lfloor{j\over q}\right\rfloor
 ={qa(a-1)\over2}+a(r+1).
 \tag{L-20815.10}
\]

Substitution and `n=aq+r` give (L-20815.7). QED.

## 3. Averaged logarithmic binomial ledger

Define

\[
 \boxed{
 G_n={1\over n+1}\sum_{j=0}^n\log\binom nj.}
 \tag{L-20815.11}
\]

Averaging (L-20815.4) gives

\[
 \boxed{
 G_n=\sum_{q=p^k\le n}\Lambda(q)\beta_{nq}.}
 \tag{L-20815.12}
\]

Thus the matrix `B=(beta_(nq))` maps the von Mangoldt vector to a vector of
manifestly nonnegative logarithms of integers.

The ledger also has the exact factorial form

\[
 \boxed{
 G_n=\log(n!)-{2\over n+1}\sum_{j=0}^n\log(j!).}
 \tag{L-20815.13}
\]

This permits an independent producer with no prime enumeration.

## 4. Positive finite minorant interface

For a real cutoff `X>=2`, put

\[
 w_X(q)={1\over\sqrt q}\log{X\over q},
 \qquad2\le q\le X,
 \tag{L-20815.14}
\]

and define the positive prime ramp

\[
 \mathcal R(X)
 =\sum_{q=p^k\le X}\Lambda(q)w_X(q).
 \tag{L-20815.15}
\]

Let `c_n>=0` be any finite family satisfying

\[
 \boxed{
 \sum_{n=q}^{\lfloor X\rfloor}c_n\beta_{nq}
 \le w_X(q)
 \qquad(2\le q\le X).}
 \tag{L-20815.16}
\]

Multiplying by `Lambda(q)>=0`, summing, and using (L-20815.12) gives

\[
 \boxed{
 \mathcal R(X)
 \ge\sum_{n=2}^{\lfloor X\rfloor}c_nG_n.}
 \tag{L-20815.17}
\]

This is a cancellation-free, finite, proof-producing interface. Every
coefficient on both sides is nonnegative.

## 5. Continuum carry kernel

For `x>=1` and `0<=theta<=1`, define

\[
 b_\theta(x)
 =\lfloor x\rfloor-\lfloor\theta x\rfloor
  -\lfloor(1-\theta)x\rfloor\in\{0,1\}.
 \tag{L-20815.18}
\]

Its uniform average is

\[
 \boxed{
 K(x)=\int_0^1b_\theta(x)d\theta
 ={\lfloor x\rfloor(1-\{x\})\over x},}
 \tag{L-20815.19}
\]

with the right-continuous value `K(m)=1` at integers. The finite coefficient is
slightly smaller than its continuum model:

\[
 \boxed{
 \beta_{nq}\le K(n/q).}
 \tag{L-20815.20}
\]

Indeed, with (L-20815.6),

\[
 K(n/q)={a(q-r)\over n},
\]

and direct subtraction from (L-20815.7) is positive.

## 6. Carry integral equals binary entropy

Let

\[
 H(\theta)
 =-\theta\log\theta-(1-\theta)\log(1-\theta).
 \tag{L-20815.21}
\]

Then

\[
 \boxed{
 \int_1^\infty {b_\theta(x)\over x^2}dx
 =H(\theta).}
 \tag{L-20815.22}
\]

One proof writes

\[
 b_\theta(x)=\{\theta x\}+\{(1-\theta)x\}-\{x\}
\]

and integrates by parts across the jump sets. Equivalently, truncate at `R`,
collect the jumps, and use the harmonic-number asymptotic; all logarithmic
cutoff terms cancel, leaving (L-20815.21).

Averaging in `theta` gives the exact normalization

\[
 \boxed{
 \int_1^\infty {K(x)\over x^2}dx
 =\int_0^1H(\theta)d\theta={1\over2}.}
 \tag{L-20815.23}
\]

This is why the leading constant in the carry programme is exactly the
archimedean constant `4`, rather than a numerical approximation to it.

## 7. Mellin transform and the zeta boundary

For `0<Re(s)<1`, scaling the fractional-part integral gives

\[
 \boxed{
 \int_1^\infty K(x)x^{-s-1}dx
 ={s-1\over s(s+1)}\zeta(s).}
 \tag{L-20815.24}
\]

Indeed,

\[
 \int_0^\infty\{ax\}x^{-s-1}dx
 =-a^s{\zeta(s)\over s},
\]

and

\[
 \int_0^1[\theta^s+(1-\theta)^s-1]d\theta
 ={1-s\over s+1}.
\]

Equation (L-20815.24) is both useful and cautionary: exact inversion of the
carry kernel introduces `1/zeta(s)`. A positivity theorem for that inverse
cannot be assumed from the positivity of the forward carry ledger.

## 8. Entropy lower bound for `G_n`

The elementary binomial entropy bound

\[
 \binom nj\ge{1\over n+1}\exp\{nH(j/n)\}
 \tag{L-20815.25}
\]

and a two-monotone-piece Riemann-sum estimate for `H` give the safe uniform
bound

\[
 \boxed{
 G_n\ge {n\over2}-\log(n+1)-3
 \qquad(n\ge2).}
 \tag{L-20815.26}
\]

The constant is deliberately loose. The true expansion begins
`n/2-(1/2)log n+O(1)`, but no sharp Stirling constant is needed by the
completion theorem.

## 9. Proof boundary

Closed exactly:

- every carry and averaged-carry identity;
- the positive finite minorant implication;
- the continuum entropy integral;
- the Mellin transform;
- a uniform entropy lower bound for the averaged binomial ledger.

Open:

- construction, at every cutoff, of coefficients `c_n>=0` saturating the
  target weights to the accuracy required by `T-20804`.

`L-20816/T-20805` isolate that construction as one explicit triangular
positivity theorem.