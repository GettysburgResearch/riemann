# Quartic and quintic conductor-density theorem: proof and dependencies

**Status.** The following is a source-qualified theorem package, not an individual L-function zero-free region and not an independent proof of the imported preprints. It uses (i) the [general-order conjugate-pair sieve replay](../2026-10-29-conjugate-conductor-sieve/README.md), derived from de Faveri's analytic machinery but not stated verbatim as a theorem there, (ii) [Goldmakher–Louvel, Corollary 1.2](https://arxiv.org/abs/1112.1642), and (iii) the [fixed-field short-detector and profile replay](../2026-10-29-cubic-short-detector-proof/README.md), including its uniform-height and fixed-type analytic inputs. The [powered-family compatibility review](../2026-10-29-full-order-density/POWERED-FAMILY-INDEPENDENT-REVIEW.md) checks the source normalization needed to combine these results. Their analytical hypotheses, source replay and interpretations remain part of the claim. No exhaustive priority claim is made.

Fix `n=4` or `n=5`, a number field K containing μ_n, a fixed good-prime set S and the de Faveri/FHL n-th-order family χ_g. Fix a unitary Hecke character ν with finite conductor supported on S and fixed infinity type. For a good n-th-power-free ideal g, write `N(σ,T;νχ_g)` for the number of zeros, counted with multiplicity, of the primitive inducing Hecke L-function in `Re s≥σ`, `|Im s|≤T`.

Subject to the above inputs, for every fixed ε>0 there is a τ>0 for which

    Σ_{g good n-free, N cond(νχ_g)≤X} N(σ,X^τ;νχ_g)
      ≪_{K,S,n,ν,σ,ε} X^{R_n(σ)+ε}.                            (1)

For n=4 this holds for `2/3<σ<1`, with `δ=2σ−1` and

    R₄(σ) = 7/6−δ/2              if 1/3<δ≤2/3,
             1−δ/[3(2−δ)]         if 2/3≤δ<1.                  (2)

For n=5 it holds for `3/4<σ<1`, with

    R₅(σ)=7/4−σ.                                                (3)

Every exponent displayed is strictly smaller than 1. For ν=1, the full good n-free family contains ≫X(log X)^{n−2} distinct primitive characters of exact order n and conductor at most X; see the [Euler-product count](../2026-10-29-nfree-conductor-count/README.md). For n=4, the excluded all-even labels contribute only O(X); for n=5 every nonunit label has exact order 5. Hence the count gives zero-free rectangles for all but a power-saving fraction of that exact-order family, at a sufficiently small fixed power height. A general fixed ν still yields the same lower bound for distinct twisted characters but need not have finite order. The estimates do not show nonvanishing for every character.

## Proof mechanism

The unique good factorization `g=∏_{j=1}^{n−1} a_j^j` has squarefree pairwise-coprime a_j. Local tame ramification gives good conductor `∏a_j`, including the exponent-two quartic part, and only bounded fixed bad-place factors. Thus in a conductor box the product of the dyadic sizes A_j is O(X).

The rectangular sieve controls the paired factors `(a_j,a_{n−j})` with a common squarefree source vector. For n=4, the pair `(a₁,a₃)` uses effective order four; the singleton a₂ uses the quadratic large sieve applied directly to `χ_q²`. Goldmakher–Louvel §2 uses the same FHL S,c,E data as de Faveri; its primitive inducing characters agree with de Faveri's original presentations on good ideals, including zero at primes dividing squarefree q. Splitting according to whether `A₂≥X^(1/3)` gives a common-vector second moment `≪X^ε(X+X^(2/3)Q)`. For n=5 the pairs `(a₁,a₄)` and `(a₂,a₃)` both have effective order five. The larger pair has product at least the square root of the full box product, and the analogous moment is `≪X^ε(X+X^(3/4)Q)`. In both cases the residual `Q^(2/m)` term from the rectangular sieve is absorbed by weighted arithmetic–geometric mean. The powered-family review proves compatibility of the n- and effective-order constructions with their zero masks; Corollary 1.2 handles the even-order quadratic singleton directly. Summing the O(log^{n−1}X) boxes costs a subpower.

Writing an ordinary source ideal uniquely as `qv²` with q squarefree and removing the row multiplier `χ_g(v²)` only after fixing v, the same moment follows by Minkowski and the ideal harmonic sum. Thus inverse and plain blocks of length `X^x` satisfy the common exponent `E_n(x)=max(1,c_n+x)`, where `c₄=2/3` and `c₅=3/4`. Uniform Sobolev control handles the row-dependent witness real parts and frequency using common coefficient vectors and absorbs the fixed-height losses.

The detector replay supplies simultaneous inverse and plain witnesses with lengths r,m satisfying `r+m≥t`, `r≤t`, `m≤1/2` up to arbitrarily small fixed losses, and each squared response is at least its length to power `δ=2σ−1`. Applying both moments gives the row-count exponent

    min{max(1,c_n+r)−δr, max(1,c_n+m)−δm}.

Optimizing t and the witness pair yields (2) and (3). Choosing losses first and τ afterward absorbs the finite bins, dyadic factors, Sobolev height cost, and individual zero multiplicity. Detailed arguments, including the endpoint and strict quantifier order, are in the [quartic proof](../2026-10-29-full-quartic-density/README.md) and [full-order proof](../2026-10-29-full-order-density/README.md).

## Examples and comparisons

At σ=4/5, the conditional exponents are `R₄=13/15` and `R₅=19/20`. For K=Q(i) and K=Q(ζ₅), respectively, the cited general all-character conductor theorem of [Khale–O'Kuhn–Panidapu–Sun–Zhang](https://arxiv.org/abs/2008.09677v3) gives fixed-height X exponent 1 at that point; for sufficiently small fixed τ, the displayed family exponents remain smaller after its height factor is included. The stronger squarefree-label bounds of Blomer–Goldmakher–Louvel and de Faveri concern a smaller label family, while de Faveri's full n-free result is ordered by index norm rather than conductor; conjugate reordering incurs the losses described in the [comparison audit](../2026-10-29-quartic-quintic-density-prior-art.md). The cited general-character bound wins again for σ sufficiently close to 1. These are comparisons with identified theorems, not an exhaustive novelty determination.

**Independent review.** High_match checked the theorem quantifiers, exponent calculations, prime-label exact-order density, Goldmakher–Louvel singleton and stated source qualifications. The general-order sieve and detector remain the separately identified source replays.
