# Three questions on Mertens means and prime biases

The November 18 branch proposes answers to questions in §8 of Tianyu Zhao's 2025 paper. All three use exact prime statistics. Their hypotheses and the extent of the classifications differ. [Original paper](https://doi.org/10.1007/s40993-025-00640-y)

**The third Mertens product.** The proposed proof removes the remaining regularity assumption when zeta zeros approach the line of real part one. In that case the integrated normalized Mertens product error has positive and negative excursions of size \(X^{1-o(1)}\). The arithmetic positivity for every \(X>2\) is therefore equivalent to RH. The argument retains the finite-product prime-power correction. One proof imports Zhao's Lemma 10; a separate Gaussian and power-sum proof derives the required lower bound directly, including multiplicities and clusters. A refinement gives both signs in every sufficiently late shrinking logarithmic window. [Criterion](zhao-third-mertens-nov18.md) · [Direct proof](zhao-native-oscillation-nov18.md) · [Local envelope](zhao-sharp-envelope-nov18.md)

**Integrated prime counts.** For quadratic characters, under individual GRH, central nonvanishing, and independence of the distinct positive ordinates, exactly 19 fundamental discriminants have the eventual negative sign. The sufficiency direction for those 19 needs only their own GRH. The paper's proposed inclusion encounters the unconditional counterexample \(-59\), which is in Table 3. Its phase-zero Fourier value under GRH lies below \(-2/3\), and an off-line zero would force sign changes by the separately verified absence of real zeros in the relevant segment. Through conductor 10,000 the individual computations give 6,067 unconditional sign changes among 6,086 discriminants; for the other 19 eventual negativity is equivalent to individual GRH. For primes in residue classes, joint GRH, absence of central zeros and the stated independence of inducing ordinates give the full classification in the progression note. Unconditional phase certificates, density results and bounds requiring fewer assumptions are separate. [Discriminants](zhao-bias-classification-nov18.md) · [Progressions](zhao-progression-classification-nov18.md) · [Unconditional results](zhao-bias-unconditional-nov18.md)

**Prime ideals.** Exactly **2,580 number fields up to rational isomorphism** satisfy the unconditional strict inequality
\[
 b_K=2\xi'_K(1)/\xi_K(1)<2,
\]
where \(\xi_K\) is the pole-cancelled completed Dedekind zeta function. No field has equality. Under the Riemann hypothesis for that field this is precisely Zhao's spectral condition \(B_K<2\). For every field on the list the proposed proof makes its own Riemann hypothesis equivalent to eventual positivity of the integrated prime-ideal harmonic error. Independent direct contour evaluations recover the same fields without assuming GRH for the analytic predicate. The degree cannot exceed eight. Published complete field tables, exact prime ideal decompositions, finite explicit formulas and rigorous contour evaluations supply the proposed classification.

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

Among all these fields, 229 are abelian and 233 are Galois. The remaining four Galois fields are normal closures of cubics. A small value of \(b_K\) independently excludes real zeros that could obstruct the converse from positivity. The [sign-equivalence proof](zhao-field-sign-equivalence-nov18.md) proves the individual and positive weighted criteria. Without an independence or phase argument the classification of the strict spectral bound does not classify eventual signs for all fields outside the inventory. [Degree and discriminant bounds](zhao-field-catalogue-bounds-nov18.md) · [Direct unconditional comparison](zhao-field-unconditional-replay-nov18.md) · [Independent unconditional cubic and quartic tests](zhao-low-degree-unconditional-nov18.md) · [Complete catalogue sources](zhao-field-catalog-source-nov18.md)

Twelve [quaternionic fields outside the census](zhao-quaternion-bias-nov18.md) each have a central zero of multiplicity exactly two, no real off-critical zeros, and \(b_K<18\), unconditionally. The smallest example has \(12.7594<b_K<12.7596\). For each of the twelve, eventual positivity of the integrated prime-ideal harmonic error is equivalent to its own Riemann hypothesis. Global Dedekind GRH thus gives at least 2,592 eventually positive fields. The [least positive margin](zhao-minimum-margin-nov18.md) among the 2,580 fields in the strict census is approximately 0.00003315475517, attained by a unique quartic field of discriminant −15,788. The [field product argument](zhao-field-product-nov18.md) extends the third-product equivalence to all 2,592 fields.

For at least 188,960 of the 300,000 distinct cyclotomic fields with conductor at most 400,000, the integrated harmonic error and the integrated product error both change signs infinitely often. This conclusion is unconditional. The proof uses 192 certified character witnesses and Platt's published low-height verification. [Cyclotomic sign changes](zhao-field-minus163-nov18.md) · [Low-ordinate argument for general fields](zhao-field-low-zeros-nov18.md)

These proposed mathematical results and finite certificates have internal checks. They leave the truth of RH open.
