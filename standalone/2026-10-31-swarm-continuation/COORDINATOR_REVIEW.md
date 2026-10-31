# Coordinating mathematical review and composition boundaries

Reviewer: coordinating agent, 2026-10-31. This records my mathematical review of the three research lanes and my authorship of the local certificate. It is additional internal scrutiny, not external refereeing or formal verification.

I read the full anchor, cofinal Bessel, and cosine/native manuscripts and reconstructed their load-bearing arguments. I contributed the exponential cross-projection observation used by the anchor proof and the exact-prefix obstruction discussion in the native lane; those portions are therefore not independent author-versus-reviewer checks by me. The separate reviews identify their own independence and bind the final file bytes. I authored the local-gate note and checker, which were reviewed by the Bessel lane.

## Anchor lane

The exact Laguerre/exponential coefficients give the geometric cross-projection with exponent `-2(b+c)(N+1)/a`, fixing the support length at **2L**. The contraction/density argument and weak-to-strong projection argument are valid. The weighted dilation formula gives a Schur estimate with the correct prefactor and limiting exponential constant.

I checked the complete-prime majorant at exponent `(1+eta)/2>1`, the zero action of a delay at or beyond the support endpoint, and the distinction between strong and norm convergence. The exact actual-source form has the correct digamma constant, kernel, pole-product factor, and prime weight. The moving-minimizer proof uses the logarithmic Fourier coercivity to obtain precompactness and cannot be replaced by a bare strong-operator argument. The liminf direction, support of the limit, exponential-weight upgrade, and lower semicontinuity are consistent.

The threshold shift norm is a finite-chain adjacency norm. At integral length/delay ratios, the exceptional longer chain has measure zero; the ceiling formula in the manuscript handles that endpoint correctly. The form-domain approximation needed for continuity is supplied explicitly. No unbounded positive-window theorem follows from continuity.

For the budget obstruction I checked the sign of the trace lower bound, the alternating Fejer vector, the separation of the complete remainder from the logarithmic model, and the endpoint digamma/Mangoldt inequality. The rational constants give the claimed `29/12`, and the explicit log-2 lower bound makes the threshold 128 strict. The two-dimensional control retains positivity of every matrix while its positive-part estimates fail; it is a counterexample to the estimates, not to positivity.

The independent Bessel-lane review reached the same conclusions and replayed all 606 exact checks. The relocated normal/optimized coordinator replays are recorded separately.

## Cofinal Bessel lane

I checked the theta cusp sector at `x=+/-i`: the square-root map puts the theta cusp parameter in a closed right sector, so all algebraic derivative losses are absorbed by its exponential flatness. The endpoint strip Fourier bound is therefore available for the exact exponential weight needed by the angular sum. It does not assert analytic continuation across the cusps.

The Skellam mean and variance have the normalization needed for the source sample `w(n/a)`. The good/bad split cancels the full first-order expectation before estimating the exceptional part. The probability and first-moment bounds retain integrable tails after the change of variables to the physical coordinate. The finite-cutoff argument includes the full omitted range. These justify the quantitative complete-source rate and the explicit logarithmic cutoff schedule.

I independently derived the companion integral by symmetrizing the modified-Bessel I integral. Its sine-times-sinh term has a plus sign before substituting imaginary order. The Fourier representation of the angular sum gives a uniform `1/a` error with the endpoint Fourier estimate. The finite-order cutoff exponent is exactly the stated H(S), which is negative for S at least three.

The radial Wronskian has value one. Inverting it gives both normalized cancellation identities and the exact rational residue formula. The leading large-a constants give `pi exp(-2a)` for the zero separation and `2pi a exp(-2a)` for residues. The simple-zero and nonzero-companion hypotheses are essential. The uniform imaginary-part quotient outside target-zero neighborhoods uses a valid short vertical-segment argument near the real axis.

I also reconstructed the appendix integration by parts and the value at energy `-1/16`. The decaying auxiliary function must subtract the single growing exponential, as in the final manuscript; subtracting a symmetric pair would introduce a nondecaying boundary term. The final proof uses the correct auxiliary function. The negative-axis controls prevent a global anti-Herglotz shortcut but leave the local problem open.

A separate reviewer subsequently checked the full manuscript, prior normalization, and exact structure checker without editing them. Ordinary diagnostics were never used as premises of these analytic conclusions.

## Cosine/native lane

I checked the multiplier order, its central unit-modulus normalization, and the order of cosine/inversion in the concrete logarithmic-coordinate operator. The transform is not claimed to preserve positivity or multiplication. The reciprocal-cell embedding, its weight, and the `2/pi` integral normalization are consistent.

The finite summation-by-parts calculation produces the harmonic compensator `y log(n)/n`; it cannot be dropped when passing to the full series. The dilation cocycle and full infinite cosine-series identity follow with the same coefficients. The transported zero-functional uses a smooth extension on the unused negative half-line; its Schwartz transform can be divided by the polynomially bounded reciprocal multiplier. The fractional native regularity supplies the positive-order domain where it is needed.

For the native Sobolev bound I checked the cell length/amplitude exponents and the split at `ceil(B^2/E)`. Interpolation gives the displayed exponent of both budget and error. For the full frequency tail I checked the translated reciprocal-cell exceptional measure, the averaged Fourier multiplier, and the symmetry factor; the exact constant is bounded by 16 as stated.

The Mobius full-series rearrangement has an absolutely summable cubic tail. Its two endpoint sums yield compact convergence, while the exact prefix gives the stated lower bound for the complete norm. The finite prefix equations force the low-index Mobius coefficients, making the growing budget explicit. The safe compact and large-frequency bounds do not jointly establish complete-norm convergence.

The independent final review reconstructed these arguments and reproduced the 30,783-check receipt byte for byte in normal and optimized Python. Its review distinguishes finite overlap checks from proofs of universal identities.

## Local certificate

I authored the primitive rational coefficient replay, Graeffe/Rouche complete root count, residue isolation, Bernstein boundary proof, and maximum-principle consumer. The independent local review read this code and its inherited interval backend, reconstructed the analytic argument, and replayed the order-50 source and both negative controls. It inspected, but did not independently rerun, the order-100 receipt. My separate relocated optimized replay of order 100 is recorded in `LOCAL_RELOCATED_REPLAY.json`.

The certificate does not equate the denominator-pole count to the transform-zero count. It proves that every transform zero inside the specified disk is real by exhausting all possible nonreal poles, checking every real residue, and comparing the boundary rational function to the decaying Weyl function. This is the full local consumer required for that conclusion.

## What is and is not composed

The README and claim ledger summarize these separately reviewed components. They do not establish a new implication by combining unrelated partial results. In particular:

- Positive residues near simple real target zeros would not exclude nonreal target zeros.
- The two finite Bessel certificates are not a cofinal sequence.
- The moving-matrix support bridge still needs actual increasing-window positivity.
- Compact native synthesis still needs a complete-norm estimate for the same coefficients.

The remaining claims are deliberately mathematical: increasing-window coercivity, an expanding cofinal local gate, or a full native approximation. No amount of repeating the existing finite checks resolves those missing statements.
