# Third review of absolute Mellin sampling at \(p=3\)

The actual \(p=3\) packet construction passes. For every sign realization the test satisfies the manuscript’s printed value bounds and has finite whole-strip norm. For almost every independent sign realization the absolute evaluation on the actual nontrivial zeta zeros diverges. This establishes failure of a general absolute-sampling assertion at that endpoint. The signed symmetric height limit is a different question, which this argument does not decide. [Construction](weighted138_critical_endpoint_campaign.md) · [Independent adversarial proof](analytic139_critical_endpoint_adversarial.md) · [Sufficiency for \(p>3\)](weighted135_critical_log_repair_review.md)

## Uniform deterministic packet estimate

Write \(w(t)=\sqrt{1+t^2}\log^3(e+|t|)\). For \(d=|t-\nu|\), the inequalities
\[
 \langle t\rangle\ll\langle\nu\rangle(1+d),\qquad
 \log(e+|t|)\le \log(e+|\nu|)+\log(1+d)
\]
give \(w(t)^{1/2}\ll w(\nu)^{1/2}(1+d)^2\). Thus the weighted envelope of any fixed finite integer block of translates of
\[
 J_\beta(v)=\int\psi(u)e^{(\beta-1/2)u}e^{ivu}\,du
\]
is bounded by the convolution envelope \(\sum_\nu |c_\nu|w(\nu)^{1/2}g(t-\nu)\), where \(g(v)=(1+|v|)^{-M}\) for any fixed \(M>1\). The rapid decay of \(J_\beta\) is uniform on the closed strip \(-1/4\le\beta\le5/4\) by compact support and integration by parts. The \(L^2\) norm of this positive envelope is at most
\[
 \bigl(\sup_t\sum_{\nu\in\mathbb Z}g(t-\nu)\bigr)^{1/2}
 \|g\|_1^{1/2}\left(\sum_\nu |c_\nu|^2w(\nu)\right)^{1/2},
\]
by pointwise Cauchy–Schwarz followed by integration. There is no dependence on block length, location, phases, or amplitudes. Apply this to \(\nu=\pm n\) with the cosine coefficient split equally between the two frequencies. These two deterministic terms share the same random sign and are not treated as independent variables.

For the \(j\)-th block, \(w(n)a_{j,n}^2\ll\lambda_j^2/(n\log n)\). Each dyadic shell contributes at most \(C\lambda_j^2/r\), and the extra terminal integer in the closed carrier set is covered by the last shell. The translation by \(j\) contributes \(e^{(\beta-1/2)j}\), bounded by \(e^{3j/4}\) everywhere on the strip. Integrating over its fixed length gives whole-strip norm at most
\[
 C e^{3j/4}\lambda_j\sqrt{S_j}
 =C e^{5j/4}/\sqrt{S_j}\le C e^{-3j/4}.
\]
The triangle inequality therefore gives finite \(N_3\) without any cross-block orthogonality.

The value envelope verifies the Mellin identity independently of the weighted \(L^2\) limit. Each physical block consists of finitely many carriers, and the supports near \(u=j\) are disjoint and locally finite. On that support its absolute size is \(O(\lambda_j)\), because \(\sum_{n\ge2}1/(n\log^2 n)<\infty\), so the physical \(f(x)=x^{-1/2}F(\log x)\) is \(O(x^{-4})\) at infinity and vanishes near zero and one. Real smoothness requires no derivative estimate at infinity. The absolute Mellin packet-integral bounds are \(O(e^{3j/4}\lambda_j)\), summable uniformly in \(\beta\) and all real ordinates. Thus the continuous transforms of the partial physical packets converge uniformly to the actual Mellin integral on the stated strip. Their weighted \(L^2\) limit agrees with this integral by local uniqueness. In particular there is no representative ambiguity when evaluating at specific zeros.

## Single-carrier lower bound and sample expectation

On \(2^r<\gamma\le2^{r+1}\), choose a nearest integer \(n\) with \(|\gamma-n|\le1/2\). The carrier set includes both endpoints of its full range, so this also works at the top shell endpoint. The Mellin transform of the unsigned carrier at \(\rho=\beta+i\gamma\) is
\[
 \frac{a_{j,n}}2e^{(\beta-1/2)j}
 \left[e^{i(\gamma-n)j}J_\beta(\gamma-n)
       +e^{i(\gamma+n)j}J_\beta(\gamma+n)\right].
\]
For \(0\le\beta\le1\), \(|v|\le1/2\), the first transform has \(\Re J_\beta(v)\ge e^{-1/16}\cos(1/16)>0\), by the bump support and integral one. The external oscillatory factor need not have positive real part, so the argument uses its modulus only. The other half of the same cosine is uniformly negligible as \(r\to\infty\). Since \(n\asymp2^r\), the entire single-carrier coefficient has modulus at least a fixed multiple of \(e^{-j/2}\lambda_j/(2^r r^2)\). No pointwise lower bound for the whole unsigned block is used.

Fix one zero. For a complex finite Rademacher sum \(Z=\sum_m\varepsilon_m b_m\), let \(V=\sum_m|b_m|^2\). Expanding over even index multiplicities gives
\[
 \mathbb E|Z|^2=V,\qquad
 \mathbb E|Z|^4=2V^2+\left|\sum_m b_m^2\right|^2-2\sum_m|b_m|^4\le3V^2.
\]
These identities pass to the infinite coefficient sequence by the sign-uniform absolute bound for the Mellin integral. Hölder gives \(\mathbb E|Z|^2\le(\mathbb E|Z|)^{2/3}(\mathbb E|Z|^4)^{1/3}\), hence \(\|Z\|_2\le\sqrt3\,\mathbb E|Z|\). The zero case is immediate. This is an explicit substitute for the first Paley–Zygmund step.

There are \(\gg2^r r\) actual positive ordinates in each dyadic shell for all sufficiently large \(r\), counting multiplicities, by Riemann–von Mangoldt. This uses no short spacing or critical-line hypothesis. Summing the expectation lower bound gives \(\gg e^{-j/2}\lambda_j/r\) per shell and \(\gg e^{-j/2}\lambda_jS_j\gg1\) per block. Disjoint exponent ranges prevent double counting. Conjugation for real \(f\) identifies magnitudes at the reflected heights, but the lower bound needs only the positive ones. [Classical zero count](../../sources/equivalence_round2/titchmarsh1986.pdf)

## Positive probability and the tail event

Let \(X_T\) be the sum of the absolute evaluations at \(0<\gamma\le T\). This finite measurable random variable belongs to \(L^2\), and Minkowski with the per-zero estimate gives \(\|X_T\|_2\le\sqrt3\,\mathbb E X_T\). Thus Paley–Zygmund yields
\[
 \mathbb P(X_T\ge \mathbb E X_T/2)\ge 1/12
\]
whenever its mean is positive. The block lower bounds make \(\mathbb E X_T\to\infty\). For any \(B>0\), choose \(T\) with \(\mathbb E X_T>2B\). Monotonicity gives \(\mathbb P(X_\infty>B)\ge1/12\), and continuity on decreasing threshold events gives \(\mathbb P(X_\infty=\infty)\ge1/12\). This extra second-moment argument is essential, since infinite expectation alone would not establish existence.

The almost-sure upgrade is valid on the actual countable product. Changing finitely many signs adds a finite sum of compactly supported smooth logarithmic profiles. Its Mellin transform is rapidly decreasing in height uniformly on \(0\le\beta\le1\), hence is absolutely summable on the zero multiset by the classical count. The triangle inequality therefore makes the divergence event invariant under every finite sign modification. Enumerate the countable signs and, for each \(m\), set the first \(m\) signs to \(+1\). This is a measurable map. The pulled-back divergence event depends only on signs after \(m\) and equals the original event pointwise by invariance. Consequently that event belongs to the tail sigma field, and independence plus its positive probability gives probability one.

The source’s ordinary integral and prime terms converge absolutely for every realization by \(O(x^{-4})\) decay and vanishing near one. In particular this failure is in actual absolute zero sampling, beyond merely showing that a Cauchy–Schwarz majorant diverges at the endpoint. The checks do not establish divergence of the signed symmetric zero sum, failure of an endpoint Dini result for arbitrary tests, or publication priority. No canonical records changed.
