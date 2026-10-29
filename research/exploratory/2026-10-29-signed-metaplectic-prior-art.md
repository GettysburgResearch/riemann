# Signed metaplectic estimates near the long-dual target

This targeted source comparison does not prove a new signed estimate. The required `D^(5/36)` saving and the separated off-diagonal target `Z_off,D(5/6+η+it)≪D^(1/36+ε)(1+|t|)^A` are derived, with masks and the additional physical-kernel bridge, in [the Mellin-gap note](2026-10-29-signed-theta-mellin-gap.md). The target's dual row and column norms are `H=D^(7/6)` and D. The actual physical sum is signed and coupled; estimates for a fixed-profile positive model are not automatically equivalent to it.

## Cubic cusp forms

[Dunn, *Metaplectic cusp forms and the large sieve*, Theorem 1.5](https://arxiv.org/abs/2403.13151v4), proves a Type-II bound for Fourier coefficients of a **fixed cubic metaplectic cusp form** on his specified lowest-level group. For squarefree α supported at `Na≈A`, arbitrary β at `Nb≈B`, `X≈AB`, fixed ray-congruence data v,u and smoothness parameter K, its bound is

    |B_f(α,β)| ≪_{ε,f} (XK Nv)^ε K⁸(Nv)⁴
                       [(AB)^(1/2)+A^(3/2)B^(1/4)]
                       ||μ²α||_∞ ||β||₂.

The paper identifies its nontrivial Type-II range as `B≫X^(2/3+ε)` with bounded α. At the endpoint of our putative cubic/quadratic decomposition, `X=HD=D^(13/6)`, and even the larger side H is `X^(7/13)<X^(2/3)`. Moreover the source kernel is a fixed cuspidal coefficient at ab: it does not state a bound for the residual cubic theta family with a moving, same-row quadratic character χ_n(v)³, nor a uniform moving-level version adequate for the physical mask. Thus it is a useful circle-method/Voronoi model, not the requested signed estimate.

## A quartic cancellation mechanism and its exact limitation

[David–Dunn–Hamieh–Lin, *Quartic Gauss sums over primes*, §§1 and 7](https://arxiv.org/abs/2306.11875v5), use the CRT identity for their **quartic** normalized Gauss sums over Q(i): up to explicit ray phases, `g₄(ab)=g₄(a)g₄(b)(a/b)₂` on their coprime squarefree support. The fixed one-variable Gauss factors may be absorbed into common coefficient sequences, leaving an ordinary quadratic residue kernel. The quadratic large sieve then gives the source's `X^(5/6+ε)` Type-II bottleneck in its stated balanced interval. Their Type-I part additionally uses the specific quartic theta coefficient at squares and treats its pole separately.

In the present Q(ω) sextic problem, factoring `χ₆,n(v)=χ₆,n(v)^4χ₆,n(v)^3` absorbs the cubic part into a cubic Gauss coefficient, but **the quadratic factor still depends on the same pair (n,v)**. Its accompanying θ coefficient and reciprocal-sieve weights do not become the fixed independent coefficient sequences of the quartic theorem. A separate complete formula or spectral decomposition for this coupled kernel, including the original nonunit masks, is needed; simply applying the quartic theorem would change both the field and the arithmetic kernel. See [the mixed-cubic–quadratic calculation](2026-10-29-mixed-cubic-quadratic-gap.md) for the quantified loss from making an independent quadratic-row copy.

## First moments and quotient L-values

[Mohammad H. Hamdar, arXiv:2509.06152v2](https://arxiv.org/abs/2509.06152v2), computes the first moment of **cubic** Hecke L-functions over Q(ω) away from the central line. It exploits a cancellation at s=1/3 between a principal contribution and residues of cubic Gauss Dirichlet series; it also uses a cubic L² average and Kubota–Patterson theta coefficients. Its family is a one-parameter cubic family, not the two-index signed sextic ratio-character sum in the Mellin gap. Its cancellation therefore cannot be transferred to that sum without a new identity preserving both moving indices and masks.

In particular, even an ideal positive mean-square bound for the quotient characters of the form `Σ_(n,m≈D) |L(5/6+η+it,ξ*_{n,m})|² ≪ D^(2+ε)(1+|t|)^A`, with the correct finite masks, gives only `Z_off,D≪D^(1+ε)(1+|t|)^A` by Cauchy, because `Σ_(n,m)|b_n b_m|²≪1`. This hypothetical calculation does not assert such a moment theorem; it shows why an unsigned L² average alone does not yield the much smaller D^(1/36) sufficient target. Even individual Lindelöf-strength bounds followed by absolute summation produce the same D-scale because `Σ_n|b_n|≈D^(1/2)` for typical nonzero annular weights.

The moving-level cubic Gauss estimates and the available higher-order averages are compared in the linked gap notes. None of the cited statements was found to deliver the required signed power saving while simultaneously retaining the moving quadratic twist, theta residual, finite ray phases and coupled physical profiles. This is a targeted, nonexhaustive search, not a claim that such an estimate cannot exist.
