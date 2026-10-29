# A quadratic-sieve slice of the long dual correlation

**Status.** This is a source-qualified partial upper bound for a restricted dual-frequency set, not a full signed-core estimate or an individual zero-free region. It assumes the original fixed-sector physical Poisson expression and uniform Fourier/profile separation used in [the low-dual note](2026-10-29-low-dual-theta-bound.md), plus the squarefree quadratic Hecke large sieve of [Goldmakher–Louvel, Theorem 1.1](https://arxiv.org/abs/1112.1642) and the source-to-quadratic reciprocity, conductor and zero-mask matching specified below. None of those source claims is independently proved here.

Put `P=Y^(6/5)`. In a dual dyad `Nv≈H`, restrict the good dual ideals to

    v=c³ a⁶,    c squarefree good,    Nc≈C,    B=C³.          (1)

The factors a and c may share primes; (1) is the unique decomposition of a good ideal whose sixth-free core is a squarefree cube. The remaining exponent patterns of sixth-free dual cores are not covered. Fix the original gcd/divisor dyads `Nd₀≈D₀`, `Nk≈K`, the auxiliary gcd dyad `Ng≈G`, and the source's fixed ray sectors. In the source's nonnegligible dual range

    H ≲ Y^ε P²K/(Y D₀²),                                      (2)

the physical contribution of this slice is

    ≪ Y^ε (Y/P)(D₀/K)(H/B)^(1/6) [B^(1/3)+P/(D₀G)]          (3)

and hence

    ≪ Y^(1/30+ε) [D₀^(2/3) K^(−5/6) B^(1/6)
                    + Y^(6/5) D₀^(−1/3) K^(−5/6)G^(−1) B^(−1/6)].  (4)

The source rapid-tail input is retained separately. The estimate bounds this selected set after absolute values and Cauchy; it makes no positivity claim about the complementary dual frequencies and does not bound the complete original correlation.

## Proof and masks

In the fixed-sector source formula, write the two coprime residual columns as `r_i=g n_i`; n_i are good squarefree with norm `≈D=P/(D₀G)`. Fix d₀, k, g, a and every finite ray sector before averaging c. The fixed a-mask and the k/divisor and g factors are common to both the n-polynomial and every c row. The exact identity, including zeros, is

    χ_n(c³a⁶)=χ_n(c)³ 1_{(n,a)=1}.                            (5)

Thus a separated one-column sum has coefficients

    λ_n = C(n) ξ(n) χ_n(g)^4 χ_n(k)^5
          1_{(n,a d′)=1} W(Nn/D)/sqrt(Nn),                     (6)

up to fixed-sector phases and fixed bounded norm twists, with `d₀=k d′`. The original source's exact powers and punctures are retained; equivalently, if an alternative fixed sector places a conjugate on the entire column, conjugate the common vector. Their squared mass is `≪D^ε`, by squarefree ideal counting and the source coefficient bounds. Crucially, neither λ_n nor the a-mask depends on c. The exterior factor involving `χ_g(c³a⁶)` is a row contraction and may be removed only after the two-column Cauchy step. No coprimality between c and a, g or k is assumed.

At every good prime, the cube of the sextic residue symbol is the quadratic residue symbol. Assume the finite primary/ray sector calibration identifies `χ_n(c)³`, including its zeros at `(n,c)>1`, with the quadratic FHL matrix in Goldmakher–Louvel up to a finite separable row/column phase. After splitting the finitely many fixed reciprocity sectors, the transposed or adjoint quadratic sieve applies to the common λ-vector and yields

    Σ_(c good squarefree; Nc≈C) |Σ_n λ_n χ_n(c)³|²
       ≪ (CD)^ε (C+D).                                        (7)

This is the important source interface: it does not follow from a quadratic sieve if its reciprocity phases depend on c in a way that changes the n-coefficients within a sector. The assumption is exactly the fixed-ray order-two matching, not a conductor-only comparison.

For `Nb≈B`, `Nv≈H`, the root count is `O((H/B)^(1/6))` (and the set is empty unless `B≲H`). Use this count after Cauchy, then enlarge the c sum to (7). The physical prefactor is `(Y/P)/(GK)`; there are `O(D₀/K)`, `O(K)` and `O(G)` choices of d′, k and g respectively, up to small powers. This proves (3). Inserting (2) gives (4). The kernel's bounded compact-norm dependence is separated before any row average by the source's logarithmic Fourier method; fixed sufficiently high tail orders and source seminorms are part of the assumption.

For the often-useful `D₀=K=1` case, (4) reduces to

    ≪ Y^(1/30+ε) [B^(1/6)+Y^(6/5)G^(−1)B^(−1/6)].          (8)

Writing `H=Y^h`, `B=Y^b`, `G=Y^g`, the more precise unspecialized bound (3) has main exponents `−1/5+(h+b)/6` and `1+(h−b)/6−g`. On the natural range `h≤7/5+ε` and `b≤h`, the first is harmless at target `Y^(21/20)`, and the second is within that target whenever

    b+6g ≥ h−3/10.                                             (9)

At the endpoint h=7/5 this requires `b+6g≥11/10`. For the weaker threshold `E*=19949123/18750000` needed merely to beat θ, the second exponent is strictly below E* when `b+6g>h−1199123/3125000` with fixed margin. The γ-range in (9) is an auxiliary-g dyad condition, not permission to cancel an artificial diagonal within a single dyad.

The slice is nonempty in the unresolved high-frequency band. For example, choose `H≈Y^(13/10)`, `B≈Y^(11/10)`, `G≈1`, `Nc≈Y^(11/30)` and `Na≈Y^(1/30)`. Squarefree ideal counting supplies ≫Y^(11/30) choices of c and ordinary ideal counting ≫Y^(1/30) choices of a in fixed compatible annuli; their products are distinct by uniqueness of (1). This is a genuine subset of the formerly unresolved `H>Y^(63/50)` band, but does not resolve the rest of that band or imply an improved zeta boundary.

## Square and fourth-power sixth-free cores: cubic sieve

A different slice has good sixth-free core `b=ℓ²` with ℓ cube-free, again allowing ℓ and a to share primes in `v=b a⁶`. After fixing a, g, k and d′, (5) is replaced by `χ_n(v)=χ_n(ℓ)² 1_{(n,a)=1}`. The cubic power-residue reciprocity and the same fixed-sector source matching identify `χ_n(ℓ)²`, including shared-prime zeros, with the cubic FHL matrix indexed by cube-free ℓ and squarefree n. De Faveri's Θ₃ bound gives the common-vector mean

    Σ_(Nℓ≈B^(1/2), ℓ cube-free) |Σ_n λ_n χ_n(ℓ)²|²
      ≪ Y^ε [B^(1/2)+D+(B^(1/2)D)^(2/3)],                   (10)

with D and λ as in (6). The coefficient and row masks remain as before; enlarging the ℓ sum is permitted after Cauchy. This uses [de Faveri Theorem 1.1](https://arxiv.org/abs/2610.04045) and the order-six-to-order-three FHL phase/mask calibration as source inputs.

Applying the same physical prefactor, root count and dual cutoff gives

    ≪ Y^(1/30+ε) [D₀^(2/3)K^(−5/6)B^(1/3)
      +Y^(6/5)D₀^(−1/3)K^(−5/6)G^(−1)B^(−1/6)
      +Y^(4/5)K^(−5/6)G^(−2/3)B^(1/6)].                    (11)

In particular, in the critical gcd range `d+g+(6/5)κ<7/50`, with `D₀=Y^d`, `K=Y^κ`, `G=Y^g`, this is `O(Y^(21/20+ε))` whenever `11/10≤b≤13/10`, where `B=Y^b`. The second and third faces are at most 21/20 from these b bounds and d,g,κ≥0. Nonempty support has `b≤7/5+κ−2d+O(ε)`, making the first face at most `1/2−κ/2+O(ε)`.

For the further special case `b=c⁴` with c squarefree, the cubic row length is `B^(1/4)` instead. The conjugate cubic FHL orientation handles `χ_n(c)^4`; thus the three exponents, after the same cutoff, are

    1/30+2d/3−5κ/6+b/12,
    37/30−d/3−5κ/6−g−b/6,
    5/6−5κ/6−2g/3.                                         (12)

In the same critical gcd range the first is at most `11/50+O(ε)` using the nonempty-support bound on b; the last is at most 5/6. Therefore every such fourth-power core with `b≥11/10` within the natural dual support is controlled at `Y^(21/20+ε)`. These square/fourth-power slices are distinct from the squarefree-cube slice except for the unit core. They do not cover general sixth-free cores with valuation 1, valuation 5, or mixtures of residue exponents.

## Fifth-power sixth-free cores: sextic sieve

There is a further high-core slice `b=c⁵` with c squarefree. Here `χ_n(c⁵)=overline(χ_n(c))`, including zeros, so the conjugate sextic FHL matrix and de Faveri's Θ₆ theorem apply to c-rows of norm `≈B^(1/5)` and the same fixed common λ-vector. Retaining all four faces of Θ₆ and inserting the physical factor and dual cutoff yields exponents

    1/30+2d/3−5κ/6+b/30,
    37/30−d/3−5κ/6−g−b/6,
    13/30+d/3−5κ/6−g/3,
    31/30−d/6−5κ/6−5g/6−b/10.                           (13)

In `d+g+(6/5)κ<7/50`, the first is at most `13/75+O(ε)` by `b≤7/5+κ−2d`; the third is at most `12/25`; and the fourth is already below 21/20. The second is at most 21/20 whenever `b≥11/10`. Hence this pure fifth-power slice is also controlled at `Y^(21/20+ε)` throughout the critical gcd range, subject to the sextic source orientation, sector calibration and profile inputs. This does not handle a general core containing both fifth powers and primes of other exponent classes.

## A mixed-core limitation of freezing two groups

Every good sixth-free core with no valuation 1 can be written uniquely as

    b=ℓ₂² ℓ₃³ ℓ₅⁵,   ℓ₂ cube-free, ℓ₃,ℓ₅ squarefree,        (14)

with pairwise coprime supports. The valuation-4 part is included through the square factors of ℓ₂. One may freeze any two groups, keep their characters as bounded common column multipliers with original zero masks, and apply the cubic, quadratic or sextic sieve to the remaining group. This is a valid arithmetic partition, but these three one-group bounds do not close the mixed region.

For example, at `D₀=K=G=1`, `H=Y^(7/5)`, and `Nℓ₂≈Nℓ₃≈Nℓ₅≈Y^(3/25)`, the core has `B=Y^(6/5)` and the residual column length is `D=P=Y^(6/5)`. The row/root prefactor is `Y^(1/30)B^(−1/6)`. In each of the three one-group sieves, its `D` face is the largest source face; summing the other two frozen groups costs `Y^(6/25)`. All three displayed upper bounds are therefore

    Y^[1/30−1/5+6/5+6/25+ε] = Y^(191/150+ε),              (15)

well above 21/20. Applying the full Θ₆ sieve directly to the sixth-free b-row instead improves this example's upper bound to `Y^(37/30+ε)`, still above the target. The dyad is nonempty: the a-root scale is `Y^(1/30)`, and disjoint-support ideals exist in the displayed fixed norm annuli. This calculation is a barrier to **these stated uses of the upper bounds**, not a lower bound for the actual dual sum or a claim that every possible method fails. Exploiting joint cancellation among the quadratic, cubic and sextic row groups, while retaining their coupled masks and phases, would require additional input.

**Independent review.** Families checked the power-character masks and source-qualified prefactors, the nonempty dyads, the square/cube/fourth/fifth-power scalar bounds, and the mixed-core exponents, conditional on the named source matching and analytic estimates.
