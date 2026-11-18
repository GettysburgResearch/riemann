# Independent QA of the rooted CUE moment window

18 November 2026. I checked both derivations of the formal joint coefficient window, the first beyond-window correction, and the numerical replay. The two finite endpoint conventions reconcile exactly: the Fourier **dimension** is \(n=N+1\), and the upper **index** is \(N=n-1\). The prime84 calculation gives the exact finite cutoff in terms of \(n\); the weighted84 transfer passes immediately to its scaled continuum version. The first-crossing integral is strictly negative for the cosine moment. For a mixed cosine–sine direction its coefficient can have either sign or vanish. No arithmetic extension is implicated. [Weighted review](weighted84_cue_moment_window_review.md) · [Prime review](prime84_cue_moment_window.md)

## Complement, base determinant and Neumann paths

After the global Haar/root-label derivative-square tilt, the \(N-1\) free points are the projection with the two vanishing conditions on the dimension-\(n\) Fourier space \(E=\{0,\ldots,n-1\}\). In an orthonormal decomposition \(E=P\oplus Q\), take \(A=E e^F E\). The free generating function is \(\det A_{PP}\). The Schur complement gives \(\det A_{PP}=\det A\det (A^{-1})_{QQ}\), with all inverses legitimate formally because \(A(0)=I\). The root at angle 0 contributes exactly \(e^{-H_N z_c}\). It is absent only from the free determinant and contributes zero to the sine statistic.

For the base determinant on \(U(n)\), a signed word is zero unless its positive and absolute negative frequency totals agree, by scalar rotation. In equal weighted degree \(m\le n\), the Schur expansion and Haar orthogonality are unrestricted because every partition of \(m\) has at most \(n\) parts. The symmetric-group power-sum inner product is exactly the centered complex Gaussian Wick rule. Thus whenever \(rK_N/2\le n\), the base determinant has the coefficients of \(e^{H_N(z_c^2+z_s^2)/4}\) through degree \(r\), where \(K_N=\lfloor bN\rfloor\) for a nonempty band. Conjugation is used in this inner product, but subsequent manipulations are formal, with independent commuting \(z_c,z_s\). In particular \(u=z_c-i z_s\) and \(v=z_c+i z_s\) are two formal combinations with \(uv=z_c^2+z_s^2\). No Hermitian conjugation of \(z_c,z_s\) is introduced.

For a tagged monomial of signed totals \(P,Q\), each Neumann path has finitely many steps, with each step a sum of signed Fourier sources in one exponential block. A path starts and ends in \(E\). To visit both forbidden regions it must traverse from \(\le-1\) to \(\ge n\), or the reverse, between two vertices. This needs \(n+1\) positive or \(n+1\) negative total, regardless of grouping. Thus if \(P,Q\le n\) its finite inverse coefficient equals the sum of the two half-line inverse coefficients minus the full-line coefficient. With \(T(g)_{ij}=g_{i-j}\), the left half-line factorizes as upper \(T(e^{F_-})\) times lower \(T(e^{F_+})\), because an intermediate index in that order is at least the two endpoints. The inverse reverses the order. On the right half-line the orders interchange. This is exact coefficientwise, with no infinite-order norm convergence of an \(N\)-dependent symbol required.

## Exact oriented compression, including the gap

With net displacement \(D=P-Q\), the valid starts \(j\) are the integers in the half-open interval
\[
 I=[\max(0,Q-P),\min(n,n+Q-P)).
\]
The contribution from the left inverse has \(j\ge Q\); that from the right inverse has \(j<n-P\). For \(P,Q\le n\), both cutoff positions \(Q,n-P\) lie in the *closed hull* of \(I\), even when one equals its excluded endpoint. On \(I\), the signed indicators combine as follows:
\[
 1_{j\ge Q}+1_{j<n-P}-1=
 \begin{cases}
   1_{Q\le j<n-P}, & Q\le n-P,\\
   -1_{n-P\le j<Q}, & Q>n-P .
 \end{cases}
\]
Thus the exact signed sum of \(U(j+D)U(j)^{\mathsf T}\) is the oriented half-open sum from \(Q\) to \(n-P\). It is valid when the total absolute frequency exceeds \(n\) but each sign total stays within \(n\). The sign of the gap is negative. At \(P+Q=n\) the signed sum is empty; at \(P+Q=N=n-1\) it contains one grid site. These cases explain the apparent one-site discrepancy between continuum integration at length \(N\) and the exact dimension-\(n\) formula.

Set \(\ell=n-P-Q\). For this oriented sum the signed number of indices is \(\ell\), and the midpoint of \(j-(n-1)/2\) is \(-D/2\). Its squared deviation about that midpoint has oriented sum \(\ell(\ell^2-1)/12\), including when \(\ell<0\). Consequently
\[
 D_{00,n}=\ell/n,\quad
 D_{01,n}=-\sqrt3\,\ell D/(n\sqrt{n^2-1}),\quad
 D_{10,n}=-D_{01,n},\quad
 D_{11,n}=\ell(\ell^2-1-3D^2)/(n(n^2-1)).
\]
This independently yields prime84 (4) and, upon scaling by \(n\) or \(N\), the same continuum matrix in weighted84. If a pure total equals \(n\), the true and extrapolated coefficients both vanish. If it exceeds \(n\), the true coefficient still vanishes because no endpoints fit, whereas extrapolation can be nonzero. The no-both-exits condition is sufficient and sharp as a support guarantee, although individual paths or monomials can agree outside it. For example with \(n=5\), tagged shifts \((-1,+6,-1)\) can follow the path \(0,-1,5,4\). The two label orderings give a degree-three finite-minus-inclusion-exclusion entry of \(-2\) at \((4,0)\); the one- and two-block terms cannot visit both forbidden regions.

## Formal summation, joint signs and correction

The signed \(e^{-F_+},e^{-F_-}\) coefficient masses are \(e^{uH_N/2},e^{vH_N/2}\). Dividing by those masses is a formal construction. The normalized total frequency variables \(p=P/n,q=Q/n\) have independent formal cumulants \((u/2)d_N,(u/2)J_{2,N},(u/2)J_{3,N}\) and the same with \(v\); no probability with complex parameters is inferred. Let \(l=1-d_N z_c\) and \(R=p+q,\ D=p-q\), now in scaled units. Then
\[
 E((1-R)D)=-i z_s(d_N l-J_{2,N}),\qquad
 E((1-R)^3-3(1-R)D^2)
 =l^3+2z_cJ_{3,N}+3l z_s^2d_N^2-6z_s^2d_NJ_{2,N}.
\]
The second equality uses the bilinear joint cumulants, so \(ED=-i z_s d_N\), \(\operatorname{Cov}(R,D)=-i z_s J_{2,N}\) and \(\operatorname{Var}D=\operatorname{Var}R=z_c J_{2,N}\) in the formal sense. The two off-diagonals are negatives of one another. The square of the imaginary entry therefore subtracts the square of its real coefficient from the determinant. The \(l^2d_N^2\) and \(ld_NJ_{2,N}\) terms cancel, leaving \(-3J_{2,N}^2 z_s^2\). The finite diagonal correction from \(\ell^2-1\) is the printed \(-l^2/n^2\) in the determinant numerator, divided by \(1-1/n^2\). Combining the mass squared, the root and the base Wick term gives prime84 (5). Uniform boundedness of the mass \(H_N\) makes the fixed-degree Riemann summations immediate. In particular \(r b=1\) is included since \(r\lfloor bN\rfloor\le N<n\).

At the first crossing \((r-1)b\le1<rb\), finite mixed-sign monomials still have \(P,Q\le N\), and the base Wick determinant remains valid since \(rb\le1+b<2\). The only missing inverse-compression terms in homogeneous degree \(r\) are the pure signs with total \(m>n\). A determinant perturbation beginning at degree \(r\) changes that degree by its trace, because the constant matrix is \(I\); the other factors have constant term 1. The extrapolated finite compression trace is
\[
 A_n(m)=\frac{2(m-n)(m^2+nm-n^2+1)}{n(n^2-1)} .
\]
The joint discrepancy is therefore
\[
 -\frac{(z_c-i z_s)^r+(z_c+i z_s)^r}{2^r r!}
    \sum_{k_1+\cdots+k_r>n}\frac{A_n(k_1+\cdots+k_r)}{k_1\cdots k_r}
\]
with all \(k_i\) in the band. Repeated frequencies are correctly counted by the ordered expansion. The sum converges by bounded Riemann summation to the proposed integral with \(A(t)=2-4t+2t^3\), and the threshold hyperplane has measure zero. For the cosine raw moment, the factorial cancels and the two signs give the multiplier \(-2^{1-r}\). Since \(A(t)=2(t-1)(t^2+t-1)>0\) on \(t>1\) and the open corner \(x_i\) close to \(b\) has positive volume, the correction is strictly negative. For a real ray \((z_c,z_s)=(c t,s t)\) the multiplier is \(-2^{1-r}\Re(c+i s)^r\), which need not be negative. Sine-only odd moments vanish by symmetry. The all-order tagged path rule in weighted84 is consistent beyond this range; a factorial is absent for squarefree tags within an exponential block because the commuting permutations cancel the exponential factorial.

To regard the continuum derivatives as moments of the weak-limit law, not just limits of finite moment sequences, I checked the finite exponential-moment argument in prime77. For real \(t\) the compressed exponential is positive definite and \(\log(1+x)\le x\) cancels the linear mean. The remainder is bounded by \(C_t\int f_N^2 P_N(u,u)du=O_t(1)\) using the uniform localized tail estimate. Both signs give uniform integrability of each fixed moment along any real ray. [Full law and moment passage](prime77_rooted_cue_band_limit.md)

## Exact independent checks and source scope

- Direct exact matrices at \(n=5,\ P=4,\ Q=3\) give the degree-two mixed inverse coefficient with exactly two nonzero shifted entries, \((2,1)\) and \((3,2)\), each \(-1\). This is the negative oriented gap. At \(n=5,\ N=4\), retain only \(k=2\) in the cosine band and take order \(r=3\). Full rational projection traces give mean \(-1/4\), variance \(63/400\), third cumulant \(-13/1600\), and raw third moment \(-227/1600\). The finite formal surrogate gives \(-3/25\). Their difference is \(-7/320\), exactly \(-2^{-2}2^{-3}A_5(6)\) with \(A_5(6)=7/10\).
- Replaying the supplied script with OpenBLAS one thread reproduced the recorded byte stream. Script SHA-256 f4b87f035aa75b2c78a85a7033d1ed24fc1936ccfb04c42fa5fc76659b3d5706; output SHA-256 91ecd374298e68e26632ee1b2cbe173bf54412fc7f1aeb9e44fed9d4694f6a17. The symbolic antiderivatives and finite eight cases complement, rather than substitute for, the analytic proof. [Script](../../scripts/prime84_cue_moment_window_check.py) · [Output](../../experiments/results/prime84_cue_moment_window_check.txt)
- Read Diaconis–Evans Theorem 2.1(a) and its Schur proof, preprint p. 3, for the maximum of the two weighted degrees condition and independent Gaussians. Read Bump–Diaconis §1, pp. 254–258, especially the Hall/class function comparison around (1.8) and the Haar inner product, and pp. 259–261 for Theorems 1–2 and the bridge to general minors. This supports the exact classical basis calculation, with no assumption that the fixed minor asymptotics yield the current moving-symbol result. [Diaconis–Evans](../../sources/prime84_cue/diaconis_evans.pdf) · [Bump–Diaconis](../../sources/prime84_cue/bump_diaconis.pdf)
- Read Borodin–Okounkov arXiv:math/9907165v1, §2 Theorem 1 (2.3)–(2.4) and its algebraic/analytic setup, giving the finite Toeplitz determinant as Szegő factor times a tail-index Fredholm determinant. Read Basor–Widom arXiv:math/9909010v3, the initial setup and Second Proof, for the upper/lower triangular product, finite compression and Jacobi-related identity. They are primary antecedents. The present two-sided path exclusion and the power-sum Wick argument were derived directly. No priority assertion follows. PDF pins observed a1a6eccd6735311dbbe8b30eb43530f65c6434160788e28d697cad10ff43fd4f and 912cbdccc08d8ad297e09789e1b1d5ee277e92c4423ae33277425a0193cfffd2 respectively. [Borodin–Okounkov](https://arxiv.org/pdf/math/9907165v1) · [Basor–Widom](https://arxiv.org/pdf/math/9909010v3)

The exact finite degree limit \(rK_N\le n\), the inclusive continuum range \(rb\le1\), and the first-crossing correction are supported. This note does not assign a new archival theorem or assert any further arithmetic moment range.
