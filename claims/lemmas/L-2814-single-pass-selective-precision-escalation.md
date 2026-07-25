# L-2814 — One directed pass suffices; precision may be escalated shardwise

Claim ID: L-2814  
Title: Exact fixed-vector certification permits heterogeneous precision and selective shard reruns  
Status: PROPOSED  
Authoring agent: `gpt56-01-f`  
Created: 2026-07-25  
Dependencies: L-2804/T-2810 interval composition  
Scope: complete directed fixed-vector prime certificates  
Related counterexample candidates: any future D-0801 fixed-vector witness

## Statement

Let the exact complete fixed-vector prime value be a finite sum

\[
 P=\sum_{s=1}^{m}P_s.
\]

Suppose, for every shard `s`, one proof-producing calculation at any chosen
precision supplies a rational interval

\[
 P_s\in I_s=[\ell_s,u_s].
\]

Then

\[
 P\in I:=\sum_{s=1}^{m}I_s
\]

and this single collection of directed intervals is sufficient for the exact
L-2804/T-2810 final sign test.  A duplicate higher-precision pass is not a
logical requirement.

If a second valid calculation gives `P_s in J_s`, then

\[
 P_s\in I_s\cap J_s
\]

whenever the intersection is nonempty.  Replacing any subset of shard intervals
by such intersections preserves validity and can only narrow the complete
interval.  Consequently:

1. different shards may use different working precisions;
2. a first complete pass may be run at one precision;
3. if the final interval is strict, certification is complete;
4. if it meets zero, only selected wide or poorly conditioned shards need be
   rerun at higher precision;
5. an empty overlap is an adversarial failure signal, not a value to be merged.

## Center-radius form

Write

\[
 I_s=[c_s-r_s,c_s+r_s],\qquad r_s\ge0.
\]

Let the exact alpha contribution and nonprime correction together have a
certified enclosure

\[
 B=[c_0-r_0,c_0+r_0].
\]

For the convention `Q=B-P`, the full interval has center and radius

\[
 C=c_0-\sum_sc_s,
 \qquad
 R=r_0+\sum_sr_s.
\]

Thus

\[
 C+R<0
\]

certifies negativity, while

\[
 C-R>0
\]

certifies positivity.  A sufficient per-shard error allocation for a midpoint
moat `mu=|C|>r_0` is any set of rational budgets `epsilon_s` satisfying

\[
 r_s\le\epsilon_s,
 \qquad
 \sum_s\epsilon_s<\mu-r_0.
\]

This allocation may be nonuniform: shards with large phase or accumulation
width receive tighter precision targets, while already narrow shards need not
be repeated.

## Proof

Finite interval addition is inclusion monotone.  Since each exact `P_s` lies in
`I_s`, their sum lies in the Minkowski sum `I`.  No relation among the numerical
backends or their precisions is required.

If `P_s` lies in both `I_s` and `J_s`, it lies in their intersection.  Replacing
`I_s` by a nonempty subset containing `P_s` preserves containment.  Intersections
cannot enlarge endpoint width, so selective replacement narrows or preserves
the complete interval.

The center-radius formula follows from addition and subtraction of real
intervals.  The two strict sign conditions are exactly the statements that the
upper endpoint is negative or the lower endpoint is positive.  The budget
corollary follows from

\[
 R\le r_0+\sum_s\epsilon_s<|C|.
\]

## Production consequence for the active target

The PR #65 target has 50 fixed-vector ranges at

```text
c = 10^11
T = 94184072727073 / 20
K = 1024
```

and an ordinary midpoint leading moat of approximately `2.691e-4`.  This
midpoint is not proof input, but it indicates that a first 192-bit complete
directed pass should be attempted before duplicating all 50 ranges at 256 bits.
If its exact final interval is strict, the proof computation is finished at that
precision.  A 256-bit pass then serves independent reproduction.  If the first
interval is unresolved, the center-radius ledger identifies exactly which shard
radii must be reduced.

## Certificate requirements

A heterogeneous-precision merger must still enforce:

- exact contiguous coverage;
- exactly one higher-prime-power stream;
- common vector, parameter, and normalization fingerprints;
- exact term-count identities;
- valid outward intervals from every producer;
- nonempty intersection before combining duplicate calculations;
- strict final endpoint comparison after alpha and correction composition.

The working precision is evidence metadata, not a mathematical compatibility
constraint.

## Gap audit

- The lemma does not prove that a producer's interval is valid.
- A smaller midpoint discrepancy is not a substitute for interval overlap.
- Choosing shards for escalation after examining widths is safe; replacing a
  valid interval by an unjustified narrower estimate is not.
- The ordinary target midpoint motivates scheduling only and never enters the
  final exact sign proof.
- A negative final D-0801 interval still requires independent T-2801 review and
  backend reproduction before an unconditional RH-disproof claim.

## Suggested next attack

Run every PR #65 range once at 192 bits with resumable hash-bound outputs.  Feed
the resulting exact intervals directly to `assemble_directed_certificate.py`.
Only if the composed checker returns `UNRESOLVED` should selected ranges be
escalated to 256 or 384 bits.
