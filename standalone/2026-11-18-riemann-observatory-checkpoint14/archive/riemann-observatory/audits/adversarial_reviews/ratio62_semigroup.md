# Independent spectrum and domain check for the \(\xi\)-weighted translation

2026-11-17. Assume RH. Let \(F(w)=\xi(1/2+w)\), \(H_t(w)=F(w)/F(w+t)\), and \(W_tf(w)=H_t(w)f(w+t)\) on the right-half-plane \(H^2\). I obtain a strongly continuous contraction semigroup with every \(W_t\), \(t>0\), injective, compact and quasinilpotent. Its actual generator has empty spectrum. This is conditional and concerns this specific weighted translation on this Hardy space. Priority for the \(\xi\) application remains unassessed.

## Semigroup and maximal generator

Use the Hardy norm \(\|f\|^2=\int_{\mathbb R}|f(iu)|^2\,du\). Under RH the paired product or the [Lagarias–Suzuki positive-real logarithmic derivative](ratio62_herglotzpriority.md) gives \(\Re (F'/F)(w)\ge0\) on the open half-plane. Thus \(F\) has no zeros there and
\[
H_t(w)=\exp\!\left(-\int_0^t (F'/F)(w+r)\,dr\right),\qquad |H_t|\le1.
\]
The cocycle identity \(H_{s+t}(w)=H_s(w)H_t(w+s)\) makes \(W_{s+t}=W_sW_t\). Right translation \(C_tf(w)=f(w+t)\) is a strongly continuous contraction, for example from the Paley–Wiener model where it multiplies the Laplace-side function by \(e^{-tu}\) for \(u\ge0\). Since multiplication by \(H_t\) contracts, \(\|W_t\|\le1\). For every boundary ordinate away from the countable zero set, \(H_t(iu)\to1\) as \(t\downarrow0\). Bounded convergence against \(|f(iu)|^2\,du\) gives \((H_t-1)f\to0\) in \(H^2\). With \(W_tf-f=H_t(C_tf-f)+(H_t-1)f\), this proves strong continuity. It is \(W_t\) that is the operator semigroup, while \(H_t\) is the scalar cocycle.

Put \(G=F'/F\). The exact domain and action are
\[
D(A)=\{f\in H^2:f'-Gf\in H^2\}, \qquad Af=f'-Gf.
\]
For necessity, evaluate a converging generator difference quotient at any interior point. Bounded point evaluation and the pointwise product rule give \(Af(w)=f'(w)-G(w)f(w)\). For sufficiency take \(h=f'-Gf\in H^2\). Differentiating \(W_sf(w)\) in real \(s\) gives \(W_sh(w)\). Integrate that scalar derivative and use bounded evaluation to identify \(W_tf-f=\int_0^t W_s h\,ds\) with the \(H^2\)-valued Bochner integral. Thus the norm derivative at zero is \(h\). This proof permits cancellation in \(f'-Gf\) and never requires \(f'\) and \(Gf\) separately to belong to \(H^2\).

## Compactness at each fixed positive time

The zeta-completion quotient on \(s=1/2+iu\) is
\[
H_t(iu)=\frac{s(s-1)}{(s+t)(s+t-1)}\,
       \pi^{t/2}\frac{\Gamma(s/2)}{\Gamma((s+t)/2)}
       \frac{\zeta(s)}{\zeta(s+t)}.
\]
For fixed \(t>0\) the polynomial ratio is bounded at large \(|u|\). Vertical Stirling gives a factor \(O_t((1+|u|)^{-t/2})\). On RH, the critical-line Lindelöf bound and the fixed-distance Littlewood reciprocal bound give \(\zeta(s)=O_\eta((1+|u|)^\eta)\) and \(1/\zeta(s+t)=O_{t,\eta}((1+|u|)^\eta)\) for every \(\eta>0\). If \(t>1/2\), absolute convergence of the reciprocal Dirichlet series suffices for the second bound. Use \(\eta<t/4\). This proves \(H_t(iu)\to0\) uniformly as \(|u|\to\infty\), with constants allowed to depend on the fixed time. No near-critical uniformity in \(t\) is used.

Regard \(W_t\) as mapping into boundary \(L^2(du)\). The part of its output supported on \([-R,R]\) is Hilbert–Schmidt, since \(\|{\rm ev}_{t+iu}\|^2=(4\pi t)^{-1}\). Indeed Parseval in an orthonormal basis followed by Tonelli gives squared Hilbert–Schmidt norm
\[
\int_{-R}^R |H_t(iu)|^2\,\|{\rm ev}_{t+iu}\|^2du<\infty.
\]
The remainder is bounded in operator norm by \(\sup_{|u|>R}|H_t(iu)|\), because \(C_t\) is a contraction. Thus the boundary map is compact. Its range is contained in the closed Hardy boundary subspace, so \(W_t\) is compact as an \(H^2\)-valued operator. The cutoff maps themselves need not have Hardy range.

## Spectra and entire resolvent

On the open half-plane \(H_t\) never vanishes. If \(W_tf=0\), then \(f(w+t)=0\) everywhere and analytic uniqueness gives \(f=0\). Suppose \(W_tf=\lambda f\) for \(\lambda\ne0\). For any \(w\) with \(f(w)\ne0\), iteration gives
\[
f(w+nt)=\lambda^n\frac{F(w+nt)}{F(w)} f(w).
\]
At fixed \(\Im w\), Stirling in the positive real direction and \(\zeta(1/2+w+nt)\to1\) show \(\log|F(w+nt)|=(nt/2)\log(nt)+O_w(nt)\). This dominates any exponential \(|\lambda|^n\). Bounded point evaluation instead gives \(|f(w+nt)|\ll(\Re w+nt)^{-1/2}\|f\|\). Hence no nonzero eigenvalues occur. The Riesz–Schauder theorem gives \(\sigma(W_t)=\{0\}\), with zero in the spectrum since an invertible compact operator cannot act on this infinite-dimensional space. In particular \(W_t\) is neither a nonzero nilpotent nor an invertible operator.

Fix one positive \(t_0\). The spectral radius formula applied to \(W_{t_0}\) gives \(\|W_{nt_0}\|\le C_b e^{-bnt_0}\) for every \(b>0\). Contractivity for the intervening times extends it to \(\|W_t\|\le C'_b e^{-bt}\). Therefore
\[
R(z)=\int_0^\infty e^{-zt}W_t\,dt
\]
is defined by the strong integral, with the tails converging in operator norm for all \(z\in\mathbb C\) and is entire. To check that it is the resolvent for every \(z\), use the time-shift identity for \(W_hR(z)\). It gives \(\lim_{h\downarrow0}h^{-1}(W_hR(z)f-R(z)f)=zR(z)f-f\), so \((zI-A)R(z)f=f\). Conversely for \(f\in D(A)\), differentiate \(e^{-zt}W_tf\) in \(H^2\), integrate, and use the decay at infinity to give \(R(z)(zI-A)f=f\). This proves \(\sigma(A)=\varnothing\), with no appeal to a converse spectral mapping theorem. The argument rules out this specific candidate as an operator with the ordinates in its spectrum. It makes no assertion about other Hilbert–Pólya constructions. The Hadamard product provides a conditional multiplier and no proof of RH.

## Quantitative time decay and the Hardy kernel test

There is also a direct two-sided estimate:
\[
\log\|W_t\|=-\tfrac12t\log t+\tfrac12(1+\log(2\pi))t+O(\log t),\qquad t\to\infty.
\]
For the upper bound, the formula for \(G\), the absolutely convergent Dirichlet series for \(\zeta'/\zeta\), and uniform complex Stirling in the right half-plane give, for \(r\ge2\) and all real \(u\),
\[
\Re G(r+iu)=\tfrac12\log\bigl(|r+1/2+iu|/(2\pi)\bigr)+O(1/r).
\]
In fact the polynomial logarithmic derivatives are \(O(1/r)\), the digamma error is \(O(1/r)\), and the \(\zeta'/\zeta\) tail decays exponentially in \(r\). Integrate the lower bound \(\Re G(r+iu)\ge\frac12\log(r/(2\pi))-C/r\) from 2 to \(t\). Since \(|H_2(iu)|\le1\), the cocycle shows that this estimate bounds \(H_t(iu)\) uniformly for all \(u\), and hence bounds the operator norm. For the lower bound use the weighted-composition adjoint on the reproducing kernel at fixed \(x>0\), giving \(\|W_t\|\ge |H_t(x)|\sqrt{x/(x+t)}\). Positive-real Stirling yields the stated lower bound up to \(O_x(\log t)\).

For the normalized kernel \(k_x(w)=\sqrt{x/\pi}/(w+x)\), the reverse triangle inequality and \(\|k_x(\cdot+\epsilon)-k_x\|_2=O(\epsilon)\) identify the squared displacement slope with the [general Herglotz Poisson-energy slope](herglotz_atomic_energy_rt62_herglotz.md). Under RH the representing masses are \(m_\gamma\) at the ordinates and the infinity mass coefficient is zero. Every summand for a positive mass is positive, and there are nontrivial zeros, so this slope is positive. Thus each \(k_x\) fails the generator-domain norm-derivative test. There is also a direct local proof using the exact domain: near a boundary zero \(i\gamma\), \(G(w)=m_\gamma/(w-i\gamma)+O(1)\) and \(k_x(i\gamma)\ne0\), so \(k'_x-Gk_x\) has a nonremovable simple pole. Its squared integral along a vertical line \(\Re w=\delta\) diverges at least as a positive multiple of \(1/\delta\) as \(\delta\downarrow0\). Neither proof says the domain is not dense. A dense domain for the \(C_0\)-semigroup generator need not contain the reproducing kernels.

## Classical antecedents and limits of the comparison

- [Burnol, arXiv:math/0202166, Theorems 1.3 and 3.1](https://arxiv.org/pdf/math/0202166) already proves the fixed-shift bound \(O_\eta(|s|^\eta)\) for the uncompleted critical-line quotient under RH. Combined with Stirling it is an alternative direct source for the compactness tail.
- [Gallardo–Gutiérrez, Siskakis and Yakubovich, arXiv:2110.05247, Theorem 2.1](https://arxiv.org/pdf/2110.05247) gives the corresponding maximal weighted-composition domain and cocycle formula in disk spaces. The half-plane proof above gives the same domain directly and does not need an unstated unitary-identification step.
- [Chalendar and Partington, arXiv:2212.02172, §2, Theorem 2.2 and (2.7)](https://arxiv.org/pdf/2212.02172) identify compact weighted composition with compactness of the corresponding half-plane Carleson embedding and emphasize treatment of infinity. Here the associated measure lies on \(t+i\mathbb R\) with density \(|H_t(iu)|^2du\), so the half-plane small-box test by itself is vacuous. The proof by cutoff and Hilbert–Schmidt approximation directly shows the decay at infinity needed for compactness. Their comparison case \(h=1,\ \phi(w)=w+1\) is expressly noncompact. [Kucik, arXiv:1610.00485, Theorem 6](https://arxiv.org/pdf/1610.00485) concerns composition without the weight.
- [Avicou, Chalendar and Partington, accepted manuscript, Theorem 3.2 and §4](https://eprints.whiterose.ac.uk/id/eprint/93689/1/holo-semigroup-jmaa-final.pdf) records the classical compact-resolvent criterion and related half-plane generator results for unweighted composition. The resolvent here is itself compact. For \(t>0\), \(W_t\) is norm-continuous as a function of \(t\): for a fixed \(t_1>0\), factor \(W_t=W_{t-t_1/2}W_{t_1/2}\) near \(t_1\), and use that strongly convergent uniformly bounded operators converge uniformly on compact subsets after applying the fixed compact factor. The resolvent integral restricted to a compact positive-time interval is therefore a norm limit of compact finite sums, and the tails at zero and infinity are small in operator norm. This is consistent with the standard criterion.
- [Manzur, Noor and Santos, arXiv:2111.05398v2](https://arxiv.org/pdf/2111.05398) study a distinct discrete RH-related weighted composition semigroup on the disk, indexed multiplicatively, \(f(z)\mapsto(1+\cdots+z^{n-1})f(z^n)\). Their invariant spaces and cyclic vectors are not spectral results for the \(\xi\)-ratio horizontal translation.
- [Callewaert, Neyt and Vindas, arXiv:2507.20376, §1 and main theorem](https://arxiv.org/pdf/2507.20376) construct left-translation semigroups on a different Banach space and show that empty generator spectrum alone does not quantify semi-uniform decay. The present decay conclusion uses the positive-time operators' spectral radius, or the explicit \(\xi\) quotient estimate, and does not reverse the general implication.

The primary-source [retrieval and version hashes](../../sources/ratio62_semigroup/retrieval.tsv) and the companion [Herglotz priority note](ratio62_herglotzpriority.md) identify the comparisons. The searches found established general methods and examples with empty spectrum. No checked source was found applying the same combination to this specific completion-weighted semigroup. That limited result does not settle historical priority.
