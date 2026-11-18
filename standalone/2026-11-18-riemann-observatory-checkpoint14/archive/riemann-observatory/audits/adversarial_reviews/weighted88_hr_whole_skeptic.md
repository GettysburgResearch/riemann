# Whole-work reconstruction of Hughes–Rudnick’s 2002 zeta statistics

**PAPER-AN79-HR-ZETA.** I reread the complete four-page journal article of Chris Hughes and Zeév Rudnick, *Linear statistics for zeros of Riemann’s zeta function*, *C. R. Math. Acad. Sci. Paris* **335**(8) (2002), 667–670, and the complete longer arXiv v1. The Fourier-window arithmetic and ordinary CUE comparison check out. The literal whole-line weight class admits an infinite first moment. The theorem holds with Schwartz weights and, more generally, with the exact logarithmic moment qualification below. The journal does not state either decay condition. This file supports a version-specific director decision and makes no promotion. [Canonical record](../../papers/PAPER-AN79-HR-ZETA.md) · [Journal](https://archive.numdam.org/item/CRMATH_2002__335_8_667_0.pdf) · [Longer v1](https://arxiv.org/pdf/math/0208220v1)

## Controlling edition and version history

Controlling manifestation is the four-page Numdam typeset PDF at sources/analytic79_prior_art/hughes_rudnick_zeta_journal.pdf, DOI **10.1016/S1631-073X(02)02541-4**, SHA-256 **b4572e5bdbf3cf7e891a4128aeb3bb56d151f2b16d23f9e63a94b1a2d2c09139**. It records receipt 29 August 2002, acceptance 2 September 2002, presentation by Christophe Soulé, and bilingual abstracts. The independent nine-page comparison copy at sources/analytic79_prior_art/hughes_rudnick_zeta_v1.pdf has SHA-256 **2225d590d97abd13a4b973bd3d936a7b07fb45a3296739438f8ce57f657cdebd**. The arXiv record lists only v1, 28 August 2002. Journal (2), (3), (4), (5), (6) correspond respectively to preprint (3), (4), (5), (6), (7). Journal Lemma 2.2 includes the averaging claim in preprint Lemma 2.3, with the pointwise smooth estimate in preprint Lemma 2.2. Journal Proposition 2.3 corresponds to preprint Proposition 2.4. Longer Proposition 2.5 and Theorem 2.6 split out the oscillatory variance and higher moments, followed by its grouped-prime proof. The factor 2 in the surviving variance sum of preprint p. 6 is visibly correct and can be lost by extraction.

Exact-title, DOI, and arXiv-ID searches with erratum, corrigendum and correction terms located no separate author correction. The captured Crossref response has no registered update relation. This bounded search does not establish absence of circulated amendments. Near-contemporary Hughes and later Kargin restatements retain the broad wording in the passages examined. Some later authors instead use finite height intervals. Fazzari–Gerspach–Minelli use only the original oscillatory moment theorem for a bandlimited majorant, and derive a sharp-average variant separately. None of these silently revises the pinned theorem. [Numdam record](https://archive.numdam.org/articles/10.1016/S1631-073X%2802%2902541-4/) · [Submission history](https://arxiv.org/abs/math/0208220) · [Source receipts](../../sources/analytic79_prior_art/receipt.md) · [Later statements and correction-history audit](analytic85_hughes_weight_repair_review.md)

## pp. 667–668, introduction and exact theorem

Use nontrivial zeros \(\rho=1/2+i\gamma\), allowing complex \(\gamma\), counted with multiplicity. The introductory decomposition is \(N(T)=\overline N(T)+S(T)\), with
\[
 \overline N(T)=1+\pi^{-1}\Im\log\{\pi^{-iT/2}\Gamma(1/4+iT/2)\}.
\]
On the continuous theta branch, Stirling gives
\(\Im\log\{\pi^{-iT/2}\Gamma(1/4+iT/2)\}
 =\frac T2\log(T/(2\pi e))-\pi/8+O(T^{-1})\).
Thus the printed \(7/8\) term is correct. \(S\) can be read as the remainder with the same endpoint convention at an ordinate. The cited Selberg background concerns even moments of this remainder normalized by \(\sqrt{\log\log t/(2\pi^2)}\), with \(T^a\le H\le T\) and \(1/2<a\le1\). The cited Fujii result concerns increments of that remainder on scales longer than the microscopic scale. Longer v1 spells out \(h\to0\) with \(h\log T\to\infty\) and separately \(h\to\infty,\ h\ll T\). These are prior results used for motivation. The authors' proof uses neither Selberg's moment theorem nor Fujii's theorem. I checked the reference identities and roles, with no full reconstruction of the original 1946 proof or entire 1999 chapter. [Fujii chapter record](https://doi.org/10.1007/978-1-4612-1544-8_9)

For real even \(f\) with \(\widehat f\in C_c^\infty\) under the \(2\pi\) convention, put \(L=\log T\) and
\[
 N_f(\tau)=\sum_\gamma f(L(\gamma-\tau)/(2\pi)),\qquad
 \langle W\rangle=\int W(T+Hu)w(u)\,du,\qquad H=T^a,\quad 0<a\le1 .
\]
Fourier inversion gives an entire \(f\). At fixed \(T\), its arguments stay in a fixed horizontal strip and decay rapidly in the real direction. The unit-window zero count implies absolute convergence at every real \(\tau\) and local uniformity. The reflected zero set pairs conjugate arguments, so the statistic is real without RH. The interval-indicator example on RH counts a window of half-width \(2\pi/L\), and that indicator is outside the Fourier test class.

The journal Theorem 1.1 states convergence of the first \(m\) Gaussian moments, \(m\ge1\) fixed, when \(\operatorname{supp}\widehat f\subset(-2a/m,2a/m)\). The target mean is \(I=\int f\) and variance is \(\sigma_f^2=\int \min(|v|,1)\widehat f(v)^2\,dv\). Compactness gives a fixed support radius \(\sigma<2a/m\). Centered targets are 0 for odd orders and \((2k)!\sigma_f^{2k}/(2^k k!)\) for order \(2k\); raw moments follow by translation. For \(m=1\) this asserts only the mean. A fixed moment window does not identify a law. The average is in a continuous real center against \(w\); the result assumes neither RH nor derivative-square zero weights.

## pp. 668–669, exact explicit formula and pointwise estimates

In Lemma 2.1 take \(g\in C_c^\infty\), \(h(r)=\int g(u)e^{iru}du\). The standard contour reconstruction fixes every constant in (2). For \(\Lambda_*(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\), integrate \(\Lambda_*'/\Lambda_*\) against \(h((s-1/2)/i)\) on paired verticals \(c,1-c\), \(1<c<2\). Shift on good heights, using strip decay of \(h\), the standard zero count and the partial-fraction bound for \(\zeta'/\zeta\) away from zeros. The poles at \(0,1\) each have logarithmic-derivative residue \(-1\). The functional equation reflects the left line, giving the right-line test \(h((s-1/2)/i)+h((1/2-s)/i)\). Shift the gamma-only part to \(1/2\) and use the absolutely convergent \(\zeta'/\zeta=-\sum\Lambda(n)n^{-s}\) on \(c\). Moving the two horizontal \(h\)-integrals to the real line gives the \(n^{-1/2}\) factor and \(g(\pm\log n)\). Thus
\[
 \sum_\gamma h(\gamma)=h(i/2)+h(-i/2)
  +\frac1{2\pi}\int h(r)\Omega(r)\,dr
  -\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}[g(\log n)+g(-\log n)],
\]
where \(\Omega(r)=\frac12\psi(1/4+ir/2)+\frac12\psi(1/4-ir/2)-\log\pi\) and \(\psi=\Gamma'/\Gamma\). This checks both polar signs and all Fourier factors.

For \(g(u)=e^{-i\tau u}\widehat f(u/L)/L\), (3) is the gamma integral \(G_f\) plus polar terms \(P_f=f(L(i/2-\tau)/(2\pi))+f(L(-i/2-\tau)/(2\pi))\). Equation (4) is the exact finite polynomial
\[
 S_f(\tau)=-\frac1L\sum_{2\le n\le T^\sigma}
    \frac{\Lambda(n)}{\sqrt n}\widehat f(\log n/L)
        (e^{i\tau\log n}+e^{-i\tau\log n}) .
\]
The explicit formula is valid for every real \(\tau\) at fixed \(T\), independently of averaging tails. The compact Fourier support makes the prime-power term finite. Since \(\Omega'(r)=O((1+|r|)^{-1})\) and \(\Omega(r)=\log(1+|r|)+O(1)\), substitute \(r=\tau+2\pi x/L\). On \(|x|\le\sqrt L\) the Taylor difference costs \(O(|x|/[L(1+|\tau|)])\) before the extra \(L^{-1}\). On its complement use Schwartz decay and the logarithmic triangle inequality. Comparing the entire integral with \(I\Omega(\tau)/L\) yields an \(O_A(L^{-A})\) tail uniformly in \(\tau\), which suffices for the printed (5), with bounded \(|\tau|\) absorbed in the first error. In particular, uniformly for real \(\tau\),
\[
 G_f(\tau)=I\log(1+|\tau|)/L+O_f(L^{-1}).
\]

The signed mean polar estimate in Lemma 2.2 is valid under the original \(L^1\) weight hypotheses. Fubini writes it with multiplier \(\widehat w(HLv/(2\pi))\), retaining only \(|v|\ll(HL)^{-1}\), where the imaginary-shift exponential is bounded. The signed polar mean is \(O((HL)^{-1})\). Likewise \(\langle S_f\rangle=0\) eventually by compact support and the minimum prime frequency \(\log2\). The mean problem arises precisely when computing the average of \(G_f\), before Proposition 2.3.

## Weight counterexample and corrected theorem

Both versions explicitly assume only \(w\ge0,\int w=1,\widehat w\) compactly supported. They require \(\widehat f\in C_c^\infty\) for the separate statistic, with no parallel assumption on \(\widehat w\). Let \(w_0\) be a normalized square of a real Schwartz bandlimited function and \(w(u)=\sum_{n\ge1}2^{-n}w_0(u-\exp(4^n))\). This is smooth, nonnegative, mass one, bandlimited by \(L^1\) convergence of the translated series. A fixed positive mass around each translating center gives an infinite first logarithmic moment by Tonelli. The weight can also be symmetrized. Qualitative localization \(\tau/T\to1\) in probability at \(a<1\) does not eliminate it.

The finite prime polynomial and polar terms are uniformly bounded in \(\tau\) at fixed \(T\). The gamma estimate yields
\[
 N_f(T+Hu)=I\log(1+|T+Hu|)/L+O_{f,T}(1).
\]
For \(I>0\) the first average with the witness is \(+\infty\). Choose \(f\) itself as a square of a real even bandlimited Schwartz function of sufficiently small support to meet the strict window. More generally, if \(I\ne0\), this growth proves that finite \(m\)-th absolute moment at fixed \(T\) is equivalent to \(\int w\log^m(2+|u|)<\infty\). If \(I=0\) the statistic is bounded at fixed \(T\). The corrected theorem retains all original assumptions and adds the alternative
\[
 I=0\quad\text{or}\quad \int w(u)\log^m(2+|u|)\,du<\infty.
\]
This is sufficient for all first \(m\) Gaussian moment limits in the same window, and the \(O(L^{-1})\) mean of Proposition 2.3. In particular it covers the intended Schwartz subclass with the original compact Fourier support. [Independent witness and mixed-moment repair](weighted82_hughes_rudnick_weight_review.md) · [Independent necessity and zero-mean review](analytic85_hughes_weight_repair_review.md)

## p. 670, finite-prime pairing, rates and odd orders

Expanding the \(j\)-th power of \(S_f\), \(j\le m\), gives a Fourier multiplier \(\widehat w(\pm H\log(M/N)/(2\pi))\), with \(M,N\) the products on the two signs. Global sign reversal swaps the sign convention of the phase and multiplier without changing the sum. If \(M>N\), then \(\log(M/N)\ge\log(1+1/N)\ge1/(2N)\) while \(N\le\sqrt{MN}\le T^{j\sigma/2}\). The strict \(m\sigma/2<a\) therefore eliminates all unequal products for large \(T\). The balanced coefficient is exactly \(\widehat w(0)=1\) and its center phase is one. This step does not need a tail bound on \(w\).

Group by underlying prime in each balanced tuple. Its local exponents have matching positive and negative totals. A block of size two is necessarily oppositely signed with equal exponents. Blocks of size \(\ell\ge3\) have even total exponent at least four, so the sum over all local exponents and their prime costs
\[
 O_\ell\!\left(L^{-\ell}\sum_p(\log p)^\ell p^{-2}\right)
\]
by geometric decay with polynomial multiplicities at fixed total. Size-two blocks with exponents \(\ge2\) cost \(O(L^{-2})\). This argument covers all nonpair structures in longer v1 Lemma 2.7. Between the nominal distinct pairs, equating two prime labels also contributes \(O(L^{-4}\sum_p(\log p)^4/p^2)\), so the asymptotic independent pair summation is legitimate. Odd \(j\) requires some nonpair block and tends to zero. For \(j=2k\), there are \((2k)!/(2^k k!)\) pair partitions and two sign orientations per pair. The leading term is \((2k)!/k!\) times the \(k\)-th power of
\[
 A_T=L^{-2}\sum_n \frac{\Lambda(n)^2}{n}\widehat f(\log n/L)^2 .
\]
The prime number theorem gives \(A_T\to\int_0^\infty v\widehat f(v)^2\,dv=\sigma_f^2/2\) when \(m\ge2\), since then \(\sigma<1\). The claimed \(O(1/L)\) scale follows from quantitative PNT partial summation, for instance first deriving \(\sum_{p\le x}(\log p)^2/p=\frac12\log^2 x+O(1)\) from \(\vartheta(x)=x+O(x/\log^3x)\), and then inserting the fixed smooth multiplier. Prime powers contribute \(O(L^{-2})\). For \(m=1\) no variance claim is needed. The pairing constants are the printed p. 670 constants and the rendered longer Proposition 2.5 convention. This reconstructs the finite prime-sum theorem over its unmodified weight class.

## Mixed smooth and polar terms at every order

Write \(\Delta(u)=G_f(T+Hu)-I\). The Fourier assumption gives a bounded continuous representative of \(w\) by inversion. If \(I=0\), the uniform smooth formula immediately gives \(\|\Delta\|_\infty=O(L^{-1})\). Every mixed product \(|S_f|^r|\Delta|^j\), \(j\ge1,\ r+j\le m\), then has average \(O(L^{-j})\) from the bounded available even moment at \(2\lceil r/2\rceil\le m\), or \(r=0\).

If \(I\ne0\), put \(K=T/H\ge1,\ v=u+K\). The uniform background estimate gives
\[
 |\Delta(u)|\ll_f L^{-1}[1+\log(2+|u|)+\log_+(1/(|v|+H^{-1}))].
\]
For the positive log difference use \(H\le T\). For the negative part use \(|v|\ge K/2\) or, in its complement, \(|u|\ge K/2\) and \(\log T-\log(1+H|v|)=\log K-\log(|v|+H^{-1})\). The two nonconstant errors are handled separately to avoid asking for an absolute odd highest moment of \(S_f\).

For \(\log(2+|u|)\), reproduce \(w=w*\psi\) using a Schwartz \(\psi\) with \(\widehat\psi=1\) on the support of \(\widehat w\). The positive bandlimited function \(\kappa(u)=\operatorname{sinc}^2(u)+\operatorname{sinc}^2(u-1/2)\), with normalized sinc, is bounded below by a constant times \((1+|u|)^{-2}\). Consequently \(|\psi(u)|(1+\log^j(2+|u|))\ll\kappa(u)\). The logarithmic triangle inequality yields a positive bandlimited majorant for \(w(u)(1+\log^j(2+|u|))\), namely a constant times its convolution with \(\kappa\). This has finite mass by hypothesis. Use the same bounded even prime moment under that fixed majorant.

For the moving log singularity let \(0<\varepsilon<a-m\sigma/2\). The interval \(|v|\le\delta\), \(T^{-\varepsilon}\le\delta\le1\), is majorized by a nonnegative integrable bandlimited bump \(B(v/\delta)\) of mass \(O(\delta)\). The effective height range \(H\delta\) retains the fixed exponent gap for Fourier separation through degree \(m\). The same even moment bound then gives \(\int_{|v|\le\delta}|S_f|^rdu\ll\delta\), uniformly, by Hölder. The log annuli contribute \(\sum_{\ell\ge0}(1+\ell)^j e^{-\ell}<\infty\). The smallest interval contributes \(O(T^{-\varepsilon}L^j)\), by the ceiling \(\log H\). Bounded \(w\) suffices here. Hence \(\langle |S_f|^r|\Delta|^j\rangle=O(L^{-j})\) also in the nonzero-mean case.

At the imaginary shifts of (3), Fourier integration by parts gives \(|P_f(\tau)|\ll_A T^{\sigma/2}(1+|\tau|)^{-A}\). The vertical exponential costs \(T^{\sigma/2}\), while derivatives \(O(L^A)\) are absorbed by real-direction gain \(L^{-A}\) off \(|\tau|\le1\). Also \(\|S_f\|_\infty\ll T^{\sigma/2}\) from its finite coefficients. Every mixed averaged term with a polar factor and total degree \(\le m\) is consequently \(O(T^{m\sigma/2}/H)=o(L^{-1})\), by boundedness of \(w\), the \(d\tau/H\) scaling, and decay absorbing powers of the smooth background logarithm. A small signed mean for the isolated polar term would not suffice. This proves additive \(o(1)\) comparison of every raw moment through \(m\) with \(I+S_f\), and a mean error \(O(1/L)\). Centering by the actual averaged mean then gives the same limits. In both the journal and v1 the displayed multiplicative \(1+O(1/L)\) shortcut is not justified by the smooth mean alone, especially for vanishing odd targets. The additive repair establishes the intended conclusion under the stated replacement.

## CUE comparison, upstream roles and scope

On p. 668 the ordinary CUE comparison is obtained by periodizing \(f(n\theta/(2\pi))\), with Fourier coefficients \(n^{-1}\widehat f(k/n)\). Haar traces of nonzero frequency have mean zero. The exact trace covariance \(\mathbb E|\operatorname{Tr}U^k|^2=\min(k,n)\) gives (1) in the limit by Riemann summation. For \(m\) with closed support \([-2/m,2/m]\), any balanced trace product has total positive frequency at most \(n\). Schur orthogonality then gives the exact power-sum Wick rule in that range, as in the later v2 of the cited [2, Theorem 6.5]. It has a closed ordinary-CUE window and a different measure. The statement that higher moments are not Gaussian describes a general failure beyond their guaranteed window. A smaller support can still give additional Gaussian moments. For example, a nonnegative nonzero test with nondegenerate limiting variance gives a nonnegative ordinary-CUE statistic at every \(n\). Convergence of all moments to a nondegenerate Gaussian would contradict the support restriction by moment determinacy and tightness. The broader arithmetic comparison mentioned conjecturally in longer v1 is outside the theorem.

Journal reference [2] is Hughes–Rudnick's low-lying \(L\)-function preprint math/0208230, whose later v2 also contains the separate character-family result. The compact-group preprint math/0206289v1 is dated 27 June 2002, with journal publication in 2003. These are the relevant primary contexts for the paper's self-citation and mock-Gaussian comparison. The 2002 zeta note is credited for its own continuous-height Fourier window and balanced prime products. The repaired tail qualification does not change that credit. The ordinary CUE and character-family schemes, HKO derivative rooting and derivative-square arithmetic sampling remain distinct. A bounded later-literature search does not determine first priority for every ingredient. The funding acknowledgement records the EC TMR quantum-chaos network and supplies no mathematical input. [Cited low-lying zeros preprint](https://arxiv.org/abs/math/0208230v2) · [Compact-group preprint](https://arxiv.org/abs/math/0206289v1) · [Prior source comparison](analytic79_prior_art.md)

**Level 3 coverage checklist, for director adjudication**

- Exact four-page Numdam pin and abstracts through acknowledgements, full longer v1 comparison with numbering, visual variance normalization, submission history and bounded erratum search.
- Introduction's gamma constant and conventions, Selberg and Fujii reference roles, complex ordinates and entire extension, exact \(H=T^a\), support, and \(m=1\) scope.
- Lemma 2.1 contour and residue signs, absolute convergence, \((2)\)–\((4)\) and their gamma, pole and finite prime-power parts.
- Lemma 2.2 pointwise (5), justified signed polar mean, failure of the literal smooth average, Proposition 2.3 and the corrected mean error.
- p. 670 finite Fourier separation, prime-power grouping, collision counts, odd/even limits, PNT and variance normalization.
- Additive mixed-term reconstruction for every admissible order, exact \(I=0\) exception and \(I\ne0\) log-moment necessity, Schwartz sufficiency, and no RH assumption.
- Ordinary CUE comparison and closed support endpoint, bounds on interpreting higher moments, context of [2] and outside historical results, explicit disjoint sampling laws.
- Upstream inputs accepted at their stated scope include the zeta functional equation, unit-window zero count, fixed-strip good-height logarithmic derivative, Stirling, quantitative PNT and Haar/Schur orthogonality. No claim to complete historical ancestry or full proof checks of Selberg and Fujii background. Literal unrestricted-weight theorem is not endorsed. The independent reviews are available, while the director's direct adjudication and any canonical Level 3 update are still required. [Skeptic arithmetic and weight reconstruction](weighted82_hughes_rudnick_weight_review.md) · [Independent analytic repair](analytic85_hughes_weight_repair_review.md)
