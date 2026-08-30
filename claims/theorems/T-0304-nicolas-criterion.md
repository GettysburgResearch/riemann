# T-0304 — Nicolas primorial criterion

Claim ID: T-0304  
Title: Nicolas's primorial Euler-totient criterion for RH  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: external theorem of Nicolas (1983)  
Scope: imported equivalence; finite one-index witness  
Related counterexample candidates: Issue #15

## Statement

Let `p_k` be the `k`-th prime and `N_k=prod_{j=1}^k p_j`.  Then RH is
equivalent to
\[
 \frac{N_k}{\varphi(N_k)}
 >
 e^\gamma\log\log N_k
 \qquad\text{for every }k\ge2.
\]

Moreover, Nicolas's result records that if RH is false, the inequality holds
for infinitely many `k` and fails for infinitely many `k`.

Hence one rigorously certified `k>=2` satisfying
\[
 \frac{N_k}{\varphi(N_k)}
 \le e^\gamma\log\log N_k
\]
is a finite disproof of RH.

## Source

Jean-Louis Nicolas, *Petites valeurs de la fonction d'Euler*, Journal of
Number Theory 17 (1983), 375--388,
DOI 10.1016/0022-314X(83)90055-0.

Inspection note: publisher metadata was located.  The exact inequality and
oscillation statement were checked in later primary treatments that explicitly
cite Nicolas.  The original full paper was not inspected in this session.

## Motivation

Unlike Robin, candidates are indexed only by `k`, and L-0322 gives an exact
streaming recurrence.  It is therefore attractive for a massively parallel
certified search.

## Proof status

Imported theorem; proof not reproduced.

## Analytic/domain audit

- The domain begins at `k=2`.
- Natural logarithms are used.
- `log log N_k=log theta(p_k)` by L-0322.
- Strict inequality matters; equality is a failure.

## Dependency audit

L-0322 supplies arithmetic identities only.  The RH equivalence remains the
external Nicolas theorem.

## Gap audit

- A prime-generation omission changes both sides.
- Approximate Mertens products do not certify the exact ratio.
- The oscillation statement under `not RH` is asymptotic and gives no practical
  upper bound for the first failure.
- Secondary variants may use a prime variable rather than `k`; translate
  carefully.

## Remaining uncertainty

Independent review should inspect the original French paper and identify the
exact theorem number and endpoint wording before promotion.

## Suggested next attack

Claim Issue #15 and build a segmented, checkpointed prime stream with exact or
outward-rounded products and independent primality verification.
