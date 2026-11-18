# The logarithmic endpoint fails for absolute zero sampling

18 November 2026. A real smooth test can have finite critical logarithmic Mellin strip norm at \(p=3\) while its absolute sum over the actual zeta zeros diverges. The director independently checked the weighted synthesis, zero-count lower bound and probability argument, and read two independent reconstructions and a third adjudication. The proof is unconditional. It sharpens the earlier sufficient \(p>3\) theorem **for universal absolute sampling in this scale**. It does not settle signed symmetric height convergence at \(p=3\), characterize every valid explicit-formula test, or establish publication novelty.

Independent proofs: [construction](weighted138_critical_endpoint_campaign.md), [adversarial reconstruction](analytic139_critical_endpoint_adversarial.md), [third adjudication](geometry141_critical_endpoint_adjudication.md). The source-specific background and the sufficient theorem are in the [Mellin adjudication](director_mellin_explicit_formula_round15.md).

The [primary-source comparison](prime146_mellin_trace_prior_art.md) derives the same sharp threshold on the unrestricted weighted holomorphic strip space from Luecking's 1986 embedding criterion. The construction here imposes the additional smoothness, reality and physical decay requirements explicitly. Priority for this constrained version is unresolved.

## Exact assertion

There is a real \(C^\infty\) function \(f\) on \((0,\infty)\), vanishing near zero and one and satisfying \(f(x)=O(x^{-4})\) at infinity, such that its Mellin transform \(h\) satisfies

\[
\int_{-1/4}^{5/4}\int_{\mathbb R}
\sqrt{1+t^2}\,[\log(e+|t|)]^3|h(\beta+it)|^2\,dt\,d\beta<\infty,
\qquad \sum_\rho|h(\rho)|=\infty.
\]

The zeros are the nontrivial zeta zeros counted with multiplicity. Since \(w_p\le w_3\) for \(p\le3\), the same example also rules out a universal absolute-sampling guarantee from these weaker weights. Its arithmetic and archimedean terms are absolutely finite by the value bounds and vanishing near one.

## Smooth finite-carrier packets

Fix a nonnegative smooth bump \(\psi\) of integral one supported in \((-1/8,1/8)\). Choose disjoint integer shell ranges \([L_j,U_j]\), with \(L_{j+1}\ge U_j+3\), all starting sufficiently high, and

\[
S_j=\sum_{r=L_j}^{U_j}\frac1r\ge e^{4j},\qquad
\lambda_j=e^{j/2}/S_j,\qquad
\mathcal C_j=\mathbb Z\cap[2^{L_j},2^{U_j+1}].
\]

Each range is finite; harmonic divergence permits any prescribed lower bound on \(S_j\), however large its starting point. For signs \(\varepsilon_{j,n}\in\{-1,1\}\), set

\[
F(u)=\sum_j\psi(u-j)\sum_{n\in\mathcal C_j}
\varepsilon_{j,n}\frac{\lambda_j\cos(nu)}{n(\log n)^2},\qquad
f(x)=x^{-1/2}F(\log x).
\]

The physical supports are disjoint and locally finite. Every packet has finitely many carriers, so every sign choice gives a smooth function. Its packet value is \(O(\lambda_j)\), and \(\lambda_j\le e^{-7j/2}\), proving the stated decay and absolute Mellin integrability on the closed strip. No global bound on the derivatives is assumed.

Write \(J_\beta(v)=\int\psi(u)e^{(\beta-1/2)u}e^{ivu}du\). This is uniformly Schwartz on the strip. The moderate weight \(w_3\) and integer spacing give the synthesis bound

\[
\left\|\sum_\nu c_\nu J_\beta(t-\nu)\right\|_{L^2(w_3dt)}
\le C\left(\sum_\nu w_3(\nu)|c_\nu|^2\right)^{1/2}.
\]

To verify uniformity in the number of carriers, majorize the weighted translates by \(C_Mw_3(\nu)^{1/2}(1+|t-\nu|)^{-M}\), apply Cauchy–Schwarz with the uniformly bounded sum of these integer translates, and integrate the other factor. The translation phases have modulus one. Since

\[
\sum_{n\in\mathcal C_j}w_3(n)
\left(\frac{\lambda_j}{n(\log n)^2}\right)^2
\ll\lambda_j^2 S_j,
\]

the full strip norm of packet \(j\) is at most \(Ce^{3j/4}\lambda_j\sqrt{S_j}\le Ce^{-3j/4}\). Summing these norms proves finite endpoint norm for **every** sign choice, not merely in expectation. The weighted-space limit agrees with the integral Mellin transform.

## Actual zeros and the two probability steps

Now choose all signs independently. For a zero \(\beta+i\gamma\) in shell \((2^r,2^{r+1}]\), \(L_j\le r\le U_j\), choose an integer carrier nearest to \(\gamma\). It lies in \(\mathcal C_j\). On \(|v|\le1/2\), \(\Re J_\beta(v)\) has a positive lower bound uniform in \(0\le\beta\le1\). The other half of the same cosine samples \(J_\beta(\gamma+n)\) and is uniformly negligible at high frequency. Thus that one unsigned carrier coefficient \(b_{j,n}(\rho)\) has

\[
|b_{j,n}(\rho)|\gg e^{-j/2}\lambda_j/(2^r r^2).
\]

This is a modulus bound, not a real-part bound after ignoring a rotating phase. Other carriers can cancel it for particular signs; the randomization handles them. For a complex Rademacher sum \(Z=\sum\varepsilon_i b_i\), write \(V=\sum|b_i|^2\). Expansion gives

\[
\mathbb E|Z|^2=V,\qquad
\mathbb E|Z|^4=2V^2+\left|\sum b_i^2\right|^2-2\sum|b_i|^4\le3V^2.
\]

Paley–Zygmund therefore gives \(\mathbb E|Z|\ge c\sqrt V\), with an absolute positive constant. The carrier series at each fixed zero is absolutely convergent uniformly in signs, so the inequality passes to it. Unconditional Riemann–von Mangoldt counting supplies \(\gg2^r r\) positive zeros per sufficiently high dyadic shell. The expected absolute sum over range \(j\) is consequently at least

\[
c e^{-j/2}\lambda_j\sum_{r=L_j}^{U_j}1/r=c.
\]

Divergent expectation alone would not establish existence of an infinite value. For the finite height sum \(X_T=\sum_{0<\Im\rho\le T}|h(\rho)|\), Minkowski and the preceding pointwise comparison instead give \(\|X_T\|_2\le C\mathbb E X_T\). A second application of Paley–Zygmund gives \(\mathbb P(X_T\ge\mathbb E X_T/2)\ge c_0>0\), uniformly as its expectation tends to infinity. Monotonicity in \(T\) and then in the threshold implies \(\mathbb P(X_\infty=\infty)\ge c_0\). Some fixed sign sequence therefore gives the asserted counterexample.

One can strengthen this existence statement to probability one. A finite change of signs changes \(f\) by finitely many compact smooth carriers; their Mellin transforms are uniformly rapidly decreasing on \(0\le\beta\le1\), hence absolutely summable on the zeros. Divergence is thus invariant under finite sign changes. It is a measurable tail event on the countable sign product, and Kolmogorov's zero–one law upgrades positive probability to one. Existence alone already proves the stated obstruction.

The frequencies are impractically large, and the proof supplies an existence result rather than a list of numerically useful signs. It cannot be promoted to a failure of signed symmetric convergence. A precise next problem is whether the endpoint class with its original value bounds guarantees that weaker height limit, or whether a different sign-coherent construction defeats it. Separately, effective positivity computations should use the quantitative \(p>3\) trace tail and a certified local zero-count constant.
