# PAPER-E014 — A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis

**Author:** Luis Báez-Duarte

**Version inspected:** [arXiv:math/0202141v2](https://arxiv.org/abs/math/0202141v2), 18 February 2002, seven pages. The archive lists v1 on 15 February and says v2 corrects three typos and adds one reference.

**Published version:** [Rendiconti Lincei, Ser. 9, 14(1) (2003), pp. 5–11](https://www.bdim.eu/item?fmt=pdf&id=RLIN_2003_9_14_1_5_0). The journal scan identifies the same title, author, main theorem and Balazard–Saias estimate. It adds a section on a constructive approximating sequence and has different numbering and pagination. The [archive DOI](https://doi.org/10.48550/arXiv.math/0202141) is separate from the journal publication, for which no DOI was verified. PAPER-E001 covers the sequel, arXiv:math/0205003.

**Audit level:** 0. Close reading focused on the theorem, Möbius and quotient estimates, and the two ordered norm limits in preprint §§1–3. The published Lemma 1 was independently located in the indexed journal scan.

**Theorem 1.1 in v2 and Theorem 1 on journal p. 5.** RH is equivalent to the indicator of \((0,1]\) belonging to the closed span of the fractional parts \(\{1/(nx)\}\) for positive integers \(n\) in \(L^2(0,\infty)\). The proof first sends the cutoff to infinity with fixed positive damping and then sends the damping to zero.

**Reusable input:** The general half-plane Möbius approximation in v2 Lemma 2.1, p. 3, and journal Lemma 1, p. 6, both equation (2.1), quotes Balazard–Saias [PAPER-E007](PAPER-E007.md), Lemme 2. If \(\tfrac12\le b<1\), \(\zeta\) is zero-free for \(\Re s>b\), \(b+\delta\le\Re s\le1\), and \(N\ge2\), then for each fixed \(\delta,\eta>0\),
\[
\sum_{n\le N}\frac{\mu(n)}{n^s}=\frac1{\zeta(s)}
+O_{b,\delta,\eta}\!\left(N^{-\delta/3}(1+|\Im s|)^\eta\right).
\]
The implied constant depends on the fixed gap \(\delta\).

**Evidence:** [Local v2 PDF](../sources/ratio62_weightedprior/baez_duarte_0202141v2.pdf), SHA-256 3ce4aff466443c71094affc1f8b6f5f0dd36cb4377dc5d2ceddbd2537c1d1819. Accessed 2026-11-17. Direct bdim PDF download returned HTTP 503, while the indexed PDF rendering showed the complete formula on journal p. 6.
