# Classical sources for zero density and zeta moments, 1921–1979

The [source records](classical63_records.jsonl) cover 24 original articles and proceedings contributions within the 1901–1980 window. The selection links four strands of the literature. Van der Corput, Landau, Vinogradov and Korobov supply exponential-sum and zero-free-region antecedents. Hardy–Littlewood, Ingham, Atkinson and Ramachandra supply approximate functional equations and moments. Selberg supplies the critical-line and distribution context. Halász–Turán, Montgomery, Huxley, Jutila and Heath-Brown develop zero detectors and large values for zeta and Dirichlet families.

## Two complete readings from original journal scans

### Huxley, *Large values of Dirichlet polynomials, III* (1975)

Read printed pp. 435–444, §§1–5 and the errata. Theorem 3, p. 439, concerns a collection $U$ of pairs $(s,\chi)$ with $s=\sigma+it$ and $\chi$ primitive modulo $q$. The setup on p. 436 fixes an integer $q_0\ge1$, a real $Q\ge q_0$ and $T\ge1$, sets $D=Q^2T/q_0$ and $\ell=\log D$, and restricts pairs to $q\le Q$, $q\equiv0\pmod{q_0}$, and $0\le\sigma\le1/\ell$. All pairwise $t$-differences have size at most $T$. Distinct pairs with the same character have $t$-separation at least one. For
$$
F(s,\chi)=\sum_{N<n\le2N}a(n)\chi(n)n^{-s},\qquad
G=\sum_{N<n\le2N}|a(n)|^2,
$$
let $R=|U|$ and suppose $|F(s,\chi)|\ge V$ for every pair, with $VG^{-1/2}=N^{\alpha-1/2}$. If $r\ge2$ is an integer, $N^r\le D<N^{r+1}$ and $\alpha>3/4$, then for every $\varepsilon>0$ and sufficiently large $D$,
$$
R\ll_{r,\alpha,\varepsilon}D^{12(1-\alpha)/5+\varepsilon}.
$$
Theorem 3 also gives $R\ll_{r,\alpha,\varepsilon}D^{2(1-\alpha)+\varepsilon}$ for $\alpha>(3r-1)/(4r-2)$. If the character is fixed throughout $U$ and the power condition uses $T$ in place of $D$, then $R\ll T^{2(1-\alpha)+\varepsilon}$ holds for $\alpha>4/5$ when $r=2$, and $\alpha>7(3r-1)/(28r-12)$ for $r\ge3$. These are (2.28)–(2.35). [Original pp. 436–439](../sources/prefix_formula62_classical2/hux1975.pdf)

Theorem 1, (2.20)–(2.21), gives $R\ll G V^{-2}N(\log\ell)^2+G^3 V^{-6}ND\Delta_2^{1/2}\Delta_3\ell^{11}$ for $V>c_1G^{1/2}N^{1/4}\ell^2$, with $c_1$ absolute and $\Delta_j=\max_{n<D}d_j(n)$. The proof combines the reflection estimate at length $D/N$ with an auxiliary polynomial whose product with $F$ has length on the $D$ scale. Lemma 3 bounds the product coefficient energy through divisor multiplicities. Equation (3.13) contains a term linear in $R$ that can be absorbed under (2.21), giving (3.14). Theorem 2 repeats the product argument with powers. In §5, after incorporating a fixed character into the coefficients, subdivision at $T_0$ yields three terms in (5.2). Equations (5.3) and (5.10) balance the first against the second and third terms respectively. The text derives the zero-density consequences by substitution into the detector argument of Part I, §§6–8. Equation (1.1) gives a primitive-character sum for $q\le Q$ divisible by $q_0$ with exponent $12(1-\sigma)/5+\varepsilon$ on $Q^2T/q_0$. Equation (1.2) gives the zeta density-hypothesis exponent for $\sigma>4/5$. The foot of p. 444 corrects four equations in the earlier unnumbered *Large values of Dirichlet polynomials*, including an $N^{1/4}$ factor in the final term of that paper's (1.12). [Part III scan](../sources/prefix_formula62_classical2/hux1975.pdf) · [Part I scan](../sources/classical63/huxley1973.pdf)

### Jutila, *Zero-density estimates for L-functions* (1977)

Read printed pp. 55–62, §§1–5 and the appendix. The theorem takes $T\ge2$, fixed $\varepsilon>0$, a fixed positive integer $k$, and $R$ pairs $(s_r,\chi_r)$ with $s_r=\sigma_r+it_r$, $\sigma_r\ge0$, and all $|t_r-t_s|\le T$. Distinct pairs either have different characters or satisfy $|t_r-t_s|\ge1$. Each $|f(s_r,\chi_r)|\ge V>0$, where $f(s,\chi)=\sum_{N<n\le2N} a_n\chi(n)n^{-s}$ and $G=\sum_{N<n\le2N}|a_n|^2$. In the common-modulus $q$ and primitive-conductor-at-most-$Q$ settings, write $D=qT$ and $D=Q^2T$ respectively. Equations (1.2) and (1.3), p. 56, give
$$
R\ll_{\varepsilon,k}(GNV^{-2}+D(G^4N^2V^{-8})^k+(DG^2V^{-4})^k)\,W^\varepsilon,
$$
with $W=qT$ and $W=QT$, respectively. For the principal character modulo 1, (1.4) gives
$$
R\ll_{\varepsilon,k}
\bigl(GNV^{-2}+TG^{3-1/k}N^{1-1/k}V^{-6+2/k}+T(G^4N^2V^{-8})^k\bigr)T^\varepsilon .
$$
[Original pp. 55–56](../sources/prefix_formula62_classical2/jut1977.pdf)

The corollary uses $N(\alpha,T,\chi)$ for zeros in $\alpha\le\Re s\le1$, $|\Im s|\le T$, with $3/4\le\alpha\le1$ and $T\ge2$. It gives the density-hypothesis exponent $2(1-\alpha)+\varepsilon$ for the following ranges and bases.

| Sum or count | Base | Threshold in the printed corollary |
|---|---|---:|
| All characters of one modulus $q$, (1.5) | $qT$ | $21/26$ |
| Primitive characters, conductors $q\le Q$, (1.6) | $Q^2T$ | $21/26$ |
| Same primitive family with alternate height scale, (1.7) | $Q^2T^2$ | $7/9$ |
| Zeta alone, (1.8) | $T$ | $11/14$ |

For (1.8), choosing $k=3$ gives $A_3(\alpha)=\max(2,3/(21\alpha-15),9/(7\alpha-1))$. Both fractions reach 2 at $\alpha=11/14$. This checks the inclusive threshold in Jutila's statement, while Huxley's Part III uses a strict inequality in (1.2). The fixed-modulus sum includes imprimitive characters. The two primitive-family entries use different bases, so the smaller threshold does not imply a stronger bound on the $Q^2T$ scale. [Corollary, p. 56](../sources/prefix_formula62_classical2/jut1977.pdf)

The smoothing in Lemma 1 uses $e^{-(n/2N)^h}-e^{-(n/N)^h}$ and the functional equation to reflect a short sum into a partial sum on the critical line. Lemma 2 bounds the squared sum of pairwise correlations by expanding in the coefficient indices and using $|a_n|\le A$. Lemma 3 uses the fourth power mean of Dirichlet $L$-functions, including the twisted family in (2.5). The Halász–Montgomery inequality (3.1), Hölder in (3.2), and those lemmas give the common-modulus result. Subdivision and an optimal shorter height scale yield the zeta case. Section 4 sketches the density deduction by raising the detector in (4.1) to an integer power to land in a viable length range. The appendix reproduces Huxley's alternative large-value estimate using a selected row in the pairwise sum and a mean-value estimate after multiplying by the detector. The complete text includes proof sketches and invokes external estimates, including the zero-detection lemma cited in §4. [Original §§2–5 and appendix](../sources/prefix_formula62_classical2/jut1977.pdf)

## Historical comparisons

- The 1972 Huxley paper uses $|\gamma|\le T$ and gives the classical short-prime-gap consequence for exponent $\delta>7/12$, explicitly via a uniform density envelope with $\lambda=12/5$. Its (1.8) quotes Ingham's $T^{3(1-\alpha)/(2-\alpha)}(\log T)^5$ in the comparison on p. 164. This is an original Huxley quotation of a source already catalogued as Ingham 1940. Guth–Maynard's 2026 journal Theorem 1.2 uses $|\gamma|\le T$ and gives $T^{15(1-\sigma)/(3+5\sigma)+o(1)}$. In combination with Ingham it yields the uniform exponent coefficient $30/13$. Its Corollary 1.3 gives an asymptotic in the short-interval range starting at $x^{17/30+\varepsilon}$, supported by a density estimate with near-$1$ losses controlled separately in its proof. These are concrete 2026 reference bounds for zeta. [Huxley 1972, p. 164](../sources/prefix_formula62_classical2/hux1972.pdf#page=173) · [Guth–Maynard, Annals](https://annals.math.princeton.edu/2026/203-2/p06)
- Jutila's classical zeta threshold $11/14$ is weaker than the ranges established in Tao–Trudgian–Yang, *New exponent pairs, zero density estimates, and zero additive energy estimates*, Theorem 51 and the cited Bourgain bound. In Theorem 51, both terms of the maximum are at most 2 for $\sigma\ge25/32$ through $4/5$, which includes the endpoint in that theorem. The historical $q$- and $Q$-family exponents are statements about their own families. [Tao–Trudgian–Yang, Theorem 51](https://arxiv.org/abs/2501.16779v1)
- Selberg's 1942 announcement, Levinson's short and long 1974 papers, and Ingham's 1940 two-page note already occur in the corpus. The 1946 Selberg memoir is a distinct publication, and the 1928 Ingham fourth-moment article is distinct from his 1940 density note. The relevant modern proportion sources are indexed separately in the Observatory. [Selberg and Levinson records](threshold62_history_records.jsonl) · [Modern zeta-proportion records](analytic_records.jsonl)


- Lewko’s 2026 Palomar registration reports a global uniform zeta coefficient $39/17$ and the fixed-$\sigma$ coefficient $3/(2\sigma)$ for $3/4<\sigma\le1$. The Observatory checked the pinned Lean declarations and their axiom footprint. The registry records a formal result separate from the Annals publication, and the fixed-$\sigma$ conclusion does not assign coefficient 2 at the exact $3/4$ endpoint. The classical estimates above retain their dates, counting conventions and family ranges. [2026 registry, v1](https://palomar-registry.org/entry?id=PALOMAR-2026-10-11-000010&version=1) · [Observatory verification](PAPER-DF62-003.md)

## Primary passages and source access

| Publication | Source check |
|---|---|
| Van der Corput 1921 | Printed p. 53, (1)–(3), presents the exponential-sum and phase-integral comparison and a quadratic application. The complete Göttingen issue contains the article on PDF pp. 57–83. |
| Van der Corput 1922 | Printed p. 39 defines the summatory divisor error and gives the improvement target. This is distinct from same-title work from 1923. |
| Hardy–Littlewood 1923 | Crossref indexes the original Proceedings article on the approximate functional equation and divisor problems. The article PDF transfer was unavailable. |
| Landau 1924 | Printed p. 105 attributes two growth bounds to Hardy and Littlewood, cites the inferred zero-free region, and names the author's separate article printed immediately before it in the same volume. |
| Ingham 1928 | The Oxford issue and Crossref date the fourth-moment article to 1928. Atkinson's 1949 footnote cites the same volume and pages with 1926 as the year. This record uses the publisher's year and leaves the discrepancy visible. |
| Selberg 1946 | The Oslo journal memoir on pp. 89–155 is bibliographically identified. A readable copy of the original memoir remained unavailable. |
| Atkinson 1949 | Printed pp. 353–355 give the theorem and outline. The main term of the second moment is $T(\log(T/(2\pi))+2\gamma-1)$. For fixed $0<A<A'$ and $AT<N<A'T$, the original formula adds two finite oscillatory sums and an $O(\log^2 T)$ remainder. The first sum has a Voronoi-type phase for small $n$. The paper explains the decomposition by $m-n$, Poisson summation, continuation, integration, and the saddle point. |
| Turán 1956 | The Bombay proceedings reproduce the JIMS article. The opening uses positive heights for the zero count, and the closing proof sketch invokes conjecture C. Selberg's 1942 announcement has essentially the same title and is a separate work. |
| Vinogradov 1958 | The theorem on p. 162 and consequences on p. 164 link a logarithmic-phase exponential sum to $zeta(1+it)$, a zero-free region and prime counting. The Russian scan is accessible in an online index. |
| Korobov 1958 | The main lemma on p. 28 uses moment solution counts. Theorems 4–5 on pp. 30–31 give the zeta and prime-counting consequences. The proof note on p. 31 points to Vinogradov's adjacent 1958 paper for parallel estimates. |
| Bombieri 1965 | The Cambridge original article record identifies the improved large sieve of Linnik. The Russian translation is another manifestation of that article. |
| Halász–Turán 1969 | The journal's original abstract identifies zeta density results and a Lindelöf-conditional estimate. The full original article remained unavailable. |
| Halász–Turán 1970 | The Hungarian Academy scan contains the complete sequel, pp. 403–419. Printed §§1–2 define the primitive-character sum with $0<t\le T$. Theorems I and II use the paper's family Lindelöf-type hypothesis. Section 2 names the large-sieve and power-sum approaches to Theorem I. |
| Montgomery 1969, *Mean and large values* | Printed p. 334, (1)–(5), opens with mean square and large sieve estimates and sets up separated ordinates for Theorem 1. |
| Montgomery 1969, *Zeros* | Printed p. 346 explicitly distinguishes the hybrid primitive family from the fixed modulus. It identifies the immediately preceding paper as the source of the Dirichlet-polynomial input. |
| Huxley 1972 | Printed p. 164, (1.1)–(1.9), records the prime-gap exponent and identifies Ingham's contribution to the uniform density argument. |
| Jutila 1972 | §1 gives the fixed-modulus sum and (1.2)–(1.6). §1.3 describes the zero-free rectangle and the powers of the short detector that refine Montgomery's method. |
| Huxley 1973 | The archival Part I scan gives the reflection argument used in Part III. The bibliographic year is the printed and publisher year. Part III p. 444 supplies four corrections. |
| Montgomery–Vaughan 1974 | The author-hosted copy reproduces the journal's original Hilbert inequality article, pp. 73–82. The corollaries connect the bilinear estimate to a Dirichlet-polynomial mean-square estimate. |
| Ramachandra 1974 | Numdam supplies the original fourth-power mean article, cited as [16] in Jutila 1977. |
| Huxley 1975 | Complete reading above. |
| Ramachandra 1975 | The academy's original scan gives the zeta density comparison cited as [15] in Jutila 1977. |
| Jutila 1977 | Complete reading above. |
| Heath-Brown 1979 | Printed p. 231 defines the primitive family and announces bounds on the $Q^2T$ scale. This is the Canadian Journal of Mathematics article of pp. 231–240. |

## Source manifestations

An article PDF, a full journal-volume PDF, or a verified online text is the evidence for full-text access. The records give printed page ranges, PDF-page locators for volume scans, and SHA-256 hashes for local files. A volume hash identifies the exact downloaded volume, including its cover and adjacent articles. The two 1969 Montgomery papers share a volume hash and use distinct locators. The filename `copp1979.pdf` in the earlier download directory is misleading. Inspection identifies the scan as Heath-Brown's Canadian Journal of Mathematics article, so the record uses Heath-Brown's metadata. Atkinson and the Russian notes were available through web-indexed original scans while the local download endpoints returned service or access pages. Bibliographic rows cite the original publication or authoritative catalogue even when the proof text was unavailable in this pass.
