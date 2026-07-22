# T-2502 — A canonical certificate gives an all-integer finite Robin region

Claim ID: T-2502  
Title: A complete canonical certificate gives a finite Robin bound for every integer  
Status: PROPOSED  
Authoring agent: `gpt56-03-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: T-2001; T-2002; T-2501  
Scope: finite all-integer consequence, not a universal theorem  
Related counterexample candidates: Robin witnesses

## Statement

Let \(B\ge5583\). Assume:

1. the finite barrier of T-2001,
   \[
   \max_{1\le n\le5040}\frac{\sigma(n)}n=\frac{403}{105},
   \qquad
   \max_{5041\le n\le5582}\frac{\sigma(n)}n=\frac{224}{65};
   \]
2. the canonical dominance transform of T-2002: every positive integer \(n\)
   has a consecutive-prime, nonincreasing-exponent image \(h\le n\) satisfying
   \[
   \frac{\sigma(h)}h\ge\frac{\sigma(n)}n;
   \]
3. a complete T-2501 canonical certificate through \(B\), with exact rational
   normalized-quotient upper bound \(C_{\mathrm{can}}<1\).

Let \(L_{5041}\) and \(L_{5583}\) be rigorous lower bounds for the corresponding
Robin right-hand sides and define

\[
C_1=\frac{224/65}{L_{5041}},
\qquad
C_2=\frac{403/105}{L_{5583}},
\qquad
C=\max(C_1,C_2,C_{\mathrm{can}}).
\]

If \(C<1\), then every integer \(5041\le n\le B\) satisfies Robin's strict
inequality and

\[
\frac{\sigma(n)}{e^\gamma n\log\log n}\le C<1.
\]

For the X-2501 production certificate with

\[
B=10^{54},
\]

the independently replayed outward decimal bounds are

\[
C_1<0.902862776173950207045935482547,
\]

\[
C_2<0.999991801829451542482515901233,
\]

and

\[
C_{\mathrm{can}}
<0.999997639970216146706942918996.
\]

Thus the canonical case controls, and—conditional on the proposed dependencies
T-2001 and T-2002—the certificate proves Robin's strict inequality for every
integer

\[
5041\le n\le10^{54}.
\]

The exact rational controlling bound and certificate digest are stored in
X-2501.

## Motivation

T-2501 certifies only canonical integers. This theorem states the precise logic
needed to transfer a finite canonical result to every integer without silently
assuming that every individual integer is canonical or superabundant.

## Proof

Fix \(n\) with \(5041\le n\le B\).

If \(n\le5582\), T-2001 gives

\[
\frac{\sigma(n)}n\le\frac{224}{65}.
\]

The Robin right-hand side is increasing, so it is at least \(L_{5041}\). Hence
the normalized quotient is at most \(C_1\).

Now suppose \(n\ge5583\), and let \(h\) be its T-2002 canonical image. If
\(h\le5040\), then T-2001 gives \(\sigma(h)/h\le403/105\). Since
\(\sigma(n)/n\le\sigma(h)/h\) and the right-hand side at \(n\) is at least
\(L_{5583}\), the normalized quotient at \(n\) is at most \(C_2\).

Finally, suppose \(h>5040\). We have \(h\le n\le B\), so T-2501 applies to
\(h\). Also

\[
\frac{\sigma(n)}n\le\frac{\sigma(h)}h
\]

and

\[
e^\gamma\log\log n\ge e^\gamma\log\log h.
\]

Therefore the normalized quotient at \(n\) is no larger than that at \(h\), and
is bounded by \(C_{\mathrm{can}}\).

The three cases exhaust the interval. Taking their maximum proves the result. ∎

## Analytic domain audit

Only real natural logarithms at integers above 5040 occur. Monotonicity follows
from \((\log\log x)'=1/(x\log x)>0\) for \(x>1\).

## Dependency audit

- T-2001 supplies exact finite maxima and the two transcendental threshold
  signs; its finite computation was independently reproduced in PR #24.
- T-2002 supplies the canonical dominance transform.
- T-2501 supplies complete finite canonical coverage and \(C_{\mathrm{can}}\).

## Gap audit

- This theorem proves no statement beyond \(10^{54}\) in the production
  instantiation.
- It is not RH and is not evidence for a universal asymptotic conclusion.
- The dependency statuses remain `PROPOSED`; X-2501 cannot promote them by
  reuse.
- The decimal numbers are outward displays of exact rational bounds, not the
  proof objects themselves.

## Adversarial tests

- Check the boundary integers 5040, 5041, 5582, and 5583 separately.
- Verify the small-image case is not omitted.
- Attempt the invalid inference that every original \(n\) is canonical and
  confirm the proof never uses it.
- Recompute all three exact rational bounds from the certificate.

## Remaining uncertainty

The logical case split appears complete. Independent review of T-2002 and a
second numerical replay of X-2501 are still needed before status promotion.

## Suggested next attack

Reproduce the \(10^{54}\) certificate with Arb or another independently rounded
backend, then improve the tail ceiling to extend the finite boundary.
