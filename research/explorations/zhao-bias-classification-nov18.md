# Exact classification for independent ordinates in Zhao's quadratic prime bias

Assume the quadratic character's GRH, central nonvanishing, and rational linear independence of its distinct positive nontrivial ordinates. Then the eventual negative inequality of [Zhao's §8(2)](https://doi.org/10.1007/s40993-025-00640-y) holds **exactly** for the following nineteen fundamental discriminants:
\[
 -23,-20,-15,-11,-8,-7,-4,-3,5,8,12,13,17,21,24,28,33,40,41 .
\]
For the nineteen, their own GRH suffices. For the other discriminants the claimed negative sign fails along an unbounded sequence under the stated hypotheses. There is no undetermined equality at the threshold in this classification. Only the stronger assumptions used for this complete list go beyond the published question.

Put \(S=\sum_\rho 1/|\rho(\rho+1)|\), counting multiplicity, including both conjugates. The [normalized explicit formula](zhao-bias-kernel-nov18.md) and Kronecker's theorem applied to successively larger finite sets of frequencies give \(\limsup I_D=-2/3+S\) when the positive ordinates are rationally independent and there is no central zero. Indeed for each frequency the desired complex phase makes its coefficient negative real. Absolute convergence controls all remaining frequencies uniformly. For the sufficiency direction \(S<2/3\), the triangle inequality alone gives \(\limsup I_D<0\).

For \(c\ge1/2\), let \(s=1/2+c\), \(a=\mathbf1_{D<0}\). The real completed logarithmic derivative gives
\[
 M(c)=\sum_\rho\frac{1}{c^2+\gamma^2}
 =\frac{\log(|D|/\pi)+\psi((s+a)/2)+2(L'/L)(s,\chi_D)}{2c}.
\]
In the Hadamard product centered at \(1/2\), conjugates have opposite ordinates and the completed function is even. The sum of their logarithmic derivatives is \(2c/(c^2+\gamma^2)\) per pair, with a central zero of multiplicity \(m\) contributing \(m/c\). This proves the formula including endpoints. In particular \(S\ge M(3/2)\). At \(s=2\), \((L'/L)(2,\chi)\ge-\sum\Lambda(n)n^{-2}>-0.57\). Digamma monotonicity gives \(\psi((2+a)/2)\ge-\gamma_E\). Since \(\log(130/\pi)-\gamma_E-1.14>2\), **every conductor at least 130 has \(S>2/3\)**.

The exact integral average
\[
 S=\frac2\pi\int_0^{\pi/2}M\left(\sqrt{1/4+2\sin^2\theta}\right)d\theta
\]
follows termwise by \(t=\tan\theta\). The integrand decreases, so equally spaced endpoint rectangles give two rigorous bounds using only real positive \(L\)-function arguments. In the [small-conductor calculation](../../experiments/X-nov18-quadratic-bias/classify_li.py), the Dirichlet series and its derivative are evaluated by summing the deflated Hurwitz zeta functions over one character period. The deflation is valid since the character sums to zero. Arb interval evaluations and at most four panels at each conductor suffice. The [integer-directed table](../../experiments/X-nov18-quadratic-bias/small-norms.tsv) records all 79 discriminants in the remaining range. Also Cauchy–Schwarz gives \(S\le\sqrt{M(1/2)M(3/2)}\), used as an independent upper check for all nineteen in the [refinement](../../experiments/X-nov18-quadratic-bias/refined.tsv).

## Individual determinations without independence

For \(1<|D|\le10,000\), a reflected prime-tail and low-zero [census](../../experiments/X-nov18-quadratic-bias/README.md) unconditionally certifies both signs for 6,053 of the 6,086 nonprincipal discriminants. For 14 characters the last step uses a single Hardy sign-change interval \(((j-1)/26,j/26)\) with \(j\le3\). This certifies a positive zero with \(|1/(\rho(\rho+1))|>2/3\) under GRH. The central point is nonzero by its separate real-value enclosure and the published real-zero computations. Apply the [Bohr coefficient bound](zhao-bias-central-nov18.md); a nonnegative function \(K+2/3\) cannot have a coefficient greater in magnitude than its mean. The [off-critical dichotomy](zhao-bias-unconditional-nov18.md) disposes of a possible failure of individual GRH. The nineteen negative cases have the expected sign if and only if their individual GRH holds, by the same real-zero dichotomy. The other fourteen in this finite accounting have conductor at most 73.
