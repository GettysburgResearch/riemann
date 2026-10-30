# A many-row prime-slot obstruction to a positive conductor graph

**Status.** This is an elementary construction for a broad class of prime slots with freely chosen coefficients. It obstructs one positive-majorant proof strategy. It is not a counterexample to the selected large-sieve operator bound, to the detector's fixed smooth physical prime coefficients, or to any zero-free region. No priority claim is made.

## Finite matrix lemma

Let `V=(v_ip)` be any complex `M×N` matrix with `|v_ip|=1`. There are coefficients `a_p` with `|a_p|≤1` such that for at least `M/2` rows,

    |Σ_p a_p v_ip|² ≫ N²/[M log(2N)].                            (1)

The constant is absolute. Choose independent uniform phases `ζ_j` on the unit circle and put

    H_ij=Σ_p v_ip overline(v_jp),  Z_p=Σ_j ζ_j overline(v_jp).

For each i, conditioned on every other phase, `(Hζ)_i=Nζ_i+z` for some fixed z. A circle of radius N has at most one third of its normalized arc inside any disk of radius N/2; consequently `|(Hζ)_i|≥N/2` with conditional probability at least 2/3. The expected number of such rows is at least `2M/3`.

For each fixed p, the summands in Z_p are independent mean-zero complex random variables of modulus one. Hoeffding's inequality applied separately to their real and imaginary parts and a union bound imply

    max_p |Z_p| ≤ C√(M log(2N))

with probability at least `1−1/12`, for a sufficiently large absolute C. Since the number of successful rows is at most M, the expectation restricted to this event is at least `2M/3−M/12 > M/2`. Hence some phase vector has this cap and at least M/2 successful rows. Set `a_p=Z_p/[C√(M log(2N))]`. Then `|a_p|≤1` and

    Σ_p a_p v_ip = (Hζ)_i/[C√(M log(2N))],

which proves (1). This phase-averaging argument retains a positive proportion, not necessarily every prescribed row.

## Application to sextic prime slots

Work over the Eisenstein field in any fixed admissible good ray sector, and suppose the standard prime-ideal theorem in this sector and the source's sextic residue-character normalization. Fix `0<w<1`, `P=Y^w`, and `0≤σ<1`. Let the slot run over good prime ideals with `P≤Np≤2P`; its cardinality satisfies `N≍P/log P`. Choose `M=⌊P^c⌋` distinct good prime row ideals of norm in `[Y/2,Y]`, in a fixed admissible row ray class, where `0<c<1−σ`. A prime ideal theorem in that class supplies these rows because `M≪Y/log Y`.

For sufficiently large Y no slot prime divides a row prime. Thus each `v_ip=χ_{u_i}(p)` has modulus one, including all source zero masks. Applying (1) and rescaling the coefficients by `P^(−1/2)` gives a single row-independent prime-slot vector satisfying

    |a_p|≤P^(−1/2),       Σ_p |a_p|²≪1/log P,
    |Σ_p a_p χ_{u_i}(p)|² ≫ P/[M (log P)^3]                  (2)

for at least M/2 of the prescribed rows. For fixed c<1−σ, the last expression exceeds `P^σ` for all sufficiently large Y. All those rows therefore satisfy the broad amplitude-selection hypothesis with one prime slot. Fixed bad primes and fixed ray restrictions remove only a fixed or positive-density set of primes and do not alter these powers. Fix one permitted generator per row: the resulting entries still have modulus one, so the matrix lemma applies without assuming that a change of unit has a p-independent phase.

In the pair-conductor graph from [the weighted-support note](../2026-10-29-weighted-gcd-support/README.md), these rows have distinct exponent-one supports `A=u_i` of norm ≍Y, each with multiplicity one, and coprime pairs have `gcd(A,B)=1`. Hence the associated nonnegative weighted graph has off-diagonal entries ≍1 and operator norm ≫M. Equivalently, the positive square-root-conductor majorant at the balanced source length L=Y is ≫MY. Amplitude selection alone therefore cannot make this positive graph bounded independently of Y. This does not lower-bound the original signed Gram operator: cancellation between its off-diagonal character sums remains possible.

For `σ=223/500`, for example, choose fixed `w` close enough to 1 and fixed `c<1−σ=277/500` with `wc>1/2`; then the selected prime-row count is ≫`Y^(wc)` and the positive graph still grows by that power. The graph diverges for any fixed positive w and c, while the particular count exceeding `Y^(1/2)` requires w close to 1. A detector that permits only a smaller fixed mesh width, prescribes a fixed smooth profile or twist, imposes a detector-fiber condition, or otherwise restricts the coefficients needs a separate analysis. The construction does not establish that those stronger physical conditions hold.

**Independent review.** High_match checked the circle probability, Hoeffding union bound and simultaneous normalization, disjoint good-prime masks, and positive-graph and physical-slot scope; no defect was found. Amplified_opt also checked the matrix lemma and corrected the unit-choice wording.
