# Heat-trace calculation: current status after prior-art review

Status: **REVIEWED INDEPENDENT DERIVATION, STRICTLY WEAKER THAN LOCATED PRIOR ART**.  
Date: 2026-10-30. This status supersedes the drafting-time status in the frozen report.

The [frozen report](report.md), SHA256 `5d37be05f210cad78c1d03d7aafff2eb33e9b0cfbec11b7e79bfd59d03dd27a5`, was independently reviewed by all three research agents. Its analytic argument and conservative constants passed those reviews. The report is retained unchanged so that the reviews refer to exactly the text they audited.

During the overlap check we located the same zero heat trace in Nicholas G. Polson and Vadim Sokolov, *Computing the Riemann Hypothesis: Thorin Measures, Pólya Densities and Hitting Times*, repository commit [`f7fdd71`](https://github.com/VadimSokolov/computing_rh/tree/f7fdd71f29826a69d84f7d1d416768fdfc02d477). The exact primary statement is [chapter source, label `ps:thm:free`](https://github.com/VadimSokolov/computing_rh/blob/f7fdd71f29826a69d84f7d1d416768fdfc02d477/ch/ch12.tex), Theorem 5.1.16 in the pinned book's cross-reference record.

That source states all-order alternating derivative positivity on 0<t<=1.70 and all-time positivity through order 1.70(H−23)^2, with H=3×10^12, exceeding 1.52×10^25. Our calculation supplies a much smaller time interval and the all-time endpoint 1.125×10^18. Therefore it is **not a new derivative-order frontier**. We inspected the source theorem and proof but did not rerun its large ball-arithmetic computation.

The retained value of this appendix is its elementary saddle-phase proof, its explicit dependence on the zero-count inputs, and the independent countermodel showing that all-order signs on a short time interval do not imply complete monotonicity on the whole positive axis.

Reviews:

- [Arithmetic review](../arithmetic/REVIEW_HEAT_TRACE.md).
- [Dynamics review and local/global countermodel](../dynamics/REVIEW_HEAT_TRACE.md).
- [Positivity review, source comparison and normalization audit](../positivity/REVIEW_HEAT_TRACE.md).

The [constant replay](check_constants.py) checks 28 exact rational endpoint inequalities. It does not evaluate the enormous derivative orders, authenticate an external zero verification, or prove the analytic arguments by itself.
