# What was actually checked

The analytic proof and checker have the same author. No independent mathematical referee, separate agent review, formal proof build, deep upstream reconstruction, actual L-value evaluation, zero census, full-repository test suite or remote CI is claimed.

## Exact accepting executions

`python verify.py` and `python -O verify.py` reproduce CHECKS.json byte for byte. The report contains 35,766 counted finite predicates, many of which are repeated parameter guards; this is a coverage count, not a confidence score or a number of analytic theorems.

The primitive finite coverage is:

- Two elementary Mobius constructions agree for every rational integer through 1,024.
- Complete residue arithmetic in F_7 and F_13 at all six character powers, with exponent-zero NONUNIT values still zero. Their product is used in finite convolution fixtures. These are local convention checks, not a full globally compatible number-field character census.
- Every integer n-th-power decomposition through 1,024 for n=3,4,6,8; literal sixth-power masks include shared factors.
- Fifteen complete flat-cutoff convolution cases, with every coefficient through the complete product cap retained, and full small mollifier cubes. The rational cutoff in the checker is not smooth; it checks the finite algebra only. The analytic theorem uses a fixed smooth cutoff and the required Mellin estimates in prose.
- Seven polynomial identities in the formal indeterminate n are verified by exact coefficient arithmetic. The all-n proof is not inferred from integer sampling. Additional rational parameter checks cover n=6,...,128, moment orders through 40, and declared conductor fractions.
- Three-factor Holder on all specified rational two-entry arrays. A complete grid of Gaussian-rational L and M values checks the pointwise capped-transfer inequality, including L=0.

## Corrupted executions

Seven actual separate optimized Python processes are run by run_mutations.py. The expected gates are recorded in MUTATIONS.json. They reject erased nonunit zeros, replacing conjugate products by ordinary products, a false shared-prime coprimality condition, a wrong cutoff dilation, an insufficient pointwise-mollifier budget, loss of the actual conductor prefactor, and assigning a zero-valued reciprocal summand instead of the prescribed cap at an L-zero.

The pointwise-mollifier bound is VALID but too weak for the claimed exponent. Its rejection does not refute that old bound; it rejects using it as a certificate for the stronger new conclusion. The corrupted processes mutate specified formulas inside the independent checks; they do not prove the new infinite theorem by failing.

## Development and proof checks

A numerical linear-program scout using scipy first found a 7/9 candidate from unbalancing X alone. That candidate was superseded by the written 11/15 argument using joint M6/R2/R4 moments. The optimizer is not an input to acceptance or the proof. The final arithmetic equalities and limited-envelope lower certificate are exact.

During prose review, an endpoint in the shorter-mollifier inequality was recognized as non-strict at n=6,a=1/2; the final proof states nonpositivity, not a false strict margin.

The cap removal was attempted but NOT achieved: at an actual zero the relative error is one and the reciprocal summand is U^theta. Since f_n>0 and theta<1, neither bound excludes one prescribed zero. The limited f_n envelope calculation is not an arithmetic no-go theorem and not a lower bound on the actual error.

## Integrity and publication

MANIFEST.json binds all payload files except itself by SHA-256, length and Git blob ID. replay.py authenticates it before executing both checker modes and all seven mutation subprocesses. A fresh ZIP extraction and an add-only minimal Git-fixture application are replayed separately; the final outer delivery receipt records their outcomes. The fixture is not an authenticated full repository checkout. No inherited source bytes were edited.
