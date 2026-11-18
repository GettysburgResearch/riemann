# Advocate reconstruction of Hughes–Rudnick’s 2002 zeta note

**PAPER-AN79-HR-ZETA.** The four-page journal note proves the intended finite Gaussian moment window for Schwartz bandlimited averaging weights once its centering step is made additive. The same proof extends to the literal weight class when the test has mean zero, and otherwise the exact additional condition is a finite logarithmic moment of the claimed order. The oscillatory theorem already holds for the full printed weight class. This review supplies a reconstruction for the director’s decision. The canonical record remains at L1. [Canonical record](../../papers/PAPER-AN79-HR-ZETA.md)

I read pp. 667–670 of Chris Hughes and Zeév Rudnick, *Linear statistics for zeros of Riemann’s zeta function*, *C. R. Math. Acad. Sci. Paris* **335**(8), 667–670 (2002), DOI **10.1016/S1631-073X(02)02541-4**. The inspected file is `sources/analytic79_prior_art/hughes_rudnick_zeta_journal.pdf`, SHA-256 **b4572e5bdbf3cf7e891a4128aeb3bb56d151f2b16d23f9e63a94b1a2d2c09139**. I also read the nine-page arXiv v1, deposited 28 August 2002, at `sources/analytic79_prior_art/hughes_rudnick_zeta_v1.pdf`, SHA-256 **2225d590d97abd13a4b973bd3d936a7b07fb45a3296739438f8ce57f657cdebd**. I visually inspected its p. 6. The variance sum in Proposition 2.5 contains the explicit factor 2, consistent with its next display and with the journal. [Journal](https://archive.numdam.org/item/CRMATH_2002__335_8_667_0.pdf) · [Preprint v1](https://arxiv.org/pdf/math/0208220v1) · [Archive receipt](../../sources/analytic79_prior_art/receipt.md)

## pp. 667–668 | Setting and claims

The English and French abstracts describe a smooth zero count at microscopic scaling with only a finite moment window. Page 667 records receipt on 29 August, acceptance on 2 September, and presentation by Christophe Soulé. The introduction separates the remainder \(S(t)\) from the smooth Riemann–von Mangoldt count. With the continuous argument for the gamma factor, Stirling gives
\[
\pi^{-1}\operatorname{Im}\log\{\pi^{-iT/2}\Gamma(1/4+iT/2)\}
=\frac{T}{2\pi}\log\frac{T}{2\pi e}-\frac18+O(T^{-1}).
\]
The leading 1 in the smooth count gives the printed \(7/8\). Endpoint counting can be absorbed into the definition of the remainder. Selberg’s cited even moments for \(S(t)\) use the normalization \(\sqrt{\log\log t/(2\pi^2)}\) and \(T^a\le H\le T\), \(1/2<a\le1\). Fujii’s cited increment results concern windows longer than the mean spacing. The preprint distinguishes small \(h\) with \(h\log T\to\infty\) from \(h\to\infty\), \(h\ll T\). These references motivate the microscopic setting. Their deep moment estimates are outside the dependencies of the proof.

Use the convention \(\widehat f(v)=\int f(x)e^{-2\pi ixv}dx\). Take \(f\) real, even, with \(\widehat f\in C_c^\infty(\mathbb R)\). Put \(L=\log T\), \(H=T^a\), \(0<a\le1\), and
\[
N_f(\tau)=\sum_{\rho=1/2+i\gamma} f(L(\gamma-\tau)/(2\pi)),\qquad
\langle W\rangle=\int W(T+Hu)w(u)du.
\]
Zeros are counted with multiplicity. The entire extension from Fourier inversion decays rapidly in the real direction on fixed strips. At fixed \(T\) the zero arguments lie on such a strip, and the usual unit-height zero count gives absolute convergence and local uniformity in \(\tau\). Symmetry about the critical line gives conjugate pairs of \(\gamma\) and makes the sum real. Under RH the indicator example would count a window of half-width \(2\pi/L\). The smooth Fourier hypothesis governs all actual proof steps.

The printed assumptions on the fixed averaging weight are \(w\ge0\), \(\int w=1\), and compact support of \(\widehat w\). Theorem 1.1 assumes \(\operatorname{supp}\widehat f\subset(-2a/m,2a/m)\) for fixed integer \(m\ge1\). It asserts convergence of every raw moment through order \(m\) to those of a real Gaussian with mean \(I=\int f\) and variance
\[
V=\int_{\mathbb R}\min(|v|,1)\widehat f(v)^2,dv.
\]
For \(m=1\) only the expectation is tested. A fixed finite set of matched moments leaves the limiting law undetermined. The argument takes place under a continuous height average and requires no RH.

## pp. 668–669 | Explicit formula and the mean

For Lemma 2.1, use \(h(r)=\int g(u)e^{iru}du\), \(g\in C_c^\infty\). Integrate the logarithmic derivative of \(\pi^{-s/2}\Gamma(s/2)\zeta(s)\) with test \(h((s-1/2)/i)\) across the strip between \(c\) and \(1-c\), \(1<c<2\). Rapid strip decay of \(h\) and the standard good-height logarithmic derivative bound remove the horizontal sides along a sequence. Residues at the completed zeta poles \(0,1\) are each \(-1\) for the logarithmic derivative, giving the positive terms \(h(\pm i/2)\) on solving for the zero sum. The functional equation reflects the left vertical to the right and adds the reflected test \(h((1/2-s)/i)\). Shift the gamma part to \(1/2\) and substitute the convergent Mangoldt series for the zeta part on \(c\). With \(b=c-1/2\), the prime term uses the horizontal line at \(\operatorname{Im}r=-b\) for the direct test, with \(n^{-s}=n^{-1/2}e^{-ir\log n}\), and its reflection for the other test. Moving each to the real axis gives \(g(\pm\log n)\) by Fourier inversion. Thus journal (2) has the constants
\[
\sum_\gamma h(\gamma)=h(i/2)+h(-i/2)+\frac{1}{2\pi}\int h(r)\Omega(r)dr
-\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}[g(\log n)+g(-\log n)],
\]
where \(\Omega(r)=\tfrac12\psi(1/4+ir/2)+\tfrac12\psi(1/4-ir/2)-\log\pi\) and \(\psi=\Gamma'/\Gamma\).

In (3)–(4) set \(h(r)=f(L(r-\tau)/(2\pi))\), \(g(u)=L^{-1}e^{-i\tau u}\widehat f(u/L)\). The identity becomes \(N_f=G+P+S_f\) with
\[
\begin{aligned}
G(\tau)&=L^{-1}\int f(x)\Omega(\tau+2\pi x/L)dx,\\
P(\tau)&=f(L(i/2-\tau)/(2\pi))+f(L(-i/2-\tau)/(2\pi)),\\
S_f(\tau)&=-L^{-1}\sum_{2\le n\le T^\sigma}\frac{\Lambda(n)}{\sqrt n}
\widehat f(\log n/L)(e^{i\tau\log n}+e^{-i\tau\log n}),
\end{aligned}
\]
where \(\operatorname{supp}\widehat f\subset[-\sigma,\sigma]\) and \(m\sigma/2<a\). Stirling gives \(\Omega(r)=\log(1+|r|)+O(1)\) and \(\Omega'(r)=O((1+|r|)^{-1})\). On \(|x|\le\sqrt L\) the difference from \(\Omega(\tau)\) is \(O(|x|/[L(1+|\tau|)])\). On the complement the difference of the two logarithms in Stirling's leading terms is at most \(\log(1+2\pi|x|/L)\) in absolute value, uniformly in \(\tau\). Rapid decay therefore gives an arbitrary power saving in \(L\) on the difference integral. This gives the estimate (5), including uniform control at bounded \(\tau\), and in particular
\[
G(\tau)=\frac{I}{L}\log(1+|\tau|)+O_f(L^{-1}).
\]

The signed average \(\langle P\rangle=O((HL)^{-1})\) follows by Fourier inversion against \(w\). Each term is supported in frequency on \(|v|\ll(HL)^{-1}\) after multiplication by \(\widehat w(\pm HL v/(2\pi))\), so its exponential from the imaginary shift stays bounded. The prime average is exactly zero for large \(H\) because its smallest nonzero angular frequency is \(\log 2\). The remaining part of journal Lemma 2.2 and hence Proposition 2.3 requires controlling the average of \(G\). The all-real-line tails of \(w\) matter even when \(a<1\). These journal results correspond to v1 Lemmas 2.2–2.3 and Proposition 2.4; journal (2)–(6) correspond to v1 (3)–(7).

## p. 670 | Arithmetic theorem for the oscillation

For any fixed \(j\le m\), the integrated expansion attaches
\(e^{-iT\log(M/N)}\widehat w(H\log(M/N)/(2\pi))\) to the signed prime-power tuple, using the global sign convention in the paper. Here \(M,N\) are products of the positive and negative entries. Either global sign convention gives the same sum. If \(M>N\), the frequency is at least \(\log(1+1/N)\ge 1/(2N)\). Since \(N\le\sqrt{MN}\le T^{j\sigma/2}\), compact Fourier support eliminates every unequal pair of products for large \(T\). The multiplier on equality is exactly one. This proves the separation with the strict window \(m\sigma/2<a\).

In a balanced tuple group the entries \(p^e\) by their base prime \(p\), with equal signed exponent totals in each group. A two-entry group has one sign of each kind and equal powers. Every group of size \(b\ge3\) has even total exponent at least four. Summing the absolute weights of one such group independently over its prime and exponents costs at most \(C_b L^{-b}\sum_p(\log p)^b/p^2\). The estimate follows by summing the geometrically decaying \(p^{-s/2}\) over even total exponents \(s\ge4\), with at most polynomially many compositions for fixed \(b\). Dropping the distinct-prime restriction for bounds does no harm. Two-entry groups are bounded after normalization. The same large-block estimate controls collisions when replacing distinct primes of the pair partition by unrestricted pair choices. This reconstructs the result of longer v1 Lemma 2.7 without having to reduce individual prime-power configurations to triples.

Put \(A_T=L^{-2}\sum_n\Lambda(n)^2n^{-1}\widehat f(\log n/L)^2\). By partial summation, \(\sum_{p\le x}(\log p)^2/p=\tfrac12\log^2x+O(1)\), using for instance \(\vartheta(x)=x+O(x/\log^3x)\). Inserting the smooth multiplier costs \(O(L^{-2})\) after normalization, since its variation in \(\log p\) is uniformly bounded. Higher powers also contribute \(O(L^{-2})\). Therefore \(A_T=\int_0^\infty v\widehat f(v)^2dv+O(L^{-2})\). For \(m\ge2\) the strict support has \(\sigma<1\), and this integral is \(V/2\).

Odd \(j\) requires a block of size at least three, or has no balanced tuples. Its signed moment tends to zero with an additive error of order at most \(L^{-1}\). For \(j=2k\), the \((2k)!/(2^k k!)\) pair partitions have two sign orientations per pair, giving \((2k)!A_T^k/k!\) up to the negligible groups and collision costs. The resulting moment is \((2k)!V^k/(2^k k!)+O(L^{-1})\). In particular, longer Proposition 2.5 has \(2A_T\), in agreement with the rendered p. 6. This includes v1 Theorem 2.6 and justifies the pairing invoked by the journal via its reference [2].

## Literal weight, necessity and repair

For an explicit test of the weight hypotheses, choose a nonzero real even Schwartz function \(q\) with smooth compact Fourier transform and let \(b=q^2/\int q^2\). Take \(w(u)=\sum_{n\ge1}2^{-n}b(u-e^{4^n})\). The series converges in \(L^1\), has mass one, is nonnegative, and its Fourier transform vanishes off the support of \(\widehat b\). Every summand contributes a fixed positive fraction of its mass within a fixed distance of its center, where \(\log(2+|u|)\gg4^n\) for large \(n\). Tonelli proves an infinite logarithmic first moment. Take \(f\) to be a real even bandlimited Schwartz square by the same construction, choosing its Fourier radius sufficiently small to satisfy the strict window. Then \(I>0\). At fixed \(T\) both \(S_f\) and \(P\) are bounded on the real line, so the formula for \(G\) forces \(\langle N_f\rangle=+\infty\). This failure applies even to the mean and even if the translated weight is symmetrized.

More precisely, with \(I\ne0\), at each fixed \(T>1\) the absolute value of \(N_f(T+Hu)\) is comparable to \(\log(2+|u|)\) for sufficiently large \(|u|\). Thus existence of the finite absolute moment of integer order \(m\) is equivalent to \(\int w(u)\log^m(2+|u|)du<\infty\). For \(I=0\), \(N_f\) is bounded at each \(T\). The sufficient condition for the full theorem is the alternative
\[
I=0 \quad\text{or}\quad \int w(u)\log^m(2+|u|)du<\infty.
\]
This retains every fixed nonnegative Schwartz weight of mass one with compact Fourier support. Requiring \(\widehat w\in C_c^\infty\) would be a convenient stronger condition. The logarithmic alternative also repairs the stated mean rate, using order 1 for the mean alone and \(H=T^a\). The standalone mean formula likewise holds for \(H\to\infty\), \(H\le T\) under the corresponding first-log condition or \(I=0\).

### Additive comparison, including odd highest orders

Write \(D(u)=G(T+Hu)-I\), \(K=T/H\), and \(v=u+K\). Since \(\widehat w\) is bounded and integrable, use the bounded continuous representative of \(w\). For \(I=0\), \(D=O(L^{-1})\) uniformly. Otherwise the gamma estimate and \(K\ge1\) give
\[
|D(u)|\ll_f L^{-1}\big[1+\log(2+|u|)+\log_+(1/(|v|+H^{-1}))\big].
\]
For the upper fluctuation use \(1+|T+Hu|\le T(2+|u|)\). For the lower fluctuation use \(|v|\ge K/2\), when the logarithmic ratio costs at most \(\log 2\), or \(|v|<K/2\), when \(K\le 2|u|\) and the ratio is \(K/(|v|+H^{-1})\).

The following localization supplies the mixed-moment estimates directly. Choose a fixed nonnegative integrable bandlimited Schwartz bump \(B\ge1\) on \([-1,1]\) by squaring and dilating a real bandlimited Schwartz function nonzero at the origin. For \(0<\epsilon<a-m\sigma/2\), a slab \(|u-c|\le\delta\), \(T^{-\epsilon}\le\delta\le1\), is covered by \(B((u-c)/\delta)\). Under this weight the effective height scale is \(H\delta\), the Fourier multiplier forces equality uniformly in the center \(c\), and the total mass is \(O(\delta)\). The preceding arithmetic gives bounded even moments after normalization. Consequently \(\int_{|u-c|\le\delta}|S_f(T+Hu)|^rdu\ll\delta\) whenever \(r=0\) or \(2\lceil r/2\rceil\le m\), by Hölder.

For \(q\ge1\) and \(r+q\le m\) this covers every needed power \(r\), including when \(m\) is odd. To handle the weight in the growing logarithm, reproduce \(w=w*\eta\) with \(\eta\) Schwartz and \(\widehat\eta=1\) on the support of \(\widehat w\). For each integer unit cell \([n,n+1]\),
\[
\sup_{u\in[n,n+1]}w(u)\le C_N\int w(y)(1+|n-y|)^{-N}dy.
\]
The sum of these suprema multiplied by \(1+\log^q(3+|n|)\) is finite: use Tonelli, the logarithm of the product bound \(3+|n|\le(3+|y|)(1+|n-y|)\), and the uniformly summable shifted lattice kernel for \(N>2\). Applying the unit-slab moment estimate cell by cell therefore bounds \(\int |S_f|^r[1+\log^q(2+|u|)]w(u)du\). For the moving local logarithm use boundedness of \(w\) and annuli \(e^{-\ell-1}<|v|\le e^{-\ell}\) down to \(T^{-\epsilon}\); their contribution is bounded by a constant times \(\sum_{\ell\ge0}(1+\ell)^q e^{-\ell}\). The innermost slab costs \(O(T^{-\epsilon}L^q)\), since the local logarithm is at most \(\log H\). These bounds give \(\langle |S_f|^r|G-I|^q\rangle=O(L^{-q})\). When \(I=0\) use just the uniform bound and the unlocalized even moments.

For the polar term Fourier integration by parts gives \(|P(\tau)|\ll_A T^{\sigma/2}(1+|\tau|)^{-A}\). The Fourier exponential from the imaginary argument costs \(T^{\sigma/2}\); the loss of \(L^A\) in its derivatives is absorbed by integration by parts against the real phase. Trivially \(\|S_f\|_\infty\ll T^{\sigma/2}\) from \(\Lambda(n)\le \log n\) and summing \(n^{-1/2}\). Every averaged term that contains a polar factor and has total degree at most \(m\) therefore costs \(O(T^{m\sigma/2}/H)\), using bounded \(w\), the change of variable \(d\tau/H\), and decay in \(\tau\) sufficient to integrate any powers of \(\log(1+|\tau|)\) from \(G\). The strict support makes this error smaller than \(L^{-1}\).

Expansion now compares every raw moment of \(N_f\) through order \(m\) with the moment of \(I+S_f\) with additive error \(O(L^{-1})\). The mean and the moments centered at the actual average follow as well. The multiplicative comparison printed on p. 669 and in v1 p. 6 does not follow from the mean estimate and would in particular impose an unwarranted constraint whenever the signed prime moment vanishes. The mixed estimates supply the missing step, including for the historical Schwartz subclass. [Previous weight audit](weighted82_hughes_rudnick_weight_review.md) · [Repair review](analytic85_hughes_weight_repair_review.md) · [Skeptic whole-paper reconstruction](weighted88_hr_whole_skeptic.md)

## Comparison and references

The ordinary CUE statement on p. 668 uses Fourier coefficients \(n^{-1}\widehat f(k/n)\) for the periodization. Nonconstant terms are powersum traces of a Haar unitary. Haar scalar invariance forces the two signed totals of Fourier indices to agree, and Haar trace covariance \(\mathbb E|\operatorname{Tr}U^k|^2=\min(|k|,n)\) gives the stated variance by Riemann sums. With \(\operatorname{supp}\widehat f\subset[-2/m,2/m]\), the common positive frequency total of a balanced product through degree \(m\) is at most \(n\). In this range Schur orthogonality for partitions of that total gives power-sum inner products \(\mathbf 1_{\lambda=\mu}\prod_k k^{b_k}b_k!\), where \(b_k\) are the multiplicities of part \(k\). These are the complex Gaussian trace pairing moments, yielding the real Gaussian moments for the periodized statistic. The variance at independent trace degree is the same since the individual frequencies in a contributing balanced product are at most \(n\). The closed CUE support window is consistent with this calculation. The remark on higher moments signals a failure in general beyond a guaranteed window. A narrower test may allow a longer window. For example, an admissible nonnegative test of positive limiting variance gives nonnegative CUE statistics, which cannot converge in all moments to a nondegenerate Gaussian by Gaussian moment determinacy. The wider zeta window and unrestricted variance proposed in longer v1 are expectations, outside the journal theorem.

The three journal references are Fujii’s 1999 chapter for increments, the authors’ math/0208230 for the pairing method, ordinary CUE comparison and Dirichlet-family context, and Selberg’s 1946 work for the longer-scale Gaussian remainder moments. The EC TMR acknowledgment supplies funding context. Ordinary CUE, low-lying character-family sampling, and the continuous-height zeta statistic use different averaging laws. The result also supplies no derivative-square zero-weight transfer. The preprint’s remark about weaker explicit-formula test classes is unused in this reconstruction. Historical source and correction-search context is documented in the earlier audits. [Low-lying zeros preprint](https://arxiv.org/abs/math/0208230v2) · [Prior-art audit](analytic79_prior_art.md) · [Correction-history audit](analytic85_hughes_weight_repair_review.md)

## Whole-paper coverage checklist

- [x] Four-page controlling journal PDF, DOI, verified SHA-256, bibliographic and editorial details, both abstracts and acknowledgment.
- [x] Introduction, zero-count normalization, Selberg and Fujii roles, complex ordinates, entire test class, real statistic, scaling and exact Theorem 1.1 hypotheses.
- [x] Lemma 2.1 via completed zeta, functional equation, residues, gamma and Fourier constants; formulas (2)–(4) pointwise.
- [x] Lemma 2.2 and (5), separate signed polar computation, zero oscillatory mean and repaired Proposition 2.3 with mean rate.
- [x] Page 670 strict \(m\sigma/2<a\) cutoff, balanced prime powers, collisions, parity, pair counts, PNT, variance, and longer v1 proof and visual variance factor.
- [x] Independent counterexample, exact log-moment necessity for \(I\ne0\), all-order sufficiency including odd \(m\), zero-mean case and Schwartz case.
- [x] Ordinary CUE comparison, higher-moment scope, cited reference roles, and boundaries of the arithmetic statement.
- [x] Accepted upstream inputs at the stated scope include Stirling, standard zero count and good-height contour bounds, the functional equation, quantitative PNT and Schur orthogonality. The Selberg and Fujii proofs are background and were outside the reconstruction. Director adjudication remains pending.
