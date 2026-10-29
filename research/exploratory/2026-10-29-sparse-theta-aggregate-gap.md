# The sparse shared-factor theta estimate

**Status.** This identifies a sufficient source-conditional estimate and its generic-sieve range. The new sparse estimate is not proved in full and no zero-free region follows. The setup and source imports are those of [the growing-k calculation](2026-10-29-low-dual-theta-bound.md); in particular the theta polynomials use paper 5 v3 (9.1), with original zero masks and fixed finite-ray data.

Fix a squarefree good outer ideal d′ and dyadic scales K,G,D,H≥1. Take squarefree k≈K and g≈G with `(k,g d′)=1` and `(g,d′)=1`, and nonzero integral v with Nv≤H. For a common smooth annular U, let

    S_{h,f}(D;d′) = Σ_{n sf, (n,d′)=1}
       C_{−1}(n) ν(n) χ_n(h) χ_n(f)^4 U(Nn/D)/sqrt(Nn).  (1)

The true sparse rows and labels are h=vk and f=gk. The useful **aggregate** target is

    Σ_{k≈K} Σ_{g≈G} Σ_{Nv≤H} |S_{vk,gk}(D;d′)|²
       ≪_ε (K G D H Nd′)^ε K G (H+DG).                  (2)

A fixed-k target has no leading K; (2) is the corresponding sum over ≈K possible k. A bound of the form G(H+DG) for the aggregate would be false. Indeed take d′=1, D≈1 and choose U supported in a small neighborhood of 1 so the unit ideal is the only n, with U(1)=1. Then S=1 and standard good squarefree counts give LHS ≫KGH times logarithmic/subpower factors. Thus for H≫DG the version lacking K fails by a full K. This example does not refute a fixed-k estimate or (2).

In the physical dyad `Nd≈D₀`, `Nk≈K`, the residual column scale is D≈P/(D₀G). For fixed d′, the prefactor is `(Y/P)/(KG)`. There are ≪(D₀/K)^(1+ε) choices of d′, so (2), profile/sector matching, and the true cutoff `H≲Y^ε P²K/(YD₀²)` would imply

    block(d≈D₀,k≈K) ≪ Y^ε [Y/K + P/D₀].                 (3)

Consequently this target would control every dyad with D₀≥P/Y=Y^(1/5), independent of growing K. It would still leave smaller original gcds and therefore does not alone prove the complete inverse-moment bound.

Paper 5 (9.3) applied after dropping the shared-divisibility incidence instead gives only K²G(H+DG): the entire label annulus has scale GK and the entire row range scale HK. The missing saving is exactly a factor K. One cannot insert the density of multiples of k into that complete positive mean without an estimate that preserves the incidence.

## What the ordinary sextic large sieve already proves

For fixed k and g the moving χ_n(k)^5χ_n(g)^4 factors, puncture and finite rays are part of an arbitrary column coefficient vector of squared norm ≪D^ε; the v variable remains unrestricted. The de Faveri unrestricted-row sixth-order L₂ bound therefore gives, for every individual k,g,

    Σ_{Nv≤H}|S_{vk,gk}(D;d′)|²
       ≪ (K G D H Nd′)^ε
          [H + H^(1/6)D + H^(5/6)D^(1/3)
             + H^(1/3)D^(5/6)]
       ≪ (K G D H Nd′)^ε (H+D²).                        (4)

Hence the desired aggregate (2) follows whenever **H≥D²** or **G≥D**, up to the usual finite-sector, profile and subpower qualifications. The first condition makes (4) O(H), and the second makes D²≤DG. These are actual generic-sieve ranges, not a proof in their complement. At d=κ=0 and the maximal physical scale H=Y^(7/5), D=P/G, the first criterion is G≥Y^(1/2); it does not cover smaller auxiliary gcds, for which D>Y^(7/10). A precise shared-incidence estimate in that complement remains the analytical gap.

**Independent review:** High_match and Families checked the aggregate K factor, unit-column lower bound, d′ count, and the generic-sieve ranges. The cited source bounds and profile matching are imported, and (2) is open outside the indicated ranges.
