# Pintz Corollary 4 and the BGSTB fixed slab

Scoped source reading of János Pintz, arXiv:2310.04544v1, title page, §§1–3 and (3.1)–(3.16), and BGSTB arXiv:2306.04799v1, (2.5), Lemma 6(b), and §6. This is a source-dependent application of a particular density estimate. [Pintz primary PDF](../../sources/latest62_analytic2/2310.04544.pdf) [BGSTB primary PDF](../../sources/analytic/2306.04799.pdf)

## Density exponent and range

Pintz counts \(\beta\ge\sigma\) and \(0\le\gamma\le T\), with multiplicity, in (1.1). In (1.2), (1.11), \(B(\eta)\) is the slope multiplying \(1-\sigma=\eta\) in the exponent, which also has an arbitrary fixed positive loss. For \(\ell=2\), \(\alpha_2=3/4,\alpha_1=1/2\). The input (2.1) gives \(\mu(3/4)\le1/16\) and \(\mu(1/2)\le1/6\). Thus (2.4)–(2.5) give
\[
u_2\le\frac{1}{4(1-4\eta)},\qquad v_2\le\frac{1}{3(1-4\eta)}.
\]
Both branches \(4u_2\) and \(3v_2\) have the same upper bound. Consequently Corollary 4 states
\[
N(1-\eta,T)\ll_{\eta,\epsilon}T^{f(\eta)+\epsilon},
\quad f(\eta)=\frac{\eta}{1-4\eta},
\quad 0<\eta<1/4.
\]
Theorem 1’s introduction prints \(\eta<\max(1/3,2^{-\ell})\), whereas the proof at (3.1) requires \(\eta<\min(1/3,2^{-\ell})\). For \(\ell=2\), the needed range is the strict \(\eta<1/4\), which is exactly the proof range. In the difference interval the proof’s displacement \(1/4-\eta\) changes sign. This argument supplies no bound using the larger printed interval. At \(\eta=1/8\), \(f(\eta)=2\eta=1/4\). The sentence following Corollary 5 says “breaks” for an inclusive range, but the exponent improvement from Corollary 4 is strict only for \(0<\eta<1/8\). At equality the statement only gives the density-hypothesis exponent with an arbitrary power loss.

## Reconstruction of the \(\ell=2\) mechanism

Fix \(\eta\) and a small fixed internal margin \(\delta>0\). Fix \(\ell=2\), \(u=\mu(3/4)/(1/4-\eta)\), \(v=\mu(1/2)/(1/2-2\eta)\), and use \(X=T^{\delta^2},Y=T^{u+\delta}\). The source reduces to ordinates \([T/2,T]\) separated by at least one. A maximal separated set covers the original half-height interval by its unit-radius intervals. The standard unit-window zero count gives a factor \(O(\log T)\), including multiplicities. Dyadic summation in height preserves the exponent with the arbitrary loss.

For the zero detector take \(L=\max(\log Y,\log T)\), \(a_n=\sum_{d\mid n,d\le X}\mu(d)\), and weight
\[
f_Y(n)=\frac{1}{2\pi i}\int_{(3)} e^{s^2/L}(Y/n)^s\,ds/s.
\]
Shift the integral for \(M_X(\rho+s)\zeta(\rho+s)e^{s^2/L}Y^s/s\) to \(\Re s=3/4-\beta\). The pole of \(1/s\) is canceled by \(\zeta(\rho)=0\). The zeta pole at \(1-\rho\) has Gaussian suppression \(\exp(-\gamma^2/L)\). On the shifted line with \(s=3/4-\beta+it\), the Gaussian is \(\exp(-t^2/L)\) times a bounded factor, while the zeta argument has imaginary part \(\gamma+t\). For \(|t|\le T/4\) this height is comparable to \(T\), and the remaining tail is exponentially small by polynomial vertical bounds. This distinction repairs the blurred \(t\) and \(\gamma+t\) Gaussian in (3.7). The bound is \(O(T^{\delta^2+\mu(3/4)+o(1)}Y^{-(1/4-\eta)})=o(1)\) with \(\delta\) sufficiently small in terms of \(\eta\). The \(n=1\) term is \(1+o(1)\), all \(1<n\le X\) vanish, and the terms \(n>e^3Y\) are \(o(1)\) by shifting to \(\Re s=L\), as in (3.8). Therefore the remaining sum has absolute value at least \(1-o(1)\). This uses its modulus. With the integrals as printed its signed main term would be \(-1\), since the full integral is \(o(1)\). The coefficients have divisor growth and polylogarithmic weight by shifting to \(\Re s=1/L\).

Dyadic subdivision and pigeonholing give a block at \(U\le e^3Y\) with mean absolute value over the \(K\) separated zeros \(\gg1/\log T\). Let \(R=T^{v+O(\delta)}\) be the required minimum length, with fixed positive margin. If \(U\ge R/2\), square the polynomial, so \(U^2\ge R\) for large \(T\) and its length is \(O(Y^2)\). Otherwise take the least \(h\ge2\) with \(U^h\ge R\). If \(h=2\), \(U^h\le O(Y^2)\). If \(h\ge3\), \(U^{h-1}<R\) gives \(U^h\le R^{3/2}\). The lower cutoff \(X\) bounds \(h\) in terms of the fixed margins. Hölder and a bounded dyadic subdivision of \([U^h,(2U)^h]\) give a new block of length scale \(M\), with mean absolute value \(\gg_{\eta,\delta}(\log T)^{-h}\), coefficients \(T^{o(1)}\), and
\[
T^{v+\delta}\ll M\ll T^{\max(2u,3v/2)+O(\delta)}.
\]
Constants in the cutoff \(R\) may be enlarged to ensure the indicated lower bound after subdivisions.

For each off-diagonal term in the Halász Cauchy–Schwarz step, put \(s_0=1-\eta_j-\eta_k+i(\gamma_j-\gamma_k)\), so \(\Re s_0\ge1-2\eta>1/2\) and \(1\le|\Im s_0|\le T/2\). For \(M\le T\), Perron with height \(2T\) and contour shift to \(\Re(s_0+w)=1/2\) gives
\[
\left|\sum_{n\in I(M)}n^{-s_0}\right|
 \ll_{\eta,\delta} M^{2\eta}/|\gamma_j-\gamma_k|+T^{-c_{\eta,\delta}}.
\]
For the bound one can put the two cutoffs at half-integers and use truncated Perron with error \(O(M^{1-\Re s_0}\log T/T)\) up to a bounded factor. The zeta pole gives the first term. On the left edge the estimate is \(M^{-(\Re s_0-1/2)}T^{\mu(1/2)+o(1)}\), with logarithms absorbed in \(o(1)\), so the lower length margin gives a fixed power saving. For the horizontal edges to the left of \(\Re w=0\), \(T^{\mu(1/2)-1+o(1)}\) suffices. To the right use \(M^\kappa\le T^\kappa\), \(\kappa\le1-\Re s_0+1/L\), and \(\mu(\Re s_0)<\Re s_0\) with a uniform margin. For \(M\ge T\), the first derivative bound and partial summation give \(O(M^{2\eta}/|\gamma_j-\gamma_k|)\), since the phase derivative in cycles is of magnitude \(|\gamma_j-\gamma_k|/(2\pi n)\) and stays away from all nonzero integers. This is the split in (3.3)–(3.6).

The diagonal contributes \(O(K M^{2\eta})\) up to a fixed factor. Unit separation gives \(\sum_{j\ne k}|\gamma_j-\gamma_k|^{-1}\ll K\log(2K)\). Therefore Cauchy–Schwarz and absorption of the \(T^{-c_{\eta,\delta}}K^2\) contribution give \(K\ll M^{2\eta}T^{o(1)}\), reproducing (3.16) on the stated range after making the internal margin sufficiently small for a prescribed final exponent loss. This reconstruction concerns the \(\ell=2\) range only.

## BGSTB full-height slab

Fix \(0<d\le1/16\), let \(I=[7/8+d,1-d]\), \(L=\log T\), and define the full-height slab sum
\[
H_I(T)=\sum_{\substack{0<\gamma\le T\\ \beta\in I}}
 \frac{T^{2\beta-1}}{1+L^2(\beta-1/2)^2}
\]
with multiplicities. The slab degenerates to a singleton at \(d=1/16\) and is empty if \(d>1/16\). Set
\[
\Delta_d=\min_{\eta\in[d,\,1/8-d]}
 \left(2\eta-\frac{\eta}{1-4\eta}\right)>0.
\]
The gap is concave since \(f''(\eta)=8/(1-4\eta)^3>0\), so the minimum is the smaller endpoint value. The normalized exponential weight has exponent \(2\beta-2=-2\eta\). Partition \([d,1/8-d]\) into a fixed finite set of cells \([a,b]\) of length at most \(\epsilon/4\), that is, independent of \(T\). All zeros in a cell are covered by the inclusive count \(N(1-b,T)\) and have normalized weight at most \(C_d T^{-2a}/L^2\). Apply Corollary 4 at each right endpoint with exponent loss \(\epsilon/2\). As
\[
f(b)-2a\le-\Delta_d+2(b-a),
\]
we obtain \(H_I(T)\ll_{d,\epsilon}T^{1-\Delta_d+\epsilon}/L^2\). For a singleton use the density bound directly. The finite grid avoids assuming uniformity in a continuum of thresholds or circularity between the grid and \(T\). Both boundary lines of the slab are included.

For the BGSTB far-pair sum write \(m=\max(L|\beta-1/2|,L|\beta'-1/2|)\), \(x=L|\beta-\beta'|\ge1\), \(w=L(\gamma-\gamma')\). Lemma 6(b) gives modulus \(\ll e^x/(x^2+w^2)\), with the displayed bounded \(4/(4-z^2)\) factor absorbed. Since \(x\le 2m\), writing \(r=2m-x\) gives \((1+m^2+w^2)/(x^2+w^2)\ll(1+r)^2\). Hence each pair contributes at most \(C e^{2m}/(1+m^2+w^2)\). Charge a maximizer and use same-height reflection to put it on the right of \(1/2\). The unit-window count (2.5) gives \(O(L/(1+m^2))\) after summing over all partners. The shell at height distance less than 1 gives this directly and shells \(j\le|\gamma-\gamma'|<j+1\) have summed bound \(O(L\sum_{j\ge1}(1+m^2+j^2L^2)^{-1})=O(1/L)\). The resulting far-pair contribution charged to a right maximizer in \(I\) is \(O(LH_I(T))=O_{d,\epsilon}(T^{1-\Delta_d+\epsilon}/L)\), hence \(o(TL)\). A pair merely containing a zero in \(I\) can have its maximizer outside \(I\). The conclusion concerns the charged contribution.

## Boundary test

At \(\beta=7/8\), a single abstract slab atom of multiplicity count \(\lfloor T^{1/4}L^2\rfloor\) satisfies every fixed-\(\epsilon\) Corollary 4 estimate at each fixed threshold for its counting profile. For larger thresholds it is absent, and for smaller thresholds use the strict increase of \(f\). Its \(H_I(T)\) contribution would be comparable to \(T\) if this endpoint were included. Its copies can be spread over unit height windows if a local \(O(\log T)\) count is also imposed. Thus the power-loss density bound alone does not give the normalized weighted saving at \(7/8\), even with the logarithmic denominator. This is a test of the inference from these bounds and does not construct zeta zeros or rule out a stronger input. The fixed slab estimate by itself supplies no result for the rest of the BGSTB far-pair sum.
