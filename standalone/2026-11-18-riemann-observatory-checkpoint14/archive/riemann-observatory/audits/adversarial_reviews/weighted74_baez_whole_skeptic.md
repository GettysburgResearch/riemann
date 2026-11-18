# Whole-work audit of Báez-Duarte’s original strengthening

The archived work is **PAPER-E014**, Luis Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, *Rendiconti Lincei*, series 9, **14**(1) (2003), 5–11, and arXiv math/0202141v1–v2. I read the complete journal text and compared both seven-page preprints. Published Theorem 1, its corollary, and constructive Theorem 2 survive the checks below. The constructive proof uses the genuinely uniform shrinking-shift estimate already accepted as a scoped reconstruction. [PAPER-E014](../../papers/PAPER-E014.md) · [Publisher record](https://www.bdim.eu/item?id=RLIN_2003_9_14_1_5_0) · [arXiv history](https://arxiv.org/abs/math/0202141)

## Source identity, version evidence and earlier decisions

The journal scan identifies the note as presented by E. Bombieri, received on 21 August 2002, and received in final form on 6 September 2002. It contains two archive leaves plus all seven printed pp. 5–11. The HTTP publisher PDF worked, while its HTTPS equivalent returned 503. The journal PDF SHA-256 is 9bfb3943ec8d7690d452b8ac7d50fb10614b4e814738dc091390e6ab4994f0b8. The v1 PDF, submitted 15 February 2002 and dated 13 February in the text, hashes to a0b876c54be79af5d1af53d181c6cd6fc94d94cc35d32b22697a97b15c99f589. The v2 PDF from 18 February has the existing archive pin 3ce4aff466443c71094affc1f8b6f5f0dd36cb4377dc5d2ceddbd2537c1d1819. The arXiv history reports three typos corrected and a reference added in v2. Direct comparison confirms \(a>1\) to \(a\ge1\) in the abstract and the added Vasyunin reference. Both preprints still show identical gamma arguments in the ratio on p. 3. The journal p. 7 has the correct minus sign in the denominator. The journal extends Lemma 2 to \(\epsilon_0<1/2\) and adds constructive §3 and its acknowledgements. [Journal PDF](http://www.bdim.eu/item?fmt=pdf&id=RLIN_2003_9_14_1_5_0) · [v1](https://arxiv.org/pdf/math/0202141v1) · [v2](https://arxiv.org/pdf/math/0202141v2)

**PAPER-E001**, math/0205003v1 submitted 1 May 2002, is the separate *criterion …, 2*. It describes the earlier result and includes the quantitative construction as Proposition 3.1. Its audit discussed the normalization, integrability range, tail exponent and RH-dependent identification. Those issues are checked here against the actual E014 journal and are not new findings about the sequel. The prior director decision accepted **THM-E-D202–D204** for the scoped finite-height reciprocal bound, uniform shrinking-shift Perron estimate and rate. Recovery of the journal closes that decision’s published-version access limitation. Targeted searches by exact title and correction/erratum terms did not locate a separate author erratum. No canonical record or theorem ID was changed. [PAPER-E001](../../papers/PAPER-E001.md) · [Prior sequel audit](../baez_duarte_deep_round2.md) · [Scoped director decision](director_round3_adjudication.md)

## §1, continuous and integer closures

Work in \(H=L^2((0,\infty),dx)\), with \(\rho_a(x)=\{1/(ax)\}\), \(\chi=\mathbf1_{(0,1]}\), \(B=\operatorname{span}\{\rho_a:1\le a\in\mathbb R\}\) and \(B_{\rm nat}=\operatorname{span}\{\rho_n:n\ge1,\ n\in\mathbb Z\}\). Theorem 1 means RH iff \(\chi\in\overline{B_{\rm nat}}^{\,H}\). Each generator is square-integrable by boundedness near zero and the exact tail \(1/(ax)\) for \(x>1/a\). The endpoint value of \(\chi\) makes the pointwise Möbius identity exact and has no effect on the Hilbert space. The journal cites [4] for the full-half-axis unconstrained variant of the original Nyman–Beurling criterion on \((0,1)\).

A direct check of strictness uses \(y=1/x\) on \(1<y<2\), with measure \(dy/y^2\). All integer generators restrict to affine functions of \(y\), a closed two-dimensional subspace. Each real \(a\in(1,2)\) gives \(y/a-\mathbf1_{\{y\ge a\}}\) with a distinct jump. Distinct such generators are independent modulo the affine subspace, so the quotient of the real by the integer norm closure is infinite-dimensional. Using \(a>1\) for the continuous family in the abstract is equivalent after closure, since \(\rho_a\to\rho_1\) in \(H\) as \(a\downarrow1\) by dominated convergence. The integer \(1\) cannot be omitted. For \(n\ge2\) all generators restrict to scalar multiples of \(y\) on \((1,2)\), which cannot approximate the constant value of \(\chi\) there.

The historical statements concern \(F_n=\sum_{a\le n}\mu(a)\rho_a\). The source credits restricted \(L^1(0,1)\) and a.e. convergence to the 1993 paper [1], and cites [2,3] for nonconvergence in \(H\). The latter is explicit in [3]’s precursor math/0011254v1, Prop. 4.6. It applies the earlier invariant unitary operator to \(F_n\), giving \(M(n)-1\) on \((0,1/n)\). Norm convergence would force \(n^{-1}|M(n)-1|^2\to0\), contrary to the zero-based \(M(n)\ne o(\sqrt n)\) consequence cited there. The lower scale (1.2) is credited to Báez-Duarte–Balazard–Landreau–Saias, *Notes …, 3*, and the strengthened constant to Burnol. Burnol math/0103058, Thms. 1.2–1.3, explicitly distinguishes the distinct-zero and multiplicity-sensitive bounds on the continuous real-dilation distance with parameter \(\lambda=1/N\). For large \(N\) these supply the stated \(C/\sqrt{\log N}\) scale. A globally uniform interpretation would fail near \(N=1\), since \(F=\rho_N\) remains at bounded distance from \(\chi\). This endpoint was already noted in the sequel audit. [1993 article](https://doi.org/10.1006/aima.1993.1038) · [Earlier divergence](https://arxiv.org/pdf/math/0011254) · [Notes 3](https://doi.org/10.1006/aima.1999.1861) · [Burnol lower bound](https://arxiv.org/pdf/math/0103058)


The historical restricted convergence can also be checked from the classical quantitative prime number theorem for \(M(n)\). It gives \(c_n=\sum_{a\le n}\mu(a)/a=o(1/\log n)\) by partial summation, since the infinite sum is zero. For \(1\le y\le n\), \(F_n(1/y)+1=c_n y\), whose \(dy/y^2\) integral of the absolute value is \(|c_n|\log n=o(1)\). For \(y>Rn\), the bound \(|F_n|\le n\) costs \(O(1/R)\). For \(n<y\le Rn\), discard \(a\le\eta n\) at cost \(O(\eta n)\) pointwise. The weight \(a\mapsto\{y/a\}\) on \([\eta n,n]\) has total variation \(O(R/\eta)\), so partial summation and \(M(u)=o(u)\) give \(o(n)\) for the remaining terms uniformly at fixed \(R,\eta\). Integrating, then taking \(R\) large and \(\eta\) small, proves the \(L^1\) statement. Pointwise convergence follows from the finite-floor representation and \(c_n\to0\). This verifies the historical introductory implication without claiming a complete reading of the 1993 antecedent.

## §2.1, the two lemmas

**Lemma 1, p. 6.** The exact source is Balazard–Saias, *Notes sur la fonction ζ de Riemann, 1*, *Adv. Math.* **139** (1998), 310–321, Lemme 2 on pp. 315–316. The relevant preceding Lemme 1 gives a fixed-gap subpower bound for reciprocal zeta. This is **PAPER-E007**, separate from the later Expo. Math. paper in the archive. The estimate is
\[
 \sum_{a\le n}\mu(a)a^{-s}
 =\frac1{\zeta(s)}+O_{\alpha,\delta,\eta}\!\left(n^{-\delta/3}(1+|\Im s|)^\eta\right)
\]
for \(n\ge2\), \(1/2\le\alpha<1\), fixed \(\delta,\eta>0\), \(\alpha+\delta\le\Re s\le1\), assuming no zeros in \(\Re s>\alpha\). The reciprocal is zero at 1 by continuation. To recheck Perron, take \(X=n+1/2\), initial abscissa \(1-\Re s+1/\log X\) and height \(X^4\), then shift to \(\Re w=\alpha-\Re s+\delta/2\le-\delta/2\). Its only crossed residue is \(1/\zeta(s)\). The reciprocal bound on the rectangle uses a freely small subpower exponent relative to \(\delta\) and \(\eta\), preserving the gain \(n^{-\delta/3}\). In the truncated Perron error, the terms indexed by \(m\asymp X\) give \(O(X^{1-\Re s}\log X/X^4)\), using \(|\log(X/m)|\gg |X-m|/X\) and the half-integer separation; the remaining terms satisfy the same bound by absolute summation on the initial line. This proves the correct endpoint convention and fixed-gap dependence. The reproduced 1998 text has degraded formula extraction and publisher-quality PDF access remained unavailable. The complete lemma is also quoted by the work under audit and corroborated by Burnol. [1998 source identity](https://doi.org/10.1006/aima.1998.1760) · [Prior primary-text retrieval and scoped reconstruction](../baez_uniform_dependency_round2.md)

**Lemma 2, pp. 6–7.** For \(s_\pm=\frac12\pm\epsilon+it\), the functional equation and conjugation give
\[
 \left|\frac{\zeta(s_-)}{\zeta(s_+)}\right|
  =\pi^{-\epsilon}
    \left|\frac{\Gamma(1/4+\epsilon/2+it/2)}
                 {\Gamma(1/4-\epsilon/2+it/2)}\right|
  \ll_{\epsilon_0}(1+|t|)^\epsilon,\qquad
 0\le\epsilon\le\epsilon_0<1/2.
\]
This uses uniform Stirling on a fixed positive gamma strip at large \(|t|\) and compactness at bounded \(|t|\). The cited Rademacher [15, (21.51)–(21.52)] provides this Stirling step. Paired zeros have equal multiplicity, so the quotient at a paired ordinate is understood by removable continuation locally in \(t\), or defined arbitrarily there for \(L^2\) purposes. No RH premise appears in this bound. The two identical gamma arguments in E014 v1/v2 would instead give \(\pi^{-\epsilon}\), missing the growth of order \(|t|^\epsilon\) at fixed \(\epsilon>0\). Journal p. 7 already prints the correct expression.

## §2.2, norm convergence

The finite shifted sum is \(f_{\epsilon,n}=\sum_{a\le n}\mu(a)a^{-\epsilon}\rho_a\). The fractional part identity yields (2.3). For each \(x>0\), the floor terms vanish when \(a>1/x\), and the remaining tail is absolutely summable for \(\epsilon>0\), giving
\[
 f_\epsilon(x)=\frac1{x\zeta(1+\epsilon)}
   -\sum_{a\le1/x}\mu(a)a^{-\epsilon}\left\lfloor\frac1{ax}\right\rfloor .
\]
As \(\epsilon\downarrow0\), the first term vanishes and the finite floor sum tends to \(\chi\) by grouping \(\sum_{k\le1/x}\sum_{a\mid k}\mu(a)\). This is the unconditional pointwise statement (2.5).

For the unnormalized transform in (2.6), substitution \(x=e^u\) gives ordinary Fourier Plancherel and target measure \(dt/(2\pi)\), with inverse obtained by the same unitary substitution. Journal p. 7 instead prints \((2\pi)^{-1/2}dt\). The transform of \(\chi\) is \(1/(\frac12+it)\) and its squared ordinary integral is \(2\pi\), an exact normalization check. Journal p. 10 uses the correct \(2\pi\) norm-square identity. Also, for \(0<\Re s<1\),
\[
 \int_0^\infty \rho_a(x)x^{s-1}dx=-a^{-s}\frac{\zeta(s)}s .
\]
After the dilation changes of variable the integral is \(\int_0^\infty\{u\}u^{-s-1}du\), which converges absolutely. Obtain the zeta formula by integrating against \(\lfloor u\rfloor\) on \([1,\infty)\) initially for \(\Re s>1\), continuing the bounded fractional-part integral there and adding its explicit \((0,1)\) portion. This checks the Titchmarsh (2.1.5) input.

Use \(\nu\) for the Mellin weight, distinguishing it from the unweighted coefficient shift. For \(X_\nu=x^{-\nu}\) and \(0<\nu<1/2\), termwise finite transformation gives
\[
 \mathcal M(X_\nu f_{2\nu,n})(t)
 =-\frac{\zeta(\frac12-\nu+it)}{\frac12-\nu+it}
       \sum_{a\le n}\mu(a)a^{-1/2-\nu-it}.
\]
This weighted domain has a genuine endpoint. At \(\nu=1/2\) even \(x^{-1/2}\rho_1\notin H\), by the divergent integral \(\int_1^\infty\{u\}^2du/u\) over the second halves of the unit intervals. Under RH, Littlewood’s convergence theorem, cited as Titchmarsh 14.25(A), or Lemma 1, gives the pointwise limit
\[
 G_\nu(t)=-\frac{\zeta(\frac12-\nu+it)}
               {(\frac12-\nu+it)\zeta(\frac12+\nu+it)} .
\]
Keeping the free exponent \(\eta\) distinct from \(\nu\), Lemma 1 gives Möbius error \(O_{\nu,\eta}(n^{-\nu/3}(1+|t|)^\eta)\). The RH consequence of Lindelöf on the right together with the functional equation gives \(|\zeta(\frac12-\nu+it)|\ll_{\nu,\eta}(1+|t|)^{\nu+\eta}\). Thus the pointwise transform difference is bounded by \(C_{\nu,\eta}n^{-\nu/3}(1+|t|)^{-1+\nu+2\eta}\), an \(L^2\) bound for \(0<\eta<(\frac12-\nu)/2\), and the limit kernel is itself in \(L^2\) by Lemma 2. Journal p. 8, unlike E014 v2 p. 5, overextends the displayed majorant \((1+|t|)^{-1+2\nu}\) to \(\nu_0<1/2\). Its square behaves like \(1/|t|\) at \(\nu=1/4\). The restriction \(\nu<1/4\) suffices for Theorem 1, and the free exponent proves the full fixed weighted range without claiming a uniform constant as \(\nu\downarrow0\).

An a.e.-convergent subsequence from the weighted norm limit identifies its inverse Mellin transform with the already known pointwise \(X_\nu f_{2\nu}\). On \((0,1)\), unweighting multiplies by the contraction \(x^\nu\). On \(x>1\), \(f_{2\nu,n}(x)=x^{-1}\sum_{a\le n}\mu(a)a^{-1-2\nu}\); journal (2.9) still has \(1+\nu\) where \(1+2\nu\) is needed. Absolute convergence of that scalar coefficient gives the remaining unweighted norm convergence. This places \(f_{2\nu}\) in \(\overline B_{\rm nat}\).

Now send \(\nu\downarrow0\) after the fixed-\(\nu\) limit in \(n\). Lemma 2 gives the square-integrable envelope \(C(1+|t|)^{-1+\nu_0}\) for the analytic kernels \(G_\nu\). Off critical-line zeros, \(G_\nu\to-1/(\frac12+it)\). At a critical zero of order \(m\) the ratio of zeta factors tends to \((-1)^m\), on a discrete irrelevant set. Hence the analytic-kernel limit is unconditional. Identifying it with \(X_\nu f_{2\nu}\) still uses the RH-dependent first limit. On \((0,1)\),
\(f_{2\nu}+\chi=x^\nu(X_\nu f_{2\nu}+\chi)+(1-x^\nu)\chi\), which tends to zero in norm. On \(x>1\) the coefficient \(1/\zeta(1+2\nu)\) tends to zero. Closedness yields the desired integer approximation.

The other implication can be verified directly. At a nontrivial zero \(\rho\) with \(1/2<\Re\rho<1\), the bounded \(H\)-functional
\[
 \Lambda_\rho(F)=\int_0^1 F(x)x^{\rho-1}dx+
              \frac1{1-\rho}\int_1^\infty F(x)\frac{dx}{x}
\]
equals Mellin evaluation on the generators by their exact tails. It vanishes on their norm closure, while \(\Lambda_\rho(\chi)=1/\rho\ne0\). The functional equation pairs the two off-line sides. This establishes the converse without the original Hardy-space proof, in accord with the author’s p. 9 remark.

## Corollary and retained hypothesis

The printed corollary concerns \(H\)-convergence of the original shifted partial sums for all sufficiently small fixed \(\epsilon>0\). A sequence of such shifts tending to zero is enough. If \(f_\epsilon\in H\), its restriction to \((0,1)\) has Mellin transform holomorphic on \(\Re s>1/2\) by Cauchy–Schwarz, also locally uniformly after differentiation. Initially for \(\Re s>1\), the floor decomposition and \(\int_0^1\lfloor1/u\rfloor u^{s-1}du=\zeta(s)/s\) give
\[
 \int_0^1 f_\epsilon(x)x^{s-1}dx
 =\frac1{\zeta(1+\epsilon)(s-1)}
   -\frac{\zeta(s)}{s\zeta(s+\epsilon)} .
\]
The floor integral follows by summing indicator steps and all series exchanges are absolute in that region. If an off-line zero \(\rho\) has \(\Re\rho>1/2\), then for every sufficiently small \(\epsilon>0\), \(s=\rho-\epsilon\) lies in the holomorphic region, is different from 1, and is not a numerator zero by isolation of zeros. The right side would have a pole. Consequently in this hypothetical case \(f_\epsilon\notin H\) for every sufficiently small \(\epsilon\). Any norm limit of \(f_{\epsilon,n}\) must equal its pointwise limit a.e., giving the corollary. The same obstruction limits the free-standing interpretation of “unconditionally” in §1 and at the second limit on p. 9. The inverse Mellin family of the analytic kernels is unconditional. Its identification with the original weighted pointwise sums would itself imply RH over a sequence of small shifts. Burnol analyzes this distinction in the contemporary response. [Burnol math/0202166, §§3–4](https://arxiv.org/pdf/math/0202166) · [Burnol journal record](https://pubmed.ncbi.nlm.nih.gov/15916175/)

## §3, the constructive approximation rate

Theorem 2 asserts under RH that for some constant \(c>0\), the approximant \(-f_{\epsilon_n,n}\) with \(\epsilon_n=c/\log\log n\) has error \(O((\log\log n)^{-1/3})\) in \(H\). This is asymptotic, with the range \(\epsilon_n\le1/2\) starting only once \(\log\log n\ge2c\). On \(s=\frac12+it\), put \(M_n(w)=\sum_{a\le n}\mu(a)a^{-w}\). The p. 10 Plancherel split is an algebraic inequality on the finite polynomial and bounds the squared norm by a constant times
\[
 I_{n,\epsilon}=\int_{\mathbb R}|\zeta(s)|^2
     |M_n(s+\epsilon)-1/\zeta(s+\epsilon)|^2\,dt/|s|^2,\qquad
 J_\epsilon=\int_{\mathbb R}|\zeta(s)/\zeta(s+\epsilon)-1|^2\,dt/|s|^2 .
\]

For \(J_\epsilon\), [8] is Burnol math/0202166, Theorem 1.3 and Lemma 3.1, giving under RH \(|\zeta(s)/\zeta(s+\epsilon)|\ll|s|^{\epsilon/2}\) uniformly for \(0<\epsilon\le1/2\). At \(s+\epsilon=1\) the reciprocal is zero. One can also derive the estimate from the order-one centered Hadamard product for \(\xi(1/2+z)\). Under RH its paired \(\pm i\gamma\) factors have moduli nondecreasing from \(it\) to \(\epsilon+it\), since \(|(\epsilon+it)^2+\gamma^2|^2=(\gamma^2-t^2)^2+2\epsilon^2(\gamma^2+t^2)+\epsilon^4\). The centered function is even, so the paired product has no residual linear exponential. Its polynomial and gamma factors give the claimed bound by Stirling and compactness. Away from the union \(|t-\gamma|\le\delta\) with \(\delta\le1\), the standard local logarithmic derivative formula in \(1/2\le\sigma\le3/4\) and the unit-window zero count bound the logarithmic change by \(C(\epsilon/\delta)\log(2+|t|)\). Exponentiation for small \(\epsilon/\delta\) gives a ratio defect \(O((\epsilon/\delta)(1+|t|)^{1/4})\); use \(|e^w-1|\le |w|e^{|w|}\) and split the quarter power between the exponential and logarithmic factors. Its squared weighted integral is \(O(\epsilon^2/\delta^2)\). On the union the Burnol bound gives \(O((1+|t|)^{-3/2})\) after weighting, so the integral is \(O(\delta\sum_\gamma(1+|\gamma|)^{-3/2})=O(\delta)\). Take \(\delta=\epsilon^{2/3}\). This only requires small \(\epsilon\), ensuring the horizontal segment lies in the stated strip.

For \(I_{n,\epsilon}\) the printed uniform estimate is stronger than Lemma 1 with its fixed-gap constants. I independently checked the already accepted quantitative reconstruction, using a half-integer Perron cutoff. Titchmarsh–Heath-Brown, 2nd ed., book pp. 354–355, (14.14.1)–(14.14.5) gives the necessary RH bounds. The equality-line statement (14.14.4) is not by itself a half-plane estimate. The adjacent interval is supplied by (14.14.5) and the remaining bounded right strip by fixed-strip Phragmén–Lindelöf for a branch of \(\log\zeta\), with absolute convergence at \(\sigma=2\). A sufficient consequence under RH is
\[
 \sup_{\substack{|v|\le V\\1/2+A_0/\log\log V\le\sigma\le2}}
     |1/\zeta(\sigma+iv)|\le \exp(K\log V/\log\log V)
\]
for fixed sufficiently large \(A_0\) and \(V\). For \(|v|\ge\exp(\sqrt{\log V})\), \(\log\log|v|\ge\frac12\log\log V\), allowing use of the actual-height theorem with \(A_0\ge2A\). At smaller heights let \(\lambda=A_0/\log\log V\) and apply Borel–Carathéodory to the holomorphic logarithm of the pole-removed \((s-1)\zeta(s)\) in disks centered at \(2+iv\) with outer radius \(3/2-\lambda/2\) and inner radius \(3/2-\lambda\). Fixed-strip polynomial growth and the Euler-series branch at the center give \(O(\lambda^{-1}\log(|v|+3))=O((\log\log V)\sqrt{\log V})\), absorbed by the desired estimate. This specifically addresses the low-height regime instead of substituting \(V\) for the actual \(v\).

Now use \(X=n+1/2\), height \(X^4\), and move the Perron abscissa to \(-\epsilon/2\) in the shift variable. The cutoff yields exactly the first \(n\) terms. The reciprocal argument stays to the right of \(1/2+\epsilon/2\), so the previous bound with \(V=|t|+X^4+3\) applies if \(c\ge2A_0\). Its exponential loss is \(\exp(K_1\log n/\log\log n+K_2\mathcal L(t))\), where \(\mathcal L(t)=\log(|t|+3)/\log\log(|t|+3)\). The left integral costs \(X^{-\epsilon/2}\log X\) times this factor. The horizontal integrals cost at most \(X^{-7/2}\) times the same factor. The half-integer truncation bound from Lemma 1 applies. Take \(c\) large enough to pay \(K_1\log n/\log\log n+\log\log X\) out of the \(\epsilon\log n/6\) margin. This proves the required uniform \(O(n^{-\epsilon/3}e^{K_2\mathcal L(t)})\) error. It is an endpoint check of the previously accepted scoped reconstruction rather than an additional rate theorem.

The RH bound (14.14.1) on the critical line is \(e^{O(\mathcal L(t))}\). The remaining \(e^{O(\mathcal L(t))}/|s|^2\) is integrable since \(\mathcal L(t)=o(\log(|t|+3))\). Hence \(I_{n,\epsilon}=O(n^{-2\epsilon/3})\) uniformly, and \(J_\epsilon=O(\epsilon^{2/3})\). Substitution of \(c/\log\log n\) followed by taking a square root gives the stated norm error. The journal credits the theorem’s statement and proof to M. Balazard, the independent shift suggestions to Balazard and E. Bombieri, and the ratio approach to Burnol. The rate concerns this specified sequence under RH, with no numerical threshold or optimality claim. [Titchmarsh source and prior reconstruction](../baez_uniform_dependency_round2.md) · [Independent scoped review](baez_uniform_skeptic_round2.md) · [Director decision](director_round3_adjudication.md)

The strongest stress tests isolate version-level presentation issues, domain endpoints, and the distinction between fixed and shrinking shifts. They leave the published mathematical scope intact with the indicated reconstructions. The archival canonical records and earlier theorem pins are unchanged.
