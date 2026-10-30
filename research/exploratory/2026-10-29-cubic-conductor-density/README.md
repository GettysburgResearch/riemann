# Conductor-ordered cubic zero density by conjugate reordering

**Status:** Direct consequence conditional on a cited preprint, with independent internal review of the cubic case. This is a family zero-density estimate, not an individual zero-free region. No priority claim is made; the cited paper already proves the norm-ordered estimate, and the simple reordering below has not been checked against the broader literature. De Faveri's preprint has not been independently verified here.

## Statement

Fix a number field K containing μ₃, let d=[K:Q], and fix the finite set S and the cubic Fisher–Friedberg/De Faveri family `χ_g` in [De Faveri, arXiv:2610.04045v1](https://arxiv.org/abs/2610.04045v1), §§1–2. Thus S contains the primes above 3, the ring of S-integers has class number one, g ranges over good cube-free integral ideals, and the original family values retain zero masks. Let `f_g` be the primitive conductor. For X≥2, T≥2 and 1/2<σ<1, define

    D_cond(X;σ,T) = Σ_{g good cube-free, N f_g≤X} N(σ,T,g),

where `N(σ,T,g)` counts zeros with multiplicity of the primitive inducing L-function, with `Re ρ≥σ` and `|Im ρ|≤T`. The zero-free half-plane Re(s)>1 need not be included in the counting region. The principal label is allowed; its pole is not counted as a zero. The original imprimitive and primitive L-functions have the same zeros in Re(s)>0, because each deleted Euler factor is nonzero there.

Let δ₃(σ) be the n=3 function in De Faveri Corollary 1.5. Then, subject to that source result, for every ε>0,

    D_cond(X;σ,T) ≪_{K,S,σ,ε}
       X^{(3/2)(1−δ₃(σ))+ε}
       T^{1+d(1−σ)/(3−2σ)+ε}.                         (1)

At 5/6≤σ<1 the source function is

    δ₃(σ) = (8σ²−10σ+3)/(1−12(1−σ)²).

It equals 1/3 at 5/6 and increases thereafter. Thus for 5/6<σ≤7/8, (1) saves a power of X over the trivial O(X^(1+ε)) count for fixed or polylogarithmic T. For example,

    D_cond(X;17/20,T) ≪ X^{135/146+ε} T^{1+3d/26+ε},
    D_cond(X;7/8,T)  ≪ X^{21/26+ε} T^{1+d/10+ε}.

For σ>7/8, Hu's independently imported claimed 7/8 theorem would make the count zero, so no advantage is asserted there. The bounds count family labels; they remain upper bounds after deduplicating primitive characters. The source bound is for the untwisted fixed family: arbitrary fixed Hecke twists, other height windows, and conductor-varying target twists are not asserted here.

## Proof

Write each good cube-free ideal uniquely as `g=a b²`, where a,b are squarefree and coprime. De Faveri §2.5.1 gives primitive conductor `f_g=c_g·rad(g)` with `c_g` supported on the fixed S modulus. Consequently

    N(ab)=N rad(g)≤N f_g≤X.                               (2)

The same section states the multiplicativity and original zero extension of the cubic family. Therefore

    χ_(a b²) = conjugate(χ_(b a²)),                       (3)

including at ideals meeting ab: away from ab, the characters take values in μ₃, and on noncoprime ideals both sides are zero. Thus their primitive inducing characters are conjugates and their L-zero multisets are reflected across the real axis. The count in the symmetric window |Im ρ|≤T is identical, including multiplicities.

For each pair (a,b), choose either g=a b² or its conjugate label g'=b a² so that the squared factor in the chosen label has norm at most `(N(ab))^(1/2)`. Its ideal norm is therefore at most

    N(ab)·min(Na,Nb) ≤ X^(3/2).                           (4)

The map from original labels to chosen labels has multiplicity at most two: the unordered pair {a,b} determines both possible labels. The chosen label is again good and cube-free. Apply De Faveri Corollary 1.5 with its norm cutoff `N=X^(3/2)` and rename the arbitrarily small loss. Equation (3) preserves the zero count, and the factor two does not affect the estimate. This gives (1) for all displayed σ,T. The only source input to this density deduction is Corollary 1.5 and the conductor/family properties; De Faveri's separate central second moment Theorem 1.2 does not by itself imply (1).

The elementary trivial family bound is `D_cond≪ X^(1+ε)(T+1) log(X(T+3)^d)`: count pairs `(a,b)` with `N(ab)≤X`, and apply the standard individual Hecke zero count. Hence the displayed bounds are particularly meaningful for fixed and polylogarithmic heights; for polynomial T, the additional T exponent in (1) must also be included in the comparison. □

## Density-one zero-free rectangles

The bound has a direct family-level zero-free consequence. Let `F(X)` be the set of **distinct primitive characters** induced by the good cube-free labels with conductor norm at most X. The fixed modulus c in De Faveri §2.5.1 gives `f_p=c_p p` and `Nc_p≤Nc` for every good prime ideal p. Thus every good p with `Np≤X/Nc` gives a character in F(X), and different p give different primitive characters because their conductors have different good-prime supports. The prime ideal theorem therefore gives

    #F(X) ≫_{K,S} X/log X.                                (5)

Let `Bad(X;σ,T)` be the subset of these distinct characters that have at least one zero with `Re(s)≥σ` and `|Im(s)|≤T`. It has cardinality at most `D_cond(X;σ,T)` regardless of repeated labels. Therefore, if

    0≤τ < [1−(3/2)(1−δ₃(σ))] /
               [1+d(1−σ)/(3−2σ)],

then at T=max(2,X^τ) a proportion tending to one of F(X) has **no** such zero. The numerator is positive for 5/6<σ<1. This is a density-one statement as X→∞: it does not assert an individual uniform zero-free region or nonvanishing at unbounded heights for any single character.

For the Eisenstein field d=2 and σ=17/20, the admissible height range is

    0≤τ<143/2336 = 0.06121575… .

For example τ=1/20 gives

    #Bad(X;17/20,X^(1/20)) ≪_ε X^{9359/9490+ε},

so (5) yields a power-saving exceptional proportion. The σ and height exponents follow directly from (1), and the exceptional count and prime-ideal lower bound count **distinct** characters as specified.

## Comparison with other source claims

The fixed-Eisenstein, small-power-height [rStation paper 52, version 5, Theorem 1](https://rstation.ai/problems/riemann_hypothesis/papers/52), claims stronger cube-free norm-ordered density with fixed finite twists. The same conjugate reordering yields better conductor exponents at sufficiently small power height; for example its exponent 15/29 at σ=17/20 becomes 45/58 after the factor 3/2. Its admissible positive height power depends on the fixed data and is not explicitly quantified there. Thus (1)'s distinctive feature is its explicit T dependence and its fixed-field scope, not a claim to the strongest low-height Eisenstein density result. This comparison imports that recent source and does not independently verify its analytic proof.

## Extension to arbitrary fixed order n≥3

De Faveri's same source gives a formal general-order conductor-reordering consequence. Fix n≥3, a fixed number field K containing μ_n, and the source's good n-th-power-free Hecke family. Define the analogue of `D_cond` above. Let δ_n(σ) be the full piecewise function in De Faveri Corollary 1.5. For X≥2, T≥2 and 1/2<σ<1,

    D_cond,n(X;σ,T) ≪_{K,S,n,σ,ε}
      X^{(n/2)(1−δ_n(σ))+ε}
      T^{1+d(1−σ)/(3−2σ)+ε}.                        (6)

To prove (6), write a good n-th-power-free index uniquely as

    g=∏_{j=1}^{n−1} a_j^j,

where the a_j are pairwise coprime squarefree ideals. Its conjugate label is `g'=∏ a_j^(n−j)`. Source multiplicativity and zero extension give χ_g'=conjugate(χ_g), including for composite n and at every noncoprime argument. Source §2.5.1 gives `f_g=c_g g*`, where `g*=∏_{n∤v_p(g)}p`; since the index is n-th-power-free, `g*=rad(g)`. Therefore

    Ng · Ng' = (N rad(g))^n ≤ X^n.

Choose the smaller of g,g'; its norm is at most X^(n/2), and the map has fibers of size at most two. Symmetric-height zero counts agree under conjugation. Applying the source norm-ordered density to the chosen labels gives (6).

In the source's last branch `1−1/(2n)≤σ<1`, put u=1−σ. Then

    δ_n(σ)−(1−2/n)
       = 2(1−nu)(1−2nu) / [n(1−4nu²)].

Thus `(n/2)(1−δ_n(σ))<1` for σ>1−1/(2n), giving the same density-one conclusion at sufficiently small polynomial heights after the prime-ideal lower bound (5). For n=3 this starts at 5/6, below Hu's claimed 7/8 boundary; for n≥4 the threshold is at least 7/8, so the conditional density statement is not an improvement over that claimed individual boundary. No priority or optimality claim is made. Two independent internal reviews checked the general-order conductor, conjugation, two-to-one map and last-branch algebra; they do not verify the cited preprint.

**Internal review:** Independent reviewers checked the cubic and general-n reordering, primitive conductor and deleted Euler factors, zero multiplicities, prime-label distinctness, the explicit height and exceptional exponents, and the rStation comparison. Their review is conditional on the cited source theorems.

## Stronger small-height consequence of rStation paper 52

For K=Q(√−3), the same conjugate reordering gives a stronger conductor-ordered statement if one also assumes [rStation paper 52, version 5, Theorem 1](https://rstation.ai/problems/riemann_hypothesis/papers/52). Fix a finite-order Hecke twist ν with conductor supported on the fixed S. For each fixed `5/6≤σ<1` and each ε>0, there is a τ>0, depending on σ, ε, S and ν, such that

    Σ_{g good cube-free, N cond(νχ_g)≤X}
      N(σ,X^τ;νχ_g) ≪_{σ,ε,S,ν} X^{(3/2)E_new(σ)+ε}.     (7)

The source function E_new is given by paper 52, equations (1b)–(1e). In particular, its stated values give

    σ=5/6:    exponent 9/10+ε,
    σ=17/20:  exponent 45/58+ε,
    σ=7/8:    exponent 27/44+ε.

At good primes the fixed twist is unramified and cannot cancel the nontrivial cubic ramification, so `N rad(g)≤N cond(νχ_g)`; the fixed S-conductor contributes only fixed factors. Choose the smaller conjugate label as before. If a label is conjugated, the zero count for `νχ_g` becomes that for `conjugate(ν)χ_g'` in the same symmetric height window. The source theorem permits each of these two fixed twists, so both orientations are covered, each with its own fixed constants and admissible height exponent.

The source theorem is dyadic, at height `P^h` for a sufficiently small h>0 depending on σ, ε, S and the fixed twist; it does not state one common height bound for all conductor dyads. To obtain (7), fix a small λ>0 below `(3/2)E_new(σ)`, choose τ<λh, and apply the source theorem to dyads P≥X^λ, whose permitted height is at least X^τ. For P<X^λ use the elementary ideal count O(X^λ) and individual zero bound O((X^τ+1)log(X(T+3)^2)); choose λ and τ so that λ+τ<(3/2)E_new(σ). Summing the O(log X) dyads gives (7) after shrinking losses. The constants and the existence of τ are not claimed uniform as σ approaches 1, nor as ν varies. The n=3 family, prime-label lower bound and resulting density-one interpretation are as above.

This sharper assertion is conditional on a separate recent source theorem and its analytic inputs, none independently verified here. It does not supply the explicit all-T dependence of (1), nor an individual zero-free region. No priority claim is made.

**Index versus conductor at σ=4/5:** The [ordering comparison](../2026-10-29-defaveri-cubic-density-ordering.md) records that Corollary 1.5 is summed over **cube-free** indices but ordered by index norm, and that its 8/11 exponent at σ=4/5 is a conductor-ordered statement only for the squarefree-index subfamily. Applying the general fixed-family conjugate reordering to all conductor≤X cube-free indices gives 12/11, not 8/11. Source §2.5.1 (2.4) supplies the exact label conjugation, including zero masks; an additional external fixed twist has its own conjugation and source-uniformity requirements.
