# Whole-work reconstruction of Nakamura–Suzuki, arXiv v1

18 November 2026. This audit covers the full five-page primary arXiv text of Takashi Nakamura and Masatoshi Suzuki, *On infinitely divisible distributions related to the Riemann hypothesis*, PAPER-SM63-POS-040. The inspected PDF has SHA-256 `756288c39bfd743f08f24b1e5074bb8a4adbe8a959d42edd763af07678801830`. The argument is reconstructed below by complete passage coverage, with external inputs and two convergence qualifications stated explicitly. [Primary arXiv v1](https://arxiv.org/pdf/2306.08317v1) · [Corpus source and reading entry](../../papers/suzuki_model63_positivity_notes.md)

## Coverage ledger

| Pages and loci | Mathematical content and coverage |
|---|---|
| p. 1, abstract and §1, (1.1) | Dirichlet series, meromorphic continuation, entire completion, the rotated zero coordinate and the RH equivalence. See §1 below. |
| p. 1, §1, (1.2)–(1.4) | Definition of infinite divisibility, Fourier convention, Gaussian parameter, drift and Lévy conditions, and finite small-jump variation. See §1. |
| p. 2, §1, (1.5)–(1.7), Theorems 1.1–1.2 | Arithmetic formula, endpoint convention, precise statement of both theorems, nonrepeated zero index with multiplicities, and unconditional zero-sum identity. See §§2–5. |
| pp. 2–3, end of §1 | Euler-product compound Poisson law, completely multiplicative extension, distinction from the completed-xi distribution and the older signed-measure criterion, and the role of the logarithmic derivative. See §2. |
| p. 3, §2, Lemma 2.1, (2.1), forward implication | Zero strip, convergent inverse powers, central nonvanishing, reflection and conjugation, compound Poisson construction and triplet. See §§3–4. |
| pp. 3–4, §2, Lemma 2.2, (2.2)–(2.4) | Genus-one factorization, normal convergence, elimination of exponential drift in the entire factorization, one-term transform and its domain, infinite sum/interchange. See §3. |
| p. 4, §2, reverse implication | Real logarithm, modulus bound, fixed-sign Laplace singularity, positive real nonvanishing of ξ, pole exclusion with multiplicities and reflection. See §4. |
| pp. 4–5, §3, (3.1)–(3.2) | Completion derivative, polar, linear and shifted-prime transforms, endpoint and Fubini controls, Hurwitz–Lerch summation, digamma identity, and weighted Fourier uniqueness. See §5. |
| p. 5, acknowledgments and references [1]–[10] | Acknowledgments have no proof role. Reference dependencies and what was checked are recorded in §6. |

## 1. Normalizations and probability preliminaries

Equation (1.1) sets
$$
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad E(z)=\xi(1/2-iz).
$$
Here $\zeta(s)$ is the absolutely convergent Dirichlet series for $\operatorname{Re}s>1$, then its meromorphic continuation with a simple pole at $s=1$. Entireness of $\xi$ uses cancellation at $s=0,1$ and at the negative even integers, in addition to the absence of further poles. The nontrivial zeros of $\zeta$ are the zeros of $\xi$, with multiplicity. The coordinate $s=1/2-iz$ turns the critical line into the real $z$-axis. The facts about $\xi$ required below are order one, the functional equation, real conjugation symmetry, the zero strip, and nonvanishing on the real axis. Reference [9] supplies the classical analytic zeta facts. In particular, the positivity used at real $0<s<1$ follows from the alternating eta series, which has positive sum, and $\zeta(s)=\eta(s)/(1-2^{1-s})<0$. Since $s(s-1)<0$ and the gamma and power factors are positive, $\xi(s)>0$. For real $s>1$, positivity follows from the Dirichlet series. The value at $s=1$ is $1/2$ by the residue, and reflection gives the real nonvanishing for $s\le0$. This supplies both the central value and the whole positive-axis condition needed in the proof. Complex conjugation symmetry extends from the real coefficients on the Dirichlet-series half-plane by continuation.

The paper uses $\widehat\mu(t)=\int e^{itx}\mu(dx)$. Infinite divisibility means the existence of a probability convolution root of every positive integer order. Its convention in (1.2) uses the truncation $h(\lambda)=\lambda/(1+\lambda^2)$ and the exponent
$$
-\tfrac12 a t^2+ibt+\int_{\mathbb R}
 (e^{it\lambda}-1-it h(\lambda))\,\nu(d\lambda),
$$
with Gaussian variance parameter $a\ge0$, real drift $b$, and positive Lévy measure $\nu$ satisfying $\nu(\{0\})=0$ and $\int(1\wedge\lambda^2)\,d\nu<\infty$ in (1.3). The subtracted linear term makes the integrand $O_t(\lambda^2)$ at zero. Large jumps have finite mass and the integrand is bounded on their range. If also $\int_{|\lambda|\le1}|\lambda|\,d\nu<\infty$, then $\int |h|\,d\nu<\infty$ and (1.4) removes the truncation with $b_0=b-\int h\,d\nu$. This small-jump condition does not assert a finite first absolute moment over all $\lambda$. References [7, Theorem 8.1, Remark 8.4 and (8.7)] supply the Lévy–Khintchine theorem and the convention change.

## 2. Arithmetic exponent and the prior probabilistic statements

For $t\ge0$, (1.5) defines $g_\zeta$ as the sum of four real terms
$$
-4(e^{t/2}+e^{-t/2}-2),\quad
\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n),\quad
-\tfrac t2(\psi(1/4)-\log\pi),\quad
\tfrac14\left[e^{-t/2}\Phi(e^{-2t},2,1/4)-\Phi(1,2,1/4)\right].
$$
Extend evenly to negative $t$. Here $\Lambda(p^r)=\log p$ for primes and integers $r\ge1$, $\Lambda$ otherwise vanishes, $\psi=\Gamma'/\Gamma$, and $\Phi(u,s,a)=\sum_{n\ge0}(n+a)^{-s}u^n$ is used only at $s=2$, $a=1/4$, $0<u\le1$. The Lerch endpoint at $u=1$ is absolutely summable. The prime sum is finite locally and a newly included term vanishes at $t=\log n$, so its endpoint convention causes no jump. Thus $g_\zeta$ is continuous and $g_\zeta(0)=0$. The paper credits [8, (1.1), (1.3), (1.8)] for its introduction in connection with Weil and Li criteria, and [8, Theorem 1.1(2)] for (1.7). Its own appendix proves (1.7) independently of [8].

The context paragraph has a different measure. For $\sigma>1$ the Euler product gives
$$
\frac{\zeta(\sigma+it)}{\zeta(\sigma)}
=\exp\left(\sum_{p,r\ge1}\frac{p^{-r\sigma}}{r}(e^{-itr\log p}-1)\right).
$$
The sum is absolutely convergent and defines a finite Lévy measure at $-r\log p$. The factor $1/r$ is present in the rendered v1 PDF. It can be lost in text extraction. This proves the stated compound Poisson assertion and identifies [2, Example 17.6] as background. For a normalized, absolutely convergent Dirichlet series with completely multiplicative nonnegative coefficients $c(n)$, the same mechanism replaces $p^{-r\sigma}$ by $(c(p)p^{-\sigma})^r$. Absolute convergence gives $c(p)p^{-\sigma}<1$ for each $p$ and summability over primes, so the local log expansions sum. The nonzero coefficient at $n\ge2$ in the cited statement makes the distribution nontrivial. The text attributes this generalization to [5, Theorem 2].

References [1] and [3] are related examples or surveys. Reference [6] gives an earlier criterion for the separate characteristic function $\xi(\sigma+it)/\xi(\sigma)$ for every $1/2<\sigma<1$, involving a pretended-infinitely divisible signed-measure representation. Reflection $t\mapsto-t$ reconciles the sign convention of the formula in [6]. This context uses neither a positive finite Lévy measure for that representation nor the identical exponent of (1.5). The present work proceeds through the logarithmic derivative in Lemma 2.2.

## 3. The zero sum and the transform of its spectral side

Let $\gamma$ run over distinct zeros of $E$, with multiplicities $m_\gamma$. The strip $|\operatorname{Im}\gamma|\le1/2$ follows from the critical strip and the chosen coordinate. The order-one bound implies $\sum_\gamma m_\gamma|\gamma|^{-\alpha}<\infty$ for every $\alpha>1$. For example Jensen's formula and order one give $n(r)=O_\eta(r^{1+\eta})$ for every $\eta>0$, and partial summation applies for $1+\eta<\alpha$. Central nonvanishing excludes $\gamma=0$. For $t$ on a compact real interval the factor $|e^{-i\gamma t}-1|$ is uniformly bounded by $e^{|t|/2}+1$, giving Lemma 2.1 by the inverse-square sum.

Define the spectral side of (1.7) provisionally by $G(t)=\sum_\gamma m_\gamma(e^{-i\gamma t}-1)/\gamma^2$. The functional equation $\xi(s)=\xi(1-s)$ in (2.1) makes $E$ even and gives $\gamma\mapsto-\gamma$ with unchanged multiplicity. Conjugation for $\xi$ gives $E(\bar z)=\overline{E(z)}$ using evenness, and hence $\gamma\mapsto\bar\gamma$. Reflection gives $G(-t)=G(t)$ and conjugation gives $\overline{G(t)}=G(-t)$. This supplies the full reality argument behind the discussion after Lemma 2.1.

Hadamard factorization with order one and $E(0)\ne0$ gives $E(z)=e^{a_1+b_1 z}\prod_\gamma[(1-z/\gamma)e^{z/\gamma}]^{m_\gamma}$. These constants are separate from the probability parameters. Its logarithmic derivative yields (2.3) with the factor $i$ from $E'(z)=-i\xi'(1/2-iz)$. The series of $1/(z-\gamma)+1/\gamma$ is normally convergent away from its poles because the combined terms are $O_K(|\gamma|^{-2})$ on compact $K$ as $|\gamma|\to\infty$. At $z=0$ each term vanishes. Differentiating (2.1) away from zeros gives (2.4), so at $s=1/2$ the finite logarithmic derivative is zero. Thus $b_1=0$.

For each zero the separate exponential and constant integrals are both absolutely convergent for $\operatorname{Im}z>\max(0,\operatorname{Im}\gamma)$, and give
$$
\int_0^\infty\frac{e^{-i\gamma t}-1}{\gamma^2}e^{izt}\,dt
=\frac{i}{\gamma^2}\left(\frac1{z-\gamma}-\frac1z\right)
=\frac{i}{z^2}\left(\frac1{z-\gamma}+\frac1\gamma\right).
$$
The printed auxiliary line on p. 4 lists only $\operatorname{Im}z>\operatorname{Im}\gamma$. The constant term also requires positive damping if $\operatorname{Im}\gamma<0$. This qualification leaves the applied half-plane $\operatorname{Im}z>1/2$ unchanged. For example the test values $\gamma=-i/4$ and $z=-i/8$ satisfy the printed condition but make the integral diverge for the corresponding model term. The test values are a check of the integral formula’s domain, without identifying either value as a zeta zero.

For the infinite sum on $\operatorname{Im}z>1/2$, the integrable absolute majorant is $(e^{t/2}+1)e^{-(\operatorname{Im}z)t}\sum m_\gamma/|\gamma|^2$. Compact uniform convergence in Lemma 2.1 alone would not control the entire integration range. The same strip argument gives the global majorant. It follows that the one-sided transform of $G$ is $z^{-2}(\xi'/\xi)(1/2-iz)$, giving Lemma 2.2 once §5 identifies $G=g_\zeta$. This order of proof avoids using (1.7) circularly.

## 4. Both implications and the precise Lévy measure

Under RH all $\gamma$ are real and nonzero. In (1.6) the mass $m_\gamma/\gamma^2>0$ belongs at $-\gamma$ because the characteristic convention uses $e^{it\lambda}$. Including both signs already accounts for all zeros. The measure has no zero atom and total mass $v=\sum m_\gamma/\gamma^2<\infty$. Consequently it satisfies (1.3) and finite small-jump variation. By (1.7), the exponent is $\int(e^{it\lambda}-1)\,d\nu_\zeta$ with exactly zero Gaussian term and untruncated drift, $(a,b_0,\nu)=(0,0,\nu_\zeta)$. For the truncation of (1.2), symmetry and absolute integrability of $h$ give $\int h\,d\nu_\zeta=0$, so $b$ is also zero. A direct construction is a Poisson number of independent jumps of law $\nu_\zeta/v$, with rate $v$, or the point mass at zero if $v=0$. The transform is $\exp(g_\zeta)$ and division of the intensity by each positive integer gives a convolution root. This proves the forward direction of Theorem 1.1, the compound Poisson designation in Theorem 1.2, and the claimed triplet. Sato's uniqueness theorem also identifies the triplet for the stated truncation.

For the reverse direction it is enough that $e^{g_\zeta}$ is a characteristic function of a real-line probability. The arithmetic exponent is real and even, its exponential is strictly positive, and the characteristic-function bound gives $g_\zeta\le0$. Infinitely divisible structure is used in the theorem's forward construction. It is not needed for this converse. The paper also explains that evenness of the transform removes its sine part under the representation.

Let $h(t)=-g_\zeta(t)\ge0$ for $t\ge0$ and $L(w)=\int_0^\infty h(t)e^{-wt}\,dt$. Put $w=-iz$. The global bound in §3 gives initial absolute convergence for $\operatorname{Re}w>1/2$. The real convergence abscissa $b$ is therefore at most $1/2$, possibly $-\infty$. On any right half-plane $\operatorname{Re}w>b$, a slightly smaller real damping value in the convergence range gives local domination and holomorphy. If $b>0$, the fixed-sign singularity theorem [10, Chapter II, Theorem 5b] forces a singularity at the real point $w=b$. A direct proof of the needed form uses a point $w_0>b$ sufficiently close to $b$ in any presumed neighborhood of analyticity. The Taylor series in $w_0-w$ has nonnegative coefficients $\int t^j h(t)e^{-w_0t}\,dt/j!$. Analyticity through $b$ makes this series converge for some real $w<b$, and monotone convergence then gives a finite integral there, a contradiction.

Lemma 2.2 identifies $L(w)=-z^{-2}\xi'(1/2-iz)/\xi(1/2-iz)$ initially for $\operatorname{Re}w>1/2$, with $z=iw$. Along real $w>0$ the argument to $\xi$ is $1/2+w$, where $\xi$ is nonzero, and $z\ne0$. The same quotient extends analytically around every point of that ray. Continuation along the ray gives analytic extension at any putative $b>0$, which is impossible by the fixed-sign theorem. Hence the transform of $g_\zeta$ is holomorphic on $\operatorname{Im}z>0$. The initial identity can now be multiplied by $z^2 E(z)$ and continued as an identity of holomorphic functions on the connected upper half-plane. At an upper-half-plane zero of $E$ of order $m$, the left-hand side vanishes to order at least $m$ and the right-hand side $iE'(z)$ to order exactly $m-1$. Thus no upper-half-plane zero exists. Evenness excludes the lower half-plane. This completes Theorem 1.1 with all multiplicities allowed.

## 5. Appendix calculations and identification of the two sides

Write $w=-iz$, $s=1/2+w$. For $\operatorname{Re}w>1/2$ one has $\operatorname{Re}s>1$. The Euler product logarithmic derivative is $\zeta'/\zeta(s)=-\sum_{n\ge2}\Lambda(n)n^{-s}$ there, absolutely convergent. Differentiating (1.1) gives
$$
\frac{\xi'}{\xi}(s)=\frac1{s-1}+\frac1s-\tfrac12\log\pi+\tfrac12\psi(s/2)
-\sum_{n\ge2}\Lambda(n)n^{-s}.
$$

- **Polar terms, p. 4.** Transforming $-4(e^{t/2}+e^{-t/2}-2)$ gives $-4[(s-1)^{-1}+s^{-1}-2/w]$. This equals $z^{-2}[(s-1)^{-1}+s^{-1}]$ using $z^2=-w^2$ and $s=w+1/2$. Integration is absolute for $\operatorname{Re}w>1/2$.
- **Linear term, p. 4.** $\int_0^\infty t e^{izt}\,dt=w^{-2}=-z^{-2}$ for $\operatorname{Re}w>0$. The coefficient $-\tfrac12(\psi(1/4)-\log\pi)$ then contributes $z^{-2}(\psi(1/4)-\log\pi)/2$.
- **Shifted primes, p. 4 through top of p. 5.** The lower endpoint is exactly $\log n$. A change of variables gives $\int_{\log n}^\infty (t-\log n)e^{izt}dt/\sqrt n=w^{-2} n^{-s}=-z^{-2}n^{-s}$. This single-term calculation needs $\operatorname{Re}w>0$. Interchange for the prime sum is valid for $b=\operatorname{Re}w>1/2$ because the summed absolute integral equals $b^{-2}\sum_{n\ge2}\Lambda(n)n^{-1/2-b}<\infty$. This uses the real Dirichlet series of $-\zeta'/\zeta$ or $\Lambda(n)\le\log n$. The boundary at equality $t=\log n$ contributes zero.
- **Lerch term and (3.1)–(3.2), p. 5.** With $a_n=n+1/4$, expand the Lerch difference as $\sum_{n\ge0}(e^{-2a_n t}-1)/a_n^2$. For all $t\ge0$, the absolute value in the numerator is at most one, and with damping $b>0$ the summed absolute integral is at most $b^{-1}\sum a_n^{-2}$. The individual integral before multiplying by $1/(4a_n^2)$ equals $(w+2a_n)^{-1}-w^{-1}$. After multiplication this is $(2z^2)^{-1}[1/a_n-1/(n+s/2)]$. The absolutely convergent digamma series (3.2), $\psi(v)=-\gamma_{\rm E}-\sum_{n\ge0}[(v+n)^{-1}-(n+1)^{-1}]$, gives the sum as $(2z^2)^{-1}(\psi(s/2)-\psi(1/4))$. Here $\operatorname{Re}(s/2)>1/4$, so there are no singular denominators. This proves (3.1) on its full stated half-plane. The Euler constant and $\psi(1/4)$ terms cancel as required when combining the transforms.

Their sum is $z^{-2}\xi'(s)/\xi(s)$, the same as the spectral transform in §3. Fix any $b>1/2$. Both $e^{-bt}g_\zeta(t)\mathbf1_{t\ge0}$ and the corresponding function of $G$ are in $L^1(\mathbb R)$ by the absolute controls just checked. The transforms on $z=x+ib$, all real $x$, agree. Fourier uniqueness gives almost-everywhere equality and continuity gives equality everywhere on $t\ge0$, including $t=0$. Evenness gives (1.7) for negative $t$ as well. No appeal to a boundary distribution or continuation to $\operatorname{Im}z=1/2$ is required.

## 6. External dependencies and version boundary

- [1] Biane–Pitman–Yor and [3] Lagarias–Rains supply context only. [2] Gnedenko–Kolmogorov, Example 17.6, and [5] Lin–Hu, Theorem 2, are cited for the older Euler-product probability results. Their relevant mechanism is reconstructed in §2.
- [4] Lebedev, (1.3.16), supplies the standard digamma expansion (3.2), which also follows by logarithmically differentiating the convergent Weierstrass product of $1/\Gamma$. Its use is local to the Lerch transform.
- [6] Nakamura, *A complete Riemann zeta distribution and the Riemann hypothesis*, is historical context only. Its primary abstract independently confirms the stated range and the pretended-infinitely divisible criterion. [Primary predecessor](https://arxiv.org/abs/1504.03438)
- [7] Sato supplies the exact general Lévy–Khintchine statements. The forward direction within this paper can also be checked directly via the finite-rate compound Poisson law in §4. [8] Suzuki supplies the originating exponent and earlier zero identity. The article's own appendix eliminates reliance on [8] for the main equivalence.
- [9] Titchmarsh with Heath-Brown supplies the analytic continuation, completion, zero strip, order, functional equation and Dirichlet-series identities. The article cites Theorem 2.1, §2.12 and Theorem 2.12, (2.1.13) and (1.1.8) at the indicated places. The proof checks how those hypotheses are used, and supplies the central and real-axis nonvanishing explicitly. Hadamard factorization and uniqueness of the Fourier transform on $L^1$ are further standard structural inputs.
- [10] Widder supplies the fixed-sign abscissa singularity theorem. Section 4 independently reconstructs the needed nonnegative real Laplace case, including convergence and analyticity on the open right of the abscissa.

The current arXiv history lists only v1, deposited 14 June 2023. The inspected PDF prints an author version date of 16 June 2023. Both dates record what their respective sources say. The journal catalogue and Crossref identify *Statistics & Probability Letters* 201 (October 2023), article 109889. Crossref returned no relation or update record, and a bounded search for the title or DOI with corrigendum and erratum terms found none. The publisher's public abstract and opening metadata were accessible through search. The direct publisher page returned HTTP 403 to the detailed comparison, so the journal proof and possible silent textual changes remain unverified. The convergence qualifications above apply to the inspected arXiv manifestation. [arXiv history](https://arxiv.org/abs/2306.08317) · [Journal DOI](https://doi.org/10.1016/j.spl.2023.109889) · [Crossref record](https://api.crossref.org/works/10.1016/j.spl.2023.109889)
