# Full Gauss-profile conditioning below the square-root scale

**Status.** A proposed source-qualified Gram estimate. It uses standard fixed-field Hecke functional equations, the finite-ray sextic reciprocity and zero-mask conventions, and the [unrestricted-row sextic large sieve](../2026-10-29-sextic-collapsed-moment/README.md) derived from de Faveri's theorem. These analytical inputs are imported. The result concerns the full-norm inverse-oriented profile family in the [theta-overlap note](../2026-10-29-cubic-theta-overlap-average/README.md); it does not control its orthogonal complement or establish a zero-free region. Two independent source-level reviews have checked the proof conditional on the stated inputs.

Fix δ>0. Let 1≤H≤P^(1/2−δ), and index profiles v⁻_(P,h) by the good sixth-free ideals h with Nh≤H, one primary generator per ideal. Fix a smooth annular nonnegative weight w(Ns/P) on the squarefree source ideals s in one finite ray sector, nonzero on an interval. Write

    D_h = P^(−1) Σ_(s sf,good,in sector) w(Ns/P) 1_((s,h)=1),
    G_hk = (P√(D_h D_k))^(−1)
             Σ_(s sf,good,in sector) w(Ns/P) χ_s(k) overline(χ_s(h)).

This is the Gram matrix after normalizing the profiles individually; G_hh=1. Standard squarefree ideal counting and prime deletion give H^(−ε)≪D_h≪1. Under the stated inputs,

    ||G−I|| ≪_(δ,ε) P^(−δ/2+ε).                                (1)

Thus every profile is simultaneously conditioned for H≤P^(1/2−δ), a stronger statement than the high-Gram subspace of the companion note. Choose ε<δ/2. A finite collection of norm profiles is covered after replacing the diagonal by its fixed within-h profile Gram block, provided those profiles are linearly independent; (1) is written for one profile to avoid suppressing this block normalization.

## Squarefree inversion and small squares

Insert `1_(s sf)=Σ_(v²|s) μ(v)` and write s=v²t. All v,t are good ideals. Complete multiplicativity retains the zeros exactly:

    χ_(v²t)(h)=χ_(v²)(h)χ_t(h).

Fix v and its finite ray sector; the source sector becomes a fixed sector for t, and the factors χ_(v²)(h) only multiply each column by a scalar of modulus ≤1. The t weight is the same fixed smooth annular profile at scale X=P/Nv². The allowed norms satisfy Nv≪√P; bounded nonempty scales X≈1 are handled by fixed constants. Put

    T=P^(1/2−δ/2)/H.

The assumed H range ensures T≥P^(δ/2) and T≪√P. For h≠k, fixed-field reciprocity on the sector turns the t-dependence into a nonprincipal finite-order Hecke character ξ, times the exact masks at primes shared by h,k and a fixed finite ray factor. A good prime where the sixth-free exponent vectors differ supplies nontrivial ramification, so a fixed S-ray character cannot make ξ principal. Let Q be its primitive conductor norm, and let E be the squarefree product of the additional deleted good primes. Tame local exponents and the original masks give

    Q E ≪_S Nh Nk ≤ H².                                          (2)

At a prime dividing both labels, Q and E together use at most two powers of that prime, whereas Nh Nk contains at least two. At a prime dividing only one, at most one power is used. The fixed S part is bounded. Expanding the E-deletion by divisors e and shifting the primitive Hecke L-function to a fixed far-left line gives, for every M>0,

    |Σ_t w(Nt/X) ξ(t) 1_((t,E)=1)|
       ≪_(M,ε,S,w) Q^(1/2+ε) (QE/X)^M (QE)^ε.                 (3)

This is the standard smoothed functional-equation bound: the gamma ratio has fixed polynomial vertical growth, and w has a rapidly decaying Mellin transform. On our small-square range, `(QE)/X≪H²(Nv)²/P≤P^(−δ)` up to fixed constants. Taking M sufficiently large depending on δ and summing at most O(T) v and O(H) labels per matrix row makes the entire small-square **off-diagonal** operator O(P^(−A)) for any prescribed A after division by P and diagonal normalization. No cancellation between h,k is assumed here.

## Large squares and the diagonal subtraction

For each v, the unrestricted t-sum with its nonnegative row weight defines a positive semidefinite Gram operator K_v. The unrestricted-row sextic large sieve, with sixth-free h columns and X=P/Nv², gives

    ||K_v|| ≪_ε (PXH)^ε [X+H X^(1/6)+X^(5/6)H^(1/3)
                                  +X^(1/3)H^(5/6)].              (4)

It also bounds the diagonal operator of K_v, since each diagonal entry is nonnegative and at most ||K_v||. Hence `||K_v−diag K_v||≤2||K_v||`. Summing (4) for T<Nv≪√P, using ideal counting, gives

    Σ_(Nv>T)||K_v|| ≪_ε (PH)^ε [P/T + H√P
       + P^(5/6)H^(1/3)T^(−2/3) + P^(1/2)H^(5/6)].         (5)

The four terms are O(P^(1−δ/2)), O(P^(1−δ)), O(P^(1−2δ/3)), and O(P^(11/12−5δ/6)), respectively. Thus all large-square off-diagonal terms have unnormalized operator norm O(P^(1−δ/2+ε)). Dividing by P and conjugating by diag(D_h^(−1/2)) costs only H^ε. Combining with the small-square estimate yields (1). The diagonal terms of the Möbius expansion need not be evaluated or estimated asymptotically: they add exactly to diag(D_h), including every mask.

## Consequence and limits

Combine (1) with the source-qualified averaged theta overlap. For any fixed δ>0 and H=P^(25/54−δ), the complete span of all inverse-oriented profiles with sixth-free Nh≤H is conditioned, and its Möbius projection has squared norm

    ≪ (PH)^ε P^(−1)(H+H^(3/2))(1+|t|)^A.

At P=Y^(6/5), the full-row operator bound then gives projected energy `≪Y^(1−9δ/5+ε)(1+|t|)^A`. This promotes the former high-Gram **partial subspace** conclusion to the full indexed span at this H, conditional on the inputs above. It does not cover all h with `N rad(h)≤H`, because such labels may have full norm up to H⁵; nor does it control the complementary operator, the full inverse moment, or an individual zero-free region.

## Fixed order n≥3 over a fixed field

The same proof gives a general source-qualified statement. Fix n≥3 and a number field K containing μ_n, together with de Faveri's fixed good set, admissible character representatives and reciprocity ray sectors. Index the columns by good n-free ideals h with Nh≤H, and let the source rows s be good squarefree ideals of norm ≍P in one fixed ray sector. Form the individually normalized Gram matrix of the n-th order residue-character columns, retaining all source zeros. If the standard FHL reciprocity and tame conductor/mask comparison `QE≪_K Nh Nk` holds in the chosen presentation, then for H≤P^(1/2−δ),

    ||G−I|| ≪_(K,n,δ,ε) P^(−δ/2+ε).                           (6)

Distinct n-free exponent vectors differ nontrivially modulo n at a good prime, even when n is composite, so the small-square quotient is nonprincipal. The far-left Hecke functional equation has a fixed degree-dependent polynomial height cost, absorbed by the fixed test's Mellin decay. The diagonal density and masks are treated exactly as above. For the large-square part use the arbitrary-order unrestricted-row consequence of de Faveri's theorem,

    X+H X^(1/n)+X^(1−1/n)H^(2/n)+X^(2/n)H^(1−1/n).             (7)

Summing at X=P/Nv² for Nv>T gives, up to small powers, P/T and HP^(1/2) for the first two terms. The third is at most `P^(1/2+δ(1/2−1/n)) H`. For the fourth, the v-sum converges at its upper endpoint only for n=3, is logarithmic for n=4, and is dominated by √P for n>4; in all three cases the contribution is O(P^(1/2+δ/2+ε)H). Since H≤P^(1/2−δ), every term is O(P^(1−δ/2+ε)). As before, subtract the exact diagonal, apply PSD to each fixed v, and normalize by the diagonal density. The result is conditional on the source's full arbitrary-order sieve, reciprocity presentation and primitive conductor identities, not on any claimed new zero-free theorem.

**Independent reviews.** Families and Other_families checked the sector and local conductor/mask comparison, the far-left Hecke bound, diagonal subtraction via positive Gram operators, all tail exponents and the general-order cases. These reviews import the cited sieve and analytic inputs; they do not supply complement control.

**Additional independent review:** Amplified_opt checked the small-square range with `s=v²t`, the moving sector and common v-dependent coefficient vector, tame conductor/deleted-mask inequality `QE≪Nh Nk`, and the divisor-expanded far-left Hecke functional equation giving (3). The unrestricted-row large sieve must include the term `H X^(1/n)`; its contribution after summing v is `H√P`, as in (5). The two remaining n-dependent tail sums, diagonal subtraction by positivity, diagonal normalization and the general-order n=3, n=4 and n>4 cases also check, subject to the stated FHL reciprocity, uniform analytic and source large-sieve hypotheses. This is a source-level audit, not a Lean verification or complement bound.
