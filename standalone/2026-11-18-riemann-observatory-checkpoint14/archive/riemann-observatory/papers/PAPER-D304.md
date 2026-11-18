# PAPER-D304: Fourier transforms with only real zeros

Charles M. Newman. Proceedings of the American Mathematical Society61(2),245–251(1976). DOI10.1090/S0002-9939-1976-0434982-5. [Primary scan](https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf).

**Audit scope:** L1; completed substantive reading=True. All printed pages245–251 read; main theorem statements/classification product and cutoff endpoint checked against page images. Gaussian-convolution/weak-limit proof architecture and four lemmas reconstructed. Independently checked quartic lower bound and cutoff closure; external polynomial real-zero-preservation/entire-function antecedents and every estimate not independently audited.

**Versions/corrections:** No exhaustive correction search. Issue dateDecember1976 and copyright1977 kept separate; source identity confirmed with Crossref. SourceSHA256 `f154969b9a39b0e64075570eb9f4c920affbea85bbcee0367eb66302e7a1be28`.

## Exact source results

- Theorem1,p246: Real even integrable f with super-Gaussian decayexp(−|u|^γ),γ>2,and initial Fourier zero stripΔ has strip sqrt(max(Δ²−2δ,0)) after multipliere^{δu²},δ>0.
- Theorem2,pp246–247: Even nonnegative finite measures whose Gaussian-damped Laplace transforms have only imaginary zeros for everyb>0 are exactly a symmetric pair of atoms includinga0 case, or the canonical quartic/second-power densities with factors(1+u²/aj²)exp(−u²/aj²),Σaj^-4<∞,and stated integrability conditions. Exact formula in audit/theorem record.
- Theorem3 andRemark2,p247: For originalΞ_b(x)=∫exp(ixu−bu²)F(u)du,withΞ_0(x)=ξ(1/2+ix), there is−1/8≤b0<∞ with real zeros iff b≤b0. RH meansb0≥0, and Newmanconjecturesb0≤0. Under inspected Rodgers–Tao scalingΛ_standard=−4b0.

## Proof architecture

- Gaussian convolution approximates the input measure by densities with canonical products inherited from the damped transforms.
- Bounded shape parameters yield normal-family density limits; divergent parameters force symmetric pair support.
- Polynomial/canonical-product approximations prove sufficiency.
- The classified densities have quartic-type lower tails, incompatible with the super-exponential Riemann kernel.
- Strip contraction gives a nonempty real-rooted half-line; exclusion from the classified class makes its threshold finite; Hurwitz gives endpoint inclusion.

## Limitations

- Finite Riemann cutoff does not imply finite cutoff for every positive rapid kernel;quarticexamples havethreshold−∞.
- A finite positive measure need not admit all positive heat tilts.
- Newmanb runs opposite to modernheat and has an additional scale4 relative to Rodgers–Tao.
- The classification is an all-b result, not a finite coefficient criterion.

## Concrete research questions

- Formalize the elementary logarithmic inequality and the exact atomic cutoff.
- Review the smooth positive-kernel/Li-prefix construction and sharpness proof.
- Do not infer global cutoff convergence from locally uniform transform convergence.

## Research reuse

`audits/heatflow_round2.md` preserves the exact source conventions and independently reconstructed positive-kernel controls. It separates atomic measures from admissible kernel functions and finite Li-type prefixes from all-zero/all-parameter theorems. The finite numerical enclosure is reproducible with `experiments/code/heatflow_round2.py`; independent adversarial review remains explicitly pending.
