# RSC26 validation and scope

## Accepting computation

The accepting range is Y=3,7,15,31,63,127,255,511,1023,2047 and output through 4,194,303. All q=1,2,4 partitions are complete inclusive integer partitions. Reports use denominator 2^128 and integer outward rounding; displayed decimals play no role in acceptance. Exact Fraction algebra is used for the completion and local identities.

produce.py uses a prime/multiple sieve and forward cumulative arithmetic. verify.py imports no producer: it trial-factors the prefix through 2047, forms the product convolution, and uses the classical Newton identity to reconstruct every one of the 4,194,303 output coefficients. Their full coefficient digests must match. It then uses 176-bit cumulative calculations to validate all 31,546 stored endpoint occurrences and every complete input/output E,F,eta,A state. Overlap across stages is counted in the endpoint number.

The verifier re-expands every endpoint-only physical and innovation certificate, including the completion term and the final simultaneous-cutoff gate. It additionally performs 136 literal exact-Fraction cell checks through Y=15. The large Q coarse/residual diagnostics are authenticated producer reconstructions, not a second full original-product Gram enumeration. The Q source identity is independently tested exactly at Y=7, and 600 residual kernel pairs including above-endpoint columns are checked exactly in algebra.py. This limitation does not enter the endpoint physical/innovation gain certificate.

The accepting gate for every 1<=Y<=2047 comes from the maximum-range endpoint upper bound on F, NOT from assuming A is monotone or interpolating the displayed ten cutoffs. The exact upper numerator, at denominator 2^128, is

    632332958097321075858201468775385532899.

The certificate proves (1+2V)^2<32. Measured fine-scale energies are reported for discovery only and are not substituted into the worst-case bound.

## Proof and regression checks

algebra.py checks all 243 ternary words of length five on every subinterval (3,645 local variance identities and ramp bounds), 600 polarized product-column identities, two capped nonnative Newton controls, and a finite fifteen-good-prime inverse Euler model of E_17 through 4095. The model omits other good and bad factors; it is not full L-function data. Point counts are exact.

Sixteen unittest methods cover integer endpoints/refinement, the local identity with nonzero history, uncentered non-equality, sharp ramp formulas, above-endpoint columns, full balanced product cancellation, the missing unbalanced moment term, exact reconstruction and excluded square endpoint, direct endpoint certificates, an omitted-completion mutation, finite-versus-unbounded range gates, fake source inversion failure, elliptic weight mismatch, signed interval division, twelve altered reports, integer/float/bool aliases, duplicate keys and nonfinite JSON.

Report authentication is part of acceptance. EXPECTED.json contains canonical semantic SHA-256 digests; replay.py reconstructs each report and checks its digest before running the tests. verify.py alone does not independently check every optional large Q diagnostic field. Twelve changed report variants are refused by the authenticated acceptance layer. This is stated rather than treating a receipt as an independent re-proof of every number.

Both implementations share core.py's interval primitives and root grid. Both have the same author. There is no independent human mathematical acceptance, Lean/Metamath proof, global zero computation, or whole-repository validator run.

## Draft failures and excluded ranges

An early completion prototype used an integer default divided by k, accidentally introducing a floating zero for absent entries. The exact reciprocal-moment guard rejected it. The default was replaced by Fraction(0) before the final reports.

A larger Y=4095 experiment was attempted. An early dense-table process failed; after sparse endpoint storage, its producer finished, but its separate complete verification did not finish within the execution constraints. That range and its reports are NOT part of this packet's acceptance, finite claim, or publication. The final default Y=2047 range passed both complete implementations. No extrapolation to the discarded larger range is made.

## Reproduction contract

From this directory, run

    python -S -B replay.py
    python -S -O -B replay.py

The executable code uses only the Python standard library, needs no network, and writes reports/ locally. The sixteen tests use unittest assertions and explicit ValueError guards, not bare Python assert statements disabled by optimization. SHA256SUMS authenticates committed files; generated full reports accompany the chat archive and can be regenerated from the committed programs.

Publication receipts, exact Git object comparisons, fresh-directory replay logs and archive hashes are recorded separately after the final files are frozen. The paper proofs remain PROPOSED component mathematics and the global coarse-energy bound remains OPEN regardless of successful computation.
