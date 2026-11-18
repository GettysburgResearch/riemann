# Bui–Florea–Heycock on small values of zeta

Independent source reading, 17 November 2026. *Small values of the Riemann zeta-function near the critical line*, arXiv:2610.27591v1, 20 October 2026, PAPER-LATEST62-003. Read all 56 pages, including §§1–10 and references, using the primary PDF text and visual checks of pp. 27 and 41. The PDF bytes are pinned by the paper record. The current arXiv history showed v1 only. The paper-level designation is Level 1. The scoped reconstructions below use cited pointwise and mean-value estimates as inputs. [Primary PDF](https://arxiv.org/pdf/2610.27591v1) · [Version history](https://arxiv.org/abs/2610.27591)

## Statement regimes and dependencies

All main numbered results here assume RH. The parameter \(k\) of \(I_{-k}\) means the exponent \(-2k\) on \(|\zeta|\), where \(I_{-k}=T^{-1}\int_T^{2T}|\zeta(1/2+\alpha+it)|^{-2k}dt\). The independent integer \(j\) in \(\mu_j\) is the exponent of \(1/\zeta\), so the relevant moment for the Perron transform is \(k=j/2\). Put \(B=\log(1/\alpha)\) and \(h=\log\log T\).

| Source | Parameters and claim | Proof inputs |
|---|---|---|
| Theorem 1.7, pp. 6–7 | \(\alpha=o(1)\), \(\alpha\log T\gg1\), \(V=\kappa B\) and \(\kappa\) in a fixed compact subinterval of \((0,1/2)\). Gaussian upper tail \(\ll B^{-1/2}e^{-V^2/B}\). The same form holds for all compact positive \(\kappa\) ranges if \(\alpha\log T\gg B^{12+\varepsilon}\). | Large shifts use §3 and Proposition 5.3, a single prime sum and exponential tilt. Small shifts use the cutoff recursion of §§4–6, with Propositions 5.1–5.2 and Lemmas 6.1–6.5. |
| Theorem 1.8, p. 7 | \(1\ll\alpha\log T\ll B^{12+\varepsilon}\), \(1/2\le\kappa\le\kappa_1\) fixed and \(\varepsilon_1>0\). Upper tail \(\ll\alpha^{\kappa-1/4-\varepsilon_1}\). | Same recursion. In (6.23), choose \(\rho<1\) close to 1 and use \(-\rho\kappa+\rho^2/4\le-\kappa+1/4+\varepsilon_1\). |
| Theorem 1.1, p. 2 | Fixed \(0<k<1/2\). For \(1\ll\alpha\log T\ll h\), \(I_{-k}\ll\alpha^{-k^2}\). For \((\log h)^{-c}\ll\alpha\log T\ll1\), fixed \(0<c<1\), \(I_{-k}\ll(\log T)^{O(1)}\). | (7.16), Gaussian saddle near \(V=kB\), tail Theorem 1.8 and Lemma 7.1 with \(2k<\rho<1\). The second range uses Lemma 7.1 and the trivial low-tail bound. |
| Theorem 1.2, p. 3 | \(k=1/2\). For \((\log h)^{-c}\ll\alpha\log T\ll1\), bound \(\exp(C h(\log h/\log\log h)^2)\). For \(C_1(\varepsilon)/h\le\alpha\log T\ll(\log h)^{-c}\), bound \(\exp((\log T)^\varepsilon)\). | Lemma 7.1 upper branch and Lemma 7.2 respectively. At \(2k=1\), the factor \(e^V\) needs decay beyond \(e^{-V}\). |
| Theorem 1.3, p. 3 | Fixed \(k>1/2\), \(\alpha=o(1)\), \(\alpha\ge C(k)/((\log T)^{1/(2k)}h)\). Bound \(I_{-k}\ll\alpha^{-k^2}\). | Earlier Bui–Florea for larger shifts, then Theorem 1.7 in its full-\(\kappa\) regime plus Lemma 7.3. The high-tail rate exceeds \(2k\) by order \(1/h\). |
| Theorem 1.4, p. 4 | For each positive integer \(j\), \(|\sum_{n\le x}\mu_j(n)|\ll\sqrt{x}\exp(C_j(\log x/\log\log x)^{j/(j+1)})\). | §8.1 uses Theorem 1.2 at \(k=1/2\) and pointwise reciprocal bounds for connecting segments. §8.2 uses Theorem 1.3 at \(k=j/2\) for integer \(j>1\). Theorem 8.1 separately states a real-\(j\) version with a Hankel-contour main term when \(j\) is noninteger, drawing on the earlier contour source. |
| Theorem 1.5, p. 4 | For \(0<\alpha\ll(\log T)^{-c}\) and \(\alpha\log T/h\to\infty\), the minimum of \(|\zeta(1/2+\alpha+i(t+v))|\) over \(|v|\le1\) is \(\alpha^{1+o(1)}\) in probability. | Theorem 9.5 supplies the lower bound at these shifts and Theorem 9.7 supplies the upper bound. The more explicit Theorem 9.2 uses \(\alpha\log T/(h\log h)\to\infty\). Conjectures 1.6 and 9.1 specify tighter fluctuation scales. |
| Theorem 1.9, p. 7 | Fixed \(k>0,\gamma\ge0\), \(H=(\log T)^\gamma\), \(\alpha\ll(\log T)^{-c}\), \(\alpha\log T\gg B^{12+\varepsilon}\). The normalized short-interval negative \(2k\)-th moment is \(\ll A\alpha^{-k^2}\) outside measure \(\ll T/A\), for \(1\le A\ll\alpha^{-M}\). For \(k>k_\gamma=(1+\gamma h/B)^{1/2}\), (1.6) replaces \(k^2\) by \(2kk_\gamma-k_\gamma^2\), with the stated prefactors. | Theorem 9.2 caps the local maximum of \(W_\alpha=-\log|\zeta|\); Theorem 1.7, Fubini and Markov control the rest of the layer cake. |

RH enters the reciprocal explicit formula through the zero geometry in Bui–Florea's bound, the pointwise majorants near \(1/2\), and the holomorphy of \(1/\zeta\) during contour deformation. The short-interval lower bound for \(W_\alpha\) also uses the RH extremal-minorant argument. The pure Steinhaus moments, Taylor estimates, Fourier mean-value steps, layer-cake identity, and contour bookkeeping are separate mathematical operations. In the Gaussian branch the variance changes to \(\tfrac12\log(1/\alpha)+O(1)\) at a sufficiently long cutoff. The \(\beta_j\) of the recursion are logarithmic polynomial lengths \(\log T_j/\log T\), and the \(\beta\) of §9.2 is a separate horizontal shift. Neither is the moment exponent. [Primary source, §§2–10](https://arxiv.org/pdf/2610.27591v1#page=10)

## Reconstructing the omitted Lemma 7.2 proof

Use the paper's RH pointwise bound (7.3) and prime-sum bound (7.4), which invoke Bui–Florea [14]. Fix \(0<\varepsilon,c<1\). In the second shift range of Theorem 1.2 set \(a=\alpha\log T\) and assume \(C_\varepsilon/h\le a\ll(\log h)^{-c}\), where the lower constant can be sufficiently large. For \((\log T)^\varepsilon\le V\le V_*=O(\log T)\) put \(J=\lfloor\log V\rfloor\) and \(x=T^{J/V}\). Then \(J\gg_\varepsilon h\), \(aJ/V=o(1)\), and \(aJ\ge C_\varepsilon\varepsilon/2\). Hence
\[
\frac{V}{J}\log\frac1{1-e^{-aJ/V}}
 \le \frac VJ\bigl(\log V-\log(aJ)+\log 2\bigr).
\]
Subtract this from \(V\). Because \(J-\log V\in(-1,0]\), making \(C_\varepsilon\) large yields any prescribed fixed multiple of \(V/J\) as the remaining margin. The error term in (7.4) is \(O(h)=o(V/J)\). Therefore \(W_\alpha>V\) forces \(|Q_x|>D V/J\) for an arbitrarily large fixed \(D\).

Split \(Q_x\) into the same prime blocks \(Q_j\) as in (7.6). Lemma 2.2 gives the coefficient bounds of (7.5), since the extra logarithm \(\log(1/(\alpha\log x))=\log(V/(aJ))\) is at most \(\log V\). The estimate remains uniform when the lower bound on \(C_\varepsilon\) is increased. Put \(w=D V/J\), use thresholds \(w/4\) for \(Q_0\) and \(w/(4(J-j)^2)\) for \(j\ge1\), and take \(q_j=\lfloor V/(j+1)\rfloor\). The total of these thresholds is less than \(w\). The powers \(Q_j^{q_j}\) have Dirichlet length at most \(T\). The variance estimates (7.7) and the mean-value/Markov argument in (7.9)–(7.10) give respectively
\[
\left(\frac{C h J^2}{D^2V}\right)^{\lfloor V\rfloor},
\qquad
\left(\frac{C(J-j)^8}{D^2 V}\right)^{q_j}.
\]
The first is \(O(e^{-2V})\), uniformly in the stated ranges. For the second, since \(r-8\log r\) is bounded below for \(r\ge1\), one can choose \(D\) so that
\[
\log\frac{D^2V}{C(J-j)^8}\ \ge\ j+5.
\]
Rounding the moment order costs at most \(J+4\), so \(q_j(j+5)\ge V+4V/J-(J+4)\ge V+3V/J\). Summing over \(j\ge1\) gives \(O(e^{-V-2V/\log V})\). This recovers Lemma 7.2 with the stated tail exponent and makes the reciprocal first-moment input independent of the Gaussian branch.

For the layer cake at \(k=1/2\), the area below \(U=(\log T)^\varepsilon\) is at most \(e^U\). The contribution above \(U\) is at most \(C V_*\exp(-2U/\log U)=o(1)\), since \(V/\log V\) is increasing there. Thus \(I_{-1/2}\ll e^U\). The displayed \(\ll\) in Theorem 1.2 is consistent with this argument. [Lemma 7.2 and Theorem 1.2 proof](https://arxiv.org/pdf/2610.27591v1#page=36)

## How the moment enters the Mertens exponent

For \(X=\log x\), take \(Y=\log x_0=\sqrt{X/\log X}\) and \(\alpha_0=C/(Y\log Y)\). On the central segment, \(\log(1/\alpha_0)=\log Y+O(\log\log Y)\). The RH pointwise bound (8.1) on \(1/2+\alpha_0+it\) gives a reciprocal cost at most \(\exp(O(Y))\) for \(|t|\le x_0\). Integrating \(|1/s|\) adds only a factor \(O(Y+1)\). The Perron factor contributes \(\sqrt{x}\exp(\alpha_0X)\), with \(\alpha_0X=O(Y)\). This is the balance behind (8.2).

For the vertical segment with \(|t|\asymp T_j=2^{j-1}x_0\), its shift is \(C/(\log T_j\log\log T_j)\). Thus \(\alpha_j\log T_j=C/\log\log T_j\) lies in the second range of Theorem 1.2 once \(C\ge C_1(1/3)\). The factor \(1/|s|\asymp1/T_j\) cancels the normalization factor of the mean, and \(x^{\alpha_j}\le x^{\alpha_0}\). The vertical costs are at most \(\exp(O(X^{1/3}))\), which is \(\exp(o(Y))\). There are \(O(X)\) dyadic segments. The intermediate horizontal connectors use \(|1/\zeta|\ll T_j^{1/2+\eta}\), the final connector uses pointwise bounds across \([1/2+\alpha_j,1+1/X]\), and RH permits shifting the contour without crossing reciprocal poles. Those connector estimates were read in §8.1 and have not been rebuilt from their external pointwise inputs. [Perron proof, pp. 40–42](https://arxiv.org/pdf/2610.27591v1#page=40)

The paper attributes the suggested logarithmic improvement of the contour choice to a report from Claude and records ChatGPT assistance on Propositions 5.1–5.2, parameter checks and proofreading. The evidence used here consists of the primary statements and the derivations above. [Source disclosure, p. 10](https://arxiv.org/pdf/2610.27591v1#page=10)

## Scoped variance discrepancy in the Gaussian branch

The primary PDF p. 27 prints (6.4) as \(\sigma_{\ell,j}^2=\tfrac12\log(1/\alpha)+O(1)\) for the small-shift regime (4.1), citing (4.4). For an explicit admissible regime let \(\alpha\log T=h\), \(\ell=2\), \(j=K\) with \(\beta_K\asymp1\), and \(\beta_2=r h^{-30}\). Then \(\alpha\log T_K\to\infty\), but
\[
\log\log T_2=h-30\log h+\log r,\qquad \log(1/\alpha)=h-\log h.
\]
The first case of Lemma 2.3 gives uniform \(O(1)\) about \(\tfrac12\log\log T_2\), so the literal uniform (6.4) is incompatible with the stated variance. This was checked on the rendered p. 27.

Equation (4.4) instead gives \(\sigma_{\ell,j}^2=\tfrac12 B+O(1+z_\ell^2)\) with \(z_\ell=\log(1/\beta_\ell)\). Indeed \(\log(1/\alpha)-t_\ell=\max(0,z_\ell-\log(\alpha\log T))=O(1+z_\ell)\). At levels of order \(B\), an \(O(1+z_\ell^2)\) variance change perturbs a Gaussian exponent by \(O(1+z_\ell^2)\), which can be absorbed where the bounds retain the barrier saving \(\exp(-b c_\ell)\), since \(c_\ell=e^{z_\ell/90}\). At bounded \(z_\ell\), including the terminal checkpoint, the \(O(1)\) version holds. Equation (6.18) already uses an \(O(z_\ell^2)\) effect. This identifies a local repair for the displayed inference. A line-by-line audit of every use of (6.4) and the full Gaussian theorem remains open. The reciprocal first moment in the Mertens contour uses §7's separate high-tail argument. [Variance statements, pp. 12, 16 and 27](https://arxiv.org/pdf/2610.27591v1#page=27)

Two useful follow-up checks are to quantify the summable barrier surplus after retaining \(O(1+z_\ell^2)\) at every checkpoint, and to reconstruct the final high connector directly from the published reciprocal pointwise inequalities. These checks target distinct proof inputs.
