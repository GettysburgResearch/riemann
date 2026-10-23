# Independent review of the R=4.84 logistic assembly

2026-10-21. Reviewer: boundary_attack, independent of the root's scalar
producer and global_route's wrapper. This is an audit receipt, not a
claim that imported theorems have been reproved or that RH is proved.

Reviewed exact SHA256 values:

- `../three-hour-root/LOGISTIC_MASTER_REDUCTION.md`:
  `87e4cb2825d198d49cf27ac652ff4cb89d8e891880cd9674db26b44f7ed3bfdb`.
- `../three-hour-root/certify_logistic_master.py`:
  `3200651b87fc5a04f79d793c8b86313a6ac3cf6c86331a95c76bc0668d7cd5cf`.
- Its JSON: `bac091574f8f6a1dc5f2a9c00ac7b3ea9caf200d6f27823d05f788a53d08c166`.
- `../three-hour-type/verify_logistic_master_fraction.py`:
  `cefd18641114b6fedd8cf3334bcdd2857da7d4694bbbbc951238603e90fc2413`.
- Its JSON: `3f1722d0579df61561b18ca3e1dabc66b01826d68837adf7ff951021cb18fbe6`.
- `../three-hour-global/LOGISTIC_GLOBAL_WRAPPER.md`:
  `acb4b29ef72c031eb78ec27f41c8f4169e648f554a35badc559472077a8b36cb`.
- `../three-hour-type/LOGISTIC_ADMISSIBILITY.md`:
  `a06963aef0863ef1cdf63e93aab27c4b8f0c8051cbab7f159d468e7596d7a25f`.
- `../three-hour-type/LOGISTIC_REAL_AXIS_CONSTANTS.md`:
  `9da9ad7051fcf3deb94db3d951051425c549313074d0ee5bd0dcfae3312c8139`.

No unresolved defect was found in the reviewed interfaces. In particular:

1. The three logistic-complement errors have the correct signs and
   denominators. The globally C2 compact extension and w'(0)=0 justify
   the quadratic error even beyond the support. The positive beta series
   for J and its one-sided tail are correct. The two moment algorithms
   are distinct valid enclosures of the same moments.
2. The directed implementation uses **mpmath.iv**, not Arb. Its interval
   comparisons accept only a strictly positive entire lower endpoint.
   The Fraction implementation has exact outward integer rounding,
   valid sine/cosine, exponential and logarithmic tails, and correct
   handling of intervals of either sign in integer powers.
3. `replay_logistic_review.py` independently reread both frozen JSONs,
   checked their producer hashes, recomputed every accepted box, and
   checked exact containment, disjoint interiors and area 1325/121.
   All 32 directed and 42 rational boxes passed. Finite unions of their
   closed boxes therefore cover [0,25/121] x [28,81], including edges.
   This replay does not overwrite either producer's certificate.
4. The real-axis E correction bound and gamma constant use the right
   normalization f(0)=eta*w(0)/2. The source polynomial's squared-modulus
   representation proves nonnegativity; its reconstructed coefficients
   are nonnegative. No prime lower contribution is needed here.
5. The finite minimum-zero argument is logically sufficient: any
   violation lies in the compact intermediate height range; the
   classical strict strip gives a positive minimum B; this same B
   bounds every higher zero. Reflection places all retained pairs in
   the exact logistic positivity strip. Thus no numerical initial
   classical zero-free constant or infinitesimal iteration is imported.
6. The revised wrapper's direct Lehman tail integral is valid, including
   the two signs of the zero height, k=0 separately, and conservative
   factor 10. Its numerical losses fit inside 1e-7. This review does
   not use the source's separately evaluated tail constants.

I reopened BTY's primary text, https://arxiv.org/html/2603.21490v1 :
equation (3) gives the stated Littlewood region for t>=3; equation (5)
states the finite RH input H=3e12; Section 4 gives the exact polynomial.
Those published inputs, and Lehman's quoted counting inequality, remain
external dependencies. The explicit-formula adapter has also been
independently reviewed by global_route; I checked its normalization and
its use in this assembly, not every historical proof behind the source.

The supported proposed conclusion is the classical logarithmic region
Re(s)>1-1/(4.84 log|Im(s)|), |Im(s)|>=3, subject to these stated inputs.
It does not lower the repository's distinct B_flat or imply RH. Smallest
remaining potential failure points are an error in an imported analytic
input, the adapter's explicit-formula/positivity argument, or a mismatch
between these frozen files and a later assembled version. This receipt
does not certify subsequent prime-side or parameter refinements.
