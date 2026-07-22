# L-0320 — Divisor and totient product formulae

Claim ID: L-0320  
Title: Exact prime-factor product formulae for `sigma(n)/n` and `n/phi(n)`  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: unique factorization  
Scope: exact arithmetic kernels for Robin, Lagarias, and Nicolas searches  
Related counterexample candidates: arithmetic inequality witnesses

## Statement

Let
\[
 n=\prod_{j=1}^r p_j^{a_j},
\]
where the `p_j` are distinct primes and `a_j>=1`.  Then
\[
 \sigma(n)=\prod_{j=1}^r\frac{p_j^{a_j+1}-1}{p_j-1},
\]
\[
 \frac{\sigma(n)}{n}
 =\prod_{j=1}^r\left(1+\frac1{p_j}+\cdots+\frac1{p_j^{a_j}}\right)
 =\prod_{j=1}^r\frac{1-p_j^{-(a_j+1)}}{1-p_j^{-1}},
\]
and
\[
 \varphi(n)=n\prod_{j=1}^r\left(1-\frac1{p_j}\right),
 \qquad
 \frac{n}{\varphi(n)}=\prod_{j=1}^r\frac{p_j}{p_j-1}.
\]

All displayed quantities are exact rational/integer expressions determined by
the certified factorization of `n`.

## Proof

For a prime power, the divisors of `p^a` are
`1,p,...,p^a`, so
\[
 \sigma(p^a)=1+p+\cdots+p^a=\frac{p^{a+1}-1}{p-1}.
\]
If `gcd(x,y)=1`, every divisor of `xy` is uniquely a product of a divisor of
`x` and a divisor of `y`; hence `sigma` is multiplicative.  Applying this to
the prime-power factorization proves the formula for `sigma(n)`.  Dividing by
`n=prod p_j^{a_j}` gives the two ratio forms.

For `p^a`, exactly `p^{a-1}` of the residues modulo `p^a` are divisible by
`p`, so
\[
 \varphi(p^a)=p^a-p^{a-1}=p^a(1-1/p).
\]
Euler's totient is multiplicative on coprime arguments by the Chinese
remainder theorem.  Multiplication over prime powers gives the stated formula,
and division yields `n/phi(n)`.  ∎

## Motivation

The arithmetic side of a finite witness should be exact.  These identities
isolate all transcendental uncertainty into Euler's constant and logarithms.

## Analytic domain audit

None.  All objects are finite integers or rationals.

## Dependency audit

Unique factorization, geometric sums, multiplicativity of `sigma`, and the
Chinese remainder theorem.

## Gap audit

- A claimed factorization must itself be certified.
- Floating products are not exact evaluations of the displayed rationals.
- The `n/phi(n)` ratio ignores exponents only after every prime divisor is
  known.
- An omitted large prime factor invalidates both formulas.

## Adversarial tests

Check prime powers, a squarefree integer, `n=1` (empty product), and a product
of two coprime prime powers.

## Remaining uncertainty

None beyond independent review.

## Suggested next attack

Use exact numerator/denominator cancellation or prime-exponent maps so large
searches can emit compact factorization-based certificates.
