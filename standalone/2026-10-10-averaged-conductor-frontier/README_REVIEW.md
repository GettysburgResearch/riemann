# Independent publication-synthesis review

**Verdict: PASS.** The reviewed README accurately summarizes the frozen proof notes and their conditional boundaries. No mathematical or scope must-fix was found.

Reviewer: repository-comparison research agent, independent of the README's author. The reviewer authored SMALL_GCD_CONDUCTOR_REDUCTION.md; that proof received the separate independent audit included in this packet. This report is a synthesis review, not an additional claim of independent authorship or verification of every earlier analytic input.

Review date: 2026-10-10.

Reviewed object: standalone/2026-10-10-averaged-conductor-frontier/README.md.

Reviewed bytes: 8,834.

Reviewed SHA-256:

    3805009939d7c96e7c1070233242cc139b6fcc90a008efe50ab044e5c4ff7786

This is an AI-agent mathematical and source-scope review, not human peer review, a Lean verification, or a numerical moment experiment.

## Frozen adjacent notes

The README was compared with the following exact adjacent files, including the underlying theorem statements and review qualifications:

| Note | SHA-256 |
| --- | --- |
| SMALL_GCD_CONDUCTOR_REDUCTION.md | 9a371bd84f63b7fae2a3983c05829f2d69e2bbed918ab3eed119a2e7a11125a2 |
| SMALL_GCD_CONDUCTOR_REVIEW.md | dfd260e3625385d0aeaaaf9db9ccabe904fdb49e7cc5a77ebd6c9e2f31a9abca |
| SCALE_AVERAGED_SOURCE_AUDIT.md | 55cf820fe7e7ae5ada20e09154929db95d87e37ed3bb4d0109567de271531330 |
| COFINAL_AVERAGED_REDUCTION.md | b5c6f9064c9b614ccc15990e1b21b2ee7475e710bff8ee73534cb1cc45bbcbd4 |
| COFINAL_AVERAGED_REVIEW.md | 84614cea45aa8d25c09651afd7015fc6c9a6d2414b23e8a4ad8ae4d44531e431 |
| ALL_ORDER_KERNEL_AUDIT.md | aaa19bf48c9382655d7d18265921851638b0116d5ff1889616d2f45602021e79 |

The four included source snapshots were also compared byte for byte with their immutable local Git objects. All four comparisons passed:

| Snapshot | Source commit | SHA-256 |
| --- | --- | --- |
| sources/pr917/OSCILLATING_OVERLAPS.md | 6b4723042b3d250024eef45cb1924f88f28e902c | 271f4f71bda533810ee49f6498f4ffbc42c3f0cb37c59151f9f703e715f58397 |
| sources/pr917/SCALE_AVERAGED_CRITERION.md | 6b4723042b3d250024eef45cb1924f88f28e902c | c6c543037312480fae6154f7a059248fe14658ecff6251aaecb80fe0fdbfd9c0 |
| sources/pr916/PROOF.md | dabd6da99fb92eead7c99f941331ed9cbd2ec4ad | c67f2469e2d2dfce91cdf2b70220fa53978091c0756ffac9a676737e00792a3f |
| sources/pr916/MOMENT_FRONTIER.md | dabd6da99fb92eead7c99f941331ed9cbd2ec4ad | f4da10bd33acc50633353d2c038587ca474ea117cc2830f6c281dcd95ec6bc54 |

The earlier source pins in the adjacent notes remain their dependencies; this review does not replace them with a claim that every earlier manuscript has been re-proved.

## 1. Fourth-order cutoff and the signed remainder

The README reproduces the correct tail normalization:
\[
\|T_{\ge C}\|_2^2
\ll(DH)^\epsilon D^4
\left(HC^{-3}+H^{1/3}C^{-2}+H^{2/3}C^{-7/3}\right).
\]
The three sufficient comparisons with \(HD^2\) are
\[
C\ge D^{2/3},\qquad C\ge DH^{-1/3},\qquad
C\ge(D^6/H)^{1/7}.
\]
For \(1<h\le11/10\), their maximum is \(D^{(6-h)/7}\), as stated. Its improvement over \(D^{(4-h)/4}\) is positive because
\[
\frac{4-h}{4}-\frac{6-h}{7}=\frac{4-3h}{28}>0.
\]
The residual length translation \(D/C=D^{(1+h)/7}\), compared with the old \(D^{h/4}\), is exact. It describes the residual lengths admitted within the controlled aggregate gcd tail. It does not provide a separate new estimate for every individually frozen gcd or singleton core.

The remaining tuple conditions match the proof: both one-sided gcds are below the new cutoff, the full Hermitian tuple has a singleton prime, and \(Ng_1\sqrt{Ng_2}>H\). The strictness example compares feasible incidence patterns; the README correctly avoids claiming monotonicity of the absolute value of a signed sum.

The coefficient 2 and the sign in
\[
M_4(D,D^h)\le C_\epsilon D^{h+2+\epsilon}+2\mathcal S_h(D)
\]
are correct. They come from the polynomial norm inequality before the smooth expansion. The lower bound for \(\mathcal S_h\) follows from the nonnegative complete residual square and the controlled accounting error. Both formulas retain the literal signed remainder rather than its absolute value.

## 2. Averaging, normalization, and milestones

The README's arithmetic premise is explicitly one-sided:
\[
\int_X^{2X}\mathcal S_h(D)\frac{dD}{D}
\le C_\epsilon X^{h+2+e+\epsilon}.
\]
This is the appropriate sufficient input. Direct integration of the signed inequality gives the full averaged fourth moment, so neither a pointwise moment estimate nor an integral of the absolute value is required.

The extraction uses the stipulated universal test and the fixed-row replica count \(D^{h/6}\). The fourth root of the resulting scale exponent gives
\[
\beta=\frac12+\frac{5h}{24}+\frac e4.
\]
The note preserves the quantifiers: \(h\) and the character data are fixed before the large-scale limit, every positive loss is allowed, and approaching \(h=1\) means a sequence of separate fixed-\(h\) hypotheses. The conclusion is in a strict half-plane.

The milestone arithmetic is exact. At the limiting \(h=1\), the choices \(e=0,1/2,2/3\) give \(17/24,5/6,7/8\), respectively. Relative to the earlier source-conditional boundary,
\[
4\left(\frac{139999}{160000}\right)-\frac{17}{6}
=\frac{79997}{120000}.
\]
For a fixed \(h>1\), the permitted excess must decrease by \(5(h-1)/6\), exactly as the README states. The strict inequality in the last table row is necessary and present.

The distinction between fourth and higher routes is correct. The new fourth-order reduction uses the classical cubic sieve and elementary conductor accounting; the extraction uses the universal Mellin test and the proved causal average. It does not use the imported native inverse second moment or assume a quasi-Riemann zero-free theorem. Its signed arithmetic premise is still open.

## 3. General orders and dual-character scope

The cofinal section correctly retains the inherited native second moment. For \(b<1\), the row-uniform pointwise bound on smaller scales is an additional premise; \(b=1\) requires only the elementary pointwise estimate beyond the native second moment.

At \(Q_0=D^q\), the controlled incidence contribution has excess \((2b-1)q\). Adding a signed averaged remainder with excess \(e\) gives
\[
\lambda=\max\{e,(2b-1)q\},
\qquad
\beta_k=\frac12+\frac{5h}{12k}+\frac{\lambda}{2k}.
\]
The README records both formulas without suppressing the baseline or changing the row height at shortened column scales.

For cofinal fixed orders, \(h_k,q_k,e_k=o(k)\) and \(1/2<b_k\le1\) force the displayed boundary to tend to \(1/2\). The native range restriction on \(h_k\) is explicit. The example \(q_k=e_k=\sqrt k\) is a permissible conditional choice, not a claimed arithmetic estimate.

The target character and fixed row remain fixed while selecting the sufficiently large but finite order that excludes a hypothetical zero. Order-dependent finite exclusions do not hide a zero in \(\Re s>0\). Constants need not be uniform in the order. The README also correctly requires contragredient coverage before using the functional equation to obtain a critical-line conclusion for a complex character. The all-finite-order-character hypothesis supplies that coverage. The principal Dedekind-zeta member is self-dual and contains the ordinary zeta factor.

No quantitative height-dependent shrinking band follows from this qualitative cofinal selection, and the README explicitly avoids such a claim.

## 4. Collision-kernel scope and the unchanged bottleneck

The pinned PR #916 enlarges its fixed \(S\) to include prime norms at most \((2k)^3\). This hypothesis controls the positive reconstruction kernel at its square-root weight and is correctly retained. Its norm transfer still requires a full rectangle of smaller factor scales at the same physical row range.

The Gauss coefficient's twisted multiplication is different from the completely multiplicative Möbius kernel. The README therefore correctly refuses to treat this kernel as an automatic removal of the moving Gauss-family exclusions in the A2/theta interface.

Combining the available anisotropic bound with that transfer gives precisely
\[
\lambda_k=(k-1)(2b-1),\qquad
\alpha_k=b+\frac{5h/6-(2b-1)}{2k}.
\]
For \(b\) near \(7/8\) and \(h>1\), the correction is positive. It tends to zero but does not give a boundary below \(b\) or a sublinear moment defect.

The opening and closing scope statements agree with all adjacent notes: the packet proves new reductions and conditional implications, not the remaining averaged arithmetic estimate. It does not attain \(17/24\), improve the earlier source-conditional boundary, or prove RH. Completely disjoint long tuples remain unresolved in the relevant fourth and cofinal regimes.

The README's source and validation links are publication-packaging references; this mathematical review does not substitute for the separate final manifest and link checks. No frozen proof note was modified during this review.
