# Source trace for Hu's fixed-type fourth moment below 3/4

**Status:** Independent source-level audit and proposed conditional proof extension. The source's arithmetic and analytic assertions are imported; the finite induction has not been independently replayed in every local case, and no zero-free region follows from the moment alone.

**Precise target.** Take all definitions, coefficient classes, masks, fixed-field and fixed-infinity-type hypotheses of Hu, [Theorem 4.2](https://hexagonmath.org/2610.00216v1). Replace its interval `3/4 <= kappa <= 1` with `13/18 <= kappa <= 1`, retaining the same finite-order Hecke zero-free premise when `kappa<1`. The proposed conclusion is exactly Hu's (4.4)–(4.5), with the mesh chosen uniformly on the enlarged compact interval before the slot count. It does not assert a zero-free estimate for the infinite-type background.

**Imports.** Use Hu §§3–4's stated fixed-type coefficient, local and orbital-Poisson assertions, in particular Lemmas 3.3, 4.4, 4.8, 4.11 and 4.12; Hu's conductor and mask relations (4.35)–(4.37); the two-transform, diagonal and exceptional-case estimates quoted in his §4.8 from OpenAI §18; and a standard logarithmic-derivative estimate on a line a fixed positive distance to the right of the finite-character zero boundary. Use Xu–Sang, [arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), Appendix A, for their explicit audit of the parameter occurrences in the OpenAI induction. These are source inputs, not mathematical claims independently established by this note.

## Trace of the fixed-type and field interfaces

1. **Coefficient class.** Hu §4.1 writes the live character as `lambda_u=omega_0 xi_u` and pairs every selected slot with coefficient `omega_0^-1` times a finite `Theta` combination. Lemma 4.4 explicitly preserves the whole-product character, the common mask and both orientations after each transform and extraction. The actual character in a live prime sum is consequently finite-order. Conjugation is applied to a whole product, not to a single character stripped of its mask. None of these identities contains `kappa`.
2. **Extra masks and ordinary reflection.** Equation (4.35) removes a common extra radical by exact divisor expansion; (4.36) retains the primitive conductor *and* redundant radical in the common width; (4.37) bounds the reflected plain length. These statements, including fixed infinity-type gamma factors, make no reference to `kappa`. A variable norm phase is in the smooth profile, and its polynomial height cost remains in the source bounds.
3. **Positive-slot input.** Hu (4.38) is derived from a logarithmic-derivative bound on `Re(s)=(1+kappa)/2+e`. If the finite-order Hecke family is zero-free to the right of `(1+kappa)/2`, every selected finite character is nonprincipal: otherwise the inducing finite character would belong to `Theta`, contrary to the positive-slot row restriction. Smooth prime counting gives the normalized squared slot exponent `kappa+2e` per unit length; removal of row and common-mask primes must retain the source's divisor/height losses. Since all declared lengths are bounded, choose `e` in the initial loss budget uniformly for `13/18<=kappa<1`. At `kappa=1` use Hu's absolute-counting case. The new lower endpoint stays a fixed distance above `kappa=0`; no infinite-type zero-free premise is used here because of item 1.
4. **Exceptional rows.** Hu Lemma 4.11 treats an exceptional fixed background by equal-product residue cancellation, retaining a common mask. In §4.8 the second-transform exceptional condition forces sixth powers in finite unit sectors and gives (4.44). The counting and local valuation deficits that follow use no `kappa`. The method does not identify an exceptional finite inducing character as an exceptional arbitrary Hecke background; its live background is carried separately.
5. **Loss and order.** Hu Lemma 4.12 propagates finitely many seminorms and height powers backward through a finite tree. Proposition 4.14's ordinary-capacity stability uses `0<=6kappa-1<=5`; this remains true for the enlarged interval. Its other inputs are a fixed positive width drop and finite factorization types. This gives a uniform slot mesh only after the induction and its stated source bounds are available; one must not change the number of slots or the target midway through the construction.

## Parameter-dependent steps

Write `M` for effective width, `z` for total live slot length and `A=n1+n2+z`. On the proposed interval the capacity `n1+n2+6kappa z<=M` gives

    kappa z <= M/6,       z <= 3M/13.

In Hu's width floor the first inequality pays the positive-slot cost. In the centered range `A>5M/6`, one has `(6kappa-1)z<M/6` and `6kappa-1>=10/3`, hence `z<M/20` and `A-z>47M/60> M/2`. Hu's comparison length is `M/4`; the reflected comparison formula (OpenAI (18.15), repeated in Hu §4.8) then implies the same bounds as before:

    A_comp <= 3M/2 - A + 2z + xi < 23M/30 + xi,
    A_comp + (6kappa-1)z < 14M/15 + xi.

Both retain a margin at least `M/15` against their respective `5M/6` and `M` boundaries, before `xi`. For a positive child with affine defect `F`, each removed slot of length `s` reduces that defect by `6kappa s` and costs `kappa s`; a whole-slot greedy prefix therefore costs at most `F/6 + kappa eta <= F/6+eta`. If slots run out, use the zero-slot moment instead. The source's independent width-gain bound pays `F/6`. For perturbations, `6kappa-1<=5` preserves the source's aggregate error `|delta M|+|delta A|+5|delta z|`.

These are the exact changes in Xu–Sang Appendix A, whose finite-type induction starts from the same OpenAI Lemma 18.1. Hu §4.8 explicitly describes the same sequence for fixed type: zero-slot bands, uncentered and centered stages, one-pool amplification, two-transform width drop, clipping, and exceptional cancellation. The displayed source trace gives no further *numerical* obstruction at `13/18`.

## Review boundary

The proof extension is justified if Hu's κ-independent assertions and the referenced OpenAI induction hold with the displayed field/type and mask quantifiers: then the calculations above replace each use of `3/4`, and finite propagation gives the same conclusion. Hu's printed theorem itself cannot be cited for `kappa<3/4`. A line-by-line independent replay of the source's two finite transforms, sectorwise coefficient independence and exceptional-frequency ledger has not been performed, so this note does not certify those imports or claim unconditional closure. In particular, it has not independently shown that every hidden use of the old interval in the referenced induction has been exposed; Xu–Sang's appendix is an external source assertion for that completeness check. The nontrivial analytic burden remaining for an improved zero-free theorem includes the variable-geometry high-side contour and common-probe estimate, even if this moment extension is granted.

**What was checked:** Hu (4.35)–(4.44), Lemmas 4.4, 4.11–4.12 and Proposition 4.14, the relevant formulas in OpenAI §18, and Xu–Sang Appendix A; exact rational algebra of all displayed κ margins. No full Lean or local arithmetic proof replay was performed.
