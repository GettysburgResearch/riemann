# Prior-art and source-status ledger

Status: **TARGETED PRIMARY-SOURCE SCREEN, NOT AN EXHAUSTIVE NOVELTY CERTIFICATE**. Date: 2026-10-30.

## Source inputs and direct overlap

| Source | Exact identity / inspection depth | Consequence for this packet |
|---|---|---|
| Suvrit Sra, *On some positivity properties of the Riemann Xi function* | [Author-site v2](https://suvrit.github.io/papers/riem-xi/), released 29 October 2026; [author PDF](https://suvrit.github.io/papers/riem-xi/riem-xi-v2.pdf), Git blob `f98e0bd0d2d1353245a482581ffa74580c644996`. Full PDF text inspected, especially Proposition 3.3 and Appendix C. External computation not rerun. | Reciprocal-density positivity, log-concavity, finite PF extraction, explicit counting and verified-height inputs are attributed to this source. Our finite factor-removal theorem extends its tilted-residual mechanism. |
| Nicholas G. Polson and Vadim Sokolov, *Computing the Riemann Hypothesis: Thorin Measures, Pólya Densities and Hitting Times* | [Repository at f7fdd71](https://github.com/VadimSokolov/computing_rh/tree/f7fdd71f29826a69d84f7d1d416768fdfc02d477), 28 October 2026; README edition 1, version 1.4.1; DOI [10.5281/zenodo.23741450](https://doi.org/10.5281/zenodo.23741450). Exact relevant TeX inspected, full book and large certificates not audited. | Directly overlapping and stronger heat-trace derivative range. Our heat calculation is demoted to an independent weaker appendix. The book already treats finite-test limitations. |
| Polson–Sokolov, `ch/ch12.tex` | [Pinned source](https://github.com/VadimSokolov/computing_rh/blob/f7fdd71f29826a69d84f7d1d416768fdfc02d477/ch/ch12.tex), blob `bf3b3bd9e964c4358e48267c3831450c8eaac2f2`, label `ps:thm:free`. Same trace and time normalization as our H. | The source states all-order signs on 0<t<=1.70, and all-time signs through 1.70(H−23)^2>1.52×10^25 for H=3×10^12. We have not independently rerun its ball-arithmetic prime-power calculation. |
| Polson–Sokolov, reciprocal-density chapters | [polya3.tex](https://github.com/VadimSokolov/computing_rh/blob/f7fdd71f29826a69d84f7d1d416768fdfc02d477/ch/polya3.tex), blob `8afa33439d7d30379279f044c0a77c958767742e`; [polya6.tex](https://github.com/VadimSokolov/computing_rh/blob/f7fdd71f29826a69d84f7d1d416768fdfc02d477/ch/polya6.tex), blob `e70ac40d1a6db71e08e26c385f128943419ee51e`. Relevant complete sections inspected. | The explicitly floating-point PF2 certificate is not an exact analytic certificate. The `pol:thm:approxpf` estimate is uniform density/derivative closeness, not a total-variation estimate. No sequential factor-removal induction was found in the screened sections. |
| R. C. Vaughan, *Some applications of Montgomery's sieve* | [Publisher record](https://doi.org/10.1016/0022-314X(73)90059-0), Journal of Number Theory 5(1), February 1973, pp. 64–79; metadata and abstract inspected. Full theorem text not inspected here. | Classical shifted-prime/totient means are prior-art territory. The weighted-prime lemma in our profile note is independently proved from classical PNT and Brun–Titchmarsh; it is not presented as a newly discovered mean-value phenomenon. The exact compensator application remains a limited-screen research construction. |

## Existing repository programmes

The frozen baseline is [`f99d9e3908dde4865377c75d9ca051c1f545bf4f`](https://github.com/GettysburgResearch/riemann/tree/f99d9e3908dde4865377c75d9ca051c1f545bf4f). The following existing objects were read or supplied to the lane authors before judging overlap:

- [PROGRAMMES.md](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/PROGRAMMES.md), [OPEN_CUTS.md](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/OPEN_CUTS.md), and [CURRENT_RESULTS.md](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/research/integrated/CURRENT_RESULTS.md).
- [Issue #740](https://github.com/GettysburgResearch/riemann/issues/740), the existing off-line propagation programme. The arithmetic detector is a specific construction within that programme, not a renamed discovery of propagation.
- The [prior literature repository map](https://github.com/GettysburgResearch/riemann/blob/56c62d6e63a0111074c9837aaef30112792abb72/standalone/2026-10-30-literature-pass/REPO_MAP.md), including exact heads of PRs #1017, #1019–#1023.
- Existing derivative-entry/descent, finite Weil/Pick positivity, and principal-conductor extraction gaps. The dynamics and arithmetic lanes explicitly preserve these distinctions.
- Existing Nyman–Beurling work in PRs #804 and #805; this route was not reintroduced as a fresh lane.

Targeted repository searches for the Artin constant, totient progression profile and p²−p−1 did not find an existing occurrence in the searched results. This is not proof that every branch, comment or historical file lacks the construction. Web search was intermittently unavailable early in the run and recovered later; later source findings supersede earlier availability comments in frozen reports.

## What is and is not being claimed as a contribution

The arithmetic contribution of this pass is the combined detector contract, sharp sign obstruction, exact conductor weights, and explicit profile/compensator with its open error estimate. Character orthogonality, Euler products, divisor switching and the underlying prime mean-value methods are classical.

The positivity contribution is the explicit removal invariant, source-qualified finite extension and exact failure-of-iteration model. Sra's finite factor extraction and Polson's infinite-divisibility framework are prior inputs. The generic fact that finite positivity tests do not settle RH is already known.

The dynamics contribution is a concrete order-matched hidden quartet, exact critical-value/Jensen gate and solvable root-flow model. The high-derivative/descent distinction and heat-flow approach are existing theory and repository context.

The heat-trace calculation is an independently obtained weaker proof. Neither its range nor its broad saddle idea is asserted to be novel relative to the pinned book.

An absence in these targeted searches is not a global priority claim. The source ledger is deliberately narrower than a publication-level historical survey.
