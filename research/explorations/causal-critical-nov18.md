# The critical normalization of the centered octave norm

Proposed synthesis of the dyadic converse and the classical Cramér mean-square bound. The critical exponent and logarithm can both be retained. Write
$$
 E(y)=\pi(y)-\int_2^y\frac{dt}{\log t},\qquad
 V_j=\inf_{c\in\mathbb R}\left(\int_{2^j}^{2^{j+1}}|E(y)-c|^2\frac{dy}{y}\right)^{1/2}.
$$
Then RH is equivalent to
$$
 \sup_{j\ge1} j(\log2)\,2^{-j/2}V_j <\infty.
$$
If RH fails the limsup is infinite. In the finite case its numerical value is at least 0.1969 by the independent residue argument. [Converse and finite lower bound](causal-octave-nov18.md)

**Converse.** The displayed bound gives the hypothesis of the disjoint-octave criterion for each $a>1/2$. That proof uses Ingham density and applies with no restrictions on the fitted constants.

**Forward direction.** The classical Cramér theorem under RH is
$$
 \int_2^x |\psi(t)-t|^2\,dt\ll x^2.
$$
Here $\psi(t)=\sum_{n\le t}\Lambda(n)$. On a block $X\le t\le2X$ this gives an $L^2(dt/t)$ norm $O(\sqrt X)$. The prime power correction satisfies $0\le\psi(t)-\vartheta(t)\ll\sqrt t$ unconditionally: squares contribute $O(\sqrt t)$ by Chebyshev, and powers of exponent at least three cost $O(t^{1/3}\log t)$. Partial summation gives
$$
 E(t)=\frac{\vartheta(t)-t}{\log t} +\int_2^t\frac{\vartheta(u)-u}{u\log^2u}\,du+\frac{2}{\log2}.
$$
For each dyadic interval ending at $Y$, Cauchy–Schwarz bounds the integral of the absolute error term in the integral by $O(\sqrt Y/\log^2 Y)$, adjusting constants on the lowest blocks. Summing the geometric sequence through $2X$ yields the same order $O(\sqrt X/\log^2 X)$ for the running integral on the block. The first term has block norm $O(\sqrt X/\log X)$. Taking $c=0$ in the infimum proves the forward implication.

### Reconstructing the mean-square input from the zeros

For clarity, Cramér's estimate here only needs the following elementary consequence of the classical von Mangoldt explicit formula and zero count. Under RH, away from the countable prime-power endpoints, write
$$
 e^{-v/2}(\psi(e^v)-e^v)
 =-\lim_{U\to\infty}\sum_{|\gamma|\le U}\frac{e^{i\gamma v}}{1/2+i\gamma}+O(e^{-v/2})
 \qquad(v\ge\log2).
$$
One may take the usual symmetric sequence of good truncation heights. The trivial-zero terms and the constant are bounded in the indicated range. For any finite exponential sum with coefficients $b_\gamma$, its squared integral on any translate of $[0,\log2]$ is bounded by
$$
 C\sum_{k\in\mathbb Z}\left(\sum_{k\le\gamma<k+1}|b_\gamma|\right)^2.
$$
Indeed majorize the interval indicator by a translate of a smooth compactly supported nonnegative function. Two integrations by parts bound its Fourier transform by $C/(1+|u|^2)$. Group the resulting double sum by unit intervals and apply the $\ell^1$ convolution inequality with kernel $(1+|k|^2)^{-1}$. The implied constants are translation invariant. The zero count in a unit interval is $O(\log(2+|k|))$, so for $b_\gamma=1/(1/2+i\gamma)$ the sum over $|k|\ge K\ge2$ is $O(\log^2(2K)/K)$. This proves uniform block $L^2$ convergence of the series. The explicit formula identifies its limit almost everywhere. Restoring $e^{v/2}$ gives the required block bound, and summing squared blocks gives Cramér's estimate.

Thus the classical cancellation from oscillations within one fixed-length logarithmic interval suffices for the forward direction at the exact scale. The unknown estimate is the converse hypothesis for the actual primes.

## Recurrence of an arithmetic profile on dyadic blocks

There is a stronger unconditional bound on the limsup: **it exceeds 0.26**. The proof uses a mechanism different from reading residues at finitely many frequencies. If RH fails, the converse already makes the limsup infinite. Suppose RH holds. For every integer $m\ge1$, the following fixed profile occurs as an $L^2[0,L]$ subsequential limit of the functions $jL\,2^{-j/2}E(2^j e^u)$, where $L=\log2$:
$$
 H_m(u)=2^{-m/2}\big[\psi(t)-t+\log(2\pi)+\tfrac12\log(1-t^{-2})\big]-e^{u/2},
 \qquad t=2^m e^u .
$$
Values at the jumps are irrelevant. This is a statement concerning actual prime counting even though its proof passes through the zeros.

Indeed partial summation as above shows the normalized integral remainder is $O(1/j)$ uniformly. Replacing $jL/\log(2^je^u)$ by 1 costs $O(1/j)$ in block norm. The square correction $(\psi(y)-\vartheta(y))/\sqrt y$ tends uniformly to 1 as $y\to\infty$ by the prime number theorem at $\sqrt y$ and the elementary higher-power estimate. Thus the profile differs by $o(1)$ in block norm from
$$
 -e^{u/2}\left(1+\sum_\gamma e^{ijL\gamma}e^{iu\gamma}/(1/2+i\gamma)\right).
$$
The tail after $|\gamma|>K$ has norm $O(\log(2K)/\sqrt K)$ uniformly in $j$ by the block estimate. There exist arbitrarily large integers $j$ for which the first finitely many phases approach $e^{imL\gamma}$ simultaneously. This follows by recurrence of a rotation on a finite torus, or by partitioning that torus into small boxes and subtracting two arbitrarily separated indices landing in the same box, then adding $m$. Diagonal selection and the uniform tail prove convergence to the series with $j=m$. Substitution of the full classical explicit formula on that fixed octave, including its constant and trivial zeros, gives $H_m$ above.

Orthogonal projection off constants is continuous. Hence the limsup in question is at least the distance of each $H_m$ from the constants. For $m=10$ we enclosed this distance by an elementary sieve of the prime powers through 2047 and interval integration on $[1024,2048]$ with measure $dt/t$. Each integration cell is confined to one integer step. Its exact logarithmic length multiplies ball enclosures for both the profile and its square. The script omits the additive constant $\log(2\pi)/32$ and adds 1 to limit interval overestimation in the variance calculation. Its strict ball comparison certifies that the variance is greater than $0.26^2$. [Reproduction script](check_recurrent_octave_nov18.py)
