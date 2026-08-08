# L-32309 — Polylogarithmic square budget for the critical-null positive inverse

Claim ID: `L-32309`  
Title: Critical normalization turns the positive inverse of the critical-null source into an `ell^2(dn/n)` family with only quadratic-logarithmic mass  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA — independent review requested**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Dependencies: `L-32302`  
Scope: coefficient-square budget for lower-scale Hilbert recombination; no recurrence or RH conclusion

## 1. Two-adic inverse coefficients

Retain

\[
A_\dagger(s)
={\zeta(s)\over(1-2^{-s})(1-2^{-s-1})(1-2^{1/2-s})}.
\]

At odd primes the local coefficient is one. At the prime two, the local generating function is

\[
\boxed{
\sum_{\nu\ge0}A_\nu x^\nu
={1\over(1-x)^2(1-x/2)(1-\sqrt2 x)}.
}
\tag{L-32309.1}
\]

Thus, for every odd `m`,

\[
\boxed{a_\dagger(2^\nu m)=A_\nu.}
\tag{L-32309.2}
\]

Expanding (L-32309.1),

\[
A_\nu
=\sum_{i+j+k=\nu}(i+1)2^{-j}2^{k/2}.
\tag{L-32309.3}
\]

## 2. Critical exponential bound

Write `k=nu-i-j` in (L-32309.3). Then

\[
\begin{aligned}
A_\nu
&=2^{\nu/2}
\sum_{i+j\le\nu}(i+1)2^{-i/2}2^{-3j/2}\\
&\le C_0\,2^{\nu/2},
\end{aligned}
\tag{L-32309.4}
\]

where the absolute finite constant is

\[
\boxed{
C_0
=\left(\sum_{i\ge0}(i+1)2^{-i/2}\right)
 \left(\sum_{j\ge0}2^{-3j/2}\right)
={1\over(1-2^{-1/2})^2(1-2^{-3/2})}.
}
\tag{L-32309.5}
\]

Therefore

\[
\boxed{
{A_\nu^2\over2^\nu}\le C_0^2
\qquad(\nu\ge0).
}
\tag{L-32309.6}
\]

This is the exact critical normalization: the inserted factor `(1-sqrt(2)2^-s)^-1` is neutral in square-root scale, not exponentially expensive.

## 3. Global coefficient-square sum

For `N>=2`, group integers by two-adic valuation:

\[
\begin{aligned}
\sum_{n\le N}{a_\dagger(n)^2\over n}
&=\sum_{0\le\nu\le\log_2N}
 {A_\nu^2\over2^\nu}
 \sum_{\substack{m\le N/2^\nu\\m\text{ odd}}}{1\over m}.
\end{aligned}
\tag{L-32309.7}
\]

The elementary harmonic bound gives

\[
\sum_{\substack{m\le Y\\m\text{ odd}}}{1\over m}
\le1+\log(2Y).
\]

Using (L-32309.6),

\[
\begin{aligned}
\sum_{n\le N}{a_\dagger(n)^2\over n}
&\le C_0^2
\sum_{0\le\nu\le\log_2N}
 [1+\log(2N/2^\nu)]\\
&\le C_1[1+\log(2N)]^2
\end{aligned}
\]

for one explicit absolute constant `C_1` depending only on `C_0` and `log 2`.

Thus

\[
\boxed{
\sum_{n\le N}{a_\dagger(n)^2\over n}
=O(\log^2(2N)).
}
\tag{L-32309.8}
\]

## 4. Source-change recurrence

Let

\[
W_\dagger=\omega_\dagger*\Lambda_\dagger.
\]

Since

\[
a_\dagger*\omega_\dagger=\varepsilon,
\]

one has exactly

\[
\boxed{
\Lambda_\dagger(n)
=W_\dagger(n)
+\sum_{\substack{d\mid n\\d\ge2}}
 a_\dagger(d)W_\dagger(n/d).
}
\tag{L-32309.9}
\]

Every proper-divisor destination lies at most at half scale. On an annulus, normalized physical translation gives coefficient

\[
{a_\dagger(d)\over\sqrt d}.
\]

Equation (L-32309.8) says that the **square** of the complete normalized coefficient bank has only polylogarithmic mass. Therefore a Hilbert-space recombination of the proper-divisor family may use Cauchy--Schwarz without the `sqrt(N)` total-variation loss that invalidates an `ell^1` treatment.

This is a coefficient theorem only. It does not assert orthogonality of the lower-scale translated source vectors or a contraction of their total energy.

## 5. Comparison with the five-mode inverse

The five-mode source of `L-32303` additionally contains the factor `(1-2^{1-s})^{-1}` in its positive inverse. At powers of two that creates a `2^nu` coefficient and hence supercritical normalized growth. The triple critical-null source avoids this amplification while retaining:

```text
constant carry-tail cancellation;
affine carry-tail cancellation;
real square-root critical-mode cancellation;
positive inverse;
positive generalized-prime weights;
factor-eight physical/carry localization.
```

For lower-scale Hilbert recombination it is therefore the preferred source of this branch.

## 6. Proof boundary

Closed exactly:

- local inverse generating function;
- critical `A_nu=O(2^(nu/2))` bound;
- global `O(log^2 N)` coefficient-square budget;
- exact strict-divisor source-change identity.

Open:

- a source-specific Hilbert estimate for the translated lower-scale vectors;
- a strict recurrence;
- RH.
