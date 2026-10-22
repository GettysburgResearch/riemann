# PR #473 exact direct-integral normalization obligation

Frozen proposal head: `71d6a859ea741fe035de709e8d10ed37301b778e`

## The required statement

Let positive root fibers satisfy

\[
P_s=P_s^{\rm cur}+
\sum_i a_i(s)A_{s,i}Q_{s,i}.
\]

The hereditary consumer requires

\[
\int\sum_i a_i(s)m(A_{s,i}Q_{s,i})d\lambda(s)
<
\frac18\int m(P_s)d\lambda(s).
\]

After grouping by source/provenance label `b`, write the actual aggregate child
target mass as `M_b`. The correct normalized decomposition is

\[
P=P^{\rm cur}+\sum_bM_bA_b\widehat P_b,
\qquad
m(\widehat P_b)=1,
\]

and, after normalizing the parent,

\[
\sum_b\alpha_b
=
\frac{\sum_bM_b}{m(P)}
<
\frac18.
\]

## What PR #473 proves

PR #473 proves the coefficient identity and strict coefficient bound for one
packet. It also proves positive endpoint integration of already specified typed
identities.

It does not prove the mass-weighted inequality above, define the normalized
aggregate children, or establish that one common rough-prime coefficient list
represents the first-owner direct integral.

`X-91692` checks only a toy example with one common hard-coded coefficient per
prime.

## Why simple coefficient grouping is insufficient

Take two unit-mass fibers and one common provenance label, with fiberwise child
coefficients

\[
a_1=\frac19,
\qquad
a_2=\frac1{100}.
\]

The aggregate child target mass is

\[
M=\frac19+\frac1{100}.
\]

After parent normalization by total mass two, the hereditary coefficient is

\[
\alpha
=
\frac M2
=
\frac{109}{1800},
\]

not `1/9`, not `1/100`, and not an unweighted count of the two coefficients.
The desired contraction remains true, but it follows from target-mass
integration and normalization, not from the phrase “the outer coefficient list
appears once.”

## Known successor

PR #476 at `9f16ce483954d4233b68ee09cb6bec47400aa3cc` adds `L-91694`, which proves exactly the required
Tonelli/mass-normalization statement. It is a material successor and should be
made an explicit dependency of any repaired SONTR proposal.
