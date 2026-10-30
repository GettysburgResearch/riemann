# Collapsed inverse and prime slots, including overlaps

**Status:** A source-qualified common-orientation selected-moment estimate. It uses the unrestricted-row sextic large sieve and, for a second optional bound, Han Wu's Hecke subconvexity. It is not a new zero-free region or an independently verified detector input. All coefficients and profiles must be common across rows. The actual PR94 source-selection and norm normalizations still require a separate match.

Let Y be the row scale, `D=Y^r` the inverse scale and `P_j=Y^{z_j}` the scales of a fixed finite number J of prime slots; put `P=∏P_j=Y^z`, `z=Σz_j`, and `B=DP`. Use one fixed finite ray twist and the **same sextic orientation** for the squarefree Möbius inverse and every prime slot. The prime supports can overlap when J≤4, or J may be any fixed finite number if the supports are pairwise disjoint. Assume fixed smooth compact-annular profiles and normalized row-independent slot coefficients with `Σ_p|λ_{j,p}|²≪1`. Retain all fixed and row/source coprimality zero masks.

Multiplicativity gives

    M_D(g) ∏_j Q_j(g) = Σ_(Nc≪B) b_c χ_c(g).                (1)

The inverse index is squarefree. Each prime contributes at most once from it and at most J times from the slots; hence every source ideal c is sixth-free under the stated J/support alternatives. At overlap, do not omit the product: its local valuation is counted with its full multiplicity and its value is zero whenever the row shares that prime. The finite fixed ray twist and slot coefficients are absorbed into b_c. The number of factorizations of c into these fixed J+1 factors is bounded by a fixed divisor function. Cauchy and ideal counting give

    Σ_c|b_c|² ≪_ε B^ε,       Σ_c|b_c| ≪_ε B^(1/2+ε).          (2)

The first estimate uses the product of the slot ℓ² masses and the inverse coefficient mass `D^(−1) Σ_(Na≪D)1≪1`; the second is Cauchy and `#{Nc≪B}≪B`. The factorization constants may depend on fixed J and support ratios, not on Y or the chosen coefficients. Mixing a conjugated or differently powered slot with the inverse is not covered: overlapping local exponents can cancel modulo six while retaining a zero mask, so the identical-source principal diagonal need not capture every principal term.

For all good ideal rows `Ng≈Y`, the unrestricted-row sextic large sieve yields

    Σ_g |M_D(g)∏Q_j(g)|²
      ≪_ε (YB)^ε [Y+B Y^(1/6)+Y^(5/6)B^(1/3)
                          +Y^(1/3)B^(5/6)].                   (3)

Finite ray/unit classes can be split before the estimate, with fixed overhead. Alternatively, pair distinct c₁,c₂. Their local valuation differences lie in `[-5,5]`, so a nonzero difference cannot vanish mod 6: after fixed-sector normalization the quotient character is ramified at some good prime and nonprincipal. Its conductor and deleted-mask radical are `≪B²`. Smooth Hecke covariance and Wu's `103/512` conductor exponent, together with (2), give the second bound

    Σ_g V(Ng/Y)|M_D(g)∏Q_j(g)|²
       ≪_ε (YB)^ε [Y+Y^(1/2) B^(359/256)].                 (4)

The identical-c principal part is at most `YΣ|b_c|²`; all other pairs are bounded absolutely. For sixth-free rows the auxiliary Euler series is `L(s,ξ)/L(6s,ξ^6)`; for all good rows it is `L(s,ξ)`. Fixed-sector projection and moving common-prime masks add only the stated small powers. The two inequalities have different inputs; using one does not establish the other.

If F consists of rows where `|M_D|²≥D^δ` and each `|Q_j|²≥P_j^{σ_j}`, positivity and (3) imply

    #F ≪_ε Y^[E(r+z)−δr−Σ_j σ_j z_j+ε],                    (5)
    E(b)=max{1, b+1/6, 5/6+b/3, 1/3+5b/6}.

No constraint `r<min z_j` or `r≤1/2` is needed. The corresponding covariance alternative from (4) replaces E(b) by `max{1,1/2+(359/256)b}`. It is valid for arbitrarily large fixed J with disjoint supports, or J≤4 for overlapping supports, under the common-orientation convention.

## Comparison at the PR94 bottleneck

The source-style proxy is `σ_j=2δp_j`, `0≤p_j≤1/2`, so `σ_j≤δ`. At `δ=223/500`, `p_j=1/2`, the relaxed bound is minimized at `b=r+z=1`, since

    E(b)=1                 for b≤1/2;
         5/6+b/3           for 1/2≤b≤1;
         b+1/6             for b≥1.

The resulting count exponent is `7/6−223/500=1081/1500≈0.7206667`, larger than the existing count `≈0.6093711`. With optimistic total prime width `z=619/10000`, choose `r=9381/10000` to attain b=1; unlike the earlier separate-slot covariance proof, this does enter the source's long-inverse length `r≥3/5`. It is still far weaker at this limiting point. Actual PR94 slot class, zero witness, joint source quantifiers, smooth-profile matching and height costs have not been verified for (5), so this comparison is a scalar diagnostic, not a new admissible tracker branch.

The optional Wu bound (4) reaches O(Y) only for `b≤128/359≈0.356546`, whereas the sextic large sieve (3) reaches O(Y) through `b≤1/2`. Thus Wu's bound does not improve the unconditional main-term region for these sixth-free collapsed coefficients. Its relevance would require another structure not present in the absolute covariance calculation.

## Comparison with the unmarked long-inverse source

A stronger pointwise comparison rules this collapsed bound out as an improvement over the existing unmarked inverse witness at the bottleneck, under matched source normalizations. Take `δ=223/500`, total slot width `0≤z≤619/10000`, and a long inverse `r≥3/5`. For the best possible slot amplitudes `σ_j=δ`, the collapsed estimate gives count exponent

    C_coll = E(r+z)−δr−δz.

The cited unmarked inverse estimates give `C_old=1−δr` for r<1 and `C_old=(1+5r)/6−δr` for r≥1, with their original fixed-profile, sixth-free-row, source and small-loss hypotheses. If `3/5≤r≤1` and `r+z≤1`, then

    C_coll−C_old = (r−1/2)/3+(1/3−δ)z
                  ≥ 395389/15000000 ≈ 0.02635927.

If `r≤1<r+z`, the difference is `r−5/6+(1−δ)z>1/6−δz>0.139`. If `r≥1`, it is `r/6+(1−δ)z≥1/6`. Thus this **particular source-qualified count upper bound** is strictly worse even than the unmarked inverse-witness bound at the selected point, before invoking PR94's stronger joint count. This compares formulas under the assumed shared scales, witness threshold and slot-slope normalization; it does not establish those detector matches or preclude a different structured moment.

**Independent review:** High_match checked the earlier separate-slot covariance and its detector restriction. Families checked the collapsed factorization for disjoint supports, overlaps with J≤4, common orientation, masks and coefficient mass; the unrestricted-sieve formula and comparison above remain subject to the cited source hypotheses.

**Second independent review:** High_match checked the collapsed exponents under overlapping and disjoint supports, original masks, factorization multiplicity and coefficient masses, nonprincipal quotient, the two source bounds, and the exact three-case comparison with the unmarked long-inverse witness. The detector and common-orientation match remains open.
