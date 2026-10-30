# A second-Poisson bound for the auxiliary-g dyad

**Status.** This is a source-qualified partial estimate for the [physical signed correlation](2026-10-29-61-72-dual-correlation/README.md), using the exact phase and frequency-fibre identities of paper 5 v3 §10.2–§10.3 and the unrestricted sixth-order L₂ sieve. It does not prove the inverse target or a zero-free region. Independent audit is requested. All fixed-ray, bad-prime and height conditions are as in the [low-dual note](2026-10-29-low-dual-theta-bound.md).

Fix the original squarefree gcd `d`, its good divisor `k|d`, and an auxiliary gcd dyad `Ng≈G`. Restrict to `D₀≤Y^(7/10)` up to small losses, since the generic original-gcd bound already covers larger d. Let `Nd≈D₀`, `Nk≈K`, residual column length `D≈P/(D₀G)`, and original dual-frequency length `H`. For each fixed d,k,g the theta polynomial from the first Poisson expansion is

    S_g(v) = Σ_(n good sf, (n,d)=1)
      C_{−1}(n) ν(n) χ_n(v) χ_n(g)^4 χ_n(k)^5 U(Nn/D)/sqrt(Nn).  (1)

This expression keeps all original zero masks. It has row v of size H and label g of size G. It is essential to use this v as the row: the variable h in paper 5 §10.2's `h f² g²/d` is the **new Poisson frequency**, not the original row `vk`. One could absorb the fixed twist into a new inverse row divisible by k once, not k³; we instead retain it as a column multiplier and apply the sieve directly to the undilated new frequency. The factor `χ_n(k)^5=overline(χ_n(k))` is multiplicative, zero-extended and may be included in the coefficients. No uniform growing-conductor fixed-ray theorem is invoked.

For each fixed d,k, replay paper 5 (10.3)–(10.10) on (1), with its label scale F=G and original row scale H. The exact Gauss phase, coprime projector, divisor masks, logarithmic Fourier separation and frequency-fibre count are unchanged by this additional multiplicative coefficient; after the common-factor split it contributes only unit-bounded outer scalars and the column multiplier `χ_n(k)^5`. At the stage corresponding to (10.10), apply the arbitrary-coefficient unrestricted-row sextic sieve to each residual inverse polynomial rather than the source's special inverse mean. If

    B(R,D)=R+D R^(1/6)+R^(5/6)D^(1/3)+R^(1/3)D^(5/6),
    R₀=D²G²/H,

then the replay yields

    Σ_(g≈G) Σ_(Nv≤H) |S_g(v)|²
       ≪ (YD₀KG H)^ε G [H + H/(GD) B(R₀,D)].               (2)

Here the terms H and R₀ arise respectively from the original diagonal and the first sieve term. The source's internal gcd and projector dyads cost only subpowers: their residual column scale is ≤D, `Σ_(Ns≈S)1/Ns≪1`, and the frequency fibre has divisor-bounded multiplicity. For a twisted column the unrestricted sieve applies because its ℓ² mass is `≪D^ε`, regardless of the growing conductor of k. Fixed punctures are zero masks in that coefficient vector. Fourier-profile and nonempty-tail conditions are the same as in §10.3; when R₀<1 use the source's rapid-transform tail before inserting the sieve. Formula (2) includes only the nonprincipal physical terms, with the artificial principal restoration dealt with as in the low-dual note.

The first Poisson exterior factor is `(Y/P)/(GK)`; there are `≪D₀^(1+ε)` admissible pairs `(d,k)` with `k|d` in these norm dyads. The natural cutoff is `H≤H₀=Y^ε P²K/(Y D₀²)`. The right side of (2), multiplied by H/(GD) where appropriate, is nondecreasing in H, so it suffices to substitute H₀. Then `R₀=Y^(1+O(ε))/K`. At `P=Y^(6/5)` put `D₀=Y^d`, `K=Y^κ`, `G=Y^g`. Up to subpowers the resulting bound for the full `(d,κ,g)` physical dyad is

    Y^(6/5−d) + Y^(1−κ)
      + Y^(41/30−d−g−κ/6)
      + Y^(37/30−d/3−g/3−5κ/6)
      + Y^(4/3−5d/6−5g/6−κ/3).                         (3)

Hence this portion is `O(Y^(1+ε))` if

    d≥1/5,
    g≥11/30−d−κ/6,
    g≥7/10−d−5κ/2,
    g≥2/5−d−2κ/5,                                       (4)

along with the original dyad feasibility and g≥0. In particular at `(d,κ)=(1/4,1/10)`, (4) only requires `g≥1/5`, whereas the first unrestricted-sieve route in the [sparse-dilation note](2026-10-29-sparse-dilation-theta-target.md) requires `g≥3/10`. Neither route alone controls all g in the unresolved small-gcd region. The result depends on an exact replay of the cited phase, transform, and fibre identities with the extra k twist; those analytic inputs and this replay have not been formally verified.

**Independent reviews.** Families and High_match checked the common-factor cancellation of `χ_s(k)^5`, the surviving arbitrary column multiplier, the unchanged frequency-fibre bound, the normalized formula (2), and the exact exponents and inequalities (3)–(4). These reviews remain conditional on the cited phase, profile, mask and sieve inputs.
