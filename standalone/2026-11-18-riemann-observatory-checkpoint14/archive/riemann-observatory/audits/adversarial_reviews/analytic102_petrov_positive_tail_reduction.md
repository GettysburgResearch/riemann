# Positive rank-J reduction and uniform tail approximation for rooted CUE

Petrov’s tilted Fredholm factor divided by the ordinary ambient Fredholm factor is itself a positive determinant of size \(J\) on the real Laplace axis. The full Hardy determinant gives a simple lower bound for both tails and their quotient. These bounds are uniform in matrix size on compact real intervals, including at the first positive zero of the formal moment polynomial. A Hankel truncation at a prescribed number of bandwidths approximates the real factors with a factorial error in that number. [Independent source and factor check](analytic100_petrov_match_skeptic.md)

## Exact reduction

Use CUE size \(N\), rank \(J\), \(m=N-1\), \(n=m+J\), and \(P_n\) for the first \(n\) Hardy modes, with \(Q_n=I-P_n\). Write
\[
F_+(w)=-\sum_{k\in\mathcal B_N}\frac{w^k}{2k},\quad F_-(w)=F_+(w^{-1}),\quad
H_N=\sum_{k\in\mathcal B_N}\frac1k,\quad \phi=e^{z(F_++F_-)} .
\]
The band is \(aN<k\le bN\), \(0<a<b<1\). Put \(\phi_\pm=e^{zF_\pm}\), \(b_0=\phi_-/\phi_+\), and \(X=T((1-w)^J)|_{P_m}\). With \(C=T(\phi_-)X\), Petrov has \(R=C^*\) for real \(z\) and \(\Gamma=C^*C>0\). The symbol is smooth, nonvanishing, and of zero winding, with logarithm \(z(F_++F_-)\), so it meets Petrov §3.1. The row and column factors satisfy §4.1, and the Gram is invertible at every real \(z\). This uses Theorem 4.4, with no fixed-tail-chart assumption from Proposition 4.6. I checked (3.5)–(3.6), Theorem 4.4 and Corollary 3.3 in the v1 PDF with SHA-256 `f8b1c3386d49e61e767ae969a02131b509a42af276151ff04492b8be75a79214`. [Petrov v1](https://arxiv.org/pdf/2605.24976v1)

For real \(z\), let \(K=H(b_0)H(b_0)^*\) and \(A=I-K\). The Toeplitz product formula gives \(A=T(b_0)T(b_0)^*\). Since \(T(b_0)=T(\phi_-)T(\phi_+^{-1})\), the operator norm of its inverse is at most \(e^{|z|H_N}\). Thus
\[
 \delta I\le A\le I,\qquad \delta=e^{-2|z|H_N}.
\]
The point that reduces the quotient to finite rank is that the range of \(C\) lies in \(P_nH\). The map \(X\) ends there by polynomial degree, and the upper-triangular Toeplitz factor \(T(\phi_-)\) preserves that span. Consequently the exact tilted space is
\[
 V=(\operatorname{Ran}C)^\perp=Q_nH\oplus W,\qquad W=P_nH\ominus\operatorname{Ran}C,
 \qquad \dim W=J.
\]
Let \(Y:\mathbb C^J\to W\) be orthonormal columns and let \(D_n=Q_nA|_{Q_nH}\). The quotient is
\[
 \frac{L_{\rm obl}}{L_n}=\det S,qquad
 S=Y^*AY-Y^*A Q_nD_n^{-1}Q_nAY .
\]
In fact the compression to \(V\) has these two blocks. Products of the triangular eliminators are identity plus finite rank, each with determinant one, and yield \(S\oplus D_n\). This proves the quotient despite the infinite-dimensional tail. Its Schur complement satisfies \(\delta I_J\le S\le I_J\): its quadratic form is the infimum of \(\langle Yu+v,A(Yu+v)\rangle\) over \(v\in Q_nH\), and the upper bound follows by \(v=0\). This choice of tail charts only the \(J\)-dimensional difference from the ambient splitting. It remains valid where Petrov’s optional graph over the \(m\)-tail becomes singular.

## A finite formula for the quotient and a corrected continuum Gram

Write \(L=P_nT(\phi_+)|_{P_n}\), a unit lower-triangular matrix, and let \(U\) be orthonormal columns for the complement of \(X\) in \(P_nH\). Since the upper factor preserves \(P_nH\), \(C=L^*X\). Consequently \(Y=L^{-1}U M^{-1/2}\) is an orthonormal basis of \(W\), where \(M=U^*L^{-*}L^{-1}U\). The full ambient Schur complement of \(A\) across \(Q_nH\) is \((P_n A^{-1}|_{P_n})^{-1}\). Petrov’s Wiener–Hopf identity (3.5) gives \(P_n A^{-1}|_{P_n}=L^{-1} A_n L^{-*}\), using the triangular outer factors. Hence
\[
 S=Y^*L^*A_n^{-1}LY=M^{-1/2}(U^*A_n^{-1}U)M^{-1/2}.
\]
This computes the tail quotient exactly with finite matrices of order at most \(n\). The normalized Gram itself satisfies \(\det\Gamma/\det\Gamma(0)=\det M\), either by the exact quotient or by finite Jacobi applied to \(LL^*\), whose determinant is one. Since \(L\) and \(L^{-1}=P_nT(e^{-zF_+})|_{P_n}\) both have norm at most \(e^{|z|H_N/2}\), all eigenvalues of \(M\) lie in \([e^{-|z|H_N},e^{|z|H_N}]\), improving the determinant bound for this factor alone.

For a direct continuum description of the corrected Gram, take real \(z\ge0\). After dividing the coefficients of \(e^{-zF_+}\) by \(e^{H_Nz/2}\), they form the law of a compound Poisson integer shift. Its jumps at \(k\in\mathcal B_N\) have rates \(z/(2k)\). Two independent copies, divided by \(n\), converge to compound Poisson totals \(p,q\) with common intensity \(z\,dx/(2x)\) on \([a,b]\). This follows from the exponent of the characteristic function by Riemann summation. On the mode grid, multiplying \(U\) by \(L^{-1}\) performs a shift that vanishes before the corresponding displacement. Thus
\[
 e^{-H_Nz}M_{ij}\longrightarrow
 G_{ij}(z)=\mathbb E_z\left[
 \mathbf 1_{\max(p,q)\le1}\int_{\max(p,q)}^1
       u_i(t-p)u_j(t-q)dt\right],
\]
where \(u_i\) are the orthonormal shifted Legendre polynomials. The grid Riemann approximation is uniform for \(p,q\in[0,1]\) by bounded polynomial derivatives, and the displayed kernel with zero extension is continuous at the boundary since its interval shrinks there. Thus weak convergence gives the matrix limit. Its eigenvalues are bounded below by \(e^{-2Hz}\) by the finite bounds, and \(\det G(z)>0\).

In the coefficient window, the distinction from the oriented formal kernel can be seen directly. For shifts \(p,q\le1\), put \(D=p-q\) and change variables in the Gram kernel by \(s=t-p\). Its integration range is \([\max(0,q-p),1-p]\) with integrand \(u_i(s)u_j(s+D)\). The transposed formal compression has the same integrand over the **oriented** range \([q,1-p]\). Subtracting the latter leaves the ordinary lower piece \([\max(0,q-p),q]\), of length \(\min(p,q)\), even when the oriented interval is reversed. This vanishes for pure-sign words and explains why the two-sided distinction first appears at quadratic order. Outside the coefficient window the exact Gram continues with the true cutoff, whereas the formal polynomial uses extrapolated oriented entries.

## Explicit uniform separation from the formal zero

For any closed subspace \(E\subset H\), the positive eigenvalues of the compression of \(K\) to \(E\), in decreasing order and with multiplicities, are bounded by those of \(K\) by min–max. Therefore the associated determinant lies between the full determinant and one. The full determinant is exactly \(e^{-H_N z^2/4}\) by Petrov (3.6). Apply this to both \(V\) and \(Q_nH\). Since \(L_n\le1\) and \(S\le I\), this gives
\[
 e^{-H_N z^2/4}\le \frac{L_{\rm obl}}{L_n}=\det S\le1 .
\]
The normalized Gram ratio is the ambient complementary determinant divided by \(\det S\). The finite ambient symbol compression \(A_n=P_nT(\phi)|_{P_n}\) lies between \(e^{-|z|H_N}I\) and \(e^{|z|H_N}I\), by the pointwise bounds on the positive symbol. If \(U\) denotes the original deleted-mode columns in \(P_nH\), the exact quotient from the prior review now yields
\[
 \begin{aligned}
 e^{-J|z|H_N}&\le \det(U^*A_n^{-1}U)\le e^{J|z|H_N},\\
 e^{-J|z|H_N}&\le \frac{\det\Gamma(z)}{\det\Gamma(0)}
      \le e^{J|z|H_N}.
 \end{aligned}
\]
For example, writing \(R_{J,N}(z)=e^{-JH_Nz}\det(U^*A_n^{-1}U)\), at any positive formal determinant zero \(z_*\) we have the strict quantitative discrepancy
\[
 \liminf_{N\to\infty} R_{J,N}(z_*)\ge e^{-2JH z_*}>0,
 \qquad H=\log(b/a).
\]
These inequalities hold uniformly on compact real parameter intervals because \(H_N\) is bounded. They exclude an interpretation of the formal zero as an emerging small eigenvalue of the exact complementary or tail factors. The factorization remains compatible with agreement of the low Taylor coefficients. [Formal fixed-rank window and zero](analytic93_rank_three_skeptic.md)

## Factorial truncation in the number of bandwidths

This reduction admits uniform finite approximations of the infinite tail by simply truncating the Hankel factor. Fix \(|z|\le Z\) real and let \(k_*=\max\mathcal B_N\). Write \(g=F_--F_+\), so \(b_0=e^{zg}\). For a Laurent sequence use the seminorm \(\|u\|_*^2=\sum_k|k||u_k|^2\). The triangle inequality for \(\sqrt{|k|}\), followed by Young’s convolution inequality, gives
\[
 \|u*v\|_*\le \|u\|_*\|v\|_1+\|u\|_1\|v\|_*.
\]
Here \(\|g\|_1=H_N\) and \(\|g\|_*^2=H_N/2\). In particular \(\|g^{*r}\|_*\le rH_N^{r-1}\sqrt{H_N/2}\). Its frequencies lie in \([-rk_*,rk_*]\). Let \(P_M\) project onto the first \(M\ge n\) Hardy modes. A Hankel entry removed by cutting both rows and columns has \(i+j+1>M\), so with \(H_b=H(b_0)\) we have
\[
 \|H_b-P_MH_bP_M\|_2
 \le \left(\sum_{k>M} k|(b_0)_k|^2\right)^{1/2}
 \le |z|\sqrt{H_N/2}\sum_{s\ge\lfloor M/k_*\rfloor}\frac{(|z|H_N)^s}{s!}.
\]
The same convolution estimate without the support restriction bounds \(\|H_b\|_2\le |z|\sqrt{H_N/2}e^{|z|H_N}\). Put \(H_M=P_MH_bP_M\), \(K_M=H_MH_M^*\). By Schatten Hölder,
\[
 \|K-K_M\|_1\le (\|H_b\|_2+\|H_M\|_2)\|H_b-H_M\|_2.
\]
Since \(\|H_M\|\le\|H_b\|\), both \(I-K_M\) and \(I-K\) have the same spectral lower bound \(\delta\). On either \(E=V\) or \(E=Q_nH\), interpolate these positive compressed operators. Differentiating the log determinant along the trace-class segment gives
\[
 |\log L_E-\log L_{E,M}|\le \delta^{-1}\|K-K_M\|_1 .
\]
Here \(L_{E,M}\) is the corresponding compressed determinant for \(K_M\). It needs only the first \(M\) coordinates since \(M\ge n\) and both spaces split off the entire tail \(Q_MH\). For a fixed real compact parameter interval, choosing \(M\ge\max(n,Lk_*)\) thus gives a bound in terms of the factorial tail \(\sum_{s\ge L}(Z\sup_NH_N)^s/s!\), uniformly in \(N\). The same estimate with twice the constant controls the log quotient. In this construction the range \(W\) and the Gram are exactly finite from the start, and the Hankel coefficients may be computed from the convergent scalar exponential. This supplies a controlled finite-dimensional realization of the corrected factors on the real axis. It does not use a formal moment extrapolation to compute them.

No priority claim follows from this specialization of the classical operator identities. The inequalities and finite truncation here concern the real Laplace parameter and the finite rooted CUE model, with no arithmetic implication.
