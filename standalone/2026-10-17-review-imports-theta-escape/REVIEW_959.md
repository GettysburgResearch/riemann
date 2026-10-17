# Adversarial review of PR #959

Reviewed head: `7b845294207d96b883c1fa95028663082267804f`.
Reviewed file: `standalone/2026-10-17-numerator-mean-refinement/PROOF.md`.

## Verdict and independence boundary

**No fatal inconsistency identified in the analytic interfaces and exponent calculation inspected. The composition is provisionally coherent, not independently certified.** The new use of a family second mean is legitimate provided the explicit character-family adapter is retained. The review below is a fresh AI derivation against primary texts and a separately written arithmetic checker. It is not external peer review, a second human/agent referee, or validation of all upstream analytic foundations. The complete 11/12 theorem should continue to be called proposed.

The review deliberately did not infer correctness from the PR's Git hashes, 1,344 test count, source-author reputation, or the fact that its inputs are stated unconditionally. Source-compatible composition is the actual question.

## 1. What was checked against the sources

**CT source and scale:** the actual v2 TeX, rather than its abstract or the repository's paraphrase, supplies the dyadic reflected estimate and explicitly discusses every fixed support exponent M>1. Its additive normalization is 1/Y+1/X. With X=Z^alpha, Y=Z^beta and beta<=alpha, these give the claimed theta exponent alpha+beta/2-1/2. The full Mellin monomial gives C=1/6+alpha/3 and b=1-C. No old normalization may be retained after alpha changes.

**Correction domain:** the five local convergence conditions and both linear branches of the final shell condition agree with the inequalities in #959. All original and retuned vertices checked in `verify.py` satisfy the resulting convex domain for 0<e<=10^-5. Principal residues are handled separately. The joint Gaussian depends on Im(xi)+Im(z), not on Im(xi) alone; rapidly decreasing z weights are necessary for the horizontal-tail argument.

**Exact family:** CT's unique allowed generators modulo sixth-power S-units can be used for de Faveri's freely chosen representative generators. A deep ray-principal generator is a local sixth power at S. Therefore the two generators differ by an allowed sixth power, after multiplying by one of a fixed finite set of S-unit representatives. Their residue symbols agree on coprime test ideals. On noncoprime ideals both must retain their zero extension. The extra S-unit symbols are fixed finite-order ray twists, not the generally infinite-order angular theta phase.

This identifies the intended families at the stated algebraic interface. It is not an independent reconstruction of Kummer theory or an actual field computation. The ordering is by the full sixth-free ideal norm; replacing it by radical or conductor ordering would invalidate the transfer.

**Central numerator mean:** BGL (5.1) really contains the relevant sixth-free subfamily of its all-index weighted mean. Its proof keeps complete approximate-functional-equation columns. The squarefree/powerful decomposition does not discard non-squarefree columns: their root weights are summable with a positive loss. Fixed ray twists multiply column coefficients; root numbers are row phases. The remaining powerful-row sums have orders U, L sqrt(U), and (UL)^(2/3), with L approximately U^(1/2) times a height factor. This is compatible with the stated U^(1+epsilon) mean and polynomial height cost.

For a zero-selected subset C, the deterministic inequality

    sum_C |L| <= sqrt(#C) sqrt(sum_all |L|^2)

does not require random selection or independence. Uniform bounds for the reciprocal and correction must be taken first. In particular it does NOT estimate a moment of 1/L. The U^(1/4) gain over separate convexity bounds on U numerators is real in this upper-bound calculation.

**Density and reciprocals:** de Faveri's proof of Corollary 1.5 supplies the displayed full detector inequality, with both indices sixth-power-free. Direct substitution of the three original parameter sets reproduces all ten norm powers and ten height powers per threshold. Conjugation preserves zero counts in the symmetric rectangles. Fixed exceptional sets must be chosen before subsequent arbitrarily small reciprocal losses. The zero-free logarithm disks have the required nesting; Borel--Caratheodory followed by three circles permits U^eta for each later eta>0 without redefining the sets.

**Contours and conclusion:** the good class has full size, each middle class is counted at the lower threshold but shifted beyond the upper one, and the last class remains on an Euler-convergent xi line. The two principal remainders, small frequencies and the large-frequency line with positive e all fit the recorded budgets. The horizontal estimate uses the two-variable height decay. The Mellin argument is point-by-point in fixed positive e and does not assert a uniform e->0 bound. H is nonzero in the relevant region, and the abelian descent uses entire nonprincipal Hecke factors, not unproved general Artin holomorphy.

## 2. Concrete corrections and cautions

**Source numbering:** #959 calls the correction estimate “CT Lemma 11.1” and principal nonvanishing “CT Lemma 11.2.” In the inspected v2, the former is the calculation in Section 11.1, especially (11.1)--(11.2); principal nonvanishing is **Lemma 11.1 in Section 11.2**, TeX label `lem:principal-nonzero`. This is a reference error, not a contradiction of the estimates. Labels and exact statements should be used in any revised manuscript.

**Three-way endpoint tie:** with the original parameters tending to alpha=beta=1/2, the theta estimate, the good nonprincipal class, and the principal z remainder all have growth exponent 1/4. Consequently improving the theta bound ALONE, while leaving the other estimates and contours unchanged, does not improve the zero-free conclusion. This qualifies the informal description of the next bottleneck; it does not invalidate the 11/12 proposal. `THETA_ESCAPE.md` removes these additional ties explicitly.

**Do not oversell the independent check:** rational arithmetic verifies substitutions into formulas; it cannot verify that a theorem was imported into the right family. This report separately inspected that adapter, but did not run a proof assistant, rebuild CT's metaplectic theory, reproduce BGL's entire infinite-tail proof, or audit every transitive axiom in the upstream formalization. A further genuinely external audit is still appropriate before a public theorem announcement.

## 3. Research consequence of the review

The averaging lemma is not the obvious place to search for another easy gain. The sharper task is a signed estimate for a restricted portion of the original theta pairing. High-powerful rows can already be removed with a quantified saving, and the Poisson comparison can be retuned to leave room for a small improvement. This yields a falsifiable single remaining analytic target rather than the vague instruction “improve Cauchy.”

No modification to #959's original proof or scientific status is made by this packet. A separate review comment links this report so its qualifications remain visible beside the proposed theorem.
