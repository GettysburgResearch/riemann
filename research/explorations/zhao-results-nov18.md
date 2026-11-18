# Three questions on Mertens means and prime biases

The November 18 branch proposes answers to questions in §8 of Tianyu Zhao's 2025 paper. All three use exact prime statistics. Their hypotheses and the extent of the classifications differ. [Original paper](https://doi.org/10.1007/s40993-025-00640-y)

**The third Mertens product.** The proposed proof removes the remaining regularity assumption when zeta zeros approach the line of real part one. In that case the integrated normalized Mertens product error has positive and negative excursions of size \(X^{1-o(1)}\). The arithmetic positivity for every \(X>2\) is therefore equivalent to RH. The argument retains the finite-product prime-power correction. One proof imports Zhao's Lemma 10; a separate Gaussian and power-sum proof derives the required lower bound directly, including multiplicities and clusters. A refinement gives both signs in every sufficiently late shrinking logarithmic window. [Criterion](zhao-third-mertens-nov18.md) · [Direct proof](zhao-native-oscillation-nov18.md) · [Local envelope](zhao-sharp-envelope-nov18.md)

**Integrated prime counts.** For quadratic characters, under individual GRH, central nonvanishing, and independence of the distinct positive ordinates, exactly 19 fundamental discriminants have the eventual negative sign. The sufficiency direction for those 19 needs only their own GRH. The paper's proposed inclusion encounters the unconditional counterexample \(-59\), which is in Table 3. Its phase-zero Fourier value under GRH lies below \(-2/3\), and an off-line zero would force sign changes by the separately verified absence of real zeros in the relevant segment. For primes in residue classes, joint GRH, absence of central zeros and the stated independence of inducing ordinates give the full classification in the progression note. Unconditional phase certificates, density results and bounds requiring fewer assumptions are separate. [Discriminants](zhao-bias-classification-nov18.md) · [Progressions](zhao-progression-classification-nov18.md) · [Unconditional results](zhao-bias-unconditional-nov18.md)

**Prime ideals.** Exactly **2,580 number fields up to rational isomorphism** pass Zhao's strict spectral test under their Riemann hypotheses. The degree cannot exceed eight. Complete discriminant tables, exact prime ideal decompositions, finite explicit formulas and interval evaluations of the completed Dedekind zeta function supply the proposed census.

| Degree | Number of passing fields | Inventory |
|---:|---:|---|
|1|1|The rational field|
|2|168|[Quadratic fields](zhao-number-fields-nov18.md)|
|3|367|[Cubic fields](zhao-cubic-fields-nov18.md)|
|4|871|[Quartic fields](zhao-quartic-fields-nov18.md)|
|5|616|[Quintic fields](zhao-quintic-fields-nov18.md)|
|6|487|[Sextic fields](zhao-degree6-fields-nov18.json)|
|7|68|[Septic fields](zhao-degree7-fields-nov18.json)|
|8|2|[Octic fields](zhao-degree8-fields-nov18.json)|

Among all these fields, 229 are abelian and 233 are Galois. The remaining four Galois fields are normal closures of cubics. Under GRH the spectral sum is the unconditional analytic value \(b_K=2\xi_K'(1)/\xi_K(1)\), with the pole-cancelled completion. A small value of \(b_K\) independently excludes real zeros that could obstruct the converse from positivity. The [sign-equivalence proof](zhao-field-sign-equivalence-nov18.md) proves the individual and positive weighted criteria. Without an independence or phase argument the classification of the strict spectral bound does not classify eventual signs for all fields outside the inventory. [Degree and discriminant bounds](zhao-field-catalogue-bounds-nov18.md) · [Direct unconditional comparison](zhao-field-unconditional-replay-nov18.md) · [Complete catalogue sources](zhao-field-catalog-source-nov18.md)

These proposed mathematical results and finite certificates have internal checks. They leave the truth of RH open.
