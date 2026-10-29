# Off-diagonal reduction for the selected long-source seed

**Status:** A rigorous Gram-matrix reduction conditional on the selected-row bounds identified below. It does not prove the long-source seed, a return inequality, or a zero-free region. No priority claim is made.

Let F be any finite selected set of sixth-power-free Eisenstein element rows of norm at most Y, and S any finite set of nonzero source ideals of norm at most L. Put

    K(u,I)=idealRowHom(u,I),
    G(I,J)=Σ_{u∈F} overline(K(u,I)) K(u,J).

The source norm `selectedNorm(F,S)` is the largest eigenvalue of this positive semidefinite Gram matrix. The only fact used about the kernel for the general block bound below is `|K(u,I)|≤1`, including at bad primes and with all source zero masks.

Fix an integer d≥2. Factor each nonzero ideal uniquely as `I=I₀ A^d`, with I₀ d-th-power-free. Let `G_diag,d` keep entries G(I,J) whose d-th-power-free parts coincide and set every other entry to zero. This is block diagonal, and each block is a Gram matrix, hence positive semidefinite. Ideal counting gives at most `O(L^(1/d))` source ideals in each block: if the common skeleton is I₀, then `N(A)≤(L/N(I₀))^(1/d)`. Since every Gram entry has modulus at most #F, each block has operator norm at most `#F` times its size. Consequently

    0 ≤ ||G_diag,d|| ≤ C_d (#F) L^(1/d).                 (1)

Suppose `#F≪Z^ε Y^α`, `1≤Y≤L`, and `α≤1−1/d`. Then

    ||G_diag,d|| ≪ Z^ε L.                                (2)

The elementary bound holds for *arbitrary* ideal sources, source masks, ray classes, and row-dependent restrictions within F; it does not require the source ideals themselves to be d-th powers. The matrix of all remaining terms `G_off,d=G−G_diag,d` is Hermitian but need not be positive. To prove the central long-source seed `selectedNorm(F,S)≪Z^ε L`, it is therefore enough to prove the one-sided off-block quadratic-form estimate

    Σ_{I,J∈S, I₀≠J₀} b_I overline(b_J) G(I,J)
       ≪ Z^ε L Σ_I |b_I|²                                (3)

for all coefficient vectors b, with the same quantifiers as the physical slot system. Conjugating the coefficients if desired accounts for Gram convention. This formulation isolates precisely the part not controlled by row count and source-fiber size; it is not asserted that (3) follows from the general sextic large sieve.

## Two applicable thresholds

1. For the broad arbitrary-ideal slot interface, the conditional de Faveri argument in [the selected-count note](../2026-10-29-natural-selected-count/README.md) gives `α=7/6−σ`, up to an arbitrarily small loss. Thus every **sixth-power** block contribution satisfies (2) for every fixed `σ>1/3`. At `σ=223/500`, `α+1/6=4/3−σ=1331/1500=0.887333…`; at L=Y the diagonal blocks are bounded by `Z^ε Y^0.887334`. This removes the entire equal-sixth-power-skeleton part, including masks, even though the slots themselves may use arbitrary ordinary ideals.

2. For fixed smooth prime slots with fixed finite-ray twists and the explicit physical assumptions of [the smooth-prime note](../2026-10-29-smooth-prime-selected-count/README.md), the conditional Xu–Sang row count gives `α=R((1+σ)/2)`. At σ=223/500, `α=0.6381045115…<2/3`, so every **cube-power** block contribution satisfies (2). At L=Y it is at most `Z^ε Y^(0.971437845…)`. This requires the stated smooth physical-slot matching; it does not cover arbitrary prime subsets, arbitrary coefficients, or general PR93 slot sources. A finite number of such slot tests can be unioned after a small exponent loss.

The existing PR94 bin count `α≈0.6093710568`, if imported with the correct physical-row and selected-subset matching, gives the stronger cube-block exponent `α+1/3≈0.9427043901` at L=Y. This uses the existing count and still leaves the off-block correlation.

For arbitrary source coefficients or the physical case alike, d=2 would require a count exponent at most 1/2 from this argument alone; none of these counts supplies it. The difference between sixth-power and cube-power blocks is simply the size of their source fibers; the argument does not assume that a cubic power evaluates trivially under a sextic character.

## Exact sextic off-block form for good ideals

If I,J are coprime to the fixed primes above 6, then on each row the zero-extended sextic character obeys

    overline(K(u,I)) K(u,J) = K(u, I^5 J).

At a common nonunit both sides are zero, and elsewhere conjugation is the fifth power. Furthermore I and J have the same sixth-power-free skeleton exactly when `I^5 J` is a sixth-power ideal. Thus the d=6 off-block term in (3) is exactly the weighted correlation over pairs for which `I^5 J` is not a sixth power. The row sum must retain its original zero mask. Arbitrary sources with bad-prime factors may first be split into the logarithmically many possible bad-prime exponent vectors, at a `Z^ε` loss under the source's fixed polynomial cap `L≤Z^P` (with constants depending on P and the fixed bad set); the general block estimate (1) itself needs no such splitting.

The obvious strategy of expanding a selected prime spike and applying the unrestricted sextic large sieve to the collapsed tensor has at L=Y a term `Y^(7/6) H^(5/6−σ)` for amplifier length H. At σ=223/500 that worsens as H grows. The [distinct-prime amplifier](../2026-10-29-squarefree-slot-amplifier/README.md) removes repeated-prime terms while retaining a spike, but the general sieve remains sharp even on squarefree indices. An improvement requires a mixed estimate for the selected rows and tensor coefficients, or further physical structure, rather than the unrestricted norm alone.

**Independent review:** A second researcher checked positivity and operator norms of the skeleton blocks, the exponents, and the exact sixth-power criterion and zero masks. The complementary off-block estimate remains open.

## Overshoot obstruction and a clipped mixed target

A tempting approach is to bound a full positive mixed moment with the actual distinct-prime amplifier D_k, writing `H=P^k`:

    Σ_{Nu≤Y} |D_k(u)|² |Σ_{I∈S} b_I K(u,I)|²
       ≪ Z^ε L H^σ Σ_I |b_I|².                         (4)

This estimate is **false** when σ<1, even for fixed smooth untwisted prime weights and good ordinary sources. Take the row u=1, a fixed nonnegative smooth prime window `Q(1)≈P^(1/2)/log P`, and use all good ideals of norm ≤Y as dual sources, each with coefficient `(#S)^(−1/2)`. The unit row has `K(1,I)=1`; ideal and prime counts give

    |Σ_I b_I K(1,I)|² ≫ Y,
    |D_k(1)|² ≫ P^k/(log P)^(2k) = H/(log P)^(2k).

Choosing Y=Z and P=Z^w with fixed positive w makes this one row alone contradict (4) at L=Y for sufficiently small fixed loss ε. Requiring row norms in a dyad `[Y,2Y]` removes this particular unit-row counterexample, but arbitrary bounded prime coefficients still defeat (4): choose a good prime row u₀ in the dyad and phases `a_p=P^(−1/2) overline(K(u₀,p))`, on a prime window with P≪Y; choose normalized source coefficients aligned with `K(u₀,I)` over good I of norm at most Y/2. The prime row cannot divide those sources, so the same `≫YH/(log P)^(2k)` lower bound holds. Coefficients are row-independent once chosen, but the slot phases were tailored to u₀. This dyadic construction does not refute a hypothesis restricted to fixed smooth finite-twist prime weights.

These examples **do not disprove the selected operator bound**: the single-row matrix has squared norm only O(L). They show why paying for an untruncated spike can be too expensive even when it is legitimate to select that row. This construction was identified by an independent researcher; the unit-row variant also exposes why a full-row formula needs a dyadic or principal-row restriction.

A logically sufficient positive target is instead the **clipped** estimate

    Σ_{Nu≤Y} min(|D_k(u)|²,H^σ)
       |Σ_{I∈S} b_I K(u,I)|²
       ≪ Z^ε L H^σ Σ_I |b_I|².                        (5)

Here `Y≤L≤Y²`, the physical prime slot uses its actual tensor coefficients, and the fixed source cap, finite twist, unit classes and zero masks must be retained. This is unproved; without quantitative information on the cutoff it can be as hard as the selected norm itself. On a physical spike `|Q(u)|²≥P^σ`, the distinct-prime identity gives `|D_k(u)|²≥(1−o(1))H^σ`; after a fixed negligible threshold loss the clipped weight is comparable to H^σ. Hence (5) implies the desired selected norm. For aggregate selection, use the positive-width pigeonhole in the selected-count note at a slightly smaller slope σ₀<σ, subject to matching the physical slot conditions.

The general de Faveri sieve applied after collapsing the tensor gives only the bound in (4) of the selected-count note. At L=Y its worst displayed term is `Y^(7/6) H^(5/6)` before division by spike height, whereas the false unclipped target would require `Y H^σ`. The count-and-Gram reduction above shows that only off-skeleton interactions require new work for the selected operator itself; one must also control overshooting rather than inserting the untruncated amplifier weight into a positive moment.

## The full-row clipped target also fails for arbitrary prime phases

The clipped estimate (5), when quantified over arbitrary bounded row-independent prime coefficients, is false in part of its proposed range. Fix σ>0, a positive integer k, and a width w>0 with `k w σ<1/6`; let `Y=Z`, `P=Y^w`, H=P^k, and L=Y. In the source quantifier order choose w after the early mesh is supplied, with w below that mesh, and then keep w fixed as Y grows. Take all good prime ideals p with `P≤Np≤2P` and independent random unit phases `a_p=P^(−1/2)e^{iθ_p}`. Let D_k be the ordered distinct-prime slot amplifier.

For every nonzero row of norm at most Y, at most `log Y/log P=1/w` such primes can divide the row. The prime ideal theorem therefore gives, uniformly in the row,

    E|D_k(u)|² ≫_k (log P)^(−k),
    E|D_k(u)|⁴ ≪_k (log P)^(−2k).

For k=1 these follow directly from phase orthogonality and `E|Q|⁴≤2(E|Q|²)²`; for fixed k they follow by expanding the independent phases and counting matching index multisets. Since `min(x,T)≥x−x²/T` for x,T≥0, the two moment estimates imply

    E min(|D_k(u)|²,H^σ) ≫_k (log P)^(−k)                 (6)

for large Y, uniformly in all these rows.

Xu–Sang's [Theorem 1.1](https://arxiv.org/html/2610.17675v2) supplies a deterministic coefficient vector of squared mass one, supported on good squarefree ideals of norm at most L=Y, with

    Σ_{Nu≤Y, u squarefree} |Σ_I b_I K(u,I)|² ≫_η Y^(7/6−η).

This includes the source matrix of the theorem after fixing the compatible primary family and good-prime exclusions. Multiply (6) by the nonnegative source energy for each row and average over the phases. Some fixed phase choice then gives a left side in (5) at least `≫Y^(7/6−η)(log P)^(−k)`. The proposed right side would be `O(Y^(1+k w σ+ε))`; choose η and ε with `η+ε<1/6−kwσ` to contradict it. The phases are fixed before the rows are summed and all coefficient magnitudes satisfy the physical normalization, but they need not be finite-ray twists or smooth deterministic phases.

This is a failure of a **full-row weighted moment**, not a counterexample to the selected norm: typical random-phase responses have squared size about `(log P)^(−1)`, far below the selecting threshold `P^σ`. In particular, the bad contribution in this proof comes from rows that need not be selected. It also does not exclude using larger k with `k w σ≥1/6`, or a structurally narrower smooth-twist slot class. The estimate demanded by selection must suppress the low-response bulk rather than merely clipping high responses.

In fact, this random-phase obstruction can be realized while **no row is selected**. For each row, Hoeffding's inequality applied separately to the real and imaginary parts gives `Pr(|Q(u)|²≥P^σ)≪exp(−cP^σ)`, uniformly, because the sum of squared coefficient magnitudes is O(1). A union bound over O(Y) element rows shows that the probability of any selected row is `≪Y exp(−cP^σ)`. The clipped mixed functional is at most `H^σ·O(Y²)` by the trivial row and source counts. Its contribution on that exponentially rare event is negligible compared with the above expected lower bound. Thus there is a deterministic phase choice with no selected rows and with the large clipped mixed moment. This quantifies why the clipped full-row estimate can fail while the selected operator is identically zero.

One possible quantitative localization is `W_j(u)=min(1,(|Q(u)|²/P^σ)^j)` for a fixed integer j. It equals one on every selected row and suppresses the random-phase bulk more strongly than simple clipping. The same random-phase argument obstructs a uniform all-row estimate `Σ W_j(u)|A_u|²≪Z^ε L` whenever `j w σ<1/6`: the moments of a Steinhaus prime sum give `E W_j(u)≫_j P^(−jσ)(log P)^(−j)` uniformly. Thus for σ=223/500 and P=Y^w, this approach needs at least `jw≥250/669≈0.37369` to evade that particular obstruction. Increasing j after the positive slot-width floor is fixed may reach that scale, but no estimate for W_j is proved here. Dropping the saturation to use an untruncated polynomial moment reintroduces the single-row overshoot obstruction.
