# A zeta-zero obstruction to the weighted closure in Theorem 5.5

Independent functional analysis, 2026-11-17. Novelty unassessed. Targeted source reading, with independent review pending. No outreach.

## Published statement and counterexample

PAPER-E012 is Eva A. Gallardo-Gutiérrez and Daniel Seco, *Zero-Free Regions of the Riemann Zeta Function and Approximation in Weighted Dirichlet Spaces*, Complex Analysis and Operator Theory 19 (2025), article 38. A fresh rendering of p. 26 from the local publisher PDF sources/logarithmic_riesz_round3/gallardo_seco2025.pdf was inspected visually. Its Theorem 5.5 reads, with mathematical notation transcribed:

> Let \(\alpha\in[-3,-2]\), \(a\in[1,(1-\alpha)/2)\) and \(\Omega_\alpha=\{z\in\mathbb C:\Re(z)>(-1-\alpha)/2\}\). The function \((1-z)^{1-a}\) is in the closure in \(D_{\alpha+2}\) of \(\operatorname{span}\{(1-z)^{1-a}h_k:k\ge 2\}\) if and only if \(\Omega_\alpha\) is a zero-free region of the Riemann zeta function.

The same iff is present in the staged arXiv v6 text on p. 21. Theorem 2.1 on publisher p. 5 states an approximation-to-zero-free implication. Theorem 5.5 has no separate proof beyond the lead-in referring to the preceding results. [Publisher DOI](https://doi.org/10.1007/s11785-025-01661-2)

For the allowed pair \((\alpha,a)=(-3,7/4)\), the prescribed half-plane is \(\Re s>1\), which is zero-free by the Euler product. Yet the asserted closure fails. A critical-line zero, whose existence follows from Hardy's theorem, gives a bounded linear functional that vanishes on every generator and takes a nonzero value on the target. The same argument excludes the closure for every allowed \(a>3/2\) at \(\alpha=-3\). The proof is independent of the bounded-bijection conclusion of Proposition 5.1 and applies with \(a>-(\alpha+1)/2\), strictly above that proposition's disputed endpoint.

## Definitions and source identities

The coefficient norm on publisher p. 3 is \(\|f\|_{D_\gamma}^2=\sum_{n\ge 0}(n+1)^\gamma |[z^n]f|^2\). Put
\[
 t=-(\alpha+1)/2,\quad c=a-1,\quad 0\le c<t,\quad
 h(z)=(1-z)^c,\quad u(z)=1/h(z),\quad f_0(z)=1/(1-z).
\]
All powers take the analytic branch positive on \((0,1)\). Define
\[
 r_k(n)=n-k\lfloor n/k\rfloor,\qquad
 R_k(z)=\sum_{n\ge1}r_k(n)z^{n-1},\qquad
 h_k(z)=\frac{\log((1+z+\cdots+z^{k-1})/k)}{1-z}.
\]
The log branch is real on \((0,1)\). The operator on publisher p. 21 is \(T_af=f'-af/(1-z)\), and its composition with multiplication by \(h\) maps
\[
 hT_au=-f_0,\qquad hT_a(uh_k)=R_k.
\]
Indeed \(a=c+1\) gives \(hT_a(uv)=v'-v/(1-z)\). For \(v=h_k\), this is \(((1-z)h_k)'/(1-z)\). The derivative of the numerator log is \(1/(1-z)-kz^{k-1}/(1-z^k)\), so division by \(1-z\) gives \(R_k\) by summing the floor sequence. This independently checks the signs and Eq. (29) on p. 26.

For \(c>0\), the coefficients of \(u\) are \(O_c((n+1)^{c-1})\). The coefficients of \(h_k\) are \(O_k((n+1)^{-1})\), from the expression \(H_n-H_{\lfloor n/k\rfloor}-\log k\) and the harmonic number asymptotic with error \(O(1/n)\). Splitting the convolution into its two halves gives coefficients of \(uh_k\) bounded by \(O_{c,k}((n+1)^{c-1}\log(n+2))\). Both the target and generators are therefore in \(D_{\alpha+2}\), since \(\alpha+2c<-1\). When \(c=0\) the corresponding membership follows from the constant target and the coefficient bound on \(h_k\).

## The weighted Mellin functional

For \(\sigma=\Re s>0\), define
\[
 \mathcal L_s(g)=\frac{1}{s\Gamma(s)}
 \int_0^1(-\log r)^{s-1}(1-r)g(r)\,dr
\]
on functions for which the integral converges absolutely. It is a bounded functional on
\[
 W_{\alpha,c}=\{g:g/h\in D_\alpha\},\qquad
 \|g\|_{W_{\alpha,c}}=\|g/h\|_{D_\alpha}
\]
whenever \(\sigma>t-c\). Writing \(q=g/h\), Cauchy–Schwarz gives
\[
 |q(r)|\le \|q\|_{D_\alpha}
       \Big(\sum_{n\ge 0}(n+1)^{-\alpha}r^{2n}\Big)^{1/2}
 \ll_\alpha\|q\|_{D_\alpha}(1-r)^{-t-1}.
\]
Here \(-\alpha=2t+1\), and the exponential sum is \(O((1-r)^{-2t-2})\) by grouping \(n+1\) into blocks of length comparable to \((1-r)^{-1}\). The absolute integrand near \(1\) is bounded by a constant times \(\|q\|_{D_\alpha}(1-r)^{\sigma+c-t-1}\), integrable under the stated strict estimate on \(\sigma\). On \((0,1/2]\), \(q\) is uniformly bounded by the same coefficient estimate and every real power of \(-\log r\) is integrable there.

For the target space, the functional
\[
 \Lambda_s(f)=\mathcal L_s(hT_af)
\]
is bounded on \(D_{\alpha+2}\) for \(\sigma>t-c\). This follows from the independent boundedness of \(T_a:D_{\alpha+2}\to D_\alpha\) in [the earlier operator audit](gallardo_seco_operator_impact_advocate_round4.md). It also follows directly. With \(\beta=\alpha+2=1-2t\), coefficient Cauchy–Schwarz gives, for \(1/2<r<1\),
\[
 |f(r)|\ll \|f\|_{D_\beta}(1-r)^{-t},\qquad
 |f'(r)|\ll \|f\|_{D_\beta}(1-r)^{-t-1}.
\]
For the derivative, use the exponential sum with coefficient weight \(n^2(n+1)^{-\beta}\) and factor \(r^{2n-2}\). Both evaluations are uniformly bounded on \(0\le r\le 1/2\), by separate coefficient sums. The radial bound on \(T_af\) then gives the same integrability and operator norm bound.

## Exact Mellin values

For bounded coefficients \(g(z)=\sum_{n\ge1}b_nz^{n-1}\), insertion of the series gives
\[
 \mathcal L_s(g)=\frac1s\sum_{n\ge1}b_n\big(n^{-s}-(n+1)^{-s}\big),\qquad \Re s>0 .
\]
Indeed \(x=-\log r\) gives \(\int_0^1(-\log r)^{s-1}r^{n-1}\,dr=\Gamma(s)n^{-s}\). Absolute interchange holds since the series of absolute integrands is bounded by a constant times \((-\log r)^{\sigma-1}\).

For \(f_0\), the sum telescopes to \(1/s\). For \(R_k\), use \(r_k(0)=0\) and boundedness of \(r_k(n)\) in finite summation by parts. For \(\Re s>1\) this gives
\[
 \mathcal L_s(R_k)
 =\frac1s\sum_{n\ge1}\big(r_k(n)-r_k(n-1)\big)n^{-s}
 =\frac{\zeta(s)}s(1-k^{1-s}).
\]
The difference in parentheses is \(1-k\mathbf1_{k\mid n}\). The initial difference-of-powers sum converges locally uniformly for \(\Re s>0\) because \(n^{-s}-(n+1)^{-s}=s\int_n^{n+1}x^{-s-1}\,dx\). Analytic continuation gives the identity in all of \(\Re s>0\), with the singularity of its right side at one removable.

## Separation and consequence for the proposed core argument

For each zeta zero \(\rho\) with \(\Re\rho>t-c\), the continuous functional \(\Lambda_\rho\) annihilates \(uh_k\) for every \(k\) and satisfies \(\Lambda_\rho(u)=-1/\rho\). It yields the positive lower bound \(1/(|\rho|\,\|\Lambda_\rho\|)\) on the \(D_{\alpha+2}\) distance to the generator span. Equivalently \(\mathcal L_\rho\) separates \(f_0\) from the closure of \(\operatorname{span}\{R_k:k\ge2\}\) in \(W_{\alpha,c}\).

Consequently the printed approximation implies zero-freeness in the enlarged half-plane \(\Re s>t-c\). At \((-3,7/4)\), it would force zero-freeness in \(\Re s>1/4\), contrary to Hardy's critical-line theorem. The counterexample uses existence of one critical-line zero. [Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed. (1986), Ch. X §§10.1–10.2](../../sources/equivalence_round2/titchmarsh1986.pdf)

The target-closure transfer from ordinary \(D_{-3}\) to \(W_{-3,3/4}\) fails for the specific remainder span. The ordinary closure follows by applying the bounded operator \(T_1:D_{-1}\to D_{-3}\) to the unconditional Bergman approximation to 1, with images \(T_1(1)=-f_0\) and \(T_1(h_k)=R_k\). The weighted closure fails by the functional above. [Bergman approximation proof](../../proposals/independent_campaigns/noor_critical_bergman_advocate_round4.md)

An attempted transfer by bounded inverse on the full unweighted range could only detect the generally stronger range norm. The radial integral separates the arithmetic family itself. Dilation and boundary-cutoff ideas would need to preserve the same arithmetic span while evading this separation, which is impossible at the counterexample parameters. The stricter zero-free condition is necessary. Its converse in the remaining parameter regimes is a separate question. The assessment concerns only the stated direction of Theorem 5.5.

For the unconditional counterexample one can also use the Riemann–von Mangoldt count, which supplies a nontrivial zero, followed by the functional-equation symmetry \(\rho\mapsto 1-\overline\rho\), which supplies one with real part at least \(1/2\). A zero on the line itself is unnecessary. [Titchmarsh, Theorem 9.4 and §2.12](../../sources/equivalence_round2/titchmarsh1986.pdf)

## Source version and correction scope

Fresh renders from the local publisher PDF p. 26 and the local arXiv:2206.02654v6 PDF p. 21 were inspected visually. Both say “if and only if” for the same parameter intervals and threshold. The publisher PDF SHA-256 is 05615ae82b3d52e7591474859f774ae2244357c7986c592590129386beea26d4. The v6 PDF SHA-256 is 0cee802b54eb53f3b9a74c02bf2b636b414c5ed3efb0ddfb4c759d9d84959939. The staged arXiv abstract snapshot dated 2026-11-17 labels v6 the latest submission, last revised 5 June 2024. The publisher Version of Record was published online 29 January 2025. The staged Crossmark record dated 2026-11-17 says “Document is current” and lists zero updates, and the staged five-result Crossref title query returned the original publication and four unrelated titles. These snapshots bound the checked correction scope. [arXiv v6](https://arxiv.org/abs/2206.02654v6) [Version of Record](https://doi.org/10.1007/s11785-025-01661-2) [Crossmark](https://crossmark.crossref.org/dialog/?doi=10.1007%2Fs11785-025-01661-2)
