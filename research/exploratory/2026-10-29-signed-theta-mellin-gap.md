# A Mellin series for the signed theta remainder

**Status.** This identifies a concrete transformed series and the quantitative gap in the **separated all-natural-row model** of [the signed-theta note](2026-10-29-signed-theta-mass-cancellation.md). It does not identify the full coupled physical Poisson expression with that model or prove the displayed target estimate. The bounds attributed to [rStation paper 5 v3](https://rstation.ai/problems/riemann_hypothesis/papers/5/v3) retain that source's imported analytic dependencies and have not been independently verified here.

Fix the good-prime set, finite ray data and a nonzero smooth annular U. Let

    P_h(D)=D^(−1/2) Σ_{n good sf} α(n)^(−1)γ₂(n)ξ(n)χ_n(h)U(Nn/D),

with its original zeros, as in the [diagonal calculation](2026-10-29-sextic-dual-diagonal-obstruction.md). First take h to range over nonzero good ideals with the appropriate primary/finite-unit presentation; a finite sum handles the original element-row sectors. Define for Re s>1

    Z_D(s)=Σ_h |P_h(D)|²/(Nh)^s.                             (1)

The column sum is finite for each D. Open its square. For each ordered pair (n,m), the row factor χ_n(h)overline(χ_m(h)), after the fixed finite sector/primary presentation, is an imprimitive Hecke character. Its primitive conductor is supported on rad(nm) and fixed S; the original missing zeros are finitely many Euler deletions. If n≠m, a good prime occurs in exactly one of these squarefree indices, so the ratio is nonprincipal. Therefore, for Re s>1 and hence by continuation,

    Z_D(s)= Z_diag,D(s) + Z_off,D(s),                        (2)
    Z_off,D(s)=Σ_{n≠m} b_n overline(b_m)
                 L_K(s,ξ^*_{n,m}) E_{n,m}(s),

where b_n is the displayed normalized θ coefficient, ξ^* is primitive nonprincipal, and E is the exact finite Euler-deletion product, including S and shared-prime masks. Finite unit and fixed ray sectors contribute a finite sum of expressions of this same kind. For an unrestricted good-ideal h sum the diagonal is

    ζ_K(s) Σ_n |b_n|² ∏_{p∈S ∪ supp(n)} (1−(Np)^(−s)).      (3)

With a fixed h-ray sector, (3) is its principal character component; the remaining finite ray-character components are holomorphic at s=1. For each fixed D, the off-diagonal in (2) is a **finite** combination of entire Hecke L-functions times entire finite products. Thus it has no genuine secondary pole in s; the only possible pole in Z_D is the principal diagonal pole at s=1. The exponent 5/6 in the known mean bound does not itself assert a pole at s=5/6. A second generating series in the varying parameter D could have different singularities, and this observation does not analyze or exclude them.

Let V be the smooth radial primal row profile supported away from 0 and let f(t) be its radial Fourier transform in the self-dual measure. Its Mellin transform `F(s)=∫₀∞ f(t)t^(s−1)dt` is holomorphic for Re s>0, rapidly decays on fixed vertical strips, and obeys F(1)=0. For H=D²/Y, Mellin inversion gives

    Σ_h f(Nh/H)|P_h(D)|²
       = (1/2πi) ∫_(c) F(s) H^s Z_D(s) ds,   c>1.           (4)

The diagonal pole at s=1 contributes no residue because F(1)=0; its remaining shifted integral is not zero. On Re s=5/6+η, the finite Euler products and Σ_n |b_n|²≪1 give Z_diag,D(s)≪D^ε(1+|t|)^A, hence this integral is ≪H^(5/6+η)D^ε, which is ≪D^(35/36+O(η)+ε) when H=D^(7/6). Fixed finite masks and unit sectors may be inserted before summing. The nonprincipal terms can be shifted in Re s>0 subject to the usual polynomial vertical bounds, but (4) remains the separated model: the exact physical kernel depends on both individual column norms and its gcd/divisor data, and cannot be replaced by one fixed f without proof.

## Source bound and a specific improvement target

At H=D^(7/6), choose σ₀=5/6+η with η>0 fixed and small. The off-diagonal estimates in paper 5 §10 give, for a fixed common smooth row profile,

    offdiag(K) ≪ (KD)^ε [D + K^(5/6)D^(1/6)].              (5)

Its Theorem 5 also bounds the positive full row mean by K(KD)^ε, and the diagonal is O(K); hence offdiag(K) is independently O(K(KD)^ε). A smooth dyadic decomposition of (1) therefore uses

    offdiag(K) ≪ (KD)^ε min{K, D+K^(5/6)D^(1/6)}.

Summing dyads K≤D with the first bound and K>D with the second yields, after allocating small powers and profile-seminorm costs,

    Z_off,D(5/6+η+it) ≪_{η,ε} D^(1/6+ε)(1+|t|)^A.       (6)

The fixed finite ray phases are expanded before applying the two inverse norms. The exponent A is fixed after η and the smooth partition are selected. This inference is conditional on the source's uniform smooth-profile and polynomial-height statements; at the endpoint η=0 it would need an extra limiting argument.

A sufficient improvement for the signed model is, for every small fixed η>0,

    Z_off,D(5/6+η+it) ≪ D^(1/36+ε)(1+|t|)^A,                (7)

or the correspondingly weaker statement only for the integral in (4) with its actual F(s). Shifting (4) to that line gives `H^(5/6+η)D^(1/36+ε) ≪ D^(1+ε')`, after choosing η and the preliminary loss small enough. In contrast, (6) yields `H^(5/6)D^(1/6)=D^(41/36)` up to losses, exactly the currently available separated remainder. The needed source-exponent improvement is D^(5/36). Alternatively, a uniform subpower bound on Z_off,D at Re s=6/7+η would also meet the D-scale after shrinking losses.

No such estimate is claimed in the cited sources. A pointwise theorem for a fixed single Hecke character, an unrestricted positive second moment, or a spectral decomposition without control of the moving quadratic–cubic coupling does not establish (7). The finite-D pole calculation likewise does not prove that D^(41/36) is sharp or that the off-diagonal cancels. Any actual zero-free application must additionally restore the coupled row Fourier kernel, nonunit masks, gcd/divisor strata and common profiles in the full physical expression.

## Comparison with available L-value averages

The closest general higher-order central moment located is Diaconu–Ion–Paşol–Popa, [arXiv:2607.27131v1](https://arxiv.org/abs/2607.27131v1), Proposition 7.2.4. It bounds a positive weighted average of `|L(1/2,ψχ_af)|²` over a with fixed f, with a conductor cost `N(rad f)^(1/2+ε)`. It does not state a signed bilinear L-value sum over the two simultaneous θ-coefficient indices in (2). Its standing field hypothesis for order r is μ_{2r}⊂K; the r=6 form is not directly applicable over Q(ω), which does not contain μ₁₂. Its multiple-Dirichlet-series techniques may be a starting point for a new estimate but do not themselves provide (7).

De Faveri–Dunn–Hoffstein, [arXiv:2607.07911v2](https://arxiv.org/abs/2607.07911v2), use Rankin–Selberg methods and Kubota-series second moments to show large-sieve nonorthogonality in cubic and quartic families. That result gives no uniform cancellation estimate for this sixth-order quotient-character L-combination. The fixed-level cubic Gauss Type-I/II and metaplectic results face the moving quadratic twist and common-coefficient issue detailed in [the mixed cubic–quadratic gap note](2026-10-29-mixed-cubic-quadratic-gap.md). Expanding the L-functions in (2) by a Dirichlet series or approximate functional equation recovers a version of the original coupled row correlation; applying an absolute generic second moment by itself discards the signs that (7) needs. This is a targeted search, not an exhaustive nonexistence or priority claim.

**Independent review:** High_match checked the dyadic exponent and D^(1/36) threshold, and identified the shifted diagonal and fixed-ray qualifications stated above. The source’s uniform profile and height hypotheses remain imported.
