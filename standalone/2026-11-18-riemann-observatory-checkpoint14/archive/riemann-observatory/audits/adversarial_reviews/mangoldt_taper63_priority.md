# Antecedents for the prescribed logarithmic von Mangoldt taper

The closest source ingredients are Balazard's discrete quotient obstruction, Selberg's explicit formula for smoothed sums of \(\Lambda\), and Bettin–Conrey–Farmer's use of the same scalar logarithmic taper in the classical constant-target problem. The bounded primary-text comparison below did not locate the combination of the explicit factorial target, its prescribed von Mangoldt array, and the \(1/\log N\) boundary-norm constant. The selection leaves publication priority open. The scope of the proposed norm asymptotic is RH. [Balazard Proposition 11](../../sources/jump_generator63_antecedents/balazard_1812.04309.pdf) · [Titchmarsh–Heath-Brown Theorem 14.20](../../sources/selberg_round2/titchmarsh_zeta.pdf) · [Bettin–Conrey–Farmer arXiv v1](../../sources/ratio62_priority/bettin_optimal.pdf)

## Exact test for a match

For fixed \(k\ge2\), let \(c=\log k\), \(P(s)=k^{1-s}-1\), and \(W(s)=-(P(s)\zeta(s))'\). In the physical integer-cell model the target \(a^{(k)}\) has value \(k\log(\lfloor n/k\rfloor!)+k\lfloor n/k\rfloor c-\log(n!)\) on cell \(n\), and Mellin transform \(W(s)/s\). The quotient
\[
 G(s)=W(s)/\zeta(s)=P(s)(-\zeta'/\zeta)(s)+c k^{1-s}
\]
has Dirichlet coefficients \(w_k(n)=k1_{k\mid n}\Lambda(n/k)-\Lambda(n)+kc1_{n=k}\). Write \(L=\log N\) and \(A_N(s)=\sum_{n\le N}w_k(n)(1-\log n/L)n^{-s}\). The asserted leading term is for the squared full weighted boundary norm of \(W-\zeta(A_N-A_N(1))\), with \(\|F\|_*^2=(2\pi)^{-1}\int_{\mathbb R}|F(1/2+it)|^2/|1/2+it|^2\,dt\). Under RH the proposed constant is the sum of \(|W(\rho)|^2/|\rho|^2\) over distinct simple zeros, including both signs of the ordinate. The companion infimum is over actual ordinary integer Dirichlet polynomials of length at most \(N\). [Factorial target and quotient](jump_generator63_antecedents.md)

Balazard, arXiv:1812.04309v1, Proposition 11 already proves the qualitative membership obstruction with full zero jets on this same discrete step space. Proposition 10 gives the RH density implication, and Propositions 7–9 identify the jump quotient and its coefficients. The specialization to \(W\) yields the membership equivalence, since \(P(\rho)\ne0\) at any right-half zero in the open critical strip. The paper does not give a norm rate for these coefficients. Its §1 explicitly distinguishes pointwise arithmetic representations from convergence in the step norm. [Balazard §§1,3–5](../../sources/jump_generator63_antecedents/balazard_1812.04309.pdf)

## Classical Mangoldt smoothing and its exact algebraic transfer

Put \(B_X(s)=\sum_{n\le X}\Lambda(n)(1-\log n/\log X)n^{-s}\) for \(X>1\). For \(N>k\), a change of index gives the precise finite relation
\[
 A_N(s)= k^{1-s}\frac{\log(N/k)}L B_{N/k}(s)-B_N(s)
     + ck^{1-s}(1-c/L).
\]
The single-endpoint Riesz kernel is therefore the same elementary log weight as in the classical cutoff for \(\Lambda\). Selberg's formula as proved in Titchmarsh–Heath-Brown Theorem 14.20 uses the two-piece weight \(\Lambda_x(n)=\Lambda(n)\) through \(x\) and \(\Lambda(n)\log(x^2/n)/\log x\) on \((x,x^2]\), with zero further out. Its Dirichlet polynomial is exactly \(2B_{x^2}-B_x\). Its contour kernel is the difference of the two one-endpoint kernels, so the occurrence of the logarithmic taper in a prime sum has a classical primary antecedent. [Titchmarsh–Heath-Brown §§14.20–14.21](../../sources/selberg_round2/titchmarsh_zeta.pdf)

More precisely write \(F=-\zeta'/\zeta\) and
\[
 R_X(s)=\frac{X^{1-s}}{(1-s)^2}
   -\sum_{\rho}^{\rm distinct} m_\rho\frac{X^{\rho-s}}{(\rho-s)^2}
   -\sum_{q\ge1}\frac{X^{-2q-s}}{(-2q-s)^2}.
\]
At \(\Re s>1\), Theorem 14.20 gives
\[
 \bigl((\log(x^2))B_{x^2}-(\log(x^2))F\bigr)
   -\bigl((\log x)B_x-(\log x)F\bigr)=R_{x^2}-R_x .
\]
Iterate on \(x,x^2,x^4,\ldots\). The zero sums tend to zero as the final cutoff tends to infinity on this half-plane, by the unit-window zero count and the squared denominator. Absolute convergence of the log-weighted Dirichlet series gives \((\log X)(B_X-F)\to F'\). Hence
\[
 (\log X)B_X=(\log X)F+F'+R_X .
\]
For fixed \(X\), the residue series give meromorphic continuation on compact sets away from their poles. The identity continues with the matching singular parts canceled. This also follows by shifting the one-endpoint Perron integral with double kernel \((z-s)^{-2}\). Thus the residue identity can be obtained directly from an existing explicit formula, even though that formula does not analyze the factorial-target norm.

Substituting the formula for \(B_X\) into the exact finite relation gives
\[
 LA_N=LG+G'
 -\sum_{\rho}^{\rm distinct} m_\rho P(\rho)\frac{N^{\rho-s}}{(\rho-s)^2}
 -\sum_{q\ge1}P(-2q)\frac{N^{-2q-s}}{(-2q-s)^2}.
\]
In the residue with exponent \(\rho\), the shifted cutoff gives \(k^{1-s}(N/k)^{\rho-s}=k^{1-\rho}N^{\rho-s}\). The pole at 1 cancels because \(P(1)=0\), and the differentiated terms combine to \(G'\). This formula initially follows on the far right and has the same continuation as the formula for \(B_X\).

Under RH all the nontrivial poles are on the line. The anchor estimate from their explicit multiplicity-weighted residues is
\[
 A_N(1)=\frac{c\gamma_{\rm E}-c^2/2}{L}+O_k(N^{-1/2}/L).
\]
Indeed \(G(1)=0\), \(G'(1)=c\gamma_{\rm E}-c^2/2\), and the residue term at 1 from each nontrivial pole has size bounded by \(N^{-1/2}O_k(m_\rho/(1+|\gamma|^2))\). The trivial-pole contributions decay faster. A fixed left contour just below \(1/2\) gives the same estimate. Its exponential contribution at 1 is \(O_k(N^{-1/2-\delta}/L)\). This anchor estimate is a deduction from the quotient and contour identities. The correction has norm at most \(|A_N(1)|\|\zeta\|_*\) and changes only coefficient 1.

The distinction producing the proposed constant is the simple pole of the logarithmic derivative at every zero, with residue controlled by multiplicity and the bounded multiplier on the line. In the one-endpoint error each such term is proportional to
\[
 \frac{\zeta(s)}{L}\frac{1-N^{\rho-s}}{(s-\rho)^2}.
\]
Near that zero the remaining analytic multiplier is \(\zeta(s)/(s-\rho)\). Its value is \(\zeta'(\rho)\) at a simple zero and is zero at a multiple zero. The local profile has squared integral 1 after rescaling, since \((1-e^{-iv})/(iv)\) is the Fourier transform of the indicator of \([0,1]\). This is the reason the coefficient is \(|W(\rho)|^2/|\rho|^2\) and no reciprocal derivative occurs. To pass from fixed zeros to the full rate requires a uniform weighted tail and a lower bound for all approximants. These are separate from the residue identity. The unconditional existence of simple critical-line zeros, for example from the \(\kappa^*\) bound in Pratt–Robles–Zaharescu–Zeindler, makes the displayed constant positive. [Simple critical-line proportion in the primary text](../../sources/latest62_analytic2/1802.10521.pdf)

## Comparison with the primary approximation literature

| Source and inspected locator | Exact relevant overlap | Comparison with the factorial-target theorem |
|---|---|---|
| Bettin–Conrey–Farmer, Theorem 1, Lemmas 2–3 and §3 | Uses \(1-\log n/\log N\), the same full weighted norm, and the same Perron double kernel. | Their numerator is \(1\) and the coefficients are \(\mu(n)\) from \(1/\zeta\). The asymptotic uses RH and a negative moment of \(\zeta'\) that requires simplicity. Their arithmetic residue problem has reciprocal derivatives. [Primary arXiv v1](../../sources/ratio62_priority/bettin_optimal.pdf) |
| Maier–Rassias, Theorem 1.1 and Lemma 2.3 | Analyze the same prescribed Möbius taper, with the BCF residue formula. | The result concerns the numerator \(1\) and additional off-line-zero hypotheses. It gives distinct off-line oscillatory terms rather than the factorial-target norm. [Journal text](../../sources/ratio62_rstation48/maier_rassias.pdf) |
| Balazard–de Roton, main theorem and §2 Proposition 1 | Uses Möbius coefficients and compares the shifted reciprocal to its truncation in the same Mellin weight. The opening recalls a Chebyshev prime-sum application of balanced fractional parts. | The approximated function is the constant on the physical half-line. The shift \(n^{-\epsilon}\) and its RH upper bound concern the constant-target distance. The occurrence of \(\Lambda\) in the Chebyshev discussion is a prime-sum comparison. [Primary arXiv v1](../../sources/selberg_round2/balazard_roton.pdf) |
| Báez-Duarte, *On a General Strong Nyman–Beurling Criterion*, Theorems 1.2–1.3 and §3 | General target formulation via the Müntz operator and its dilates. | The target and generator family vary together. The theorems give closure criteria and a transfer by a bounded convolution, with no stated prescribed prime taper or scaled asymptotic. [Primary preprint](../../sources/prefix_formula62_generalL/baez_general.pdf) |
| De Roton, 2005 Theorem 2.3 and 2006 §§6–8 | Generalized continuous complementary-function criterion and multiplicity-sensitive lower-bound calculus for Selberg-class generators. | The density criterion and lower-bound construction use the indicator target and continuous contractions. They supply methodological precedents for transform and zero-jet estimates. [2005 primary text](../../sources/prefix_formula62_generalL/deroton_note.pdf) · [2006 primary text](../../sources/prefix_formula62_generalL/deroton_lower.pdf) |
| Delaunay–Fricain–Mosaki–Robert, I Theorems 2.2–2.4 and 4.3, II Theorems 2.1–2.2 and 4.1 | Continuous dilation spaces, general cutoff kernel and Hardy-space zero tests. Part II compares two subspaces' distances for general targets. | Their distance comparison uses continuous spaces and parameter \(r\), without an ordinary integer cutoff \(N\) or the explicit arithmetic coefficients above. [Part I](../../sources/prefix_formula62_generalL/dfmr1_arxiv.pdf) · [Part II](../../sources/prefix_formula62_generalL/dfmr2_arxiv.pdf) |
| rStation papers 4 v1 and 48 v2, Lemma 1/Theorem G and §9 respectively | Projected nonconstant target regularity and insertion of \(W/\zeta\) into the logarithmic Perron formula. | Paper 4's target is the approximable part of the constant under a finite-off-line hypothesis, with simplicity and a negative moment. Paper 48 obtains an optimal infimum for that setting by adaptive coefficient changes. These are close method antecedents for general numerators. The proposed array uses the initial taper without adaptive corrections because its quotient has only simple poles with controlled residues. [Paper 4 v1](../../sources/ratio62_rstation48/rstation_4_v1.md) · [RST048 v2 §9](../../sources/ratio62_q1_priority/rstation_48_v2.md) |

The existing primary-text audit of logarithmic coefficient families also examines the continuous log target and divergent pointwise or frozen-coefficient approximations. The earlier hard \(\Lambda\) truncation in the factorial-target antecedent audit is a different finite array with a cutoff dilation to match initial cells. Its recorded norm-defect claim concerns that displayed array and remains a separate review item. It neither supplies a proof nor obstructs this tapered construction. [Báez-Duarte continuous log-target audit](../growing_logarithmic_riesz_priority_skeptic_round4.md) · [Hard truncation calculation](jump_generator63_antecedents.md#the-exact-von-mangoldt-coefficients-and-a-failed-direct-truncation)

## Search limits

Queries combined Nyman–Beurling and Báez-Duarte with Mangoldt, prime coefficients, Cesàro, Riesz mean, Selberg taper, logarithmic derivative, eta derivative, logarithmic factorial, prescribed approximation, and general targets. I checked the linked primary proof or statement passages and the cited version locators. De Roton's 2009 *Une approche séquentielle de l'hypothèse de Riemann généralisée* remains a relevant sequential candidate. The available publisher and HAL records describe a GRH-conditional sequence for an indicator target. Four publisher and HAL PDF routes returned access errors in this follow-up, so the full construction supplies no basis for a comparison here. The presence of classical components and this bounded search leave exact historical attribution of the combined factorial-target norm result open. [De Roton 2009 publication](https://doi.org/10.1016/j.jnt.2009.05.017) · [HAL author deposit](https://hal.science/hal-00091966v2) · [Earlier retrieval receipts](../../sources/prefix_formula62_generalL/retrieval_status.md)
