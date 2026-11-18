# Robin1984: scoped original-source audit

2026-11-17. Actual scan inspected, not abstract-based. Whole27-page French article read; local technical reconstruction only. Source provenance/hashes and access failures are in sources/robin_round2/source_manifest.json.

## Inspected claims with no issue found in reconstructed portion

1. **Threshold/quantifiers:** Theorem1,p188, strict inequality for every integern≥5041; no claim for1≤n≤5040. Source §3Proposition3,p204, lists27 positive exceptions below the threshold.
2. **Sharp versus rounded constant:** Theorem2,p188,0.6482… with equalityn=12; abstract's0.6483 is a convenient rounded strict upper bound. Exact sharp constant is forced by equality:K=(7/3−e^γloglog12)loglog12.
3. **Ties:** CA definition is a non-strict global maximum,p189. Thep190 proposition explicitly permits four maximizers at coincident prime thresholds. The disjoint-threshold assertion is not assumed proved.
4. **Sparse endpoint reduction:** §3Proposition1,p192, follows unconditionally from h″(t)>0 for h(t)=εt−loglogt and the common supporting parameter. It is valid across adjacent CA values including tie choices. Finite ranges need bracketing endpoints and a separate startup check if their left endpoint violates the inequality.
5. **Converse scale:** §4Proposition1,pp204–205, is two-sided oscillation on CA integers, for everyb∈(1−Θ,1/2). The deterministic CA correctionO(x^(−1/2)/logx) is negligible at this scale. Nicolas's1983 input is not independently proved in this track.
6. **Lagarias transfer:** Positive CA excess dominates7n/logn. Thus all sufficiently largeCA values suffice globally to test Lagarias, but no finite endpoint certificate for its right side was established.

## Small printed-formula issue: awaiting independent confirmation

Onp195,§3Lemma1, the scan prints the leading denominator `log n` in

    F_(ρ,n)= n/(n−ρ) · x^(ρ−n)/(log n)+r_(ρ,n).

The intended denominator is `log x`. Independent integration by parts, the n=1 application, and the paper's subsequent formula onp197 all requirelogx. The cropped original is `sources/robin_round2/lemma1-bottom.png`. This is a local notational/typographical inconsistency, not evidence against the principal theorem. Parent was asked to check it independently before elevation. No public characterization of the theorem as erroneous is warranted.

For completeness, with x>1, n≥1 andReρ<n, put a=ρ−n. Directly integrating twice gives

    ∫_x∞ t^(a−1)(n/logt+1/log²t)dt
    = n/(n−ρ)·x^a/logx
      + ρ/(ρ−n)²[−x^a/log²x+2∫_x∞t^(a−1)/log³t dt].

The printed remainder has the correct negative sign. The genericρ∈C wording must be read with convergence conditions; in its actual RH applicationρ is a nontrivial zero withReρ=1/2<n. This observation narrows the integral domain and is not a newly discovered gap in the application.

## Important unverified dependencies

- Nicolas,Petites valeurs de la fonction d'Euler(1983),Theorem3 and its Landau-oscillation input.
- The historical six-exponentials argument controlling coincidentCA thresholds.
- Source computations of2347CA values and all explicit finite constants/tableentries.
- The integrated explicit-formula interchange in its original external dependency; the decay mechanism was inspected but every limit was not fully re-proved.
- Corrections/version search: selective searches for Robin1984 errata/corrections found no authoritative erratum in this run; absence of a correction has not been established. The archived scan is not a version history.

## No additional mathematical claim about RH

The local reconstructions recover known proof mechanisms and a direct sparse Lagarias corollary. Novelty has not been established. Neither a proof nor a disproof ofRH results.
