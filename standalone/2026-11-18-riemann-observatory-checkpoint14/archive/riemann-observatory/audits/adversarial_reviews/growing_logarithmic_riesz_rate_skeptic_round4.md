# Independent review of the growing-order rate

2026-11-17. Reviewer `/root/li_skeptic`. Scope: proposed **THM-E-W313**, `proposals/independent_campaigns/growing_logarithmic_riesz_rate_round3.md`. The complete proposed proof was read, and the new estimates were independently reconstructed rather than accepted from the previously reviewed qualitative result. **No issue found in the inspected argument**, conditional on RH and the same explicit classical inputs. No improved published source rate or novelty claim.

Fix `c>0`, `q>=1`, `L=log N`, `epsilon=c/loglog N`, and `alpha=epsilon L`. All constants below can depend on fixed `c,q`, and thresholds can be enormous. This supplies no estimate for moving `c` or `q`.

The exact absolute kernel moment is correct. Since

\[
 |K(v)|dv=B_\alpha(1+y^2)^{-(\alpha+1)/2}dy,
 \qquad y=v/\epsilon,
\]

substitution `u=1+y²` on each half-line gives

\[
 \int|K(v)|\frac{|v|}{\epsilon}dv
 =\frac{2B_\alpha}{\alpha-1}=O(\alpha^{-1/2})
 \quad(\alpha>1).
\]

The factor two and the denominator `alpha-1` are exact. Here `B_alpha=O(sqrt(alpha))` by Stirling. No Gaussian approximation is needed.

Put `R_v(t)=zeta(s)/zeta(s+epsilon+iv)` and `R_0(t)=zeta(s)/zeta(s+epsilon)`. On the central region `|v|<=eta epsilon`, the vertical logarithmic-derivative bound and the horizontal completed-product bound give

\[
 |R_v-R_0|\le C\frac{|v|}{\epsilon}
 \log(|t|+3)(|t|+3)^{\epsilon/2+D_1\eta}.
\]

This follows from `|exp(w)-1|<=|w| exp|w|`; it does not divide by the numerator at a zero. With the fixed `eta` already chosen so the exponent is at most1/8, the weighted `L²(dt/|s|²)` norm of the height factor is finite uniformly in `N`. Minkowski and the exact first moment give central error `O(alpha^(-1/2))`.

The three-term subtraction is exact because the full **complex** kernel mass is one:

\[
 \zeta V_N-R_0
 =\int_{\rm central}K(R_v-R_0)dv
  +\int_{\rm tail}KR_vdv-R_0\int_{\rm tail}Kdv.
\]

The first tail has norm `O_(q,c)(sqrt(alpha) exp(-kappa_eta alpha/2))` by the independently reviewed free-auxiliary-exponent argument. The last term has the stronger exponential tail-mass bound, since the weighted norm of `R_0` stays uniformly bounded by the horizontal xi-product estimate. This verifies the proposed intermediate estimate, including the mass-subtraction term; replacing the central kernel mass by one without that term would not have been an exact identity.

For the horizontal rate, let `B_delta` be the union of intervals of radius `delta<=1/4` around critical zero ordinates. On this union, `|R_0-1|²<=C(1+(|t|+3)^epsilon)`. Each interval has length `2delta`, and its weight is comparable to the corresponding zero-ordinate weight. Riemann–von Mangoldt therefore bounds the total weighted integral by

\[
 C_q\delta\sum_\gamma
       (3+|\gamma|)^{-2q+1/8}\le C_q'\delta.
\]

Multiplicity only overcounts this union, and the weighted sum converges. Finitely many low-height zeros contribute another fixed constant. Neither separation nor simplicity is used.

Off this union every point on the horizontal segment has vertical distance at least `delta` from every zero. Titchmarsh9.6(A) and local zero counting give `|zeta'/zeta|<=C log(|t|+3)/delta` uniformly along the segment; the bounded-height partial fraction patch is valid on the same strip and does not cross the pole at1. Integrating the derivative yields

\[
 |R_0-1|\le C(\epsilon/\delta)\log(|t|+3)
                 (|t|+3)^{C\epsilon/\delta}.
\]

Once `epsilon/delta` is small, its squared weighted norm is bounded by `C_q epsilon²/delta²`. All constants in that last height integration are uniform for sufficiently small ratios, since the power can be held below a single fixed integrable exponent. It follows that

\[
 \|R_0-1\|_q^2\le C_q(\delta+\epsilon^2/\delta^2).
\]

The choice `delta=epsilon^(2/3)` gives the claimed norm bound `O(epsilon^(1/3))`; the zero ordinates themselves are a null set. The kernel error `alpha^(-1/2)` and its exponential tail are smaller for the specified array. Thus

\[
 d_q(V_N)=O_{q,c}((\log\log N)^{-1/3}),\qquad
 d_q(V_N)^2=O_{q,c}((\log\log N)^{-2/3}).
\]

The same conclusion for fixed `q>=1` can also be obtained from `q=1` by `d_q<=2^(q-1)d_1`; no new growing-q uniformity follows. This rate matches the previously reconstructed scale for a different shifted Möbius array and is not being described as a better RH consequence. Historical priority for the exact moving logarithmic weights remains unassessed.
