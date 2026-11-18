# Independent reconstruction and repair of a boundary estimate

Date: 2026-11-17. Source: Levent Alpöge and Ralph Furman, *More than two thirds of the zeta zeros are simple and on the critical line*, arXiv:2608.13637v2 (19 August 2026), https://arxiv.org/abs/2608.13637v2 . Source file: `sources/analytic/2608.13637.pdf`. Scope inspected independently: definitions (2.3)–(2.11), Proposition 5.2 and its proof (manuscript pp.8–9), Propositions 5.3–5.5, Theorem 5.7 and Remark 6.1. Pages 8–9 were also checked as rendered images. This is a scoped technical audit, not an endorsement or full audit of the paper's main critical-line claim.

## Outcome

The printed proof of Proposition 5.2 ends with a bound for its exterior integral E₂ which, after the displayed normalization, is weaker than the proposition's stated remainder by a factor comparable to L. That observation alone does not refute the proposition. An independent replacement estimate below, using Parseval and the sample-grid orthogonality, is stronger than required and repairs this specific proof step. The parent agent independently checked this replacement after receiving its statement.

Classification: **valid estimate supplied by an alternate argument; quantitative bookkeeping issue in the inspected proof repaired**. No claim that the paper's main theorem is false is supported by this finding. No novelty is asserted for the frame estimate.

## Precise assumptions and notation

Take T sufficiently large, L=log(T/(2π)), X=e^L=T/(2π), h=2π/L, d=floor(T/h), I=[T,2T). Let α_k=T+kh, k=0,…,d−1. Let φ be real, even, C², supported in [−L/2,L/2], satisfying 0≤φ≤1 and, for a constant C independent of T,

|φ̂(r)|≤C min(L,|r|⁻¹,|r|⁻²), r real.

These properties hold for the two fixed tapered windows used in the source, by its (2.7)–(2.8). The Fourier transform convention is φ̂(r)=∫ φ(u)e^(−iur)du. Also assume a=∥φ∥²₂/L≥a₀>0 uniformly, as holds for either fixed source window. Constants below may depend on the taper/window and a₀.

Define the real column vector v(τ)=(φ̂(τ−α_k))_{0≤k<d} and K(τ,τ′)=v(τ)^T v(τ′). Let ν=ν_X from the source. The only property of ν needed here is (5.7):

|ν(τ)|≤B+w_T(τ), B=L+4√X, w_T(τ)=log⁺(|τ|/(4T)).

Thus B²=O(T). Define the raw exterior integral

E₂=∫∫_{(I×I)^c} K(τ,τ′)² ν(τ)ν(τ′) dτ dτ′.

All bounds below concern this unnormalized E₂. The matrix Hilbert–Schmidt expression divides it by (aL²)²=a²L⁴.

## Lemma 1: uniform unweighted Gram bound

Let H₀=∫_R v(τ)v(τ)^*dτ. Then H₀≤2πL Id in the Hermitian matrix order.

Indeed, for any c∈C^d, Parseval gives

c*H₀c=2π∫ |φ(u)|² |sum_k c_k exp(iα_k u)|²du
≤2π∫_{−L/2}^{L/2}|sum_k c_k exp(2πiku/L)|²du
=2πL sum_k|c_k|².

Conjugating the coefficient vector if necessary yields the same expression under either inner-product convention. The common modulation exp(iTu) has unit modulus. The last equality is exact orthogonality on an interval of length L. This estimate does not depend on d.

## Lemma 2: a small weighted far tail

Set W=∫_R w_T(τ)v(τ)v(τ)^*dτ. Then W is positive semidefinite and

∥W∥≤tr W=O(d/T³).

The weight is zero for |τ|≤4T. For |τ|>4T and α_k∈[T,2T), one has |τ−α_k|≥|τ|/2. Hence ∥v(τ)∥²≤C′d|τ|⁻⁴ and

tr W≤C′d∫_{|τ|>4T} log(|τ|/(4T)) |τ|⁻⁴dτ=O(d/T³).

For H_ν=∫_R |ν(τ)|v(τ)v(τ)^*dτ, it follows from Lemma 1 that

∥H_ν∥≤2πBL+O(d/T³)=O(BL).

Here d=O(TL), so d/T³=O(L/T²) is negligible. This bound accounts explicitly for the logarithmically unbounded ν outside the central range; no global supremum assumption on ν has been made.

## Lemma 3: exterior diagonal mass

One has

J₀:=∫_{τ∉I}∥v(τ)∥²dτ=O(L log L).

To verify this, set R(δ)=∫_δ^∞ |φ̂(r)|²dr for δ≥0. The stated Fourier bound yields

R(0)=O(L), R(δ)=O(min(L,δ⁻¹)) for 0<δ≤1, and R(δ)=O(δ⁻³) for δ≥1.

For the sample α_k, the distance to the left endpoint is kh. Its distance to the right endpoint is T−kh≥(d−k)h. Therefore, using evenness,

J₀≤R(0)+2 sum_{j=1}^d R(jh).

For 1≤j≤1/h the sum is bounded by C h⁻¹ sum_j j⁻¹=O(L log L). For j>1/h it is bounded by C h⁻³ sum_j j⁻³=O(L). This proves the claim. The sample exactly at α₀=T contributes the finite R(0) term and causes no endpoint problem.

Combining with Lemma 2 gives the weighted version

J_ν:=∫_{τ∉I}|ν(τ)|∥v(τ)∥²dτ
≤B J₀+tr W=O(BL log L).

## Repaired exterior estimate

Since K²≥0 for real τ,τ′, symmetry and the union bound for (I×I)^c give

|E₂|≤2∫_{τ∉I}|ν(τ)| [∫_R K(τ,τ′)²|ν(τ′)|dτ′]dτ.

The inner integral is v(τ)^*H_ν v(τ). Lemmas 2–3 therefore imply

|E₂|≤2∥H_ν∥J_ν=O(B²L² log L).

After division by a²L⁴, this is

O(B² log L/L²)=O(T log L/L²)=O(N log L/L³),

where N=N(T,2T) is comparable to TL. Proposition 5.2's printed bound for E₁ is O(L³B² log L), whose normalized size is O(T log L/L)=O(N log L/L²). Thus E₁ dominates, and the proposition's stated total remainder follows from the printed E₁ estimate plus this alternate E₂ proof.

## What the printed estimate alone gives

The last line of the printed proof, manuscript p.9, is |E₂|≪L³B² l log L with l=L. Its normalization gives only O(T log L)=O(N log L/L). This does not by itself yield the smaller displayed Proposition 5.2 remainder. Propositions 5.3–5.5 concern the interior double integral and do not state a cancellation estimate for E₂. Remark 6.1 even records a log log T/log T rate, which is consistent with the weaker exterior bound. These observations motivated the repair; they are not counterexamples to the asserted estimates.

The alternate argument does recover the stated Proposition 5.2 remainder and removes this particular obstacle to the O(N/L) rate in Theorem 5.7. It does not check every other estimate in that theorem, the inertia argument, the main critical-line proportion, or the accompanying formalization.

## Reusable mathematical lesson and next step

The individual-entry estimate K²≤L²|K| loses the orthogonality of the sampled Fourier family and introduces an unnecessary long-distance logarithm. Bounding its full Gram matrix first supplies a factor O(L), while the exterior *squared* Fourier tails have total mass O(L log L). This is a concrete transfer of a frame bound to an explicit-formula truncation problem.

An immediate useful task is to apply the same weighted-Gram estimate to other finite-height explicit-formula matrices and record which window regularity assumptions suffice. For the present source, a future full audit should keep this replacement as a separate dependency lemma and inspect the remaining prime mean-value and zero-side steps independently. No communication to the authors or public allegation was made.
