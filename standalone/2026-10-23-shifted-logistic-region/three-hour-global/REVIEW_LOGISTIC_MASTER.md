# Independent audit of both logistic scalar certificates

Reviewer: global-route agent. The reviewer authored the separate global
minimum-zero wrapper, but did not derive the scalar lower reduction or
author either numerical producer. Accordingly this is an independent
component review, and a coauthor check of its intended global use. It is
not human review or an external certification of the complete theorem.

## Frozen inputs

* ../three-hour-root/LOGISTIC_MASTER_REDUCTION.md:
  87e4cb2825d198d49cf27ac652ff4cb89d8e891880cd9674db26b44f7ed3bfdb.
* ../three-hour-root/certify_logistic_master.py:
  3200651b87fc5a04f79d793c8b86313a6ac3cf6c86331a95c76bc0668d7cd5cf.
* ../three-hour-root/LOGISTIC_MASTER_CERTIFICATE.json:
  bac091574f8f6a1dc5f2a9c00ac7b3ea9caf200d6f27823d05f788a53d08c166.
* ../three-hour-type/LOGISTIC_FRACTION_REPLAY.md:
  7849149e4f9a8a14ff14d3d4cb820957f0c49bcbb85c60dfbee2c472f842cc34.
* ../three-hour-type/verify_logistic_master_fraction.py:
  cefd18641114b6fedd8cf3334bcdd2857da7d4694bbbbc951238603e90fc2413.
* ../three-hour-type/LOGISTIC_FRACTION_CERTIFICATE.json:
  3f1722d0579df61561b18ca3e1dabc66b01826d68837adf7ff951021cb18fbe6.

No outstanding issue was found in the reviewed scalar argument.

## Mathematical reduction

I checked the algebraic identity for the elementary w formula against
BTY Definition 1. The global inequality |w(v)-w0|<=500v^2 follows from
the compact C2 extension, not an unsupported continuation of the
trigonometric formula. The complement C(z) has the indicated sign in
F=W-C. Its error is at most 1000eta^3/(z+alpha)^3; the direct reflected
term has denominator z2^3. All three errors enter the lower bound with
the unfavorable sign. The gamma resource has precisely f0=eta*w0/2,
and consequently the leading factor A*aP*w0/4. There is no extra kappa.

For J, substituting t=exp(-alpha*u) gives the positive beta expansion.
Its initial term and ratio n*alpha/[2(b+n*alpha)] are correct, and the
tail after index 48 is bounded by 1/(2^49*b). The stated one-sided
interval includes the entire tail. The W Taylor error follows by
integrating the degree-24 exponential remainder against 0<=w<=6 on
support below 1.1. Its absolute size is below 10^(-20).

The parent's complex integration-by-parts moment recurrence and the
second producer's direct even/odd power series both give the correct
moments. In the second implementation kU=2theta is used exactly.
The discarded complex exponential tail bounds both real and imaginary
parts; omitting the denominator n+m+1 from its upper bound is safe.
No cancellation is assumed in either interval calculation.

## Arithmetic and coverage

I read both producers in full. The parent uses mpmath's directed iv
arithmetic, not ordinary mpmath point estimates. All input rational
endpoints are enclosed before arithmetic. Its depth limit fails rather
than accepts an unresolved box. The independent producer uses only
Fraction/integer operations for decisions, with correct outward floor
and ceiling at 192 binary places. Its signed interval powers and
reciprocals preserve enclosure. Its exponential, logarithm and sine/
cosine remainder estimates have the stated directions and domains.

The Fraction producer uses a different moment computation, direct
polynomial summation and alternating coordinate subdivision. Its exact
containment, nonoverlap and total-area checks establish coverage of the
closed rectangle: a finite union of closed boxes cannot omit even a
boundary point without leaving a relative open subset of positive area.
The A=0 face is only the continuous scalar extension; no physical
zero-detector argument divides by eta there.

Independent replay in this review:

* Recomputed the parent's 32 boxes and checked their coverage separately
  by all coordinate-grid cells with exact rational comparisons. All
  margins were positive, the smallest exceeding .0001167. The helper
  replay_logistic_master_review.py also rejected a missing box, an
  invalid W Taylor domain and a deliberately overlarge claimed constant.
* Copied the exact Fraction producer into fraction-replay/ and ran it
  in ordinary and optimized Python. Both runs passed: 42 boxes, 83
  evaluations, minimum rational lower bound greater than .0000655,
  exact area 1325/121, and the deliberately overlarge A negative control.
  Acceptance uses no assert statements and remains active under -O.

The independent source already fixes the same rational constants and
mathematical inequality as the parent. Agreement is therefore evidence
against an implementation error, not two independent proofs of the
external analytic theorems. The explicit formula, kernel positivity,
zero-count tail, finite RH verification, Littlewood region and global
minimum-zero argument remain separate obligations.
