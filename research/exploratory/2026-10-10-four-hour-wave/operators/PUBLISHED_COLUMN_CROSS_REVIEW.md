# Independent source audit of the published-height column

Verdict: **ACCEPT at the separately stated imported-contract scopes.**
Reviewed [PUBLISHED_VERIFIED_COLUMN.md](../xi/outer-ray/PUBLISHED_VERIFIED_COLUMN.md)
at SHA256
`8d8b7ee89f8d58f30eca2029cfb346fcfc777dc97703a9d0ecc3d8aa02b4a829`,
2026-10-10 14:35 UTC. The direct column argument was already independently
accepted in [CENSUS_FULL_COLUMN_CROSS_REVIEW.md](CENSUS_FULL_COLUMN_CROSS_REVIEW.md).

The reviewer read the literal extracted pages 2--3 of Platt--Trudgian,
*The Riemann hypothesis is true up to 3*10^12*, arXiv:2004.09765v1.
The downloaded PDF SHA256 is
`3362f66af9fa9373977eee70e2282ec33989d5d8b97e0852df9e32cc25b52885`,
and the extracted text SHA256 is
`eae9298a2482d36719f37aa8d0b66a1e1c5c8f6c10fcc9988b2632f07a99551e`.
Both hashes were independently recomputed. This audits the source reading;
it does not reproduce the published interval, sign-change or Turing run.

Theorem 1 explicitly states RH through height 3,000,175,332,800 and locates
the lowest 12,363,153,437,138 nontrivial zeros on the critical line. This
supplies the complete location premise through the smaller H=3*10^12.
The complete-product localization and strict lower-interior companion
sector retain every integer multiplicity and use no simplicity argument.
Consequently PV2, with y>0, follows from the stated location theorem alone.
The positive-width condition is r+2<6*10^12, exactly the integer range
0<=r<=5,999,999,999,997.

The theorem wording alone does not state simplicity. Section 2 explicitly
describes counting completed-zeta sign changes and using Turing's method
to confirm that all expected zeros are accounted for. It also states that
once a sign change was found it was counted and the algorithm moved on;
the default lattice sufficed to isolate 999,997.5 out of each million zeros.
The literal section does not separately spell out the treatment of every
remaining interval; that belongs to its imported algorithm/method contract.
Thus the
manuscript correctly identifies a stronger imported method contract:
distinct strict sign-change intervals saturate the complete zero count,
which counts analytic multiplicity. Each interval consumes at least one
unit of that count. Equality leaves exactly one unit per interval and no
zeros elsewhere, excluding both odd multiplicity greater than one and
even multiplicity without a sign change. This proves simplicity under
that explicitly stronger imported saturation contract. PV3 then follows
from the real-boundary simplicity induction in the column theorem.

This source distinction is material: importing only the paper's location
theorem supports PV2; including y=0 requires the additional saturation
contract. Neither assertion is a new large-height numerical verification.
Both columns have finite real-part range, preserve the unknown complete
tail beyond H, and supply no RH proof.
