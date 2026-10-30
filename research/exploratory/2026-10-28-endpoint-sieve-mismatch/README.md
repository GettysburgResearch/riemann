# Why a full sextic-sieve lower bound does not decide a selected endpoint

**Status:** Exact finite countermodel to a proposed inference. It is not a counterexample to the actual sextic-character estimate and proves no zero-free region.

**Sources:** Xu and Sang, [arXiv:2610.17675v2](https://arxiv.org/abs/2610.17675), Theorem 1.1, claim that the full squarefree sextic sieve norm at balanced cutoffs `Q,Q` is at least `Q^(7/6-epsilon)`. Their statement relies on the cited analytic inputs. The selected-norm contract in [tracker PR #93](https://github.com/GTimG/QuasiRiemannTracker/pull/93), head `70c4d642c4c6263a09bf0f3930a74e2aa7c99f00`, is in `src/Candidate/Local/Qrh/JointDetector/FineNaturalSelectedNormContract.lean` and uses a high-response selection of rows. Neither input has been independently verified here.

At `Y=L=Q`, the proposed endpoint form `Z^epsilon (L+sqrt(YL))` is of scale `Q^(1+epsilon)` if `Z` is a fixed power of `Q`. This is smaller than the quoted **full** norm. But the endpoint estimate concerns only the rows selected by a separately specified slot polynomial, whereas Xu–Sang's lower bound concerns the full matrix. A lower-bound witness supported on rows removed by selection is irrelevant to the selected norm. The following model proves that this distinction can be as large as a power of the dimension, even with unit-modulus matrix entries and a normalized slot vector.

## Exact model

For each `N=2^m` with `m>=1`, let `H` be the real Sylvester Hadamard matrix, so its `N` rows have entries `±1`, are mutually orthogonal, and each has squared Euclidean norm `N`. Let `h0` be its all-ones row and let `h1,...,h_(N/2)` be distinct nonconstant rows. Construct an `N`-by-`N` row-by-column matrix `M` whose first `N/2` rows equal `h0` and whose remaining rows are `h1,...,h_(N/2)`.

Define the slot coefficients `a=h1/sqrt(N)`, so `sum_j |a_j|^2=1`. For a row `r` write `P(r)=sum_j M[r,j] a_j`, and retain exactly the rows satisfying

    |P(r)|^2 >= N^(1/2).

This is the formal numerical analogue of a single width-one slot at amplitude parameter `delta=1/2`; in particular the threshold is on **squared** amplitude. Orthogonality gives `P(r)=sqrt(N)` for the single row `h1` and `P(r)=0` for all other rows. Thus the selected matrix consists of just `h1`, and its squared operator norm is exactly `N`.

For the full matrix, test its operator on the unit vector `h0/sqrt(N)`. Each of the first `N/2` output coordinates equals `sqrt(N)`, and every other output coordinate is zero. Therefore

    ||M||^2 >= N^2/2,       ||M_selected||^2 = N.

The same conclusion holds with a fixed cutoff or mask that retains `h1` and removes the duplicate rows. Both matrices use the identical column set; the slot coefficients have unit squared mass. There is no rounding or limiting step in the argument.

## What remains

This is a synthetic matrix, not an Eisenstein sextic residue-character matrix; in particular it does not respect the number-theoretic factorization or coprimality constraints of the cited theorem. It shows only that the **full-norm lower bound by itself** cannot refute the selected endpoint bound. A genuine obstruction would need a large-norm sextic witness whose row support is proved to satisfy the *same fixed slot polynomials*, widths, masks, and amplitude inequalities, with the quantifier order and allowable `Z`-loss preserved. Conversely, the absence of such a witness does not prove the endpoint estimate.

**What was run:** exact symbolic construction and the Hadamard orthogonality identity; no arithmetic large-sieve computation or independent proof of either preprint.

## A separate threshold discontinuity at `delta=1/2`

The strict-gap estimates alone also do not imply their endpoint by taking a limit. Fix any integer `t>=1`; for every positive integer `q`, let `Z=N=2^(2tq)`, `k=2^q`, and take the `N`-by-`N` all-ones matrix. Give the rows abstract size `Y=N` and let the ordinary source cutoff be `L=N`. There are `t` slots, each of width `w=1/t`; the support of each slot is the first `k` columns and its coefficients there are all `1/sqrt(k)`. Thus every slot has squared coefficient mass one and `k=Z^(w/2)<=Z^w` support columns. On every row every slot polynomial has squared amplitude exactly `k=Z^(w/2)`. Their product is exactly `Z^(1/2)` because the total width is one.

The aggregate selection at `delta=1/2` therefore retains **all** rows, while every fixed `delta>1/2` retains **none**. The selected squared operator norm at the endpoint is `N^2`. A hypothetical bound `C Z^epsilon (L+sqrt(YL))` would equal `2 C N^(1+epsilon)`, and fails along this sequence for every fixed `C` and `epsilon<1`. Taking `t` arbitrarily large makes the slot width smaller than any prescribed fixed positive mesh. Thus neither a limit of strict-gap selection bounds nor early-mesh quantifiers by themselves establish the endpoint.

Again, this is an abstract unit-entry matrix with abstract source sizes, not an actual sextic character matrix. In particular, we have not realized the all-ones matrix with admissible physical Eisenstein rows and ideal sources. It is a logical countermodel showing why a genuinely arithmetic input is required; it does not disprove the actual selected estimate.
