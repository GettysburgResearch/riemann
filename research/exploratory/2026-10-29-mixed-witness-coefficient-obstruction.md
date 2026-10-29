# Prime-pair coefficient mass in a Möbius–ordinary witness

This is an unconditional coefficient-norm lower bound in a fixed number field. It does not lower-bound a character-family row moment, show that an actual zero realizes the relaxed witness, or rule out cancellation between different columns after the character sum is formed.

Fix t>0 and put `r=2t/3`, `m=t/3`, `D=X^r`, `N=X^m`, so D=N² and both tend to infinity. Let W₁,W₂ be fixed nonzero continuous compact-annular profiles. For β in a fixed compact real interval and arbitrary real h₁,h₂, consider the centrally normalized coefficient sequences

    a_l = D^(−1/2) μ_K(l) W₁(Nl/D) (Nl/D)^(−β−ih₁),
    b_k = N^(−1/2)       W₂(Nk/N) (Nk/N)^(−β−ih₂).

For any multiplicative character χ with its original zero extension, the exact product has ideal-index coefficients

    M_r(χ) S_m(χ) = Σ_j c_j χ(j),    c_j=Σ_{l k=j} a_l b_k.  (1)

There are fixed positive-width intervals I₁,I₂ on which respectively `|W₁|≥c₁>0` and `|W₂|≥c₂>0`. Restrict l and k to good prime ideals with norms in D I₁ and N I₂, respectively. These primes are distinct for sufficiently large X. Their product j=l k is squarefree, and unique factorization of ideals gives exactly four divisors 1,l,k,lk. Because D/N→∞ and N→∞, only l can lie in the fixed D-annulus while its complementary factor lies in the fixed N-annulus. Thus there is no cancellation in this particular convolution coefficient:

    c_(lk)=−(DN)^(−1/2) W₁(Nl/D)W₂(Nk/N)
                 ·(Nl/D)^(−β−ih₁)(Nk/N)^(−β−ih₂).          (2)

The prime ideal theorem gives ≫D/log D and ≫N/log N choices of l and k in the two selected intervals. Each ordered pair produces a distinct ideal j. Fixed bad primes or fixed ray-class restrictions with positive prime density cost only constants. Even a common coprimality mask supported on an ideal R with `NR≤X^C` removes at most O_C(1) prime ideals from each selected positive-power annulus, because each such divisor has norm ≫X^m. The phases in (2) have modulus one, and bounded β and the fixed annuli give a uniform positive lower bound for the remaining norm factors. Consequently

    Σ_{j squarefree} |c_j|² ≫ 1/[(log D)(log N)].             (3)

The implied constant depends on K, S, W₁,W₂, the fixed β interval and the chosen nonempty ray sectors, but is uniform in h₁,h₂ and in X. The same conclusion holds if the coefficient sequences are multiplied by fixed unit-modulus character factors. In the detector's cutoff profile `W₁(y)V≤(D y/X^t)`, the cutoff is identically 1 on the fixed annulus for all sufficiently large X because r<t, so it does not change the lower bound.

Thus no estimate of the form `Σ_{j squarefree}|c_j|²≪X^(−η)` with fixed η>0 can follow for this mixed coefficient vector merely by retaining its exact Möbius convolution. Any such saving would contradict the prime-pair terms. This does **not** preclude a smaller norm on a particular row subset, cancellation in the subsequent character sum, a genuinely arithmetic mixed-moment estimate, or a detector that avoids this witness configuration. If either profile is allowed to shrink with X or to vanish on all admissible primes, the uniform lower bound must be reconsidered.

## What the diagonal of a natural-row average shows

Let the outer family consist of all good n-free FHL labels u with Nu≤X, with fixed n≥3 and the usual original zero extensions. Expanding the nonnegative row moment gives the exact diagonal expression

    Diag = Σ_j |c_j|² Σ_{u good n-free; Nu≤X} |χ_u(j)|².

For every selected prime pair j=lk in (2), the inner factor equals the number of rows coprime to lk. The good squarefree labels alone have cardinality ≫X, while the numbers divisible by l or k are respectively `≪X/Nl` and `≪X/Nk` by fixed-field ideal counting (and are zero if the prime norm exceeds X). These losses are o(X) uniformly for the chosen positive-power annuli. Hence

    Diag ≫ X/[(log D)(log N)].                              (4)

This verifies a non-negligible diagonal for the *actual* natural family, even with the Möbius convolution and the original masks. It does **not** lower-bound the whole moment: the real offdiagonal sum can have either sign and can cancel part of the diagonal. For a concrete abstract model, take a unit vector v with N equal coordinates and the positive semidefinite Gram matrix `G=I−vv*`. Its diagonal entries all equal `1−1/N`, yet `v*Gv=0`. Thus positive diagonals and a positive semidefinite total quadratic form do not by themselves rule out exact cancellation for one distinguished coefficient vector. A real saving or lower bound for the actual character matrix needs additional arithmetic control of the offdiagonal; the model does not assert that the sextic matrix has this null vector.

**Independent review.** Families checked the normalization, prime-pair uniqueness, polynomial-norm common masks, uniformity in β and the frequencies, and the distinction from a row-moment lower bound.
