# Prime-cyclic low-height transfer for Artin L-functions

**Status:** Proposed consequence of published zero-free and low-order theorems; independent review and prior-art assessment required.  
**Scope:** Finite Galois number-field extensions, representations on which a chosen odd-prime subgroup acts nontrivially.  
**Novelty:** No priority or best-known claim. The arithmetic, induction and simple-zero principles are classical. The fixed half-plane claimed by [Liu (2026)](https://arxiv.org/abs/2610.26835), if verified, would dominate this logarithmic region. This note does not assume that preprint.  
**Check performed:** Exact character identity and inequalities derived below; no numeric or symbolic computation is needed.  
**Smallest remaining gap:** Independent verification of all cited analytic hypotheses and the claimed coverage, and an exhaustive search for previously published versions.

## Proposed theorem

Let K/k be a finite Galois extension of number fields, with group G. Choose a subgroup H≤G of odd prime order p, and write M=K^H, D=|disc(K/Q)| and d=|disc(M/Q)|. Assume [M:Q]≥7. For every irreducible representation ρ of G on which H acts nontrivially, L(s,ρ) is holomorphic and nonzero in

    Re(s)>1−(p−1)/[15.10 log(D/d)],
    |Im(s)|<(1/3)tan(π/8).                              (1)

The discriminants are absolute. The weaker, simpler region obtained by replacing log(D/d) by log D also follows. The statement includes s=1, interpreted by holomorphic continuation. No global Artin holomorphy is assumed. The action condition is equivalent to ρ being nontrivial on the normal closure of H in G.

## Proof

The extension K/M is cyclic of degree p. Let λ be a generator of its character group. By the conductor-discriminant formula, all nontrivial characters λ^j have the same finite conductor f, with Q=N_{M/Q}f, and

    D = d^p Q^{p−1},
    A := d Q = (D/d)^{1/(p−1)}.                       (2)

Their associated primitive Hecke L-functions are entire and have order p≥3 as Hecke characters. The [Ahn–Kwon zero-free theorem](https://doi.org/10.1016/j.jnt.2014.06.008) implies each L_M(s,λ^j) is nonzero in (1); the relevant standard Artin–Hecke equality includes the ramified local factors.

The zeta factorization for K/M is

    ζ_K(s) / ζ_M(s) = ∏_{j=1}^{p−1} L_M(s,λ^j).       (3)

It follows that the quotient extends holomorphically and is nonzero throughout (1); hence away from s=1, ord ζ_K = ord ζ_M. At s=1, both zeta functions have simple poles with nonzero residues, which is consistent with (3).

By [Das–Gaba–Lee–Savalia–Wong, Theorem 1.2](https://arxiv.org/html/2506.19319), since [M:Q]≥7, ζ_M has at most one zero in the region σ≥1−1/(11.51910 log d), |t|≤1, and any such zero is real. It is simple by Ahn–Kwon's separate low-height ζ_M theorem: a zero in the Das region also lies in σ>1−1/(2 log d), |t|<1/(2 log d). Since D≥d^p, we have

    [15.10/(p−1)] log(D/d) ≥ 15.10 log d > 11.51910 log d.

Thus (1) lies within that Das region, and ord ζ_K≤1 at every point there other than 1. By Stark's theorem on low-order zeros of Dedekind zeta functions, every irreducible Artin L-function of K/k is holomorphic at such a point; see [Lemke Oliver–Thorner–Zaman](https://rlemke01.math.tufts.edu/papers/27-ApproximateArtin.pdf), discussion following Theorem 3.3.

For each nontrivial λ^j, Frobenius reciprocity gives

    Ind_H^G λ^j = Σ_{ρ∈Irr(G)} ⟨Res_H ρ, λ^j⟩ ρ,

with nonnegative integer coefficients. The Hecke L-function on the left is nonzero. Since all the factors on the right are holomorphic, any constituent with positive coefficient is nonzero. Every ρ on which H acts nontrivially contains at least one nontrivial character λ^j on restriction, so it is covered. At s=1, the classical Brauer–Hecke nonvanishing theorem gives the same conclusion for all nontrivial irreducible ρ. This proves (1). □

The group-theoretic mechanism can also be written as the positive identity

    reg_G − Ind_H^G 1 = Σ_{j=1}^{p−1} Ind_H^G λ^j.    (4)

Unlike a signed Brauer decomposition, every summand here is a genuine character, so once Stark supplies holomorphy, zero-freeness of their L-functions transfers to each constituent without cancellation ambiguity.

## Examples and comparisons

* Every nonabelian finite simple G having an element of odd prime order p has normal closure N=G, so every nontrivial irreducible is covered. For A6 use p=5 and [G:H]=72; the simpler denominator is (15.10/4)log D=3.775 log D. For PSL₂(11), use p=11 and [G:H]=60; the denominator is (15.10/10)log D=1.51 log D. The groups act over arbitrary number-field bases k.
* For S5 use p=5. Its 5-cycles normally generate A5, so the only irreducibles not covered are the trivial and sign characters. All five remaining irreducibles have the denominator 3.775 log D. No statement about the sign character is implied.
* For A5, p=5 gives 3.775 log D for all nontrivial irreducibles, sharpening the 7.55 common denominator in [the earlier A5 note](2026-10-29-a5-hecke-transfer.md). The five-dimensional member still has the stronger 1.8875 bound there.
* For PSL₂(7), p=7 gives 2.516667 log D for all nontrivial irreducibles, agreeing with the more tailored computation in [the nonreal induction note](2026-10-29-nonreal-induction-transfer.md). Its dimensions 6 and 8 have sharper member-specific bounds there.

For comparison only, the 2026 Das theorem applied directly to ζ_K and then Stark gives a denominator 11.51910 log D for all dimension≥2 irreducibles, for |t|≤1. The present region is wider near t=0 for every p≥3, though narrower in height; other estimates can be stronger in the very thin central region, depending on p. The cited results have stronger or more specialized versions; this comparison does not rule out a better published Artin result. The claimed 2026 fixed half-plane is wider if it withstands independent review.

The same calculation applies uniformly to the classical families. For every n≥5, choose an odd prime p≤n and take H generated by a p-cycle in A_n; [A_n:H]≥12 and every nontrivial irreducible is covered. Bertrand's postulate supplies p>n/2, so the simpler discriminant denominator can be taken strictly below 30.20/(n−2) times log D. This is a statement about the displayed arithmetic bound; it is not a comparison with all existing A_n-specific results.

For G=PSL₂(q), q≥4, choose any odd prime p dividing |G|=q(q²−1)/gcd(2,q−1). The group is simple, has an element of order p by Cauchy's theorem, and [G:C_p]≥7, so (1) applies to every nontrivial irreducible. For example p can be any odd prime divisor of q, q−1 or q+1. The bound may be optimized by selecting a largest such prime divisor; no analytic uniformity in the field or representation is needed beyond the explicitly cited inputs.

## Sharper order-at-least-five input

For p≥5 one can use the stronger Ahn–Kwon order-at-least-five constant c=0.1149 at the smaller height |t|≤0.13, quoted in [Zaman (2016), introduction, equation (1.1)](https://arxiv.org/html/1502.05679). It must be intersected with the region where ζ_M has order at most one. The same proof therefore gives all conclusions of the theorem in

    σ > 1 − min{ 0.1149(p−1)/log(D/d),  1/[11.51910 log d] },
    |t| ≤ 0.13.                                       (5)

Strict σ avoids boundary issues. The separate Ahn–Kwon thin-strip theorem makes any real ζ_M exception simple as before. From d^p≤D and log(D/d)≤log D, the explicit subregion

    σ > 1 − min{ 0.1149(p−1), p/11.51910 }/log D,
    |t| ≤ 0.13                                         (6)

is also covered. In particular the guaranteed coefficient of 1/log D is 5/11.51910≈0.43406 for p=5, 7/11.51910≈0.60769 for p=7, and 11/11.51910≈0.95494 for p=11. The 0.1149 Hecke region cannot be used alone in the Stark step unless one separately proves ζ_M has order≤1 on that larger domain. For 0.13<|t|<tan(π/8)/3, retain the earlier 15.10-based result.

**Further coverage:** The same proof in fact covers every irreducible representation of degree at least two, even if H acts trivially: once Stark supplies nonnegative vanishing orders, `ord ζ_K=Σ dim(ρ) ord L(s,ρ)≤1` excludes positive order in degree ≥2. The restriction-to-H argument additionally covers one-dimensional characters nontrivial on H. See [the odd-cyclic generalization](../research/exploratory/2026-10-29-odd-cyclic-transfer/README.md).
