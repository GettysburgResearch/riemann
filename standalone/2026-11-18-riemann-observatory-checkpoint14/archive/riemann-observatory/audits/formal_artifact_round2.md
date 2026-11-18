# Formal artifact inspection, round 2 — live checkpoint

Review date: 17 November 2026. This is a scoped artifact audit. **Static source inspection, source-reported build logs, local compilation, exact rational verification and external proof-kernel replay are distinct evidence categories.** No headline theorem is labeled locally kernel-verified in this checkpoint.

## Pinned artifacts

| Artifact | Exact object inspected | Relationship to paper |
|---|---|---|
| [anthropics/zeta-23-lean](https://github.com/anthropics/zeta-23-lean/tree/3635e74826a4c1fcece7d1cd2b6fa75e43a00510) | Annotated tag `v1.0`: tag object `82ee6340d6fb15d51fc73ba1ba7b8cac672a7bba`; peeled commit `3635e74826a4c1fcece7d1cd2b6fa75e43a00510` | Companion formalization referenced by arXiv2608.13637v2. Do not replace the pinned tag with moving HEAD. |
| [kristianmk/839](https://github.com/kristianmk/839/tree/0e961ea199b425010843bc8044676d4ad29fe031) | Tag `v1`, commit `0e961ea199b425010843bc8044676d4ad29fe031`, commit message identifies arXiv version1 | Ancillary code for arXiv2610.08965v1. Includes exact finite certificate data and source code. |

AF pins Lean `leanprover/lean4:v4.33.0-rc2`, executable commit `d8b18978322de05a8f3dba51ef03cf5461676c17`, and Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`. The exact dependency revisions are in the checked `lake-manifest.json`; file SHA256 hashes are exported in `experiments/results/formal_round2_static.json`. AF source license is Apache2.0. Knausgård uses MIT for reference code/data and Apache2.0 for Lean code; preserve NOTICE if distributing their code.

## What the AF statements actually say

Read `comparator/ChallengeDeps.lean`, `Challenge.lean`, `Challenge/Multiplicity.lean` and their `Solution` counterparts, then inspected the library final wrappers and finite-window proof. The counting definitions are grounded in Mathlib:

- `IsNontrivialZero ρ := riemannZeta ρ=0 ∧ 0<Reρ ∧ Reρ<1`;
- `zeroMult ρ := (analyticOrderAt riemannZeta ρ).toNat`;
- `zerosIn T1 T2` uses **T1<Imρ≤T2**, not absolute ordinates;
- `Ncount` is a finite sum with multiplicity, `Ndist` counts distinct points, `N0simple` counts multiplicity-one points with Reρ=1/2.

The nine primary definitions match the library text after whitespace normalization. Finiteness is not silently assumed: `Statement/Seam.lean` proves local finiteness away from the pole using the analytic identity theorem and ζ(2)≠0, treats the pole through its nonzero residue, then uses compactness of the closed rectangle to prove finite windows. Consequently the use of `Set.ncard` and `finsum`, which have fallback conventions on infinite sets, has an explicit source-level finiteness proof. Its correctness still depends on successful compilation and the interpretation of Mathlib's definitions.

The strong statement is the epsilon form, for example

`∀ ε>0, ∃ T0, ∀ T≥T0, (2/3−ε) Ncount(T,2T) ≤ N0simple(T,2T)`.

The primitive-Dirichlet statements explicitly quantify q>1 and a primitive character, before epsilon/T0; the threshold may depend on the fixed character. These are not uniform conductor estimates. The base comparator config contains weaker Cauchy–Schwarz constants for some statistics; the separate multiplicity config contains the paper's strong 2/3 and5/6 constants. Inspecting only `Unconditional.lean` would miss that distinction.

Independent static scan of329 Lean files,103396 lines, blanking nested comments and strings:

- zero explicit `axiom`, `admit`, `native_decide`, `unsafe`, `implemented_by`, `run_meta`, `initialize`, `addDecl` tokens;
-33 `sorry` tokens, all in deliberate Challenge statement placeholders; no such token in `Zeta23/` or Solution proofs;
- all15 base,12 multiplicity and6 ξ′ Challenge/Solution theorem types match after whitespace normalization.

These are **static facts**, not a substitute for an axiom-dependency query or compilation. In particular, abstract analytic hypothesis structures occur in intermediate theorems; the inspected final wrappers instantiate them through `paperInputs_zeta`, `zetaEF` and the source Riemann–von Mangoldt assembly. The existence of those source proof terms is stronger than a README assertion but is not yet local kernel replay.

## A source-level difference that matters

`PrimeSideA/Ends.lean` retains the weaker endpoint estimate with raw error `O(L·l·log l·(l²+X))`; `FinalMult.lean` proves fixed-λ results with **λ<1**, then approaches1 through epsilon arguments. Thus the formal artifact has a route to the asymptotic proportion that does not require the manuscript's sharper displayed λ=1 remainder. This agrees with the round1 conclusion that an insufficient printed boundary estimate does not refute the limiting theorem. Do not infer that every quantitative prose estimate was formalized from a proof of an asymptotic headline statement.

The bandwidth-one ceiling development is a separate trust boundary. `PairCeiling/CeilingLaw256.lean` explicitly retains `EnclOK`: the true form-factor values must lie in256 supplied interval enclosures. `LawN256.lean` says the underlying exact-rational law witness is available from the authors and supplies a SHA256; that witness is not present in the inspected checkout. Hypothesis-free axiom lists do not prove an explicit hypothesis supplied to a theorem. An independent integer replay here validates512 row/edge inequalities **conditional on the enclosures**; it does not prove `EnclOK`, the existence of the advertised law, or a ceiling for every vaguely similar RH approach. Reading the paper §7.2 pp13–14 confirms it explicitly discloses this boundary and retains a derivative-variation error term; its below0.6819 conclusion applies to the stated windows and derivative budget below8.2, rather than an unrestricted universal bound for every certificate.

## Knausgård artifact: disclosed trust boundary confirmed in code

The first-window main statement uses1645064/1960733 for distinct zeros; its simple-zero corollary uses1329395/1960733 anywhere in the strip. The separate **simple AND critical-line** statement uses1669159/2478195. The third `Line889` target uses50652159/56956375 for the multiplicity-weighted **union of simple zeros anywhere OR critical-line zeros**, not critical-line zeros alone. Multiple critical-line zeros contribute their full multiplicity; multiple off-line zeros contribute0. The independent statement-grounding table and precise locators are in `audits/adversarial_reviews/839_statement_grounding_round2.md`. Definitions in the Mathlib-only Challenge files and the corresponding Solution statements were inspected. All12 theorem types (six numerical results plus six ceiling statements) match textually after whitespace normalization.

Static inspection found exactly three active `native_decide` uses:

- `lean/Distinct839/Local/RunAll.lean:17`: `checkAll kTabArray=true`;
- `lean/Simple673/Local/RunAll.lean:21`: `checkAllPar kTabArray 32 96=true`;
- `lean/Line889/Local/RunAll.lean:18`: `checkAll kTabArray=true`.

No explicit axiom declarations were found, but `native_decide` generates the disclosed computational axioms. The repository's `axioms.txt` is **author-produced recorded output**, not output locally regenerated here. The source itself clearly distinguishes checker soundness, table soundness and successful compiled search evaluation. Twelve `sorry` tokens occur in Challenge files; no other active `sorry` was found in the checked Lean tree.

The required upstream dependency differs from AF's standalone tag: `anthropics/formal-math` commit `fbdc36bbf17d20af3fd0447c6d1a8a02773c9844`, subdirectory `zeta23`, plus a14-file patch relaxing moment lower bounds. The exact upstream subtree was retrieved through its pinned Git tree:347 files,5,495,689 bytes, each verified against its Git blob SHA1. The supplied patch dry-ran and applied without rejects or fuzz to a separate cache copy, changing exactly14 files. ChallengeDeps, Challenge, Solution and the mathematical zero-count Statement layer remain byte-identical. The standalone AF tag shares314 files, differs in11 (seven linear-algebra differences are comments/attribution only), and lacks22 upstream packaging files; substituting it silently would still be an undocumented build. Results and changed-file hashes are in experiments/results/formal_upstream_patch.json. No Knausgård Lean build is claimed here.

`sha256sum -c CHECKSUMS.sha256` checked354 files and all matched. This proves checkout/manifest self-consistency, not the correctness of those files or independent provenance of the manifest. The first reference checker was compiled without source edits using Debian g++14.2.0, C++23, `-O3 -DNDEBUG -D_GLIBCXX_ASSERTIONS -DVERIFY_POINT_COUNT=7`. Its full run completed in433.816s with PASS_COB_CONTINUUM,60,467,309 nodes,30,233,655 accepted leaves,21,157,274 basic and9,076,381 affine acceptances, maximum stack49: all counts match the author record. Result and hashes: experiments/results/839_reference_rerun.json. It does not itself establish kernel-table soundness; the source header says that condition explicitly.

## Local build and computation status

Pinned Lean installed successfully in a task-specific directory. Mathlib cache downloads failed with CONNECT403 at the official Azure endpoint; repetitive attempts were stopped after substantial consistent failure. Mathlib and all manifest dependencies are cloned. The scoped **source build of `Zeta23.LinAlg.RankTrace` succeeded**,2770 jobs, at the pinned commit. The subsequent local Lean theorem/type and `#print axioms` query exited0. Both `RHLinalg.rank_trace_ineq` and its c=2 specialization depend exactly on `propext`, `Classical.choice`, `Quot.sound`; no custom/computational axiom was reported. Actual output and olean/query-source hashes are in `experiments/results/formal_ranktrace_build.json`; a compact type/axiom record is `formal_ranktrace_summary.json`. This is local Lean checking of the algebra module, not a full zeta theorem or an external independent-kernel replay.

The larger `Solution.Multiplicity` source build then started sequentially, reusing completed dependencies with four Lean threads. The runner waits for the earlier process to end and checks against duplicate builds. Its live status is `experiments/results/formal_multiplicity_build.json`. No successful main target/query is claimed until that result records completion. Raw source/cache logs remain private.

The independent exact integer AF row check passed512 inequalities. A separately written Python Fraction verifier completed all209010 first-window kernel cells with zero mismatches in89.11s; see the detailed analytic reconstruction in audits/adversarial_reviews/kernel_cell_reconstruction_round2.md and its result JSON. This is exact rational validation with classical analytic bounds, not Lean execution. The Knausgård author C++ reference search completed successfully with exactly matching counts; this is execution of the original implementation, distinct from the independent table reconstruction.

Offline reproducibility: the first-window binary and exact inputs, source license and pinned PROVENANCE.json are now bundled under experiments/inputs/839_first_window. Run `python experiments/code/independent_kernel_cells.py` with no arguments; no external download is needed for this check. The code asserts positive even H, positive V, nonnegative R and exact coefficient/denominator identity. Parent independently reviewed the analytic cell argument; see the scoped review.

The unmodified MIT-licensed reference checker and parameter generator are bundled in experiments/code/vendor/839_reference with license and attribution. `bash experiments/code/replay_839_reference.sh` replays the first local inequality offline. Combining this with independently validated table entries still leaves the checker's mathematical soundness and analytic transfer as separate proof obligations; inspected branch coverage and endpoint conventions found no issue, but no full independent search implementation is claimed.

## Minor conductor-normalization discrepancy, separately scoped

The rendered arXiv2608.13637v2 PDF p12 says the μ term gains `−log(q)/(2π)` in the primitive-character extension. The pinned formal source `ThmE/GammaFactsChiProof.lean:47–51` instead gives μ_q(t)=(Reψ(1/4+κ/2+it/2)+log(q/π))/(2π), also used in `EFLitChi.lean:37–42`. The latter sign follows independently from differentiating the archimedean factor q^{s/2}π^{−(s+κ)/2}Γ((s+κ)/2): its logarithmic derivative is log(q/π)/2+ψ((s+κ)/2)/2. The PDF page was visually rendered to exclude an OCR sign mistake.

This appears to be a prose sign typo in the stated substitution. The formal source uses the standard plus sign, and a fixed-q constant change is lower order relative to TlogT; this observation does not challenge the limiting proportion. Record as a source/prose normalization discrepancy pending director adjudication, not an erroneous-main-theorem finding. No numerical or mathematical premise was replaced silently.

## Independent finite-search skeptic review

A separately delegated skeptic started from the source and frozen inputs without reading this agent's derivation. `audits/adversarial_reviews/839_search_skeptic_round2.md` reconstructs continuum coverage, span clipping, closed-cell endpoints, the negative-gain label-share bound, affine shortcuts and integer limits. It found no error witness. Supplementary exact code checked6,400 label comparisons (27 with negative gains) and204 reference API queries against independent Fraction interpolation/range-minimum semantics. Its coarse frozen bounds are2.70954247700185088·10^17 for basic intermediates and6.5990023632844486606848·10^22 for affine values, below signed64/128-bit limits.

This agent separately inspected the acceptance loop, span clipping, affine cell bounds and parameter generator. In particular the parameter generator copies weights/rewards/knots unchanged, maps knot abscissae to3/4+k/8, rounds17/20 downward to13926 grid steps, and uses the same sorted pair order as the seven-point inequality. The local mathematical statement is the source `Distinct839/Defs.lean:162–172`: for all six real gaps≥17/20 and all128 simple/double labelings, the frozen reward sum is bounded by α times the span plus weighted squared kernels plus six piecewise-linear B potentials. The finite computation concerns that statement; extending it to proportions of zeta zeros still requires the local-to-global and analytic layers.

## Second and third windows: exact table and energy checks

A separate generic reconstruction, reusing the parent-reviewed analytic derivative/Taylor argument and shared exact trigonometric enclosures, completed both remaining tables in210.42s. Each has262,144 cells, zero mismatches. The second window has ten inspected cosine coefficients, positivity margin49333/62500 and energy cap6639737/5000000; the third has six, margin382929/500000 and cap6662319/5000000. Both densities have integral1. Their coefficient arrays match the corresponding pinned Lean Defs and frozen JSON, with exact file hashes in the separate offline PROVENANCE files. Results: experiments/results/independent_kernel_cells_second_third.json.

Across all three windows,733,298 whole-cell inequalities are independently reconstructed. This is one family of certificate components, not733,298 research papers or independently novel theorems. The second/third full local searches were not rerun here, nor were their global analytic transfers certified. MIT-licensed second/third frozen inputs are bundled for offline reproduction.

## Finite transfer reconstruction and a conditional boundary improvement

The independent transfer review, audits/adversarial_reviews/839_transfer_skeptic_round2.md, distinguishes the paper's near-pair, nonnegative symmetric energy statement from the repository's all-pairs directed nonnegative statement. It reconstructs the reward loss, pressure, telescoping state and48epsilon*ell error. A valid weakening allows signed directed near-pair energies with exact symmetrized pair defects; extending to all pairs still needs nonnegative symmetrized far energy. An explicit counterexample refutes deleting that requirement without replacement.

A separate proposer and skeptic derive a stronger **finite boundary constant**, conditional on the original first-window seven-point local inequality. Combining unused pressure with the boundary potentials replaces0.432480 by516027/2000000=0.2580135. This is an O(1) change and yields no asymptotic zero-proportion improvement. The generic extension must retain y>=6alpha*theta; an exact singleton counterexample shows positivity of the proposed constant alone is insufficient. Proof and independent checks are in proposals/independent_campaigns/finite_transfer_boundary_round2.md, audits/adversarial_reviews/839_transfer_advocate_round2.md and the skeptic note. Director adjudication accepted this scoped conditional statement; see audits/adversarial_reviews/director_round3_adjudication.md.

A **local Lean check actually completed** for the finite integer certificate: experiments/code/839_transfer_boundary_core.lean imports Std only, uses decide without native_decide, sorry or custom axioms, and exited0 in2.276s. It verifies390 integer knot inequalities,54 zero-knot equalities, six small-chain inequalities and constant arithmetic. Its embedded knots were independently compared with the pinned frozen JSON. Output and hashes: experiments/results/839_transfer_boundary_core.json. This is not a Lean proof of piecewise-linear domination, general chain bookkeeping or the analytic zeta transfer.

A failed attempt to materially improve the uniform kernel-error coefficient found the128-label maximum total local weight is47.999993, nearly48; the naive bound is essentially saturated by all-double labels. The exact finite exploration is preserved in experiments/results/839_transfer_error_budget.json, with no asymptotic gain claimed.

## An external trace critique and independent localization repair

A new inspected primary source, Arias de Reyna arXiv2610.24612v1, Proposition16/footnote1 pp15–16, bounds the trace error byO(U sqrt(T)logT), insufficient atU=sqrt(T), and uses a smaller buffer. PAPER-A007 is a partial-reading record, not a whole-work audit. The defective geometric step in AF Proposition4.2 does not establish theorem failure: a separately tasked skeptic and this reviewer independently repair the estimate by splitting interior, endpoint and exterior zeros. The repaired bound is

trG_U=N(I)+O(sqrt(X)),

trG_U=N(I')+O(sqrt(X)+(U+1)L),

uniformly0<=U<=T/2, under the explicitly documented window decay, boundedness and zero-count hypotheses. This is enough at the originalU=sqrt(T). The independent review is audits/adversarial_reviews/AF_trace_localization_skeptic_round2.md, compared with audits/adversarial_reviews/analytic_trace_buffer_round2.md.

The pinned Lean source has a separate prime-side trace route, PrimeSideA.prop_trace_mu/prop_trace and PrimeSideB/Traces, using smooth density integrals and Riemann–von Mangoldt. Its source proof does not literally formalize the problematic complex zero-side paragraph. This distinction is static source evidence; no full headline build is claimed.

A further hypothesis weakening is under review: no buffer at all appears necessary for the limiting constants if one accepts the weakerO(N/sqrt(logT)) convergence rate. The reconstructed tail bound is then||E_0||_1=O(sqrt(T))=o(sqrt(N)), enough for the squared Hilbert–Schmidt transfer although not for small-operator-norm/Weyl arguments. The conditional proof and exact dependency question are recorded in proposals/independent_campaigns/zero_buffer_localization_round2.md. The independent dependency review is now complete in `audits/adversarial_reviews/AF_zero_buffer_skeptic_round2.md`; the director has accepted this scoped replacement; see audits/adversarial_reviews/director_round3_adjudication.md. A further independently checked conditional extension, `AF_zero_buffer_VK_skeptic_round2.md`, imports the classical Vinogradov–Korobov zero-free strip stated in BGSTB§2 p6. It gives an unbuffered nuclear tail `O_A(sqrt(T)L^(-A))` for every fixed A, retaining the separately established prime-side rate. The original VK proof and full prime-side moment are not certified by this truncation argument.


## Corrected source-build checkpoint after interruption

The first main Multiplicity build was interrupted before completion. The observed lake process was a zombie with SIGKILL exit status9; its runner was absent, and no source-level error appeared in the retained tail. Cause of the kill is not established. That attempt is preserved in experiments/results/formal_multiplicity_attempt1.json. Dependencies were retained and an exact-source continuation was started after confirming no other Lean/lake build remained active.

The original dotted-name import estimate was too small: both comparator/ChallengeDeps and several analytic library files import the bare Mathlib aggregate. The parser now includes standalone names, public/meta import headers and nested-comment/string blanking. Consequently even the narrower library headline targets do not avoid the large aggregate. About8300 Mathlib source files exist and2698 had compiled at the resume checkpoint. This affects build resources, not the already successful RankTrace module or the mathematical source conclusions. The main build remains uncompleted until actual exit/query output says otherwise.

## Explicit scope countermodel for the unbuffered argument

The proposer and independent reviewer constructed a synthetic fixed gamma multiset showing why relative-Hilbert–Schmidt smallness cannot be silently promoted to a vanishing operator tail. It has a critical real inverse-RvM background and sparse off-line quartets, preserves localO(logT) counts, the RvM main count+O(logT), symmetries and eventual VK strip, yet an excluded diagonal entry diverges along a sparse sequence of heights. Its relative Hilbert–Schmidt error still tends to0. Exact Fourier identity, signs, sparse-distance estimates and limits are in audits/adversarial_reviews/AF_no_buffer_operator_countermodel.md. This is an independently reconstructed counterexample to an altered abstract inference, accepted by the director at this explicit scoped level; it is not a claim about actual zeta zeros, the explicit formula or the prime-side moment.

## Later actual finite perturbation check

The archive proof experiments/code/ObservatoryHoffmanWielandt.lean actually compiled locally, exit0 in8.386s. It derives the sorted-eigenvalue squared-distance inequality from the already built von Neumann trace theorem, then the finite Lipschitz empirical-test squared bound by Cauchy–Schwarz. Both queried theorem dependencies are exactlypropext,Classical.choice,Quot.sound. Result/hash/type output is formal_hoffman_wielandt.json; THM-F014 names only this finite core. No full weak-convergence, global clipped-polynomial proof or zeta theorem is labeled formally checked by that run.

Independent ordinary reviews use this core to transfer a bounded Lipschitz clipping of a polynomial minorant, even when the unbuffered operator norm is large. The explicit quartic has clipping constant6. This needs no transfer of higher moments to the zero-side matrix. The signed-moment frontier is now explicitly stated for the full prime matrix, with its arithmetic bound still unproved. See frontiers/moment_combination_missing_lemma.md and zero_buffer_clipped_moment_third_round3.md.

The first K839 majorant/close-pair/Bessel component has also been reconstructed and independently replayed:42 exact whole intervals, the source boundLambda<=16711/10000, Fourier support vanishing at the exact separation endpoint, and pinned-table close-pair coverage. THM-F013 remains a separate component, not certification of the full source theorem.

## Latest interruption/continuation boundary

The main source target suffered a second observed SIGKILL after a transient exec transport outage. No source-level error was logged; cgroupOOM counters were0 and memory peak was below the configured limit. The safe helper preserved attempt2 and resumed the exact source asPID57846, with caches retained and periodic progress output. Current truth is determined by formal_multiplicity_build.json plus process state, not by this historical paragraph. No completed main target was observed when writing it.

The unique complete reading update for A004 is AF_full_reading_round2.md; it is Level1 for the21-page work with all stronger scopes separated. New PAPER-A008 supplies only an inspected external Mertens theorem statement, not a new audited formal dependency. Its withdrawal/version history and mathematical use are explicit in its record.

## Completed local Solution.Multiplicity build and theorem queries

On 17 November 2026 at 20:58:24 UTC, the pinned AF by-multiplicity source target completed with Lake exit 0 and 8,887 jobs at commit 3635e74826a4c1fcece7d1cd2b6fa75e43a00510 under Lean 4.33.0-rc2. The fourth attempt reused intermediate compiler output created by the earlier local source runs. The tracked checkout remained clean. The command lake env lean then ran the dedicated queries and exited 0. Each of the 12 expected declarations reported exactly propext, Classical.choice, and Quot.sound. The query produced no standard error.

The eight zeta declarations give dyadic and cumulative asymptotic bounds for simple zeros on the critical line and distinct zeros, at the rational fractions 2/3 and 5/6 and their Montgomery–Taylor variants. The four dyadic Dirichlet declarations take a primitive character of fixed modulus q>1 and give the corresponding bounds. The displayed types use an arbitrary positive ε and an eventual threshold. Their concrete counting definitions were separately inspected in the count-semantics review. The actual Lean output and artifact hashes are in [the completed result](../experiments/results/formal_multiplicity_build.json) and [the compact summary](../experiments/results/formal_multiplicity_summary.json).

This resolves the earlier incomplete local-build status for this target. The local result concerns these 12 formal declarations in the pinned source and uses Lean's kernel and toolchain trust boundary. A comparison against a separately restricted Challenge environment, an external independent-kernel replay, and the Knausgård formal build were outside this run. [Continuation log](../logs/formal62_continuation.md)
