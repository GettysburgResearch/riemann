# Intrinsic rooted CUE moment window and its first correction

For the derivative-square tilted rooted CUE of size \(N\), the cosine band statistic has limiting moments given by the formal quartic generating expression through every fixed order \(r\) with \(rb\le1\), for \(0<a<b<1\). This includes the boundary \(rb=1\). The first fixed order with \((r-1)b\le1<rb\) has a strictly negative correction to that formal moment. The proof uses the finite Toeplitz inverse coefficient by coefficient, and uses no arithmetic kernel. The HLZ arithmetic comparison remains restricted to \(rb<1/2\). [Rooted law from HKO](weighted73_rooted_cue_band_match.md) · [Arithmetic formal coefficients and their scope](weighted79_formal_band_obstruction_review.md)

## Finite determinant and dimensions

Let \(E_N\) project onto the circle Fourier indices \(0,\ldots,N\), of dimension \(n=N+1\), and let \(Q_N\) project onto the span of the constant and centered-linear coefficient vectors on those indices. The non-root process has projection \(P_N=E_N-Q_N\) of rank \(N-1\) by the HKO derivative-square tilt. The included root at angle zero is deterministic. Define
\[
 C_N=-\sum_{aN<k\le bN}k^{-1}\sum_j\cos(k\theta_j),\qquad
 S_N=-\sum_{aN<k\le bN}k^{-1}\sum_j\sin(k\theta_j),
 \quad H_N=\sum_{aN<k\le bN}\frac1k.
\]
Here \(j\) runs through all \(N\) points including the root, after shifting to root-centered angles. For formal parameters \(z_c,z_s\) write
\[
 F_N(\theta)=-\sum_{aN<k\le bN}k^{-1}
                  (z_c\cos(k\theta)+z_s\sin(k\theta)),\quad
 A_N=E_N e^{F_N}E_N\big|_{E_N}.
\]
The rooted generating determinant is exactly
\[
 e^{-z_c H_N}\det(A_N)
             \det\nolimits_{Q_N}\bigl(Q_N A_N^{-1}Q_N\bigr).
\]
Indeed the projection-DPP expectation is the compression determinant on \(P_N\), and Jacobi's complementary minor identity on the orthonormal decomposition \(E_N=P_N\oplus Q_N\) gives the two displayed factors. The inverse exists as a formal series with constant matrix \(I\). The root contributes only \(e^{-z_c H_N}\). This does not confuse the rank \(N-1\) rooted process with the ordinary \(U(N+1)\) determinant \(\det(A_N)\).

The latter ordinary-unitary factor has exactly the coefficients of
\[
 \exp\bigl(H_N(z_c^2+z_s^2)/4\bigr)
\]
through any total degree \(r\) with \(rbN/2\le N+1\). To see this, expand in power sums of signed frequencies. Unequal positive and negative total degree vanishes by scalar rotation. For equal total degree \(d\le n\), Schur orthogonality under Haar and the symmetric group character change of basis give \(\langle p_\lambda,p_\mu\rangle=\delta_{\lambda,\mu}z_\lambda\), because all partitions of \(d\) have length at most \(n\). This is the exact Wick rule for independent centered circular complex Gaussians of variance \(k\) at frequency \(k\). The bound uses \(rbN/2\), since a balanced signed term has half its total absolute frequency on each side. This ordinary-unitary factor stays in its Wick range strictly beyond the first rooted correction considered below.

## Coefficientwise two-boundary inverse

Let \(F_+\) and \(F_-\) denote the strictly positive and strictly negative Laurent parts of \(F_N\), and write \(B_L,B_R\) for the inverses of \(e^{F_N}\) compressed to the half-lines \(j\ge0,j\le N\). On \(j\ge0\) the factorization is \(T_L(e^{F_-})T_L(e^{F_+})=T_L(e^{F_N})\). The intermediate index of this upper-triangular times lower-triangular product is above both endpoints, so no path drops below the left boundary. The inverse is \(B_L=T_L(e^{-F_+})T_L(e^{-F_-})\). On the right half-line the orders reverse, and \(B_R=T_R(e^{-F_-})T_R(e^{-F_+})\). On the full Laurent line \(B_0=e^{-F_N}\).

To compare these with the finite inverse, expand each inverse as \(\sum_{\ell\ge0}(-1)^\ell(A-I)^\ell\) on its index set. For a specified monomial in signed Fourier modes, each path has step lengths equal to sums of groups of those signed frequencies. Let \(P\) and \(Q\) be the sums of the positive frequencies and of the absolute negative frequencies of that monomial. A path that visits both an index below 0 and one above \(N\) must traverse from at most \(-1\) to at least \(N+1\), or back. It therefore uses at least \(N+2\) in one signed direction. In particular, when \(P,Q\le N\), no such path exists, and
\[
 A_N^{-1}= E_N(B_L+B_R-B_0)E_N
\]
for that coefficient. This is inclusion–exclusion for the two forbidden regions with the same path weights. More generally \(P,Q<N+2\) suffice for this inverse identity alone. The stronger \(P,Q\le N\) also gives the exact orientation argument in the next paragraph. All expansions at a fixed degree are finite coefficient operations; no infinite-order asymptotic of a moving symbol is assumed.

Set \(p=P/N\), \(q=Q/N\). Factor \(e^{-F_+}\) into coefficients of positive total shift \(P\), and \(e^{-F_-}\) into coefficients of negative total shift \(-Q\). The endpoint index \(j\) and \(j+P-Q\) both lie in \(E_N\). The left half-line inverse imposes also \(j\ge Q\), while the right half-line inverse imposes \(j\le N-P\). For \(P,Q\le N\), both cut points \(Q,N-P\) lie within the endpoint interval. The continuum transfer matrix is therefore the oriented integral
\[
 M(p,q)=\int_q^{1-p}u(t+p-q)u(t)^{\mathsf T}\,dt,
       \qquad u(t)=\binom{1}{\sqrt{12}(t-1/2)} .
\]
For \(p+q\le1\) it is the intersection of the two constraints. For \(p+q>1\), still with \(p,q\le1\), it is the negative integral over the intervening gap, since neither half-line term counts that gap while the full-line subtraction does. If \(P+Q>N\), integer endpoints contribute a discrepancy of size at most a bounded number of grid sites against the oriented integral. This is \(O(1/N)\) in the \(Q_N\) matrix. In all these cases the matrix formula approximates the discrete one uniformly with \(O(1/N)\) error, using the explicit constant and centered-linear basis normalization and polynomial Riemann sums. The pure signed sums condition holds for every monomial of any degree \(r\) with \(rb\le1\), including equality because \(r\lfloor bN\rfloor\le N\). Throughout, \(Q_N\) retains its original rank and \(N\), not \(N+1\), sets the upper Fourier endpoint in the transfer integral.

## Gaussian factor and the finite-rank quartic

Write \(\lambda_\pm=(z_c\mp i z_s)/2\). The coefficient sums from \(e^{-F_\pm}\) have total masses \(e^{\lambda_\pm H_N}\). After formally dividing by these masses, they are compound-Poisson series for \(p,q\) with respective intensity measures
\[
 \lambda_+\sum_{aN<k\le bN} k^{-1}\delta_{k/N},
 \qquad
 \lambda_-\sum_{aN<k\le bN} k^{-1}\delta_{k/N}.
\]
For complex intensities this is only an identity of formal power series, obtained by expanding exponentials. Let \(H=\log(b/a)\), \(d=b-a\), \(J_2=(b^2-a^2)/2\), \(J_3=(b^3-a^3)/3\), so their continuum cumulants of orders \(1,2,3\) are \(\lambda_\pm d,\lambda_\pm J_2,\lambda_\pm J_3\). Define \(R=p+q\), \(D=p-q\), \(\ell=1-R\). The exact polynomial form of the transfer integral is
\[
 M(p,q)=
 \begin{pmatrix}
 \ell&-\sqrt3\,\ell D\\
 \sqrt3\,\ell D&\ell^3-3\ell D^2
 \end{pmatrix}.
\]
This follows by centering the integration variable at the midpoint of \(q,1-p\). In the mean transfer matrix set \(l=1-dz_c\). Since \(ER=dz_c\), \(ED=-i z_s d\), \(\operatorname{Var}R=\operatorname{Var}D=z_c J_2\), \(\operatorname{Cov}(R,D)=-i z_s J_2\), and \(\kappa(R,R,R)=\kappa(R,D,D)=z_c J_3\), the entries are
\[
 \mathbb E\ell=l,\quad \mathbb E(\ell D)=-i z_s(d l-J_2),\quad
 \mathbb E(\ell^3-3\ell D^2)=l^3+2z_cJ_3+3l z_s^2d^2-6z_s^2dJ_2.
\]
The \(\lambda_++\lambda_-=z_c\) masses restore a factor \(e^{H z_c}\) to the matrix, and hence \(e^{2H z_c}\) to its determinant. The two off-diagonals cancel the terms depending on \(d^2z_s^2\) and \(dJ_2z_s^2\) in the determinant, leaving only \(-3J_2^2z_s^2\). The root removes \(e^{H z_c}\), so the limiting coefficients through each total degree \(rb\le1\) are those of
\[
 \exp\!\left(H z_c+\tfrac H4(z_c^2+z_s^2)\right)
 \left[(1-d z_c)^4+2J_3 z_c(1-d z_c)-3J_2^2z_s^2\right].
\]
For coefficient convergence, the uniform \(O(1/N)\) matrix transfer error is summed against bounded total weight at each fixed order, because \(H_N\to H\), and the finite sums of powers of \(k/N\) converge by Riemann summation. This proves the scalar quartic and also the intrinsic joint coefficient formula. For example the logarithm gives \(\operatorname{Var}S=H/2-6J_2^2\) and \(\kappa(C,S,S)=6J_2^2(-4d+2J_3)\), in agreement with the previous separate lower-order calculations. [Joint arithmetic and rooted cubic checks](weighted81_joint_third_review.md)

## First additional chamber and exact general coefficient rule

Suppose \((r-1)b\le1<rb\), \(b<1\). For all mixed-sign monomials of degree \(r\), each of \(P,Q\) is at most \((r-1)bN\le N\), even if \(P+Q>N\). The oriented gap formula remains valid for them. An all-same-sign monomial of total absolute normalized frequency \(t=x_1+\cdots+x_r>1\) has no valid starting and final indices in \(E_N\). Its actual inverse coefficient therefore gives zero. Its formal continuation would have trace
\[
 \operatorname{tr}M(t,0)=2-4t+2t^3=2(t-1)(t^2+t-1)>0.
\]
The only degree-\(r\) difference thus comes from that missing homogeneous coefficient of the \(Q_N\) matrix. All lower-degree coefficients agree with the formal expression, so the determinant difference at that order is exactly the trace difference, as the matrix constant term is \(I\). Multiplication by the two other factors has no further effect at the first differing order. The ordinary CUE factor is still Wick, since \(rb\le1+b<2\). In the scalar cosine case the two choices of common sign each contribute \(2^{-r}\) per ordered \(r\)-tuple; the exponential factorial cancels upon taking the \(r\)-th moment. The exact first correction to that moment therefore is
\[
 -2^{1-r}\!
 \int_{\substack{(x_1,\ldots,x_r)\in[a,b]^r\\ x_1+\cdots+x_r>1}}
   [\,2-4t+2t^3\,]\prod_{i=1}^r\frac{dx_i}{x_i}.
\]
The integrand vanishes at the cut surface and the region has positive volume since \(rb>1\), so the integral is strictly negative. Thus the fourth moment first differs for \(1/4<b\le1/3\), with coefficient \(-1/8\) times the displayed integral at \(r=4\); the fifth first differs for \(1/5<b\le1/4\), with coefficient \(-1/16\) at \(r=5\). At \(rb=1\) the region has zero measure and the formal moment is valid.

There is also an exact direct rule for later chambers of the inverse. Introduce separately tagged parameters \(t_i\) in \(F=\sum_i t_i S^{d_i}\) for any fixed list of signed integer shifts. In the squarefree monomial \(t_1\cdots t_r\), let \(\pi=(B_1,\ldots,B_j)\) run over ordered partitions into nonempty blocks. The inverse coefficient is the sum of the paths with successive steps \(\sum_{i\in B_j}d_i,\ldots,\sum_{i\in B_1}d_i\), with factor \((-1)^j\). There are no factorial weights here because each exponential block is squarefree in its own tags and the shifts commute before compression. If the path has normalized offsets \(s_0=0,s_1,\ldots,s_j\) and total shift \(s_j\), the matrix contribution is the Riemann integral
\[
 (-1)^j\int_{-\min s_i}^{\,1-\max s_i}u(t+s_j)u(t)^{\mathsf T}\,dt ,
\]
with zero when the lower limit exceeds the upper. This follows immediately from the finite Neumann series and gives the chamber polynomials of the inverse without the one-boundary approximation. Chamber boundaries arise from signed subset sums that decide the path extrema or interval disappearance. For \(rb<2\) the base determinant Wick factor is still available, so these inverse coefficients and the two-by-two determinant suffice to evaluate each further rooted moment in that range. The first correction above is the closed form at the first exceeded degree. No unrestricted moment formula is inferred here.

## Classical source landmarks

Bump–Diaconis, *Toeplitz Minors*, JCTA **97** (2002), 252–271, develops Toeplitz minors via Schur and power-sum orthogonality. I checked pp. 253–258 and their general minor discussion preceding Theorem 3. Their fixed-shape minor limits do not by themselves supply the present varying-band, derivative-rooted two-vector inverse calculation. Borodin–Okounkov, *A Fredholm determinant formula for Toeplitz determinants*, Integral Equations Operator Theory **37** (2000), 386–396, expresses the finite Toeplitz determinant using a Fredholm determinant supported in the tail of the index set. Basor–Widom, *On a Toeplitz determinant identity of Borodin and Okounkov*, same volume, 397–401, gives the operator factorization treatment with upper/lower triangular Toeplitz products, including the beginning of the arXiv text and its formulas (3)–(5). These are primary antecedents for the standard Toeplitz and Wiener–Hopf tools. The proof here used only the finite complementary minor identity, the elementary one-sided triangular factorization, and the coefficientwise interval path calculation, thereby avoiding uniform asymptotics for an \(N\)-dependent symbol. No novelty or priority claim is made. [Bump–Diaconis primary PDF](https://sites.math.washington.edu/~billey/classes/symmetric.functions/bump.diaconis.pdf) · [Borodin–Okounkov primary preprint](https://arxiv.org/abs/math/9907165) · [Basor–Widom primary preprint](https://arxiv.org/abs/math/9909010v3)

The all-order quartic extrapolation has a signed inverse that precludes a probability moment sequence. The exact first boundary correction identifies where it starts to fail on the rooted CUE side. Nothing in this comparison extends the arithmetic HLZ moment window.
