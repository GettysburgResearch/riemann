# L-9508 — Exact Bernoulli–Möbius decomposition of the quartic totient error

Claim ID: `L-9508`  
Title: A quartic cutoff turns the centered totient error into five explicit Mertens channels  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: Möbius inversion for `phi(n)/n`; elementary Bernoulli/Faulhaber identities  
Scope: proof-facing arithmetic decomposition for `T-9502`  
Related counterexample candidates: none

## Exact quartic cell sum

For real `y>1`, define

\[
S_2(y)=\sum_{1\le m<y}
 \left(1-\frac{m^2}{y^2}\right)^2.
\tag{L-9508.1}
\]

Let `{y}=y-floor(y)` and use the Bernoulli polynomials

\[
B_3(u)=u^3-\frac32u^2+\frac12u,
\tag{L-9508.2}
\]

\[
B_4(u)=u^4-2u^3+u^2-\frac1{30},
\tag{L-9508.3}
\]

\[
B_5(u)=u^5-\frac52u^4+\frac53u^3-\frac16u.
\tag{L-9508.4}
\]

Then the finite sum has the exact formula

\[
\boxed{
S_2(y)=
\frac{8y}{15}-\frac12
-\frac{4}{3y^2}B_3(\{y\})
+\frac1{y^3}B_4(\{y\})
-\frac1{5y^4}B_5(\{y\}).}
\tag{L-9508.5}
\]

This remains valid when `y` is an integer. The endpoint term has weight zero,
so the strict cutoff `m<y` creates no convention ambiguity.

## First proof: finite Faulhaber algebra

Put

\[
r=\lceil y\rceil-1=y-\{y\}
\]

with the integer-endpoint interpretation `r=y-1` when `{y}=0`. Expand

\[
S_2(y)
=r-\frac2{y^2}\sum_{m=1}^r m^2
 +\frac1{y^4}\sum_{m=1}^r m^4.
\]

Insert

\[
\sum_{m=1}^r m^2=\frac{r(r+1)(2r+1)}6,
\]

\[
\sum_{m=1}^r m^4=
\frac{r(r+1)(2r+1)(3r^2+3r-1)}{30},
\]

write `r=y-{y}`, and collect powers. The result is exactly (L-9508.5).

## Second proof: compact Poisson/Bernoulli transform

For

\[
k_2(u)=(1-u^2)^2\mathbf1_{|u|<1},
\]

its Fourier transform at `t=2*pi*xi` is

\[
\widehat k_2(\xi)
=16\frac{(3-t^2)\sin t-3t\cos t}{t^5}.
\tag{L-9508.6}
\]

Poisson summation gives

\[
S_2(y)=\frac{8y}{15}-\frac12
+y\sum_{\ell\ge1}\widehat k_2(\ell y).
\tag{L-9508.7}
\]

Using

\[
\sum_{\ell\ge1}\frac{\sin(2\pi\ell y)}{\ell^3}
=\frac{2\pi^3}{3}B_3(\{y\}),
\]

\[
\sum_{\ell\ge1}\frac{\cos(2\pi\ell y)}{\ell^4}
=-\frac{\pi^4}{3}B_4(\{y\}),
\]

\[
\sum_{\ell\ge1}\frac{\sin(2\pi\ell y)}{\ell^5}
=-\frac{2\pi^5}{15}B_5(\{y\}),
\]

one obtains (L-9508.5) again.

## Quartic totient observable

For real `x>1`, put

\[
\mathcal Q(x)=
\frac1x\sum_{1\le n<x}
 \frac{\varphi(n)}n
 \left(1-\frac{n^2}{x^2}\right)^2
\tag{L-9508.8}
\]

and

\[
\mathcal E_2(x)=\mathcal Q(x)-\frac{16}{5\pi^2}.
\tag{L-9508.9}
\]

Using

\[
\frac{\varphi(n)}n=\sum_{d\mid n}\frac{\mu(d)}d
\]

and applying (L-9508.5) at `y=x/d` gives the exact decomposition

\[
\boxed{
\begin{aligned}
\mathcal E_2(x)={}&
-\frac8{15}\sum_{d\ge x}\frac{\mu(d)}{d^2}
-\frac1{2x}\sum_{d<x}\frac{\mu(d)}d\\
&-\frac4{3x^3}\sum_{d<x}
 \mu(d)d B_3\!\left(\left\{\frac xd\right\}\right)\\
&+\frac1{x^4}\sum_{d<x}
 \mu(d)d^2 B_4\!\left(\left\{\frac xd\right\}\right)\\
&-\frac1{5x^5}\sum_{d<x}
 \mu(d)d^3 B_5\!\left(\left\{\frac xd\right\}\right).
\end{aligned}}
\tag{L-9508.10}
\]

The first series is absolutely convergent; every other sum is finite.

The main constant follows from

\[
\frac8{15}\sum_{d\ge1}\frac{\mu(d)}{d^2}
=\frac8{15\zeta(2)}
=\frac{16}{5\pi^2}.
\tag{L-9508.11}
\]

## Mertens transfer

Let

\[
M(X)=\sum_{n\le X}\mu(n).
\]

Suppose, for some `beta in [1/2,1]`, that for every `epsilon>0`,

\[
M(X)=O_\varepsilon(X^{\beta+\varepsilon}).
\tag{L-9508.12}
\]

Then

\[
\boxed{
\mathcal E_2(x)
=O_\varepsilon(x^{\beta-2+\varepsilon}).}
\tag{L-9508.13}
\]

### Proof

The first two lines follow by ordinary partial summation:

\[
\sum_{d\ge x}\frac{\mu(d)}{d^2}
=O_\varepsilon(x^{\beta-2+\varepsilon}),
\]

\[
\sum_{d<x}\frac{\mu(d)}d
=O_\varepsilon(x^{\beta-1+\varepsilon}),
\]

using the convergence of `sum mu(d)/d` to zero.

For `j=1,2,3`, let

\[
f_{j,x}(t)=t^jB_{j+2}(\{x/t\}).
\]

The periodic Bernoulli functions in question are continuous at integers and
have bounded derivative on every open cell. Therefore

\[
|f_{j,x}(t)|\ll t^j,
\qquad
|f'_{j,x}(t)|\ll t^{j-1}+x t^{j-2}
\tag{L-9508.14}
\]

away from finitely many cell boundaries; the function itself is continuous
there, so piecewise partial summation introduces no jump term. Hence

\[
\sum_{d<x}\mu(d)f_{j,x}(d)
=O_\varepsilon(x^{\beta+j+\varepsilon}).
\tag{L-9508.15}
\]

Multiplication by `x^(-j-2)` gives (L-9508.13) for all three Bernoulli channels.

## Significance

At `beta=1/2`, every term in the exact finite arithmetic decomposition has the
same critical exponent `x^(-3/2+epsilon)`. There is no hidden larger boundary,
archimedean, or rounding channel.

Thus the quartic kernel packages the full Mertens/RH exponent into one finite
totient sum while retaining a proof-facing decomposition into bounded periodic
weights.

## Gap audit

- The decomposition is exact and finite, but it does not prove the Mertens bound.
- The convergence `sum mu(d)/d=0` uses the prime number theorem; under
  (L-9508.12) it is automatic.
- Bernoulli periodicity at integer cell boundaries is load-bearing for the
  no-jump partial-summation argument.
- An ordinary finite scan of `E_2(x)` cannot prove the uniform exponent.

## Independent-review targets

1. Re-expand the finite power sums and verify all coefficients in (L-9508.5).
2. Check the strict-cutoff convention at integer `y`.
3. Reconstruct every power of `x` and `d` in (L-9508.10).
4. Audit the piecewise partial-summation bound (L-9508.14)--(L-9508.15).
