# Full archimedean ideal resolution and sharper radial moments

**PROPOSED unconditional component mathematics. Independent mathematical review
is required. No improved zero-free constant, fixed-principal-twist moment,
17/24 result or RH proof is asserted.**

Continuation after #959, based on its exact head
`7b845294207d96b883c1fa95028663082267804f`. Only this directory is added.
The proofs use elementary Gaussian/Hecke-character geometry and ideal counting,
not #959's imported theta/zero-density foundation. All orders are fixed.

## Results, with the different averages distinguished

Work over K=Q(sqrt(-3)). For an ideal I=(alpha), add the genuine angular Hecke
character psi_l(I)=(alpha/|alpha|)^(6l), alongside the norm twist (NI)^(it).
Every original Mobius coefficient, physical row, exclusion and nonunit zero
is retained. The four native/coupled completions from #955 are covered.

**1. An improvement for the SAME short norm-only moment.** At every fixed k,
for 1<=T<=X^(k/2), the original radial Gaussian mean satisfies

    integral g_T(t-t0) M_(2k,t)(X;w) dt
      <= C_k w(total) X^(2k) log(3X)^((k-1)^2) / T.

The preceding #955 envelope has the same power and logarithmic exponent
2k^2-2k+1. The new logarithmic exponent is smaller by k^2. At fourth order,
for 1<=T<=X, this replaces X^4 log^5 X/T by X^4 log X/T. The projection back
to angular mode zero PAYS a factor T; no unaveraged estimate is inferred.

**2. A full two-parameter diagonal-size moment at every fixed order.** Average
t with a normalized Gaussian of width R and l with the normalized discrete
Gaussian of width R, R>=1. Uniformly in the two centers,

    <M_(2k)(X;w)>_R <= C_k w(total) X^k log(3X)^((k-1)^2)
                                                   (1+X^k/R^2).

At R>=2X^(k/2), this is within relative error 600/2401 of the ACTUAL product-
IDEAL diagonal. For the scalar principal native hard window, that diagonal
has sharp order X^k log(X)^((k-1)^2). In particular the full averaged fourth
moment has order X^2 log X, rather than the norm-only diagonal's X^2 log^5 X.
The measures differ. Two widths X have total effective volume X^2, just as
one radial width X^2 does. This does not save a power of averaging volume.

**3. The entire Gaussian cumulative energy, with no discarded tails.** For
the unchanged W_c(y)=y^(-c) exp[-log(y)^2/4]/(2sqrt(pi)), let E_k(D) integrate
the 2k-th moment against dX/X^(k+1) from zero to D at the SAME row measure.
If Delta_k is its product-IDEAL diagonal, then

    |<E_k(D)>_R-Delta_k(D)|
       <= C_k w(total) (D^k/R^2) log(3+D)^((k-1)^2),
    Delta_k(D) <= C_k w(total) log(3+D)^((k-1)^2+1).

For scalar native coefficients Delta_k has that sharp logarithmic order.
At R=D^(k/2), the relative off-diagonal error is O(1/log D).

At second order there is an explicit asymptotic

    <E_1(D)>_(R=sqrt(D)) ~ kappa_c delta_S log D,
    kappa_c=exp((2c-1)^2/2)/(2sqrt(2pi)),
    delta_S=Res(zeta_K,1)/zeta_K(2) product_(p in S)(1+1/Np)^(-1).

The absolute error from the exact ideal diagonal is O(1). The coupled scalar
source has its own explicit positive density and the same one-log result.
These replace the earlier norm-fiber log-squared mean by a geometrically
resolved one-log mean, under the stated extra angular average.

## Mechanism and significance

Norm twists cannot distinguish two different ideals with the same norm.
Norm and angle together distinguish their generators up to the six units.
A nonzero difference of two Eisenstein generators has norm at least one.
The exact Gaussian kernel turns that lattice gap into a Schur near-isometry.
Its arithmetic diagonal uses ideal equality, so the classical transport count
has only (k-1)^2 logarithmic dimensions; norm equality instead sees the
additional norm-fiber factors. This is full-moment mathematics, not a selected
singleton sector or an independent-prime model.

Classical hybrid large-sieve geometry, Gaussian Poisson summation and matching
counts are credited. No claim of global novelty is made. Even bounded arbitrary
ideal coefficients satisfy the analogous averaged theorem: the gain is a
resolution theorem, not previously missing Mobius-specific cancellation.

## Boundary and reading order

Read PROOF.md for Theorems A and D, exact family/measure, the 600/2401 constant,
sharp lower order and uniform-center volume obstruction. Read
GAUSSIAN_ENERGY.md for Theorems B and C and all infinite-tail arguments.
LATEST_REVIEW.md records the bounded review of #959 and the failed inference
from finite-order to angular twists. SOURCES.md separates full source reads,
abstract-only inspiration, classical inputs and failed fresh accesses.
VALIDATION.md states every executed test and its limits.

No extraction of t=l=0 from the hybrid average is proved. Adversarial norm
centers already force a lower bound X^(2k)/R^2 even for native coefficients.
Those centers are not the principal center. The old fixed-center signed
covariance remains open. Main and the integrated scientific record are unchanged.
