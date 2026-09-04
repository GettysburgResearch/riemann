# Quadratic mixed-difference continuation — PR #790

**RH and the unrestricted mixed inequality remain unproved.** This packet
contains a proposed complete proof of a uniform quadratic positivity region.
Independent mathematical/code review and external novelty assessment are pending.

Parent head: `11f20a995d740347177bb39e378cf5261d25132b`.
Branch: `research/astra/20260905-theta-bernstein-exterior-closure`.
This is an add-only child of the two existing packets; their files are unchanged.

## New theorem ASTRA-QW-01

For the SAME invariant xi function and mixed differences as in the parent,
put n=a+1 and r=b/n. Then

    a>=0, b>=10^8(a+1)^2
       ==> H_(a,b)(1) > (1/8) r^b/(1+r)^(a+b+1) > 0.

Both indices are unbounded. No zero scan, numerical extrapolation, or
change of v is used. The constant is conservative, not optimized.
The gain is the quadratic exponent in a+1; for small a the earlier cubic
region has a better constant, so all previously proved regions are retained.

The proof combines the two complex phase fractions before estimating.
Their linear contribution cancels at the real saddle |A| approximately r.
A local zero-count lower bound supplies positive mass near gamma=sqrt(r).
A matching local upper bound controls the Gaussian tail of the potentially
negative middle terms; remote low and high tails are estimated separately.
The high zeros used here need NOT be on the critical line or simple.

The new classical input is only Rosser's 1941 bound as reproduced in
Trudgian's Table 1, and the elementary completion remainder, yielding
|N(T)-F(T)|<log T above 1467. The sharper modern S(T) bounds used by one
part of pass2 are not needed for this theorem. The original Rosser proof
is imported, not independently rebuilt. The two source pages were rendered
and inspected. No current external priority claim is made.

## What is now proved on this branch

Subject to the stated classical inputs and independent review:

- Every a>=0 and every v>0: all 0<=b<=22 mixed inequalities are positive.
- At v=1: every b>=0 works for 0<=a<=19.
- At v=1: a>=2 and b<=100a is an unbounded positive cone.
- At v=1: b>=max(10^6,8000(a+1)^3) is the earlier cubic positive region.
- At v=1: b>=10^8(a+1)^2 is the new quadratic positive region.

The pass2 phase rectangle pays still more cells. These facts do not leave
a finite verification task. The still-uncontrolled region is contained in

    a>=20,
    100a<b<min(max(10^6,8000(a+1)^3),10^8(a+1)^2).

The exact negative-row-mass growth theorem from pass2 is retained:

    limsup_N (sum_a binom(N,a)|H_(a,N-a)(v)|)^(1/N)
      = sup_A (v+|A|)/|v+A|.

The rate is one exactly under RH. A proof of the complete source-side
subexponential Laguerre-trace bound would therefore close every mixed
inequality. This packet does not prove that bound.

## Review and replay

Read `PROOF.md`, especially Sections 3--7, then `VALIDATION.md`.
The exact checker binds the original HEAT_BERNSTEIN.md and THETA_COUNT.md
Git blobs before checking finite rational algebra. Run from this directory:

    python verify.py --check checks.json
    python -O verify.py --check checks.json
    sha256sum -c SHA256SUMS

Executed: 657 exact rational/Gaussian-rational controls in each mode, with
byte-identical full JSON; four refusal tests (corrupted result and corrupted
published parent, each in both modes); the original 225-check finite suite
rerun in both modes. These are not machine proofs of the infinite theorem.
No new high-zero computation, new interval census, Lean build, remote CI
success, independent referee acceptance, or full RH proof is claimed.
