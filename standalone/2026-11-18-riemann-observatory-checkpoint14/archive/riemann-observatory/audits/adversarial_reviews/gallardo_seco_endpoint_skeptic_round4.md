# Independent source and endpoint review of Proposition5.1

2026-11-17. Reviewer `/root/li_skeptic`. Canonical work: **PAPER-E012**, Eva A. Gallardo-Gutiérrez and Daniel Seco, *Zero-Free Regions of the Riemann Zeta Function and Approximation in Weighted Dirichlet Spaces*, Complex Analysis and Operator Theory19(2025), article38, DOI10.1007/s11785-025-01661-2.

**Finding:** the inclusive equality case in the printed auxiliary Proposition5.1 has an explicit counterexample. At `alpha=-3,a=1`, the stated operator is bounded and injective but is not onto. This is a local result about that operator proposition. It does not establish that the paper's main RH-related results or Theorem5.5 are false.

The operator, norm and endpoint were checked in the actual publisher PDF and arXiv2206.02654v6 before reading the other agent's endpoint audit. The polynomial and non-surjectivity calculations below were independently reconstructed. The root and equivalences agent separately reconstructed the same witnesses; the root retains final archive adjudication.

## 1. Exact source and inspected scope

Publisher PDF: `sources/logarithmic_riesz_round3/gallardo_seco2025.pdf`, SHA256 `05615ae82b3d52e7591474859f774ae2244357c7986c592590129386beea26d4`. Printed/PDFp21 Proposition5.1 was visually read in `gallardo_seco_journal_p21.png`; the surrounding definition and full proof pp21–25 were read from the extracted primary text. Definition of the norm is on publisherp3. This is targeted reading, not a whole27-page publisher audit.

Preprint PDF: `sources/logarithmic_riesz_round3/gallardo_seco2206v6.pdf`, SHA256 `0cee802b54eb53f3b9a74c02bf2b636b414c5ed3efb0ddfb4c759d9d84959939`. The arXiv stamp is5June2024 and the manuscript date is6June2024; those are distinct source dates. Its Proposition5.1 onp17 was independently rendered and visually read in `gallardo_seco_preprint_p17_skeptic.png`. The same inclusive endpoint appears in both versions. The canonical record's whole-v6 read is the equivalences agent's scope, not this reviewer's additional full read.

The source defines, for real `gamma`,

\[
 D_\gamma=\left\{f(z)=\sum_{n\ge0}a_nz^n:
       \|f\|_\gamma^2=\sum_{n\ge0}|a_n|^2(n+1)^\gamma<\infty\right\}.
 \tag{1}
\]

These are Hilbert spaces isometric to the stated weighted sequence spaces. There is no requirement `f(0)=0`, no quotient, and no boundary condition on `f` in Proposition5.1.

It defines

\[
 T_af=\frac{((1-z)^af)'}{(1-z)^a}
       =f'-\frac{af}{1-z},\qquad a>0.
 \tag{2}
\]

The branch for noninteger `a` is holomorphic on the disk; at our witness `a=1` there is no branch issue. The actual proposition says for `alpha in[-3,-2)` that `T_a:D_(alpha+2)->D_alpha` is **bijective and bounded if and only if `a>=-(1+alpha)/2`**. Thus `alpha=-3,a=1` is expressly included. Taking the permitted multiplier `h=1` also places the witness in its optional `T_(a,h)` formulation.

The paragraph describing Noor reverses the source and target of its `T` in one sentence, while the proposition and its proof use the derivative-compatible direction `D_(alpha+2)->D_alpha`. That sentence does not provide an alternate interpretation of Proposition5.1: reversing these spaces would also fail boundedness for elementary monomials. The review uses exactly the proposition's displayed mapping and norm.

## 2. Exact polynomial witness: no bounded inverse

For each integer `K>=0`, put

\[
 f_K(z)=\sum_{n=0}^Kz^n=\frac{1-z^{K+1}}{1-z},
 \quad M=K+1.
\]

Every `f_K` is in the displayed domain `D_-1`, and

\[
 \|f_K\|_{-1}^2=\sum_{m=1}^M\frac1m=H_M\longrightarrow\infty.
 \tag{3}
\]

Differentiating the exact finite identity `(1-z)f_K=1-z^(K+1)` gives

\[
 T_1f_K=-\frac{M z^K}{1-z}.
 \tag{4}
\]

Consequently

\[
 \|T_1f_K\|_{-3}^2
 =M^2\sum_{m=M}^{\infty}m^{-3}
 \le M^2\left(M^{-3}+\int_M^\infty x^{-3}\,dx\right)
 =\frac1M+\frac12\le\frac32.
 \tag{5}
\]

The normalized domain vectors `f_K/sqrt(H_M)` have norm one and image norm tending to zero. A bounded linear bijection between the two Hilbert spaces would have bounded inverse by the open mapping theorem and hence would be bounded below. Equations(3)–(5) contradict that consequence.

No numerical approximation, asymptotic norm equivalence or external zeta fact is involved in this witness. Even subtracting the constant term from `f_K` leaves a norm-divergent sequence with bounded images, so an unprinted normalization `f(0)=0` would not repair a bounded-below claim on that closed domain.

For completeness, boundedness at this endpoint can be proved directly without relying on the proposition under review. For `f=sum a_nz^n`, the derivative norm satisfies `||f'||_-3^2<=2||f||_-1^2`. The prefix-sum multiplier `f/(1-z)` has matrix

\[
 A_{nk}=\frac{\sqrt{k+1}}{(n+1)^{3/2}}1_{k\le n}
\]

after conjugating domain and range to ordinary `ell²`. With Schur weights `p_j=(j+1)^(-1/2)`, its row sums weighted by `p_k` equal `p_n`, and its column sums weighted by `p_n` are at most `2p_k`, because `sum_(n>=k)(n+1)^(-2)<=2/(k+1)`. Schur's test gives multiplier norm at most `sqrt2`. Therefore `T_1` is bounded, and the failure is not a question about an undefined operator on some domain element.

## 3. An explicit target proves actual failure of surjectivity

Define a holomorphic disk function

\[
 g(z)=\sum_{n\ge0}b_nz^n,
 \qquad b_n=\frac{n+1}{\log(n+2)}.
 \tag{6}
\]

Its radius of convergence is one. Moreover

\[
 \|g\|_{-3}^2=\sum_{n\ge0}
 \frac1{(n+1)\log^2(n+2)}<\infty
\]

by the integral test, so it is an admissible target in `D_-3`.

Suppose an analytic `f=sum a_nz^n` solves `T_1f=g`. Define `S_n=sum_(k=0)^n a_k` and `t_n=S_n/(n+1)`. Comparing Taylor coefficients in(2) gives

\[
 (n+1)a_{n+1}-S_n=b_n,
\]

and hence

\[
 t_{n+1}-t_n=\frac{b_n}{(n+1)(n+2)}
             =\frac1{(n+2)\log(n+2)}.
 \tag{7}
\]

Thus, for every possible complex choice of `a_0`,

\[
 t_n=a_0+\sum_{j=2}^{n+1}\frac1{j\log j},
 \qquad \operatorname{Re}t_n\longrightarrow+\infty.
\]

For `n>=1`, the same recurrence gives either of the equivalent exact identities

\[
 a_n=t_{n-1}+\frac{b_{n-1}}n
     =t_n+\frac{b_{n-1}}{n+1}.
 \tag{8}
\]

The added term is positive real, so `|a_n|>=1` eventually for any `a_0`. It follows that `sum |a_n|²/(n+1)=infinity`. Therefore **no analytic solution belongs to `D_-1`**. Equation(6) is a specific element of `D_-3` outside the range of the claimed operator, proving non-surjectivity rather than just failure of a uniform inverse bound.

The homogeneous solutions are `C/(1-z)`, which are not in `D_-1` unless `C=0`. Thus the endpoint operator is injective as well as bounded, while surjectivity fails. This explains why the printed final check of the homogeneous solution detects injectivity correctly but does not establish the separate claimed onto property.

## 4. The same obstruction at every printed equality endpoint

This extension is an independently derived diagnostic, not needed to refute the proposition. Fix any `alpha in[-3,-2)` and set `a=-(1+alpha)/2`, so `1/2<a<=1`. Let

\[
 c_n=(a)_n/n!,\qquad f_K=\sum_{n=0}^Kc_nz^n.
\]

The exact coefficient identity for `(1-z)^(-a)` is

\[
 (n+1)c_{n+1}=a\sum_{j=0}^nc_j.
\]

It yields

\[
 T_af_K=-a\left(\sum_{j=0}^Kc_j\right)\frac{z^K}{1-z}.
\]

The elementary gamma-ratio asymptotic `c_n~n^(a-1)/Gamma(a)` shows that the domain norm squared grows as a positive constant times `log K`, since `2a+alpha=-1`. The image norm squared remains bounded: its coefficient factor is `O(K^a)`, while `sum_(n>=K)(n+1)^alpha=O(K^(alpha+1))`, and `2a+alpha+1=0`. Hence the claimed bounded bijection fails bounded-below at **every** included equality endpoint. This suggests excluding equality in a corrected bounded-bijection statement, but this review does not purport to prove the complete strict-inequality replacement theorem.

## 5. Fair scope and next steps

The proof in the paper proceeds by constructing polynomial families, asserting that they and their images form Riesz bases, then checking injectivity through the homogeneous solution. The endpoint witnesses above show that those onto/Riesz conclusions cannot all hold as printed. No additional hypothesis in the actual proposition removes our examples. Equivalent coefficient norms, the disk branch, an invertible multiplier, or the fact that the kernel leaves the domain at equality do not resolve the failure of surjectivity.

The exact finding is a **verified counterexample to the inclusive endpoint in auxiliary Proposition5.1**, subject to the root's final classification. The other agent's independently produced note is `audits/gallardo_seco_endpoint_round3.md`; both reviews should be retained as independent reconstructions of the same work, not counted as separate papers or separate discoveries. The main zero-free-region implications in earlier sections do not depend on this calculation in any way established by this review. The downstream closure criterion needs a source-specific dependency audit before asserting its truth, falsehood or repair at the exceptional boundary. No author has been contacted and no public correction claim has been made.
