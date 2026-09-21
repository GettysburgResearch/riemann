# Audit of the first #903 packet and transfer boundary

Reviewed remote #903 head: `67132424e3cbe35a94752581a5b5271ab8bfc56f`.
Earlier #848 parent: `617cfaca6130addd2d16bbce6af117a55aef761b`.
Current #848 observed during this pass:
`7de75c02417d5d8db7eafb1ceba364380e72d16a`, including the separate
rough-squareclass continuation. That contribution is preserved, not
silently replaced or claimed as this pass's work.

## 1. Publication defect

Reading the actual uploaded PROOF_NOTES.md showed that many LaTeX
backslashes had been consumed before publication; `\tag` had become a
literal tab and other commands had lost their backslash. The same problem
is visible in the PR body. This packet supplies correctly escaped source
as file bytes and an explicit superseding reading order. It does not
pretend that the existing remote files have already been repaired.

## 2. What the earlier mathematical sketch really established

The one-prime divisor-pair identity and two-prime inclusion-exclusion
identity are valid elementary facts. The antichain statement is valid
when the chosen prime is the least prime, so the remaining divisors are
rough relative to it. A multiplicative window alone is not an antichain:
4 and 8 both lie in (15/5,15] and one divides the other.

None of those observations specified the K_Y needed for the energy.
The earlier packet explicitly deferred it, supplied no executable,
produced no signed covariance table, and proved no all-scale gain.
It was a plan, not an executed arithmetic attack.

## 3. The substantive scope correction

For e=delta-1*g with g the true prefix, e vanishes below b=Y+1.
Therefore `mu*e*e` is zero below b^2. The new prefix's energy must be
studied through `g*e`, not by treating the vanishing reconstruction error
as though it were the annular output. PROOF.md supplies that map exactly.

## 4. What changed after testing the map

The prime-pivot collapse is genuinely source-specific: arbitrary
multiplicative squarefree signs do not suffice for inversion of the
fixed sequence 1. However, it does not turn cumulative energy into a
small positive sum. On the native source, large-prime semiprime channels
have coherent positive covariance. PROOF.md gives finite exact lower
bounds and their PNT asymptotics.

Accordingly, the old target of bounding a sum of positive blocks must
not be promoted for the raw pivot partition. Its failure is not merely
a hypothetical fake-source objection. It occurs on mu itself. A
coarser, signed grouping remains possible; no result here excludes it.

## 5. Relation to other #848 kernels

The newly computed matrix is for the physical Mertens annulus and the
exact A/F completion interface. It is not the table of PCR26 harmonic
product covariance, nor RCB26 rough-squareclass covariance. Calling all
three quantities C_Y without identifying their source maps would hide
a serious mismatch. Their exact common consumer is stated in PROOF.md.

## 6. Sylvester is a model of proof design, not an imported RH theorem

In Burungale--Tian the norm of a first division can be a nonzero point of
E[lambda] although the original trace is zero. In a complex vector space,
ordinary scalar division commutes with a trace and has zero kernel; the
same construction collapses to zero. The arithmetic source of their
nonzero boundary has no literal replacement here.

Our finite Euler cancellations are exact and useful, but are not Tate
cohomology, do not supply a Frobenius obstruction, and do not convert
nonvanishing into a uniform upper bound. The rank-one L-family adapter
uses the actual imported theorem separately, at precisely its central-
order scope. It does not rebrand that theorem as a result on all zeros.

## 7. Honest assessment

The first packet did not justify calling the new partition promising on
the basis of a better norm bound. This executed pass narrows that claim:
it produces an exact arithmetic map, falsifies the naive positive-block
estimate, and identifies the signed compensation that cannot be thrown
away. The desired unbounded native estimate is still not proved.
