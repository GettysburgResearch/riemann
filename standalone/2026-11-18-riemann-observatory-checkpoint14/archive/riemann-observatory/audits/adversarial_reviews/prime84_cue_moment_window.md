# Exact low-frequency moment window for global derivative-rooted CUE

18 November 2026. This is an intrinsic random-matrix calculation. Use the global Haar matrix/root-label tilt by the derivative square and include the chosen root at angle zero. For a fixed band \(0<a<b<\infty\), denote the negative cosine and sine traces integrated with the finite weights \(1/k,\ aN<k\le bN\), by \(C_N,S_N\). Put
\[
 H=\log(b/a),\quad d=b-a,\quad
 J_2=(b^2-a^2)/2,\quad J_3=(b^3-a^3)/3,\qquad q=2J_3.
\]
The mixed moments of the limiting rooted CUE law at each total degree \(r\) with \(rb\le1\) are the coefficients, with the usual factorials, of
\[
 {\cal F}(z_c,z_s)
 =e^{H z_c+H(z_c^2+z_s^2)/4}
   \big[(1-dz_c)^4+qz_c(1-dz_c)-3J_2^2 z_s^2\big].
 \tag{1}
\]
In particular its cosine moments agree with the quartic formal expression of the arithmetic work on this larger RMT window. At the first integer \(r\) with \((r-1)b\le1<rb\), the cosine moment is strictly smaller than that formal coefficient. The joint homogeneous correction is explicit below. The inclusion of \(rb=1\) in the RMT claim is justified at finite \(N\). This result supplies no arithmetic moment beyond the source window \(rb<1/2\), and no publication priority is claimed. [Full rooted CUE law and uniform moments](prime77_rooted_cue_band_limit.md) · [Arithmetic window](prime79_hlz_formal_moment_obstruction.md)

## 1. Complementary finite Toeplitz determinant

Set \(n=N+1\), and let \(E\) be the Fourier subspace of degrees \(0,\ldots,n-1\). The free points are the orthogonal projection of rank \(n-2\) onto the polynomials in \(E\) vanishing twice at 1. Let \(U\) have the two orthonormal columns of the complementary projection \(Q=UU^*\), given in degree coordinates by
\[
 U_0(j)=1/\sqrt n,\qquad
 U_1(j)=(j-(n-1)/2)/\sqrt{n(n^2-1)/12}.
\]
The density and projection follow directly from the derivative-square root tilt. Let \(f_c(\theta)=-\sum \cos(k\theta)/k,\ f_s(\theta)=-\sum\sin(k\theta)/k\), summing \(aN<k\le bN\). Define \(F=z_c f_c+z_s f_s\), with \(H_N=\sum_{aN<k\le bN}1/k\). The symbol \(e^F\) and \(A=T_n(e^F)=E M_{e^F} E\) determine the finite generating function. Jacobi's complementary-minor identity in an orthonormal basis starting or ending with \(U\) gives
\[
 E e^{z_c C_N+z_s S_N}
 = e^{-H_N z_c}\det A\,\det(U^*A^{-1}U).
 \tag{2}
\]
One may also obtain this via the Schur complement since \(A(0)=I\); the complement compression of \(A\) is the free-particle determinant. The factor \(e^{-H_N z_c}\) is exactly the chosen root. All ensuing uses of (2) are formal Taylor coefficient identities at the origin. [Tilt and first-two-moment projection](prime71_hlz_band_covariance.md)

Take independent formal sources at each signed Fourier frequency for the moment. For a given monomial define its positive and negative weighted totals as the sums of its positive and absolute negative frequencies, counting multiplicities. Whenever both totals are at most \(n\), the coefficient of \(\det A\) is its usual stable CUE coefficient. One route is Diaconis–Evans, Theorem 2.1(a), whose correct condition is \(n\ge\max(\text{positive total},\text{negative total})\). Equivalently expand the two exponential series using Schur functions and their Cauchy identity. In weighted degree \(m\le n\), every partition of \(m\) has at most \(n\) parts, so the unrestricted Schur orthogonality calculation agrees with the finite one. For our sources, the stable formal factor is \(\exp\{H_N(z_c^2+z_s^2)/4\}\), because the positive and negative Fourier values of \(F\) are \(-u/(2k),-v/(2k)\) with \(u=z_c-i z_s,\ v=z_c+i z_s\), and the Szegő quadratic form is \(\sum_{k>0} k F_k F_{-k}\). For a pure-sign monomial \(\det A=1\) in every degree after the opposite-sign sources are set to zero, by triangularity. [Diaconis–Evans, Theorem 2.1](../../sources/prime84_cue/diaconis_evans.pdf) · [Bump–Diaconis, Toeplitz minor and Schur antecedents](../../sources/prime84_cue/bump_diaconis.pdf)

## 2. Finite inverse through the two-edge support range

For a subset \(J\) of the integer mode line, expand the inverse of \(T_J(e^F)\) in the formal Neumann series in \(T_J(e^F)-I\). Coefficients are finite sums of paths with all intermediate vertices in \(J\). A matrix step may combine several signed Fourier sources from one exponential coefficient. A segment of any path cannot have a positive net displacement larger than the monomial’s positive total, nor a negative one with magnitude larger than its negative total. Start and finish in \(E=\{0,\ldots,n-1\}\). To hit both a vertex \(<0\) and a vertex \(\ge n\) requires a displacement of at least \(n+1\) in one direction. Thus if each signed total is at most \(n\), inclusion–exclusion gives the finite inverse coefficient as the sum of its left and right half-line inverse coefficients minus the whole-line inverse coefficient, for each entry on \(E\). This establishes finite coefficient localization without an analytic strong Szegő limit or a fixed-symbol assumption.

Write \(F=F_++F_-\) for its strictly positive and negative parts. On the left half-line \(j\ge0\), the factorization
\(T(e^F)=T(e^{F_-})T(e^{F_+})\) is exact. In the matrix convolution of upper times lower triangular factors, the intermediate index is at least both endpoint indices, so the half-line boundary omits no summands. The inverse there is \(T(e^{-F_+})T(e^{-F_-})\). On the right half-line \(j\le n-1\), use the opposite orders. On the whole line the inverse is convolution with \(e^{-F}\). These identities hold as formal coefficients, since each order has finite support. Write \(\beta_p,\eta_q\) for the coefficients at shifts \(p,-q\) of \(e^{-F_+},e^{-F_-}\), with \(p,q\ge0\).

For \(U^*A^{-1}U\), the term weighted by \(\beta_p\eta_q\) starts in the whole-line representation with endpoints \(i=l+p,\ j=l+q\) and \(l\) in \([-\min(p,q),n-1-\max(p,q)]\). Subtracting the left-boundary omission leaves \(l\ge0\). After reflecting the right-boundary omission, its two endpoints are \(l+q,l+p\), with \(l<0\), and the coefficient-vector parity supplies \(\(-1\)^{\nu+\mu}\) for basis labels \(\nu,\mu=0,1\). Consequently its two-by-two compression matrix is
\[
 D_{\nu\mu,n}(p,q)
 =\sum_{l=0}^{n-1-\max(p,q)}U_\nu(l+p)U_\mu(l+q)
  -\(-1\)^{\nu+\mu}\sum_{l=-\min(p,q)}^{-1}U_\nu(l+q)U_\mu(l+p).
 \tag{3}
\]
For the admissible monomial \(p,q\le n\). The upper sum can be empty at \(p=n\) or \(q=n\). Using finite sums of \(1,l,l^2\), (3) simplifies in both orderings of \(p,q\) to the polynomials
\[
 \begin{split}
 D_{00,n}&=1-(p+q)/n,\\
 D_{11,n}&=\frac{(p+q-n)(1-n^2+2n(p+q)+2p^2+2q^2-8pq)}
                  {n(n^2-1)},\\
 D_{01,n}&=\frac{\sqrt3(p-q)(p+q-n)}{n\sqrt{n^2-1}},
 \qquad D_{10,n}=-D_{01,n}.
 \end{split}
 \tag{4}
\]
The endpoint \(p=n\) is included. The distance between the two closest forbidden vertices \(-1\) and \(n\) is \(n+1\), so the path proof still applies. The first sum in (3) is then empty and the second need not be. For an independent exact endpoint example, the mixed \(st\) coefficient of \(T_n(\exp(s z^n+t z^{-1}))^{-1}\) is \(-T_n(z^{n-1})\), since \(T_n(z^n)=0\). Its compression is the negative outer product of the last and first rows of \(U\), which equals (4) with \(p=n,q=1\). In the pure case \(p=n,q=0\), all corresponding entries vanish. The off-diagonal entries cannot be dropped for a sine source. The denominators are nonzero for \(n\ge2\). The code checks (4) by discrete polynomial antiderivatives. This shrinking Fourier scale calculation is not an invocation of a fixed-index Toeplitz minor limit. The Bump–Diaconis framework supplies a relevant antecedent for representing Toeplitz minors and asymptotics, not the finite moving-frequency coefficient identity here. [Bump–Diaconis, §§2–3](../../sources/prime84_cue/bump_diaconis.pdf) · [Symbolic compression and direct determinant check](../../scripts/prime84_cue_moment_window_check.py)

## 3. Joint finite surrogate and its limit

Let \(K_N\) be the largest integer in the band, taking zero for an empty band. Put
\[
 d_N=\#\{aN<k\le bN\}/n,\qquad
 J_{2,N}=\frac{\sum_{aN<k\le bN}k}{n^2},\qquad
 J_{3,N}=\frac{\sum_{aN<k\le bN}k^2}{n^3}.
\]
Sum the formal polynomial in (4) against \(\beta_p\eta_q\). The total mass of these coefficients is \(\exp((u+v)H_N/2)=\exp(z_c H_N)\). After dividing by this mass, the formal first three cumulants of \(p/n\) are \(u d_N/2,u J_{2,N}/2,u J_{3,N}/2\); for \(q/n\) replace \(u\) by \(v\). This follows on replacing the Fourier variable in \(e^{-F_+}\) by \(e^{t/n}\) and dividing by its value at 1, and similarly for the negative sector. In particular joint averages of factorable polynomials are computed by multiplying the corresponding formal moments.

For clarity set \(L_c=1-d_N z_c\) and \(\epsilon=1/n^2\). The normalized \(00\) entry is \(L_c\), and the normalized \(01\) entry is
\[
 -i\sqrt3\, z_s(d_N^2 z_c+J_{2,N}-d_N)/\sqrt{1-\epsilon}.
\]
The normalized \(11\) entry is
\[
 \{L_c^3+2J_{3,N}z_c+
      [3d_N^2-3d_N^3 z_c-6J_{2,N}d_N]z_s^2-\epsilon L_c\}/(1-\epsilon).
\]
The other off-diagonal is its negative under this formal convention. Taking the determinant cancels the additional \(z_c z_s^2,z_c^2z_s^2\) terms and yields the finite surrogate
\[
 {\cal F}_N(z_c,z_s)= e^{H_N z_c+H_N(z_c^2+z_s^2)/4}
 \frac{L_c^4+2J_{3,N}z_c L_c-3J_{2,N}^2 z_s^2-\epsilon L_c^2}
      {1-\epsilon}.                                               \tag{5}
\]
The exponential here combines the mass squared of the two-by-two compression, the base determinant and the chosen root. Each Taylor coefficient agrees with (2) through total degree \(r\) whenever \(rK_N\le n\). More generally, before specializing signed sources, equality holds for each monomial with positive and negative totals individually at most \(n\). All coefficient products preserve this conclusion, since their submonomials satisfy the same bounds. In the limit \(H_N\to H,d_N\to d,J_{j,N}\to J_j\), by Riemann sums, proving (1) for \(rb\le1\). These are the moments of the actual RMT limit because the full-law theorem supplies uniform exponential integrability. In particular the result is not a Gaussian claim for this band. [Moment convergence of the complete rooted law](prime77_rooted_cue_band_limit.md)

## 4. First departure and finite checks

Suppose \((r-1)K_N\le n<rK_N\). At order \(r\), a word having both frequency signs still satisfies the individual shift conditions, because each sign occurs at most \(r-1\) times. Hence the only possible departure from (5) comes from pure-sign words of total unsigned shift \(p>n\). On one sign, the Toeplitz matrix and its inverse are triangular with symbol \(e^F\) and \(e^{-F}\), respectively. Coefficients with total shift \(p>n\) have identically zero entries in the true compressed matrix. In the polynomial extrapolation (4) their contribution to the inverse compression is given by \(D_{\nu\mu,n}(p,0)\) or its transpose. The first discrepancy of the determinant is its trace discrepancy, since all lower coefficients agree and its constant matrix is \(I\). Its trace polynomial at this shift is
\[
 A_n(p)=D_{00,n}(p,0)+D_{11,n}(p,0)
       =\frac{2(p-n)(p^2+np-n^2+1)}{n(n^2-1)}.
\]
The base determinant is exactly 1 in pure signs, and the root factor cannot change a first discrepancy because it is 1 at the origin. Thus the degree-\(r\) discrepancy of the finite joint Taylor series is exactly
\[
 -\frac{(z_c-i z_s)^r+(z_c+i z_s)^r}{2^r r!}
      \sum_{\substack{k_1,\ldots,k_r\text{ in band}\\p=k_1+\cdots+k_r>n}}
                 \frac{A_n(p)}{k_1\cdots k_r}.
 \tag{6}
\]
This uses the ordered expansion of \(e^{-F_+}\) and \(e^{-F_-}\). It also accounts for powers repeating the same frequency.

When \((r-1)b\le1<rb\), the finite conditions for (6) hold eventually and the sum tends to
\[
 I_r=\int_{\substack{(x_1,\ldots,x_r)\in[a,b]^r\\x_1+\cdots+x_r>1}}
        A(x_1+\cdots+x_r)\prod_{j=1}^r\frac{dx_j}{x_j},
 \qquad A(t)=2-4t+2t^3.
\]
Here \(A(t)=2(t-1)(t^2+t-1)>0\) for \(t>1\), and a positive-measure portion near the upper corner has sum \(>1\). The boundary does not affect the Riemann sum. The joint homogeneous difference is the expression (6) with the sum replaced by \(I_r\), and the first cosine raw-moment discrepancy is \(-2^{1-r}I_r<0\). In particular the initial matching window ends precisely at the first integer beyond \(rb\le1\). No formula after this first chamber is asserted. Specifying any signed list of frequencies whose separate totals are at most the mode dimension continues to suffice coefficientwise.

The exact script checks (4) and the full joint polynomial determinant, then directly evaluates finite rooted projection determinants independently of the complementary-minor calculation. It uses the Taylor matrices \(P T_n(F^j)P/j!\), their inverse recurrence, and \((\log\det A)'=\operatorname{Tr}(A^{-1}A')\); thus no low-rank inverse formula is built into that benchmark. At \(N=100\), fourth and fifth moments of \([1/20,1/10]\) agree with the finite surrogate, and first-crossing fourth and fifth moments of \([13/50,8/25]\) and \([41/200,49/200]\), respectively, agree after the correction (6). Both the cosine ray and the ray \((z_c,z_s)=(0.8t,0.6t)\) are tested. Two further runs at \(N=99\), band \([4/25,21/100]\) and order 5, check the inclusive case \(rK_N=n=100\) on both rays. All discrepancies across the ten examples are below \(2\cdot10^{-15}\) in the recorded double-precision run. These are implementation checks accompanying the finite proof, not numerical certificates of an arithmetic result. [Exact symbolic and finite benchmark code](../../scripts/prime84_cue_moment_window_check.py) · [Recorded outputs](../../experiments/results/prime84_cue_moment_window_check.txt)
