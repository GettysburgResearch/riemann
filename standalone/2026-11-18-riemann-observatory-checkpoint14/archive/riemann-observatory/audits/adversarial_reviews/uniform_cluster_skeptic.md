# Independent adversarial reconstruction: uniform two-root remainder

Reviewer: li_advocate. Date:2026-11-17. The equivalence agent's new proof was not read. Parent supplied the proposed exact Gram formula and limiting function. Result: the uniform O_C(1/L) assertion is correct, with the definitional repair below if it is asserted for every finite L. An explicit, deliberately crude constant is supplied. No publication novelty is claimed.

## Statement and the coalescence convention

Let N≥0,L=N+2,d=L+1, S=∑_(k=0)^L exp(ikθ). For distinct roots at1 and exp(−iθ), the optimal squared H² residual of degree≤N polynomial approximation is

E_N(θ)=(2d−2Re S)/(d²−|S|²).

At θ∈2πZ, the displayed formula is0/0. Its continuous extension is the double-root optimum 2(2L+1)/[(L+1)(L+2)]. Define E this way at **all** such coalescences, not just θ=0.

For each finite C≥0,

sup_(|c|≤C) |L E_N(c/L)−F(c)| ≤ K_C/L,

where

F(c)=2[1−sin(c)/c]/[1−(2sin(c/2)/c)²], F(0)=4,

and one valid explicit choice is K_C=18(12+C²)^2. This constant is not optimized. If only c=0 is to be extended, then the statement should instead restrict to sufficiently large L>C/(2π), since otherwise additional coalescences c=2πjL can lie in the interval and the formula is undefined there. The usual asymptotic uniform assertion already holds without this finite-L repair.

## Proof via variance and quadrature

Set f_c(x)=(1−cos(cx))/c² for c≠0 and f_0(x)=x²/2. For x∈[−1,1],

0≤f_c(x)≤x²/2, |∂_x f_c(x)|=|sin(cx)/c|≤|x|≤1,

including the continuous c=0 case. The normalized endpoint grid average is A_L f=(1/d)∑_(k=0)^L f(k/L).

For any function f of Lipschitz constant M on[0,1],

|A_L f−∫_0^1 f(x)dx|≤M/L.

Proof: the left Riemann sum differs from its integral by at most M/(2L). Its difference from the normalized endpoint grid average is |f(1)−R_left|/(L+1)≤M/(2L), by averaging the distances1−k/L. For a two-variable function separately Lipschitz with constant M in each variable, applying the one-variable estimate twice gives an error≤2M/L.

Define

U_L(c)=A_L[f_c(x)],
V_L(c)=(1/d²)∑_(j,k=0)^L f_c((j−k)/L),
U(c)=∫_0^1 f_c(x)dx,
V(c)=∫_0^1∫_0^1 f_c(x−y)dxdy.

For c≠0 these equal

U_L=(1−Re S/d)/c², V_L=(1−|S/d|²)/c²,
U=[1−sin(c)/c]/c², V=[1−sinc²(c/2)]/c².

Consequently L E_N(c/L)=2L/(L+1)·U_L/V_L and F=2U/V whenever the distinct-root expression is defined; at c=0 both are defined by the integral/grid expressions. These formulas avoid subtracting nearly equal floating numbers in the proof.

The Lipschitz bounds give, **uniformly for all real c**,

|U_L−U|≤1/L, |V_L−V|≤2/L.

Also U≤1/6 and U_L≤1/4 (indeed U_L≤(2L+1)/(12L)). The stronger denominator estimate supplied by the equivalence agent and independently checked here is

V(c)≥1/(12+c²)≥1/(12+C²)=:v_C>0.

Here is a complete proof. For real x put u=x². If u≤3/2, the alternating series of (1−cos(2x))/2 gives sin²x≤u−u²/3+2u³/45: the omitted first term is negative and subsequent term magnitudes decrease (the initial ratio after u is u/3≤1/2, and all following ratios are smaller). Multiplication by1+u/3 gives u−u³(9−2u)/135≤u. If u≥3/2, u/(1+u/3)≥1≥sin²x. Thus sinc²x≤1/(1+x²/3) for every real x, including x=0 by continuity. Substituting x=c/2 yields the asserted bound for V, including equality V(0)=1/12.

If L≥4/v_C, then V_L≥v_C/2. Splitting the ratio difference and using the preceding bounds gives

|L E_N−F|
≤2|U_L/V_L−U/V| + [2−2L/(L+1)]U_L/V_L
≤[5/v_C+4/(3v_C²)]/L.

For the finitely many smaller L, use0≤E_N≤1 (take approximant0) and0≤F≤1/(3v_C). Then

L |L E_N−F|≤L²+L/(3v_C)<52/(3v_C²)<18/v_C².

Since v_C≤1/12, the large-L coefficient is also below18/v_C². Thus K_C=18/v_C²=18(12+C²)^2 works for all L≥2 with the continuous coalescence convention. This proves the asserted estimate.

At c=0, U(0)=1/6,V(0)=1/12, while U_L(0)=(2L+1)/(12L), V_L(0)=(L+2)/(12L). Therefore the extension gives exactly

L E_N(0)=2L(2L+1)/[(L+1)(L+2)],

which tends to4 and agrees with the independently established double-root optimum. There is no tiny-c loss: both the quadrature estimates and the lower bound for V include c=0 explicitly.

## Adversarial cases

* Fixed c=2πj with j≠0: F(c)=2 and its denominator is1, so these are not singularities of the limiting expression. For sufficiently large L and q=exp(ic/L), one has S=1 and exactly E_N=2/(L+2). Thus L E_N−2=−4/(L+2), which is O(1/L) with no resonance blowup.
* Near c=0: direct ratio evaluation is ill-conditioned, but the integral formulation removes the c² cancellation. A failure of floating arithmetic here would not refute the theorem.
* At c=2πjL: the finite Gram matrix becomes singular because its two rows coalesce. The original formula needs its double-root extension. These extra points disappear from every fixed bounded interval as L grows.
* No constant uniform over arbitrary C should be expected for the all-L statement. At c=2πL, F(c)=2 while L E_N tends to4 as L→∞. Thus the smallest admissible K_C along C=2πL must satisfy K_C≥L|2L(2L+1)/[(L+1)(L+2)]−2|~2L=C/π. The bounded-C assumption is material.

Classification: independently checked with no issue in the substantive uniform asymptotic; missing finite-L convention at nonzero aliases if the formula is read literally. This is a correction to the research program's proposed statement, not an alleged error in a published paper. It establishes a finite polynomial uniformity bound only, with no transfer to ζ zero sums or arithmetic approximants.

## Revision and independent cross-check

The first independent proof used the elementary lower bound V(c)≥1/[18(1+C)^3], obtained by integrating only |x−y|≤1/(1+C); that already proved the uniform assertion with K_C=5832(1+C)^6. After the parent and equivalence agent supplied a sharper sinc inequality, I independently verified its alternating-series proof and algebra above. The same direct quadrature proof then improved the valid constant to18(12+C²)^2. The equivalence agent's separately proposed38(12+C²)^2 is also valid; the improvement here follows from a direct two-variable kernel estimate. These constants are analytical bounds, not fitted numerical observations.
