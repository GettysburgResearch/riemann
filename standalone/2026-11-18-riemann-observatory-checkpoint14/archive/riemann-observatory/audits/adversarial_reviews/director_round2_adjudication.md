# Round-two director adjudication

2026-11-17. These are claim-level audits. No complete source paper is promoted to whole-paper Level3. Established results independently reconstructed are explicitly distinguished from new-to-this-session derivations and unassessed novelty.

## Fixed-size multi-cluster approximation and correction

Sources/motivation: Burnol, BCF, Avdonin–Ivanov, de Boor, with exact inspected passages in the new paper records. Proposer: multicluster_uniform.md. Independent skeptic: multicluster_skeptic_round2.md. Director independently checked Hermite–Genocchi normalization h_j=x^j E exp(ixU), the triangular jet basis, the rescaled Hilbert-matrix lower bound delta=s^(2m−1)/(4 trace(H_m^-1)), endpoint quadrature, alias exclusion at the large-L threshold, and the trivial small-L bound. Uniformity holds through all collisions for fixedm and bounded scaled diameter; common frequency translation cancels from Gram matrices.

The second correction also checks: normalized quadrature is G_L=G+(B_end−G)/(L+1)+R, ||R||≤M2/(12L²); the inverse identity and L/(L+1) normalization give LE=kappa−beta/(L+1)+O(L^-2). At complete coalescence beta=(m^4+m²)/2 agrees with the exact all-m product expansion. This is a finite model, not an infinite arithmetic estimate. The stabilization mechanism has established prior sources; publication novelty is not claimed.

The later continuous/discrete block bounds and grouped-residue identity have additional independent review in block_and_residue_skeptic_round2.md. The director checked that the discrete alias denominator, not ordinary center distance alone, controls the finite geometric sum. Local cluster comparisons must use the SAME residual degreeL. The Hermite contour/DD identity removes artificial internal-separation denominators but leaves the zero-removed factor and infinite contour tails uncontrolled. Preserve those limitations.

## Bounded finite auxiliary levels

Proposer: auxiliary_spectral_complexity.md. Independent reviewers: auxiliary_skeptic_round2.md and auxiliary_third_round2.md. Director independently checked the finite negative-subspace proof of count shift0≤xi≤M and norm convergence of spectral-cutoff couplings P_n B→B. This is a norm-resolvent argument, not an arbitrary Galerkin limit. Rewriting the statistic as N((2K,4K])−2N((K,2K]) eliminates the zero endpoint entirely. All three counts share the same shift reference, yielding3M, not6M. Exact examples attain both signs. The graph consequence costs E+M and is restricted to bounded block coupling.

## Finite-deficiency self-adjoint boundary changes

The independent real-resolvent derivation is in extension_interlacing_round2.md and extension_resolvent_third_round2.md. Director independently checked both branches: for x>a, reciprocal eigenvalues count a positive compact-resolvent tail; for x<a, the oriented prefix is minus a negative tail. If the real resolvent difference has inertia(p,m), both oriented shifts lie in[−m,p], whose length is rankr. A simpler common anchor a<K uses only the positive branch for the three target cuts. Compact resolvents ensure such a common real anchor exists even for two-sided spectra.

For a common symmetric restriction with deficiency(d,d), the nonreal resolvent difference has range in ker(S*−i), hence rank≤d; resolvent identities transfer this to a real common anchor. Therefore the three-height count curvature changes by at most3d. Momentum boundary-phase examples attain3d. This is a proved elementary consequence of standard finite-rank interlacing/resolvent machinery; the semibounded Theorem1.1 of the inspected source is NOT cited as a theorem covering the two-sided case.

## Fixed Selberg coefficients, weighting and necessary simplicity

The q=1 implication was independently rediscovered, then located as PRIOR ART: Wei–Wu Proposition1.9. It is not claimed new. Parent, source researcher and independent reviewer reconstructed the exact Mellin/unitary identity, small-u coefficient bound and Abelian pole argument. Merely assuming RH does not supply the fixed-array norm convergence from the inspected sources; the reverse is explicitly a problem in the earlier primary literature. This is a missing justification in a source interpretation, not proof that the equivalence itself is false.

The all-fixed-integer-q extension is checked by two independent reconstructions and the director: I f(u)=integral_0^u f(v)dv/v is bounded with norm2 on L²(du/u²), and Mellin multiplier1/s. The unitary reflected multiplier chi(s)((1−s)/s)^q maps the critical residual exactly to I^(q−1)(W_N−g). On the small interval, I preserves C_N u and g remains−2u+O(u³/3^(q−1)). Thus weighting more strongly does not remove the fixed-profile multiplicity obstruction. Full-sequence convergence is essential to the global Abelian argument; a subsequence cannot be silently substituted.

The separate unrestricted-coefficient weighted criterion has a clean exact Hardy-space proof in weighted_criterion_round2.md. The inner factor(s−1)/s cancels the zeta pole, has modulus1 on the boundary, and gives a nonzero evaluation witness at every off-line zero. Consequently prescribed subsequential convergence implies RH, but simplicity requires additional full-sequence control. No distinction between optimized infima and a prescribed array is suppressed.

## Geometric hypotheses and countermodels

Proposer report: frontiers/geometry_round2.md. Independent source/lemma review: geometric_coinvariant_skeptic_round2.md. Director independently checked the symbolic5-shift code for A=[[2,1],[1,3]]: each label determines its arrival vertex, so primitive graph cycles inject into primitive5-symbol necklaces. Thus the formal rational genus-one function has nonnegative integral Euler exponents yet off-circle reciprocal roots. It is NOT a curve zeta function.

The actual constant-arithmetic lisse-sheaf example must send GEOMETRIC Frobenius toA (arithmetic toA^-1), so detA=5 corresponds to Q_l(-1). Its geometric monodromy is trivial; all tensor coinvariants survive and produce uncontrolled extra global poles. This explains exactly why pairing/rationality/positive even traces are insufficient.

The weakened sufficient hypothesis—sublinear excess weights on an unbounded sequence of even-tensor coinvariants—is valid under the explicit affine-curve, rationality, algebraicity and self-duality assumptions. Hc0=0; Hc2 is coinvariants(-1); assumed pole radii and nonnegative local/global coefficients bound each local tensor eigenvalue. Degree factors cancel correctly and duality gives the lower bound. Rational formal-series descent from Q_l(t) to Q(t) and cancellation only removing poles were checked. This is a source-method specialization/hypothesis reformulation, not a classical RH theorem or established novel result.

## Exact kernel-table component

Parent reviewed independent_kernel_cells.py mathematically and independently of the author program; a third reviewer saved kernel_cell_third_round2.md. The six-cosine density is positive and has integral1. Its Fourier derivative bounds are |K'|≤pi and |K''|≤pi². The rational closed expression, midpoint signs modulo periods, outward Machin-pi enclosure, Taylor remainder directions, derivative Lipschitz bound and squared lower-bound rounding are sound. Ignoring a common period sign is safe because the final bounds are absolute; the cosine reflection within one period remains essential.

The all209010-cell run had zero mismatches. This validates the first-window table component with exact rational arithmetic and ordinary analytic lemmas. The separate60-million-node author-code replay passed, and an independent finite-search reviewer inspected coverage, pruning and frozen-data integer bounds. Neither success alone validates the full analytic transfer to zeta or constitutes local Lean-kernel checking. Later windows retain separate statuses.

## Global Lagarias concavity update

The eventual threshold was first improved analytically to2048, then the compact interval[1,2048] was covered by170 rational cells. The director checked the exact numerator identity B B_second−Bprime²=−exp(2h)(logh+1)/h²+exp(h)((h−2)logh+2−3/h)−1. Negative numerator and positiveB,Bprime permit the conservative derivative bounds to give a strict interval upper bound. H(x) is enclosed by a finite harmonic-continuation sum and decreasing-tail integral bounds, with endpoint monotonicity. Every cell covers its entire closed interval.

The initial Arb implementation and the separate standard-library192-bit integer interval implementation both passed independent replay. The latter proves exp/log enclosures using positive Taylor/atanh remainders and outward rounding; it does not require a special-function black box or Arb. The claim is therefore an exact computational interval proof with ordinary analytic lemmas, not a floating observation or Lean certificate. The supporting-parameter endpoint consequence extends to every shared-maximizer pair withu>=1; an arbitrary pair of abundant integers still lacks the required support certificate. No infinite-tail or RH conclusion follows.
