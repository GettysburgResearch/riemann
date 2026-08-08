# Integration handoff — extra-high critical-null dyadic attack

Agent: `gpt56-pro-xhigh`  
Date: 2026-08-08  
Base: PR #322 at `72d68a043a008209455375b720cd107a436e7f32`  
Branch: `research/gpt56-pro-xhigh/323-critical-mode-null-source`  
Status: **reviewable exact advances; final RH-bearing recurrence unproved**

## Canonical new claims

```text
L-32301  multiplicative finite-difference parity sign
R-32301  five-adic critical scaling is neutral, not 1/5 contracting
L-32302  critical-null triple dyadic source
T-32301  corrected six-row RH criterion
L-32303  five-mode Euler/carry compatibility filter
L-32304  corrected paired five-mode strip frame
L-32305  critical-null source = dyadic bottom-charge difference
L-32306  exact dyadic sign blocks of the five-mode carry bank
L-32307  positive critical digital dual
L-32308  critical-null annular physical/carry isometry
L-32309  positive-inverse polylog square budget
L-32310  direct paired critical-null strip frame
L-32311  uniform critical-null carry Schur reserve
L-32312  finite Chebyshev potential for the RH-sensitive source
O-32301  radix-two principal-mode pivot
X-32301  exact Q(sqrt2) regression
```

## Two corrections made during construction

Before review, two self-audited normalization errors were repaired:

1. `T-32301`: the carry system begins at `q=2`; the correct Mellin transform has the unit-source term `-1`.
2. `L-32304`: PR #263's parity polynomial is expressed relative to the odd Euler product; the new five-mode pair requires both factors `(1∓z)(1∓z/2)`.

Do not review earlier intermediate versions of those files.

## Preferred source

Use the **triple** source

\[
P_\dagger(x)=(1-x)(1-x/2)(1-\sqrt2x),
\]

not the five-mode source, for the main lower-scale recurrence. It has:

```text
no off-line pole cancellation;
positive inverse;
positive generalized-prime sequence;
critical real-mode cancellation;
factor-eight compact carry image;
six averaged carry rows;
closed-strip parity frame;
positive digital dual;
exact annular physical/carry isometry;
O(log^2 N) normalized inverse-square budget;
O(sqrt n) generalized-prime correction.
```

The five-mode filter is retained as an analytic compatibility adapter to PR #263's pole/half-pole Green machinery.

## Correct final frontier

The new work removes:

```text
five-adic source-free residue quotienting;
critical real-mode ambiguity;
physical/carry metric ambiguity;
infinite current carry tail;
coefficient ell1 source-change explosion;
pairwise wavelet degeneracy;
unknown RH-sensitive carry coefficient form.
```

The RH-sensitive carry feature is exactly the additive defect of

\[
H_\dagger(x)
=\sum_{r=0}^3c_r\psi(x/2^r)
-(\log2)\sum_{2^r\le x}r c_r.
\]

The remaining theorem is a source-complete quadratic recurrence for this exact feature together with its strict-divisor family and the dyadic odd-column commutator.

A reviewer is **not** asked to invent that recurrence; it is explicitly unproved.

## Exact status

```text
new finite/source algebra                     proposed complete
five-adic 1/5 scaling claim                   false as a scaling consequence
annular source isometry                       proposed complete
critical-null paired strip reserve            proposed complete
one-wavelet carry reserve                     proposed complete
lower-scale inverse square budget             proposed complete
source-complete collective recurrence         UNPROVEN / RH-BEARING
Riemann Hypothesis                             UNPROVEN
```
