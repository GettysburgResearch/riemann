# Conditional Upper Bounds for Large Deviations and Moments of the Riemann Zeta Function

Louis-Pierre Arguin, Emma Bailey and Asher Roberts. arXiv:2604.25579v1, 28 April 2026, 16 pages. The archived arXiv landing page shows one version and gives a repository DOI. [Version history](https://arxiv.org/abs/2604.25579v1) · [Primary PDF](https://arxiv.org/pdf/2604.25579v1)

## Reading and verification

Read all 16 pages of the primary PDF through its layout-preserving text, including §§1–3, both appendices and references. Level 1 denotes complete substantive reading. The detailed polynomial approximation, Gaussian comparisons and cited arguments have not been independently audited. The private PDF is `sources/recent_corpus_round5/2604.25579.pdf`.

- Theorem 1.1, p. 2. Under RH, fix $k>0$ and let $V(T)\sim k\log\log T$. For sufficiently large $T$, $T^{-1}\operatorname{meas}\{t\in[T,2T]:\log|\zeta(1/2+it)|>V\}\le \exp(e^{ck})e^{-V^2/\log\log T}/\sqrt{\log\log T}$, for an absolute $c>0$.
- Corollary 1.2, p. 2. Under RH, for $k\ge2$ and sufficiently large $T$, the normalized $2k$-th moment is bounded by $\ll\exp(e^{ck})(\log T)^{k^2}$, with the same $c$ as in Theorem 1.1. The paper cites the unconditional range $0\le k\le2$ separately.
- Proposition 1.3 and §2.3, pp. 3 and 7–9. Soundararajan’s RH-dependent pointwise inequality controls a late crossing of the lower barrier. The paper chooses the truncation using the size of the remaining deviation and splits the difference of prime sums into a disjoint-prime-block increment and a change of abscissa. Appendices A and B transfer polynomial averages to Steinhaus variables to obtain Gaussian bounds on the good events.
- Corollaries 3.1–3.2, pp. 9–10. The source gives short-interval applications under RH. Its exceptional-set wording uses “Lebesgue measure” while §1.2 defines probability using the uniform law on $[T,2T]$. The needed normalization is unresolved in this scope. These corollaries are not recorded as standalone precise exceptional-set estimates.

## Follow-up

A useful proof-level question is whether the polynomial approximation and two-abscissa covariance in Appendix B can be controlled with explicit uniform constants over a growing range of $k$. A separate scope check is to reconstruct the short-interval step from the normalized level-set estimate and the discretization in Arguin–Bailey 2023, tracking every factor of $T$. These are open audit tasks for this record.
