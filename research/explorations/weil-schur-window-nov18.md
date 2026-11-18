# A larger positive Weil window from weighted prime translations

**Status.** Proposed finite and asymptotic positivity theorems. The proofs build on the [flat passband and finite-difference argument](weil-window-positivity-nov18.md). Both use a critical-line census up to a specified height. No assumption about zeros above that height is made. The finite arithmetic calculation bounds a weighted translation norm; it does not discretize test functions.

## Results

1. Using the published verification through $T_0=3\,000\,175\,332\,800$, every $g\in C_c^\infty(-12/5,12/5)$ satisfies
$$W(g)\ge \tfrac18\,2100^{-2m}\|g\|_2^2,\qquad m=2^{31}.$$
The original autocorrelation has prime-power cutoff $e^{24/5}\simeq121.51$.
2. For every fixed $0<\epsilon<1$ there is a $T_\epsilon$ such that for every $T\ge T_\epsilon$, $\mathrm{RH}(T)$ implies coercivity on the entire window $|u|<\log((1-\epsilon)\log T)$. The positive lower constant may depend on $T,\epsilon$. The asymptotic input concerning primes is the classical prime number theorem.

## An operator bound available on the complement

On $[-A,A]$ let $K_A$ denote the sum of compressed translations by both $\pm\log n$, with weights $\Lambda(n)/\sqrt n$, using zero extension. Its quadratic form is the signed prime-power term subtracted in the explicit formula. The positive Schur weight $v(x)=e^{x/2}+e^{-x/2}$ gives $\|K_A\|\le \sup (K_Av)/v$, including endpoints in the prime sums for an upper bound. In fact Cauchy–Schwarz with these row weights, or $2|f(x)f(y)|\le|f(x)|^2v(y)/v(x)+|f(y)|^2v(x)/v(y)$, proves the bound. For $z=e^x$ and $s=e^A$ the row ratio is
$$
 {1\over z+1}\sum_{n\le s^2}\Lambda(n)
 \left[(z+1/n){\bf1}_{nz\le s}+(1+z/n){\bf1}_{n\le sz}\right].
 \tag{1}
$$
Evenness permits restricting to $1\le z\le s$. Between consecutive breakpoints the numerator is affine, so the extrema are at the endpoints, using inclusive inequalities there to dominate both one-sided limits.

At $s=12$ the supremum is strictly below $15.31$. The [exact rational check](check_weil_schur_nov18.py) upper-rounds every logarithm to a thousandth after a 12-term atanh expansion with rational tail bound, and evaluates (1) at the 47 prime powers' relevant breakpoints and both endpoints. Its largest rational upper bound occurs at $z=139/12$ and is strictly less than $1531/100$. With a nonrational interval endpoint below $\log12$, the norm on the smaller test space is bounded by the norm reported for $\log12$ by zero extension.

Recall $P$ from §2 of the preceding proof with $y(t)=\operatorname{sinc}^2(t/R)$. The complement $1-P^2=(1-P)(1+P)$ expands into a nonnegative linear combination of monomials $y^j(1-y)^k$ of total degree at most $6m-2$, by the two binomial sums. For real $t$, $y(t)$ is the squared modulus of the multiplier $\operatorname{sinc}(t/R)$. Also
$$
 1-y(t)=\tfrac12\mathbb E|e^{itU/R}-e^{itV/R}|^2
$$
for independent uniforms $U,V$ on $[-1,1]$. Multiplying these identities with independent copies expresses the complement as a positive mixture of squared multipliers whose inverse transforms are finite measures supported on $[-(6m-2)/R,(6m-2)/R]$. Consequently the prime contribution on $(1-P^2)|\widehat g|^2$ is bounded above by $Q I$ whenever $Q\ge\|K_A\|$, $A\ge L+6m/R$, and $I=(2\pi)^{-1}\int(1-P^2)|\widehat g|^2$. The arithmetic formula on the enlarged window may include the extra prime powers: the sum of the weighted integrals is exactly the complement, and every mixed test is supported in that window.

## Numerical constants for the full continuum estimate

Use $L=12/5$, $m=2^{31}$, $R=80m$, so $L+6m/R=2.475<\log12$. The gamma multiplier $M(t)=\Re\psi(1/4+it/2)-\log\pi$ exceeds $15.56$ for $|t|\ge4\cdot10^7$ by the digamma estimate in the preceding proof ($\log((4\cdot10^7)/(2\pi))>15.66$). Everywhere $M(t)\ge-6$. Combining $Q<15.31$ with the Schur bound, the gamma-minus-prime complement is at least
$$
 \tfrac14 I-22 I_{\rm low},
 \qquad I_{\rm low}=(2\pi)^{-1}\int_{|t|\le4\cdot10^7}(1-P^2)|\widehat g|^2.
$$
The backward-difference argument uses $2LR=384m$ exactly, so $I\ge2100^{-2m}\|g\|_2^2$ as before. Inequalities (2)–(3) of the passband proof give $I_{\rm low}\le2\cdot2600^{-2m}\|g\|_2^2$ since $\sqrt{8/3}(4\cdot10^7)/R<1/2600$. The pole loss is bounded by $700\cdot8^m R^{-2m}\|g\|_2^2$, now using $2Le^L<54$.

For $|\Re z|=t>T_0$, $q=(1.001R/t)^2<1/250$ bounds $|y(z)|$, since $e^{1/(2R)}<1.001$. The same binomial argument gives
$$|P(z)|\le 2^{3m}(1+q)^m q^{2m}\le 9^m(1.001R/t)^{4m}.$$
Here $T_0/R>17$, so $9(1.001R/T_0)^4<1/8000$. The dyadic count of the preceding proof bounds the complete exterior contribution in absolute value by $2\cdot10^{17}\,8000^{-2m}\|g\|_2^2$. The census gives nonnegative contributions at every other ordinate. The three losses together are strictly less than $\tfrac18\,2100^{-2m}\|g\|_2^2$. This proves the first assertion.

## Asymptotic transfer from a verified zero height

Write $\psi_0(u)=\sum_{n\le u}\Lambda(n)$. The first and third pieces of the two brackets in (1) before division contribute $z\psi_0(s/z)+\psi_0(sz)$. By PNT, for any fixed $\nu>0$, $\psi_0(u)\le(1+\nu)u+C_\nu$ for all $u\ge1$. Dividing by $z+1$ bounds the resulting contribution by $(1+\nu)s+C_\nu$. The remaining terms give a weighted average of $\sum_{n\le s/z}\Lambda(n)/n$ and $\sum_{n\le sz}\Lambda(n)/n$, hence $O(\log(2s))$ by partial summation. Therefore uniformly on the full test space
$$\|K_A\|\le(1+o(1))e^A \qquad (A\to\infty).$$

This constant in the bare prime-operator norm is sharp. Test on $v_A(x)=\exp[-(A-|x|)/2]$ on $[-A,A]$, whose squared norm is $2(1-e^{-A})$. For $\log n\in[A,2A]$ put $u=2A-\log n$. In the overlap of the two translated intervals the product of the two profiles is exactly $e^{-u/2}$, so its integral is $u e^{-u/2}$. Keeping just these nonnegative terms gives
$$
 \langle K_Av_A,v_A\rangle
 \ge 2e^{-A}\sum_{e^A\le n\le e^{2A}}\Lambda(n)\log(e^{2A}/n)
 =(2+o(1))e^A
$$
by PNT and partial summation. Dividing by the norm shows $\|K_A\|=(1+o(1))e^A$. Improving the leading frequency threshold by a fixed factor through a uniform bound on this operator alone is therefore impossible.

Take $L=\log((1-\epsilon)\log T)$, $A=L+1/L$. Write $Q$ for the supremum in (1), $V=100e^Q$, $m=\lceil100L V\rceil$ and $R=6mL$. Then $Q\le(1-\epsilon/2)\log T$ for large $T$, and $R\le T^{1-\epsilon/3}$. The gamma multiplier exceeds $Q+1$ for $|t|\ge V$. The finite-difference lower bound for $I$ is
$$
 [2e(2LR+m)/m]^{-2m}\|g\|_2^2=[2e(12L^2+1)]^{-2m}\|g\|_2^2,
$$
using the floor of $2LR$ if it is not an integer. The absolute low-frequency error is at most $2(Q+7)(\sqrt{8/3}\,V/R)^{2m}\|g\|_2^2$. Its ratio to this floor tends to zero because $\sqrt{8/3}(V/R)\cdot2e(12L^2+1)<1/2$ eventually and $m\ge100 L V$. The pole correction from the passband proof costs $O(Le^L)\,8^m R^{-2m}\|g\|_2^2$ and is also smaller by a factor tending to zero.

For $|\Re z|>T$, the exterior estimate costs $O(Le^L T\log(2T))[9(1.001R/T)^4]^{2m}\|g\|_2^2$. Since $R/T\le T^{-\epsilon/3}$, this is $o(1)$ times the floor: the negative exponent is $\gg_\epsilon m\log T$ while the prefactor costs $O(\log T)$ and the log of the inverse floor is $O(m\log L)$. This gives a strictly positive lower bound for all tests. Nestedness gives the same conclusion for smaller $L$.

**Scope.** The argument provides a complement theorem for transferring finite critical-line verification to an infinite-dimensional test space at a prescribed radius. Establishing a cofinal sequence of such radii without unbounded verified heights is still open.
