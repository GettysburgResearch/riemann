# Conditioning all five prime-power Gauss modes

**Status:** Proposed source-qualified extension of [the full-Gram bound](full-gram.md), audited by Families. It uses fixed-field Hecke Poisson, finite-ray reciprocity, the effective-order sextic/cubic large sieves and the quadratic Hecke large sieve. It controls a concrete profile span, not its complement or a zero-free region. The source inputs and powered-character normalization are not formalized here.

For each good prime ideal p and `e∈{1,2,3,4,5}`, use the source profile `v_(P,p^e)` with its original zero at p|s, and choose one primary generator per ideal. For any fixed δ>0 and `H≤P^(1/2−δ)`, the individually normalized Gram matrix of **all** labels `p^e` with `Np≤H` satisfies

    ||G−I|| ≪_(δ,ε) P^(−δ/2+ε).                                (1)

Although `N(p^e)` can be H⁵, its radical is p. This is a prime-power-family extension, not the same as a bound for arbitrary sixth-free h with radical ≤H.

## Proof

The [full-Gram argument](full-gram.md) applies the squarefree source decomposition `s=v²t` with `T=P^(1/2−δ/2)/H`. On small squares, the quotient of two distinct labels `p^e,q^f` is nonprincipal: if p≠q one good local exponent is nonzero modulo 6; if p=q then `e−f∈{±1,…,±4}` is nonzero modulo 6. Its primitive conductor Q and additional deleted radical E satisfy `QE≪Np Nq≤H²`; fixed S/ray factors only change the constant. The same Poisson/functional-equation estimate makes the small-square off-diagonal operator arbitrarily power-small.

For large v, partition the coefficient vector by the five values of e and use Cauchy across these five blocks. In each block all labels have underlying prime norm ≤H, and the row-dependent factor χ_(v²)(p)^e is a common diagonal coefficient multiplier. Powers e=1,5 give order-six characters; e=2,4 give order-three characters through the compatible fixed-ray residue normalization. Apply the corresponding unrestricted-row sixth/cubic large sieve. For e=3, apply the Goldmakher–Louvel quadratic Hecke large sieve after decomposing t=t₀a²; its unrestricted-row bound is

    X + H sqrt(X)                                               (2)

up to arbitrarily small powers. Thus, at `X=P/(Nv)²`, the e=3 block sums over `T<Nv≪sqrt P` to `≪(PH)^ε[P/T+H sqrt(P) log P]`. The sixth and cubic blocks satisfy the tails already checked in [full-gram](full-gram.md). Dividing by P, retaining the exact diagonal subtraction and normalizing by the deleted-prime densities proves (1). All finite ray partitions and bounded bad-prime factors cost only fixed constants or small powers. □

## A mixed span with improved Möbius projection

Let `H₀=P^(25/72−δ₀)` and `H₁=P^(25/54−δ₁)`, where δ₀,δ₁>0 and `H₀≤H₁`. Take all five powers `p^e` with `Np≤H₀`, and additionally `p⁵` with `H₀<Np≤H₁`. Both cutoffs are below `P^(1/2−η)` for fixed positive η, so the complete mixed Gram is conditioned by (1).

For all five small-scale powers, the [individual moving-reflection bound](../2026-10-29-gauss-profile-low-rank/moving-twist-overlap.md) gives total squared Möbius overlap `≪P^(−1+ε)H₀²`. For p⁵ at the larger scale, the [inverse-oriented theta average](../2026-10-29-cubic-theta-overlap-average/README.md) gives `≪P^(−1+ε)(H₁+H₁^(3/2))`; this is exactly the source's orientation because its average is indexed by h=p and the profile is v_(p⁵). The conditioned Gram transfers the sum to the projection onto the **whole** mixed span. With `P=Y^(6/5)` and the unrestricted source operator squared norm `≪Y^(41/30+ε)`, its projected source energy is

    ≪ Y^[1−min(12δ₀/5,9δ₁/5)+ε] (1+|t|)^A.                  (3)

The height order A must be included in the common source budget. This span contains a positive-power number of explicit prime-power modes beyond the previous full conditioning range. It still leaves all other modes and the orthogonal complement uncontrolled and therefore does not establish the `61/72` inverse moment target.

**Independent review:** Families checked the powered-character, small-square and large-square cases under the cited fixed-order and quadratic Hecke sieve inputs. A second independent audit is pending.

## Combined full-norm and prime-power frame

Let `H₀≤H₂≤P^(1/2−η)` and form the union of (i) every good sixth-free ideal h with `Nh≤H₂` and (ii) every prime power `p^e`, `Np≤H₀`, `1≤e≤5`, removing duplicate ideals and choosing one generator per ideal. Use the inverse-oriented profiles throughout. This entire union also has Gram matrix `I+O(P^(−η/2+ε))`. Indeed every label has radical norm ≤H₂, so the small-square conductor/deletion argument above remains valid for every pair, including a full-norm label against a prime power. For large squares, partition an arbitrary coefficient vector into the full-norm sixth-free block and five prime-power exponent blocks; Cauchy costs only a fixed factor six, and each source scale is at most H₂. Apply the sixth/cubic/quadratic unrestricted-row sieves as above.

Taking `H₂=P^(25/54−δ₂)` and `H₀=P^(25/72−δ₀)` with `H₀≤H₂`, the full-norm block's theta-averaged squared overlap is `≪P^(−1+ε)H₂^(3/2)` and the added prime-power block's individual-reflection contribution is `≪P^(−1+ε)H₀²`. Hence at `P=Y^(6/5)` the projection of the Möbius vector onto the **entire deduplicated union** has source energy

    ≪ Y^[1−min(9δ₂/5,12δ₀/5)+ε] (1+|t|)^A.                  (4)

This contains all good sixth-free profiles of full norm up to H₂ and all five prime-power profiles of prime norm up to H₀. It still does not bound the complement or any cross term in the full inverse moment.

**Combined-frame independent review:** Families checked distinct ideals, unit choice, mixed conductor/mask inequality, all six large-sieve blocks and both overlap exponents. The cited source estimates remain assumptions.

## Two averaged prime-power modes

The larger theta-average cutoff also applies to the original `p²` profiles. Their overlap contains `χ_s(p)^4`. In the October 5 source's notation

    Ψ_k(n)=ξ(n)χ_n(k)χ_n(f)^4,

choose `k=1`, `f=p`. Proposition `prop:R` with row range ℋ=1 (or a fixed constant ≥1) gives uniformly in each good prime p

    |T(X;1,p)|² ≪_ε (XP)^ε [1+Np/X].

Summing over `Np≤H` gives `≪(XP)^ε[H+H²/X]`. The exact cube inverse has the factor `Ψ_1(d)^3=ξ(d)^3χ_d(p)^{12}`; since the last factor is the original `1_(d,p)=1` zero mask, its modulus is ≤1. The same short-cube Cauchy bound and uniform `T(X;1,p)≪X^(1/2+ε)` tail used in the [theta-overlap proof](../2026-10-29-cubic-theta-overlap-average/README.md), with `C³=P/sqrt H`, yield

    Σ_(Np≤H)|⟨m_P,v_(P,p²)⟩|²
       ≪_ε (PH)^ε P^(−1)[H+H^(3/2)](1+|t|)^A.           (5)

Thus in the combined frame above, both original `p²` and `p⁵` profiles may be retained through the larger `H₂=P^(25/54−δ₂)` cutoff, while `p`, `p³` and `p⁴` use the smaller `H₀=P^(25/72−δ₀)` cutoff. The full-norm sixth-free block remains unchanged. Deduplicate coinciding ideals; the resulting Gram is conditioned and the energy bound (4) remains valid, with only fixed changes to the constant. These are still explicit subspaces; no control of the full complement follows.

**Independent p² review:** Families and High_match checked the k=1, f=p source specialization, moving-f uniformity, χ_d(p)¹² zero mask, cube-tail argument and projection scope, conditional on the stated October 5 theorem.

## The quadratic prime mode via paper 5 Theorem 6

The original `p³` profile admits a stronger row-scale average than (5). Paper 5 v3 Theorem 6 (12.2) includes its squarefree core and allows any fixed nonzero angular order. At angular order −1 its coefficient is `overline(α(n))γ₂(n)ξ(n)`, exactly the Möbius/Gauss coefficient up to a fixed finite-ray phase. Its row twist is `χ_p(n)^3`; sextic reciprocity in finitely many fixed ray sectors changes this to `χ_n(p)^3`, with the original zeros at p|n on both sides. Restricting its squarefree rows to primes p and summing dyadic row scales gives, subject to the stated theorem,

    Σ_(Np≤H)|⟨m_P,v_(P,p³)⟩|² ≪_ε P^(−1)H(PH)^ε(1+|t|)^A.

This is the same row-scale saving as the original p⁵ profile. Let `H_max=P^(1/2−δ)`, `H₂=P^(25/54−δ₂)` and `H₀=P^(25/72−δ₀)`, with `H₀≤H₂≤H_max`. Using the union conditioning proved above, retain all sixth-free inverse-oriented profiles of full norm ≤H_max, original p³ and p⁵ profiles for `Np≤H_max`, original p² profiles for `Np≤H₂`, and original p and p⁴ profiles for `Np≤H₀`, deduplicating actual profile ideals. The whole union is conditioned and its projected source energy at `P=Y^(6/5)` is

    ≪ Y^[max(23/30−6δ/5, 1−9δ₂/5, 1−12δ₀/5)+ε]
        ·(1+|t|)^A.

The underlying paper 5 row mean, quadratic-theta mean and Oct5 completed-theta mean are imported source results. Families and High_match independently checked the p³ coefficient/orientation, finite-ray reciprocity and normalization. This enlarged explicit span still leaves the full orthogonal complement and its cross term open.
