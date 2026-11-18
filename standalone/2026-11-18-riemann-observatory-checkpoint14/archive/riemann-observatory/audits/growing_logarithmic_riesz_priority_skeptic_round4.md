# Priority investigation of the moving logarithmic Riesz array

Search/read cutoff:2026-11-17. Investigator `/root/li_skeptic`. **Priority remains unassessed.** This investigation recovered and read Lee's original six-page article and compared several additional actual primary-source passages. No inspected source has yet been found to state the exact moving array and critical weighted norm. That bounded search result is not evidence of historical novelty.

## Exact object whose provenance is being tested

For every fixed `c>0`, put `L=log N`, `epsilon_N=c/loglog N`, and `alpha_N=epsilon_N L`. The independently reconstructed RH-conditional proposition concerns

\[
 V_N(s)=\sum_{n\le N}\mu(n)
 (1-\log n/\log N)^{\alpha_N}n^{-s},
\]

and convergence to zero of

\[
 d_q(V_N)^2=\frac1{2\pi}\int_\mathbb R
 |1-\zeta(\tfrac12+it)V_N(\tfrac12+it)|^2
 |\tfrac12+it|^{-2q}\,dt
 \qquad(q\ge1\text{ fixed}).
\]

The order grows like `c log N/loglog N`, while `alpha_N/log N` tends to zero. The claimed rate is `d_q=O_(q,c)((loglog N)^(-1/3))`; it is the same scale as an earlier shifted-array reconstruction, not a better RH bound. The formal logarithmic Riesz means and their Perron formula are classical. The unresolved priority question is the particular simultaneous order/cutoff choice and the weighted product convergence, not the invention of Riesz summability or variable orders.

## 1. Lee1996: actual original recovered, endpoint explicitly absent

**PAPER-LRP001** is Jungseob Lee, *Convergence and the Riemann hypothesis*, Communications of the Korean Mathematical Society11(1)(1996),57–62. The official publisher dates printing to1March1996. The primary PDF was recovered from the current KMS archive, rather than inferred from later citations:

- Landing: `https://ckms.kms.or.kr/journal/view.html?uid=1217`.
- PDF: `https://ckms.kms.or.kr/journal/download_pdf.php?spage=57&volume=11&number=1`.
- Local: `sources/logarithmic_riesz_priority_skeptic_round4/lee1996.pdf`; SHA256 `debbc5132b4338e06b8f2d81cb20ab8c47051e1d4e0cda15af713077c9ef4099`.

All six pages were substantively read; the theoremp59 and central passagespp60–61 were also visually checked. The theorem states, for fixed `1<p<=2`, equivalence between no zeta zeros in `Re(s)>1/p` and convergence of

\[
 f_N(x)=\sum_{n\le N}\mu(n)\{1/(nx)\}
 \longrightarrow-1
\]

in every fixed `L^r(0,1)` with `1<r<p`. It also gives density statements for the constrained Beurling spaces with real/rational dilation parameters. The sum uses **`n<=N`**, as the actual typeset theorem makes clear. Equation(2),p60, subtracts `(sum mu(n)/n){1/x}` to satisfy the coefficient constraint.

This is the earlier arithmetic Beurling theorem expressly credited by Balazard–Saias, *Notes1*,p320. It is historically important and must be attributed to Lee when the dependency is discussed. It contains no growing logarithmic taper and at `p=2` omits the critical `L²` norm. It is therefore not an exact earlier statement of the proposition being tested.

Reading is not an audit of every proof transition. In particular the printed Perron argument onp59 displays an infinite positive absolute-majorant integral which diverges as written; the intended fixed-distance estimate requires a legitimate truncated contour or another argument. The theorem is not thereby disproved; the later Balazard–Saias route supplies an independently reconstructed proof of the fixed-distance convergence result. This investigation does not promote a new error claim about Lee's main theorem.

## 2. Báez-Duarte2000: natural arrays and a frozen-series barrier

Actual primary preprint `arXiv:math/0011254v1`, *Arithmetical Aspects of Beurling's Real Variable Reformulation of the Riemann Hypothesis*, dated20October2000 internally and posted29November2000, was downloaded. The introduction/definitionspp1–5, the relevant divergence statements and proofspp17–20, and references were read; the whole21-page paper was not read. Its later related publication is *New versions of the Nyman-Beurling criterion for the Riemann hypothesis*, IJMMS31(7)(2002),387–406, DOI10.1155/S0161171202013248. The publisher-quality PDF was not recovered here; a degraded published-text preview confirms matching introductory definitions and main-result descriptions but not every revision.

The exact sequences in preprint Eqs1.14–1.19,pp4–5, include the unsmoothed Möbius sums and two different coefficient-constraint corrections; its `F_n` there is a dual approximation with uniformly spaced dilation parameters, not a growing Riesz power. Proposition4.4,p17, states that the unsmoothed sequence and its anchored version diverge in the endpoint `L^p` if there is a zero on `Re(s)=1/p`. Proposition4.7,pp19–20, rules out convergence of a series with **fixed coefficients** in the natural constrained generators at such an endpoint. These facts explain why taking Lee's `r` to `p` is not permitted.

The moving taper depends on `N` even for coefficients already present at smaller cutoffs. It is not the sequence of partial sums of one fixed-coefficient series. Thus the source's frozen-series obstruction is compatible with the proposed array, even though its individual coefficients tend to the natural Möbius values. No moving order of the particular size above was found in the inspected passages. This does not establish absence from all remaining passages or from the broader literature.

## 3. Defant–Schoolmann: exact logarithmic means, different growth domain

Actual primary text: arXiv2107.10145v3,22March2022, *Riesz summability on boundary lines of holomorphic functions of finite order generated by Dirichlet series*. Published metadata: Mathematische Zeitschrift303(4)(2023), article102, DOI10.1007/s00209-023-03235-4. The manuscript's definitions, classical restatements and comparisonpp1–10, Perron formula and boundary theoremspp15–18, and selected references were read. The complete38-page proof was not audited, and the journal mathematical version was not compared.

For a frequency `lambda_n`, its means are exactly `sum_(lambda_n<x) a_n exp(-lambda_n s)(1-lambda_n/x)^k`; choosing `lambda_n=log n` gives the same **first-kind logarithmic** convention. Theorem4.1,p15, and Remark4.2,p16, give the exact gamma/Perron kernel and complex kernel mass. These are genuine prior machinery, not new ingredients of the archive's construction.

However the boundary theorem, Theorem5.1,p17, assumes fixed `k>ell>=0` and a function in the space defined by Eq22,p9:

\[
 \sup_{\operatorname{Re}z>0}|f(z)/(1+z)^\ell|<\infty.
\]

Take the prospective reciprocal function `f(z)=1/zeta(1/2+z)`. Under RH it is holomorphic on the open right half-plane, but near every boundary zero `1/2+i gamma`, its modulus tends to infinity as `Re z` decreases to zero with `Im z=gamma`. The factor `(1+z)^ell` stays finite there. Thus it belongs to **none** of these finite-order uniform-growth spaces. This is an exact failed-hypothesis check, not a claim that the general theorem is weak or incorrect.

Their Theorem1.2,p8, restates a classical Riesz boundary theorem allowing **finitely many** boundary poles of orders below `k+1` and a uniform large-height polynomial bound. Reciprocal zeta has infinitely many such boundary poles, so this version is also not directly applicable. Their appendix supplies a proof of that classical statement, but that appendix and Riesz's original1909 note were not read in this investigation.

Consequently these inspected theorems do not themselves imply the moving-order weighted **product** norm. They supply the formal kernel and illuminate the missing uniform-boundary hypothesis which the moving-array proof bypasses with an explicit RH near-line bound and a paid kernel tail. Whether another theorem in this general theory subsumes the construction remains a priority question.

## 4. Variable order already exists, but the located theorem has a different regime

Actual primary text: Shakro Tetunashvili, *On Divergence of Fourier Series by Some Methods of Summability*, Journal of Function Spaces and Applications2012, article542607, DOI10.1155/2012/542607. The paper is nine pages; the downloaded ten-page file ends with an unrelated advertising page. Its introduction/triangular matrix definitions, Theorems1.3–1.4,pp5–7, and Remark2.4,pp8–9, were read; the full proofs were not audited.

Remark2.4 explicitly defines variable-order arithmetic Riesz weights `(1-k/(n+1))^(alpha_n)`. The discussed hypotheses are `alpha_n<=C/log n` with `C<log2`, in particular orders tending to zero, and the conclusions are Fourier-series divergence examples. The frequency is arithmetic, the order regime is the opposite of the present growing order, and neither Möbius coefficients nor the critical weighted zeta product occurs. This source decisively prevents describing variable-order Riesz summability itself as a new concept, but is not an exact antecedent of the claimed norm criterion.

## 5. Wintner–Ingham–Segal: actual later primary comparison, originals still missing

The actual eight-page article by Kanemitsu, Kuzumaki and Tanigawa, *On the Wintner-Ingham-Segal summability method*, Hardy–Ramanujan Journal41(2018),40–47, DOI10.46298/hrj.2019.5104, was retrieved from the journal. The volume year2018 and DOI online date23January2019 must be distinguished. Its initial definitions, Eq1.1, the fixed smoothing class, Eqs3.18–3.19 and Theorem3.4, plus references were inspected. This was scoped reading, not an audit of the full argument.

Its Ingham mean is `x^(-1)sum_(d<=x) d a_d floor(x/d)`. Its generalized smoothing uses a **fixed** function `F(k/r)` satisfying the stated monotonicity, endpoint and prime-number-theorem decay conditions. It is an arithmetic Dirichlet-convolution summability theorem, not an `N`-dependent logarithmic Riesz order or a boundary `L²` product theorem. Substituting `F=F_N`, changing arithmetic frequencies to `log n`, and then asserting weighted uniformity would require additional arguments absent from those inspected statements.

This source led to Wintner's *Eratosthenian averages*(1943) and *On Arithmetical Summation Processes*, Amer.J.Math.79(3)(1957), DOI10.2307/2372562. The original1957 full text was **not** obtained: the JSTOR URLs returned a challenge HTML page with HTTP200, not a PDF. Those responses are saved and explicitly renamed as HTML. No mathematical conclusion about the unread original is drawn from its title or this later paper's description.

It also led to Segal's *Ingham's Summability Method and Riemann's Hypothesis*, Proc.LondonMath.Soc.(3)30(2)(1975),129–142, DOI10.1112/plms/s3-30.2.129, and a separate same-title one-page1977 item,34(3),438, DOI10.1112/plms/s3-34.3.438. Crossref metadata verify these are distinct items; the later article's abbreviated reference must not be mistaken for primary-source access. Neither original was read. Their exact statements and any correction history remain high-priority continuation tasks.

## Search coverage and continuation

Methods actually used included exact-title searches, searches pairing Möbius/Dirichlet/Riesz with logarithmic, variable, growing, increasing and infinite-order terminology, backward references from the located primary sources, Crossref identity verification, and OpenAlex forward references to Lee. The saved OpenAlex response contains eleven citing works, including the Báez-Duarte and Balazard–Saias branch; this is that service's indexed result, not a complete citation network.

Persistent source files, retrieval metadata, failed responses and Crossref records are in `sources/logarithmic_riesz_priority_skeptic_round4/`. The executed query families and remaining access gaps are recorded in `logs/growing_logarithmic_riesz_priority_skeptic_round4.md`. No search count is being converted into a mathematical reading count.

The next precise tasks are:

1. Obtain and read Wintner1957 and Segal1975/1977, checking the exact smoothing coefficients and correction scope.
2. Inspect general variable-order typical-mean theorems, especially statements that recover Abel limits with `k/x->0`; a theorem with constants controlled through a shrinking half-plane could subsume the construction.
3. Compare the mathematical journal version of the Báez-Duarte2000 preprint and its remaining approximation mechanisms, preserving version changes.
4. Inspect the relevant remaining general-Dirichlet-series theorems or contact an expert only if separately authorized. No messages to authors or other researchers have been sent.

At this checkpoint, the correct status is **a fully written and independently checked conditional reconstruction with unassessed historical priority**. The source comparisons above give no warrant for calling it a publishably new theorem.
