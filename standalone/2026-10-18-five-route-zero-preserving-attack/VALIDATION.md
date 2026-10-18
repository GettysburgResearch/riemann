# Executed finite validation and its limits

The full accepting runs contain **20,279 explicit predicates per interpreter
mode**, including repeated coefficient, matrix and parameter guards. This is
not a count of independent analytic theorems or actual zeros.

| Lane | Predicates | Complete finite scope |
| --- | ---: | --- |
| Quadratic fields | 11,172 | Eleven actual fundamental discriminants, all convolution coefficients through 256, ramified primes, the entire discriminant family through 65,536, 26 character moduli with complete prefix tests, four weighted-array error tests. |
| Paired probes | 2,221 | Orders 1--8, complete 40-term rational source rescalings, 512 integer separation tests, finite positive mod-3/mod-4 paired terms, synthetic multiplicities 1--12. |
| Strip compactness | 652 | Full three-point/product laws through moment 20, exact reciprocal quadratic roots, seven rare-jump parameters with exact variance, finite disk-tail factors. |
| Native Newton | 5,273 | Every old product for Y=2,...,24, all complete coefficients through Y^2, square/cube masks, above-output witnesses, full root-budget and conditional exponent checks. |
| Determinants | 961 | Complete cycle polynomials through 32, rational primitive projectors and positive minors through 9, outward elementary-function controls, 34 all-mass comparisons including ten target-scale masses, complete unit-sensitive rearrangements. |

All normal and optimized outputs match byte for byte. CHECKS.json binds the
SHA-256 of EACH complete lane output; `python -B verify.py --lane <name>`
regenerates it, including every directed mass enclosure. Full reports also
accompany the conversation delivery as separate verification details.

The determinant comparisons use the positive totient series through 128 and
an explicit bound on its entire omitted tail. No tail is sampled or set to
zero. Rational log, square-root, arctangent and Machin-pi enclosures use a
96-bit outward dyadic grid. This new backend is written by the same author;
it is not an independently commissioned implementation or a formal kernel.
It compares the exact cyclotomic determinant polynomials with the positive
infinite-series representation, not with fitted zeta-zero data.

## Twelve executed negative controls

Each mutation is a separate optimized Python process, required to exit with
code 2 and its specific REJECT gate. MUTATIONS.json records the gates:

- treating ramification as splitting; deleting inverse-kernel prime powers;
- dropping probe normalization; using commensurate probes;
- wrong probability normalization; failing to compensate rare-jump variance;
- deleting above-output products; failing to pay the core root-norm cost;
- losing the square-scale factor two in the recurrence;
- deleting prime powers from the determinant; using the wrong mass coordinate;
- omitting the unit correction from the full divisor rearrangement.

The accepted replay does not count a generic crash as a successful negative
control. Exact gate text, return code and absence of stdout are required.

## Runtime and unsuccessful execution attempts

An early combined report command exceeded a 20-second tool limit. Subsequent
combined attempts also timed out at 120 and 90 seconds with ordinary site
startup enabled. They are NOT counted as passed. Standalone accepting lanes
and the direct lost-unit corruption completed; a progress-enabled parallel
run completed all five ordinary/optimized lane pairs and ten mutations before
its outer timeout while two heavier corruption subprocesses remained.

The final runner isolates children with `-I -S -B` and explicitly places only
this packet on their module path. This excludes unrelated site/startup hooks;
it does not change the mathematical functions or bypass any accepting gate.
The complete final five-lane/twelve-mutation generation then completed, and
was repeated after the last small-field extension. Parallel children are
finite verification jobs, NOT separate research agents.

The positive B-series finite cutoff was reduced from 512 to 128 to shorten
replay. Its exact full-tail allowance increases correspondingly and remains
inside every accepting budget. No mathematical error bound was relaxed and
no finite comparison was removed; ten actual target-scale masses were added.

## Mathematical review boundary

The same author wrote the five notes and tests. Self-review corrected the
prior moment-only compactness idea, protected the common field channel,
retained ramification and divisor tails, separated sparse-cut from all-Y
recurrences, and recorded the determinant's larger bulk-subtraction tradeoff.
These are scoped complete proposed arguments, not externally accepted proofs.

No separate agent or human mathematical referee was launched. No Lean build,
upstream quasi-RH proof reconstruction, physical CT integral computation,
actual L-value or zero census, whole-repository validator or remote CI was
run. The five critical upper/feasibility estimates remain open. Publication
and finite replay do not establish an improved zero-free half-plane.
