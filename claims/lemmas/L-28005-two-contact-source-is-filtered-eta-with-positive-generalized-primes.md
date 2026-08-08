# L-28005 — The dyadic two-contact source is a finite eta filter with positive generalized primes

Claim ID: `L-28005`  
Title: A boundary-safe finite dyadic filter converts the reciprocal-eta cascade into the exact two-contact carry source and a positive generalized-prime Dirichlet system  
Status: **PROPOSED EXACT CROSS-ROUTE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #280  
Dependencies: `L-28001`; PR #269 `L-26201`; generalized reflected Selberg identity  
Scope: exact Dirichlet/carry algebra; no physical transference estimate

## 1. Finite filter of the eta inverse

Let `b_eta` denote the coefficient sequence of `1/eta(s)` and put

\[
 \boxed{
 b_2=(\varepsilon-\delta_2)*\mu.
 }
\tag{L-28005.1}

Its Dirichlet series is

\[
 B_2(s)={1-2^{-s}\over\zeta(s)}.
\tag{L-28005.2}

Since

\[
 {1\over\eta(s)}
 ={1\over(1-2^{1-s})\zeta(s)},
\]

one has the exact finite-filter relation

\[
 \boxed{
 b_2
 =(\varepsilon-3\delta_2+2\delta_4)*b_\eta,
 }
\tag{L-28005.3}

because

\[
 (1-2^{-s})(1-2^{1-s})
 =1-3\,2^{-s}+2\,4^{-s}.
\tag{L-28005.4}

The multiplier in (L-28005.4) has zeros only on `Re(s)=0` and `Re(s)=1`.
It therefore does not cancel a zeta zero in the open critical strip.

## 2. Positive inverse Dirichlet system

The convolution inverse of `b_2` has Dirichlet series

\[
 \boxed{
 A_2(s)={\zeta(s)\over1-2^{-s}}.
 }
\tag{L-28005.5}

Its coefficients are

\[
 \boxed{
 a_2(n)=v_2(n)+1>0.
 }
\tag{L-28005.6}

Indeed, `1/(1-2^-s)` has unit coefficient on every power of two, and
convolution with the constant-one sequence counts the dyadic divisors of `n`.

Define

\[
 -{A_2'\over A_2}(s)
 =\sum_{n\ge1}\Lambda_2(n)n^{-s}.
\]

Then

\[
 \boxed{
 \Lambda_2(n)
 =\Lambda(n)+(\log2)\mathbf1_{n=2^r,\ r\ge1}
 \ge0.
 }
\tag{L-28005.7}

Thus

\[
 \Lambda_2(2^r)=2\log2,
\]

while every other prime power retains its ordinary von Mangoldt weight.

The exact Selberg coefficient identity is

\[
 \boxed{
 b_2*(a_2\log^2)
 =\Lambda_2\log+\Lambda_2*\Lambda_2.
 }
\tag{L-28005.8}

Every coefficient on the generalized-prime side is nonnegative.

## 3. Exact two-contact carry image

Since

\[
 \mathbf1*b_2=\varepsilon-\delta_2,
\]

one has, for integers `x>=0`,

\[
 \sum_{q\le x}b_2(q)\left\lfloor{x\over q}\right\rfloor
 =\mathbf1_{x=1}.
\tag{L-28005.9}

Consequently every atomized carry row satisfies

\[
 \boxed{
 \sum_{q=2}^{n}b_2(q)\chi_{n,q}(j)
 =-\mathbf1_{j=1}-\mathbf1_{j=n-1}.
 }
\tag{L-28005.10}

This is the exact two-contact theorem of PR #269, now derived as a finite
boundary-safe filter of the complete eta cascade.

The average row is

\[
 \boxed{
 \sum_{q=2}^{n}b_2(q)\beta_{nq}
 =-{2\over n+1}.
 }
\tag{L-28005.11}

## 4. Reflected Hermitian identity in the same system

Apply the generalized reflected Selberg identity to

\[
 A_2(s+it),
 \qquad A_2(s-iu),
 \qquad A_2(s+it)A_2(s-iu).
\]

The exact subtraction gives

\[
 \boxed{
 C_2(\sigma;t,-u)-C_2(\sigma;t)-C_2(\sigma;-u)
 =2L_2(\sigma+it)L_2(\sigma-iu),
 }
\tag{L-28005.12}

where

\[
 L_2=-A_2'/A_2.
\]

On the diagonal,

\[
 \boxed{
 C_2(\sigma;t,-t)-C_2(\sigma;t)-C_2(\sigma;-t)
 =2|L_2(\sigma+it)|^2.
 }
\tag{L-28005.13}

The same Dirichlet system therefore supplies simultaneously:

1. positive inverse coefficients `a_2`;
2. nonnegative generalized primes `Lambda_2`;
3. an exact reflected Hermitian square;
4. an inverse source `b_2` with a literal two-contact carry image.

## 5. Pole preservation

One has

\[
 {A_2'\over A_2}(s)
 ={\zeta'\over\zeta}(s)
 -{(\log2)2^{-s}\over1-2^{-s}}.
\tag{L-28005.14}

The correction has poles only on `Re(s)=0`.  Hence every zeta zero in the open
critical strip remains an uncancelled pole of the generalized logarithmic
derivative.

A critical reflected estimate for this system would therefore imply RH; the
finite dyadic filter has not weakened the zero obstruction.

## 6. New transference target

PR #269 proves the two-contact carry identity, factor-five localization, and a
strict carry-space Schur reserve, but leaves a physical-normal-to-carry map
open.  Equations (L-28005.8)--(L-28005.13) supply the exact physical Dirichlet
system whose inverse is that same carry source.

The remaining map is no longer a comparison between unrelated models.  It is
the source-bound localization of one reflected Selberg identity for `A_2`.
A valid production theorem must retain all independent-frequency translate
cross terms and the quotient cells `2,3,4` identified in PR #269.

## 7. Proof boundary

Closed exactly:

- the finite filter from reciprocal eta to `b_2`;
- preservation of open-strip poles;
- positivity of the inverse coefficients;
- nonnegativity of all generalized-prime coefficients;
- the Selberg identity;
- the pointwise two-contact carry collapse;
- the reflected Hermitian square.

Open:

- the complete localized physical-to-carry congruence;
- factor-five transition contraction in the physical metric;
- a subpower `b_2` Riesz/shell bound;
- RH.
