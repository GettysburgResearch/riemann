# L-0322 — Nicolas primorial recurrence

Claim ID: L-0322  
Title: Exact recurrence and transformed form of the Nicolas inequality  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: L-0320  
Scope: arithmetic kernel for Issue #15  
Related counterexample candidates: Nicolas primorial witnesses

## Statement

Let `p_k` be the `k`-th prime and
\[
 N_k=\prod_{j=1}^k p_j,\qquad
 \vartheta(x)=\sum_{p\le x}\log p.
\]
Then
\[
 \frac{N_k}{\varphi(N_k)}
 =\prod_{j=1}^k\frac{p_j}{p_j-1},
 \qquad
 \log N_k=\vartheta(p_k),
 \qquad
 \log\log N_k=\log\vartheta(p_k).
\]
Writing
\[
 A_k=\frac{N_k}{\varphi(N_k)},\qquad \Theta_k=\vartheta(p_k),
\]
we have exact recurrences
\[
 A_{k+1}=A_k\frac{p_{k+1}}{p_{k+1}-1},
 \qquad
 \Theta_{k+1}=\Theta_k+\log p_{k+1}.
\]

Under the imported Nicolas criterion T-0304, any `k>=2` for which a rigorous
enclosure proves
\[
 A_k\le e^\gamma\log\Theta_k
\]
is a finite disproof of RH.

## Proof

The primorial is squarefree, so L-0320 gives
\[
 \frac{N_k}{\varphi(N_k)}
 =\prod_{p\mid N_k}\frac p{p-1}
 =\prod_{j=1}^k\frac{p_j}{p_j-1}.
\]
Taking the real logarithm of the positive product defining `N_k`,
\[
 \log N_k=\sum_{j=1}^k\log p_j=\vartheta(p_k).
\]
Since `N_k>1`, taking one more logarithm gives the third identity.

Appending the next prime multiplies `A_k` by
`p_{k+1}/(p_{k+1}-1)` and adds `log p_{k+1}` to `Theta_k`, proving the
recurrences.  The final implication is exactly the contrapositive of T-0304.
∎

## Motivation

The recurrence permits a streamed one-dimensional search without constructing
the enormous integer `N_k`.  The rational product can be accumulated exactly
in blocks or enclosed by directed rounding.

## Analytic domain audit

All logarithms are real and applied to positive quantities.  `Theta_k>1` for
`k>=2`, so `log Theta_k` is defined and positive in the theorem's domain.

## Dependency audit

L-0320 proves the totient product.  T-0304 supplies the RH equivalence; this
lemma does not prove Nicolas's theorem.

## Gap audit

- A segmented sieve must prove that every prime is present exactly once.
- Storing `log A_k` instead of `A_k` requires directed-rounding error control.
- The strict direction in T-0304 matters: equality is a violation.
- The recurrence alone gives no bound on how far a first violation may lie.

## Adversarial tests

Recompute `k=2,3,4` by explicit primorials and compare exact rational products.
Restart from checkpoints and verify bitwise-equivalent certificate data.

## Remaining uncertainty

The exact original Nicolas theorem wording was checked through later primary
restatements; an independent reviewer should inspect the 1983 full text.

## Suggested next attack

Implement Issue #15 with certified segmented primes, dual exact/log
accumulation, and a compact checkpoint-plus-block certificate.
