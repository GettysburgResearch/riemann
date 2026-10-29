# Almost all squarefree Gauss-profile directions from a pair moment

**Status.** This is a source-qualified deduction, conditional on the general-order rectangular sieve and its approximate-functional-equation central-moment replay in [the conjugate-conductor note](../2026-10-29-conjugate-conductor-sieve/README.md), and on the cited theta row mean and sextic sieve. It is not a zero-free theorem. In particular, it does not control the remaining low-Gram directions or the complement of the profile span. The label restriction below is squarefree; the argument does not cover all sixth-free labels.

Fix a field K containing μ_n, the source's good ideal family and finitely many fixed reciprocity sectors. Let P,H≥2 with H≤P^C for fixed C. Let h range over good squarefree ideals Nh≤H in one fixed ray sector, and let s range over good squarefree ideals. Enlarge S once so that the conductors of all fixed ray twists are supported in S. Take a fixed smooth nonnegative row weight W supported in a compact subset of (0,∞), and define normalized columns

    u_h(s)= P^(−1/2) W(Ns/P)^(1/2) ξ_s(h) / D_h^(1/2),
    D_h= P^(−1) Σ_s μ²(s) W(Ns/P) 1_((s,h)=1).

Here ξ_s(h) denotes the relevant n-th order residue family with its original zero extension. A common unit-modulus Gauss factor in s may be inserted into every column, since it cancels in all inner products. Choose the sector with positive density and the source's fixed normalizations. Standard squarefree counting with deleted factors gives N:=#{h}≍H and D_h≳(HP)^(−ε), uniformly for H≤P^C; the normalization is defined for P sufficiently large. Write A for the matrix with columns u_h and G=A* A.

For every ε>0,

    ||G−I||_HS² ≪_{ε,K,n,W,C} H² P^(−1) (HP)^ε.                (1)

Thus at most O(H² P^(−1)(HP)^ε) eigenvalues of G lie outside [1/2,3/2]. In particular, if H≤P^(1−δ), all but o(H) eigenvalues lie in this interval after choosing ε sufficiently small. This gives a nearly full-dimensional **spectral image**; it does not bound the image of the remaining eigenvectors.

## Proof and uniformity

For h≠k write h=da, k=db with d,a,b pairwise coprime and squarefree, Na,Nb≤H/Nd. The original zero extensions give the exact identity

    ξ_s(h) overline(ξ_s(k))
       = 1_((s,d)=1) ξ_s(a) overline(ξ_s(b)).                (2)

After partitioning the finitely many ray sectors of a,b,s, reciprocity identifies the last factor with a fixed-sector Hecke character ξ·χ_(a b^(n−1))(s), times a phase constant in that sector. Sector indicators can be expanded into finitely many fixed ray characters ξ; they must be retained through the argument. Since a,b are coprime and a≠b, a good prime divides exactly one of them. Its nonzero ±1 local exponent gives nontrivial tame ramification, so χ_(a b^(n−1)) and each fixed-ray twist are nonprincipal. The conductor is ≪N(ab) with a fixed bad-prime factor.

Fix an arbitrarily small η>0. Expand μ²(s)=Σ_(v²|s) μ(v); because W is compactly supported, Nv≪P^(1/2). The v summand, with X=P/(Nv)², is a smooth Hecke character sum of scale X, multiplied by a factor of modulus at most one. Its common d-mask is opened by inclusion–exclusion over e|d. Shifting the Mellin line to Re z=1/2+η gives an absolute majorant for the square-sum over a,b of the shape

    P^(−1/2+η) (Nv)^(−1−2η) (Nd)^ε
      × ∫ (1+|t|)^(−B)
           [Σ_{Na,Nb≤H/Nd; μ²(ab)=1}
              |L(1/2+η+it, ξχ_(a b^(n−1)))|²]^(1/2) dt,  (3)

The factors ξχ_(a b^(n−1))(v²) and ξχ_(a b^(n−1))(e) vary with a,b; for each fixed v,e they have modulus at most one and are discarded only inside the ℓ² norm, not factored out as constants. Here B can be chosen arbitrarily large from the fixed profile. The factor (Nd)^ε absorbs the divisor sum Σ_(e|d)(Ne)^(−1/2−η) and the fixed deleted Euler factors, uniformly also at primes shared with ab or v; these factors retain the original zero masks. This formula is an L²-in-(a,b) bound, not a pointwise moment bound.

The central-moment proof in (6) of the linked note, replayed with 1/2+η+it, gives for fixed η and every ε>0

    Σ_{Na≤A,Nb≤B; μ²(ab)=1}
       |L(1/2+η+it, ξχ_(a b^(n−1)))|²
       ≪ (AB)^(1+ε)(1+|t|)^C₁.                             (4)

This extension is an explicit source-dependent input here: the AFE has length ≪(AB)^(1/2+ε)(1+|t|)^C₂, and the rectangular sieve is uniform in its coefficients; applying it to that longer length yields a fixed polynomial height cost. Fixed finite-ray twists and the finitely many sector expansions are included. The AFE and gamma-profile seminorms, and the cost of shifting from 1/2 to 1/2+η, must be uniform in the family; they are not independently proved by the present note. At fixed η the Mellin decay makes (3)'s integral convergent.

Apply the triangle inequality in the Hilbert space of off-diagonal pairs separately to v and d, pad each d-group to a,b≤H/Nd, and use (4). Since Σ_(Nv≪√P) (Nv)^(−1) ≪log P and Σ_d (Nd)^(−2+ε)≪1, the square-sum over all pairs before column normalization is

    ≪ P^(−1+O(η)) H² (HP)^ε.

Equivalently one may sum the squared d-group bounds, as the groups are disjoint. In particular there is no extra H factor from the common divisor. The D_h normalizations cost (HP)^ε, and choosing η small in terms of ε proves (1). A positive main term has not been discarded: G_hh=1 exactly by definition. □

## Sextic row-mean application

In the Eisenstein sextic setting, take inverse-oriented Gauss profiles on squarefree good h, with the same fixed smooth source profile and ray presentation as [the row-mean frame](../2026-10-29-theta-row-mean-frame/README.md). The theta row-mean input gives, for the normalized Möbius source vector m_P and a fixed polynomial height cost,

    ||A* m_P||² ≪ (HP)^ε (H/P)(1+|t|)^B.                       (5)

Let E be the Gram spectral space with eigenvalues in [1/2,3/2] and V=A(E). Then

    dim V ≥ N−O(H² P^(−1)(HP)^ε),
    ||Proj_V m_P||² ≪ (HP)^ε(H/P)(1+|t|)^B.                   (6)

The projection follows because all singular values of A on E are at least 1/√2. It is a bound for this spectral subspace, not for every individual profile or the full orthogonal complement.

At P=Y^(6/5) and H=P^(53/72−δ), for a fixed 0<δ<53/72, the all-row source operator obeys ||T_(Y,P)||²≪Y^(41/30+ε). Combining with (6) gives

    ||T_(Y,P) Proj_V m_P||²
       ≪ Y^(21/20−(6/5)δ+ε)(1+|t|)^B.                        (7)

Moreover, if V_old is the earlier full span of all sixth-free labels of norm at most P^(1/2−η), its dimension is O(P^(1/2−η+ε)). Whenever 53/72−δ>1/2−η, the intersection V∩V_old^⊥ still has dimension (1−o(1))N and obeys the same projection and energy bounds, because it is a subspace of V. Thus the controlled space contains many directions outside the earlier span.

The value 21/20 is the proposed sixth-moment target exponent, but (7) applies only to the projection onto V. It neither bounds the complementary part nor establishes cancellation between the two images. Source hypotheses, masks, a fixed profile, and a common cumulative height allowance remain essential. No individual zero-free conclusion follows.

**Independent review.** Literature checked the reciprocity and nonprincipal argument, squarefree inversion and common-divisor deletion, the ℓ² treatment of the v- and e-dependent factors, the d-sum, normalizations and projection arithmetic. The review is conditional on the explicitly imported shifted-line, polynomial-height AFE and rectangular-sieve moment, and on the cited source row mean.
