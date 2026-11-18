# Scoped audit: weighted-Dirichlet operator endpoint and a Mellin display

Date:2026-11-17. First reader:equivalences. **Independent review required before classification as a verified source error.** The actual arXiv primary version was read in full; this is not a full technical audit of all external inputs. The two localized claims below have explicit witnesses. Neither is a claim that the authors' main RH-related result is false.

## Primary identity and source fidelity

PAPER-E012: Eva A.Gallardo-Gutiérrez and Daniel Seco, *Zero-Free Regions of the Riemann Zeta Function and Approximation in Weighted Dirichlet Spaces*, Complex Analysis and Operator Theory19,Article38(2025),27pages, DOI10.1007/s11785-025-01661-2, published29January2025. Actual journal PDF https://link.springer.com/content/pdf/10.1007/s11785-025-01661-2.pdf was downloaded and its relevant statements visually inspected. Private copy `sources/logarithmic_riesz_round3/gallardo_seco2025.pdf`,SHA256 `05615ae82b3d52e7591474859f774ae2244357c7986c592590129386beea26d4`.

The complete22-page arXiv2206.02654v6 (listing5June2024, manuscript date6June2024) was read, including the proofs in§§2–5 and references. Private copy `gallardo_seco2206v6.pdf`,SHA256 `0cee802b54eb53f3b9a74c02bf2b636b414c5ed3efb0ddfb4c759d9d84959939`. The journal was read only in targeted portions, not all27pages. Both versions' Proposition5.1 and Lemma2.3 agree in the points inspected. Mathematical locators below specify both paginations where checked. No published correction was located by the targeted searches listed below; this is not a claim that no correction exists.

The declared coefficient norm is

||sum_(n>=0)a_nz^n||²_(D_beta)=sum_(n>=0)|a_n|²(n+1)^beta.

It is stated in preprintp2 and publisher text; beta=−1 is the usual Bergman coefficient norm. The source's §3 absolute-value bars are partly lost in extracted text: actual publisher formula has omega(m|sum mu(k)/k|). No missing-absolute-value finding is made. This illustrates why the displayed primary formula, rather than OCR alone, controls this audit.

## A. Proposition5.1 boundary: explicit polynomial approximate kernel

The journal Proposition5.1, page21of27, visually checked, says for alpha in[−3,−2),a>0, the map

T_a:D_(alpha+2)->D_alpha,

T_af=(((1−z)^a f)')/(1−z)^a=f'−af/(1−z),

is bounded and bijective if and only if a>=−(1+alpha)/2. The preprint states the same atp17; its proof occupiespp17–20. In particular it includes **alpha=−3,a=1**, with domainD_−1 and rangeD_−3. This is an actual boundary of the printed parameter range, not a limit taken outside it.

For K>=0 let

f_K(z)=1+z+...+z^K,

J=K+1.

Then exactly

||f_K||²_(D_−1)=sum_(j=1..J)1/j=H_J ->infinity.

For coefficients n<K, f_K' and f_K/(1−z) both have coefficientn+1 and cancel. For every n>=K, the derivative coefficient is0 while the cumulative coefficient isJ. Hence

T_1 f_K=−J z^K/(1−z),

||T_1 f_K||²_(D_−3)=J² sum_(j=J..infinity)j^(−3)
 <=1/2+1/J <=3/2.                                          (GS1)

The upper bound follows by separating j=J and integrating the decreasing tail: sum_(j=J+1..infinity)j^−3<=integral_J^infinity x^−3 dx=1/(2J²). The same integral gives a lower bound1/2 on the squared image norm. No unvalidated numerical approximation of zeta(3) is used.

Thus u_K=f_K/sqrt(H_J) has domain norm1 but image norm at mostsqrt[(1/2+1/J)/H_J]->0. A bounded bijection between these Hilbert spaces would have a bounded inverse, hence a positive lower bound on||T_1u|| for||u||=1, contradicting this sequence. Therefore the **printed bounded-bijection assertion at this endpoint cannot hold under the stated coefficient norms**, subject to independent source/normalization review.

This does not require assuming the operator is bounded in order to calculate the witness; boundedness is part of the conjunction being tested. Independently, derivative boundedness and the standard weighted-Bergman/Hardy estimate do give boundedness here, so the issue is bounded invertibility, not an attempt to exploit an undefined image. Each f_K is a polynomial and every displayed image is inD_−3.

### Alternative interpretations considered

* Equivalent Bergman normalizations multiply norms by bounded fixed factors and cannot remove the divergent ratio.
* There is no nonzero kernel at this endpoint: the homogeneous solution(1−z)^−1 has D_−1 norm squared sum1/j=infinity. Passing to a quotient by the kernel therefore does not fix the example.
* The printed domain is allD_(alpha+2), not a smaller graph-norm domain or an imposed boundary-value subspace. The proof explicitly tests homogeneous solutions in that domain.
* Replacing the non-strict parameter inequality by a strict one is a plausible repair, but this audit has not proved bounded bijectivity for the full repaired range. It must not silently replace the source theorem.
* The proof's surjectivity/Riesz-basis argument must be revisited at the boundary; merely observing that the kernel disappears does not establish surjectivity. A complete forensic identification of the failed estimate is pending.

The boundary issue does not refute Theorem2.1, whose Mellin/Hölder zero-exclusion argument does not require this operator. It also does not alone refute every case of Theorem5.5. Determining exactly which implication/range of the later reformulation needs repair is a separate task.

### Explicit target outside the range, independently proposed by root

Root reconstructed the polynomial witness independently and supplied a stronger coefficient target. I checked the recurrence algebra before this addition. The exact norm definition was then visually confirmed in the actual journalPDFp3 (`gallardo_seco_journal_p3.png`). Independent skeptical source review is still requested; this is not yet an adjudicated public error classification.

Let g(z)=sum_(j>=0)b_jz^j with b_j=(j+1)/log(j+2). It is analytic in the disk and

||g||²_(D_−3)=sum_(j>=0)1/[(j+1)log²(j+2)]<infinity.

Suppose an analytic f(z)=sum a_nz^n solved T_1f=g. Write S_j=sum_(k0..j)a_k and t_j=S_j/(j+1). The coefficient equation is

b_j=(j+1)a_(j+1)−S_j.

It implies exactly

t_(j+1)−t_j=b_j/[(j+1)(j+2)]=1/[(j+2)log(j+2)],

t_n=t_0+sum_(k2..n+1)1/(klogk),

a_n=t_n+b_(n−1)/(n+1)=t_n+n/[(n+1)log(n+1)], n>=1.

The real sum in t_n diverges like loglogn. No choice of the possibly complex constantt0 can cancel that divergence. Thus eventually|a_n|>=1, and even a_n=loglogn+O(1); hence sum|a_n|²/(n+1)=infinity. There is no preimage inD_−1. This is a direct nonsurjectivity witness, stronger than the failure of a bounded-inverse inequality.

This proof requires no numerical computation, inverse-mapping theorem or unproved boundary regularity assumption. Both target membership and the failure of every candidate domain preimage are controlled by explicit convergent/divergent positive series.

## B. Lemma2.3: omitted first coefficient in the displayed Mellin sum

Preprintp5 and actual journalp6 Lemma2.3 state, with f(x)=sum_(k=1..N)c_k{1/(kx)} and sum c_k/k=0,

integral_0^1 f(x)x^(s−1)dx=−zeta(s)/s *sum_(k=2..N)c_k k^(−s). (printed)

The correct constrained fractional-part calculation has the sum starting at k=1:

integral_0^1 f(x)x^(s−1)dx=−zeta(s)/s *sum_(k=1..N)c_k k^(−s),  Re(s)>0,

with the apparent pole at1 removed. Indeed the individual Mellin formula is

integral_0^1 {1/(kx)}x^(s−1)dx=1/[k(s−1)]−k^(−s)zeta(s)/s;

the constraint cancels only the first term, not the c1 term in the second sum. Equivalently retain k>=2 but replace k^(−s) by k^(−s)−k^(−1).

Explicit test: N=2,c1=−1,c2=2 satisfies the constraint. Then f(x)=2{1/(2x)}−{1/x} is the parity of floor(1/x), so it is nonnegative and equals1 on(1/2,1]. At s=2 the integral is positive; the correct value is zeta(2)/4=pi²/24. The printed expression gives−zeta(2)/4. This cannot be repaired by a branch convention or a limiting value at the pole.

The zero-exclusion argument immediately after the display survives the local repair: at any zero ofzeta the full finite Dirichlet sum is still multiplied byzeta. When moving between the constrained coefficients c_k and coefficients d_k of the basis g_k=k{1/(kx)}−{1/x}, set c_k=kd_k for k>=2 and c1=−sum d_k; this avoids reusing the same letter for distinct coefficients in the step-sequence representation. This is a localized formula/notation correction, not a mathematical counterexample to the zero-free theorem.

## Search and verification limits

Targeted searches on2026-11-17: exact DOI+correction; title+erratum; author names+Dirichlet+correction; arXiv2206.02654+v7. They returned the actual publisher source and related records; no relevant published correction was located. The arXiv and journal versions are distinct manifestations of one work, not two paper-count entries. External functional-analysis dependencies, the Selberg sign-change theorem and all estimates in§5 have not received a complete Level2 audit. Independent reviewers must inspect the source and reconstruct(GS1) before any public author-error classification.

### Current primary version/correction check

On2026-11-17 the actual arXiv landing page https://arxiv.org/abs/2206.02654 was fetched and its submission history inspected. It lists exactly six versions: v1 6June2022 14:49:16UTC; v2 11July2022 19:23:47UTC; v3 21February2023 18:50:47UTC; v4 26July2023 07:04:11UTC; v5 21September2023 09:42:39UTC; v6 5June2024 15:08:31UTC. Thusv6 is the most recent arXiv version **listed at the check**, not an inferred absence of all later private revisions. The actual landing HTML is preserved privately as `gallardo_seco_arxiv_abs_20261117.html`.

The publisher page and current Crossref DOI metadata were also fetched. Crossref's relation object is empty in the saved response. More strongly, the actual Crossmark content linked from the publisher was fetched at https://crossmark.crossref.org/dialog-content?doi=10.1007%2Fs11785-025-01661-2&domain=pdf&date_stamp=2025-01-29 . It explicitly reports **“Document is current”** and **“Any future updates will be listed below”**, with no correction/update entry displayed, and identifies first online29January2025. Snapshot `gallardo_seco_crossmark_content_20261117.html` has SHA256 `985394600b17381b692a9401e6724909d867dbda9fd392a6ab59126c8c1eed14`; the adjacent `.txt` is a plain-text extraction. The fetch log and other metadata snapshots are in the same private source directory.

The precise conclusion is that **no correction is listed by these checked primary records or located by the targeted searches as of this check**. This does not assert that nobody had previously noticed the endpoint, that no unindexed correction exists, or that the finding is novel. The counterexample is tied to the exact accessed v6 and journal version-of-record hashes.

Concrete next questions: determine the correct full bounded-invertibility range ofT_a; exhibit a target outside its range at the boundary or prove its range nonclosed; isolate the Riesz-basis estimate that fails; and reconstruct Theorem5.5 without importing the faulty endpoint assertion. Preserve the valid Mellin/Hölder results separately.

## Subsequent durable checks, kept separate in scope

The complete weighted-Hardy repair is now independently written in `audits/adversarial_reviews/gallardo_seco_hardy_repair_skeptic_round4.md` and `gallardo_seco_hardy_repair_equivalences_round3.md`. Its classification for fixedalpha<−1,a>0 is bounded bijection fordelta=a+(alpha+1)/2>0; surjection with one-dimensional kernel fordelta<0; injective dense proper nonclosed range fordelta0. THM-E-GS303 indexes this reconstruction. This repairs the operator statement; it is not a proof of every downstream closure equivalence.

The independent source/impact review `gallardo_seco_operator_impact_advocate_round4.md` confirms the exact critical pair in Theorem5.5's printed range and explains a possible weighted-target topology for the multiplier. The source's invertible-multiplier extension assumes a positive lower bound, whereas(1−z)^(a−1) vanishes at the boundary fora>1. That observation identifies an additional hypothesis-checking task, not a counterexample to Theorem5.5.

A separate forensic calculation ofEq26 is in `audits/gallardo_seco_inner_product_round3.md`. It has its own pending review scope and must not automatically inherit the endpoint finding's classification.
