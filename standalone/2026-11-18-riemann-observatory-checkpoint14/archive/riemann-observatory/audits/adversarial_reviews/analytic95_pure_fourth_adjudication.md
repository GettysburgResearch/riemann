# Adjudication of the one-sided fourth prime-band twist

Assume RH and fix \(0<a<b\) with \(1/8<b<1/6\). With \(D(s)=\sum_{Y^a<p\le Y^b}p^{-s}\), write \(P=D^4\), \(y=Y^{4b}\), and take \(T\asymp Y\) for a compact portion of the strict tail. The two reviews agree on the pure-arm reduction. The wide initial horizontals can be bounded at a good height, while the printed **sharp** stationary-phase bound on the reflected edge remains inadequate. There is also a **smooth compact-local** formulation in which the saddle replacement has a power saving. The missing input in that formulation is a signed smoothly cut nonprincipal sum, with the auxiliary shift preserved. The result does not establish the fourth moment. [Prime review](prime90_pure_fourth_bottleneck.md) · [Weighted review](weighted90_pure_fourth_review.md)

## Source and common ground

I checked Theorem 5 and §§4–6 of the HLZ journal PDF, SHA-256 `6162632530cbeee8c1664d7ea53e844cffa9dbc53fe00a8cd8270e2d713b6a82`, in particular p. 1607 for the wide rectangle, pp. 1608–1610 for (27)–(29), Lemma 7 and the Möbius reduction, pp. 1610–1615 for §4.3 and Propositions 10–11, and the large-sieve estimates (48) and (50)–(52) in §6. The extra power of \(D\) in the pure arm puts \(y\) above \(T^{1/2}\). The real binomial identity is
\[
 (\Re D)^4=\tfrac18\Re D^4+\tfrac12\Re(D^3\bar D)+\tfrac38|D^2|^2 .
\]
All mixed sides have length at most \(Y^{3b}\) and the established padding and polarization apply. The formal pure value in the reviews agrees, since integrating their four-prime polynomial against \(\prod dx_i/x_i\) gives
\[
 H_0^4+4(-4d+2m_3)H_0^3
 +6(12d^2-4dm_3+6m_2^2)H_0^2-96d^3H_0+24d^4 ,
\quad H_0=\log(b/a),\quad m_j=(b^j-a^j)/j,\quad d=m_1 .
\]
Repeated primes in the pure main term cost \(\sum_{p>Y^a}p^{-2}=o(1)\), by the lcm denominator and bounded harmonic sums.

The continuous \(J\) integral is asymmetric. For a product AFE shell \(uv\le R\) the frequency pair is \((hu,v)\), \(h\le y\). Comparable frequencies are at most \(O(\sqrt{yR})\), and one integration by parts followed by the harmonic gap sum and divisor bound gives \(T^\epsilon\sqrt{yR}\). For noncomparable frequencies direct summation with the inverse logarithm bounded gives the same bound up to logs. The diagonal \(v=hu\) costs \(T^{3/4+\epsilon}\sum_{h\le y}|c_h|h^{-3/4}\ll T^{3/4+\epsilon}y^{1/4}\) on moving the local Mellin integral to real part \(-1/4\), using the pole-annihilating AFE weight. The log weight and dyadic summation are absorbed by \(T^\epsilon\). These errors save a power for \(y\le T^\theta\) with fixed \(\theta<1\). The principal saddle sums likewise use §4.3 with Perron lengths bounded between \(T^{1-\theta}\) and \(T^{1+\theta}\) up to constants, with bounded harmonic outer sums here. The zero-free margin and short-interval savings survive. This leaves the reflected discrete side. [HLZ journal](../../sources/classical63_derivative_moments/hlz2022print.pdf) · [Direct AFE reconstruction](prime75_hlz_sharp_aggregate_review.md)

## Wide horizontals and restoring the target heights

On a real strip \(\sigma\in[-C/\log T,1+C/\log T]\), let \(H=T^\kappa\) with \(4b<\kappa<1\). By the unit-height zero count, deleting intervals of radius \(c/\log T\) about the ordinates leaves a set of measure \(\gg H\) for small fixed \(c\). The classical partial fraction bound on this set gives \(\zeta'/\zeta\ll \log^2 T\) uniformly across the strip. Uniform in \(\sigma\) the Dirichlet mean-value theorem gives
\[
 \int_T^{T+H}|P(\sigma+it)|^2dt
 \ll (H+y)\sum_{n\le y}|c_n|^2 n^{-2\sigma}\ll Hy .
\]
Here \(|c_n|\le24\). The reflection is controlled by the same calculation. Average the integral of the absolute horizontal integrand over the good set, using Cauchy–Schwarz and the convexity bound \(T^{1/2+\epsilon}\) for the product of the two shifted zeta functions. A common usable top height costs \(O(T^{1/2+\epsilon}\sqrt y)=o(T)\) for small fixed \(\epsilon\), uniformly on fixed microscopic shift circles. An identical bound controls the connectors needed to move the continuous gamma-log-derivative integral to the critical line. A fixed lower edge away from ordinates costs at most \(T^\epsilon y\). The same mean-square estimate, with derivatives in \(\sigma\) and \(t\) and a unit extension of the height interval, controls a Sobolev supremum of \(P\) in the strip over a unit-height neighborhood, with fixed log losses. Thus short connectors arising when the complex shift is absorbed into the integration variable can be controlled as well. This is a proof of wide horizontal control, stronger than shifting only to a narrow strip.

For restoring endpoints after differentiation, RH Lindelöf and Cauchy imply \(|\zeta'(\rho)|\ll T^\epsilon\) in the height window. On a unit interval, a Sobolev bound for \(D^2\), multiplied by the \(O(\log T)\) maximum number of ordinates per interval, controls the sum of \(|D|^4\) at those ordinates. Summation and the continuous mean-value theorem, using \(\sum_n |[n^{-s}]D^2|^2/n=O(1)\), bound the absolute twisted derivative-weighted mass in an interval of length \(O(H)\) by \(T^\epsilon(H+Y^{2b})=o(T)\) for sufficiently small fixed \(\epsilon\). The same argument is valid if the lower or upper endpoint moves left or right by \(O(H)\), including restoration to a strict cutoff. It controls the replacement of a sharp compact interval by a smooth one with two transitions of that width. The explicit continuous and principal residue time factors change by at most \(H\log^{O(1)}T\); the coefficients there are summed harmonically.

These estimates settle the sharp contour connectors. The stationary-phase error in Lemma 7 is a different endpoint issue. Its cutoff changes when the saddle \(t=2\pi m/k\) approaches an endpoint. There are \(\asymp k\sqrt T\) candidate integers in such a transition for each \(k\), and absolute summation yields the cited scale \(y\sqrt T\) up to fixed powers and logs. Pointwise horizontal bounds for \(P\) alone do not estimate this correlated sum. The weighted review's assertion about endpoint connectors is valid in its narrow meaning and supplies no sharp improvement to Lemma 7. The prime review correctly leaves the sharp replacement pending.

## Smooth saddle replacement

Here is a local version that avoids the sharp stationary transition. Take a smooth real cutoff \(w_T(t)\) supported in \([c_0T,C_0T]\), equal to one on a prescribed comparable-height interval away from its two transition regions of width \(H=T^\kappa\), with
\[
 \|w_T^{(j)}\|_\infty\ll_j H^{-j},\qquad (2+4b)/3<\kappa<1.
\]
Construct the cutoff as a difference of two smooth averages of upper endpoints. This uses no holomorphic extension of \(w_T\). For averaging the wide horizontals over *all* real endpoint heights rather than the good set, put \(R(t)=\int_{\sigma_L}^{\sigma_R}|\zeta'/\zeta(\sigma+it)|d\sigma\) on the above strip. For almost every \(t\), the fixed-strip partial fractions and RH give
\[
 R(t)\ll \log T+\sum_{|\gamma-t|\le1}\log(2+1/|t-\gamma|).
\]
The inverse-distance singularity becomes logarithmic on integrating over \(\sigma\). Squaring on unit intervals using the zero count and integrating the squared logs gives \(\int_I R^2\ll H\log^2T\) on any transition interval \(I\) of length \(O(H)\) comparable to \(T\). The mean-square bound for \(\sup_\sigma |P(\sigma+it)|\) on such an interval is \(\ll Hy\log^{O(1)}T\), by strip Sobolev and the same mean-value bound with a factor \(\log n\). Since the endpoint averaging densities are \(O(H^{-1})\), the averaged horizontal errors have the preceding \(T^{1/2+\epsilon}\sqrt y\) bound. Isolated heights that equal zero ordinates have measure zero. The full averaged contour identity therefore gives vertically weighted integrals with the stated cutoff.

On the reflected edge the functional-equation factor in the expanded integral is \(\chi(1-s+\beta)\) with HLZ’s definition \(\zeta(s)=\chi(s)\zeta(1-s)\). This matches Lemma 7 after shifting the variable. The occurrence of \(\chi(s-\beta)\) in the short formula just after (27) is inconsistent with that convention. The phase used here and in the saddle sum \(e(-m/k)\) is that of \(\chi(1-s)\).

Let \(x=m/k\), and put \(c'=a_T-\Re\beta>1\) with all Dirichlet series absolutely convergent. After absorbing \(\beta\) into the variable, the saddled integral for each \(x\) is formed from \(\chi(1-c'-it)x^{-c'-it}\), with weight \(w_T(t+\Im\beta)\) and the outer factors \(c_k k^{-1+\beta}B_\beta(m)m^{-\beta}\) as in the reviews. At \(x\asymp T\), Stirling with differentiable remainder gives amplitude \(x^{-c'}(t/2\pi)^{c'-1/2}(1+O(T^{-1}))\) and phase \(t\log(t/(2\pi x))-t-\pi/4\). The stationary point is \(t_0=2\pi x\) and the normalized leading term is \(e(-x)w_T(t_0+\Im\beta)\).

For an elementary uniform error bound, write \(t=Tu\) and reduce the phase near the fixed-scale support and saddle to its exact quadratic by the change of variable using the signed square root of twice its normalized increment from the minimum. All derivatives on the comparable compact scale are bounded uniformly. Include the Stirling amplitude, Jacobian and cutoff in the resulting amplitude \(A\), with its factor \(T^{-1/2}\) pulled out before time integration. Set \(\delta=H/T\). Its compact support has bounded length and \(\|A^{(j)}\|_1\ll_j\delta^{-j}\). With the quadratic oscillation parameter \(T\), Fourier inversion of the Fresnel integral shows that the difference from the leading term is bounded by
\[
 T^{-1}\int_{\mathbb R}|\xi|^2|\widehat A(\xi)|d\xi
 \ll T^{-1}\delta^{-3}=T^2/H^3 .
\]
For the last bound split at \(|\xi|=\delta^{-1}\) and use \(\|A\|_1\) and \(\|A^{(4)}\|_1|\xi|^{-4}\). The phase change can be taken throughout the fixed positive compact range containing the time support and the saddle, including when the saddle lies outside the support. The amplitude is zero near its support boundary, so the estimate also holds in that case. The relative Stirling correction to the leading term is \(O(T^{-1})\), and replacing the shifted cutoff by \(w_T(t_0)\) costs \(O(H^{-1}/\log T)\). For \(x\) outside a larger comparable range the phase derivative is bounded away from zero. Repeated integration by parts with the smooth cutoff and the Stirling symbol costs \(O_j(T^{c'+1/2}x^{-c'}H^{-j})\); in the original absolute Dirichlet series this is summable with divisor-bound log powers and at most a factor \(y\). Arbitrarily large fixed \(j\) make it negligible.

The comparable \(m\asymp Tk\) terms have total absolute coefficient mass \(\ll T^{1+\epsilon}y\), from \(|B_\beta(m)m^{-\beta}|\ll T^\epsilon\) in that range and \(k^{\Re\beta}\ll1\). Thus the saddle replacement has cost
\[
 O\!\left(T^{1+\epsilon}y(T^2/H^3+T^{-1}+H^{-1})\right)=O(T^{1-\eta})
\]
for some \(\eta>0\), choosing \(\epsilon\) sufficiently small. Uniformity holds on separated microscopic shift circles. On the unreflected side the denominator is 1 and the numerator has a fixed divisor bound, so the same estimate applies there. The smoothed principal term is the same endpoint average of the sharp principal residues in §4.3. The argument improves the **smoothed** saddle error, with the sharp boundary restoration performed on the original derivative-weighted zero sum, where the \(D^2\) estimate is available.

## The estimate that remains

In the smoothed approach it suffices to obtain \(o(T\log T)\) uniformly on the three separated microscopic shift circles for
\[
 \sum_{k\le y}\frac{c_k}{k^{1-\beta}}
 \sum_{m\ge1}\frac{B_\beta(m)}{m^\beta}\,w_T(2\pi m/k)
 \left[e(-m/k)-\frac{\mu(k/(m,k))}{\varphi(k/(m,k))}\right].
\]
Here \(B_\beta(m)=[m^{-s}]\zeta(s+\lambda)\zeta(s+\alpha)\zeta(s-\beta)/\zeta(s)\). Cauchy then costs at most \(O(\log^3T)\). A real estimate after the actual three derivatives of size \(o(T\log^4T)\) suffices as well. Setting \(\lambda=0\) before the analysis loses the derivative of the quotient. The character sum on \(q=k>1\) with \((m,k)=1\) already has weight \(\tau(\bar\psi)\psi(-1)/\varphi(k)\), with all primitive characters summed; divisor and common-factor blocks also occur. The lower bound \(q\ge Y^a\) removes polylogarithmic small conductors for \(T\asymp Y\). It does not remove the \(q\asymp y\) blocks. The HLZ absolute-value hybrid large sieve retains its \(Q^2\) term and produces the three square-root-threshold powers in Proposition 11. Smooth cutoffs alone do not give the required improvement. A proof that combines the sharp signed sum and sharp saddle error directly may instead use the weighted review’s sufficient estimate for \(K_{\rm long}-M\).

It is enough to prove compact-local estimates for each fixed ratio of upper to lower height. For the remote part the established \(D^2\overline{D}^2\) asymptotic yields a prefix bound \(\ll t\log^4 t\) for the absolute pure summand with its derivative weight. Stieltjes integration bounds the strict normalized tail beyond \(RY\) by \(O(R^{-1}(1+\log^4 R))\). On compact intervals the transition bound above permits sharp endpoints and bounded smooth weights, including approximation of \((t^2+1/4)^{-1}\). Let \(Y\to\infty\) before \(R\to\infty\). No estimate for the remaining signed sum, canonical upgrade, or author correction is supplied.
