# Classical primary sources for primes, zeros, and Dirichlet sums

This supplement covers 1874–1949 inside the requested 1859–1950 window. It adds distinct works to the existing Riemann, Genocchi, Hadamard, von Mangoldt, Hardy, and Littlewood records. The strongest new direct evidence is the French 1899 logarithmic zero-free estimate, the German 1921 unit-window lemma, and the 1949 elementary prime-number proof. Bibliography-only leads have no theorem or proof audit attached.

## Two complete readings

**Edmund Landau, 1921.** I read both pages, including the footnote and proof inequalities, in the original German. For a non-identically-zero generalized Dirichlet series $f(s)=\sum_n a_ne^{-\lambda_n s}$ converging for $\sigma>\sigma_0$, and fixed $\delta>0$, its number $A(T)$ of zeros in $\sigma\ge\sigma_0+\delta$, $T<t\le T+1$, satisfies $A(T)=o(\log^2 T)$. The proof first shifts slightly inside the convergence half-plane and normalizes the first nonzero exponential coefficient. Bounded partial sums at the shifted reference point control the late tail by Abel summation for $\sigma\ge\log t/\lambda_w$, where $w>2$ is fixed. The finite initial terms then give $|f|>1/2$ there. A Jensen disk centered at $\log(T+1/2)/\lambda_w+i(T+1/2)$ has its outer radius equal to the real part of its center. The inner radius containing the remaining unit-height rectangle is smaller by $\delta+o(1)$ in the normalized coordinates. The numerator of Jensen's bound is $O(\log T)$, and the logarithmic radius ratio is asymptotic to $\delta\lambda_w/\log T$. The resulting $\limsup A(T)/\log^2T\le1/(\delta\lambda_w)$ holds for every fixed sufficiently large $w$, which proves the little-oh bound. The 1913 paper cited in the footnote supplies an earlier big-oh comparison. Its result and the contemporaneous Wennberg sum over a growing window are separate statements. [Original scan](../sources/prefix_formula62_classical_history/landau1921_article.pdf) · [DOI](https://doi.org/10.1007/BF02102311)

**Atle Selberg, 1949.** I read §§1–4 and the final remark in the full Annals article, pp.305–313. Equations (2.8)–(2.9) give the elementary symmetry identity
$$
\sum_{p\le x}(\log p)^2+\sum_{pq\le x}\log p\log q
=2x\log x+O(x).
$$
The double prime sum here runs over ordered pairs. The proof uses Möbius inversion and elementary summatory estimates. Passing by partial summation to the averaged error for $R(x)=\vartheta(x)-x$ gives (2.14),
$$
|R(x)|\le\frac1{\log x}\sum_{n\le x}|R(x/n)|
 +O\!\left(\frac{x\log\log x}{\log x}\right).
$$
Section 3 turns bounded signed sums and an upper bound on short increments of $\vartheta$ into a subinterval of controlled relative width on which $|R(z)|/z$ is small. Section 4 pays for those subintervals in the harmonic average in (2.14), so any upper envelope $a$ holding beyond a threshold is improved by a fixed positive decrement depending on $a$. Iteration gives $R(x)=o(x)$. The final remark distinguishes the strength of the identity from the weaker errors needed by this qualitative PNT proof. The introduction also describes Selberg's earlier route through an Erdős short-interval estimate, separately from the argument printed in §§2–4. [Original journal scan](../sources/prefix_formula62_classical_history/selberg1949.pdf) · [DOI](https://doi.org/10.2307/1969455)

## Inspected original passages

| Work | Passage checked | Technical use and scope |
|---|---|---|
| Mertens, *Ein Beitrag zur analytischen Zahlentheorie* (1874) | Printed p.46, German original | The introduction writes the reciprocal-prime sum and Euler-product logarithmic asymptotics as the targets and explains its comparison with Legendre and Chebyshev. This is the logarithmically weighted prime-sum predecessor, without a PNT claim from this passage. |
| de la Vallée Poussin, *Sur la fonction ζ (s) de Riemann et le nombre des nombres premiers inférieurs à une limite donnée* (1899) | §§73–79, especially pp.69, 71, 73–74 of the original French scan | Theorem 78 gives $1-\alpha>p/(\log\beta-\log n)$ for a zero $\alpha+i\beta$ at $\beta\ge705$, with printed $p=0.034666\ldots$, $n=47.886\ldots$. It also gives a stated lower-height bound. The displayed constants refer to this formulation. This is the quantitative sequel to the separately catalogued 1896 PNT article. |
| Hardy and Littlewood, *Contributions to the theory of the Riemann Zeta-function and the theory of the distribution of primes* | Introduction and §2 opening, original Acta scan | The text documents the earlier announcements and uses the Cahen–Mellin formula with their Tauberian theorems. Its introduction lists the resulting mean estimates, including $M(x)=o(x)$. Crossref dates the volume 1916. The physical impressions of inspected sheets say June 1917. |
| Weyl, *Über die Gleichverteilung von Zahlen mod. Eins* (1916) | §1 and polynomial passage around Satz 9, German original | Satz 1 gives the Fourier-character vanishing criterion for equidistribution. The later argument reduces polynomial degree through differences. This is an exponential-sum technique predecessor, without a zeta zero-free theorem. |
| Valiron, *Théorie générale des séries de Dirichlet* (1926) | §I.1, French original viewed online | Defines Dirichlet series with arbitrary strictly increasing, unbounded real exponents, and separates the ordinary number-theoretic case $\lambda_n=\log n$ from the power-series case $\lambda_n=n$. The online Numdam PDF was readable while its local transfer repeatedly truncated. |
| Erdős, *On a New Method in Elementary Number Theory Which Leads to An Elementary Proof of the Prime Number Theorem* (1949) | pp.374–377, original PNAS reprint viewed online | Formula (2) gives $\pi((1+c)x)-\pi(x)>\delta(c)x/\log x$ for fixed $c>0$ and large $x$, with $\delta(c)>0$. The proof opens by assuming a short-interval failure and using Selberg's identity to bound its consequences. The stated chronology is the author's account. |
| Beurling, *Analyse de la loi asymptotique de la distribution des nombres premiers généralisés. I* (1937) | §1 setup and the boundary-argument summary, French original | Generalized primes and their multiplicative integers yield a Dirichlet-series analogue, Euler product, and boundary-argument description. It is the original generalized PNT framework Selberg cites in his introduction. The exact sharp threshold results were outside this passage audit. |

## Bibliographical leads whose proof texts remain unverified here

- Bohr–Landau (1914), *Ein Satz über Dirichletsche Reihen mit Anwendung auf die ζ-Funktion und die L-Funktionen*. This is the four-page source lead for the classical density problem. Springer returned a landing page in place of the PDF.
- Van der Corput (1923), *Neue zahlentheoretische Abschätzungen*. The DOI identifies the Mathematische Annalen article, distinct from the author's later same-title paper. The Springer PDF endpoint did not give readable article text.
- Ikehara (1931), *An Extension of Landau's Theorem in the Analytical Theory of Numbers*. Wiley and Crossref verify the original journal manifestation. Exact boundary hypotheses of the original theorem were not inspected.
- Titchmarsh (1931), *On van der Corput's Method and the Zeta-Function of Riemann*. The publisher identifies the journal article and its scope by title. No exponent is assigned here.
- Ingham (1940), *On the Estimation of N(σ,T)*. The Oxford record verifies this two-page density note. Its theorem's exact range and log powers were not transcribed from a primary passage.

## Screened out

Riemann's 1859 memoir, Genocchi's prime-counting paper, Hadamard's 1896 article, the two von Mangoldt forms, Hardy's stand-alone critical-line work, de la Vallée Poussin's 1896 part I, and the selected Littlewood articles already have source records. The 1899 de la Vallée Poussin memoir was retained because it contains a distinct quantitative region. Carlson's 1920 Arkiv note was located through references, but no primary article-level manifestation was confirmed during this pass. Wiener 1932 has an authoritative journal record but was deferred while retaining the closer Ikehara Tauberian anchor. The attempted Vinogradov 1936 Math-Net PDF endpoints returned access errors. To distinguish historical exponential-sum sources from later zeta zero-free estimates, no Korobov–Vinogradov result was assigned to the 1936 lead. Littlewood's June 1914 French announcement was identifiable in the Hardy–Littlewood introduction, but its separate original scan was not confirmed here.

Per-work original languages, manifestations, identifiers, source access, and reading scope are in the [records](prefix_formula62_classical_history_records.jsonl).
