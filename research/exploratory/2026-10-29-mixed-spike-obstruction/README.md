# A spike obstruction to an untruncated mixed-moment argument

**Scope:** The broad row-independent prime-slot coefficient class; one fixed slot and a finite arbitrary dual source. This is an elementary obstruction to a proposed proof strategy, not a counterexample to the desired selected operator estimate or to any zero-free region. It does not establish an obstruction for fixed smooth prime profiles.

Let K be the Eisenstein field and let χ_I(u) be the usual zero-extended sextic character, with bad primes excluded from all ideals. Assume rows are good primary squarefree elements of norm in a fixed dyadic interval comparable with B, the prime-slot annulus has norms in [P,2P], and 2P<B/2. For fixed 0<σ<1, fixed k≥1, and P=B^w with 0<w<1, consider the natural candidate mixed bound

    sup_{||b||₂=1} Σ_u |Σ_{NI≤B/2} b_I χ_I(u)|² |Q(u)|^(2k)
       ≪ B^(1+ε) P^(kσ),                                    (1)

where the slot Q(u)=Σ_{p} a_p χ_p(u) has |a_p|≤P^(−1/2) and bounded squared coefficient mass. The implied constant may depend on k,w,σ,ε but is uniform over admissible row-independent coefficients and growing B.

This bound fails for all ε<kw(1−σ). Choose a good prime element u₀ in the row interval, with Nu₀>2P. Such elements exist for arbitrarily large B, by the prime-ideal theorem and a fixed primary-generator convention. Set

    a_p = P^(−1/2) overline(χ_p(u₀))

for good prime ideals p in [P,2P]. These coefficients are fixed for the entire row sum; they do not depend on the running row u. Their squared mass is O(1/log P), and all slot values at u₀ are 1 after alignment. The prime-ideal theorem yields

    |Q(u₀)|² ≫ P/(log P)².                                  (2)

For the dual source, let I run over the ≫B good integral ideals of norm ≤B/2. They are coprime to (u₀), because Nu₀>B/2. Assign b_I=overline(χ_I(u₀))/√N, with N the number of these ideals. Then ||b||₂=1 and

    |Σ_I b_I χ_I(u₀)|² = N ≫ B.                             (3)

The single row u₀ therefore contributes ≫ B P^k/(log P)^(2k) to the nonnegative sum in (1), violating (1) for ε<kw(1−σ). For σ<1, (2) also puts u₀ in the selected family |Q(u)|²≥P^σ for large B. The same construction works with arbitrary fixed k and can retain any prescribed finite ray class containing enough prime rows. All exact zeros are avoided by the norm separation.

The point is that Markov's inequality weights the row u₀ by the *full excess* |Q(u₀)|^(2k)/P^(kσ). The selected operator itself includes u₀ only once, and a single row of this matrix has squared norm O(B), so this example does not contradict an O(B) selected bound. A proof must therefore control high-amplitude layers separately, or use a saturated weight such as

    min(1, |Q(u)|²/P^σ),

whose value is one on all selected rows. The saturated weighted operator bound would imply the selected operator bound but is not established here; unlike a nonnegative integer moment, its expansion involves cancellation or genuinely nonlinear estimates. A physical prime slot whose coefficients are a fixed smooth profile and a fixed finite-ray twist cannot be chosen to track u₀ in this manner; the example gives no obstruction there without a separate construction.

## Even an all-row saturated-weight estimate fails for small slots

The following further obstruction uses Xu–Sang's claimed sharp squarefree sextic large-sieve lower bound, Theorem 1.1 of [arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2), whose proof uses its cited zero-slot input. Assume its kernel and good-primary normalization, and assume the source interface allows arbitrary row-independent coefficients obeying the prime support and pointwise bound above. Fix σ>0 and 0<w<min(1,1/(6σ)); set P=B^w. Then there are admissible prime-slot coefficients and unit dual coefficients for which

    Σ_{Nu≤B, u squarefree} min(1, |Q(u)|²/P^σ) |T_b(u)|²
        ≫ B^(7/6−wσ−ε)/log B                              (4)

for any fixed ε>0, with the implied constant depending on ε and the fixed data. Thus an all-row saturated operator bound O(B^(1+ε₀)) is false when ε₀>0 is sufficiently small. This includes arbitrarily short fixed positive widths w. The same conclusion holds after choosing one of finitely many primary ray classes, with a constant loss; row and column coprimality masks are retained throughout. It does not establish a lower bound for the operator restricted to rows with |Q|²≥P^σ.

To prove (4), let each slot coefficient independently be `a_p=ξ_p/√P`, where ξ_p is uniform on the unit circle, and put `Q(u)=Σ_p a_p χ_p(u)`. These random coefficients are row-independent and obey the bound and mass condition for every choice of phases. A row with Nu≤B has at most log B/log P=1/w prime-ideal divisors in the annulus, counting distinct factors, while the annulus contains ≫P/log P good prime ideals. Therefore, uniformly in u,

    v_u := E|Q(u)|² = P^(−1) #{p in [P,2P]: p∤u} ≫ 1/log P.

Independence and |χ_p(u)|≤1 give E|Q(u)|⁴≤2v_u². Paley–Zygmund implies `Pr(|Q(u)|²≥v_u/2)≥1/8`. Since `v_u≪1`, for all sufficiently large B,

    E min(1, |Q(u)|²/P^σ) ≫ P^(−σ)/log P                 (5)

uniformly over rows, including their coprimality masks.

The claimed Xu–Sang lower bound gives a unit dual vector b supported on good squarefree ideals of norm ≤B such that `Σ_{Nu≤B}|T_b(u)|² ≫ B^(7/6−ε)`, after renaming its arbitrary loss. Insert (5) and average over the slot phases; some fixed phase choice has the lower bound (4). Partitioning the row set into finitely many required ray classes preserves one class with a fixed fraction of the energy. If a physical argument requires a dyadic row interval, partition the cutoff into O(log B) intervals and keep a maximizing interval; the source scale B remains the dual cutoff. This selects some dyad Q≤B, not necessarily Q comparable with B. Given any fixed δ>0, applying the stated de Faveri upper bound to rows of norm ≤B^(1−δ) shows that these rows contribute only O(B^(7/6−δ/3+ε)+B^(1+ε)); using a smaller loss in the lower bound removes them. Thus one may arrange Q≥B^(1−δ)/2, but this does not establish Q≍B. □

This explains why the saturated weight proposed above is only a formal sufficient condition and cannot be a uniform all-row estimate in the broad prime-slot class: the many unselected rows retain a small weight, and an unrestricted sextic large-sieve extremizer can amplify their aggregate beyond B. A viable argument needs more selective localization than the linear tail `|Q|²/P^σ`, and it must separately handle the rare high spikes from the previous section. The argument does not transfer to a fixed smooth profile merely by averaging over arbitrary phases.

More generally, for every fixed k>0 the same proof applies to `W_k(u)=min(1,(|Q(u)|²/P^σ)^k)`, giving a lower bound `≫ B^(7/6−kwσ−ε)/(log B)^k` for some allowed slot. Hence a bound `Σ W_k|T_b|²≪B^(1+ε₀)` is impossible for a sufficiently small loss whenever `kwσ<1/6`. If k may depend on a stipulated positive lower bound for w, taking k larger can avoid this particular obstruction; the counterexample does not rule out such a higher-order saturation.

**Independent review:** A second researcher checked the one-row and random-phase constructions, the source's coefficient-mass and mask conventions, the Xu–Sang kernel match, and the finite ray and dyadic partitions. Both arguments remain subject to the stated scope and, for (4), to the cited lower-bound theorem and its inputs.

## A conditional smooth-profile version with varying frequency

The preceding saturated-weight obstruction can also be obtained for two *fixed smooth* prime profiles, using frequency variation instead of independent prime phases. It remains conditional on Xu–Sang's sharp lower bound, and on having the indicated finite ray twist and frequency range in the intended application. In particular, it does not establish the selected-only bound false.

Fix τ>0, σ>0, and `0<w<min(τ/2,1/(6σ))`. Let `P=B^w`, `T=B^τ`. Choose a fixed nonzero nonnegative `V∈C_c^∞((1,2))`. There is a fixed quadratic finite-ray Hecke character η such that, with ν₀=1 and ν₁=η, the slot

    Q_{j,t}(u)=P^(−1/2) Σ_{p good} ν_j(p) χ_p(u)
                         V(Np/P) (Np/P)^(it)               (6)

has the following property: for every sufficiently large B, some j∈{0,1}, t∈[0,T], and unit dual vector b satisfy

    Σ_{Nu≤B, u squarefree} min(1, |Q_{j,t}(u)|²/P^σ) |T_b(u)|²
        ≫ B^(7/6−wσ−ε)/log B.                              (7)

The twist η, the smooth profile and σ,w,τ are fixed independently of B; t and b may vary with B. One of the two fixed twists works for an unbounded sequence of B by pigeonhole. The dual sources and rows have the same good-primary restrictions as Xu–Sang. Fixed ray-class and dyadic restrictions can be treated as above.

**Proof.** Take a rational prime ℓ≡1 (mod 12), split as `(ℓ)=𝔮 𝔮̄` in O. The quadratic character modulo 𝔮 is trivial on the six units: −1 is a square modulo ℓ and ω has odd order. Because O has class number one, it therefore defines a finite-ray Hecke character η on ideals prime to 𝔮, by evaluating any generator modulo 𝔮. Enlarge the fixed excluded set S to include both primes above ℓ, so both twists have conductors supported on S; use the same enlarged S in the cited large-sieve theorem. Its value on a rational prime r≠ℓ is the Legendre symbol `(r/ℓ)`. By the prime number theorem in fixed arithmetic progressions, a positive proportion of rational primes r split in K and satisfy `(r/ℓ)=−1`; the same holds in every fixed subinterval of `[P,2P]` after scaling. Their two prime ideals p,p̄ have norm r and obey `η(p)=−η(p̄)`.

Group (6) by the integer norm n, writing `Q_{j,t}(u)=Σ_n A_{j,u}(n)(n/P)^(it)`. Prime-ideal norms are rational primes or their squares, and at most two distinct prime ideals have any fixed norm. Choose a fixed subinterval where V is bounded below. If r in that interval is one of the primes above and neither p nor p̄ divides u, both χ values have modulus one, so the parallelogram identity gives

    |A_{0,u}(r)|² + |A_{1,u}(r)|² = 4 V(r/P)²/P.

At most `log B/log P=1/w` rational primes r≥P divide Nu≤B. Thus, uniformly over all rows,

    v_{0,u}+v_{1,u} ≫ 1/log P,    v_{j,u}:=Σ_n |A_{j,u}(n)|² ≪ 1/log P.

The standard mean-value theorem for Dirichlet polynomials, applied first to Q and then to Q², gives uniformly in u

    E_{j,t}|Q_{j,t}(u)|² ≫ 1/log P,
    E_{j,t}|Q_{j,t}(u)|⁴ ≪ 1/(log P)²,

where j is uniform on {0,1}, t is uniform on [0,T], and the conditions `T/P→∞` and `T/P²→∞` follow from `2w<τ`. For the fourth moment, each integer n has O(1) ordered factorizations as the product of two prime or prime-square norms; Cauchy–Schwarz consequently bounds the squared coefficient mass of Q² by O(v²). Paley–Zygmund now yields

    E_{j,t} min(1, |Q_{j,t}(u)|²/P^σ) ≫ P^(−σ)/log P

uniformly in u. Average this inequality against the squared row values of a unit dual vector provided by Xu–Sang's lower bound. Some fixed j,t then give (7). □

This argument uses a particular pair of twists and a positive-power frequency range. If an actual physical source does not allow the enlarged fixed ramification set, allows only a single specified twist, has a much shorter frequency range, or chooses its frequency allowance after a positive lower slot width in a way incompatible with `w<τ/2`, its applicability requires a separate check.

**Independent review of the smooth-profile version:** A second researcher checked the fixed ray character, arithmetic-progression density, second and fourth mean values, bounded norm-product multiplicities and Paley–Zygmund step. The dyadic partition gives some Q≤B, with the source cutoff still B; it does not establish the same result with both row and source scales replaced by Q. The physical-source height and ramification matching remain open.

The same pair of profiles and the same second/fourth moment calculation give, for every fixed k>0, the lower bound `≫B^(7/6−kwσ−ε)/(log B)^k` with `W_k=min(1,(|Q|²/P^σ)^k)`. It suffices that `w<min(τ/2,1/(6kσ))`. In particular, a single fixed saturation power k cannot provide a uniform O(B^(1+ε₀)) all-row estimate as positive widths approach zero, under the stated frequency and twist allowances.

**PR94 physical-source matching:** A source trace found that `canonicalPrimeAmplitude F.modulus ⊤` uses the conjugate ideal-row kernel, a norm window and phase, and the mask `identityClass M ⊤`; it does not expose an arbitrary η twist. In `source_packet_amplitude_class` the contour frequency is bounded by a later height with a polynomial cost whose degree depends on the already chosen slot data D. Therefore neither the availability of η nor `w<τ/2` follows from that interface; the dyadic row scale Q may also be smaller than the dual cutoff B. Consequently (7) is not a counterexample to the PR94 physical interface.

## Removing the twist by moving to sixth-power-free rows

There is a useful variant for a row family that permits sixth-power-free rows, including a fixed cubed prime factor. Keep a fixed ℓ≡1 (mod 12), choose a prime element ξ with norm ℓ, and now define

    η'(I) = χ_I(ξ³)

for ideals I coprime to the fixed primes over 6ℓ. This is a row-independent quadratic character on good ideals. For a rational prime r split as `r=p p̄`,

    η'(p) η'(p̄) = χ_{(r)}(ξ³) = (ℓ/r).

The last equality follows by multiplying the two quadratic residue symbols of ξ in the residue fields and taking the norm `Nξ=ℓ`. For r≡1 (mod 3), quadratic reciprocity and ℓ≡1 (mod 4) give `(ℓ/r)=(r/ℓ)`, so a positive proportion of split r have opposite η' values on p and p̄. The smooth-profile proof works with η' in place of η.

To remove the twist in the j=1 alternative, take the Xu–Sang squarefree rows u and columns I to be coprime to ξ, as allowed by its fixed excluded set. Replace each row by `u'=ξ³u` and each dual coefficient by `b'_I=b_I / χ_I(ξ³)`. Multiplicativity with the original zero masks gives

    Q_{0,t}(u') = Q_{1,t}(u),     T_{b'}(u') = T_b(u),

and `||b'||₂=||b||₂`. Since ξ∤u, each u' is sixth-power-free, although it is not squarefree, and `Nu'≤ℓ³B`. Increasing the *allowed* row and source cutoffs to `ℓ³B` changes the target O(B^(1+ε)) only by a fixed constant. The j=0 case already uses the original squarefree rows. Consequently the all-row capped-weight failure (7), and its fixed-k generalization, can be realized with the untwisted fixed smooth prime profile (6) on a sixth-power-free row family.

This removes the need to include η' as an allowed slot twist, but it does **not** establish a PR94 physical counterexample: the family must permit the fixed factor ξ³ and the source ideals must permit the imposed coprimality restrictions, the allowed polynomial height must still dominate P², and the dyadic row/source-scale relation remains as above. Enlarging the excluded set in the Xu–Sang *input* only restricts its rows and sources; it does not by itself require excluding ξ from the final row family.

**Independent review of the row transport:** A second researcher checked the quadratic norm identity, positive-density progression, exact coefficient adjustment and sixth-power-free factorization. The fixed prime ξ is excluded in the auxiliary Xu–Sang input but need not be excluded from the final rows. For any fixed δ<1/2 the retained dyad can be chosen Q≥B^(1−δ)/2, so its original source cutoff B lies in the range B≲Q²; the exact balanced case Q≍B remains unproved.

The PR94 `FullWCellBound` additionally imposes detector-maximum zero-location conditions on its rows. The Xu–Sang extremal rows here are not shown to meet those conditions; this is another reason the example does not contradict a physical cell estimate.

A further source trace finds that `identityClass M ⊤` removes only ideals not coprime to M. For fixed M, this is a finite prime deletion and is harmless in the displayed mean-value argument. The final physical bad set must omit ξ: `FullWCellBound` requires its calibration residue to be nonzero, while the transported row is divisible by ξ. The auxiliary large-sieve input may still exclude ξ. Establishing that all other physical row conditions hold remains separate, including the detector-maximum conditions already noted.

For the nonprincipal row check, the tracker lemma `PrimeRows/PrincipalMask.lean::calibrated_row_nonprincipal` states exactly that a `FreeRow` different from 1 with nonzero physical calibration residue has nonprincipal `rowCharacter` residue. Thus, if the auxiliary rows avoid F.S and ξ∉F.S, the ξ³-transformed rows satisfy this particular condition; this does not supply their detector-maximum zero windows or frequency budget.

The physical slot's conjugated sextic kernel is handled by conjugating the sum and reversing t; η' is real. Its fixed real exponent `Re z=17/50` changes the profile by the fixed factor `y^(−33/50)`, preserving smoothness and nonnegativity on the compact support. Neither observation resolves the frequency-order or detector-bin gaps.
