# Independent review of the A2–coupled-theta interface

**Verdict: PASS at the explicitly stated arithmetic and classical-sieve scope.** No mathematical or scope correction is required in the reviewed version. This review does not certify a new reflection estimate, a centered covariance bound, a full fourth moment, or a new zero-free region.

Reviewed file: [INTERFACE_COMPARISON.md](INTERFACE_COMPARISON.md).

Reviewed SHA-256:

    203df24a48e54cb088a28c1236c78569ae75ea84a6b589f72a30b35720cc8e4c

Reviewer: the independent repository-comparison research agent, separate from the interface note's author. Date: 2026-10-10. The author completed the arithmetic composition before this review and then added Corollary 3.3; both were read and checked in the final version above.

## Sources and limits of review

The review compared the claimed identities with:

- PR #914, commit 0cc0428fedbbfc340044c7451b3d392c1da9a103, [A2_COMPLETION.md](https://github.com/GettysburgResearch/riemann/blob/0cc0428fedbbfc340044c7451b3d392c1da9a103/standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md), especially Theorem 4.1, the fixed-auxiliary formula (5.8), and the centered-form warning in Section 6.
- PR #915, commit 9959364671f89b86f3992ec5ed5e19f804eb607b, [COUPLED_THETA_COMPLETION.md](https://github.com/GettysburgResearch/riemann/blob/9959364671f89b86f3992ec5ed5e19f804eb607b/standalone/2026-10-10-sextic-critical-core/COUPLED_THETA_COMPLETION.md), for the physical one-axis completion and the narrower scope of its reflected component estimates.
- PR #913, commit 6498d6cc2eded03159c7332b25fd224ad07f89c1, [REFINED_ALL_ROW_SIEVE.md](https://github.com/GettysburgResearch/riemann/blob/6498d6cc2eded03159c7332b25fd224ad07f89c1/standalone/2026-10-10-sextic-moment-descent/REFINED_ALL_ROW_SIEVE.md), Theorem 3.4, for the arbitrary-coefficient squarefree-column sieve with all nonzero element rows.
- OpenAI/math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a, October 5 [paper2.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), labels eq:crt-a, eq:T, eq:completed-twist, and eq:cube-inverse, for the inherited normalizations.

This is a proof review of the new composition and its use of the pinned sieve. It does not independently re-prove every classical large-sieve input or every imported analytic theorem. The new finite inversion is also checked directly below, so it does not require analytic continuation or a reflected identity.

## 1. Cube inversion and all nonunit masks

Expanding the literal physical theta sum with
\(V_*(y)=\sqrt y\,W_2(y)\) changes its norm coefficient to
\[
\frac{\sqrt{Nb}}{\sqrt B}
\]
at cube index \(b\). The squarefree index \(n\) has no residual factor \(1/\sqrt{Nn}\). At a rescaled argument \(B/(Nh)^3\), the outside inverse coefficient \(1/Nh\) therefore combines with the rescaling to give \(\sqrt{Nh}\). Grouping \(d=hb\) leaves the common coefficient \(\sqrt{Nd}\) and the divisor sum \(\sum_{h\mid d}\mu_K(h)\). Only \(d=1\) survives.

The inverse coefficient in Lemma 2.1 is exactly
\[
\frac{\mu_K(h)\lambda(h)^3\chi_h(k)^3}{Nh}
\mathbf1_{(h,afqS)=1}.
\]
In particular \(\chi_h(af)^{12}\) is a coprimality indicator. Splitting this indicator into \((h,qfS)=1\) and the outer multiplier \(v_h(a)=\mathbf1_{(a,h)=1}\) is valid even when \(q\) and \(f\) overlap. Zeros at primes shared with the row \(k\) remain in \(\chi_h(k)^3\).

The inversion is finite on the compact physical support. The cube variable may overlap the inner squarefree variable; no erroneous condition \((n,b)=1\) has been added. The physical exclusion of \(S\) is not used to remove reflected cusp indices meeting \(S\).

## 2. Five-label composition and its norm cost

The child maps and exterior coefficient agree with the pinned A2 formula. In particular \(q_t=q_0cde\) and \(f_t=ef\) overlap at \(e\), while the surviving outer factor is coprime to both. That overlap is retained in the mixed family rather than replaced by a disjointness assumption.

The exact fixed-auxiliary normalization is
\[
\sqrt{N(cde)}
\sqrt{\frac{A_tB_t}{AB}}
=\frac1{Nc\,Nd\,(Ne)^{3/2}}.
\]
Together with cube inversion, this gives precisely the denominator
\(Nc\,Nd\,(Ne)^{3/2}Nh\) in (3.4). All exterior row multipliers have modulus at most one. Thus Minkowski applies in any fixed nonnegative weighted row Hilbert space.

There are three harmonic sums, for \(c,d,h\), and one convergent sum, for \(e\). Nonempty physical children bound each label by a fixed support-dependent multiple of \(Z\). Consequently the reciprocal coefficient sum costs \(O((\log(2Z))^3)\) in norm and \(O((\log(2Z))^6)\) in squared norm. This is correctly identified as a fixed-auxiliary positive-norm transfer. It is not an auxiliary-annulus or covariance-subtracted estimate.

## 3. The uniform classical envelope in Corollary 3.3

Put \(B_b=B/(Nb)^3\). The coefficient in the direct cube expansion (3.10) is exactly \(1/Nb\), since
\[
\frac{\sqrt{Nb}}{\sqrt{AB}}
=\frac1{Nb}\frac1{\sqrt{AB_b}}.
\]
The restrictions \((b,qfS)=1\) and \((a,b)=1\) are necessary and correctly retained. The latter is a row-independent outer coefficient mask. The factor \(\chi_b(k)^3\) is a row contraction; it is not incorporated into a coefficient that falsely depends only on the column.

For each fixed \(b\), group the squarefree product \(an=m\). Its coefficient is independent of \(k\), supported on \(Nm\asymp AB_b\), divisor-bounded, and has squared mass \(O(D^\epsilon AB_b)\). The moving masks only delete summands or insert factors of modulus at most one. PR #913's refined all-row sieve therefore applies and, after division by \(AB_b\), gives (3.11). Nonempty bounded scales below one have a fixed positive lower bound determined by the supports, so their treatment does not introduce a moving constant.

After taking square roots, the three cube sums have weights
\[
(Nb)^{-1},\qquad (Nb)^{-5/2},\qquad (Nb)^{-2}.
\]
The first is logarithmic on finite physical support; the others converge absolutely. Minkowski, squaring, and redistribution of arbitrary epsilon losses give
\[
\sum_{0<Nk\le H}|\mathcal C_{q,v}(A,B;k,f)|^2
\ll D^\epsilon\bigl[H+H^{1/6}AB+(HAB)^{2/3}\bigr].
\]
The dependence on the polynomial scale limits, fixed tests, and the stipulated subpower bounds for \(v\) is allowed. No dependence on a moving exclusion or auxiliary ideal is silently placed in the constant.

## 4. Support mismatch and the remaining analytic gap

The local support comparison is correct: the one-axis completion has formal local series
\[
\frac{1+a_py}{1-b_py^3}+a_px,
\]
whereas the A2 completion has
\[
1+a_p(x+y)+b_p(xy^2+x^2y)+b_pa_px^2y^2.
\]
These are local coefficient descriptions, not an assertion that the global twisted Gauss coefficients form an ordinary Euler product. An outer multiplier cannot create the absent correction support. The finite composition resolves that arithmetic mismatch by displaying a larger mixed family.

The note accurately preserves the remaining distinctions: growing inner exclusions are not covered merely by an outer multiplier corollary; additional auxiliaries can change reflected local exponents; squarefree-row component bounds are not full all-row estimates; smaller child rectangles need not preserve a positive conductor gap; and positive Hilbert norm transfer does not control the original signed, centered form. In particular no conclusion at exponent \(17/24\), no full higher-moment estimate, and no new zero-free half-plane follows from this interface alone.

No numerical experiment or finite prime check is used as evidence for these infinite statements. The review consists of the exact algebra, normalization, support, uniformity, and cited-theorem applicability checks recorded above.
