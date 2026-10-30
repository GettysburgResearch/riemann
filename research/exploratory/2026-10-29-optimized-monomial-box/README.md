# Optimized unbalanced boxes and monomial representations at 4/5

**Status.** Source-qualified, conditional family zero-density deductions. The generalized conjugate-pair sieve and the fixed-field buffered detector with common-profile/height control are explicit source replays in the [unbalanced-box note](../2026-10-29-unbalanced-cubic-density/README.md); they have not been independently established here. No individual zero-free region, unconditional priority claim, or comparison with all previous results is asserted. The numerical comparison below uses de Faveri's stated natural-index corollary as a specific comparator.

Fix n≥4, K containing μ_n and the corresponding good S and FHL order-n character family. Put

    a_n = (3n−10)/[5(n+2)(n−2)]                  for 4≤n≤10,
          0                                      for n≥11;
    R_n = (13n+50)/[25(n+2)]                     for 4≤n≤10,
          (13n²−5n−50)/[25n(n−2)]                for n≥11.  (1)

For σ=4/5 and ε>0, the cited conditional detector/sieve argument gives τ>0 with

    Σ_{A,B} N(4/5,X^τ;χ_(A B^(n−1))) ≪ X^(R_n+ε),            (2)

where A,B are pairwise-coprime good squarefree ideals in fixed boxes `NA≍X^a_n`, `NB≍X^(1−a_n)`. When a_n=0, take A=(1) and B in the indicated norm range. Count zeros of the primitive inducing L-function, with multiplicity; conjugation and original zero masks are retained. At each good p|AB the local exponent is ±1, so the characters have exact order n and primitive conductor `≍N(AB)≍X`. The fixed-bad-prime part is bounded. Taking A,B prime for a_n>0 gives ≫X/(log X)² distinct characters; A=(1), B prime gives ≫X/log X when a_n=0. Consequently (2) gives density-one zero-free rectangles at small polynomial height, subject to the stated inputs.

Examples: n=4 gives `a_4=1/30`, `R_4=17/25`; n=5 gives `a_5=1/21`, `R_5=23/35`; n=7 gives `a_7=11/225`, `R_7=47/75`; and n=11 gives `a_11=0`, `R_11=1468/2475`. As n grows, R_n tends to 13/25. This limit ranges over different fixed-order families; constants and τ may depend on n and no uniformity in n is asserted.

## Derivation and natural-index comparison

In the unbalanced-box note's notation, at δ=2σ−1=3/5 put

    c=1/n+a(1−2/n),   d=1−c,
    t_long=max{d+δ/2,(1−2c−1/n+δ/2)/(1−2/n)}.

For `4≤n≤10`, the a_n in (1) makes the two long-detector constraints equal:

    c = 8/[5(n+2)],
    t_long = 13/10 − 8/[5(n+2)],
    R = c+(1−δ)t_long = (13n+50)/[25(n+2)].                 (3)

For n≥11 take a=0 and the second constraint is active, giving the second formula in (1). All cases have `δ>2c` and `1<t_long<3/2`, so the cited long-cutoff detector and scalar minimax apply. In its long-range regime the maximum of the two affine constraints is minimized at the crossing for n<10, is flat up to it for n=10, and is minimized at a=0 for n>10. This does not claim a global optimization over every possible sieve, detector or arithmetic subfamily.

De Faveri [Corollary 1.5](https://arxiv.org/abs/2610.04045v1), at σ=4/5, gives natural-index exponent

    D_n = (12n²−38n+5)/(21n²−80n+50).                         (4)

All n≥4 are in its middle branch. Conjugating a label replaces `A B^(n−1)` by `A^(n−1) B`, of norm ≍X^[1+(n−2)a_n]. Good local exponents distinguish the label and its conjugate, and this reordering has multiplicity at most two. The natural-index corollary gives the comparator

    X^[(1+(n−2)a_n)D_n+ε] T^[1+[K:Q]/7+ε].                    (5)

After taking sufficiently small polynomial height and losses, the exponent in (2) is smaller than this comparator. For 4≤n≤10 the exact difference is

    (3n−10)(69n²−280n+250) /
       [25(n+2)(21n²−80n+50)] > 0,                            (6)

while for n≥11 it is

    (3n−10)²(3n²−25n+25) /
       [25n(n−2)(21n²−80n+50)] > 0.                           (7)

At n=4, the comparator exponent is 8/11≈0.72727, versus 17/25=0.68. At n=5 it is 184/245≈0.75102, versus 23/35≈0.65714. For n≥11, A=(1) is a squarefree-index subfamily and (7) compares directly without reordering. Formula (5) is one explicit comparison only; other methods could give better bounds. In particular the putative n≥11 improvement still depends on the generalized rectangular-sieve replay, which is not stated verbatim in de Faveri's paper.

## Monomial Artin and automorphic subfamilies

For n=4 take K=Q(i), and for an odd prime n=p≥5 take K=Q(ζ_p). Let d=[K:Q] (respectively 2 and p−1). If a_n>0, retain pairs A,B of prime ideals above distinct rational primes splitting completely in K. If a_n=0, take A=(1) and B above a split rational prime. In their prescribed norm ranges, the prime ideal theorem/Chebotarev gives ≫X/(log X)² pairs for a_n>0 and ≫X/log X labels for a_n=0. Since the norms of A and B have different scales, no nonidentity automorphism of K/Q fixes their good support; the same is true of a single split prime B. Thus χ has a full d-element Galois orbit, and `N_K f(χ)≍X`.

The induced finite-image Artin representation `ρ=Ind_(W_K)^(W_Q)χ` is irreducible by Mackey, and cyclic automorphic induction gives a cuspidal representation of GL_d with the same standard L-function. Artin induction and its conductor formula give

    N(ρ)=|D_K| N_K f(χ),  L_Q(s,ρ)=L_K(s,χ).                   (8)

Induced representations have fibers of size at most d among distinct inducing characters, since restriction to W_K recovers their Galois orbit. After adjusting fixed box constants to enforce conductor ≤X, the above lower counts persist up to the fixed factor d. The number with a zero in `Re s≥4/5`, `|Im s|≤X^τ` is O(X^(R_n+ε)), by (2) and the fixed conductor factor. For n=4 the representations are odd and the automorphic inductions are dihedral holomorphic weight-one theta forms. For p≥5 they are cuspidal GL_(p−1) inductions; no holomorphic or cohomological weight claim is made.

This is an arithmetic subfamily at a specified split of the conductor, not an estimate for all GL_d representations. The source density and induction inputs are explicit; comparison with all prior dihedral or automorphic density theorems remains open.

The symbolic minimax and comparator identities, positive-polynomial witnesses and rational examples are reproducible with [check_scalars.py](check_scalars.py). Independent code/mathematical reviews checked the long-branch optimization, source exponent and height factor, conductor and conjugation, the squarefree n≥11 subfamily, and split-prime induction/fibers. A targeted literature review checked the n=4 natural-index comparison and found the general finite-order Hecke comparator weaker; it was not exhaustive. None of these checks proves the source preprint, its generalized sieve replay, or the detector assumptions.
