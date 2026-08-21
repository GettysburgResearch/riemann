# M-26201 — Review protocol for the half-pole boundary-jet proposal

Claim ID: `M-26201`  
Status: **METHODOLOGY / FAIL-CLOSED REVIEW PROTOCOL**

## Freeze

Review one immutable commit. Do not use a later correction to verify the frozen
identity.

## Reconstruction order

1. Recompute the determinant `-233/64` and confirm that the old zero-mass
   conditional-Hankel claim is false.
2. Derive the all-order moment formula `L-26201.1` from the Green generator.
3. Verify weighted translation cancellation of the half-pole moment.
4. Reconstruct the Peano/B-spline formula cell by cell.
5. Expand the dyadic oversupport source and recover
   `M(Y)-M(Y/2)` exactly.
6. Build the independent-frequency physical reflected block from the source
   manifest, not from a one-frequency global vertical integral.
7. Emit the actual jet map, B-spline reserve, reflected Schur reserve, and
   negative jet matrix in one declared metric.
8. Test the source-image LMI.
9. Project to the dyadic and `2/3` Mertens shell firewalls.
10. Apply the Mellin–Landau deduction only after the finite identity is accepted.

## Mandatory mutations

- unrestricted point masses must still reproduce the negative determinant;
- removing the weight `2^-1/2` must break half-pole cancellation;
- deleting the oversupport collar must fail the Mertens projection;
- replacing the two-frequency reflected block by the old one-frequency integral
  must fail;
- the rank-`K` same-sign Möbius cube must remain visible;
- swapping one endpoint convention must break the B-spline checksum;
- noncoprime residue chains must be enumerated rather than folded into a false
  primitive step.

## Acceptance standard

The reviewer need not prove a new theorem. The branch asserts one concrete
identity and one concrete finite source-image LMI. Accept only after both have
been reconstructed symbolically or by a proof-producing general finite schema.
