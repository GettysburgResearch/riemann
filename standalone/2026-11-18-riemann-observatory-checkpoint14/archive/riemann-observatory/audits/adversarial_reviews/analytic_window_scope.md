# Scoped independent review: AF window and boundary errors

Reviewer: analytic_frontier agent. Original source arXiv:2608.13637v2, §§5.1–5.7, pp7–11; local PDF, text, rendered pp8–9 inspected. Parent separately read this source before requesting the review. This review is not whole-paper L3.

## Window lower bound

For ψMT(s)=cos(√2s), φ²(u)=ψMT(u/L) away from endpoint smoothing, so the displayed 1_{[−L/2+1,L/2−1]}≤φ² is false whenever u/L is a fixed nonzero interior point. The lower triangular correlation estimate in (5.2) is therefore indicator-specific. Check all uses:

- Prop5.2 uses only decay, upper bounds, bounded a and Fourier Poisson identity.
- Prop5.3 uses ∫Φ²=2πbL and first-moment decay; no triangular lower bound.
- Prop5.4's diagonal/offdiagonal identity and O(L²X) remainder do not use the lower bound; its final squeeze of Σ a_n²g(logn) does.
- Prop5.5 uses upper bounds and mass estimates only.
- Thm5.7 uses g(y)=L(ψ*ψ)(y/L)+O(1), and partial summation for the main term. This replaces the indicator-specific squeeze and gives the MT constant.

Thus the window issue supplies no main-theorem counterexample. Reasonable corrected scope: label the triangular lower bound and ensuing squeeze “for ψ0”; retain general rescaling for MT. A full check for arbitrary C² positive ψ needs ψ-dependent decay constants, but both displayed windows have the needed regularity and bounds.

## Boundary normalization

Prop5.2 normalizes by (aL²)². Its E1 bound L³B²logL yields O(B²logL/L). Its E2 bound L³B²l logL yields O(B²l logL/L), larger by l. At L=l, X=T/(2π), B=l+4√X, this is O(TlogL), not the displayed O(NlogL/L²)=O(TlogL/L). Both are o(N) for N≈TL/(2π). The displayed quantitative rate in Thm5.7 consequently is not established by these particular crude estimates, although the limiting constant survives. This can be repaired for the asymptotic theorem by retaining O(NlogL/L); obtaining O(N/L) would require stronger boundary control or another argument. This review has not proved that the stronger rate is false; the alternative argument below supplies the needed bound.

The distinction matters: failure of a displayed estimate to prove a sharper rate is not a witness that the asymptotic proportion theorem is wrong. The director reports independent frame-operator repair, checked below.


## Independent repair with the frame operator

After the initial loss was identified, an independent skeptic supplied a frame-operator approach; the director checked it. This reviewer then reconstructed it as follows. Put v(τ)=(hatφ(τ−α_k))_{0≤k<d}, H=∫_R |ν_X(τ)|v(τ)v(τ)^T dτ and J=∫_{τ∉I}|ν_X(τ)| ||v(τ)||²dτ. Since K(τ,τ')=v(τ)^Tv(τ'), the discarded-domain contribution satisfies |E2|≤2||H|| J. This uses a positive operator after taking absolute values, and does not assume ν_X≥0.

For every vector c, Parseval and φ²≤1 give

∫_R |Σ_k c_k hatφ(τ−α_k)|²dτ =2π∫_{−L/2}^{L/2}φ(u)²|Σ_k c_k e^{iα_ku}|²du≤2πL Σ_k|c_k|².

The last equality without φ² uses orthogonality of e^{2πiku/L} over an interval of length L. Hence the portion of H on |τ|≤4T has operator norm≤2πBL. On |τ|>4T, use |τ−α_k|≥|τ|/2, the square decay O(|τ|^{-4}), and |ν_X(τ)|≤B+log(|τ|/T); the trace is O(d(B+1)/T³). Thus ||H||≪BL.

For J use the squared envelope min(L²,r^{-2},r^{-4}), rather than the envelope's unsquared L¹ norm. An endpoint grid point contributes O(L). Distances kh∈[1/L,1] contribute O(1/(kh)); summing gives O(LlogL). Distances≥1 contribute O((kh)^{-3}) with total O(L). The far |τ|>4T tail is negligible as above. Thus J≪BLlogL and |E2|≪B²L²logL. After division by a²L⁴ this is O(B²logL/L²), smaller than the E1 error O(B²logL/L). With B²≪T and N≈TL this proves the displayed Prop5.2 remainder O(NlogL/L²). Its normalized error is smaller than O(N/L), so the Theorem5.7 rate survives.

Status: **the printed crude E2 estimate loses a factor, but an independently reconstructed frame estimate repairs the needed quantitative statement**. This is not a verified mathematical error in Prop5.2 or in the main proportion theorem. Keep the initially insufficient estimate as negative knowledge about the proof's bookkeeping. Cross-reference the independent review `li_skeptic.md` and director adjudication when their final appendices are merged.
