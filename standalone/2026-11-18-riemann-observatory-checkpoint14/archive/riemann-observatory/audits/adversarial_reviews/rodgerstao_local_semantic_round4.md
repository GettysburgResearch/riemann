# Rodgers–Tao: independent local estimate and version review

Canonical record: **PAPER-S004**. Reviewer: `analytic_frontier/semantic_skeptic`. Access and review date: 2026-11-17. This is a selected-source technical review, not a whole-paper reading or a certification or refutation of Theorem 1.

## Primary sources and version provenance

Inspected source: [arXiv:1801.05914v5](https://arxiv.org/pdf/1801.05914v5), the actual 61-page PDF cached as `sources/spectral/rodgerstao.pdf`, SHA256 `376bb2c1ab941cd5b035546835c5481f2d026767b8e830a48cd5565114a1ec91`. The literal expressions below were also checked visually in rendered PDF pages 40 and 46; text extraction alone was not used to decide their signs, domains or prefactors.

The actual [arXiv history](https://arxiv.org/abs/1801.05914) lists v1 2018-01-18 02:47:14 UTC; v2 2018-02-14 23:37:46; v3 2020-03-06 19:49:21; v4 2020-04-22 18:52:25; v5 2021-07-03 20:15:22. The current author comment attributes corrections in Section 8 to previously inadequate treatment of boundary-energy contributions, identified by Ofer Zeitouni. This is an author-acknowledged historical correction, not a new allegation.

Actual v3 and v4 PDFs were additionally downloaded and their selected sections read. Both have 47 pages. The v3 comment identifies its then-final version incorporating referee and other suggestions; the v4 comment says a recent reference was added. Their Section 8 extracted passages agree after whitespace normalization. Private cache: `sources/rodgers_tao_version_semantic_support/`.

* v3 PDF SHA256 `e9506383a7df33694482d8545bf4d39856bb911910790b6bb8e42d1e3f3ebb26`.
* v4 PDF SHA256 `1e4dec2f415050020358bd2fff9d0a5ac08ccd9233fd2d58d8dfb85200b97e3a`.

No claim that v4 implemented the boundary-energy repair is supported: it remains in the old form. The repair is visible in v5.

## 1. Lemma 16 endpoint estimate: local correction suffices

At v5 page 40, after expanding the classical-location denominator, the proof estimates

\[
 S_j=\sum_{k\in I:\,0<|k-j|<j/2}(k-j)^{-3}
\]

by a constant times `max(|j−I_-|,|I_+−j|)^{-2}`. The PDF really prints **max**. On the positive interval \(I=[J,2J]\cap\mathbb Z\), choose \(j=J\). All terms have positive index difference, and for large \(J\), \(S_J\ge1\), whereas the displayed comparison is \(J^{-2}\). No absolute implicit constant makes this true as \(J\to\infty\).

There is a direct repair. Put \(a=j-I_-\), \(b=I_+-j\), for integer endpoints (rounding endpoints only changes these to their actual integer distances). The symmetric cutoff \(|k-j|<j/2\) cancels every pair of opposite differences present on both sides. With \(d=\min(a,b)\),

\[
 |S_j|\le\sum_{r>d}r^{-3}\le \frac{2}{(1+d)^2}.
\]

Consequently \(\sum_{j\in I}|S_j|=O(1)\), uniformly in the interval length. This is exactly the summability needed in equation (64); its logarithmic factors and the already displayed \(O(\log^{O(1)}I_+/j)\) errors remain polylogarithmic after summing. Thus this local printed estimate is false as written, but replacing the maximum by a regularized minimum repairs the positive-interval calculation without changing Lemma 16's target conclusion. The source's reduction of an arbitrary interval to the positive half-line was not reconstructed here for crossing-zero intervals; applications inspected in Sections 7–8 use positive macroscopic intervals or can be handled separately.

This same maximum-distance expression appears in v4, Lemma 7.1, page 31 (v3 likewise). It is separate from the Section 8 correction.

## 2. Lemma 21(ii): explicit classical-location scale test

Definitions: v5 p41 equation (66) sets

\[
 \psi_T(j)=(1+|j|/(T\log T))^{-100}.
\]

The paragraph before Lemma 21 (p45) defines “moderately sized” as
\(O(T\log_+^3T+\widetilde E_T(t))\), with an absolute implicit constant, not soft-O. On p46 the lemma explicitly includes the classical-location replacement \(x_i(t)=\xi_i\). The printed claim (ii) is that

\[
 (\log_+T)\sum_{j\ne k}\frac{\psi_T(j)\psi_T(k)}{|\xi_j-\xi_k|}
 =O(T\log_+^3T).
\]

Here the renormalized energy is zero because its defining convex remainder vanishes at ratio one. This is an allowed specialization expressly stated by the lemma, not a synthetic zero configuration substituted for the dynamics.

Let \(n=\lfloor T\log T\rfloor\). Restrict to \(n\le j\le2n\) and \(k=j+r\), \(1\le r\le n\). For sufficiently large \(T\), the two weights are bounded below by an absolute positive constant (for instance \(4^{-200}\) works). Lemma 8(ii), equation (44), together with (43), gives uniformly in this restricted domain

\[
 |\xi_{j+r}-\xi_j|\asymp r/\log T.
\]

All summands are nonnegative, hence

\[
 \sum_{j\ne k}\frac{\psi_T(j)\psi_T(k)}{|\xi_j-\xi_k|}
 \gg n\log T\sum_{r=1}^{n}r^{-1}
 \gg T\log^3T.
\]

Multiplication by the printed \(\log_+T\) gives \(\Omega(T\log^4T)\). This cannot satisfy the stated \(O(T\log^3T)\) bound. The small fixed lower-bound constant does not change the asymptotic contradiction. The distinction between ordinary \(O\) and \(\widetilde O\) is material and explicit in the paper's notation section.

The claimed derivation uses the true pointwise inequality
\(L/d\le d^{-2}+L^2\), \(L=\log_+T\). Summing its constant term over all pairs costs
\(L^2(\sum_j\psi_T(j))^2\asymp T^2\log^4T\), not \(T\log^3T\). This is not a valid justification of the displayed claim. It also does not rule out another appropriately restricted or signed argument for the subsequent proposition.

The same claim and argument occur in v4 Lemma 7.6(ii), pp36–37 (v3 likewise). They were not changed by the acknowledged v5 Section 8 repair.

## 3. Uses in Proposition 22: what this review does and does not establish

The whole proof of Proposition 22, v5 pp47–52, was read for dependency scope. Absolute continuity and interchange of integration with the weighted nearby sum are justified on pp47–48 using Proposition 15, macroscopic estimates and the rapid weight decay; they do not invoke Lemma 21(ii). The later decomposition is \(X_1+X_2+X_3+X_4\).

* At p50, the paper obtains a signed far principal-value sum \(o(\log T)\) in the bulk and invokes Lemma 21(ii) to conclude that \(X_4\) is negligible on the \(T\log^3T+\widetilde E_T\) scale. This is the significant use: simply weakening the false lemma by one logarithm does not justify that exact implication from the stated little-o bound. A new quantitative or cancellation argument is required.
* At p52, uses in the comparison of \(X_3\) and \(X'_3\) come with explicit polynomial savings such as \(T^{-0.1}\) or \(T^{-0.2}\). A loss of a fixed logarithmic power could be absorbed there, provided an appropriate valid weaker estimate is actually proved. This observation is not a proof of all those replacements.
* Restricting the first-distance sum to the “nearby” range alone does not remove the classical harmonic logarithm: for bulk \(j\), the range \(1\le r<cT^{0.2}\) already contributes a constant multiple of \(\log T\).

Thus the literal auxiliary claim has an explicit mathematical obstruction, and the first stated use needs an independently reconstructed repair. This review does **not** show that Proposition 22 or the main theorem is false, and it does not assert that no such repair exists. In particular signed cancellation could be stronger than absolute-value estimates, and the argument has not been exhausted. Director adjudication and any downstream repair are separate records.

## 4. What actually changed in Section 8

v4 p44 Proposition 8.2 asserts a propagation bound with error \(\widetilde O(1)\), uniformly over admissible intervals. Its proof on p45 estimates the entire interaction with the environment by \(\widetilde O(1)\) merely from (91), (92), (50). In v5 this is replaced by:

1. Proposition 27, pp55–56: choose a good initial interval \(I^0\), with a time-integrated dyadic weighted control of boundary renormalized energies, using Theorem 17 and Fubini–Tonelli.
2. Proposition 28, pp56–58: propagation over time steps \(\le1/(100\log^2T)\), after shrinking by \(\log^3T\), with error \(\widetilde O(1+|I_- - I_-^0|+|I_+-I_+^0|)\).
3. Its near-boundary interaction estimate uses the selected interval's dyadic energy control; the far part and larger interval energy are handled separately. Iterating only \(O(\log^2T)\) times keeps total boundary displacement polylogarithmic.

v5 Proposition 26 preserves the old terminal-energy conclusion. The explicit Zeitouni acknowledgment is footnote 16 on p55. Lemma 12(v) corresponds to old Lemma 4.2(v); Theorem 17 to old Theorem 7.2; Proposition 22 to old Proposition 7.7. No substantive modification of those Section 4/7 statements is apparent in the selected comparison; this review does not claim a full document diff or an audit of every repaired Section 8 estimate.

## Audit disposition

* Endpoint maximum-distance bound: explicit failure; positive-interval replacement derived and summation verified.
* Classical-location specialization of Lemma 21(ii): explicit \(\Omega(T\log^4T)\) lower bound contradicts its literal claimed scale. Reviewable evidence and dependency scope supplied; director classification pending.
* Proposition 22 and main theorem: no counterexample or false-result claim. Repair of the first \(X_4\) use remains a separate technical task.
* Section 8 boundary issue: documented historical author correction, not a newly discovered uncorrected gap.

Reproducible exact finite endpoint and harmonic-model checks, which support but do not replace the analytic argument: `experiments/code/rodgerstao_local_semantic_round4.py` and its matching result JSON. Whole-paper Level 1 and Level 2 coverage are not upgraded by this note.
