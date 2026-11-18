# Rooted derivative-weighted CUE and prime-band moments

The derivative-square rooted CUE model matches the arithmetic band mean and covariance for \(0<a<b<1/4\). It also matches the centered third moment for \(b<1/6\). The common third moment is strictly negative on any such nonempty band. Fourth moments are bounded on either side, so a Gaussian weak subsequential limit is impossible in the cubic range. These are moment comparisons with an obstruction to Gaussian convergence. They do not identify a full limiting law. The arithmetic assertions assume RH. [Arithmetic covariance](weighted71_hlz_band_second_moment.md) · [Uniform HLZ cutoff audit](weighted70_hlz_cutoff_review.md)

## The HKO probability and the projection

The primary source is Hughes–Keating–O'Connell, *Proc. Roy. Soc. Lond. A* **456** (2000), pp. 2611–2627, Theorem 1.2 and §2(a), pp. 2614–2615, (2.2), (2.3), and (2.5)–(2.9). In their (1.13) and (2.4) the label of the root is averaged together with the Haar integral. To obtain a probability, normalize the joint law of the Haar matrix and uniform label by the derivative-square weight in this integral. The geometry of the tilted law follows directly from (2.8) with their moment exponent \(k=1\). After rotating the selected eigenangle to zero, the other \(N-1\) points have density proportional to
\[
 \prod_{i<j}|z_i-z_j|^2\prod_i|1-z_i|^4
\]
against circle Haar measure. The \(|1-z|^4\) combines the two powers from Haar repulsion from the root and two from its derivative-square weight. A construction that first samples a Haar matrix without changing its marginal and then normalizes the derivative-square label probabilities separately within that matrix would give a different joint density. [HKO primary source](../../sources/classical63_lfunctions/hko2000.pdf)

Write \(E\) for the projection onto circle Fourier degrees \(0,\ldots,N\). The determinant of the \(N-1\) functions \((1-z)^2 z^j\), \(0\le j\le N-2\), is the Vandermonde times \(\prod_i(1-z_i)^2\). After orthonormalizing these functions, their squared determinant is the joint density of a projection DPP. Their span consists of exactly the polynomials in \(E\) with both value and derivative vanishing at 1. Its projection is \(P=E-Q\), where \(Q\) has two orthonormal coefficient vectors
\[
 u_{0,N}(j)=\frac1{\sqrt{N+1}},\qquad
 u_{1,N}(j)=\frac{j-N/2}{\sqrt{N(N+1)(N+2)/12}},\qquad 0\le j\le N.
\]
Writing \(s=j/N\), their scaled continuum limits are \(u(s)=(1,\sqrt{12}(s-1/2))^{\mathsf T}\), uniformly with \(O(1/N)\) error after multiplying the vectors by \(\sqrt N\). In particular \(Q_{ij}\) is \(N^{-1}q(i/N,j/N)+O(N^{-2})\), where \(q(s,t)=u(s)^{\mathsf T}u(t)=1+12(s-1/2)(t-1/2)\).

Define
\[
 X_N=-\sum_{aN<k\le bN}\frac1k
 \sum_{j=1}^N\cos(k(\theta_j-\theta_{\rm root})).
\]
The fixed root is included in the inner sum. HKO (1.6) uses \(N=\log(T/(2\pi))\). In the limiting comparison this identifies \(k/N\) with \(\log p/\log Y\), using \(N/\log Y\to1\). The limiting frequency measure is \(dx/x\) on both sides, by Riemann summation for \(\sum 1/k\) and prime reciprocal Mertens for \(\sum 1/p\). The negative sign in \(X_N\) is needed for the mean and third cumulant.

## Exact rank-two covariance calculation

On the full integer Fourier basis let \(S^k e_j=e_{j+k}\). For positive \(x=k/N\), the restriction of \(S^k\) between the \(Q\) vectors tends uniformly to
\[
 M(x)=\int_0^{1-x}u(s+x)u(s)^{\mathsf T}ds
   =\begin{pmatrix}
       1-x&-\sqrt3 x(1-x)\\
       \sqrt3 x(1-x)&1-3x+2x^3
     \end{pmatrix}.
\]
For negative \(k\) use \(M(x)^{\mathsf T}\) with \(x=|k|/N\). Since \(\operatorname{Tr} E S^k=0\) for \(k>0\), the mean of the negative real trace including the root tends to \(\operatorname{Tr}M(x)-1=F(x)=1-4x+2x^3\).

For commuting circle multipliers \(f,g\), the bilinear covariance of their linear statistics for a projection \(P\) is \(\operatorname{Tr}(Pfg)-\operatorname{Tr}(PfPg)\). This identity follows from the first two determinantal intensities and holds for complex multipliers as bilinear covariance without conjugation. Subtracting the formula for \(E\) gives
\[
 -\operatorname{Tr}(Qfg)+\operatorname{Tr}(QfEg)+
   \operatorname{Tr}(QgEf)-\operatorname{Tr}(QfQg).
\]
For \(f=S^k,g=S^\ell\) with \(k,\ell>0\) and \(x=k/N,y=\ell/N\), the two intermediate path constraints are automatic if both endpoints fit in \(E\). The first three terms tend to \(\int_0^{1-x-y}q(s,s+x+y)\,ds\). For \(f=S^k,g=S^{-\ell}\), they tend to \(\int_y^{1-x}q(s,s+x-y)\,ds\). This follows by inclusion–exclusion on the intermediate points \(s-y\) and \(s+x\), since their allowable intervals cover the full endpoint interval when \(x+y<1\). The last term is respectively \(\operatorname{Tr}(M(x)M(y))\) and \(\operatorname{Tr}(M(x)M(y)^{\mathsf T})\). Exact integration gives the signed corrections
\[
 C_{++}(x,y)=C(x,y)+6x^2y^2,\qquad
 C_{+-}(x,y)=C(x,y)-6x^2y^2,
 \qquad C(x,y)=-4xy+6x^3y+6xy^3-4x^3y^3 .
\]
All limits are uniform as \(x,y\) range in the fixed permitted band, since they are bounded polynomial Riemann sums on grid intervals. The ordinary CUE projection \(E\), of size \(N+1\), has same-sign covariance zero and opposite-sign covariance \({\bf1}_{k=\ell}\min(k,N+1)\) by counting valid two-step paths. Thus cosines and sines have diagonal \(\frac12\min(k,N+1)\) and corrections \(C(x,y)\) and \(-6x^2y^2\), respectively. Reflection makes cosine-sine covariances vanish. Multiplying by the two \(1/k\) weights gives the shared diagonal limit \(\frac12\int_a^b dx/x\), and the signed corrections integrate against \(dx\,dy/(xy)\). The root is deterministic in these coordinates and adds no covariance. The argument carries over to fixed bounded piecewise continuous frequency multipliers by the same Riemann sums. [Exact covariance check](../../scripts/weighted73_cue_band_checks.py)

## Third cumulant on the arithmetic side

Take \(0<a<b<1/6\), so the largest product of primes in a cubic aggregate has size at most \(Y^{3b}\), within a fixed HLZ declared length \(T^\delta\) with \(3b<\delta<1/2\). Write \(D=\sum_{Y^a<p\le Y^b}p^{-s}\). Use \((\Re D)^3=(\Re D^3+3\Re(D^2\overline D))/4\), with divisor-closed bounded padding applied to the products \(D^3\) against 1 and \(D^2\) against \(D\). For three distinct primes, let \(x,y,z\) be their logs divided by \(L_T=\log T\). The four reduced twists are all primes on one side and the three choices of a pair on one side against the single remaining prime. Each has arithmetic factor \(1/(pqr)\) and the symmetrized local multiplier used in the second-moment proof. If \(H,K\) list the scaled prime logs in the two reduced indices, their local average is
\[
 \frac{e^{-v\sum H}\prod_{t\in K}(e^{-ut}+e^{-wt}-1)
       +e^{-v\sum K}\prod_{t\in H}(e^{-ut}+e^{-wt}-1)}2 .
\]
The uniform prime-factor errors here are \(O(p^{-1}+q^{-1}+r^{-1})\) and include the correct lcm factor when summed. Use the cubic exponentials in HLZ (5), the quartic exponentials in (24), the three residue tuples, their reflection, and the auxiliary derivative exactly as in the second-moment proof. Let \(K_3\) denote the resulting normalized average of the four raw kernels. For example at equal coordinates \(x\) the raw all-on-one-side kernel is \(1-12x+36x^2-18x^3+6x^4\), while the pair-versus-single kernel is \(1-12x+36x^2-18x^3-18x^4\).

For repeated primes, \(\cos^2 u=(1+\cos 2u)/2\). Terms with exactly two equal primes contribute \(\frac32 H_{\rm band} E_T W_Y+o(1)\). The terms containing \(\cos(2\gamma\log p)\) are \(o(1)\) after aggregating: use the cross term of \(D_2=\sum p^{-2s}\) with \(D\) for \(\Re(D_2\overline D)\), and the cross term of \(D_2D\) with \(1\) for \(\Re(D_2D)\). Distinct-prime weights are \(1/(p^2q)\), with bounded local factors, and equal-prime lcm weights at most \(1/p^2\). Terms with all three primes equal, as well as the diagonal wrongly added to the \(\frac32 H_{\rm band} E_T W_Y\) expression, are bounded absolutely by a constant times \(\sum_{p>Y^a}p^{-3/2}\). The arithmetic errors tend to zero uniformly in \(T\ge Y\) by the aggregate cutoff argument. The covariance diagonal \(\frac12 H_{\rm band}\) cancels \(\frac32 H_{\rm band} E_T W_Y\) in the centered third moment. Strict-tail transfer works for the raw first three moments before centering, using the same concentration of \(L_T/L_Y\) and the same uniform prefix errors as in the previous band calculation.

The remaining centered kernel is
\[
 \begin{aligned}
 C_3(x,y,z)
 &=K_3(x,y,z)-K_0(x,y)F(z)-K_0(x,z)F(y)-K_0(y,z)F(x)
                      +2F(x)F(y)F(z)\\
 &=8xyz\left[-1+3(x^2+y^2+z^2)-3(x^2y^2+x^2z^2+y^2z^2)
                       +2x^2y^2z^2\right].
 \end{aligned}
\]
This is independently checked symbolically by applying the rescaled residues to each prime allocation separately. No assumption of independence is made for the arithmetic phases. The unscaled centered third moment tends to the integral of \(C_3\) against \(dx\,dy\,dz/(xyz)\) on the band cube. Writing \(\Delta=b-a\) and \(\Delta_3=b^3-a^3\), it equals
\[
 -8\Delta^3+24\Delta^2\Delta_3-8\Delta\Delta_3^2+\tfrac{16}{27}\Delta_3^3 .
\]
The bracket defining \(C_3\) is at most \(-1+9b^2+2b^6<0\) for \(b<1/6\), so the integral is strictly negative. [Exact arithmetic third-kernel check](../../scripts/weighted73_cue_third_kernel_checks.py)

## Third cumulant on the CUE side

For commuting functions \(f,g,h\), the joint third cumulant of a projection DPP is
\[
 \operatorname{Tr}(Pfgh)-\operatorname{Tr}(PfPgh)-\operatorname{Tr}(PgPfh)
 -\operatorname{Tr}(PhPfg)+\operatorname{Tr}(PfPgPh)+\operatorname{Tr}(PfPhPg).
\]
It follows by extracting the coefficient of the product of the three parameters in the log of the DPP generating determinant \(\det(1+(\exp(z_1 f+z_2 g+z_3 h)-1)P)\). For the base projection \(E\) and signed frequencies \(k,\ell,m\) all traces vanish unless their sum is zero. If it is zero, the one-block trace is \(N+1\), the three two-block traces are \(N+1-|k|,N+1-|\ell|,N+1-|m|\), and the two triple traces are \(N+1-\max(|k|,|\ell|,|m|)\). For a three-step closed path, the three pairwise separations between its visited offsets are \(|k|,|\ell|,|m|\), so this maximum is its span. The base cumulant is \(|k|+|\ell|+|m|-2\max(|k|,|\ell|,|m|)=0\), including resonances.

For the correction, expand each \(P=E-Q\) in the trace words. In a term with at least one \(Q\), split the cyclic word at its \(Q\) occurrences. For a segment whose normalized shifts in operator order are \(\delta_1,\ldots,\delta_r\), put \(t_0=0\), \(t_j=\delta_r+\cdots+\delta_{r-j+1}\). The associated \(2\times2\) continuum transfer matrix is
\[
 \int_{-\min_j t_j}^{1-\max_j t_j}u(s+t_r)u(s)^{\mathsf T}\,ds .
\]
This follows by inserting the discrete \(Q\) basis, transforming the rightmost Fourier shift first, and retaining only terms whose visited Fourier indices lie in \(E\). The product of these matrices around the cyclic \(Q\) occurrences has trace equal to the segment contribution, with sign \((-1)^{\# Q}\). All paths here have span at most \(3b<1\). Finite sums converge to these matrices uniformly with \(O(1/N)\) error, by polynomial Riemann summation with explicit interval endpoints.

To evaluate the negative-cosine cumulant, take minus one fourth of the sum over the all-positive assignment and the three assignments with a single negative shift. Reflection supplies the other four. By permutation symmetry it suffices to order \(x\le y\le z\). Then signs of the differences of visited offsets are determined by this order and \(z\lessgtr x+y\), because such differences are signed sums of consecutive subsets of the three shifts. At fixed order the two open chambers therefore exhaust the branches of every transfer matrix. The exact symbolic test checks both polynomial expressions on their chambers and they agree with the arithmetic \(C_3\). By continuity the same is true on their boundaries. The deterministic root has no centered third contribution. Summing with the \(1/k\) weights gives the same triple integral as on the arithmetic side, with no additional resonant term. [Exact chamber and arithmetic checks](../../scripts/weighted73_cue_third_kernel_checks.py)

## Fourth-moment bounds and the Gaussian obstruction

On the arithmetic side, \(|W_Y|^4\le|D|^4=|D^2|^2\). This is one quadratic HLZ evaluation with length \(Y^{2b}\), admissible whenever \(b<1/4\). The bounded local kernel times the nonnegative Fourier model weights majorizes the aggregate main term by a fixed multiple of \(E_\star|D|^4=O(1)\), since the reciprocal prime mass on the band is bounded. Aggregate errors and strict-tail transfer preserve this bound. The mean is bounded, so the centered fourth moments are bounded as well.

For CUE, let \(f_N(\theta)=-\sum_{aN<k\le bN}\cos(k\theta)/k\). Its supremum is bounded, and the variance of its DPP linear statistic is bounded by the covariance estimate. For a bounded real multiplier \(f\) and a projection DPP, the fourth cumulant satisfies \(|\kappa_4|\le C\|f\|_\infty^2\operatorname{Var}\) for an absolute \(C\). To verify this, expand the log determinant through order four. Each term is a scalar times \(\operatorname{Tr}(P f^{j_1}P f^{j_2}\cdots P f^{j_r})\) with \(j_1+\cdots+j_r=4\). Insert \(I=P+(I-P)\) between each pair of adjacent multipliers inside the powers. The all-\(P\) word cancels by the degree-four coefficient of \(\log(1+(e^z-1))=z\). Every other cyclic word contains two cross blocks \(Pf(I-P)\) and \((I-P)fP\). Bounding those in Hilbert–Schmidt norm and the other factors in operator norm costs at most \(\|f\|_\infty^2\|Pf(I-P)\|_{\mathrm{HS}}^2\), and the latter squared norm is exactly the variance. The number of words and coefficients is finite. Thus \(\kappa_4+3\operatorname{Var}^2\), the centered fourth moment, is uniformly bounded. A deterministic root contribution does not affect this estimate.

On both sides every weak subsequential limit has the limiting first three moments by bounded fourth moments and uniform integrability. In the cubic range the centered third moment is negative, whereas a Gaussian has zero centered third moment. This rules out Gaussian weak subsequential limits on these fixed bands, including after standardization by the limiting nonzero variance. The first three moment matches alone give no identification of the remaining limit laws.
