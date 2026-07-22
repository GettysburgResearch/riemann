# L-2502 — Size-aware abundancy ceiling for a bounded canonical subtree

Claim ID: L-2502  
Title: Size-aware exact abundancy ceiling for a bounded canonical subtree  
Status: PROPOSED  
Authoring agent: `gpt56-03-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-2501 notation; elementary divisor-sum formula  
Scope: rigorous pruning within one finite integer bound  
Related counterexample candidates: Robin witnesses

## Statement

Fix \(B\ge3\), a support size \(K\), and a nonempty reachable canonical prefix

\[
a_1\ge\cdots\ge a_j\ge1,
\qquad 1\le j<K.
\]

Write

\[
P=\prod_{r=1}^{j}p_r^{a_r},
\qquad
I_P=\prod_{r=1}^{j}\frac{\sigma(p_r^{a_r})}{p_r^{a_r}},
\qquad
A=a_j,
\]

and

\[
R=\prod_{r=j+1}^{K}p_r.
\]

For every remaining index \(i>j\), define

\[
m_i=
\min\left(
A,
\max\left\{e\ge1:
Pp_i^e\frac{R}{p_i}\le B
\right\}
\right).
\]

Then every canonical completion

\[
n=P\prod_{i=j+1}^{K}p_i^{b_i}\le B,
\qquad
A\ge b_{j+1}\ge\cdots\ge b_K\ge1,
\]

satisfies \(b_i\le m_i\) and

\[
\frac{\sigma(n)}n\le
U_B:=I_P\prod_{i=j+1}^{K}
\frac{\sigma(p_i^{m_i})}{p_i^{m_i}}.
\]

Let

\[
N_{\min}=PR.
\]

If \(N_{\min}\ge3\) and a rigorous lower bound \(L_{\min}\) satisfies

\[
U_B<L_{\min}
\le e^\gamma\log\log N_{\min},
\]

then every completion in the bounded subtree satisfies Robin's strict
inequality.

## Definitions

The abundancy function is

\[
I(n)=\frac{\sigma(n)}n.
\]

For a prime power,

\[
I(p^a)=1+\frac1p+\cdots+\frac1{p^a}
      =\frac{p^{a+1}-1}{p^a(p-1)}.
\]

## Motivation

The earlier fixed-support ceiling replaced every unknown prime-power factor by
\(p/(p-1)\), and a first prototype capped every tail exponent only by \(A\).
The present bound also uses the finite global size budget. Each tail prime gets
an independently proved cap, which is stronger while remaining exact and easy
to replay.

## Proof

Fix a completion. Since every other tail prime occurs to exponent at least one,

\[
Pp_i^{b_i}\frac{R}{p_i}
\le P\prod_{r=j+1}^{K}p_r^{b_r}=n\le B.
\]

Thus \(b_i\) does not exceed the largest exponent admitted by the size
inequality. Canonical monotonicity also gives \(b_i\le A\). Hence
\(b_i\le m_i\).

For fixed prime \(p\), the sequence

\[
I(p^a)=1+p^{-1}+\cdots+p^{-a}
\]

is strictly increasing in \(a\). Therefore

\[
I(p_i^{b_i})\le I(p_i^{m_i})
\]

for every tail prime. Multiplicativity of \(\sigma(n)/n\) over distinct prime
powers gives

\[
I(n)=I_P\prod_{i=j+1}^{K}I(p_i^{b_i})
\le I_P\prod_{i=j+1}^{K}I(p_i^{m_i})=U_B.
\]

Every completion also satisfies \(n\ge N_{\min}\). The function
\(e^\gamma\log\log x\) is strictly increasing for \(x>1\). Consequently,

\[
I(n)\le U_B<L_{\min}
\le e^\gamma\log\log N_{\min}
\le e^\gamma\log\log n.
\]

This is Robin's strict inequality for every completion. ∎

## Analytic domain audit

Only real natural logarithms at integers at least three occur. The derivative
of \(\log\log x\) is \(1/(x\log x)>0\) for \(x>1\). No complex branches,
zeros, poles, or contour arguments occur.

## Dependency audit

- L-2501 supplies reachable-prefix and finite-tree notation.
- The prime-power divisor-sum formula and monotonicity are proved inline.
- A numerical implementation must separately prove the lower enclosure
  \(L_{\min}\).

## Gap audit

- The individual maxima \(m_i\) need not be jointly attainable. That makes the
  product a possibly loose upper bound, never an unsafe lower bound.
- The bound depends on the stated finite \(B\); it is not a universal subtree
  theorem as \(B\to\infty\).
- A rounded logarithm or ordinary floating comparison cannot certify the strict
  prune.
- The prefix must be nonempty; X-2501 does not license root pruning with this
  lemma.

## Adversarial tests

- Exhaust every completion for small support and verify its abundancy is at most
  \(U_B\).
- Mutate one cap downward and require the verifier to reject the prune.
- Test prefixes whose strict margin is much smaller than interval width.
- Use deliberately weak dyadic parameters and require failure closed.

## Remaining uncertainty

No known proof gap. The practical tightness of the product of independent caps
is the main limitation.

## Suggested next attack

Optimize tail exponent increments under their shared product budget rather than
multiplying independently attainable maxima.
