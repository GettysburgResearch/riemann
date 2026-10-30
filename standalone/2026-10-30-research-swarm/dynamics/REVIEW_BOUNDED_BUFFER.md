# Independent audit of bounded-buffer reciprocal-factor removal

Reviewer: dynamics lane. Date: 30 October 2026.  
Source: `swarm/positivity/NEAR_CUTOFF_REMOVAL.md`.  
Reviewed final SHA256: **`a78640b802953e3c21d977abf078af9fd28093acabb340dda429f4d455e28782`**.  
The predecessor hash `ce14c6f1cb8166dd77789f7eb972fd23a41c8bca8f2b2438792c25e417baa298` received the full initial review. The final change explicitly retains the original Gaussian component in the residual Lévy triplet; it was checked separately and resolves the sole wording clarification raised.

## Outcome

**Passed at the stated source-qualified finite scope.** No gap was found that requires retreating to the earlier U/8 corollary. The direct bilateral construction supports deletion through V≤U−70 for the stated verified-height range, subject to the cited counting, verification and reciprocal-law inputs. It supplies no additional zero verification, no cofinal deletion theorem, and no new all-height zero-free boundary.

## 1. Counting intervals and separation of retained factors

The lower bound on N(y+15)−N(y) is valid for y≥100000. The main-term derivative is increasing, the two endpoint errors are bounded with the correct signs, and the elementary estimates give a strict lower bound 21/4. Thus there is at least one zero even if all the count in an interval comes from multiplicity at a single ordinate.

With B=max(V,100000), the first undeleted ordinate a is at most B+15. The second retained ordinate eta can be selected in (B+30,B+45]. These are different ordinates, regardless of multiplicity, with

$$\eta-a>15,\qquad U-\eta\ge25,\qquad a\le U-55.$$

Both remain below the verified height. Removing one occurrence of a leaves the eta term available; repeated occurrences of a cause no problem. When V is small, choosing B=100000 does not require a to be close to B: the resulting larger separation only helps.

## 2. Uniform positivity and monotonicity after tilting

For 0<x≤pi, every unverified term has cos(delta x)≥0 and delta sin(delta x)≥0. For either tilt with |s|<a, the corresponding rate gamma∓s is positive. Therefore both the term and its negative derivative are nonnegative. The retained eta term makes the total strict, for both A_V and the residual B_V=A_V−exp(−ax).

For x>pi, comparison against exp(−(eta−s)x) removes the tilt from the exponential ratio. The numerator bound is consequently uniform as s approaches either endpoint of (−a,a). The derivative factor obeys

$$|\gamma-s-i\delta|\le\gamma+a+1/2<2\gamma,$$

and the retained derivative denominator is at least eta−a>15. The assumed a≤U−55 supplies the margin used in this inequality.

The maximum replacements at gamma=U are legitimate: y²exp(−pi(y−eta)) and y³exp(−pi(y−eta)) are decreasing for y≥U in the stated range. Multiplying these maxima by the reciprocal-square tail sum gives exactly the displayed E0 and E1 bounds. No pointwise zero spacing or unproved cancellation in the unverified tail is used.

An independent execution of `near_cutoff_check.py` passed. Its exact rational upper bounds give

$$E_1<5.8692\times10^{-5},\qquad E_0<1.4673\times10^{-16}$$

at the worst allowed height. The printed decimals are summaries of rational bounds; the proof uses the rational comparisons. The illustrative smaller binary64 bound is unnecessary.

## 3. Construction of the residual law

The argument does not invoke the one-sided clock positivity from Sra's C.3 outside that theorem's retained-ordinate range. Instead it proves B_V(x)>0 directly. Hence B_V(|x|)/|x| is a valid symmetric Lévy density. Its integrability near zero follows by deleting finitely many Laplace numerators from the original admissible measure; integrability at infinity follows from the positive retained rates and the absolutely summable tail.

The final source correctly specifies the whole residual triplet: retain the original Gaussian component, use zero symmetric drift, and replace A by B_V. Subtracting an exponential numerator removes exactly one centered Laplace exponent. Thus the residual characteristic function is the original characteristic function multiplied by all the stated deletion factors and one additional factor for a. This establishes the probability law before invoking any shape claim.

## 4. Analyticity, positivity and the first-factor estimate

The supplied real-axis characteristic function decays faster than every exponential. Every deletion product here is finite, even though its degree may be enormous. Multiplication by that fixed polynomial preserves the decay. Fourier inversion therefore gives entire densities for the residual and for p_V. No finite product is being treated as an infinite one, and no numerical inversion is needed.

The stronger residual lower bound

$$B_V(x)\ge(1-E_0)e^{-\eta x},\qquad x>0,$$

holds in both x-regimes. It permits extraction of the symmetric difference of two independent Gamma(1−E0,eta) variables. That difference has a positive density on the whole real line. Convolution with the remaining law therefore makes the residual density positive everywhere.

Consequently p_V is a convolution with a centered Laplace density at rate a, with positive residual mass on both sides of every location. Differentiating that convolution yields the strict bound

$$|p_V'(x)|<a p_V(x).$$

This strictness is justified by whole-line positivity, not merely by nonnegativity of the residual.

The exponential moments exist for |s|<a: each verified exponential rate is at least a, and the unverified tail begins above U>a. The same bounds provide the necessary exponential integrability of the Lévy measure. The transform identity follows on the strip from the characteristic-function identity and analytic continuation. No nonreal pole lies inside that strip, since the first undeleted positive ordinate is a.

## 5. Strict log-concavity

For each real |s|<a, exponential tilting multiplies the bilateral Lévy density by exp(sx). The separately proved monotonicity on each half-line is the self-decomposability criterion, so the classical unimodality theorem used in the cited source applies. The drift introduced by tilting does not affect this criterion.

If (log p_V)'' were positive at x0, choosing s=−p_V'(x0)/p_V(x0) would be admissible by the strict first-factor estimate. The tilted density would have a strict local minimum at x0, contradicting unimodality. This proves ordinary log-concavity.

Since p_V is positive and real analytic, failure of strict two-point log-concavity would give an affine interval for log p_V. Analytic continuation along the real axis would make it affine everywhere, producing a nonintegrable global exponential. This proves the exact strictness stated in the source. It does not assert negative second derivative at every isolated point, and the source correctly avoids that stronger conclusion.

## 6. Scope of the audit

The retained-gap variant and the order-log-U general buffer follow from the same two tail inequalities. The fixed numerical buffer 70 uses the stated upper bound on U; it is not asserted for arbitrarily large verified heights with unchanged constants.

This review checked the new derivation and independently replayed its exact rational constants. It did not rerun the cited zero census, reconstruct the external explicit counting theorem, or independently prove the source's reciprocal-xi Lévy representation and self-decomposable-law unimodality theorem. The final claim remains conditional on those clearly attributed inputs.

No further correction was requested. The earlier U/8 result remains a valid fallback but is not needed because of any identified defect in this bounded-buffer proof.
