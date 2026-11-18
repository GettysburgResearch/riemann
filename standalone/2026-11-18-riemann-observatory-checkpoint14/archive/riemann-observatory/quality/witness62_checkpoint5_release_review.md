# Checkpoint 5 release review

I compared Round 7 with the named director adjudications, generated corpus and claim records, connection references, frozen checkpoint metrics, PDF text and current continuum outputs. The scoped mathematical claims and aggregate counts agree. Two canonical evidence fields need synchronization before the next render.

## Material source-scope fixes

- In `corpus/bibliography.jsonl`, `PAPER-DR2006` is Level 1 with a whole-work reading, but its `read_scope` calls the phase repair “pending director adjudication.” Its source is `papers/prefix_formula62_generalL_records.jsonl:1`. The current director records `OBS-DR2006-PHASE-REPAIR` and `OBS-DR2006-HARDY-REPAIR` adjudicate the local findings and the replacement lower-bound proof. Add a source-scope overlay pointing to the two director reviews and retaining whole-work Level 1. The correction attaches to the printed phase and Hardy propositions and preserves Theorem 2 under its original premise.
- In the same corpus, `PAPER-OP62-CONREYLI` has a complete-work read scope and Level 1 through `quality/witness62_conrey_li_source_scope_updates_round6.jsonl:1`. Its inherited `audit_scope` from `papers/witness62_operator_frontier_records.jsonl:2` still says the examples were not independently interval-certified. Update both current scope fields together or explicitly mark the inherited field historical. The pinned manifestation is the ten-page arXiv preprint. The demonstrated interval certifications do not raise the whole-work audit level above 1.

The current 113 catalogued works, 112 selected, 106 selected full texts, 46 complete readings, 43 scoped groups, 320 claim records and 47 connections match `quality/metrics.json`, `quality/checkpoints/checkpoint5_metrics.json` and the synthesis table. The 113, 320 and 47 generated IDs are distinct within their respective files. A local scoped adjudication is separate from a paper-wide audit. The new de Roton theorem locator in `connections/selberg_phase_director_round7.jsonl:1` resolves to an explicit passage node, as the archive builder allows, and the remaining theorem IDs resolve to their records. The rendered PDF text includes all Round 7 sections. At inspection the third continuum run had an actual `PASS_COB_CONTINUUM` result and the second had a live checkpoint and no final stdout.

## Independent check of universal derivative obstruction

For \(f\in L^2(0,\infty;dx)\), write \(g(v)=e^{v/2}f(e^v)\). This is a unitary change of coordinates into \(L^2(\mathbb R;dv)\). On smooth tests, and hence distributionally by the change of variables and multiplication by the smooth weight \(e^{v/2}\),
\[
 {\cal J}(xf')=(\partial_v-\tfrac12)g .
\]
If \(xf'\) belongs to \(L^2(dx)\), the equation gives \(g'\in L^2(dv)\) because \(g\in L^2(dv)\). Conversely \(g\in H^1\) gives \(xf'\in L^2(dx)\). With the \(e^{itv}\) Fourier convention, the transformed weak derivative is \(-it\,\widehat g(t)\) as a distribution, and thus \(\mathcal M(xf')=-(1/2+it)\mathcal M f\) with line measure \(dt/(2\pi)\). Polynomial multiplication of an \(L^2\) Fourier transform is well-defined as a tempered distribution, even when the result no longer lies in \(L^2\).

The critical-line transform of \(\mathbf1_{(0,1]}\) is \(1/s\). For a measurable unimodular symbol \(u\) and \(f=U\mathbf1_{(0,1]}\), the weak derivative transform is therefore \(-u(s)\). A measurable function of modulus one almost everywhere on the full critical line cannot represent an \(L^2(dt/(2\pi))\) transform. This verifies nonmembership for the maximal weak domain without assuming a classical derivative for any phase representative. It disproves the premise of the source's application of conditional Proposition 4.1. The separate explicit zeta and \(\chi_4\) examples disprove the pointwise \(\Phi\) tail of Proposition 5.1. The two-weighted-line jet proof replaces the application and keeps the lower theorem.

## Other mathematical and execution checks

- The adaptive Selberg assertion keeps a fixed \(F\), its GRH, both signs of ordinates, arbitrary complex ordinary Dirichlet polynomials, and the whole residue term in the Mellin model. In Round 7 line 13, “no effective rate” concerns the convergence of the full optimal limit. The fixed finite-block lower error stated later is a different estimate.
- The phase-filter normalization \(\|D f_\tau\|^2=1/(4\sqrt\tau(1+\tau/4)^{3/2})\) follows from the squared-resolvent integral with measure \(dt/(2\pi)\). The error is \(\int\tau^2|s|^2(1+\tau|s|^2)^{-2}dt/(2\pi)\). Substituting \(z=\sqrt{\tau/(4+\tau)}\) gives \((z+z^3)/2\), the stated derivative frontier and the limit \(1/4\). These agree with the report and connection.
- The Conrey–Li interior ratio uses the actual quotient \(X(2+10^{-6}+282i)/X(1+10^{-6}+282i)\). The printed numerical ratio is reciprocal and has the same sign. Source credit and the scope of the reproduced forms are preserved.
- I reran `scripts/chi4_phase_certificate_skeptic62.py` with python-flint 0.9.0. It produced the reported sign-changing ordinate bracket and positive finite projections. At \(N=1000\), for example, the two-vector projection was \([0.00665531896\ \mathord{+/-}\ 2.90\cdot10^{-12}]\). These are two conjugate zero vectors of order zero, not two derivatives at one zero. The replay is an execution check. The finite numerical candidates remain pending in the Round 7 release.
