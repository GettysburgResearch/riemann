# Lagarias2007: priority context and an alternate contour estimate

2026-11-17. Scope: actual published PDF, introductionpp1689–1695, definitions/Theorem2.1pp1696–1699, and complete Section6pp1721–1726 read. Page1694 was additionally rendered to verify the exact theorem, finite-height statement, and credit to Bombieri–Lagarias. The rest of the52-page article was not read. Overall source audit remains Level0/partial, with a scoped reconstruction of the contour estimate below. No assertion that the main theorem is false; no novelty claim. An independent review of this alternate-contour note is still required before elevating a finding.

Canonical source: `PAPER-L001`, JeffreyC. Lagarias, *Li coefficients for automorphic L-functions*, Ann. Inst. Fourier57(5)(2007),1689–1740, DOI10.5802/aif.2311. The newly downloaded publisher PDF has exactly the same SHA256 as the earlier campaign copy, so this is additional reading of the same source, not another work. Local source: `sources/li_detection_priority_round3/lagarias2007.pdf`.

## Priority context actually established from the original source

Theorem1.1, equation(1.18),p1694 states, for an irreducible cuspidal unitary automorphic representation onGL(N) overQ, under its RH,

\[
 \lambda_n(\pi)=\frac N2 n\log n+C_1(\pi)n+O(\sqrt n\log n),
\quad C_1(\pi)=\frac N2(\gamma-1-\log2\pi)+\tfrac12\log Q(\pi).
\]

The constant formula is equation(1.13),p1693. Its proof depends on later sections, not all audited here. The finite-height sentence immediately after(1.16),p1694 records a finite positive-index window when RH holds to heightT, printed as `n<=T²/2(logT)²`; the denominator convention and its effective constants have not been independently audited in this note. The next paragraph explicitly credits eventual exponential growth from an off-line zero to Bombieri–Lagarias1999, Theorem1(c). Thus the first-negative-index calculation for the constructed beta family is a quantified instance of an established exponential masking mechanism. The original source does not assert the model-specific `8T²logT` asymptotic, and its priority remains unassessed.

An exact normalization confirmation appears onp1697: for the trivialGL(1) representation the article's completed entire function is `2xi(s)`. This agrees with the beta campaign convention `F(1)=1` and `Z=pi^{s/2}F/[s(s-1)Gamma(s/2)]`, without a factor one half.

## Printed step whose supplied majorants do not justify the conclusion

Section6 proves Theorem6.1, equation(6.2): the finite-place term differs from an incomplete Li sum at height `sqrt n` by `O(sqrt n logn)`, for each fixed automorphic representation.

The proof chooses horizontal height `T=sqrt n+epsilon_n`. Onp1725, equation(6.12) bounds the unit-step growth of `k_n(s)+1=(1+1/s)^n` by `e^{n/T²}<=e`. Equation(6.10),p1724 supplies a factor one half of decay per unit increase of the real part for the absolute Dirichlet-series majorant. The text then claims geometric decrease of the product. These stated upper bounds alone do not imply it, since `e/2>1`.

It would not be valid merely to replace this `e` by a number below2 at `T~sqrt n`: for `s=sigma+iT`, the exact modulus is

\[
 |1+1/s|^n=
 \left(\frac{(\sigma+1)^2+T^2}{\sigma^2+T^2}\right)^{n/2},
\]

whose logarithm is approximately `sigma+1/2` when `sigma` is small compared with `sqrt n` and `T²~n`. This can outgrow a `2^{-sigma}` majorant. An unproved cancellation of the complex integrand is not an absolute-value repair.

This observation concerns the displayed estimate, not a demonstrated counterexample to Theorem6.1. The alternate contour below proves the final stated error using the same standard inputs.

## Alternate height repairs the final theorem's remainder

Choose instead `T=2sqrt n+epsilon_n`, `0<=epsilon_n<=1`, avoiding zero ordinates by at least a constant multiple of `1/log(n+2)`. The standard `O(logT)` count in a unit interval permits this choice. Keep the same right edge `sigma_1=2sqrt n` and a left edge `-3<sigma_0<-2` avoiding the fixed finite sets of trivial-zero real parts as in the original proof.

1. **Right vertical edge.** The kernel is at most `exp(sqrt n/2)+1`. The absolutely convergent logarithmic derivative is at most a constant times `2^{-2sqrt n+O(1)}`. Their product decays exponentially, and the edge length is `O(sqrt n)`, so its integral is `o(1)`.

2. **Horizontal edges, bounded real part.** For `sigma_0<=sigma<=4`, the kernel stays bounded because `n/T²<=1/4`. The standard logarithmic-derivative estimate off zero ordinates gives `O(log²(n+2))`. This bounded-width part contributes that amount.

3. **Horizontal edges, real part at least3.** The unit-step kernel growth factor is now at most `e^{1/4}`. The Dirichlet majorant drops by one half, so their product envelope has ratio `e^{1/4}/2<1`. The extra `-1` in the kernel is bounded separately against the decaying majorant. Integrating unit segments gives a bounded contribution. One need not assert that the actual oscillatory logarithmic derivative decreases pointwise; its absolute Dirichlet majorant is what decreases.

4. **Left vertical edge.** Here `|k_n(s)|<=2`; the standard functional-equation/logarithmic-derivative estimate is `O(log(|t|+2))` on the selected edge. Its length is `O(sqrt n)`, giving `O(sqrt n log(n+2))`.

Trivial-zero residues are still `O(1)` for fixed representation, as in the source: there are finitely many in the selected real-part interval, and their transformed-root moduli are below one. Consequently the residue argument yields

\[
 S_f(n,\pi)=\lambda_n(T,\pi^\vee)+O(\sqrt n\log(n+2)).
\]

The cutoff can then be returned to `sqrt n` at the cost already allowed by the theorem. In the band `sqrt n<=|Imrho|<=2sqrt n+1`, the critical-strip condition `0<Re rho<1` implies

\[
 |1-1/\rho|^n\le(1+1/|\Im\rho|^2)^{n/2}\le e^{1/2}.
\]

Each zero therefore contributes `O(1)`, while the total band count is `O(sqrt n log(n+2))`. This proves the stated `O(sqrt n logn)` replacement error, including multiplicities. A cutoff exactly at a zero changes only a lower-order count and is covered by the same bound.

The proof still depends on standard automorphic zero-count and logarithmic-derivative facts stated in the original source; those external inputs are not being re-proved in full here. The repair loses the source's intermediate sharper horizontal estimate, but preserves precisely the final Theorem6.1 remainder used by Theorem1.1.

## Status and reuse

Classification pending independent review: printed geometric-decay justification insufficient as written; a supplied alternate contour preserves the main result's error. Do not publicly call the theorem false or claim a new correction. A discovery-only web snippet from a2026 external project already mentions a larger-height stepping repair; its mathematical source chain has not been audited. The reusable lesson is quantitative: changing a contour height by a fixed factor may repair an absolute-value estimate if the cost of moving the zero-sum cutoff fits the final remainder.

The publisher PDF carries an explicit personal-copy copyright notice. The shared research archive should contain the original analysis, source URL, bibliographic record and permitted short quotations, and exclude redistribution of that PDF unless independently authorized.

## Exact witness that the original product majorant can increase

This strengthens the observation beyond merely comparing the loose constants `e` and2. Take `n=10000`, `sigma=3`, and **any** `T in [100,101]`, so the original permitted height interval is covered, including any zero-avoiding choice. Let `A_n(s)=(1+1/s)^n`, `s=3+iT`, `y=T²`. Then

\[
 \frac{|A_n(s+1)|^2}{|A_n(s)|^2}
 =\left[\frac{(y+25)(y+9)}{(y+16)^2}\right]^{10000}
 =\left[1+\frac{2y-31}{(y+16)^2}\right]^{10000}.
\]

On `10000<=y<=10201`, the increment exceeds `19969/10217²>1/6000`. Keeping only the first three positive binomial terms therefore gives

\[
 \frac{|A_n(s+1)|^2}{|A_n(s)|^2}
 >1+\frac{10000}{6000}
    +\frac{\binom{10000}{2}}{6000^2}
 =\frac{9733}{2400}>4.
\]

Thus the actual kernel modulus grows by a factor greater than2 in this step, so its product with the `2^{-sigma}` Dirichlet majorant increases. This is a witness about the majorant, not a lower bound for the actual logarithmic derivative, whose terms can cancel. Conversely the repaired height gives envelope ratio at most `e^{1/4}/2<2/3`, using `e^{1/4}<1/(1-1/4)=4/3`.

The exact standard-library Fraction calculation is preserved in `experiments/code/lagarias_contour_majorant_exact_round3.py` and its JSON result. It uses no floating-point or transcendental evaluation. The alternate-contour proof and the published source scope remain pending independent review; no false-main-theorem classification is made.
