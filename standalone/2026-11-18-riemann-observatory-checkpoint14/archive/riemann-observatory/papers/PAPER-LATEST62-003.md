# Small values of the Riemann zeta-function near the critical line

Hung M. Bui, Alexandra Florea and André Heycock. arXiv:2610.27591v1, 20 October 2026, 56 pages. [Version history](https://arxiv.org/abs/2610.27591v1) · [Primary PDF](https://arxiv.org/pdf/2610.27591v1)

## Complete primary-source reading

Read all 56 pages, including §§1–10 and references. The private PDF and its layout-preserving text cover the same arXiv version. Visually checked pp. 27 and 41 against the PDF. Level 1 records complete substantive reading. Lemma 7.2 and the contour scale in §8.1 received separate local reconstruction. The full paper and its cited inputs have not been independently audited. The arXiv landing page checked on 17 November 2026 shows only v1. [Full source audit](../audits/bui_florea_heycock_latest62_fullsource_round5.md)

- Define $I_{-k}(\alpha,T)=T^{-1}\int_T^{2T}|\zeta(1/2+\alpha+it)|^{-2k}\,dt$. Theorem 1.1 gives the RH-conditional bound $I_{-k}\ll\alpha^{-k^2}$ for fixed $0<k<1/2$ and $1\ll\alpha\log T\ll\log\log T$. The same theorem gives a weaker polylogarithmic bound in a specified smaller-shift regime. The broader conjectured-order range in the abstract combines this with earlier work.
- Theorem 1.2 treats $k=1/2$. For fixed $0<\varepsilon,c<1$ and $C_1(\varepsilon)(\log\log T)^{-1}\le\alpha\log T\ll(\log\log\log T)^{-c}$, it gives $I_{-1/2}\ll\exp((\log T)^\varepsilon)$. This is the mean of $|\zeta|^{-1}$ and is the input to the $k=1$ contour argument in §8.1.
- Theorem 1.4 on p. 4, with §8 on pp. 40–43, gives under RH $|\sum_{n\le x}\mu_k(n)|\ll\sqrt{x}\exp(C_k(\log x/\log\log x)^{k/(k+1)})$ for each positive integer $k$, where $\mu_k$ are the Dirichlet coefficients of $\zeta^{-k}$. At $k=1$ this is the ordinary Mertens sum. For integer $k>1$ the similar contour uses Theorem 1.3 at moment parameter $k/2$. Theorem 8.1 states a separate version for real $k>0$, with a Hankel-contour main term for noninteger $k$.

## Follow-up

In §8.1, the central shift has size $1/(\log x_0\log\log x_0)$ and the Perron factor pays $\alpha_0\log x$. The pointwise reciprocal estimate (8.1) pays order $\log x_0$ in the exponent for this shift. Balancing these costs yields $\log x_0\asymp\sqrt{\log x/\log\log x}$. To test whether the contour could transmit a stronger mean estimate into a better Mertens bound, check which of these central-segment costs would still remain after replacing the dyadic vertical bounds. This is a question about the stated contour, without a claim of an improved arithmetic estimate.
