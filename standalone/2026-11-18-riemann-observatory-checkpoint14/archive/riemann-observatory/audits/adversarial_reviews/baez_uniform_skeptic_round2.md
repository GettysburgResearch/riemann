# Independent review: shrinking-epsilon Perron repair and ratio norm

Reviewer: li_advocate. Date:2026-11-17. I independently reconstructed the finite-height inverse-zeta patch and Perron error accounting from the equivalence agent's statements, then read its full `audits/baez_uniform_dependency_round2.md`. I also visually inspected Titchmarsh2nd edition1986, book pp.354–355/PDFpage182, in the downloaded primary scan. Result: no issue found in the conditional uniform reconstruction, with the small-epsilon qualification for the ratio step noted below. No novelty claim is made.

## Source-region precision

Titchmarsh Eq14.14.4 is printed on the equality line σ=1/2+A/loglogt. It cannot alone be cited as a half-plane bound. The adjoining near-line lower log|ζ| bound14.14.2 and uniform region14.14.5 bridge to a fixed positive right strip. On σ=3/4,14.14.5 gives O(sqrt(logt)/loglogt) for logζ. The fixed-strip Phragmén–Lindelöf step to σ=2 is valid: the Euler-series branch is bounded at2, and logζ divided by(Log(s+3))^(1/2) has bounded vertical boundary values and subquadratic growth. An exp(ηs²) damping argument removes the upper horizontal edge, with η↓0 afterward. All of this is conditional on RH as in the chapter; no simplicity or spacing input is added.

## Finite-height patch

For V large set δ=1/loglogV and split at U=exp(sqrt(logV)). If U≤|v|≤V, then loglog|v|≥(1/2)loglogV, so δ≥1/[2loglog|v|]; the actual-height near-line result applies with a fixed positive distance parameter and yields O(logV/loglogV).

For |v|<U, remove the pole with H(s)=(s−1)ζ(s), analytic and nonzero in Re(s)>1/2 under RH. Borel–Carathéodory on disks centered at2+iv, with radii3/2−δ/2 and3/2−δ, gives |logH|≤Cδ^(−1)log(|v|+3). The center value has this size directly from Log(1+iv)+logζ(2+iv); polynomial growth controls the real part on the outer disk. The conversion to1/ζ adds only a polynomial factor, absorbed in this bound. The result is O(loglogV·sqrt(logV))=o(logV/loglogV). Thus the finite-height reciprocal bound is uniform down to the required distance, including near fixed low zero ordinates. Substituting V for the actual height without this patch would have been unjustified.

## Perron errors and constant margin

For s=1/2+ε+it, height N^4 and left shift Re(w)=−ε/2, the reciprocal is analytic throughout the rectangle under RH; the pole of ζ becomes a zero of its reciprocal, and the only Perron residue is at w=0. If ε≥c/loglogN,c≥2, the whole rectangle lies at distance at least1/loglogV to the right of1/2, with V=|t|+N^4+3. The reciprocal bound splits as exp(A logN/loglogN+bL(t)), with A=8K,b=2K as in the draft. The splitting remains valid at small t because the N^4 argument is already in the increasing range of logx/loglogx.

The left edge gives N^(−ε/2)logN times that reciprocal bound. The two horizontal edges are O(N^(−7/2)) times it. The truncated Perron error is O(N^(−1/2)) up to harmless logarithms. At integer cutoff N, the half-weight endpoint correction is explicitly at most(1/2)N^(−Re(s)) and is included; alternatively a half-integer cutoff could avoid it.

Taking c=6(8K+1) absorbs the reciprocal loss and the logN vertical integration factor, leaving N^(−ε/3)exp(bL(t)) with constants independent of ε,N,t in the admissible range. The range may begin only at an enormous unspecified N; no effective practical threshold is claimed. This is a genuine reconstruction of uniformity and does not pretend that the original fixed-δ O-constant was already uniform.

## Independent check of J_ε=O(ε^(2/3))

For sufficiently small ε, say ε≤1/4, use the conditional uniform quotient bound |ζ(1/2+it)/ζ(1/2+ε+it)|≪|t|^(ε/2). On the union of δ-neighborhoods of zero ordinates, the squared quotient-minus1 weighted by1/|s|² is O((1+|t|)^(−3/2)); Riemann–von Mangoldt makes the total weighted union measure O(δ).

Off these neighborhoods, the RH partial-fraction logarithmic derivative bound is O(log(|t|+3)/δ) along the short horizontal segment. Integrating over length ε and exponentiating gives an error O((ε/δ)log(|t|+3)(|t|+3)^(Cε/δ)). If ε/δ is sufficiently small, this is bounded by O((ε/δ)(|t|+3)^(1/4)), whose squared weighted integral is O(ε²/δ²). Taking δ=ε^(2/3) gives J_ε=O(ε^(2/3)).

One must not assert the short-segment logarithmic derivative estimate uniformly through ε=1/2,t=0: that segment reaches the ζ pole at1. Restricting to sufficiently small ε avoids it and is exactly what the ε→0 proof requires. No unconditional quotient bound on this one-sided shift has been assumed; the Burnol-type input here is conditional on RH.

## Audit conclusion

The finite-height inverse lemma, uniform Perron rectangle, endpoint correction, constant margin and small-epsilon ratio-norm reconstruction survive this independent review. They support a scoped technical reconstruction of Báez-Duarte Proposition3.1 conditional on explicitly declared classical RH estimates. This is distinct from a whole-paper audit of every theorem in Balazard–Saias or Titchmarsh. Source limitations remain: the original BS article was read by the equivalence agent through a degraded primary-text mirror, not a publisher PDF; the published2003 Báez-Duarte version was not compared. The repair establishes the required mathematical bridge rather than an assertion about missing printed quantifiers being already explicit in the source.
