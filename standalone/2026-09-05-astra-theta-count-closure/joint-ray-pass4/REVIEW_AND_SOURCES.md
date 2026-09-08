# Sources and independent review contract

This is an author-supplied review request, not an independent review verdict.
All new analytic statements are proposed proofs; RH remains unproved.

## Primary inputs inspected during this pass

1. A. Chirre and F. Goncalves, Bounding the log-derivative of the zeta-function,
   Mathematische Zeitschrift 300 (2022), 1041-1053,
   DOI 10.1007/s00209-021-02820-9.
   https://link.springer.com/article/10.1007/s00209-021-02820-9
   ONLY Proposition 5 (unconditional Guinand--Weil for general complex zeros)
   is used. The RH-conditional main theorems and Lemma 4 are not used.
   Publisher HTML was read, including hypotheses, endpoints and Fourier sign.
   No PDF inspection or external computation was performed in this pass.
2. NIST DLMF 5.9: digamma/Gamma integral conventions.
   https://dlmf.nist.gov/5.9
   The estimates actually used are derived explicitly in PROOF.md.
3. NIST DLMF 27.2: von Mangoldt and arithmetic-function conventions.
   https://dlmf.nist.gov/27.2

## Repository input

PR #790, 337c222a54a232b89b9f47827b2caeb754145efc:
prime-heat-pass3/PROOF.md, specifically PH1 and PH6--PH7 at y=1.
The uploaded publication archive supplied the local bytes; the same live
proof was read through GitHub. SOURCE_LOCK.json records the locally computed
Git blob and SHA256. The shifted-contour algebra is rechecked in bounded
exact controls, but those controls are not an infinite analytic proof.
The prior fixed-t PH20 is not assumed by the uniform approximation: the new
Gamma-density argument proves the needed uniformity directly.

The invariant-zero normalization, critical strip and polynomial/logarithmic
zero count are classical analytic inputs. The new statements need no finite
zero verification, simplicity, linear independence, GRH, or zero-density
conjecture. The previous large finite positivity claims are not re-proved,
withdrawn, or silently imported into a global claim.

## Priority mathematical checks

- L1 versus total variation: the score calculation proves the L1 constant;
  the normal has variance 1/4 and center sqrt(k), not its mean.
- Exact Gamma mixture weights, W'<=2W, and the k=0 tail component.
- Infinite prime-tail summation: a frequency-uniform error alone is NOT
  summable; the separate y=1 contour estimate is essential.
- The small-x part of the gamma integral and t|log t| near zero.
- Fourier inversion at i/2, the sign -I_(m-1,t)/2, and E(1)=0.
- Normal convergence and pole residues of the ray generating function.
- The absence of a positive-real dominant atom in the negative-density
  lemma; the synthetic countercontrol shows why it cannot be dropped.
- Rational-ray selection excludes only FINITELY many relevant exceptions
  on a compact interval. Merely countable exclusion would be insufficient.
- Supremum, limsup, and negative-part conventions in the quantitative rate.
- Equation (22) concerns one transformed atom, not the first negative order
  of the complete zeta sum.
- The final source estimate (23) is OPEN. In particular t=m/u is outside the
  new joint asymptotic's controlled range for every fixed u.

## Literature and novelty boundary

The Gaussian score method is a standard Stein-method idea and is proved
here in the exact needed form. Gamma mixtures, Fourier inversion, Stieltjes
integration and power-sum noncancellation are classical tools. The contribution
claimed is their specific quantified use in this fixed source, not invention
of those methods. External novelty and the analytic proofs require review.
