# Montgomery 1973: original-source reconstruction and historical dependency audit

Date: 2026-11-17. Source: **PAPER-E009**, H. L. Montgomery, *The pair correlation of zeros of the zeta function*, in *Analytic Number Theory* (St Louis, 1972), Proc. Sympos. Pure Math. 24 (1973), 181–193, DOI [10.1090/pspum/024/9944](https://doi.org/10.1090/pspum/024/9944). All thirteen original printed pages were read from the author-hosted scan, not from an abstract or later paraphrase. Equations on pp185–186,189–191 were also checked visually because the scan's OCR loses signs and exponents. Source PDF, extracted text, selected page images, download URL/hash and Crossref metadata are private in `sources/montgomery_original_round2/` and must not be redistributed in the public archive.

**Scope:** whole-work substantive reading (L1). The central explicit-formula/mean-square proof and the multiplicity deduction are reconstructed below; the latter has an independent targeted review. This is not an independent reproof of Landau's starting explicit formula, the Montgomery–Vaughan mean-value theorem, the prime number theorem with remainder, or all of the paper's class-number and character-average side assertions. Do not promote the entire paper to L2 merely because its main theorem is familiar. No novel mathematics or RH proof is claimed.

## 1. Exact original statement; no modern endpoint silently inserted

Put

\[
 H_T=\frac{T}{2\pi}\log T,\qquad
 w(u)=\frac4{4+u^2},\qquad
 F_M(\alpha,T)=H_T^{-1}\sum_{0<\gamma,\gamma'\le T}
       T^{i\alpha(\gamma-\gamma')}w(\gamma-\gamma').
\]

The summation is over the **multiset** of nontrivial zeros, counting multiplicities. The paper opens (p181): RH is assumed throughout and \(\rho=1/2+i\gamma\). The unnumbered main theorem on that page says, under RH:

* for real \(\alpha\), \(T\ge2\), \(F_M\) is real and even;
* for every \(\varepsilon>0\), for \(T>T_0(\varepsilon)\), \(F_M(\alpha,T)\ge-\varepsilon\) for **all** real \(\alpha\);
* for each fixed \(0\le\alpha<1\),
  \[
  F_M(\alpha,T)=(1+o(1))T^{-2\alpha}\log T+\alpha+o(1),
  \]
  uniformly on \(0\le\alpha\le1-\varepsilon\) for each fixed positive \(\varepsilon\).

The next paragraph says that with more effort one **could** obtain uniformity through \(\alpha=1\). That sentence is not the proof of that endpoint assertion. The later formula with explicit \(O((\log T)^{-1/2})\) and closed interval \([0,1]\) must be attributed to later work, not copied into the 1973 theorem. The first error above is relative to a peak which is as large as \(\log T\); it is not a uniformly additive \(o(1)\) replacement of the peak.

On pp183–184, \(F_M(\alpha,T)=1+o(1)\) for \(\alpha\ge1\), uniformly in bounded intervals, is a **conjectural extension** supported by heuristics. The interval pair-correlation conjecture (12), the determinant higher-correlation suggestion (15), and the extreme-gap statements (16)–(17) are not proved by the theorem. The interval formula has a diagonal mass \(\delta(a,b)=1\) if \(0\in[a,b]\); endpoint conventions at the atom require care and are immaterial to the smooth-test statements audited here.

## 2. Proof dependency graph

```
Landau's explicit formula [2,p353], with symmetric zero ordering
 + zeta Euler logarithmic derivative for Re(s)>1
 + functional equation logarithmic derivative / gamma estimates
 + RH: rho=1/2+i gamma
    -> Lemma (18), pp185–186, all x>=1, real t, fixed 1<sigma<2
    -> specialize sigma=3/2: L(x,t)=R(x,t)

local zero count N(u+1)-N(u)=O(log(u+2)) [8,Thm9.2]
 + elementary convolution integral of two Cauchy kernels
    -> zero-side norm identity (26), pp187–188

Montgomery–Vaughan mean value (28), then 'to appear' [5]
 + PNT with remainder + partial summation
    -> prime-side norm (29), p189
 + pole/gamma remainder norms (27),(30),(31)
 + Cauchy–Schwarz / three overlapping x ranges
    -> main theorem uniformly alpha<=1-epsilon, pp189–190

finite Fourier identity (3),(4)
 + fixed compact support inside (-1,1)
    -> Corollary1 kernels (5),(6)
    -> nonnegative sinc-square summands + multiplicity inequality
    -> Corollary2: at least2/3 simple, pp191–192

nonnegative Fourier transform of spatial triangular kernel
 + global F>=-epsilon (or stronger exact positive-definiteness below)
 + main theorem on compact subintervals of (-1,1)
    -> Corollary3 small-gap bound, p192
```

These are mathematical dependencies, not a claim that every cited antecedent has been independently audited. Original reference[8] is Titchmarsh **1951**, not the 1986 second edition used in another observatory campaign. Reference[5] is Montgomery–Vaughan, *Hilbert's inequality*, then described as “to appear”.

## 3. Explicit formula (18), with signs, exponents and uniformity retained

For fixed \(1<\sigma<2\), all \(x\ge1\) and real \(t\), with \(\tau=|t|+2\), the lemma on p185 reads

\[
\begin{split}
 (2\sigma-1)\sum_\gamma
 \frac{x^{i\gamma}}{(\sigma-1/2)^2+(t-\gamma)^2}
={}&-x^{-1/2}\left\{
 \sum_{n\le x}\Lambda(n)(x/n)^{1-\sigma+it}
 +\sum_{n>x}\Lambda(n)(x/n)^{\sigma+it}\right\}\\
 &+x^{1/2-\sigma+it}(\log\tau+O_\sigma(1))
 +O_\sigma(x^{1/2}\tau^{-1}).
\end{split} \tag{M18}
\]

Both big-O constants depend only on the fixed \(\sigma\); they are uniform in \(x,t\). The final error is deliberately coarse; the preceding exact identity (22) separates a pole term \(O_\sigma(x^{1/2}\tau^{-2})\) and a trivial-zero term \(O_\sigma(x^{-2}\tau^{-1})\).

The initial Landau identity on p185 is unconditional, for \(x>1\) not a prime power and away from poles:

\[
 \sum_{n\le x}\Lambda(n)n^{-s}
 =-\frac{\zeta'}\zeta(s)+\frac{x^{1-s}}{1-s}
 -\sum_\rho\frac{x^{\rho-s}}{\rho-s}
 +\sum_{n\ge1}\frac{x^{-2n-s}}{2n+s}.
\]

The original zero sum here is not naively absolutely convergent; use the standard symmetric-height ordering in its cited explicit formula. Under RH, evaluating at \(s=\sigma+it\) and \(1-\sigma+it\), multiplying by appropriate powers of \(x\), and subtracting turns the two simple denominators into

\[
 \frac{1}{\sigma-1/2+i(t-\gamma)}
 -\frac{1}{1/2-\sigma+i(t-\gamma)}
 =\frac{2\sigma-1}{(\sigma-1/2)^2+(t-\gamma)^2}.
\]

This subtraction yields an absolutely convergent final zero sum (local zero counting gives \(\sum_\gamma(1+|\gamma|)^{-2}<\infty\)). Thus the final object is independent of the initial symmetric ordering. For \(\sigma>1\), replacing the Euler logarithmic derivative by \(-\sum\Lambda(n)n^{-s}\) supplies the \(n>x\) tail. The functional equation supplies

\[
 \frac{\zeta'}\zeta(1-\sigma+it)
 =-\frac{\zeta'}\zeta(\sigma-it)-\log\tau+O_\sigma(1)
 =-\log\tau+O_\sigma(1).
\]

There is no branch choice of \(\log\zeta\) in this logarithmic derivative calculation. The prime terms at the splitting point have identical weights when \(n=x\), so their sum is continuous through every prime power. This, and continuity of the final absolutely convergent zero expression, extends the result to the previously excluded \(x=1,p^j\). No jump term remains after the subtraction.

**Exact RH entry:** the replacement \(\rho=1/2+i\gamma\) makes the kernel in (M18) a real Cauchy kernel with a common width. For \(\rho=1/2+\delta+i\gamma\) the correct denominator would be \((\sigma-1/2)^2+((t-\gamma)+i\delta)^2\) and there would be a factor \(x^{\delta+i\gamma}\). Discarding \(\delta\) is not an unconditional explicit formula. BGSTB retain those terms instead.

## 4. Zero-side norm: normalization and tails

At \(\sigma=3/2\), set

\[
 L(x,t)=2\sum_\gamma\frac{x^{i\gamma}}{1+(t-\gamma)^2}.
\]

Then \(L=R\) from (M18). Since \(x\) is positive and the \(\gamma\)'s are real, expanding \(|L|^2\) gives Eq(23). The local bound \(N(u+1)-N(u)\ll\log(|u|+2)\) implies, for \(0\le t\le T\),

\[
 \sum_\gamma\frac1{1+(t-\gamma)^2}\ll\log(T+2),
\]
\[
 \sum_{\gamma\notin(0,T]}\frac1{1+(t-\gamma)^2}
 \ll\log(T+2)\left(\frac1{1+t}+\frac1{1+T-t}\right).
\]

Products and integration cost \(O(\log^3(T+2))\). The same local estimates allow extension of the integral for the truncated double sum to all real \(t\), with the same error. These errors are uniform in \(x\) because \(|x^{i(\gamma-\gamma')}|=1\).

The elementary convolution is

\[
 \int_{\mathbb R}\frac{dt}{(1+(t-\gamma)^2)(1+(t-\gamma')^2)}
 =\frac{2\pi}{4+(\gamma-\gamma')^2}=\frac\pi2 w(\gamma-\gamma').
\]

Consequently Eq(26) is exactly

\[
 \int_0^T|L(T^\alpha,t)|^2dt
 =T\log T\,F_M(\alpha,T)+O(\log^3T),\quad\alpha\ge0.
\]

The factors \(4\), \(\pi/2\), \(2\pi\) and \(H_T\) match. The left side yields the original approximate global nonnegativity. Evenness gives the negative \(\alpha\) range.

**Stronger elementary observation, separate from the printed statement.** For any finite real multiset of ordinates,

\[
 w(u)=\int_{\mathbb R}e^{-2|v|}e^{iuv}dv,
\quad
 H_TF_M(\alpha,T)=\int_{\mathbb R}e^{-2|v|}
 \left|\sum_{0<\gamma\le T}e^{i\gamma(\alpha\log T+v)}\right|^2dv\ge0.
\]

Thus this finite-sum function is in fact exactly nonnegative. This elementary strengthening needs no zero asymptotic and, as an identity about real lists, no RH. It does **not** make the prime-side formula unconditional; it also does not identify multiplicities of full complex zeros from ordinates in the absence of RH. No originality claim is made for this positive-definite kernel observation.

## 5. Prime-side mean square independently unpacked

Ignoring the harmless factor \(x^{it}\), the prime expression at \(\sigma=3/2\) is a Dirichlet series with coefficients

\[
 a_n(x)=\begin{cases}\Lambda(n)\sqrt n/x,&n\le x,\\
                    x\Lambda(n)/n^{3/2},&n>x.\end{cases}
\]

The mean-value input (28) gives

\[
 \int_0^T\left|\sum a_n n^{-it}\right|^2dt
 =T\sum a_n^2+O\!\left(\sum n a_n^2\right).
\]

The hypotheses needed for applying the infinite-series form are satisfied: both \(\sum a_n^2\) and \(\sum n a_n^2\) are finite at each fixed \(x\). Approximation by finite Dirichlet polynomials plus the same bound justifies passage to the limit in \(L^2[0,T]\). This is the nontrivial Montgomery–Vaughan input, not a consequence of merely formal orthogonality on a finite interval.

From PNT with a remainder and partial summation,

\[
 \sum_{n\le y}\Lambda(n)^2=y\log y+O(y),
\]

and more precisely enough to integrate with bounded constant error. Therefore

\[
\begin{split}
 \sum a_n^2
 &=x^{-2}\sum_{n\le x}n\Lambda(n)^2
   +x^2\sum_{n>x}\Lambda(n)^2/n^3\\
 &=\left(\tfrac12\log x+O(1)\right)
   +\left(\tfrac12\log x+O(1)\right)=\log x+O(1),
\end{split}
\]

and \(\sum n a_n^2\ll x\log(2x)\). This recovers Eq(29) as

\[
 T(\log x+O(1))+O(x\log x),\qquad x\ge1,
\]

with \(\log(2x)\) available in the error if desired at \(x=1\); the \(O(T)\) absorbs that endpoint. The two halves each supply half of the leading \(\log x\). Prime powers with exponent at least two change lower-order terms, not this coefficient.

The other squared norms, Eqs(27),(30),(31), are

\[
 M_{\log}=\frac{T}{x^2}(\log^2T+O(\log T)),\qquad
 M_{\mathrm{gamma\ error}}\ll T/x^2,\qquad
 M_{\mathrm{pole\ error}}\ll x.
\]

Cauchy–Schwarz controls all cross terms. Montgomery uses three ranges:

1. \(1\le x\le(\log T)^{3/4}\): the logarithmic term dominates; the others have relative \(o(1)\) squared norm.
2. \((\log T)^{3/4}<x\le(\log T)^{3/2}\): every squared norm is \(o(T\log T)\).
3. \((\log T)^{3/2}<x\le T/\log T\): the prime squared norm is \((1+o(1))T\log x\); the other terms are negligible relative to it.

These statements hold uniformly in each stated range. For example, at the upper edge of range3, \(x\log x/(T\log x)\le1/\log T\). For each fixed positive \(\varepsilon\), \(x=T^\alpha\), \(0\le\alpha\le1-\varepsilon\), eventually lies in their union. They prove the original uniform theorem. At \(x=T\), the error \(O(x\log x)\) is as large as the desired \(T\log T\) main term, so these estimates alone do not prove the endpoint. This is a limitation of this estimate, not a theorem that endpoint progress is impossible.

For \(\alpha>1\), p190 Eq(32) retains the explicit pole term and explains that off-diagonal sums can no longer be ignored. Their organization into shifted prime correlations \(\sum_{n\le y}\Lambda(n)\Lambda(n+h)\) is the proposed arithmetic route. The paper does not state a complete, quantified, proved error hypothesis for all those shifts; “reasonably small” and “independent” in that discussion are heuristic requirements. The character-average analogue (34) and its GRH improvement are discussed separately; neither is a proof of the zeta pair-correlation conjecture.

## 6. Fixed tests, Fourier support and the exact simplicity deduction

Use Fourier convention \(\widehat r(\alpha)=\int r(u)e^{-2\pi i\alpha u}du\). The finite-sum identity (3) is

\[
 \sum_{0<\gamma,\gamma'\le T}
 r\!\left(\frac{(\gamma-\gamma')\log T}{2\pi}\right)w(\gamma-\gamma')
 =H_T\int F_M(\alpha,T)\widehat r(\alpha)d\alpha.
\]

For a fixed sufficiently regular test with \(\operatorname{supp}\widehat r\subset[-a,a]\), \(a<1\), and \(\widehat r\) continuous at zero, the theorem gives the limiting functional

\[
 \widehat r(0)+\int_{-a}^a|\alpha|\widehat r(\alpha)d\alpha.
\]

Here \(\log T\,e^{-2|\alpha|\log T}\) has total mass1 on the real line and tends to a Dirac mass at0. This explains why dropping the narrow peak would lose the \(\widehat r(0)\) term.

For \(r_a(u)=(\sin\pi a u/(\pi a u))^2\),

\[
 \widehat r_a(\alpha)=\frac{(a-|\alpha|)_+}{a^2},\quad
 \widehat r_a(0)=1/a,\quad
 \int |\alpha|\widehat r_a(\alpha)d\alpha=a/3.
\]

Thus Eq(6), p182, is

\[
 \sum_{\gamma,\gamma'}
 \left[\frac{\sin((a/2)(\gamma-\gamma')\log T)}{(a/2)(\gamma-\gamma')\log T}\right]^2
 w(\gamma-\gamma')\sim(1/a+a/3)H_T,\quad0<a<1\ \text{fixed}.
\]

Every summand is nonnegative under RH. The equal-ordinate diagonal equals

\[
 M_2(T)=\sum_{\rho\ \mathrm{distinct},\ 0<\gamma\le T}m_\rho^2.
\]

This is not merely the usual count \(N(T)=\sum m_\rho\). It follows that, for each fixed \(a<1\), \(\limsup M_2/H_T\le1/a+a/3\). First let \(T\to\infty\), then \(a\uparrow1\): \(\limsup M_2/H_T\le4/3\). No theorem at the unsupported moving endpoint \(a=1\) is used.

For every positive integer \(m\), \(\mathbf1_{m=1}\ge m(2-m)\): equality holds at \(m=1,2\), and the right side is negative for \(m\ge3\). Summing over distinct zeros gives

\[
 N_{\mathrm{simple}}(T)\ge2N(T)-M_2(T)
 \ge(2/3+o(1))H_T.
\]

Equivalently, Montgomery sums \(2-m_\rho\) over the zero multiset. The apparently unusual sum \(\sum_\gamma m_\rho\) in the source therefore means \(\sum_{\rho\ distinct}m_\rho^2\), as its surrounding paragraph explicitly explains. It is not a mistaken extra multiplicity.

**Why RH matters for this positivity argument.** The entire function \(r_a(z)\) is nonnegative on the real axis, but is not pointwise nonnegative at arbitrary complex arguments. Without RH the natural normalized argument is \(i(\rho-\rho')\log T/(2\pi)\), which may be nonreal. Furthermore equal ordinates need not identify the same complex zero. Replacing all complex differences by their imaginary parts preserves an elementary positive kernel but loses the established unconditional prime-side identity. No unconditional 2/3 theorem follows from the original argument by dropping the words “assume RH”.

**Weight removal, separately reconstructed.** It is not needed for the diagonal simplicity bound. For fixed \(a>0\),

\[
 0\le r_a(\Delta\log T/2\pi)(1-w(\Delta))
 \le\frac{4}{a^2\log^2T}\frac1{4+\Delta^2}.
\]

The local zero count bounds \(\sum_{\gamma'}(4+(\gamma-\gamma')^2)^{-1}\ll\log T\); hence the total difference between weighted and unweighted sinc-square sums is \(O_a(T)\), which is \(o(H_T)\). The constant depends on fixed \(a\); no changing-bandwidth uniformity is asserted. This proves the sentence after Eq(6) permitting removal of \(w\), under the paper's RH setting.

## 7. Small gaps: a rigorous supplemental certificate for the printed 0.68

The spatial triangular test \(r(u)=(1-|u|/\Lambda)_+\) has nonnegative integrable transform \(\widehat r(\alpha)=\Lambda\operatorname{sinc}^2(\pi\Lambda\alpha)\). Global lower nonnegativity of \(F\) allows restriction to \(|\alpha|<1\), first with a fixed interior cutoff and then letting it tend to1. The resulting lower bound for the full pair sum is

\[
 \left(\Lambda+\frac{\operatorname{Cin}(2\pi\Lambda)}{\pi^2\Lambda}+o(1)\right)H_T,
 \quad\operatorname{Cin}(x)=\int_0^x\frac{1-\cos u}{u}du.
\]

If infinitely many zeros are multiple, the normalized liminf gap is0 already. Otherwise eventually all are simple and the equal-ordinate contribution is \((1+o(1))H_T\). Since the spatial test and \(w\) are at most1 and vanish outside the required gap range, a positive value of

\[
 C(\Lambda)=\Lambda+\operatorname{Cin}(2\pi\Lambda)/(\pi^2\Lambda)-1
\]

forces infinitely many positive gaps below \(2\pi\Lambda/\log T\). The conversion to the consecutive-gap liminf is valid: among two distinct ordinates a consecutive intervening gap is no larger, and any fixed finite set of low zeros contributes only \(o(H_T)\) pairs to the shrinking window. Since \(\gamma\le T\), the normalization by \(\log\gamma\) only improves the upper bound. This reconstructs the proved small-gap part of Corollary3.

`experiments/code/montgomery_original_checks.py` gives an **exact rational** supplemental certificate \(C(17/25)>0.008\), using the classical external rational bounds \(333/106<\pi<355/113\) and twenty terms of the alternating Cin series. Its decimal display is not the proof; the saved Fraction inequality is. The source's positive-density and large-gap refinements on p183 are described as requiring a more complicated argument, not supplied in full here; this audit does not invent that missing proof.

## 8. Local typography issue, not a failed theorem

The unnumbered triangular-transform integral on p191 visibly prints

\[
 a^{-2}\int_{-a}^a(a-\beta)F_M(\beta)\,d\beta
\]

where the Fourier transform requires \((a-|\beta|)\). Both this agent and the independent reviewer inspected the actual page image; the issue is not created by OCR. The proposed local repair is forced by evenness of the transform and by direct convolution of two boxes. At \(\beta=-a/2\), the printed factor would be \(3/(2a)\) while the transform is \(1/(2a)\); its printed mass is2 rather than \(r_a(0)=1\). The correctly stated Corollary1(6) has \(1/a+a/3\), consistent with the repaired display. The proof and resulting 2/3 theorem remain valid after this local typographic repair.

This is recorded as a **verified local mathematical transcription/typography defect**, not an assertion that Montgomery's theorem is erroneous. Parent adjudication is required before adding to any public list of issues. No independently verified formal corrigendum was located in a limited exact-title/erratum search; this is not an exhaustive negative bibliography claim.

## 9. Comparison with two later original sources

Only the following passages of the later sources were reread for this comparison; this does not add new whole-work read counts.

**BGSTB, PAPER-A006, arXiv2306.04799v1, Theorem1 pp1–2; Lemmas1,3 pp3–4; Lemma5 p6.** Their unconditional function is

\[
 F_B(\alpha,T)=H_T^{-1}\sum_{0<\gamma,\gamma'\le T}
 T^{\alpha(\rho-\rho')}\frac4{4-(\rho-\rho')^2}.
\]

On RH this equals \(F_M\); off RH it is a different function from an ordinate-only sum. Theorem1 gives real/even/nonnegative and

\[
 F_B=T^{-2\alpha}(\log T+O(1))+\alpha+O((\log T)^{-1/2}),
 \quad0\le\alpha\le1\ \text{uniformly}.
\]

The source expressly attributes the endpoint/error improvement to Goldston–Montgomery1987, Lemma8. That antecedent has not been read in this task. Their Lemma3 supplies a full-real-line squared-modulus representation using the reflected zero \(1-\overline\rho\), proving positivity of the **whole** sum; individual off-line summands need not be nonnegative. Lemma5 requires a fixed real even \(r\in L^1\), support in \([-1,1]\), Lipschitz at0. These are meaningful changes of function/hypotheses and not a restatement of a hidden unconditional 1973 theorem.

**Lamzouri, PAPER-A003, arXiv2609.02882v2, §3 pp12–13 and Lemma3.2.** This explicitly imports BGSTB Lemma5, then applies a new finite conjugation-invariant multiset inequality to complex zeros. It cannot use Montgomery's old termwise positivity at complex differences. For a fixed smooth even window, put \(Q=\eta^2*\eta^2\), \(K=\widehat{\eta^2}\), \(z=i(\rho-\rho')\log T/(2\pi)\). The exact identity

\[
 \widehat{Q-Q''/(4\log^2T)}(z)\frac4{4-(\rho-\rho')^2}=K(z)^2
\]

follows from \(\widehat{Q''}(z)=-4\pi^2z^2\widehat Q(z)\). The changing test is handled by applying the fixed-test theorem separately to \(Q\) and \(Q''\), not by silently assuming uniformity over a family of tests. The arithmetic input remains pair correlation; the new finite inequality supplies a replacement for the missing real-axis positivity argument. The updated2026 result does not turn its historical1973 antecedent into an unconditional theorem retroactively.

## 10. Reusable questions, with exact next steps

1. **Effective fixed-test transfer.** For \(Q,Q''\in C_c^\infty(-1,1)\), derive explicit constants in BGSTB Lemma5 in terms of \(\|Q\|_1,\|Q''\|_1\), local Lipschitz constants and height. Apply the two fixed tests separately to make Lamzouri's finite-height lower bounds quantitative. No prime-pair conjecture is required for this first goal.
2. **Beyond the proven Fourier bandwidth.** Starting from original Eq(32), specify the exact weighted shifted-prime sums and uniform \((h,y,x,T)\) error sufficient for a fixed support \([-1-\delta,1+\delta]\). “Hardy–Littlewood on average” is too vague unless the weights and error sum are written. The original paper identifies the obstacle but does not solve it.
3. **General finite inequality.** If a nonnegative real pair kernel with unit diagonal has total pair sum at most \(C N\), then \(N_{\rm simple}\ge(2-C)N\) and \(N_{\rm distinct}\ge(3-C)N/2\), the latter from the pointwise integer inequality \(1\ge(3m-m^2)/2\). In particular the historical \(C=4/3+o(1)\) gives a derived distinct proportion of at least5/6; this is not separately attributed as an original stated corollary. Determine which complex-zero tensor replacements preserve the required charge for simple *critical* zeros. Existing Lamzouri results already realize one such replacement; do not present this as a new discovery.

## Audit outcome and counts

One new work bibliographically verified, accessed, and substantively read in full: PAPER-E009, thirteen pages. One independent targeted reviewer reconstructs the multiplicity deduction and confirms the local transform repair. Original main-theorem and proof dependencies are now explicit; original whole-work L2 remains unclaimed. Two already-recorded later works received targeted comparison reading, not new corpus entries. No verified error in the main theorem, no RH advancement claim, and no distribution of source scans.
