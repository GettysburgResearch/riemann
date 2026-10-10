# Independent arithmetic review: mixed labels, stratified inverse and A2 exponents

Reviewer: the separate `signed_sector` agent. This review covers the finite character/mask identities, row valuation bookkeeping, finite cube convolution, and rational exponent calculations. It is not a separate verification of the completed analytic norm theorem, theta automorphy, cusp estimates, or angular reciprocal input.

## Frozen targets

| File | SHA-256 |
|---|---|
| `MIXED_LABEL_COMPLETION.md` | `5e77ec88d6a191ec214bcedebc2b42d37f95735ba2bb18955b2f8a16aedfbcad` |
| `SIXTH_POWER_STRATIFIED_INVERSE.md` | `f98cc20e361ebb99af7dbd4b5ffef83a8a55ca11c4d3f24da238bc24be4cb2e9` |
| `ANISOTROPIC_A2_NORM_TRANSFER.md` | `e671b8b1c8717ed494b3db0ba39fb4c0de374aef56f774bf9a7ca68e01b277cf` |

The exact normalization inherited from PR #918's `INTERFACE_COMPARISON.md` was also read. Its correction scales and exterior weight agree with the new A2 note.

## Verdict and mathematical checks

**PASS at the stated arithmetic scope.** No arithmetic discrepancy was found in these frozen targets.

1. The effective-row identity uses q_star=q/(q,f), retains the f character's zeros, and cubes to the mask on the entire physical cube factor. Redundant overlap removal is correct even when a row or physical column shares a prime with a moving label. The outer mask on a is independent of whether the inverse factor h meets that mask.
2. Primewise division of a valuation by six gives k=v^6 k0 with 0<=v_p(k0)<=5. There is no coprimality condition between v and k0. The character identity produces the full additional physical column exclusion rad(v), and Q_v<=Q Nv is the correct local exponent inequality after removing f and the fixed bad-prime exclusions.
3. The two local exclusion branches have energy costs with exponents (0,1,1/3); the three auxiliary extraction branches have (0,1,2/3). These follow by taking norm exponents before applying the finite branch sum. The positive row-valuation tables have the specified exceptional residues: the exclusion's exponent-four amplitude occurs at valuation 4 modulo 6, and the auxiliary's occurs at positive valuation 0 modulo 6, starting at 6. The exponent-zero branch counts occur at residues 0 and 2 respectively. All displayed progression steps and leading exponents agree.
4. The finite masked inverse closes under repeated cube factors. Grouping d=hb does not impose (h,b)=1, and the inner raw squarefree index can meet d. The c_R(d) coefficient is the sum of mu(h) over the actual h divisors above R. A cutoff below one has empty short part; a cutoff at the physical support cap has exactly empty long part. These facts justify using different positive cutoffs on disjoint row strata and on A2 children.
5. Substituting Q_v<=Q Nv, H_v<<H/(Nv)^6 and R_v<=R Nv gives short energy exponents -6, -13/2-3 beta and -17/3. On uncapped long strata the exponents are -6,-3,-6. These are all strictly below -1. The finite checker does not infer convergence from sampling; convergence is the elementary ideal-counting consequence of these explicit exponents.
6. Both proposed optimal cutoffs balance the stated increasing terms against D^2 R^-3. The transition identity is H^(8 beta) F^(4 beta) Q^(5+2 beta)=D^(5-2 beta). The beta=11/12 and beta=1 examples, admissible ranges and savings are arithmetically correct. In particular 379/228-31/19=7/228 and 25/12-31/19=103/228.
7. Independently substituting the actual A2 child scales, the effective labels F_t=F Ne and Q_t=Q Nc Nd, and R_t=R(B_t/D)^(1/3), yields all six reported exterior-weighted norm triples. The angular child's correction powers before the exterior weight are (0,-1,-1), independent of beta. The only harmonic sums are one in the angular term and two in the H term. No positive power remains to be hidden in a logarithm.

## Executed diagnostic

The new checker is `check_mixed_stratified.py`, SHA-256
`4ee32d85af1c48743050958fc0e81dc9bcd8878ecb06c596223b0e2dc893593b`.

Its generated report is `mixed_stratified_checks.json`, SHA-256
`64b6e272cd153e4a6fe37f6cfbc7203e50eab48708b2cba59baa450efe75be04`.

I ran the checker successfully. All comparisons use exact integer or rational arithmetic in Z[zeta_6] or rational exponent vectors. Every acceptance gate raises RuntimeError explicitly; none relies on a removable Python assert.

The finite coverage is:

- 2,401 effective-row relabel identities and 2,401 cubed identities, covering every zero/sixth-root assignment to the row, f-only, q-only and common q/f phases.
- 14,406 cube-inverse mask identities, covering all such physical character values and every sixth-root lambda value.
- 175 one-prime and 8,281 two-prime sixth-power identities, including 5,145 checks with a shared prime between v and k0, plus 40 effective exclusion checks.
- Exact leading exponents and 216 geometric residue checks for the local valuation tables.
- 3,136 full finite inverse identities and 25,088 truncated inverse identities over every q/f/outer-mask combination in the two-prime model and all 49 row phase/zero assignments. This includes 3,136 below-one empty-short cases and 3,136 exactly empty capped tails.
- Nonzero witnesses for all three easily lost overlaps: 1,344 repeated h/b terms, 2,688 inner n/d terms, and 780 outer-mask r/h terms.
- Exact rational vertex checks for the six-term optimization at beta=1 and beta=11/12. The checker uses the feasible log-parameter tetrahedron split by R1=R2; the resulting inequalities are affine on each piece, so it checks each piece's vertices rather than a floating-point grid.
- The six A2 norm-exponent triples at three exact beta values, their normalization, the harmonic counts, and all seven admissible one-prime A2 label-overlap patterns.

## What these checks do not establish

The finite cube model uses arbitrary exact sampled physical data with the original incidence and support rules. It verifies the convolution and masks for such data; it does not numerically construct the actual Gauss coefficients or a theta transform. Their analytic realization remains an input to the manuscripts.

Likewise, the local exponent checks do not independently prove the norm inequalities to which the exponents belong. The full A2 transfer additionally requires the source-conditional mixed completed theorem and the analytic sieve estimates with their stated uniformity. This review does not certify those inputs, the original signed first-Poisson comparison, any full higher moment, or a zero-free boundary.

The review supports publishing the arithmetic deductions and the finite diagnostics with these boundaries intact. It supplies no additional claim of external novelty, independent human peer review, or proof-assistant formalization.
