# Independent rank-three rooted CUE challenge

For the globally \(|Z'|^4\)-tilted root law, the proposed cosine surrogate is correct through every fixed order \(r\) with \(rb\le1\). Its rank-three determinant has value \(-40(m_3/d)^3\) at \(z=1/d\). The first moment after the window is strictly **larger** than its surrogate value. The positivity obstruction concerns the entire surrogate moment sequence. The finite within-window moments still come from positive laws.

## Sampling law and finite determinant

Take an \(N\)-point Haar CUE configuration jointly with a uniform root label, then globally reweight the pair by \(|Z'(\theta_{\rm root})|^4\) divided by its Haar-label expectation. Integration uses the real angles and a positive density. This weighting differs from choosing a derivative-weighted label separately within each unweighted matrix, which uses a matrix-dependent denominator. HKO §2(a), (2.2)–(2.8) gives \(|Z'(\theta_j)|=\prod_{l\ne j}|e^{i\theta_l}-e^{i\theta_j}|\) and, with HKO exponent \(k=2\), the exponent \(2k+2=6\) after rotation to root 1. The \(N-1\) free points have density proportional to the squared free Vandermonde times \(\prod|1-z_j|^6\). It is the squared evaluation determinant for \((z-1)^3z^j\), \(0\le j\le N-2\). Thus their determinantal projection \(P\) is the subspace in \(E=\operatorname{span}\{1,z,\ldots,z^{N+1}\}\) with a triple zero at 1. Its complement \(Q\) has mode vectors spanning the polynomials in the mode index of degrees 0, 1, 2. More generally a global tilt \(|Z'|^{2(h-1)}\) removes rank \(h\) in dimension \(n=N-1+h\). [HKO original, pp. 2614–2615](../../sources/classical63_lfunctions/hko2000.pdf)

Take \(0<a<b<1\), \(k\in[aN,bN]\cap\mathbb Z\), and the real statistic summing \(-\sum_k\cos(k\theta)/k\) over free points plus the deterministic root. Write \(H_N=\sum_k1/k\) and \(F=-z\sum_k\cos(k\theta)/k\). Its finite generating function is
\[
 e^{-zH_N}\det A\det((A^{-1})_{QQ}),\qquad A=E e^F E.
\]
The equality uses the projection determinant for the free points and the complementary principal-minor identity \(\det A_{PP}=\det A\det((A^{-1})_{QQ})\) in an orthonormal decomposition. This is Jacobi’s complementary-minor identity, also obtained by taking determinants of the block Schur complement. For the base determinant the Haar trace rule follows by Schur orthogonality of power sums at equal signed weights \(j\le n\). Unbalanced terms vanish by rotation and each balanced term with \(r\) factors has weight at most \(r\lfloor bN\rfloor/2\). Thus up to the stated window the determinant is the coefficient truncation of \(e^{H_N z^2/4}\). The root yields the factor \(e^{-zH_N}\). [Diaconis–Evans, Theorem 2.1(a)](../../sources/prime84_cue/diaconis_evans.pdf)

## Coefficientwise half-line calculation for arbitrary rank

To check the transfer independently, attach commuting labels to signed frequency sources and use the formal Neumann series for \(A^{-1}\). A path edge carries the net shift of the sources in its exponential block. Let \(P_+,P_-\) be the positive and absolute negative sums of all sources and \(D=P_+-P_-\). The path between endpoints in \(\{0,\ldots,n-1\}\) cannot visit both \(\le-1\) and \(\ge n\) if \(P_+,P_-\le n\), since the difference between such vertices is at least \(n+1\). The finite inverse coefficient is therefore the two half-line coefficients minus the full-line coefficient. On the left half-line the symbol factorization has upper-triangular factor \(T(e^{F_-})\) followed by lower-triangular \(T(e^{F_+})\). The intermediate mode lies above both endpoints in this order, so no term of the full product is lost. The inverse reverses the factors and negates \(F\). The order is swapped on the right. These identities are formal and require no uniform analytic inversion in \(N\).

Write \(j\) for the starting mode and \(j+D\) for the final mode. The left inverse permits \(j\ge P_-\); the right permits \(j<n-P_+\). For starts with both endpoints in range, adding those indicators and subtracting one gives exactly the **oriented** range \([P_-,n-P_+)\). If \(n-P_+<P_-\), the reversed interval is counted with a minus sign. Both endpoints of the oriented interval are within the closed hull of the admissible-start interval under \(P_\pm\le n\). Thus each coefficient is the coefficient of \(e^{-F_+}e^{-F_-}\) times the oriented compression of the two mode vectors. This argument does not use the rank or a precomputed rank-two transfer.

With \(p=P_+/n\), \(q=P_-/n\), \(D=p-q\) in scaled coordinates, and \(v_h(t)=(\sqrt{2j+1}\,\mathcal P_j(2t-1))_{0\le j<h}\) for the ordinary Legendre polynomials, the limiting compression is
\[
 C_h(p,q)=\int_q^{1-p} v_h(t+D)v_h(t)^Tdt .
\]
The finite orthonormal discrete polynomial vectors after multiplication by \(\sqrt n\) converge uniformly to \(v_h\) on the grid: their fixed-dimensional Gram matrices converge by Riemann summation and Gram–Schmidt is continuous at the positive definite limit. The oriented Riemann sums converge uniformly for the bounded scaled shift totals in a fixed order. At \(rb=1\), the rank-three dimension \(n=N+2\) gives \(r\lfloor bN\rfloor\le N<n\), including the endpoint without analytic continuation in \(b\).

## Formal averaging and the rank-three determinant

The weights in the positive-shift and negative-shift series of the inverse are both \(z/(2k)\). Each side has coefficient mass \(e^{zH_N/2}\); dividing by it and tagging the scaled shift total gives the finite formal cumulant exponent \((z/2)\sum_k (e^{u k/n}-1)/k\). The limiting variables \(p,q\) are independent in the formal moment sense with cumulant exponent \((z/2)\int_a^b(e^{u t}-1)dt/t\) on each side. For real \(z\ge0\) these auxiliary variables can also be realized as compound Poisson sums. The oriented matrix is polynomial and is evaluated for all auxiliary shifts, including those outside the coefficient window. It is the **expectation of the matrix entries** whose determinant is used. This extrapolation is not entrywise compression of a positive operator at unrestricted \(z\).

Consequently with \(H=\log(b/a)\), \(d=b-a\), \(m_j=(b^j-a^j)/j\), the rank-three limiting generating coefficients through \(rb\le1\) are those of
\[
e^{2Hz+Hz^2/4}P_3(z),\qquad P_3(z)=\det \mathbb E_z C_3(p,q).
\]
The \(+2Hz\) comes from the three determinant masses \(e^{Hz}\) and the single root factor \(e^{-Hz}\). Define \(L=1-p-q\). The change \(t=1/2-D/2+x\) centers the oriented interval at \(x=0\), with endpoints \(\pm L/2\). The two mode profiles become \((1,\sqrt{12}(x\pm D/2),\sqrt5[6(x\pm D/2)^2-1/2])^T\). Swap \(p,q\) and reflect \(x\) to see that entries with indices of opposite parity vanish after expectation. The two even cross entries agree. For example the \((0,2)\) integrand gives \(\sqrt5(L^3-L+3LD^2)/2\), and the \((1,1)\) entry gives \(L^3-3LD^2\). With \(l=1-dz\), elementary differentiation of
\[
\mathbb E_z e^{uL+vD}
=\exp\left(lu+\frac z2\sum_{j\ge2}m_j\frac{(-u+v)^j+(-u-v)^j}{j!}\right)
\]
gives the matrix
\[
\begin{pmatrix}
l&0&B\\0&C&0\\B&0&E
\end{pmatrix}
\]
where
\[
\begin{aligned}
B&=\sqrt5(l^3-l+6lz m_2-4z m_3)/2,\\
C&=l^3+2z m_3,\\
E&=(9l^5-10l^3+5l)/4
  + z(15l^3m_2-15lm_2+10m_3-6m_5)
  +z^2(45l m_2^2-60m_2m_3).
\end{aligned}
\]
Thus \(P_3=C(lE-B^2)\). At \(z=1/d\), the scalar \(l\) vanishes, \(C=2m_3/d\), and \(B=-2\sqrt5 m_3/d\); the determinant is \(-40(m_3/d)^3<0\). The sign does not depend on the sign of the off-diagonal entry in a different orthonormal-basis convention.

This gives a finite positive-square obstruction to the **all-order** surrogate. Let its moments be \(\mu_j=j![z^j]e^{2Hz+Hz^2/4}P_3(z)\) and let \(\mathcal L(X^j)=\mu_j\). At \(t=1/d\), the squares of \(q_M(X)=\sum_{j=0}^M(tX/2)^j/j!\) have \(\mathcal L(q_M^2)\to e^{2Ht+Ht^2/4}P_3(t)<0\). Indeed the double sum of absolute values is bounded by \(\sum_j|\mu_j|t^j/j!<\infty\) by entire analyticity. Some finite real square therefore has a negative value. This proof neither locates the first failing Hankel matrix nor puts that matrix within the valid moment window.

## First crossing and rank dependence

Let \((r-1)b\le1<rb\). The Gaussian base still holds because \(rb\le1+b<2\). Mixed-sign words satisfy the half-line comparison, and pure-sign words of total frequency above \(n\) have no fitting endpoints. At total exactly \(n\), their oriented extrapolation is empty. Hence only the missing pure-sign terms contribute to the first correction. As it starts in degree \(r\), its determinant contribution is the trace. In the limit, actual minus surrogate for the raw order-\(r\) cosine moment is
\[
 -2^{1-r}\int_{[a,b]^r\cap\{t=x_1+\cdots+x_r>1\}}
 \frac{A_h(t)}{x_1\cdots x_r}\,dx_1\cdots dx_r,
 \qquad A_h(t)=\operatorname{tr}C_h(t,0).
\]
For rank three direct integration gives \(A_3(t)=-3(t-1)[1+2t(t+1)(t^2-1)]<0\) on \(t>1\), so the correction is strictly positive. More generally the trace integrand on the positive-length interval \([1-t,0]\), before the orientation sign, is an alternating sum of
\((2j+1)\mathcal P_j(2(s+t)-1)\mathcal P_j(1-2s)\) with signs \((-1)^j\). Both arguments are at least one. The magnitudes strictly increase with \(j\) by the positive Taylor expansion of Legendre polynomials around 1 and the increasing \(2j+1\) factors. Thus the integrand has the sign of its final term, and the oriented trace has sign \((-1)^h\). The first crossing is strict for all ranks, since the open corner with each \(x_i\) close to \(b\) has positive measure.

The all-order positivity obstruction also extends to every fixed rank. Substituting \(t'=t+D\) in the oriented integral gives \(C_h(q,p)=C_h(p,q)^T\), and exchangeability gives a real symmetric expected matrix at real \(z\). The expected matrix at \(z=0\) is the identity. In every rank \(h\ge3\) the principal block with indices \(0,2\) at \(z=1/d\) has zero first diagonal entry and nonzero off-diagonal entry \(-2\sqrt5 m_3/d\), so the matrix has a negative eigenvalue there. Continuity of ordered eigenvalues gives a determinant zero in \((0,1/d)\). In rank one the entry \(1-dz\) vanishes at \(1/d\); in rank two that entry also supplies a determinant zero since opposite-parity entries vanish. Write \(t_*\) for the smallest positive determinant zero, and \(F_h=e^{(h-1)Hz+Hz^2/4}\det\mathbb E_z C_h(p,q)\). Since \(F_h(0)=1\), \(F_h(t_*/2)>0\). With the same Taylor polynomial \(q_M\) as above using \(t_*\), entire analyticity gives \(\mathcal L(q_M^2)\to F_h(t_*)=0\) and \(\mathcal L(q_M)\to F_h(t_*/2)\). Therefore the centered polynomial square has value
\[
\mathcal L\big((q_M-\mathcal L(q_M))^2\big)\longrightarrow -F_h(t_*/2)^2<0.
\]
This gives a finite negative square even when the determinant only touches zero. The determinant in fact has degree exactly \(h^2\): entry \((i,j)\) has degree at most \(i+j+1\), with highest-degree coefficient obtained by substitution of the means. There \(D=0\), \(L=1-dz\), and factoring the powers of \(-dz\) leaves the positive definite Gram matrix of the centered Legendre leading monomials on \([-1/2,1/2]\). The top coefficient has sign \((-1)^h\), which independently gives a negative value at some positive \(z\) for odd rank.

## Source and scope

The exact upstream ingredients are HKO’s joint root moment density, Andréief's projection determinant, Jacobi’s complementary-minor identity, triangular Toeplitz factorization and the ordinary CUE Schur trace rule. Bump–Diaconis treat classical Toeplitz minors and Basor–Widom use related Jacobi and triangular Toeplitz identities. Their fixed-symbol or fixed-minor asymptotics were not needed here. The rank-independent moving-symbol conclusion was derived at finite coefficient level by the two-edge exclusion, followed by fixed-order Riemann sums. The rank-three matrix and crossing trace were also independently expanded by symbolic polynomial integration and cumulant extraction. No arithmetic interpretation or publication priority is assigned. [Bump–Diaconis](../../sources/prime84_cue/bump_diaconis.pdf) · [Basor–Widom](https://arxiv.org/abs/math/9909010v3) · [Prior rank-two audit and primary-source checks](uniform86_cue_window_adjudication_input.md)
