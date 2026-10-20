# Type-I source and scope audit

Date: 2026-10-20. Base repository source:
\(7f6ff9dae8d3473a5835a5cbe7308148b8b3c1a0\).
The new files contain proposed mathematics with the file-level reviews
identified below; they are not certified upstream theorems. No novelty
claim is made.

## Load-bearing primary source

Dunn and Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*,
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3),
14 May 2024.

The downloaded HTML has SHA256
\(\texttt{3949e0f0ae87808d84fe02c12a3b68c5b66aa8d967d8ecb5e1605f1d985b956d}\).
This is also the source hash recorded by the inherited angular packet.

| Source location | Imported content | Use and limitation |
|---|---|---|
| (1.4), (1.5), (2.2), (2.3) | Cubic reciprocity, supplementary laws, Gauss support and twisted multiplicativity | All common-prime zero extensions retained. |
| (5.7), (5.13), (5.14), (5.73)--(5.79) | Actual theta and dual coefficients | Gives full cube support and absolute coefficient mass. The derivation (5.79) controls the ramified index; the apparent repeated ramified power in the printed (5.67) is not used literally. |
| Lemma 5.2, Lemma 5.3, Proposition 5.1 | Primitive periodic twist transform and angular Mellin functional equation | The quadratic extension verifies primitive Fourier support explicitly. This import is broader than cubic twists. |
| Lemma 5.4 | Cube completion for primitive cubic twists | General-character completion in the quadratic note is proved from the theta coefficients; it is not claimed to be the statement of this lemma. |
| Proposition 5.2 | Completed cubic functional equation; no main pole for nonzero angular order | Used at a fixed nonzero angular order. The cubic-only note follows its stated normalization. The quadratic note keeps the raw Mellin normalization, allowing fixed powers of 3 to rescale the dual weight. |
| Theorem 9.1 | Unconditional cubic large sieve | The squarefree row and column restrictions are checked each time. No conditional large-sieve improvement is imported. |

The conditional cubic-only result additionally uses the fixed-character
zero-free reciprocal argument from the inherited
[ANGULAR_TYPE_I.md](../../2026-10-20-angular-hecke-continuation/ANGULAR_TYPE_I.md).
The quadratic conditional variant instead states the exact
conductor-uniform reciprocal estimate it needs in (Q3). A separate
zero-free region for each character, with uncontrolled constants, is not
enough for that variant.

## Recent related sources checked for scope

These sources informed the research direction but their spherical
estimates are **not** imported as angular estimates in this directory.

David, de Faveri, Dunn and Stucky,
[*Non-vanishing for cubic Hecke L-functions*,
arXiv:2410.03048v2](https://arxiv.org/html/2410.03048v2),
3 March 2026. HTML SHA256:
\(\texttt{f2cba1df0d57760886d59f8f70400843d008877543d88f9d5309efd5db227a2c}\).
Lemma 6.6 gives a strong mean square for additive Kubota twists with the
spherical archimedean type. Its printed statement has no nonzero angular
parameter. Applying it to the current angular block requires an actual
angular functional-equation/mean-value argument.

De Faveri, Dunn and Hoffstein,
[*Non-orthogonality of the cubic and quartic large sieves via
Rankin--Selberg*, arXiv:2607.07911v1](https://arxiv.org/html/2607.07911v1),
8 July 2026. HTML SHA256:
\(\texttt{9bea09caf792c531940c313c6a0bcc1d1512e52020e0865f959fe37725659a14}\).
This proves unconditional nonorthogonality and discusses a
Lindelof-on-average input. It does not license an unstated growing
angular or mixed quadratic twist in the current object.

OpenAI, *An unconditional first moment for cubic Gauss sums*,
25 September 2026,
[angular section source](https://raw.githubusercontent.com/openai/math/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex).
The fetched section has SHA256
\(\texttt{f14a7c1c4f0b19b70d6705c8a2adcb658bfbc77814edb61cd57edb2465f38510}\).
The URL follows a mutable branch, so this hash identifies only the exact
fetched comparison text. Its angular Type-I treatment was checked as a
sanity comparison, not used to prove any estimate here.

## What the finite checker proves

The companion verify_type_i.py uses exact integer arithmetic in
\(\mathbb Z[\omega]\) and exact rational exponents. Its receipt
verification.json binds the three mathematical notes and checker by
SHA256. It tests the finite primary unit group, the additive profile
formula, and 432 truncated two-prime instances of the formal dual
identity with nontrivial reciprocity phases.

It does not authenticate automorphic identities from the primary source,
prove analytic continuation, verify a contour shift, certify
finite-profile closure, or establish an infinite mean-value theorem.
The analytic proof remains a mathematical review task.

## Smallest remaining interfaces

For the cubic-only \(4/5\) balanced estimate, the load-bearing new step is
the free-split combination of the full dual mass with the original
cubic large sieve. An error in either coefficient normalization or the
cube summation would invalidate that estimate.

For the quadratic extension, the additional load-bearing step is the
exact primitive transform (Q9). Its conductor factor is kept explicitly.
The binding sextic terminal row has a larger quadratic conductor than
the short prime variable, where the estimate does not provide the
required saving.

The stronger self-absorption argument additionally uses
[FINITE_PROFILE_CLOSURE.md](FINITE_PROFILE_CLOSURE.md), with the actual
source cusp rows 22, 26, 27. Its exact cyclotomic minor has
\(M^*M=3I\); the full 27-cusp reflection and the Mellin extraction give
the four-channel closure. The independent source audit is
[AUDIT_CUSP_REFLECTION.md](../mixed/AUDIT_CUSP_REFLECTION.md).
The mean-value argument itself is written in
[ANGULAR_SELF_ABSORPTION.md](../average/ANGULAR_SELF_ABSORPTION.md).

The separate verify_profile_closure.py checker exhausts 486 actual
minor coefficient cases and 2,430 source-table support cases. Both
checkers use explicit failure branches, so optimization does not remove
their checks; ordinary and optimized Python runs give the same receipts.
Their scope remains finite algebra. Analytic continuation, contour
arguments and absorption are the accompanying mathematical proofs.
