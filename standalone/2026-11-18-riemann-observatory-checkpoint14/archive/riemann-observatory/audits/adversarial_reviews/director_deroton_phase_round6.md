# A unitary-phase derivative obstruction and a replacement lower proof

Inspected source: de Roton2006, DOI10.24033/bsmf.2516, primary29-page PDF SHA256 `6b379ceeead2c10e614bd4be268c9672f0b364fa95799a5474a9479a82f9e445`, printedpp431–434. Proposition5.1(12) claims decay for bothφ=U_F1_(0,1) andΦ=xφ′, and the argument then invokesΦ∈L² to apply the conditional Proposition4.1. The director independently checked the following explicit and general contradictions. Proposition4.1's conditional statement is not itself refuted.

## Exact classical witnesses

For the zeta gamma phase,

    Uζ(s)/s=2(2π)^(-s)Γ(s)cos(πs/2)/(1−s).

Direct Mellin integration on0<Re s<1 identifies the phase image of the indicator asφζ(x)=sin(2πx)/(πx). Hence

    Φζ(x)=xφζ′(x)=2cos(2πx)−φζ(x).

At every positive integer it equals2, so it is notO(1/x). It is notL²:φζ isL² and2cos(2πx) is not, so their difference cannot beL². This uses the actual Selberg functionζ, not a hypothetical model, and no RH or numerical estimate.

Independently, for the primitive odd characterχ4,

    Uχ4(s)/s=(2/π)^sΓ(s)sin(πs/2)/(1−s),
    φχ4(x)=(1−cos(πx/2))/(πx/2),
    Φχ4(x)=sin(πx/2)−φχ4(x).

Duplication and reflection of gamma establish the first identity; integration by parts after y=πx/2 establishes the second. Alongx=4n+1 the derivative tends1 and it is bounded away from0 on infinitely many intervals of fixed positive length. Thus it also contradicts both the claimed d1 tail andL² conclusion. Period cancellation gives the complementary-functionL² premise for this actual character unconditionally. Sourcep433's differentiated Bessel model omits the chain-rule factorx^(1/d); the undifferentiated k0 phase estimate is separate and can be retained.

## A universal domain obstruction

LetM be the unitary Mellin transform fromL²(dx) toL²(dt/(2π)) on s=1/2+it, and letU be multiplication by any measurable symbolu(s) of modulus1. Putφ=U1_(0,1]. In distributions on the positive axis, D=x∂_x corresponds to−s on Mellin transforms. This identity requires no pointwise boundary integration: under the isometryg(v)=e^(v/2)φ(e^v), D corresponds weakly to∂_v−1/2, whose Fourier multiplier for conventione^(itv) is−(1/2+it).

IfDφ wereL², its Mellin transform would therefore be

    −s Mφ(s)=−s u(s)/s=−u(s),

which has modulus1 almost everywhere and infiniteL² norm. This is impossible. Equivalently the closed weak-derivative domain is preserved by every unit-modulus spectral multiplier, whereas the indicator's logarithmic representative has a jump. The obstruction is a classical operator-domain fact; no novelty or obstruction to all spectral RH approaches is claimed.

Thus the phase-image indicator can never satisfy the derivative membership required in the source's application. A pointwise tail correction alone would not justify that application. The explicit classical kernels additionally refute the printed pointwise assertion.

## Replacement proof: no differentiated phase kernel

The indicator-layer identity

    x^(-w)1_(0,1)(x)
      =1_(0,1)(x)+w∫_0^1v^(-w−1)1_(0,1)(x/v)dv

converges as anL² Bochner integral for Re w<1/2, since the dilation has normsqrt v. A bounded Mellin multiplier commutes with each dilation. This gives the corresponding phase action usingφ alone. For the explicit classical kernels it continues the zero vectors using their undifferentiated tail bounds and bypassesΦ entirely.

A more general repair avoids even pointwise bounds onφ. Letp be the actual pole order and letV=P^(-2p)U_F, P(s)=(s−1)/s, be the phase ofA=P^pψ_F. Its gamma ratio is analytic and nonzero on0<Re s<1, unimodular on the line and has magnitudeO_F(T^(d(σ−1/2))) on fixed substrips. Choose0<c<1/2<κ<1 with d(κ−1/2)<1/2. The inverse Mellin transformsR_w^c,R_w^κ ofV(s)/(s−w) exist in the respective weightedL² spaces for w near a fixed critical zero. Tested contour shifting gives

    R_w^κ=R_w^c+V(w)x^(-w).

On[λ,1] use the right side, and on[1,∞) the κ-line transform. The c-weight controls ordinaryL² near0, while the κ-weight controls it at infinity. This defines a holomorphicL² cutoff family across Re w=1/2. Its derivatives give the required finite jets; noΦ∈L² assumption appears.

The pole-canceledA is supported on(0,1), either by the direct pole-tail removal or a tested far-right Mellin shift. The phase mapsA to its conjugate inversion, supported on[1,∞). Thus after cutoff atλ the zero jets are exactly orthogonal to all permitted dilates withα≥λ. Their leading local terms are∂_w^k[V(w)x^(-w)]. The remainder has bounded weightedc-line norm. Its cross with each leading monomial is bounded uniformly inλ by the finite integral∫_0^1x^(-2c)log^(2k)(1/x)dx. The normalized finite Gram blocks are the same Hilbert matrices as in the published argument; the target cutoff error isO(λ^(1/2−c)(1+log(1/λ))^k). Projection recovers the multiplicity-squared lower constant, with a fixed-finite-set errorO(1/log²(1/λ)) in the unscaled squared distance.

The complete replacement, including complex conjugation, support, target pairings and the original complementary-functionL² premise without GRH, is in effective_cluster62_deroton_phase_repair.md. The director read and independently checked all those steps. Therefore the printed derivative estimate and its invocation need correction, but the lower theorem used by the adaptive Selberg transfer has a complete independent replacement proof. This finding does not refute that theorem.

Independent evidence: witness62_deroton2006_prop51.md; ../mellin_phase_derivative_domain_skeptic62.md; effective_cluster62_deroton_phase_repair.md; ../prefix_formula62_deroton2006_phi_status.md. Next precise task is to formalize the closed-domain obstruction or quantify finite cutoff jets. No claim is made that a correction has been published or that the issue was previously unknown.
