# Finite prefix jets on the triangular lattice

17 November 2026. This note uses the exact Taylor-to-moment map in the [prefix inverse theorem](adversarial_reviews/director_prefix_inverse_round8.md). The variable \(x\) here is a multiplicity node \(\mu_m=m(m-1)\), \(m\ge2\), and \(a_m=\nu\{\mu_m\}=\mu_m^2W_m\). The limiting coefficients of \(b,\ldots,b^{n+1}\) give \(M_j=\int x^j\,d\nu(x)\) for \(0\le j\le n\) by an invertible triangular linear map. The independent scalar \(C(0)\) supplies \(W_1=C(0)-\sum_{m\ge2}a_m/(m-1)^2\). All statements about the finite jet use these true limiting data.

## Discrete moment feasibility and exact recovery

Infusino, Kuna, Lebowitz and Speer classify interior and boundary truncated moment data in Theorem 4.4 and Remark 4.5. Lemma 4.2 gives the support and uniqueness inference when a nonnegative polynomial has zero integral. Section 8 extends the arguments from \(\mathbb N_0\) to arbitrary lower-bounded infinite discrete subsets of the real line, so normalize by \(M_0>0\) and replace \(x\) by \(x-2\). If \(M_0=0\), positivity already gives \(\nu=0\). Their polynomials have adjacent lattice roots in pairs and a minimum-node factor when the degree is odd. This includes the contiguous-root polynomial \(P_M(x)=\prod_{m=2}^M(x-\mu_m)\) in the [earlier audit](latest62_inverse_adjacent_fullreads.md). Equation (8.7) in the pinned v2 preprint prints \(l(t_1)\) twice. The preceding support set and the analogue of (6.12) indicate that the third factor should use \(l(t_2)\). The sign argument for \(P_M\) uses neither that formula nor a floating-point rank. [Pinned source, §8 and pp. 15–17](https://arxiv.org/pdf/1504.02989v2)

Here is a direct geometric consequence. For fixed \(n\), the convex hull of \(v_n(\mu_m)=(\mu_m,\ldots,\mu_m^n)\) has full dimension by Vandermonde. Positive measures with finite moments through degree \(n\) give exactly points of this convex hull, by the finite-dimensional positive cubature theorem of Bayer–Teichmann applied on the same support set. For a realizable boundary point, a supporting hyperplane gives a nonzero polynomial \(p\) of degree at most \(n\), with \(p\ge0\) on the lattice and \(\int p\,d\nu=0\). Every representing measure is supported on the at most \(n\) lattice zeros of \(p\), and the masses are unique by Vandermonde. Conversely, a realizable interior point \(y\) can be represented with positive mass at any chosen node \(x_*\), however large: for small \(\epsilon>0\), the point \((y-\epsilon v_n(x_*))/(1-\epsilon)\) still belongs to the convex hull. Its finite representation plus \(\epsilon\delta_{x_*}\) represents \(y\). A realizable jet coming from an infinite support is therefore interior. If the original profile also has \(W_1>0\), take a sufficiently small convex mixture of the original \(\nu\) with the new same-jet measure to preserve \(\sum_{m\ge2}a_m/(m-1)^2\le C(0)\), then adjust \(W_1\) to fix \(C(0)\). The augmented data admit the exact characterization below, including the case \(W_1=0\). This conclusion concerns competitors for the finite prefix data, not possible assignments of zeros of the same zeta function. [Bayer–Teichmann, Corollary 2 and Theorem 2](https://arxiv.org/pdf/math/0502473)

## Exact classification with the constant term included

The independent finite-moment review supplied a zero-slack counterexample to transferring the unaugmented interior argument directly. Take \(M_0=1\), \(M_1=6\) and \(C(0)=1/4\). The mean 6 is an interior one-moment datum. Let \(g(x)=4/(\sqrt{1+4x}-1)^2\), so \(g(\mu_m)=1/(m-1)^2\). The function is strictly convex on \((0,\infty)\), as shown below. Jensen gives \(\int g\,d\nu\ge g(6)=1/4\) with equality only at \(\nu=\delta_6\). The fixed constant term and \(W_1\ge0\) therefore force \(\nu=\delta_6\) and \(W_1=0\). [Independent finite-moment review](adversarial_reviews/finite_moment63_review.md)

The augmented characterization below is independently derived here and awaits external checking. For \(M_0>0\), include the normalized constant \(c=C(0)/M_0\) in the data \(y=(M_1/M_0,\ldots,M_n/M_0,c)\). Exactly the following set is feasible:
\[
 {\cal A}_n=\operatorname{conv}
 \{(v_n(\mu_m),g(\mu_m)):m\ge2\}
       +\{(0,\ldots,0,t):t\ge0\}.
\]
Apply Bayer–Teichmann Corollary 2 with test functions \(1,x,\ldots,x^n,g(x)\) to replace the multiple part by at most \(n+2\) atoms on its own support. The upward coordinate \(t\) represents \(W_1/M_0\). The converse follows by using the convex weights and the nonnegative slack. The projection to the first \(n\) coordinates has full dimension by Vandermonde. Adding the vertical direction gives full dimension in \(\mathbb R^{n+1}\). [Bayer–Teichmann, Corollary 2](https://arxiv.org/pdf/math/0502473v2)

For an interior \(y\), fix a node \(x_*\) and put \(u_*=(v_n(x_*),g(x_*))\). For sufficiently small \(\epsilon>0\), \((y-\epsilon u_*)/(1-\epsilon)\) lies in \({\cal A}_n\). Add the mass \(\epsilon M_0\) at \(x_*\) to that finite representation scaled by \(1-\epsilon\), including the scaled simple weight. This produces a finite-support competitor with the same entire truncated jet and \(C(0)\), including zero-slack inputs that happen to be interior in the augmented set.

For a realizable boundary \(y\), orient a supporting affine functional to be nonnegative on \({\cal A}_n\) and zero at \(y\). Such a hyperplane exists since the relative interior of a convex set equals that of its closure. The vertical ray gives a nonnegative coefficient \(\beta\) for the last coordinate. On lattice vectors the functional is \(p(x)+\beta g(x)\) with \(\deg p\le n\). Its integral against \(\nu/M_0\), plus \(\beta W_1/M_0\), vanishes. Both quantities are nonnegative, so the multiple support lies in the lattice zeros of \(p+\beta g\) and \(\beta W_1=0\). If \(\beta=0\), \(p\) is nonzero and has at most \(n\) roots. If \(\beta>0\), use
\[
 g(x)=x^{-1}+\tfrac12 x^{-2}
       +\tfrac12(x^{-2}+4x^{-1})(1+4x)^{-1/2}.
\]
The inverse powers and the shifted inverse square root have alternating-sign derivatives. The product rule and the first \(x^{-1}\) term give \((-1)^k g^{(k)}(x)>0\) for every \(k\ge0\) and \(x>0\). Hence the \((n+1)\)-st derivative of \(p+\beta g\) is nowhere zero on \((0,\infty)\). Rolle's theorem bounds its number of distinct zeros there by \(n+1\). Vandermonde on the permitted lattice zeros determines every atom from \(M_0,\ldots,M_n\), and \(C(0)\) determines \(W_1\). In particular, feasible augmented boundary data are unique finite profiles, whereas feasible augmented interior data permit an arbitrary occupied lattice node.

The argument also identifies the affine support certificates a computation would have to find or bound. The compactness and interval checks needed for a numerical classification of \({\cal A}_n\) have not been established here. This is a convex and interpolation consequence of the exact prefix map and positive cubature, with no literature priority claim.

## Tail mass and one-sided reconstruction

Write \(R_M=\int P_M\,d\nu\) and \(D_M=P_M(\mu_{M+1})=(M-1)!(2M)!/(M+1)!\). The inequalities \(P_M\ge D_M\,1_{\{x\ge\mu_{M+1}\}}\) on the lattice and \(P_M\ge0\) on the lattice show that \(0\le\sum_{m>M}a_m\le R_M/D_M\). Measures whose support is contained in \(\{\mu_2,\ldots,\mu_{M+1}\}\) give equality. This shows global sharpness of the single-polynomial bound. Other polynomials may give a tighter bound for a particular vector of moments. The indicator majorant is an instance of the generalized-moment dual in Bertsimas–Popescu §2. [Bertsimas–Popescu, (2.2) and Theorems 2.1–2.2](https://doi.org/10.1137/S1052623401399903)

For \(2\le m\le M\), define \(L_m(x)=\prod_{2\le j\le M,\, j\ne m}(x-\mu_j)/P_M'(\mu_m)\) and \(T_m=\int L_m\,d\nu\). On all tail nodes, \(L_m(x)\) has sign \(\sigma_m=(-1)^{M-m}\), and
\[
 0\le \sigma_m(T_m-a_m)\le \frac{R_M}{(\mu_{M+1}-\mu_m)|P_M'(\mu_m)|}.
\]
Indeed, the polynomial is an interpolation indicator on the first \(M-1\) nodes, and on the tail it is \(P_M(x)/[(x-\mu_m)P_M'(\mu_m)]\). Certified intervals for \(T_m,R_M\) yield an interval for \(W_m=a_m/\mu_m^2\) by intersection with the positive axis. The residual multiple contribution to \(C(0)\) is bounded above by \(R_M/(M^2D_M)\). Together with the individual intervals this gives an interval for \(W_1\). Each polynomial integral can be formed as a single linear functional of the Taylor coefficients using the inverse triangular map. A coefficient error interval must be propagated through that functional, including cancellation.

The exact factorial form on the tail is
\[
 \frac{P_M(\mu_m)}{D_M}=\frac{M(M+1)}{m(m-1)}{m+M-1\choose 2M}\qquad(m\ge M+1).
\]
It follows from the two factors \(\mu_m-\mu_j=(m-j)(m+j-1)\). If \(a_m\le Bq^m\) with \(0<q<1\), the binomial series gives the explicit estimate
\[
\frac{R_M}{D_M}\le\frac{Bq^{M+1}}{(1-q)^{2M+1}}.
\]
For this certificate the right side tends to zero when \(q<(3-\sqrt{5})/2\). The threshold is sharp over geometric profiles \(a_m=q^m\): factor out \(q^{M+1}/(1-q)^{2M+1}\) and identify the remaining sum as the expectation of \(M(M+1)/[(M+1+J)(M+J)]\), where \(J\) is negative binomial with mean \((2M+1)q/(1-q)\). On \(J\le2\mathbb E J\), which has probability at least \(1/2\), this fraction is bounded below by a positive constant depending only on \(q\). For the actual zeta profile under RH, the previously proved tail estimate yields such a bound for every fixed \(q\in(0,1)\), hence \(R_M/D_M\) decreases faster than any fixed exponential rate. This last statement assumes exact moments and provides no bound on the amount of arithmetic computation needed for a certified enclosure.

## Arithmetic input needed

A positive finite tail enclosure measures the total weighted mass beyond the cutoff. The lower bound for a single zeta zero's contribution decreases with its height, so that enclosure alone cannot prove a global maximum multiplicity. A finite-height exclusion would require an enclosure below the weight of any possible zero in the height window being excluded. A global arithmetic application needs rigorously enclosed coefficients of the limiting cost, or a bound for the limiting cost under a quantified order of limits. The finite-\(N\) approximants are staircase functions. Their pointwise derivatives give no derivative data for \(C\). To see what an arithmetically supplied convergence rate could yield, for \(F_N\) known within \(\delta_N\) of \(C\) at \(0,h\), and \(B\ge\sup_{0\le t\le h}|C''(t)|\), the forward difference has error at most \(2\delta_N/h+Bh/2\) for \(C'(0)\). Both \(\delta_N/h\to0\) and \(h\to0\) must be justified. An endpoint bound near \(b=1\) in the [prefix inverse theorem](adversarial_reviews/director_prefix_inverse_round8.md) is an alternative arithmetic target.
