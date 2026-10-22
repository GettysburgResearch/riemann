# L-3107 — Additive Nicolas margin and block certificates

Claim ID: L-3107  
Title: The Nicolas primorial inequality admits a restartable additive margin recurrence with prefix-safe interval tests  
Status: PROPOSED  
Authoring agent: `gpt56-05`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-0322 and imported Nicolas criterion T-0304  
Scope: streamed, restartable, directed-interval Nicolas searches  
Related counterexample candidates: Nicolas primorial witnesses

## Statement

Use the notation of L-0322,

\[
 A_k=\prod_{j=1}^k\frac{p_j}{p_j-1},
 \qquad
 \Theta_k=\sum_{j=1}^k\log p_j.
\]

For `k>=2`, define the logarithmic Nicolas margin

\[
 M_k=\log A_k-\gamma-\log(\log\Theta_k).
\]

Since `Theta_k>1`, all displayed logarithms are real. The Nicolas inequality

\[
 A_k>e^\gamma\log\Theta_k
\]

is equivalent to `M_k>0`, while a finite Nicolas violation is equivalent to
`M_k<=0`.

The margin has the exact additive recurrence

\[
 M_{k+1}=M_k+\alpha_{k+1}-\beta_{k+1},
\]

where

\[
 \alpha_{k+1}=\log\frac{p_{k+1}}{p_{k+1}-1},
\]

and

\[
 \beta_{k+1}
 =\log\!\left(
 \frac{\log(\Theta_k+\log p_{k+1})}{\log\Theta_k}
 \right).
\]

Therefore a restartable block certificate needs only a rigorous interval for
`(Theta_r,M_r)`, the exact consecutive prime list in the block, and outward
interval evaluations of the increments.

More precisely, suppose

\[
 M_r\in[M_r^-,M_r^+]
\]

and, for `j=r+1,...,s`,

\[
 \alpha_j-\beta_j\in[\ell_j,u_j].
\]

Then every block prefix satisfies

\[
 M_t\in
 \left[M_r^-+\sum_{j=r+1}^{t}\ell_j,
       M_r^++\sum_{j=r+1}^{t}u_j\right]
 \qquad(r<t\le s).
\]

Hence:

1. if every lower prefix endpoint is strictly positive, the whole block is
   certified free of Nicolas violations;
2. if any upper prefix endpoint is nonpositive, that index is a certified
   Nicolas violation, conditional only on T-0304;
3. otherwise the block is unresolved and must be recomputed more sharply rather
   than assigned a sign.

## Motivation

L-0322 gives multiplicative/product recurrences. For very large primorial
indices, restartability and proof-producing block exclusion are easier in an
additive margin. This lemma isolates the exact increment and supplies a minimal
checkpoint protocol whose safety does not depend on reconstructing the gigantic
primorial integer or exact rational product at every step.

## Proof

For `k>=2`, `Theta_k>=log 6>1`, so `log Theta_k>0` and every logarithm in `M_k`
is defined. Because the real logarithm is strictly increasing,

\[
 A_k>e^\gamma\log\Theta_k
\]

is equivalent to

\[
 \log A_k>\gamma+\log(\log\Theta_k),
\]

which is `M_k>0`. Equality belongs to the violating side because Nicolas's
criterion is strict.

Using L-0322,

\[
 \log A_{k+1}-\log A_k
 =\log\frac{p_{k+1}}{p_{k+1}-1}=\alpha_{k+1},
\]

and

\[
 \begin{aligned}
 &\log(\log\Theta_{k+1})-\log(\log\Theta_k)\\
 &\qquad=
 \log\!\left(
 \frac{\log(\Theta_k+\log p_{k+1})}{\log\Theta_k}
 \right)=\beta_{k+1}.
 \end{aligned}
\]

Subtracting proves the recurrence.

Interval addition is inclusion-monotone. Starting from the checkpoint interval
and adding each increment interval inductively gives the prefix enclosure. The
three certification outcomes follow directly from whether the resulting
interval lies strictly above zero, at or below zero, or overlaps zero. ∎

## Analytic domain audit

All logarithms are real. The restriction `k>=2` guarantees `Theta_k>1` and
`log Theta_k>0`. Prime inputs are positive integers. No complex branches occur.

## Dependency audit

L-0322 supplies the exact recurrences for `A_k` and `Theta_k`. T-0304 is needed
only for the final implication from `M_k<=0` to falsity of RH; this lemma does
not reconstruct Nicolas's theorem.

## Gap audit

- The prime list must be certified consecutive and complete; a skipped prime
  invalidates both recurrences.
- Checkpoint intervals must enclose the exact `Theta_r` and `M_r`, not merely a
  floating restart state.
- Directed lower and upper evaluations must preserve the nested logarithm
  directions.
- A lower endpoint equal to zero does not certify the strict Nicolas inequality.
- Additive accumulation can widen over long blocks; unresolved blocks require
  shorter checkpoints or higher precision.

## Adversarial tests

1. Recompute `k=2,3,4` from explicit primorials and compare the margin recurrence.
2. Restart halfway through a small prime list and verify containment of the
   one-shot interval.
3. Widen one increment until a prefix interval touches zero; the block must
   become unresolved.
4. Delete one prime from a synthetic block and verify that a sequence digest or
   consecutive-prime checker rejects the certificate.

## Remaining uncertainty

No mathematical gap is known. The practical interval width and optimal block
size remain to be measured.

## Suggested next attack

Build Issue #15 around hash-chained checkpoints containing exact prime-range
metadata plus dyadic intervals for `Theta` and `M`. Use cheap wide blocks far
from zero and automatic precision escalation only where a prefix interval
approaches zero.
