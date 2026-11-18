# Critical Sobolev and variation separation

I independently verified the compact example and the Fejér estimate in the analytic156 provenance note. The example belongs to the continuous strip-critical class with local (H^1) at the origin in logarithmic coordinates. The cited variation hypotheses exclude it. This establishes noninclusion of test classes. The comparison of hypotheses alone does not settle priority or whether a separate extension argument could derive the critical result from an earlier formula.

## Capacity and support

Use (widehat F(t)=int_{mathbb R}F(u)e^{itu},du), with inverse measure (dt/(2pi)). For (R>1) define
[
widehat P_R(t)=rac{pi}{log R}rac{mathbf 1_{{1<|t|<R}}}{|t|}.
]
Its integral is (2pi). Thus (P_R(0)=1), (|P_R|le1), and (P_R) is real and smooth by the even compactly supported Fourier density. In the Plancherel normalization
[
|P_R|_{H^{1/2}}^2
=rac{pi}{(log R)^2}int_1^Rrac{sqrt{1+t^2}}{t^2},dt
=rac{pi}{log R}+O((log R)^{-2}).
]
Let (u_j=2+2^{-j}), (r_j=2^{-j-3}), and (J_j=(u_j-r_j,u_j+r_j)) for (jge1). These intervals have disjoint closures in ((2,3)), accumulating only at (2). Choose (0lechi_jle1) smooth compactly supported in (J_j) with (chi_j(u_j)=1). Multiplication by each fixed (chi_j) is bounded on (H^{1/2}), by Fourier convolution, submultiplicativity up to a constant of ((1+t^2)^{1/4}), and the weighted (L^1) norm of (widehat{chi_j}). Choose (R_j) after fixing (chi_j) so that (Q_j(u)=chi_j(u)P_{R_j}(u-u_j)) has (H^{1/2}) norm at most (2^{-j}). No uniform bound in (j) for the cutoff multipliers is needed.

For (a_j=1/log(j+2)), the sum (F=sum_j a_jQ_j) converges in (H^{1/2}) by the triangle inequality and uniformly by disjoint supports and the bound (sup_{j>N}a_j) for its tail. Hence (F) is real continuous, supported in ([2,3]), and zero near the origin. The indexed interval family ([u_j-r_j,u_j]) gives increments (a_j); its harmonic sum (sum_j a_j/j) diverges. This family is permitted by the p. 271 definition, which quantifies over every choice of indexed nonoverlapping intervals and imposes no geometric ordering. Any fixed exponential tilt likewise has infinite harmonic variation because its center values are bounded below by a positive constant times (a_j), and its endpoint values remain zero. The same argument survives a monotone change of variable and multiplication by a continuous positive weight bounded away from zero on the compact support.

For (f(x)=x^{-1/2}F(log x)) the value-decay hypotheses hold at both ends, and (f) vanishes near 1. Its Mellin transform on a line (Re s=eta) is the Fourier transform of (e^{(eta-1/2)u}F(u)). On every compact beta interval multiply by an extra fixed smooth cutoff equal to one on ([2,3]). The weighted Fourier (L^1) bounds of these multipliers are uniform, by integration by parts and the common compact support. The strip (H^{1/2}) integral is therefore finite. Local (H^1) at (u=0) holds because (F) vanishes nearby. At the accumulation point (2), the quotients (F(u_j)/(u_j-2)=2^ja_j) diverge, and the mean value theorem inside the individual intervals gives unbounded derivatives approaching from the right. The corresponding obstruction at (x=e^2) survives the smooth invertible coordinate change and the positive prefactor. The example falls outside literal global condition (A) even if this point is treated as an exceptional point with a required finite one-sided derivative limit.

## Source comparison

- Barner Theorem 1, printed p. 141, uses exponentially weighted ordinary bounded variation. Büthe v4 §2 p. 3 explicitly uses (g(t)e^{c|t|}in BVcap L^1) for (c>sigma_1-sigma_0/2), midpoint values and (g(t)+g(-t)-2g(0)=O(|t|^eta)) with (eta>0). For this example the midpoint and local conditions pose no obstruction. Ordinary BV would imply harmonic BV, while the weighted test already has infinite harmonic variation. [Barner](../../sources/prime146_mellin_provenance/barner-145.xml) · [Büthe](../../sources/prime146_mellin_provenance/buethe_1308.6704v4.pdf)
- Burnol v2 pp. 7–8 condition ((A_epsilon)) requires total variation of (g(u)(u^{-epsilon}+u^{1+epsilon})); the logarithmic coordinate change and nonvanishing weights preserve the specific divergent interval test. The stronger archimedean hypothesis on p. 11 additionally requires a continuous locally BV derivative and joint derivative decay. [Burnol](../../sources/prime146_mellin_provenance/burnol.pdf)
- Avdispahić–Smajlović p. 271 lists (phi BVsubset HBV) when (sum_n phi^{-1}(1/n)/n<infty). The p. 273 condition (phi) for a regulated test asks for membership in (phi BVcap L^1) and summability with denominator (n^{1/p}) for some (p>1), which implies the p. 271 series by termwise comparison. In Theorem 6.1, printed pp. 283–284, the top derivative (g^{(M)}) must satisfy condition (phi); each (g^{(j)}) for (j=0,dots,M-1) must belong to (HBVcap L^1). The additional condition is (g^{(M)}(x)-g^{(M)}(0)=O(|log|x||^{-alpha})) for some (alpha>M+2). Thus (Mge1) requires (gin HBV) directly, and the (M=0) reading requires it via condition (phi). The theorem concerns a symmetric truncated transform integral for a special pair. This argument only uses its actual test hypotheses and does not identify its general special-pair formula with the zeta zero functional. I checked the rendered pp. 271, 273, 283 and 284. [Primary scan](https://www.math.bas.bg/infres/MathBalk/MB-17/MB-17-267-289.pdf)

## Fejér normalization

For (m_T(t)=(1-|t|/T)_+), the inverse in the stated convention is
[
K_T(u)=rac{1-cos(Tu)}{pi Tu^2}
=rac{T}{2pi}left(rac{sin(Tu/2)}{Tu/2}ight)^2.
]
It is nonnegative, has continuous value (T/(2pi)) at zero, and has mass one by Fourier evaluation at zero. The multiplier of sharp minus Fejér truncation is (|t|/T) on ([-T,T]) up to endpoint values and zero outside. Its squared dual weighted norm with unnormalized (dt) is
[
rac{2}{T^2}int_0^Trac{t^2}{sqrt{1+t^2}},dtle1.
]
Fourier inversion contributes the factor (1/(2pi)) when both norms use unnormalized (dt). On a fixed bounded frequency interval the dual squared norm is (O(T^{-2})). On its complement the bound by one multiplied by the (H^{1/2}) frequency tail yields uniform sharp-minus-Fejér decay for each fixed test.
