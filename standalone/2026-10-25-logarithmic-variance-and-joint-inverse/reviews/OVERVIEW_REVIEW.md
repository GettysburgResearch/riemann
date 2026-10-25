# Independent review of the third-pass overview and sources

Date: 25 October 2026.
Reviewer: `/root/fractional_global`.
Scope: mathematical consistency, comparison with the preceding packet, and attribution boundaries. This is an internal agent review, not external peer review or formal verification.

## Exact reviewed files

Both files are under `standalone/2026-10-25-logarithmic-variance-and-joint-inverse/`.

| File | SHA256 |
| --- | --- |
| README.md | `0fb745228bdf21fbeab677411e7910decc69d7081058483cb90b0d7ee6013afe` |
| SOURCES.md | `3b34c3104b52bab23593abbf6eeaaf4025e45997a7c9eec073c992f4de9aed4f` |

**Verdict: consistent with the reviewed mathematics and its conditional/source-dependent scope. No remaining overview-level blocker found at these hashes.** Publication completeness and authentication of the final new remote commit are separate steps.

## Comparison table

I compared the table directly with the previous `EVEN_FINITE_SELECTOR_CONSUMER.md`, including its Theorem 3. The prior criterion requires nonnegative, uniformly tight finite selectors; bounded second moments are a sufficient way to obtain that tightness. Its displayed schedule is `N_a=ceil(a^3)`, and it already avoids identifying a limit with Xi. The overview describes all three points correctly.

The new criterion allows a signed physical function and a variance as large as `a/(10 log a)` at `N_a=ceil(4a log a)`. It also requires legality below the full finite minimum for the real-zero input, whereas the preceding positive-selector theorem could be formulated on the even block. The comparison table explicitly retains the new full-minimum condition. Thus the overview does not assert that every hypothesis has been weakened or that the earlier even-only legality automatically suffices for the new proof.

The overview states the remaining all-scale existence/variance hypothesis both before and after the comparison. The cosine-power compatibility examples are explicitly distinguished from actual source resolvents.

## Formulas and claim boundaries

- The mass-normalized resolvent, variance target, retained Fourier samples, and `L^1` estimate agree with the separately reviewed logarithmic-variance theorem. The positive overlap is of order `M_a^(-1/2)`, while the residual has a fixed negative `a log a` exponent plus `O(a)` and polynomial factors. These scales support the stated shift conclusion.
- The overview describes the finite spectral consumer without reversing the Galerkin inequality. It also explains that reducing the Fourier dimension does not remove the prime sum through `exp(2a)` or establish a computational complexity breakthrough.
- The displayed prime-discrepancy floor matches the exact note: its derivative coefficient is `(pi N+(2N+1)/2)/a`, its constant is `4-gamma-pi/2-3log(2)-log(pi)`, and the continuous-model multiplier uses the digamma function at `5/4+it/2`. The PNT saving is attributed to known prime cancellation, and the absence of an exponent bootstrap is stated.
- The complete convolution uses the correct identity `mu_E*Lambda_E=-mu_E log N` and the correct inherited moment at total length `Y`, including the logarithmic cost. Its capped variant is restricted to the imported estimate's scope. The revised reversibility sentence now includes sufficiently large `Y` on the fixed annular support, so division by `log(Yx)` is legitimate.
- The prime-square correction is normalized at residual length `D/L`; the displayed mean agrees with the independently checked native calculation. The unresolved squarefree factorization-dependent coefficient is not promoted to an allowed coefficient of the unmarked source theorem.
- The Jacobi identity is stated for good squarefree ideals, preserves the common frequency, and retains its explicitly unsuccessful `U D^3` frozen-variable cost. The qualified nonprincipal subfamily is not substituted for the complete physical family.

The opening and concluding sentences correctly state that no improved zero-free boundary has been obtained. The decimal benchmark is explicitly an inherited working boundary, rather than a theorem established or independently certified by this packet.

## Source attribution checks

The primary Connes--van Suijlekom theorem was read during my analytic review. `SOURCES.md` accurately identifies its specified distribution-matrix class and one-dimensional even kernel, and the new proof supplies the necessary full-legal rank-one reduction. Neither overview treats generic matrix positivity as a real-zero theorem.

I also opened Johnston--Yang, [arXiv:2204.01980v2](https://arxiv.org/html/2204.01980v2), and checked Theorem 1.4, equation (1.7): its stated Chebyshev bound has constants `0.026`, `1.801`, and `0.1853`, with threshold `x>=23`, as used by the floor note. I did not rerun its verification computations. The packet makes this imported status explicit.

I fetched the GitHub commit object for `08769810374603b926d995fdc6ff0254e4267ea5`. Its parent is `5c7f4aa542ea2112b7f95fce984a35dfe454cfd6`; its complete eight-file change list adds only the publication review and seven independent review files. This independently supports the overview's statement that this PR #1022 follow-up does not alter the preceding mathematical files. This observation is not an endorsement of every external proof used there.

The arithmetic preprint, full-family cap, buffered-bin input, and inherited decimal comparison remain imported dependencies. `SOURCES.md` expressly disclaims reconstruction or certification of the complete external preprints. The descriptions of agent review and finite computation do not claim external peer review, formal proof verification, or an all-scale numerical certificate.

## Repair recorded

The reviewer requested the large-`Y` qualification for reversibility and clearer direction in the zero-free-region wording. Both are present at the reviewed README hash. No mathematical proof file was changed by this overview review.

The final remote mathematical commit, tree contents, and manifest consistency are to be authenticated after the publication freeze. This review is bound to the two local byte identities above and should not be described as that later authentication.
