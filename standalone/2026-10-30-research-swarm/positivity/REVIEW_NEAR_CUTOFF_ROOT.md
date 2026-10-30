# Root review of the retained-gap factor-removal theorem

Status: **INDEPENDENT ANALYTIC REVIEW; no blocking defect found**.  
Date: 2026-10-30. Reviewed source: `NEAR_CUTOFF_REMOVAL.md`.  
Reviewed SHA256: `a78640b802953e3c21d977abf078af9fd28093acabb340dda429f4d455e28782`.

The finite conclusion follows from the stated actual-source assumptions. In particular, the proof does not import Sra's one-sided residual theorem outside its allowed retained-ordinate range.

The counting inequality gives a zero in every interval (y,y+15] for y>=10^5. With B=max(V,10^5), the first surviving ordinate a is at most B+15 and a second retained ordinate eta lies in (B+30,B+45]. The hypotheses imply eta−a>15 and U−eta>=25. These are the only geometric gaps needed.

On 0<x<=pi, both the high-zero numerator and its negative tilted derivative have nonnegative terms. For x>pi, comparison with the retained exponential is valid uniformly for |s|<a. The numerator and derivative envelopes y^2 exp(−pi(y−eta)) and y^3 exp(−pi(y−eta)) decrease beyond U. The stated reciprocal-square zero tail therefore gives E0 and E1, including the factor 4/15 in the latter. The conservative rational inequality is adequate throughout 10^6<=U<=3×10^12.

The symmetric residual after extracting the first remaining Laplace factor is constructed from its explicitly nonnegative Lévy measure, retaining any Gaussian part of the original triplet. Removing finitely many exponential numerators preserves the required small-jump integrability. Its characteristic function is the actual reciprocal-xi function times the finite removed polynomial. Superexponential decay on the real Fourier axis supplies entire densities after this finite operation. The final source revision makes this triplet qualification explicit; it does not change the estimates.

The lower retained-exponential bound supplies a positive bilateral gamma component, hence a residual with full support and a positive density. Convolution with the first surviving Laplace density gives the strict score bound |p'_V|<a p_V. Every exponential tilt in that score range has decreasing positive Lévy numerators on both half-lines, and is therefore self-decomposable and unimodal. A positive log-curvature point would create a strict local minimum in the matching tilt, a contradiction. Analyticity upgrades concavity to strict two-point concavity, without claiming a strictly negative second derivative at every point.

The finite endpoint is conditional only on the explicitly cited finite-verification and counting inputs, not on RH at unverified heights. Those external inputs were read in the primary source but not independently recomputed here. The proof supplies neither a cofinal removal theorem nor another verified critical-line zero. Its buffer constants are conservative; optimizing them is not the missing global step.
