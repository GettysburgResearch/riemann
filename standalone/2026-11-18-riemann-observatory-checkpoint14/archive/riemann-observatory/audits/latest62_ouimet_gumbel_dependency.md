# Ouimet’s displaced-zeta Gumbel law and its analytic dependencies

17 November 2026. Targeted dependency audit of arXiv:2611.01905v1, a 60-page preprint. Actual source passages inspected in §§2–6 include assumptions and theorem, conditional height bins, annular localization, kernel averaging and factorial moments, continuum passage, quantile expansion, and the final zeta transfer. Followed the cited bridge and tail inputs into arXiv:2610.22821v1, a 128-page preprint, in §§3.1–3.2 and selected §§4.2–4.3 proofs. This scope leaves the records at Level 0. The claimed theorem is not being adopted as an independently certified frontier result.

## Exact result, probability, and displacement

Put \(t=\log\log T\), fix \(\theta>0,\ \varphi>7/2,\ \Phi>\varphi+1,\ C_\sigma>0\), and take deterministic \(X,\eta=\sigma-1/2\) satisfying (2.1)
\[
 T^{1/t^\Phi}\le X\le T^{1/t^\varphi},\quad
 0<\eta\le C_\sigma t^\Phi/\log T,\quad
 \eta\log X/t\longrightarrow\infty .
\]
Thus \(\sigma>1/2\) approaches the line, but the displacement obeys \(\eta\log T/t^{\varphi+1}\to\infty\). For example \(X=T^{1/t^4}\), \(\eta=c t^6/\log T\) meets the conditions for \(\varphi=4,\Phi=6,C_\sigma\ge c>0\). Neither \(\sigma=1/2\) nor a fixed numerator \(c/\log T\) in the displacement meets them.

Sample one \(\tau\) uniformly from \([T,2T]\). Set \(I_\theta=[-(\log T)^\theta,(\log T)^\theta]\), \(\ell_T=2\eta,\ s_T=\log(1/\ell_T),\ N_T=|I_\theta|/\ell_T\). The zeta quantity is the scalar
\[
 M_T^\zeta=\max_{h\in I_\theta}\log|\zeta(\sigma+i(\tau+h))|.
\]
This maximum is taken in one randomly translated window. At any zero in the window the extended log modulus is minus infinity, which is harmless for the maximum of the continuous modulus. The theorem is neither about all heights up to \(T\) nor a zero-spacing or point-process theorem.

For \(Q(s)=\sum_{p^j\le X}p^{-js}/j\), the arithmetic field \(F_h^A=\Re Q(\sigma+i(\tau+h))\) uses this same random \(\tau\). The Haar field \(F_h^H=\Re\sum_{p^j\le X}U_p^jp^{-j(\sigma+ih)}/j\) has independent uniform phases \(U_p\) indexed by primes, with the same phase to all its powers at that prime. It is an auxiliary probability law, not a Haar random matrix. The centering quantile solves \(N_T\mathbb P_H(F_0^H>u_T)=1\). Set \(m=\sqrt{1+\theta}\), \(\beta_c=2m\). Theorem 2.1 claims
\[
 \mathbb P(M_T^\zeta-u_T\le x)\longrightarrow
       \exp\{-\kappa_\theta e^{-\beta_c x}\},\qquad x\in\mathbb R,
\]
and the same limit separately for the maxima of \(F^A,F^H\). The constant is the positive finite limit of \(q^{-1}\mathbb P(D_\theta(qj)\le0\text{ for all }j\ne0)\) as \(q\downarrow0\), for the continuous Gaussian process in (2.8)–(2.9). Its covariance is \(\tfrac14\log((1+v^2)(1+w^2)/(1+(v-w)^2))\), and the drift is \(-\beta_c\log(1+v^2)/4\). The process limit in Lemma 3.3 is conditional on high bins and in \(C([-R,R])\) for each fixed microscopic \(R\), for the Euler and Haar fields. The main theorem is a scalar distributional limit for their continuum maxima and the zeta maximum. It does not assert global convergence of the unconditioned zeta field to a Gaussian process.

## Rare-event comparison and continuum dependencies

- Prior [35] Lemma 4.4 concerns a fixed number of prime-power linear forms with coefficients bounded by \(C_0p^{-j/2}\), bounded real transform parameters and imaginary parts at most \(t^{\epsilon_0/2}\), \(0<\epsilon_0<1/4\). Arithmetic truncation is at \(t^{1+\epsilon_0}\). The absolute transform and exceptional errors are exponentially small as \(\exp(-ct^{1+2\epsilon_0}+Ct)\). The proof truncates the Taylor expansion at \(\lfloor t^2\rfloor\) and uses comparison lengths \(X^{4\lfloor t^2\rfloor}=T^{o(1)}\). That makes the comparison effective relative to a fixed number of high roots with probability \(e^{-O(t)}\). The coefficients of field evaluations, increments, and the scaled derivative \(\ell_T F'(h)\) obey the bound uniformly. For the derivative it follows from \(2x e^{-x}=O(1)\) at \(x=j\eta\log p\), after extracting \(p^{-j/2}/j\). There is no assertion of transform comparison at a growing dimension of order \(N_T\).
- New Lemmas 3.1–3.3 use positive Haar tilting, then a Fourier majorant/minorant for height bins from prior Lemma 4.6. The root condition is a fixed positive separation, finite number of roots, bins of fixed positive minimum width inside a fixed bounded height band, and fixed microscopic neighborhoods within \(I_\theta\). The tilted Gaussian limit is supplemented by the bound \(C_\xi\exp(-ct\|\omega\|^2)\) in (3.23) over the Fourier cube. It is the latter estimate plus the bin smoothing that gives the *relative* joint bin asymptotic \(N_T^{-k}K_T(\boldsymbol h)\bigl(\prod_i\Theta(J_i)+o(1)\bigr)\), uniformly under those conditions. Formula (3.40) makes comparison of the arithmetic error against that scale explicit. Lemma 3.3 adds conditional path tightness using derivative bounds. A Selberg CLT or unconditioned finite-dimensional normality alone would give none of these relative or path estimates.
- New Lemmas 3.5–3.7 localize competitors from \(\ell_T R\) to order-one distance, under several separated height-bin conditions. On an annulus of radius \(d=\ell_T e^r\) the conditional drift of the root's upper part has size at least \(m_-r\) for fixed \(1<m_-<m\), up to \(O(1)\) for \(d\le t^{-3}\) and \(O(\log t)\) above that. Precisely the latter regime has \(r\asymp t\), allowing absorption. Conditional Laplace/derivative estimates and Hölder against the number of cells yield the negative exponent in (3.79) by taking \(a>0\) small. The common arithmetic exceptional event, rather than an event per cell, is what retains the uniform error after annular summation. This logic uses \(\theta>0\) through the strictly positive drift margin.
- New Lemma 4.1 averages the separated kernel over \(I_\theta^k\). The cited high-prime contribution above \(\exp(t^3)\) is pointwise small for fixed separation by PNT partial summation, and the middle-prime mean square is \(O(P^{-1}+\log t/|I_\theta|)\), \(P=t^B\). One chooses \(B\) after the polynomial height loss in exponentiating the kernel. The low-prime normalized exponential is asymptotically spatially averaged in every fixed \(L^r\) over phases, using (4.109) of [35]. This is an averaged result and does not replace the joint kernel by one at each separated tuple. Random trimming and independent offsets in each block turn sums over maximizer candidates into spatial integrals. Proposition 4.3 uses the relative bin estimates and localization for fixed order \(k\), fixed mesh \(q\), fixed height band and positive trimming. Proposition 4.4 applies finite Bonferroni and subsequently removes the trimming and upper height cap. No growing-order factorial moment comparison is required.
- Lemmas 5.1–5.2 control mesh misses near a fixed high level and small omitted spatial sets. Proposition 5.4 uses (5.43) to squeeze subsequential grid constants, taking \(T\to\infty\), vanishing trimming, then \(q\downarrow0\) and the fixed height slack down to zero. The positivity of \(\kappa_\theta\) is not a Gaussian comparison assumption. In the written proof it goes through lower tightness in Lemma 5.3, which depends on [35] Corollary 4.15. That corollary depends on critical-temperature mass spreading in [35] Proposition 4.14, via a fixed band \([-L,0]\) before exhausting \(L\). The latter uses one-point means, separated-kernel averaging and a truncated fractional-moment control (4.198) of near cells. This is a key upstream dependency to audit before independently certifying the law. The scalar upper tail in [35] (4.82) is another dependency for removing the high cap and bounding the grid constant. These are proved estimates claimed in the cited preprint, not postulated facts in Theorem 2.1.

## Actual zeta transfer

The reliance on the earlier preprint is explicit in new (6.26). Its [35] Proposition 3.3 (3.8) claims the exact uniform approximation
\[
 \sup_{h\in I_\theta}|\log|\zeta(\sigma+i(\tau+h))|-F_h^A|
 =o_{\mathbb P}(1).
\]
It uses the same parameters, random \(\tau\) and sharp prime-power cutoff, with no requirement on RH. I reconstructed the main inequalities of the bridge. A random rectangle from \(\Re s>1/2+\eta/4\), enclosing all shifts and a contour buffer of order \(\log T\), has a probability of failure \( \ll \exp(-\eta\log T/3+O_\theta(t))\) by Ingham's density bound and a union bound over zeros. In fact the exponent in the density count at \(1/2+\eta/4\) is \(1-\eta/(3-\eta/2)\). On the good event, the analytic logarithm anchored in absolute convergence is bounded by \(O((\log T)/\eta)\) to the right of \(1/2+\eta/2\) using Borel–Carathéodory. The Gaussian Mellin smoothing \(e^{w^2}X^w/w\), shifted to \(\Re w=-\eta/2\), produces a uniform \(O(\exp(-\eta\log X/2+O_\theta(t)))\) contour error. Removing this smoothing uses the Gaussian decay of the coefficients away from the cutoff, Montgomery–Vaughan mean square for the difference and its derivative, and a deterministic one-dimensional supremum bound. Prior Lemma 3.7's expected squared spatial supremum is at most \(\exp(-2\eta\log X+O_\theta(t))\). Both comparison errors vanish because \(\eta\log X/t\to\infty\). The exceptional rectangle bound tends to zero. No assertion of an everywhere zero-free strip is needed. The prior unconditional pointwise \(L^2\) comparison (3.9) uses a further fourth-moment exceptional-event bound, which is not needed for the maximum's Slutsky transfer.

Consequently, conditional on the audited-scope model extrema estimates, the final inequality \(|M_T^\zeta-M_T^A|\le\sup|\log|\zeta|-F^A|\) gives a genuine arithmetic maximum limit, not an identification by analogy. The displacement is precisely what allows this approximation over the expanding interval. There is no indication that the proof reaches the line by continuity in \(\sigma\).

## Quantile normalization check

From the prior scalar tilted tail estimate locally uniform in \(v/s_T>0\), and the new cumulant correction \(a(m)>0\), the quantile equation yields
\[
 u_T=\sqrt{s_T\log N_T}
   -\frac{\log(4\pi\log N_T)-2\log a(m)}{4m}+o(1).
\]
Here \(a(z)=\prod_p(1-p^{-1})^{z^2}\sum_{j\ge0}(z)_j^2/(j!^2p^j)\). The radius convention matters: \(\log N_T=s_T+\theta t+\log 2\). The \(\log 2\) expansion cancels the factor 2 in the alternative constant \(\log(a(m)/(2m\sqrt\pi))/(2m)\). For \(\eta=c t^A/\log T\) satisfying (2.1), the coefficient of \(\log t\) is \(-[2A(2+\theta)+1]/(4m)\), as in (2.12), distinct from the critical-line prediction.

The dependency check found no hidden RH assumption or direct conflation between Haar and zeta. It does not certify the entire multiscale proof, particularly the strong relative extremal tail and fractional-moment estimates in the long precursor, and makes no publication or priority determination.

- [November v1 primary PDF](https://arxiv.org/pdf/2611.01905v1). Private `sources/latest62_statistics/law2026.pdf`, SHA-256 `9429bc025f32ea954a9f2de78c7ee4097ded8dfea45ec07d9577bc9866d6d861`.
- [October precursor [35], v1 primary PDF](https://arxiv.org/pdf/2610.22821v1). Private `sources/latest62_statistics/ouimet_poisson.pdf`, SHA-256 `26219949e580c3c41ce081370ed9e97582d10e4d6b0f04b6679af9b97cef912a`.
