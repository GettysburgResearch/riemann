# Low-height Artin transfer from odd Frobenius subgroups

**Status:** Proposed combination of cited zero-free and low-order theorems; independent mathematical review and prior-art search are required.  
**Scope:** Finite Galois number-field extensions containing a subgroup C_p⋊C_q with odd primes p,q with q≥3 and a faithful action. No global Artin holomorphy or automorphy is assumed.  
**Novelty:** No priority or best-known claim. Artin induction, Frobenius character theory and the analytic bounds are existing inputs; the exact numerical corollary has not been searched exhaustively. A recent unreviewed preprint claims a stronger fixed half-plane.  
**Inputs:** [Ahn–Kwon's order-three theorem](https://doi.org/10.1016/j.jnt.2014.06.008) and its order-at-least-five coefficient as quoted by [Zaman (2016), equation (1.1)](https://arxiv.org/html/1502.05679); [Das et al. (2026), Theorem 1.2](https://arxiv.org/html/2506.19319); Ahn–Kwon's separate low-height Dedekind theorem; Stark's low-order theorem; Artin–Hecke induction.  
**Smallest remaining gap:** Independent verification of the Frobenius character decomposition, normalization and ramified local factors, the quoted analytic constants, and prior art.

## Theorem

Let K/k be finite Galois with group G. Suppose G has a subgroup H≅C_p⋊C_q, for odd primes q≥3, p, and a faithful action of C_q on C_p. Put P=C_p, M=K^H, E=K^P, D=|disc(K/Q)|, dM=|disc(M/Q)| and dE=|disc(E/Q)|. Assume [M:Q]≥7. Set c_q=1/15.10 when q=3, and c_q=0.1149 when q≥5. Set

    Δ=min{ 0.1149(p−1)/log(D/dE),
           c_q(q−1)/log(dE/dM),
           1/(11.51910 log dM) }.

In the region `Re(s)>1−Δ`, `|Im(s)|≤0.13`, every irreducible Artin L-function of degree at least two, and every nonreal one-dimensional factor, is holomorphic and nonzero. Across the remaining real one-dimensional factors there is at most one simple real zero. At s=1 the trivial factor has its usual pole, and every nontrivial irreducible factor is nonzero.

A simpler sufficient width is `0.1149(p−1)/log D` at the same heights. If k=Q and G has no quotient of order two, ζ_K itself is zero-free in this region, apart from its pole at 1.

## Proof

H is a Frobenius group of order pq. Its q linear characters are inflated from H/P≅C_q. The remaining irreducible characters are induced from the (p−1)/q H-orbits of nontrivial linear characters of P; each such irreducible has degree q. This follows from the faithful C_q-action on the p−1 nontrivial P-characters, the usual character inner product for induced representations, and the dimension-squared identity `q+(p−1)q=pq`. Consequently, the regular-representation identity and induction give

    ζ_K/ζ_M = ∏_{ω∈(H/P)^, ω≠1} L_M(s,ω)
              × ∏_{[λ]∈(P^−{1})/(H/P)} L_E(s,λ)^q.       (1)

Every ω has order q and every λ has order p; all are nonreal. The faithful action forces p≡1 (mod q); in particular p≥7 and p≥5. These are primitive Hecke L-functions, with the complete ramified Euler factors supplied by Artin induction and class field theory.

The extensions K/E and E/M are cyclic of prime degrees p and q, respectively. Nontrivial characters within either cyclic character group share their finite conductor. The conductor–discriminant formula yields

    A_λ := dE N fλ = (D/dE)^{1/(p−1)},
    A_ω := dM N fω = (dE/dM)^{1/(q−1)}.              (2)

These positive numbers exceed one because [M:Q]≥7. By the quoted Ahn–Kwon results, each λ-factor is entire and zero-free for `Re(s)>1−0.1149/log A_λ`, and each ω-factor is entire and zero-free for `Re(s)>1−c_q/log A_ω`, with `|Im(s)|≤0.13` in both cases. Therefore the quotient (1) is holomorphic and nonzero in the first two parts of the displayed intersection. The third part is contained in the Das et al. zero-free region for ζ_M except for at most one real zero; that zero is simple by the separate Ahn–Kwon 1/(2 log dM) theorem. Thus away from 1, ord ζ_K=ord ζ_M≤1 and any zero is real.

Stark implies all irreducible Artin L-functions of K/k are holomorphic there. Their zero orders are nonnegative integers and their degree-weighted sum is at most one. A factor of degree at least two cannot vanish, and two distinct one-dimensional factors cannot both vanish. If a nonreal one-dimensional factor vanished at the real exceptional point, its conjugate would vanish as well, a contradiction. Brauer–Hecke nonvanishing treats all nontrivial irreducibles at 1.

For the simple width, the tower formulas imply dE^p≤D and dM^{pq}≤D. Hence

    log A_λ≤log D/(p−1),
    log A_ω≤log D/[p(q−1)],
    log dM≤log D/(pq).

For q≥5, `c_q p(q−1)≥0.1149(p−1)`; for q=3, `2p/15.10>0.1149(p−1)`. In both cases `pq/11.51910≥0.1149(p−1)`. The width `0.1149(p−1)/log D` therefore lies inside all three parts of Δ. If G has no quotient of order two over Q, the only real one-dimensional representation is trivial. Its ζ_Q factor has no zeros in the low-height region: the region lies to the right of 1/2, since each log A is at least log 2; use [Platt–Trudgian](https://doi.org/10.1112/blms.12460) for nonreal zeros and the standard real-axis sign. This yields the ζ_K corollary. □

## Example and named comparison

For PSL₂(11), the normalizer of a subgroup C11 is C11⋊C5, of index 12. Thus for every PSL₂(11)-Galois extension K/k, [M:Q]≥12 and the theorem gives the exception-free width `1.149/log D` for every nontrivial irreducible at `|t|≤0.13`. Over Q, PSL₂(11) is simple, so ζ_K itself is zero-free there except for its pole.

The separately derived cyclic-C11 transfer using the same 0.1149 Hecke input and a Dedekind cap gives the uniform width `min{1.149, 11/11.51910}/log D = (11/11.51910)/log D`. The Frobenius subgroup replaces that cap by a smaller fixed field M, giving coefficient 1.149 instead of approximately 0.955: about 20.3% wider in this comparison. The cyclic method can be stronger for specific fields when exact conductor and discriminant terms are retained. Elimination of exceptional zeros in fields without quadratic subfields is classical: see [Pierce–Turnage-Butterbaugh–Wood, Theorem 5.9 and Theorem N](https://dukespace.lib.duke.edu/bitstreams/6ca77058-c44c-4932-8fa5-cb7c8c9570ec/download). No claim is made that the displayed coefficient is best known or externally new.

For PSL₂(7), the normalizer of C7 is C7⋊C3 of index 8. Taking p=7 and q=3 yields width 0.6894/log D for all nontrivial irreducible factors at |t|≤0.13, and for ζ_K itself over Q. This compares with the named cyclic-C7 capped coefficient 7/11.51910≈0.60769, a roughly 13.45% increase in this particular comparison; it is not a claim of an optimal constant.

## Composite and even complements

The following generalization includes complements of even order. Let H≅C_p⋊C_r with p an odd prime, r≥3 dividing p−1, and faithful action. Put P=C_p, J=H², F=K^J, M=K^H, E=K^P and g=gcd(2,r). Assume [F:Q]≥7. Then

    Re(s)>1−0.1149(p−1)/log D,   |Im(s)|≤0.13          (3)

has the same conclusion as the theorem: every irreducible of degree≥2 and every nonreal degree-one irreducible is holomorphic and nonzero, and at most one simple real zero from a real one-dimensional factor can remain.

Indeed H² contains P because p is odd, and its image in H/P≅C_r is the subgroup of squares. Thus |J|=pr/g, and the 1-dimensional characters trivial on J are precisely those of order at most two. The faithful C_r-action makes each orbit on the nontrivial P-characters have size r; Frobenius character theory gives

    ζ_K/ζ_F = ∏_{ω∈(H/P)^, ord(ω)>2} L_M(s,ω)
              × ∏_{[λ]∈(P^−{1})/(H/P)} L_E(s,λ)^r.   (4)

The λ characters have order p≥5 and satisfy `dE N fλ=(D/dE)^{1/(p−1)}≤D^{1/(p−1)}`. Let ω₀ be a generator of the character group of E/M, Q=N fω₀. All powers of ω₀ have conductor dividing fω₀, and its φ(r) faithful powers have the same conductor. The conductor–discriminant and tower formulas give

    dE≥dM^r Q^{φ(r)},       D≥dE^p,
    dM N fω ≤ dM Q ≤ D^{1/[p φ(r)]}.                 (5)

Every ω appearing in (4) has order at least three. Ahn–Kwon gives its zero-free region using coefficient 1/15.10; the order-p factors use 0.1149 at |t|≤0.13. Since φ(r)≥2, `pφ(r)/15.10 ≥ 2p/15.10 > 0.1149(p−1)`, so (3) lies in both Hecke regions. Also d_F^{pr/g}≤D and r/g≥2, hence the width of the Das et al. low-order region for ζ_F is at least `2p/(11.51910 log D)>0.1149(p−1)/log D`. Its possible real zero is simple by the cited Ahn–Kwon Dedekind theorem. The same Stark and complex-conjugation argument as above proves the conclusion. At s=1, use classical Brauer–Hecke nonvanishing for nontrivial factors. Over Q, if G has no quotient of order two, the only real one-dimensional factor is ζ_Q. The region is strictly to the right of 1/2 because its actual Hecke widths are bounded by 0.1149/log 2, so the cited Platt–Trudgian verification and the real-axis sign remove ζ_Q zeros. Thus ζ_K itself is zero-free there apart from its pole.

For example S5 contains C5⋊C4=AGL₁(F5), with |H²|=10 and [S5:H²]=12. All irreducible S5 Artin L-functions of degree≥2 are therefore zero-free in `Re(s)>1−0.4596/log D`, `|t|≤0.13`; over Q the sole possible real exceptional factor is the sign character. In the same named uniform comparison, the cyclic-C5 capped coefficient is 5/11.51910≈0.43406, so 0.4596 is about 5.9% wider. For PSL₂(13), a Borel subgroup C13⋊C6 gives coefficient 1.3788; over Q the corresponding ζ_K is also zero-free apart from its pole. These comparisons do not assert priority or superiority to all published bounds.

More generally, for every prime p≥7, PSL₂(p) has a Borel subgroup `C_p⋊C_{(p−1)/2}` with faithful action and index p+1. Its square subgroup has index at least p+1≥8. Thus every PSL₂(p)-Galois extension K/k has all nontrivial irreducible Artin L-functions zero-free in `Re(s)>1−0.1149(p−1)/log D`, `|Im(s)|≤0.13`. For k=Q this is also a zero-free region for ζ_K, apart from its pole. The estimate uses only the quoted Hecke coefficient and low-order results; it is not a priority or optimality claim.

## Elementary-abelian Frobenius kernels

The cyclic kernel in the preceding argument can be replaced by an additive finite field. Let p≥5 be prime, f≥1, q₀=p^f, and let H=N⋊C_r where N≅(F_{q₀},+), r≥3 divides q₀−1, and the complement embeds in F_{q₀}^× and acts by multiplication. Let K/k be finite Galois with H≤Gal(K/k), F=K^{H²}, and D=|disc(K/Q)|. If [F:Q]≥7, then all irreducible Artin factors of degree≥2 and all nonreal one-dimensional Artin factors are holomorphic and nonzero in

    Re(s)>1−0.1149 p^{f−1}(p−1)/log D,    |Im(s)|≤0.13.   (6)

At most one simple real zero from a real one-dimensional character remains; at 1 only the trivial factor has a pole. When k=Q and Gal(K/Q) has no C2 quotient, ζ_K itself is zero-free in (6), apart from its pole. This is a proposed consequence of the same classical inputs, not a priority or best-known claim.

To prove it, the complement acts freely on the nontrivial characters of N: if a≠1 in the complement fixes a character, multiplication by a−1 is invertible on N, so that character is trivial. Consequently the non-linear irreducibles of H are the inductions of those nontrivial N-characters, one per orbit, each of degree r; the other irreducibles are the linear characters of H/N≅C_r. This follows from the induced-character inner product and the dimension check `r+((q₀−1)/r)r²=q₀r`.

N⊆H² because p is odd, and H² maps onto the square subgroup of C_r; with g=gcd(2,r), `|H²|=q₀r/g`. Put M=K^H, E=K^N. As above, ζ_K/ζ_F factors into the L_M(s,ω) for complement characters ω of order>2 and the r-th powers of L_E(s,λ) for orbit representatives of nontrivial N-characters λ. Every λ has order p and kernel of size q₀/p. The intermediate field L=K^{ker λ} satisfies [K:L]=q₀/p and L/E cyclic of degree p. Its conductor–discriminant formula gives

    (d_E N fλ)^{p−1}=d_L/d_E,    d_L^{q₀/p}≤D,

so `d_E N fλ≤D^{1/[(q₀/p)(p−1)]}`. The λ conductors need not agree across distinct orbits; the bound holds separately for each. For the complement characters, E/M is cyclic of degree r. The faithful-power conductor bound and D≥d_E^{q₀} yield `d_M N fω≤D^{1/[q₀φ(r)]}` for each ω. All appearing factors are nonreal.

Use coefficient 0.1149 for order-p Hecke factors and 1/15.10 for complement factors. Since φ(r)≥2,

    q₀φ(r)/15.10 ≥ 2q₀/15.10 > 0.1149(q₀/p)(p−1).

The ζ_F low-order width is at least `q₀r/[g·11.51910 log D]`; because r/g≥2 it also contains (6). The quotient is therefore holomorphic and nonzero there; Das et al., Ahn–Kwon, and Stark complete the same multiplicity and conjugate-character argument. The no-C2 ζ_K consequence follows as before: (6) lies strictly to the right of 1/2 since `D≥2^{(q₀/p)(p−1)}`, and the trivial ζ_Q factor is zero-free at the stated low heights by the cited partial RH verification and real-axis sign.

For q₀=p^f≥7, PSL₂(q₀) has Borel subgroup `N⋊C_{(q₀−1)/2}` of this form, and [PSL₂(q₀):H²]≥q₀+1≥8. Consequently every nontrivial irreducible factor of a PSL₂(q₀)-Galois extension satisfies (6); for k=Q its Dedekind ζ-function does too, except for the pole. For example q₀=25 gives coefficient 0.1149·5·4=2.298 in front of 1/log D. These stated families and numerical comparisons have not been exhaustively checked against the literature.
