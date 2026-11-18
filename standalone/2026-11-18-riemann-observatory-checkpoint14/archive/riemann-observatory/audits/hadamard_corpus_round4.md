# Scoped reconstructions from Hadamard's original1896 PNT paper

Agent `/root/corpus`,2026-11-17. Original source and reading scope: PAPER-H401. All22article pages read; selected formulas visually verified. The following local arguments are independently reconstructed, while the historical genus/contour and character-analysis dependencies remain explicitly separate. Novelty is not claimed.

## 1. A precise sufficient version of the positive-logarithm boundary theorem

Suppose `f` on `Re s>1` has an analytic logarithm

\[
 \log f(s)=\sum_n a_n e^{-\lambda_n s},\qquad
 a_n\ge0,\quad\lambda_n>0\text{ real},
\]

absolutely convergent there. Suppose f admits meromorphic continuation to a neighborhood of each point of `Re s=1`, is holomorphic at every such point except s=1, and has a simple pole at s=1. Then `f(1+it)!=0` for every nonzero real t.

This is a modern sufficient formulation of Hadamard§5, printed202; the source uses a prime-phase concentration proof in §§2–4 rather than the following compressed trigonometric argument. Root independently checked this formulation/proof. No assertion that a positive Laplace kernel supplies these logarithmic coefficients is made.

Absolute convergence permits termwise real parts. Since `Re log f=log|f|` and `3+4cos u+cos2u=2(1+cos u)²>=0`, for every σ>1,

\[
 3\log|f(\sigma)|+4\log|f(\sigma+it)|
 +\log|f(\sigma+2it)|\ge0.
\]

If `1+it` were a zero of order `m>=1`, local meromorphy gives
`log|f(σ+it)|=m log(σ-1)+O(1)`. The simple pole at1 gives `-log(σ-1)+O(1)`. At `1+2it`, holomorphy gives `r log(σ-1)+O(1)` for a zero order `r>=0`. Their displayed combination is
`(-3+4m+r)log(σ-1)+O(1)`, tending to negative infinity because `-3+4m+r>=1`. This contradicts nonnegativity. Zero multiplicity is handled explicitly.

The sole-boundary-pole hypothesis is substantive. For example
`f(s)=(1+2^(1-s))/(1-2^(1-s))` has
`log f(s)=2 sum_(j>=0) 2^((2j+1)(1-s))/(2j+1)` with positive ordinary Dirichlet coefficients on Re s>1, and has both boundary zeros and infinitely many boundary poles. This elementary deletion test does not satisfy Hadamard's sole-pole hypothesis. The theorem is about boundary zeros only; it says nothing excluding zeros with real part strictly between1/2 and1.

## 2. Why the smoothing exponent is greater than one

For a>1, μ>1, the logarithmic derivative's absolutely convergent prime-power expansion and `integral_R |a+it|^-μ dt<infinity` justify interchanging the smoothed integral with the sum. The elementary inverse transform is zero below1 and `log^(μ-1)x/Gamma(μ)` above1. With μ>1 the value at1 is zero by continuity. Thus the source's equations18–19, printed213, follow with the minus sign in front of ζ'/ζ and the exact log p weight, not log(p^k).

The uniform summability mechanism in §§14–16 is elementary once the contour estimates are available. If `Re rho<1` for every nontrivial zero and `sum |rho|^-μ<infinity`, then for each ε>0 choose a finite subset with remaining sum<ε. For that finite subset, every `x^(Re rho-1)` tends to zero. For the remaining subset, `|x^rho|<=x` for x>=1, giving absolute bound εx. Hence the normalized zero residue contribution tends to zero without assuming a common positive distance of all zeros from the line Re s=1. The order is **tail selection, then x limit**, not an interchange justified by pointwise decay alone.

For ζ the count `N(T)=O(TlogT)` implies the required reciprocal-power convergence for each μ>1. At μ=1 it fails absolutely, and the proof cannot simply drop the smoothing factor. The paper's selected horizontal contours and logarithmic-derivative estimates are additional analytic inputs; this note does not replace them by the abstract summability observation. A coarse selected-height estimate with extra logarithmic factors would still vanish after multiplication by `T^(1-μ)`; the exact printed intermediary log factor is not independently certified in this scope.

## 3. Qualitative μ2 unsmoothing, with the limit order fixed

After higher prime powers are discarded, put

\[
 A(x)=\sum_{p<x}\log p\log(x/p),\quad
 \theta(x)=\sum_{p\le x}\log p.
\]

Then `A(y)-A(x)=integral_x^y theta(t)dt/t`. For fixed h>0, monotonicity gives

\[
 \theta(x)\log(1+h)\le A((1+h)x)-A(x),
\]
\[
 A(x)-A(x/(1+h))\le\theta(x)\log(1+h).
\]

If A(x)~x, first let x tend to infinity, holding h fixed. This bounds the upper and lower limits of theta(x)/x between `h/log(1+h)` and `h/[(1+h)log(1+h)]`. Then let h tend to zero. Both bounds tend to1, proving theta~x. No hypothesis that the error is uniform for h tending to zero with x was smuggled into this qualitative argument. This reconstructs source§18,217–218; root independently checked it.

## 4. A quantitative local modulus and a sharp generic loss

The author's question on printed219 motivates an explicit local statement. Let θ be nondecreasing and let A have increments `A(v)-A(u)=integral_u^v theta(t)dt/t`. Suppose, on `[x/(1+h),(1+h)x]`,
`|A(t)-t|<=tE`, with `0<h<=1/2` and E>=0. The preceding two monotonicity inequalities give exactly

\[
 \frac{h-(2+h)E}{(1+h)\log(1+h)}
 \le\frac{\theta(x)}x
 \le\frac{h+(2+h)E}{\log(1+h)}. \tag{H1}
\]

Using `h/(1+h)<=log(1+h)<=h`,

\[
 \left|\frac{\theta(x)}x-1\right|
 \le h+\frac{15E}{4h}.
\]

For `0<E<=1/4`, the choice `h=sqrt E` gives `19sqrt E/4`. This assumes the displayed local error modulus on that shrinking interval; it is not a deduction of a quantitative rate from the bare statement A~x.

The square-root scale cannot be improved for arbitrary monotone θ using only such integrated control. Start with θ(t)=t and its integration constant chosen so A(t)=t. At t=x0 jump θ to `(1+δ)x0`, keep it constant until t reaches `(1+δ)x0`, then resume θ(t)=t. The function is nondecreasing, its relative pointwise excess immediately after x0 is δ, and the total excess in A is exactly

\[
 x_0[(1+\delta)\log(1+\delta)-\delta]
 =\tfrac12\delta^2x_0+O(\delta^3x_0).
\]

During and after the plateau this controls the relative integrated excess by O(δ²), while the pointwise discrepancy is order δ. The integration constant is immaterial to the monotonicity inequalities; this example is a generic function, not a prime counting function. It diagnoses what extra information a stronger unsmoothing argument must use. It does not assert a new arithmetic obstruction or a new literature theorem. The quantitative addendum is a derived local lemma supplied for independent review.

## 5. What was not audited or inferred

The article's genus estimates, every selected-height avoidance constant, all fractional-μ branch contour details, the complete Lipschitz/Hurwitz functional equations and all character reductions are substantive external/remaining checks. A full original-source reading is not a full technical audit. The imprimitive character factors must be retained: finite factors `1-chi(p)p^-s` can have extra zeros on Re s=0, so primitive completed symmetry should not be asserted for the full imprimitive zero divisor without qualification.

The original final note220 directly acknowledges independent work of de la Vallée Poussin. The later logarithmic zero-free region and quantitative exponential PNT error have not been extracted from this paper. No RH, GRH, or uniform-in-modulus progression estimate was proved here. The successfully checked mathematical transition is from boundary nonvanishing and summable smoothed tails to qualitative PNT.
