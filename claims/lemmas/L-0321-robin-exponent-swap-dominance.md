# L-0321 — Robin exponent-swap dominance

Claim ID: L-0321  
Title: Inverted prime exponents are dominated in the Robin quotient  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: L-0320  
Scope: safe local pruning rule for exponent-vector searches  
Related counterexample candidates: Robin inequality witnesses

## Statement

Let `p<q` be primes, let `0<=a<b` be integers, and let `m` be a positive integer
coprime to `pq`.  Define
\[
 n=m p^a q^b,\qquad n'=m p^b q^a.
\]
Then
\[
 n'<n
 \quad\text{and}\quad
 \frac{\sigma(n')}{n'}>\frac{\sigma(n)}{n}.
\]

If additionally `e<n'<n`, then the Robin quotient
\[
 R(x)=\frac{\sigma(x)}{x\log\log x}
\]
satisfies
\[
 R(n')>R(n).
\]

Consequently a maximizer of `R(n)` within any fixed set of prime divisors and
multiset of exponents, all lying above `e`, can be chosen with exponents
nonincreasing as primes increase.

## Proof

Because `b-a>0` and `p/q<1`,
\[
 \frac{n'}{n}=\left(\frac pq\right)^{b-a}<1.
\]

For `r>=0`, let
\[
 F_r(x)=1+x+\cdots+x^r.
\]
By L-0320, factors from `m` cancel, and the desired divisor-ratio inequality is
equivalent to
\[
 F_b(1/p)F_a(1/q)>F_a(1/p)F_b(1/q),
\]
or
\[
 \frac{F_b(1/p)}{F_a(1/p)}
 >
 \frac{F_b(1/q)}{F_a(1/q)}.
\]
It is enough to prove
\[
 G(x):=\frac{F_b(x)}{F_a(x)}
\]
is strictly increasing for `x>0`.

Differentiate.  Since `F_a(x)>0`,
\[
 G'(x)F_a(x)^2=F_b'(x)F_a(x)-F_b(x)F_a'(x)
 =\sum_{i=0}^b\sum_{j=0}^a(i-j)x^{i+j-1},
\]
where terms with zero coefficient cause no issue at `x=0` and we only use
`x>0`.  In the sub-sum `0<=i,j<=a`, the `(i,j)` and `(j,i)` terms cancel.
What remains is
\[
 \sum_{i=a+1}^{b}\sum_{j=0}^{a}(i-j)x^{i+j-1},
\]
which is strictly positive because `i>j` and `x>0`.  Thus `G` is strictly
increasing.  Since `1/p>1/q`, the divisor-ratio inequality follows.

Finally, on `(e,infinity)`, `log log x` is positive and strictly increasing.
We have both
\[
 \frac{\sigma(n')}{n'}>\frac{\sigma(n)}n
\quad\text{and}\quad
 \log\log n'<\log\log n.
\]
Dividing the larger numerator by the smaller positive denominator gives
`R(n')>R(n)`.  ∎

## Motivation

Issue #2 searches monotone prime-exponent vectors.  This lemma supplies a
complete local proof for that pruning rule rather than relying on folklore.

## Analytic domain audit

Only real logarithms of numbers `>e` appear in the Robin quotient.  The first
two inequalities hold without that restriction.

## Dependency audit

L-0320 is used to factor `sigma(n)/n`.  The rest is finite algebra and
monotonicity.

## Gap audit

- The lemma permutes a fixed exponent multiset; it does not prove which primes
  or exponents a global first counterexample must use.
- If `n'<=e`, the Robin quotient statement is outside its monotone positive
  denominator argument.
- It does not establish the stronger colossally abundant reduction.
- Exponent zero is allowed to make the exchange argument useful when comparing
  supports, but `m` must remain coprime to `pq`.

## Adversarial tests

- `a=0,b=1`: compare placing a single prime factor at `p` versus `q`.
- `a=b`: strictness should disappear; this case is excluded.
- Verify exact rational ratios for small examples such as `(p,q)=(2,3)`.

## Remaining uncertainty

No known gap.  The exact role of this lemma in agent #2's broader pruning
should be reviewed separately.

## Suggested next attack

Prove and cite the precise extremal theorem that reduces a *minimal* Robin
counterexample to superabundant or colossally abundant candidates.
