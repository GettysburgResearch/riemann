# Independent check of Petrov’s tilted factors for rooted CUE

For real Laplace parameters, both the exact Gram determinant and Petrov’s tilted Fredholm determinant are strictly positive. The formal rooted CUE determinant polynomial has a positive real zero, and its quadratic coefficient already differs from that of the mass-removed Gram determinant. The exact quotient contains a tilted Fredholm factor that has a nonzero quadratic term. The optional fixed-tail chart has a separate invertibility hypothesis and can fail on the positive real axis. These conclusions concern the matching of two formulas with different scopes. [Companion derivation](geometry97_petrov_gram_match.md)

I read Leonid Petrov, arXiv:2605.24976v1, §2 Theorem 2.4 and (2.6), §3.1 (3.3)–(3.7), §§3.2–3.4 and §4 (4.2)–(4.11), including Theorem 4.4 and Propositions 4.6–4.7. The cached v1 PDF has SHA-256 `f8b1c3386d49e61e767ae969a02131b509a42af276151ff04492b8be75a79214`. The circle exponential used below satisfies the source’s symbol assumptions. Its finite chart parameter equals the number of *free* eigenangles here. [Primary PDF](https://arxiv.org/pdf/2605.24976v1)

## Hypotheses and real positivity

Let \(N\ge2\) be CUE size, \(J\ge1\) fixed removed rank, \(m=N-1\) and \(n=m+J\). Under the global Haar/root-label tilt by \(|Z'|^{2(J-1)}\), the \(m\) free angles have weight \(\prod_i|1-w_i|^{2J}\) times their squared Vandermonde. Consequently the column map \(X=T((1-w)^J)|_{P_m}\) identifies the free span within the first \(n\) Hardy modes. Its rows are paired with \(X^*=P_mT((1-w^{-1})^J)\). The two tilts have the Fourier support and regularity assumed in §4.1. [HKO, §2(a)](../../sources/classical63_lfunctions/hko2000.pdf)

Use a nonempty band with
\[
 F_+(w)=-\sum_{k\in\mathcal B_N}\frac{w^k}{2k},\quad F_-(w)=F_+(w^{-1}),
 \quad \phi=e^{z(F_++F_-)},\quad H_N=\sum_{k\in\mathcal B_N}\frac1k .
\]
The analytic logarithm \(z(F_++F_-)\) is smooth on the circle and has constant coefficient zero. For every fixed \(N,z\), the canonical factors \(\phi_\pm=e^{zF_\pm}\) and their inverses are bounded on the relevant disks up to the circle. Thus Petrov’s \(G=1\), \(Z=e^{H_Nz^2/4}\), and (4.3) becomes
\[
 R=X^*T(\phi_+),\quad C=T(\phi_-)X,\quad \Gamma=RC .
\]
For real \(z\), \(T(\phi_-)=T(\phi_+)^*\), so \(R=C^*\). The multiplication map \(X\) is injective because its polynomial multiplier is nonzero, and \(T(\phi_-)\) is invertible by the upper-triangular product rule. Hence \(\Gamma=C^*C\) is strictly positive definite, \(R\) is onto, and \(\Pi_V=I-C\Gamma^{-1}R\) is the orthogonal projection onto \(V=\ker R\) on the real axis. For complex \(z\) near zero, transversality follows instead by the nonzero determinant of \(\Gamma(0)=X^*X\).

Set \(b_0=\phi_-/\phi_+\), \(c_0=b_0^{-1}\) and \(K=H(b_0)H(\widetilde c_0)\), with \(\widetilde c_0(w)=c_0(w^{-1})\) as in Petrov (3.4). The Toeplitz product formula gives \(I-K=T(b_0)T(c_0)\). On the real axis \(c_0=\overline{b_0}\). The upper factor followed by the lower factor gives exactly \(T(b_0)=T(\phi_-)T(\phi_+^{-1})\), which is boundedly invertible. In particular \(I-K=T(b_0)T(b_0)^*\) is bounded below by a positive constant at any fixed real \(z,N\). Its compression to \(V\) shares that bound. Since \(K\) is trace class, the Fredholm determinant \(L_{\rm obl}=\det_V(I-\Pi_VK|_V)\) is strictly positive. Near complex zero the representation \(L_{\rm obl}=\det_H(I-K\Pi_V)\) from (2.6) places it on one fixed space and is analytic. No claim about chart transversality at arbitrary imaginary Laplace parameters follows.

## Quotient and strict quadratic mismatch

Use \(U\) for orthonormal columns spanning the complement of \(X\) in the first \(n\) modes, and \(A_n=P_nT(\phi)|_{P_n}\). Petrov (4.6) identifies the tilted matrix with \(X^*T(\phi)X\). After dividing its determinant by \(\det(X^*X)=\det\Gamma(0)\), the result is the determinant on the orthonormally expressed free span. Its root mark contributes \(e^{-H_Nz}\). By Theorem 4.4 the full marked transform is \(e^{-H_Nz}Z(\det\Gamma/\det\Gamma(0))L_{\rm obl}\). Independently, the ordinary BOGC formula on \(n\) modes gives \(\det A_n=Z L_n\), where \(L_n=\det_{Q_nH}(I-Q_nK|_{Q_nH})\). Finite Jacobi on the orthonormal decomposition gives the exact identity
\[
 \det(U^*A_n^{-1}U)
 =\frac{\det\Gamma}{\det\Gamma(0)}\frac{L_{\rm obl}}{L_n}.
\]
The ratios make sense locally in complex \(z\) and at every real \(z\), since on the real axis \(A_n\) is positive definite and \(Z\ne0\). No root-mark factor remains in this quotient.

The ordinary ambient tail sees two high-index Hankel coefficients. In an entry at \(i,j\ge n\), each term is \(\widehat b_0(i+\ell+1)\widehat c_0(-j-\ell-1)\) with \(\ell\ge0\). A tagged source word in the product requires positive total at least \(i+\ell+1\) and absolute negative total at least \(j+\ell+1\). This excludes nonconstant determinant terms whenever both signed totals are at most \(n\), as used in the exact compression window. In contrast, the tilted tail begins with
\[
 L_{\rm obl}(z)=1-z^2\operatorname{Tr}\big(\Pi_V(0)H(F_+)H(F_+)^*\big)+O(z^3).
\]
Indeed the first Hankel coefficients of \(b_0\) and \(\widetilde c_0\) are \(-F_+\) and \(-\widetilde F_-\), restricted to positive modes, so their product starts at order two. The constant projection in that coefficient is already the projection onto the deleted directions on the first \(n\) modes. If the largest band index is \(\le n\), the Hankel matrix is supported there and the trace is \(\kappa_{J,N}=\sum_{j<J}\|H(F_+)^*U_j\|^2>0\). One can choose \(U_0\) to be the constant vector. Pairing it with any nonzero Hankel column cannot cancel because every nonzero entry has the same sign.

Thus through degree two, whenever \(2\max\mathcal B_N\le n\), the normalized Gram \(\det\Gamma/\det\Gamma(0)\) exceeds the complementary determinant in its quadratic coefficient by \(\kappa_{J,N}\). In comparing with the formal polynomial, remove the **same** mass \(e^{JH_Nz}\) from both determinants. This leaves the quadratic coefficient difference unchanged since their constant and linear terms already agree. For fixed \(0<a<b\le1/2\) the difference persists after passage to the limit. The discrete orthonormal removed-mode polynomials converge to shifted Legendre polynomials \(u_j\) under the usual grid normalization; Riemann summation sends the trace to
\[
 \frac14\sum_{j<J}\int_0^b
 \left[\int_0^1\frac{\mathbf1_{a<s+t\le b}}{s+t}u_j(s)ds\right]^2dt>0 .
\]
The discontinuity lines have measure zero, the kernel is bounded since \(a>0\), and the constant mode supplies a strictly positive integral. Therefore the factor mismatch survives inside the limiting window, independently of the formal positive-real zero.

For the latter zero, the matrix in the formal determinant is symmetric on real \(z\) because its two auxiliary frequency totals are exchangeable and swapping them transposes the compression. It is the identity at zero. At \(z=1/d\), its normalized constant-mode diagonal is zero. For ranks one and two this gives a zero determinant by parity. For rank at least three its \((0,2)\) entry is \(-2\sqrt5m_3/d\ne0\), so the principal block has a negative eigenvalue and continuity gives a positive determinant zero. This is a coefficient extrapolation beyond the established finite moment identity. The exact positive factors have no such zero. [Formal determinant and all-rank proof](analytic93_rank_three_skeptic.md)

## Independent finite check of the optional chart

In Petrov Proposition 4.6, \(B=RP_m|_{P_mH}\) must be invertible in addition to \(\Gamma\). Proposition 4.7 then bounds the correction rank by \(2J\). At \(z=0\), \(B\) is triangular with diagonal one, so the fixed-tail chart is valid locally. It need not remain valid for all real \(z\).

Take \(N=4, J=2\), with only \(k=2\) in the band, so \(m=3,n=5\). I used the three translates of \((1,-2,1)^T\) as the columns of \(X\), built the finite Toeplitz matrices by expanding the exponential, and computed the rational determinants directly. The two expansions were
\[
 \frac{\det\Gamma(z)}{\det\Gamma(0)}
 =1+z/4+33z^2/800+O(z^3),\qquad
 \det(U^*A_n^{-1}U)=1+z/4-3z^2/200+O(z^3).
\]
The difference \(9/160\) also follows from the Hankel formula: \(H(F_+)\) has entries \(-1/4\) at \((0,1),(1,0)\) only, and the removed constant and centered linear projection has diagonal entries \(3/5,3/10\) at indices 0 and 1. For the independent chart check, \(B\) itself has rows
\[
 (1-z/4,-2,1),\quad (z/2,1-z/4,-2),\quad (z^2/32-z/4,z/2,1-z/4).
\]
Its determinant is \(-(z^3+4z^2-64z-128)/128\), equal to 1 at zero and \(-1\) at 8. The chart has a positive-real singularity even though \(\Gamma\) and \(L_{\rm obl}\) remain positive there. This is a failure of the additional chart hypothesis at that parameter and leaves Theorem 4.4 intact. No assertion about publication priority or arithmetic transfer is needed for this comparison.
