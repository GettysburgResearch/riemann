# A quadratic-sieve tail for the sextic dual core

**Status.** This is a source-qualified partial estimate for the restricted physical dual sum, not a complete inverse-moment estimate or a new individual zero-free region. It uses Goldmakher–Louvel's quadratic large sieve, the October 5 completed-theta mean and cube inversion, and the physical sector/Poisson/Fourier and zero-mask identities in [the general dual-core note](../2026-10-29-general-dual-core-sieve/README.md). The recent source proofs and their exact physical calibration are not independently established here. No Hu zero-free hypothesis is used.

## An ℓ² prefix bound

Work over E=Q(ω), with fixed good primes and finite ray data. The cube-inversion coefficient in the source is

    μ(c) overline(α(c))³ ξ(c)³ χ_c(bk)³ 1_{(c,f)=1},             (1)

with its original zeros, where α(c)=c/|c|, f is a good squarefree source label and k is fixed in the b-row sum. Put A_b(x) for its sum over `Nc≤x`. On b rows of norm ≤B,

    Σ_(Nb≤B)|A_b(x)|² ≪ (B x Nf Nk)^ε [B x+x² B^(1/2)].       (2)

Indeed write each good b uniquely as `b=b₀v²`, with b₀ squarefree. The identity `χ_c(v²)^3=1_{(c,v)=1}` is exact with zeros. For fixed v, the factor `χ_c(k)^3`, the f and v masks, μ(c), angular phase and finite-ray factors form a common column vector of squared norm `≪x`. Goldmakher–Louvel Corollary 1.2 applies to the quadratic character `χ_c(b₀)^3` for the sextic FHL source family, including its fixed ray-sector reciprocity phases. Its bound is `≪(B/(Nv)²+x)x`. Summing over `Nv≲sqrt(B)` uses `Σ 1/(Nv)²<∞` and `#{Nv≤sqrt B}≪sqrt B`, yielding (2). Here b may be further restricted to sixth-free rows after positivity. This is an average over the **actual b rows**: k stays a fixed common column factor rather than enlarging the row to bk.

## Partial summation of the cube tail

Let `P_{bk}(D;f)` be the normalized squarefree theta polynomial and `T_{bk}(Z;f)` the completed theta sum in the source cube inversion. The source's elementary coefficient bound gives uniformly in its row and f

    |T_{bk}(Z;f)|+|∂_(log Z)T_{bk}(Z;f)| ≪ Z^(1/2+ε),            (3)

with bounded or empty small scales handled separately. The derivative only replaces the common smooth W by `−W/2−xW′`. In the cube inversion, c changes the scale `Z=D/(Nc)³` but does not change the row bk, the label f, or the common profile.

For cutoff C≥1, Stieltjes partial summation, the pointwise derivative bound (3), Minkowski and (2) give the tail bound

    ||tail||_(ℓ²_b) ≪ (DBNfNk)^ε D^(1/2)
                        [B^(1/2)C^(−2)+B^(1/4)C^(−3/2)].       (4)

For the short part, source `prop:R` enlarges the row labels bk to the complete ball of norm `≪BK`. Weighted Cauchy gives

    ||short||²_(ℓ²_b) ≪ (DBNfNk)^ε [BK+B²K² Nf C³/D].           (5)

Set

    C=max{1, (D²/(B K² Nf))^(1/7),
             (D²/(B^(3/2) K² Nf))^(1/6)}.                    (6)

When the first ratio is ≥1, this C is at most `D^(1/3)` and balances the two tails against the nontrivial short term. If it is <1, the elementary bound `Σ_{Nb≤B}|P_{bk}|²≪BD` is already dominated by the first nontrivial term below. Thus, for all bounded polynomial scales,

    Σ_(Nb≤B)|P_{bk}(D;f)|²
      ≪ (DBNfNk)^ε [BK
          + B^(11/7)(Nf)^(4/7)K^(8/7)D^(−1/7)
          + B^(5/4)(Nf)^(1/2)K].                               (7)

The B²K²Nf/D term from C=1 must not be retained separately: when `B K² Nf≤D²` it is dominated by the second term of (7), and otherwise the trivial BD bound is dominated by that same second term. This global fallback is important after expanding the moving masks.

## Inserting the physical masks and deriving the core range

In the source physical ledger write original `d₀=k d′`, auxiliary `Ng≈G`, dual `v=b a⁶`, `Nb≈B`, and residual column length `D≈P/(D₀G)`. Expand the combined a,d′ puncture once over `e|rad(a d′)`. Terms with `(e,k)>1` vanish, the surviving `f=gke` is squarefree, and `χ_e(bk)` is retained as a bounded b-row factor. Apply (7) with this f and `D′=D/Ne`. After square roots and the exterior `(Ne)^(−1/2)` from n=e m, the two nontrivial e powers are respectively

    −1/2+2/7+1/14=−1/7,       −1/2+1/4=−1/4.                  (8)

Their divisor sums cost `(Na Nd′)^ε`; the BK face has exponent −1/2 and is likewise harmless. No e-dependent inequality `B Nf≤(D′)²` is assumed. Source profile, finite ray and physical phase separations must be performed before positivity, as in the general ledger.

After summing the original d′,k,g dyads and the `O((H/B)^(1/6))` roots a, the physical prefactor is bounded by `Y^(1/30)D₀^(2/3)K^(−5/6)B^(−1/6)`, using `H≲P²K/(Y D₀²)`. With `D₀=Y^d`, `K=Y^κ`, `G=Y^g`, `B=Y^b`, the three faces from (7), after `Nf≈GK`, are

    1/30 + 2d/3 + κ/6 + 5b/6,
    −29/210 + 17d/21 + 37κ/42 + 59b/42 + 5g/7,
    1/30 + 2d/3 + 2κ/3 + 13b/12 + g/2.                    (9)

The source offdiagonal in an individual g dyad is bounded by the full square and its subtracted artificial diagonal separately; the BK face budgets the diagonal, so no local diagonal cancellation is claimed.

On `d+g+6κ/5≤C`, `0≤κ≤d`, the faces in (9) are at most respectively

    1/30+2C/3+5b/6,
    −29/210+17C/21+59b/42,
    1/30+2C/3+13b/12.                                         (10)

For the second and third, substitute `g≤C−d−6κ/5`; the remaining d and κ coefficients are nonnegative and the maximum occurs at `d=C, κ=g=0`. The first is maximized at the same point. Consequently, after logarithmic dyad sums and fixed losses:

* At the `Y^(21/20+ε)` target, the restricted dual-core dyads are controlled for `b≤2257/2950≈0.76508475`.
* For a strict saving below the staged θ threshold `19949123/18750000`, every fixed `b<723364487/921875000≈0.78466656` is controlled.

The two noncritical faces in (10) remain strictly below each target at the indicated endpoints. The bound applies only inside the signed small-divisor core and only to the specified sixth-free **dual-core** range; its complement, the imported physical/source identities and the full zero-free target remain open.

**Independent reviews.** High_match and Other_families checked the GL prefix and common k mask, the source theta short/Abel tail estimates, the global trivial fallback, the two e-divisor exponents and the exact core cutoffs. The individually subtracted artificial diagonal is kept separately. These reviews do not establish the imported source/physical calibration.

## Why the short source mean still uses BK

For the completed theta factor, the source's proof of `prop:R` first writes its row label uniquely as `u₀ s v²` and applies a squarefree-row reflection estimate. If a physical row is `bk` with fixed k, writing `b=b₀v²`, `k=k₁w²` and `t=(b₀,k₁)` gives squarefree part `s=(b₀/t)(k₁/t)` and square part `vwt`. The finitely many choices `t|k₁` and the corresponding original zero masks can be separated. However, the reflected cusp kernel in the source depends on the **norm of the full squarefree part**, in particular on `N(k₁/t)²`, as well as on the auxiliary label and row norm. Although the quadratic symbol factors into a varying b₀/t character times a fixed column twist, replacing the complete row ball BK by the number B solely on that basis does not check the transformed radial weights or the associated conductor scale. The present proof therefore enlarges to BK in the short completed mean and uses actual B rows only in the independent GL prefix and elementary tail. A sparse-row reflection estimate that retains the fixed multiplier and establishes a better k-dependence would be a further arithmetic input; it is not asserted here.
