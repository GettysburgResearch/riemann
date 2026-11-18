# From the field census to an individual Riemann-hypothesis equivalence

For a number field \(K\) let \(M_K\) denote its prime-ideal harmonic Mertens constant, and put
\[
 J_K(X)=\int_2^X\left(\sum_{N\mathfrak p\le x}(N\mathfrak p)^{-1}-\log\log x-M_K\right)dx.
\]
For an individual field one can check an unconditional finite condition excluding the real off-critical zeros, in addition to its spectral test on GRH. Together these give the actual equivalence
\[
 \text{RH for }\zeta_K\qquad\Longleftrightarrow\qquad
 J_K(X)>0\quad\text{for every sufficiently large }X .
\]
The direction from the arithmetic sign to zero location does not assume GRH for another field. [Zhao's question in §8(3)](https://doi.org/10.1007/s40993-025-00640-y)

## The profile on GRH

For a fixed field satisfying GRH, count all zero ordinates with multiplicity. Then
\[
 \frac{\log X}{\sqrt X}J_K(X)
 =2+\sum_\rho\frac{e^{i\gamma\log X}}{1/4+\gamma^2}+o_K(1).
\]
Indeed put \(H(x)=\int_2^x(\vartheta_K(t)-t)dt\) for the prime ideal Chebyshev function. In the once-integrated explicit formula for \(\psi_K\), each nontrivial zero contributes \(-x^{1+\rho}/[\rho(1+\rho)]\) with an absolutely convergent sum. The archimedean terms and lower endpoints cost \(O_K(x\log^2(2x))\). Removing squares contributes \(-(2/3+o(1))x^{3/2}\) by the prime ideal theorem for \(K\), and the higher powers cost \(O_K(x^{4/3}\log^2(2x))\). In particular \(H=O_K(x^{3/2})\). A further partial summation gives \(P(x)=\int_2^x(\pi_K(t)-\operatorname{li}(t))dt=H(x)/\log x+O_K(x^{3/2}/\log^2x)\), by integrating the derivative of \(1/\log t+(x-t)/(t\log^2t)\) against \(H(t)\).

The integrated harmonic identity now gives \(J_K(X)/X=P(X)/X^2-2\int_X^\infty P(t)t^{-3}dt+O_K(1/X)\). For a zero term its leading coefficient is \((-1+2/(1-\rho))/[\rho(1+\rho)]=1/[\rho(1-\rho)]\). Integration by parts bounds the log-weight correction uniformly after the summable reciprocal-square denominator, and the square term produces \(2\). This proves the displayed profile. In particular \(B_K<2\) gives an eventual strict positive sign. If the distinct positive ordinates are linearly independent over the rationals, Kronecker approximation gives the limiting inferior \(2+8m-B_K\), where \(m\) is the central multiplicity; the central term itself contributes \(4m\). Thus the strict spectral test also distinguishes the signs outside the list under GRH, absence of a central zero, and this specified independence, provided equality at the threshold has been excluded. Repeated zeros cause no additional condition.

## The off-line obstruction and the real segment

Suppose \(\zeta_K\) has no real zero in \((1/2,1)\). For \(\Re s>1\) two integrations give
\[
 s(s-1)\int_2^\infty J_K(x)x^{-s-1}dx
 =\sum_{\mathfrak p}(N\mathfrak p)^{-s}
  -2^{1-s}(\log\log2+M_K)-E_1((s-1)\log2),
\]
where \(E_1(z)=\int_1^\infty e^{-zt}dt/t\) on the positive half-plane. The prime-ideal sum differs from \(\log\zeta_K(s)\) by a function holomorphic on \(\Re s>1/2\). The logarithms of \(s-1\) cancel at 1, since \(E_1((s-1)\log2)+\log(s-1)\) extends holomorphically there. The numerator vanishes at 1 by \(J_K(x)=o(x)\) and the defining Mellin integral. Hence the quotient is regular at every real \(s>1/2\). A nonreal zero with real part \(\beta>1/2\) gives a nonremovable logarithmic singularity, detected also by the pole after differentiation of the prime-ideal series. By Landau's singularity theorem applied to the Mellin transforms of \(C x^c\pm J_K(x)\), for each \(1/2<c<\beta\) both signed ratios \(\pm J_K(x)/x^c\) have infinite limiting superior. Indeed an eventual one-sided bound would give an eventually nonnegative transform with abscissa at least \(\beta\), but regular continuation across the whole real interval \((c,\infty)\). A bounded initial segment has entire transform. Thus failure of GRH forces violations of the sign whenever the indicated real segment is clear.

## Two unconditional finite certificates

Write \(D_K(s)\) for the logarithmic derivative of the entire completed function \(s(s-1)\Lambda_K(s)\). For real \(s>1\), the real-part Hadamard formula is \(D_K(s)=\sum_\rho \Re(1/(s-\rho))\) without a constant term, by conjugation and reflection across \(1/2\). Every term is positive, without any assumption on the zeros. A real zero \(\beta\in(1/2,1)\) and its mate contribute at least \(2/(s-1/2)\) by convexity. There are two practical ways to exclude such a pair.

* If the analytic quantity \(2D_K(1)<2\), the pair is impossible, since its contribution to \(2D_K(1)\) would be \(2/[\beta(1-\beta)]\ge8\). A central zero costs 4. Evaluation of \(2D_K(1)\) by the [Dedekind contour](zhao-field-catalogue-bounds-nov18.md) or an abelian L-jet does not require GRH; only the identification with \(B_K\) does.
* At any single \(s>1\), discard all prime-ideal terms over \(p>P\) in \(\zeta'_K/\zeta_K(s)\) when evaluating \(D_K(s)\). All discarded terms are nonpositive. If the resulting upper bound times \(s-1/2\) is less than 2, it excludes every real zero in \((1/2,1)\). The [interval checker](../../scripts/check_zhao_real_zero_exclusion_nov18.py) implements this test from a field polynomial with the exact ramified Euler factors included. This version allows a central zero and suffices for the Landau argument.

Either certificate, together with a strict passing spectral result when GRH holds for the field, proves the individual equivalence.
