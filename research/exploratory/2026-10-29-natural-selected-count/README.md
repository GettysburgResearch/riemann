# A partial selected-row count from the sextic large sieve

**Status:** Proposed proof conditional on De Faveri's [preprint, Theorem 1.1](https://arxiv.org/abs/2610.04045v1), and on matching its primary sextic family to the source's `idealRowHom`. It does not prove the PR93 selected-operator conjecture or a zero-free region. An independent audit is requested. The argument applies to the broad arbitrary-ideal slot interface, including non-squarefree slot ideals. No novelty claim is made.

For fixed `A>0`, loss `ε>0` and slope `1/6<σ≤1`, a sufficiently small early mesh gives the following consequence. For every fixed slot count `N`, slot coefficient-mass bound `Cslot` and positive total-width lower bound `smin`, every finite family `cores` of sixth-power-free Eisenstein element rows with `rowNorm(u)≤Y≤Z^A`, satisfying the aggregate selection hypothesis

    ∏_i |Q_i(u)|² ≥ Z^(σ Σ_i w_i)  for every u∈cores,

obeys

    #cores ≪ Z^ε Y^(7/6−σ).                              (1)

Here `1≤Y`, and the implied constant and threshold may depend on `N,Cslot,smin`, as well as the fixed field and source data. The mesh can be chosen before `N,Cslot,smin`, consistently with the source quantifier order. For the specific target `σ=223/500`, this is exponent `1081/1500 = 0.720666…`, weaker than the desired `1−σ=277/500=0.554` and weaker than the approximately 0.6094 existing detector count. It therefore does not settle the target, but provides a uniform power saving below total row count for every slope above 1/6 without assuming prime-only slots.

Each slot polynomial has row-independent coefficients and finite arbitrary nonzero ideal sources of norm at most `C Z^w`, with one fixed support constant C and squared coefficient mass at most `Cslot`; its kernel is `idealRowHom` with its original masks. The sum in (1) counts element rows. A sixth-power-free ideal has at most six generators in the Eisenstein ring, and bounded local bad-prime choices cost only a fixed factor. Ideal characters use the source zero masks. Sixth-power-free element rows can include the fixed bad primes; separate their bounded exponents and units into finitely many row classes, with column-dependent phases, as in the [collapsed-moment note](../2026-10-29-sextic-collapsed-moment/README.md).

## An unrestricted-column sieve

Let `a_c` be any finite coefficients on good integral ideals with `Nc≪B`, and put `||a||₂²=Σ_c |a_c|²`. Summing over sixth-power-free element rows of norm at most Y, the sixth-order sieve yields

    Σ_u |Σ_c a_c χ_c(u)|²
      ≪ (YB)^ε [Y B^(1/6) + B + Y^(5/6)B^(1/3)
                 + Y^(1/3)B^(5/6)] ||a||₂².              (2)

To prove this, factor each good ideal uniquely as `c=w v^6` with w sixth-power-free. For fixed v, the sixth-power factor is the row mask `1_(u,v)=1`; remove this mask when estimating that v's nonnegative squared sum. Apply the sixth-power-free row-and-column sieve to coefficients `a_{wv^6}` with column cutoff `B/(Nv)^6`. Minkowski followed by Cauchy–Schwarz over v gives the sum of the sieve constants, multiplied by `Σ_{v,w}|a_{wv^6}|²`. Summing over `Nv≪B^(1/6)` gives the four displayed terms: use ideal counting for the first, and convergence of `Σ(Nv)^(-6)`, `Σ(Nv)^(-2)`, and `Σ(Nv)^(-5)` for the other three. The norm conventions and orientation are those verified in the collapsed-moment note. Fixed support constants and all six units are harmless. To include the source's ordinary ideals, split the finitely many bad-prime exponents off each column. At each fixed exponent vector their contribution is a row multiplier of modulus at most one, which can be dropped in the squared norm; the number of vectors is `O((log(2B))^|S|)`, absorbed in the arbitrarily small power. This also covers the source convention in which the local value is zero at the prime over 3.

## Selection and amplification

A slot of width `w` has squared coefficient mass at most `Cslot` and sources of norm `≪Z^w`. Ideal counting and Cauchy–Schwarz give the pointwise upper bound `|Q_i(u)|²≪Cslot Z^{w_i}`, with a fixed implied constant. Fix any `σ₀<σ` sufficiently close to σ. Let `W=Σ_i w_i≥smin`. For each selected row, at least one slot of width at least a fixed positive `η=η(N,smin,σ−σ₀)` satisfies

    |Q_i(u)|² ≥ Z^(σ₀ w_i).                               (3)

Indeed, otherwise every wider slot is below its threshold, while the total width of the remaining slots is at most `Nη`; choosing η small makes the product of pointwise upper bounds strictly less than `Z^(σW)` for all sufficiently large Z. The constants and threshold may depend on N and Cslot, as allowed by the source quantifiers. Assign each selected row to one such slot; summing over the fixed number N of choices suffices. N=0 has no admissible data when `smin>0`.

For each chosen slot take the integer `k=max(1,ceil(log Y/(w log Z)))`. Since `w≥η` and `Y≤Z^A`, k is bounded in terms of the fixed `A,η`. Expand `Q_i^k` into an ideal polynomial of length `B≪(C Z^w)^k`, collecting equal products. Multiplicativity, including zero masks, makes this equality exact. Its coefficient squared mass is `≪_{k,ε} Z^ε`: by Cauchy–Schwarz, each product coefficient costs at most the k-fold ideal divisor function, and the total squared mass of the uncollected k-tuples is at most `Cslot^k`. The divisor bound is uniform because k is now bounded.

Because `Y≤Z^(kw)≤Y Z^mesh`, the sieve (2) gives, for its rows,

    #selected · Z^(kwσ₀) ≪ Z^ε (Y Z^mesh)^(7/6),

where the factors `C^k` have been absorbed into the constant. Since `Z^(kw)≥Y`,

    #selected ≪ Z^(ε+(7/6)mesh) Y^(7/6−σ₀).

Finally choose `σ−σ₀` small in terms of A and the requested loss, and choose the early mesh small in terms of the requested loss only. Since `Y≤Z^A`, the difference between σ₀ and σ is absorbed in the allowed `Z^ε`. These choices precede N and smin, while the later η, bound on k, constant and threshold may depend on them. This proves (1), conditional on the input theorem and convention matching. □

The selected-operator norm with arbitrary dual source S and its sharp `L+Y^(1−σ)L^σ` shape requires additional estimates. The count above is only its unit-source component, with a weaker Y exponent.

## Limitation of the direct amplified long-source estimate

The same calculation also gives a precise diagnostic for the long-source seed. Suppose one slot of scale X satisfies `|Q(u)|²≥X^σ` on all selected rows. For an integer k fixed with the slot data, write `H=X^k`. Let S be any finite ordinary ideal source set of norms at most L, with any coefficients b of squared mass one. Expand `Q(u)^k Σ_{c∈S}b_c χ_c(u)` and collect equal products. The divisor bound gives squared coefficient mass `≪Z^ε` when `LH≤Z^{O(1)}`; collisions between slot primes and the dual source are retained. Applying (2) with `B≪LH` gives the concrete bound

    selectedNorm(cores,S) ≪ Z^ε H^(−σ) [Y(LH)^(1/6) + LH
       + Y^(5/6)(LH)^(1/3) + Y^(1/3)(LH)^(5/6)].         (4)

If the slot coefficients are supported only on primes, the same inequality remains valid, but it does not yet exploit that extra support. In the central long-source case L=Y, the last term in this bound equals `Y^(7/6) H^(5/6−σ)`. At `σ=223/500<5/6` this displayed term grows with H≥1, so this particular upper bound cannot certify the desired `Y^(1+ε)` seed merely by taking higher slot powers. This observation concerns the displayed estimate, not an impossibility result for stronger arithmetic arguments or refined use of the prime-slot support.

## A distinct-prime amplifier on physical spikes

For one physical prime slot, suppose all primes have norm in a fixed annulus of scale P and `|a_p|≪P^(−1/2)`. Write `Q(u)=Σ_p a_p χ_p(u)` and fix a positive integer k. Let `D_k(u)` be the same k-fold expansion restricted to ordered tuples of pairwise distinct primes. Then uniformly on rows where `|Q(u)|≥P^g` for fixed `g>0`,

    D_k(u) = Q(u)^k [1+O_k(P^(−2g))].                    (5)

Indeed the power sums `E_j(u)=Σ_p(a_p χ_p(u))^j` satisfy `E_1=Q` and `|E_j|≪P^{1−j/2}≪1` for each j≥2. The elementary-symmetric/power-sum identities give `D_k=Q^k+O_k(|Q|^{k−2})` whenever |Q|≥1; the zero masks merely reduce the absolute values. Since the slot coefficients are row-independent, D_k is also an admissible row-independent coefficient vector on squarefree prime-product ideals. For k=1 the error is zero. If `P≥Z^η` with fixed η, (5) retains the full selected spike for all large Z.

This reduction, suggested by a separate researcher, removes repeated-prime artifacts from the slot amplifier. It does not by itself prove the long-source seed: the known sharp sextic sieve lower bound already uses squarefree row and column ideals. A new estimate would need to use the tensor-product structure of the coefficients, their correlation with the selected rows, or further physical information.
