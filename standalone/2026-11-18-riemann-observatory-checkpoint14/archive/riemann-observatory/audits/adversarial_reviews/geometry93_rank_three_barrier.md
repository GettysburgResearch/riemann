# Derivative-fourth rooted CUE, rank-three moment window and first correction

Fix \(0<a<b\), and set \(H=\log(b/a)\), \(m_j=\int_a^b x^{j-1}\,dx\), \(d=m_1\). Draw a joint Haar \(U(N)\) and marked eigenangle law with global density proportional to \(|Z'_U(\theta_{\rm root})|^4\) relative to Haar times the uniform label. Rotate the marked eigenangle to zero and include it in the negative cosine statistic
\[
 C_N=-\sum_{aN<k\le bN}\frac{1}{k}\sum_{j=1}^N\cos(k(\theta_j-\theta_{\rm root})).
\]
The limiting raw moments through each degree \(r\) with \(rb\le1\) equal \(r![z^r]\exp(2Hz+Hz^2/4)P_3(z)\), with \(P_3\) defined below. The polynomial takes a negative value at \(1/d\), precluding an all-order probability representation by this formal series. At the first crossing \((r-1)b\le1<rb\), the actual raw cosine moment is strictly larger than the extrapolated one.

## Root law and finite determinant

The derivative at its simple marked root has modulus \(\prod_{j\ne{\rm root}}|1-e^{i(\theta_j-\theta_{\rm root})}|\). The Haar Vandermonde squared contributes exponent two and the tilt adds four, yielding a free-particle density proportional to \(|\Delta|^2\prod|1-e^{i\theta}|^6\) on \(N-1\) free points. This also follows from Hughes–Keating–O’Connell §2(a), (2.2), (2.3), (2.8), with their moment parameter \(k=2\). There is one deterministic root in the observable. Global reweighting is required for the free density. [Hughes–Keating–O’Connell](../../sources/classical63_lfunctions/hko2000.pdf) · [Circular Jacobi density, (1.6)](../../sources/prime77_rmt/bourgade_nikeghbali_rouault_2009.pdf)

The free density is the projection DPP onto the span of \((w-1)^3w^j\), \(0\le j\le N-2\), in the circle variable \(w=e^{i\theta}\). This span has maximal degree \(N+1\), so \(n=N+2\) ambient modes and three removed modes. The removed space is spanned by the coefficient vectors for evaluation, first derivative, and second derivative, which are polynomials in the mode index of degree at most two. Fix positive-leading-coefficient orthonormal columns \(U\) for these discrete polynomials. The columns, multiplied by \(\sqrt n\) and evaluated in the grid variable \(s=j/n\), converge coefficientwise to the normalized shifted Legendre polynomials
\[
 u_0(s)=1,\qquad u_1(s)=\sqrt{12}(s-\tfrac12),\qquad
 u_2(s)=\sqrt5\big(6(s-\tfrac12)^2-\tfrac12\big).
\]
Set \(H_N=\sum_{aN<k\le bN}1/k\), \(f_N(\theta)=-\sum_{aN<k\le bN}\cos(k\theta)/k\), \(A=T_n(e^{zf_N})\), and \(K_N=\lfloor bN\rfloor\). The orthogonal-complement form of Jacobi's identity gives
\[
 \mathbb E e^{z C_N}=e^{-H_N z}\det A\det(U^*A^{-1}U).
\]
Indeed the free mgf is the determinant of the compression of \(A\) onto the free span, by integrating its squared basis determinant with the exponential at each angle. The root contributes the one factor \(e^{-H_N z}\). [Rank-two finite identity and classical antecedents](prime84_cue_moment_window.md)

## Inverse coefficients and the averaged matrix

Tag each Fourier source independently. For a monomial with positive and absolute negative frequency totals \(P,Q\le n\), inverse-matrix Neumann paths cannot visit both \(j<0\) and \(j\ge n\). Such a path would need total displacement at least \(n+1\) in one sign. Inclusion–exclusion expresses its coefficient as the sum of the two half-line inverse coefficients minus the full-line inverse coefficient. The half-line Toeplitz factorizations have inverse triangular factors in reversed order. For the \((i,j)\) entry, writing \(i=j+P-Q\), these respectively impose \(j\ge Q\) and \(j<n-P\) beyond the restrictions \(i,j\in[0,n-1]\) of the full-line entry. The result compresses the product of shifted basis values to the oriented sum in \(j\) from \(Q\) up to \(n-P\), excluding the upper endpoint in the ordinary order. If \(n-P<Q\), this is minus the sum from \(n-P\) up to \(Q\). The orientation handles overlap and gap with one formula, including \(P+Q=n\), when the sum vanishes. This derivation is independent of the rank of \(U\). Each side of the oriented finite sum extends as a polynomial in \(P,Q\) by discrete antidifferentiation. [Finite path proof and endpoint check](uniform86_cue_window_adjudication_input.md)

Use \(p=P/n,\ q=Q/n,\ \ell=1-p-q,\ D=p-q\). The polynomial limit of the oriented sum has entries
\[
 B_{ij}(p,q)
 =\int_{-\ell/2}^{\ell/2}u_i(\tfrac12+y+D/2)u_j(\tfrac12+y-D/2)\,dy .
\]
These are polynomial expressions also for \(\ell<0\). The finite grid sums converge uniformly when \(p,q\) stay bounded, because discrete polynomial antiderivatives split into their continuous leading terms and a uniformly \(O(1/n)\) remainder. The \(\ell<0\) finite sums use the same polynomial identity, which also gives uniform convergence for the extrapolated first crossing.

The positive and negative triangular inverse symbols \(e^{-zf_{N,+}},e^{-zf_{N,-}}\) each have coefficient mass \(e^{H_N z/2}\). After dividing by this mass, their scaled frequency variables have independent formal cumulants \(z m_{j,N}/2\), where \(m_{j,N}=\sum_{aN<k\le bN}k^{j-1}/n^j\to m_j\). Define the formal expectation \(\mathcal E\) by the joint moment-generating exponential
\[
 \mathcal E e^{up+vq}
 =\exp\left\{\frac z2\int_a^b(e^{ux}+e^{vx}-2)\frac{dx}{x}\right\}.
\]
Then \(D_{ij}(z)=\mathcal E B_{ij}(p,q)\) and \(P_3(z)=\det(D_{ij}(z))_{0\le i,j\le2}\). The three-by-three determinant supplies mass \(e^{3Hz}\), and the deterministic root offsets \(e^{-Hz}\). The base \(U(n)\) determinant has the stable Wick coefficients of \(e^{H_N z^2/4}\) whenever the positive and negative weighted total of every contributing monomial is at most \(n\). Rotation forces those totals to agree for a nonzero base coefficient. Schur orthogonality is unrestricted in equal weighted degree at most \(n\), giving the usual Gaussian inner products of the power sums. Thus \(rK_N\le n\) suffices for the full finite surrogate, and \(rb\le1\) implies this condition, including equality. All coefficient limits follow from the fixed-degree Riemann sums with \(H_N\) bounded. [Diaconis–Evans, Theorem 2.1](../../sources/prime84_cue/diaconis_evans.pdf) · [Bump–Diaconis](../../sources/prime84_cue/bump_diaconis.pdf)

## Parity and the barrier

Swapping \(p,q\) swaps the basis factors in \(B_{ij}\). Reflecting \(y\) shows \(B_{ji}=(-1)^{i+j}B_{ij}\). Since \(p,q\) have the same formal law on the cosine ray, the entries with odd \(i+j\) vanish after averaging. Let \(L=1-dz\). Direct polynomial integration yields
\[
\begin{aligned}
 B_{00}&=\ell,\\
 B_{11}&=\ell^3-3\ell D^2,\\
 B_{02}&=\frac{\sqrt5}{2}(\ell^3-\ell+3\ell D^2),\\
 B_{22}&=\frac94\ell^5-\frac52(3D^2+1)\ell^3+\frac54(3D^2-1)^2\ell .
\end{aligned}
\]
The formal cumulants give \(\mathcal E\ell^3=L^3+3Lzm_2-zm_3\) and \(\mathcal E(\ell D^2)=Lzm_2-zm_3\). Hence
\[
 D_{00}=L,\qquad D_{11}=L^3+2zm_3,\qquad
 D_{02}=D_{20}=\frac{\sqrt5}{2}(L^3-L+6Lzm_2-4zm_3).
\]
The remaining entry is explicitly \(D_{22}=\mathcal E B_{22}\), using only the first five cumulants of \(p,q\). At \(z=1/d\),
\[
 P_3(1/d)=D_{11}(D_{00}D_{22}-D_{02}^2)=-40(m_3/d)^3<0 .
\]
In particular, the entire extrapolation \(\exp(2Hz+Hz^2/4)P_3(z)\) cannot have the moments of any real law at all orders. If it had such a representing law, the even moment Taylor series of the entire extrapolation would give finite expectation of \(\cosh(tX)\) for every real \(t\), by monotone convergence. This would justify the full exponential expectation by absolute convergence and force it to be strictly positive on the real axis. The negative value contradicts this. The barrier tests the all-order extrapolation. The finite supported window and its positive moment matrices remain valid.

## All-rank barrier for integer derivative tilts

For fixed removed rank \(J\ge1\), the same density argument starts from \(|Z'|^{2(J-1)}\) and uses \(n=N+J-1\) ambient modes. The free span is \((w-1)^J\) times polynomials of degree at most \(N-2\). There are \(J\) missing evaluation jets and their normalized mode polynomials converge to \(u_j(s)=\sqrt{2j+1}P_j(2s-1)\), \(0\le j<J\). The same finite path argument and Riemann sums give the coefficient formula through \(rb\le1\) with exponential factor \(e^{(J-1)Hz+Hz^2/4}\) and polynomial \(P_J^{\rm det}(z)=\det(D_{ij}(z))_{i,j<J}\). At each fixed \(J\) the full-law estimates below apply to all \(J\) removed functions. Each polynomial entry has degree at most \(i+j+1\) in \(z\), because its oriented integral has polynomial degree at most \(i+j+1\) in the two frequency totals and formal moments up to that order have degree at most their order. Thus \(\deg P_J^{\rm det}\le J^2\) by the permutation formula. At zero, the formal totals are both zero and the oriented integral is the original orthonormality integral, so \(D(0)=I\).

The reflection and exchange identities hold at every rank, so \(D(z)\) is real symmetric for real \(z\). For \(J\ge3\), the principal block on indices \(0,2\) at \(z=1/d\) has determinant \(-20(m_3/d)^2<0\) regardless of its \(22\) entry. By the Rayleigh variational formula the full matrix then has a negative eigenvalue. Its smallest eigenvalue is continuous and equals one at zero, so some \(z_*\in(0,1/d)\) has \(\det D(z_*)=0\). For \(J=1\), the \(00\) entry directly vanishes at \(1/d\); for \(J=2\), the opposite-parity off-diagonal entries vanish and the same diagonal zero forces the determinant to vanish. For every \(J\), the entire moment extrapolation consequently vanishes at a positive real argument and the preceding \(\cosh\) argument excludes an all-order representing law. At rank three one has the stronger sign evaluation above. For general rank the principal-minor argument gives a zero without requiring a sign for the full determinant at \(1/d\).

## First crossing and its sign

For \((r-1)b\le1<rb\), a mixed-sign degree \(r\) monomial has each signed total \(\le n\) at finite \(N\). The only possible discrepancy is thus a pure sign with total frequency \(P>n\), or its reflection. These terms vanish in the true inverse because it is triangular on each one-sign ray and no two valid endpoint indices are separated by \(P\). Their polynomial extrapolation is the oriented sum. The degree-\(r\) determinant discrepancy is its trace discrepancy because every lower homogeneous part matches and the constant matrix is \(I\). The base determinant has its stable coefficients through degree \(r\). For \(r\ge2\), each potentially nonzero coefficient is balanced and obeys the signed-total bound from the mixed-sign argument. At \(r=1\), the nonconstant base coefficients vanish by rotation. Along the cosine ray the two signs combine, and the passage from the Taylor coefficient to the raw moment cancels the factorial of the ordered exponential expansion. The resulting limit of actual minus extrapolated moment is
\[
 -2^{1-r}\int_{\substack{x_i\in[a,b]\\x_1+\cdots+x_r>1}}
 A_3(x_1+\cdots+x_r)\prod_{j=1}^r\frac{dx_j}{x_j},
 \qquad
 A_3(t)=\sum_{j=0}^2\int_0^{1-t}u_j(s+t)u_j(s)\,ds .
\]
In this formula the \(u_j\) are their polynomial extensions and the integral is oriented. Ordinary zero-extended autocorrelations vanish for \(t>1\). Polynomial integration gives \(A_3(t)=-6t^5+12t^3-9t+3\), so
\[
 A_3(1+h)=-3h-24h^2-48h^3-30h^4-6h^5<0
 \qquad(h>0).
\]
The crossing region contains a positive-volume corner near \(b\). Therefore the rank-three first discrepancy is strictly positive. At finite \(n=6\), \(N=4\), with only \(k=2\) and \(r=4\), an independent exact free-span determinant gives first raw moment discrepancy \(9/160\), with agreement at all smaller degrees. This fixture has the inclusive lower boundary \((r-1)k=n\). [Exact symbolic calculation and finite determinant](../../scripts/geometry93_rank_three_barrier.py)

The same oriented sign calculation has a classical all-rank form. For \(J\ge1,\ t>1\) write the reversed interval as \(1-t\le s\le0\), \(x=2(s+t)-1\ge1\), \(y=2s-1\le-1\). The Christoffel–Darboux formula writes
\[
 \sum_{j<J}(2j+1)P_j(x)P_j(y)
 =J\frac{P_J(x)P_{J-1}(y)-P_{J-1}(x)P_J(y)}{x-y}.
\]
By Legendre parity and positivity on \([1,\infty)\), the quotient has sign \((-1)^{J-1}\), including endpoints. Orientation contributes a minus sign, giving \({\rm sgn}\,A_J(t)=(-1)^J\). Reusing the fixed-rank path argument gives first cosine correction of sign \((-1)^{J+1}\) for the global tilt \(|Z'|^{2(J-1)}\) with one marked root. This extension concerns the first crossing. The first-crossing sign and the determinant barrier use different properties of the oriented compression.

## Passage to the limiting law

In the coordinate \(u=N\theta/(2\pi)\), the free kernels converge on compact rectangles to the projection with band \([0,1]\) minus the three Fourier transforms of the \(u_j\). This follows by Riemann sums and finite-rank convergence. The diagonals are bounded by \(n/N\). Summation by parts gives \(|f_N(2\pi u/N)|\ll(1+|u|)^{-1}\) on the representative interval, using \(a>0\). The three removed normalized functions have the same bound by summation by parts on their discrete bounded-variation polynomial amplitudes. The full ambient kernel has constant diagonal and integrates \(f_N\) to zero on the circle, so the free mean is minus the integral against the removed diagonal. This mean converges by compact convergence and the integrable decay of the resulting product. The deterministic root mean is \(-H_N\). For centered statistics the variance of the tails beyond any \(R\) is \(O((1+R)^{-1})\) from the projection DPP variance upper bound \(\int f_N^2 K_N(u,u)\,du\). Thus compact-process convergence and truncation prove weak convergence of the full real statistic. For each real \(t\), the finite centered Laplace transform is bounded by \(\exp(\int(e^{tf_N}-1-tf_N)K_N(u,u)\,du)\), via the compressed positive exponential determinant and \(\log x\le x-1\). The exponent is uniformly bounded by the same squared-decay integral. This supplies uniform integrability of every fixed moment and transfers the window and crossing formulas to the actual limiting law. The estimates follow the fixed-rank proof for the derivative-square case. [Rank-two limiting-law proof](prime77_rooted_cue_band_limit.md)

These statements concern the intrinsic Haar model. The primary root-density and power-sum antecedents are identified above. The oriented argument is a fixed-rank extension of the existing finite-window calculation, with no assertion of publication priority or arithmetic extension.
