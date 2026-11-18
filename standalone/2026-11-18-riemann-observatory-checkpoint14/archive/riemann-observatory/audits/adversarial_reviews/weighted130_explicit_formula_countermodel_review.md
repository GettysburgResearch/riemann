# Independent check of a test-function countermodel for the Bombieri–Lagarias explicit formula

The proposed localized modulation construction works. It gives a real smooth test satisfying the literal (A) and (B) on manuscript p. 5 for which all arithmetic terms on p. 6 are finite, but the stated raw symmetric height sum is not Cauchy. The construction uses ordinary zero counting, without RH or any assumptions on simple zeros or short gaps. This is a targeted finding about the archived author manuscript, pending director adjudication. [Pinned author manuscript](../../sources/uniform121_bombieri_lagarias/bombieri_lagarias_author.pdf) · [Earlier whole-manuscript review](weighted121_bombieri_lagarias_whole_skeptic.md)

## Literal test and summation convention

I rechecked rendered pp. 5–6 of the 12-page manuscript with SHA-256 \(\texttt{cd13c8560f961c68e21256e5ba107bdd08fa7f34ce1e2cffbd4b63a16e8d48e0}\). Condition (A) asks for continuous differentiability on \((0,\infty)\) except finitely many permitted first-kind jumps, with the midpoint convention. Condition (B) asks for \(f(x)=O(x^\delta)\) near zero and \(f(x)=O(x^{-1-\delta})\) near infinity for some \(\delta>0\). It imposes no tail bound on \(f'\). The “Explicit Formula” display says that its zero side is the limit of the sums over \(|\Im\rho|\le T\). This is a symmetric **height** cutoff, with no averaging or taper. The journal PDF was not checked in this review.

## The test and the carrier estimates

Fix \(\delta>0\), \(0<r<1/5\), and a nonnegative nonzero \(\psi\in C_c^\infty((-r,r))\). Evenness is allowed but not needed. Choose positive carrier frequencies \(\Gamma_j\) as below. Put
\[
 a_j=e^{-(1/2+\delta)j},\qquad
 F(t)=\sum_{j\ge1}a_j\psi(t-j)\cos(\Gamma_jt),\qquad
 f(x)=x^{-1/2}F(\log x).
\]
The supports are disjoint and locally finite in \(t\), so \(f\) is real and \(C^\infty\) on its domain. It vanishes on a neighborhood of \(x=1\) and on \((0,1]\). On a packet \(t=j+O(r)\), \(|F(t)|\ll e^{-(1/2+\delta)t}\), which gives the required bound \(f(x)=O(x^{-1-\delta})\). Neither differentiability nor this estimate places a restriction on \(\Gamma_j\).

Let
\[
 J_\beta(v)=\int_{\mathbb R}\psi(u)e^{(\beta-1/2)u}e^{ivu}\,du,
 \qquad 0\le\beta\le1 .
\]
For each fixed integer \(M>0\), integration by parts on the fixed compact support gives \(|J_\beta(v)|\ll_M(1+|v|)^{-M}\) uniformly in \(\beta\). Absolute convergence and the substitution \(x=e^t\) give the exact two-carrier expression
\[
 \widehat f_j(\beta+i\gamma)=
 \frac{a_j}{2}e^{(\beta-1/2)j}
 \left[e^{i(\gamma-\Gamma_j)j}J_\beta(\gamma-\Gamma_j)
       +e^{i(\gamma+\Gamma_j)j}J_\beta(\gamma+\Gamma_j)\right].
\]
The total Mellin transform is the sum of these expressions. Absolute convergence is uniform in \(0\le\beta\le1\), since \(\sum_j a_j e^{(\beta-1/2)j}\le\sum_j e^{-\delta j}\).

Take \(c>0\) fixed and small enough that \(\cos(c(1+r))>1/2\). When \(|\gamma-\Gamma_j|\le c/j\), the real part of the first bracketed term is the integral of \(\psi(u)e^{(\beta-1/2)u}\cos((\gamma-\Gamma_j)(j+u))\), and is at least \(c_\psi>0\) uniformly in \(\beta\) and \(j\). Thus the matching carrier contributes a real quantity \(\gg e^{-(1+\delta)j}\), even at the least favorable endpoint \(\beta=0\). No phase extra to \(\cos(\Gamma_jt)\) is needed.

Impose \(\Gamma_{j+1}\ge4\Gamma_j\), with all carriers large. In the same testing window and for every \(k\ne j\), both \(|\gamma\pm\Gamma_k|\) are at least a fixed positive multiple of \(\Gamma_j\). This includes all future carriers. Also \(|\gamma+\Gamma_j|\gg\Gamma_j\) for the unmatched term of the current packet. Summing the off-carrier estimates using the convergent majorant \(\sum_k e^{-\delta k}\), their total absolute contribution is \(O_M(\Gamma_j^{-M})\). This single lacunarity estimate removes any need to choose future phases against a previously selected window. Taking \(\Gamma_j\) large enough to make this at most half the main lower bound gives
\[
 \Re\widehat f(\beta+i\gamma)\gg e^{-(1+\delta)j}
 \quad\text{uniformly for }0\le\beta\le1,\quad
 |\gamma-\Gamma_j|\le c/j .
\]

## Selecting the zero clusters

For each successive \(j\), choose \(X_j\) so large that \(X_j\ge 8X_{j-1}\) and \(\log X_j\ge j^2 e^{(1+\delta)j}\), increasing it further to meet the preceding off-carrier bound. The Riemann–von Mangoldt formula gives \(N(2X_j)-N(X_j)\gg X_j\log X_j\) for all sufficiently large \(X_j\). Partition \((X_j,2X_j]\) into intervals of length at most \(c/(2j)\) using \(O(X_jj)\) intervals. One of them contains \(\gg\log X_j/j\) positive ordinates counted with multiplicity. Choose its midpoint as \(\Gamma_j\). This choice gives the imposed lacunarity and places every selected ordinate in \(|\gamma-\Gamma_j|<c/j\). It asks for no zero count at an individual preassigned short interval.

Choose \(T_j^-<T_j^+\) bracketing the selected interval, inside \([\Gamma_j-c/j,\Gamma_j+c/j]\), with neither endpoint a zero ordinate. This is possible because the selected interval has width at most \(c/(2j)\) and the ordinates are locally finite. All positive ordinates added between these two heights have the same uniform positive lower bound on their real Mellin values, whether or not they belonged to the selected interval. Since \(f\) is real, the contribution of their negative conjugate ordinates is twice the real part. Thus the difference of the two raw symmetric partial sums is real and bounded below by
\[
 \gg e^{-(1+\delta)j}\frac{\log X_j}{j}\gg j.
\]
The endpoint sequences tend to infinity, so the prescribed zero sum fails the Cauchy criterion. This argument already works without selecting individual \(\beta\)'s or assuming that zeros in the selected bin are simple.

## Other terms and scope

For the source involution \(\widetilde f(x)=x^{-1}f(1/x)\), \(\widetilde f\) vanishes for \(x\ge1\) and is \(O(x^\delta)\) near zero. Both unweighted integrals in the explicit formula are absolutely finite. The prime terms converge absolutely since \(\Lambda(n)\ll\log n\) and \(f(n)\ll n^{-1-\delta}\). The value at 1 and both functions near 1 vanish, so there is no archimedean singularity or issue with finite-part normalization there. The remaining gamma integral has an integrable tail. Hence the discrepancy cannot be attributed to a divergent right-hand side.

One can even make \(f\) nonnegative by replacing each cosine by \(1+\cos(\Gamma_jt)\). The new zero-frequency packet terms are uniformly \(O_M(\Gamma_j^{-M})\) in each testing window by the same absolute summation, so the proof is unchanged.

This witness addresses the broad displayed class with the raw height cutoff. It says nothing against explicit formulas with stronger derivative or Fourier decay, alternate specified summation procedures, or the compact piecewise smooth approximants used for Theorem 2. It does not adjudicate Weil's original hypotheses or assign a finding to the unverified publisher manifestation. No canonical file was edited.
