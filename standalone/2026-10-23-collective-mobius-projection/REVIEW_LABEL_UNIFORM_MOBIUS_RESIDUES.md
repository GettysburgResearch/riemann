# Independent review of the label-uniform scalar residue bound

23 October 2026. Reviewed file: `../two-hour-boundary-20261023/LABEL_UNIFORM_MOBIUS_RESIDUES.md`, SHA256 `12c765c1fdcccec8ebb087b7608b80bb7b2d30114bf664ac1e43a2966b9d8f89d`.

Verdict: the stated scalar deductions L2 and L20 follow from the explicitly imported inverse estimate L3, the completed finite-vector functional equation and kernel bounds of PR1015, and the residue-only density identity L16. No additional gap was found. This is a scoped analytic review, not an independent proof of those imported inputs.

The review read the full proposed note and the pinned PR1015 files `COMPLETED_FE_KERNEL.md` and `MOBIUS_FULL_SERIES_SCALAR_REMAINDER.md` at commit `e87c5f669f81fe6371af926917d1c5b21023bce8`. Their hashes are the ones recorded in the proposed note. In particular, the completed reflection retains the actual numerator nh, retains all completion ideals, and has effective modulus scale DH/Y. It does not replace nh by n or discard a reflected pole without the stated gamma-factor cancellation.

## Local coefficient and puncture audit

For squarefree n=g e m, the decomposition g=(n,rad h) and c=e^2 l c0 includes every nonzero local branch. At a prime of h, a nonprincipal local character requires modulus exponent v_p(nh)+1; a principal local character is a Ramanujan sum and requires exponent at most v_p(nh)+1. Thus the number of possible l costs H^epsilon. The normalized local magnitudes are at most one at h and p^-1/2 at e.

More importantly, before taking these magnitudes, scaling by the free m contributes bar chi_p(m)^j at modulus p^j. After finite reciprocity sectors the free coefficient is therefore exactly the original mu(m) times bar chi_m(c0 e^2 l). A modulus exponent divisible by six still imposes its nonunit zero. Remaining Gauss roots and CRT factors depend on c0,e,g,l,h, but not on m. The puncture Qeh is fixed throughout each row average; it also removes primes of h absent from l. There is no growing ray character inserted into the actual-coefficient inverse theorem.

The c0 map into rows c0 e^2 l is injective and has norm O(U). Cauchy costs the annular sum of 1/Nc0, which is bounded. The volume square roots sum with e^-1 and the other square roots with e^-17/12. These facts justify L10 and L5, including the logarithmic rather than power cost of the first sum. Fixed smooth separation is in norm coordinates and does not alter the arithmetic coefficient.

## Completion, residue, and primitive density

The reflected completion weights after taking square roots are b^-4 and b^-3/2. They are summable over ideals, and the small-argument kernel exponent 1/6-delta makes the remaining modulus dyads convergent. The exact original finite-minus-pole identity has coefficient zeta_S(2) times the nonzero Mellin value at 2/3. Choosing the auxiliary modulus test nonnegative makes division by that fixed coefficient legitimate.

The choice Y=D for H<=D makes all four terms in L15 at most D. The choice Y=sqrt(DH) for H>D makes both original and reflected row scales equal and bounds their inverse estimates by Y. This gives the claimed full residue estimate.

The residue density is used only at the pole. Its divisor expansion introduces d^-3/2 outside the normalized m-sum, changes the length to D/d and the label to dh, and keeps a fixed puncture Qd. The squared terms are exactly D^(2/3)d^(-11/3) and (DH)^(1/3)d^-3. Their square roots are summable. Shared primes of n and h are included by extracting the fixed h-density first.

## Raw full-series remainder

For U>=sqrt(DH), put A=U^(1/6)(DH)^(-1/12). In reciprocal completion, the head a<=A is bounded by reflection and the tail by the original finite-minus-pole identity. The two volume costs, after squaring, are respectively (DH/U)A^6 and U A^-6, both equal to (DH)^(1/2). The two nonvolume costs are D H^(1/6) U^(-1/6) A and D^(5/6) U^(1/6) A^-1, both equal to D^(11/12)H^(1/12).

The remaining pole cost is (DH)^(1/6) times the bound in L2. Its extra term D^(5/6)H^(1/6) is at most D^(11/12)H^(1/12) for H<=D, and at most (DH)^(1/2) for H>D. This verifies L20 on its entire stated domain. Subunit scales remain in the exact completed identity; they are not declared empty merely because a reflected scale is small.

The result is scalar and label-uniform. It does not control arbitrary combinations of labels, the primitive continuous remainder, the complementary operator, the full signed Poisson return, or a smaller zero-free boundary. Inserting it into a projection still requires the actual label weights and Gram factors.
