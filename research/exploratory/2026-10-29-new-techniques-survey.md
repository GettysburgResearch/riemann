# Recent techniques and the remaining selected-row gap

**Status, 29 October 2026.** A targeted survey and source comparison, not an independent proof of any cited preprint. Tracker data were checked through the public GitHub API; search results need not be exhaustive.

## Current benchmark

The [QuasiRiemannTracker pull requests](https://github.com/GTimG/QuasiRiemannTracker/pulls?q=is%3Apr) have no PR newer than #94 at this check. [PR 94](https://github.com/GTimG/QuasiRiemannTracker/pull/94), merged at 07:51:58 UTC, states `Re(s)>0.87387234` for all Dirichlet L-functions. Its reported CI checks passed; this observation does not independently audit the mathematical-to-Lean interface. A proposed threshold `0.8738702` in this workspace is an unsubmitted, conditional candidate and must not be treated as a new proved benchmark.

## Structured sixth-order estimates

[de Faveri, *Optimal large sieve for fixed order characters*, Theorem 1.1](https://arxiv.org/abs/2610.04045v1) states, under its fixed-field and fixed-prime-set hypotheses, a sixth-order squared operator bound

```text
(AB)^epsilon (A+B+A^(5/6) B^(1/3)+A^(1/3) B^(5/6))
```

for sixth-power-free indices on both sides. It is uniform in the coefficient vector. At balance this is `Q^(7/6+epsilon)`. [Xu and Sang, *A matching lower bound for the sextic large sieve and structured prime moments*, v2, Theorem 1.1](https://arxiv.org/abs/2610.17675v2) claim this power is optimal even with squarefree rows and columns. Their all-range lower bound imports the cited OpenAI unmarked moment; the v1-based Appendix A is independent of that moment but has a restricted parameter range and only the weaker `Q^(17/16)` balanced lower exponent.

Their Theorem 1.2 and Proposition 7.2 instead control a **specified structured vector**, not the full operator norm. In the Eisenstein field, fix `c>0`, a maximum number `k0`, and an annular product of at most `k0` independently smooth prime factors, with every participating prime norm at least `Y^c`, total product scale comparable to `Y`, and every fixed derivative bounded by a fixed power of `log Y`. Write `beta(b)` for the resulting prime-convolution coefficient after squarefree projection. They state

```text
sum_(u sixth-power-free, Nu ~ Y) |sum_b beta(b) (u/b)_6|^2
    << Y^(kappa+epsilon) + Y^(13/6-c+epsilon),
kappa = (37-10 sqrt(6))/6 = 2.084183762... .
```

This saves any fixed power below `min(13/6-kappa,c)` against the generic `Y^(13/6+epsilon)` comparison. Their density and structured-vector branch imports both the OpenAI unmarked inverse moment and buffered detector. This result permits independently specified smooth factors but does **not** permit arbitrary source coefficients depending on the selected rows, nor assert a selected-row operator norm.

[rStation Paper 52, current version 5](https://rstation.ai/problems/riemann_hypothesis/papers/52), claims a different index-ordered cubic density improvement, using a fixed-order inverse identity, Burgess bounds, a Gram estimate and an ordinary fourth moment. At `sigma=5/6` its cube-free index exponent is `3/5+epsilon`, at heights up to a sufficiently small power of the index scale and for fixed finite twists. A separate [audit of a conductor-ordering consequence](2026-10-29-cubic-conductor-density-review.md) yields exponent `9/10+epsilon` for sufficiently small power heights if the source result is accepted. Neither the source result nor its analytic imports were independently verified here. The same audit derives a more general-field consequence of de Faveri's Corollary 1.5, with a weaker exponent but explicit arbitrary-height dependence.

## Distinct proof methods and scope

[Frei and Kai, *Exceptional zeros of Hecke L-functions*, v1](https://hexagonmath.org/2610.00466v1), develops a short fixed-base-field analogue of Kerr's Masser-polynomial approach, using small generators of quadratic extensions. The claimed conclusion is an effective but non-explicit field-dependent zero repulsion for real Hecke characters, not a fixed zero-free half-plane or a result uniform over fields. **Theorem 1.1 is false as literally printed:** it includes the trivial Hecke character with `Nq=1` and every `beta` in `(0,1)`. For known quaternion fields, `zeta_K(1/2)=0`; see the cited discussion of Fröhlich's construction in [Central values of zeta functions of non-Galois cubic fields, Introduction](https://research.chalmers.se/publication/548729/file/548729_Fulltext.pdf). The inequality would then demand `0 >= epsilon_K > 0`. Section 3 incorrectly disposes of the trivial character using only nonvanishing at `s=1`. The proof's large-conductor step, Lemma 5.4, explicitly assumes sufficiently large `Nq`; its Section 6.1 also prints the stronger assumption `(1-beta)Nq<epsilon` in place of the logarithmic assumption in the theorem. A replacement such as `log(2Nq)` might repair the small-conductor defect, but the corrected proposition and proof have not been audited here.

[Winarski, *A 15/16 zero-free half-plane for angular Hecke L-functions over the Eisenstein field*](https://hexagonmath.org/2610.00458v1) claims a frozen Lean result including all unit-compatible angular types and real norm twists. The manuscript describes verification evidence and explicitly disclaims independent human certification. Its threshold is numerically weaker than the `7/8` claim for unitary Weil L-functions in [Hu](https://hexagonmath.org/2610.00216v1); the respective formal and mathematical dependencies have not been compared here. Neither gives a stronger Dirichlet numeric threshold than PR 94.

## Concrete attack: prime-selected Gram bounds

The proposed [long-source seed and its audit](2026-10-29-long-source-seed/audit.md) isolate a possible new analytic input. Let `F` be a squarefree row family of norm about `B` selected by literal prime slots, with aggregate selection slope near `sigma=223/500`. For arbitrary source coefficients `b_n` supported on ideals of norm at most `L`, the seed would require, in particular at `L=B`,

```text
sum_(u in F) |sum_(Nn<=B) b_n chi_n(u)|^2
    << B^(1+epsilon) sum_(Nn<=B) |b_n|^2.
```

This asks for a `B^(1/6)` saving over the full balanced operator bound. Xu–Sang's structured-vector result cannot be substituted for this estimate: the vector here is arbitrary and the primal/dual masks must remain uniform. Their matching lower bound also does not disprove it, because their extremizing rows are not shown to meet the prime-slot test. If the slot class is broadened from literal primes to arbitrary sixth powers, the seed is false at slopes at most `1/6`; the linked audit gives an explicit rank-one construction. That construction does not settle the prime-only slope near `0.446`.

One concrete route is to prove a mixed Gram or trace estimate conditioned on the prime response, rather than estimating the selected-row count alone. Under a pointwise `P^(-1/2)` coefficient condition on a prime slot of scale `P=B^w`, the linked audit derives from de Faveri's asserted inequality a fixed-moment row count with a saving exceeding `1/6` for sufficiently small mesh. However, this count by itself yields only the inadequate Hilbert–Schmidt bound `|F|B`. The missing estimate must show that the exceptional singular directions responsible for `B^(7/6)` cannot concentrate on these large-prime-response rows, uniformly in all source vectors, admissible moving masks, slot profiles and scales. This is a precise open target, not a proved route to an improved zero-free region.

Even a substantial better selected bound must be incorporated into the rest of the detector and return calculation. The [exact scalar obstruction](2026-10-29-return-obstruction/README.md) shows that, with its stated fixed PR 94 five-branch formulas and parameter slice, improving the slot capacity alone cannot reach `0.87287234`; the numerator capacity or another source inequality must also change. This is a statement about that specified relaxation, not a universal barrier.
