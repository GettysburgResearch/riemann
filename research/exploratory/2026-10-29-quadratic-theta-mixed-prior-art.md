# Mixed quadratic Möbius prefix and cubic theta: source search

**Status.** A targeted, nonexhaustive literature comparison at the actual local bottleneck. No new mixed estimate or individual zero-free region is proved.

The row scale and cube prefix scale are `B=Y^(10283/11000)`, `H=Y^(579/5500)`, and the completed theta scale is `Z=Y^(4093/5500)`, with F=K=G=1. The genuinely desired joint moment has form

    Σ_(b sixth-free, Nb≈B) |A_b(H) T_b(Z)|²,
    A_b(H)=Σ_(Nc≤H) μ(c) ᾱ(c)^3 ξ(c)^3 χ_c(b)^3,

including the fixed bad/ray sectors and source zero masks. In [the eighth/tenth bottleneck analysis](2026-10-29-eighth-holder-tail/BOTTLENECK.md), the active Hölder inequalities bound it at exponent `28373/22000=1.2896818...` in base Y, before the exterior `H^(−2)` and physical prefactor. A useful input must save a fixed power **uniformly for the actual shared b row**, profiles, derivatives and mask variants. Separate estimates for A and T do not by themselves provide the necessary arithmetic decorrelation.

## Exact source matches and mismatches

* [OpenAI October 5 manuscript, Proposition R and cube inversion](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), states the completed-theta mean `Σ_b|T_b(Z)|²≪B+B²/Z` (with fixed source and profile data) and the precise μ-weighted quadratic prefix obtained by cube removal. It does not state the needed mixed quadratic-prefix × completed-theta moment. Its transformation turns the completed theta into a quadratic-twisted dual theta sum, but applying its quadratic large sieve after independently expanding the prefix does not automatically keep the two factors in a single common coefficient vector.
* [David–de Faveri–Dunn–Stucky, arXiv:2410.03048v2](https://arxiv.org/abs/2410.03048v2), treats mollified central moments of **cubic** Hecke L-functions for squarefree Eisenstein character labels. Its Proposition 1.4 bounds a cubic-family mollified remainder and Remark 1.9 permits the stated second-moment asymptotic through mollifier length below `Q^(1/6)`. Their §6 cubic Gauss Dirichlet-series mean is a useful source for a different, one-parameter cubic Gauss average. Neither statement is the above mixed second moment of a *quadratic* angular Möbius prefix and sextically twisted completed theta over the same b labels; it cannot be substituted without a new reciprocity and kernel argument.
* [Liu, arXiv:2610.26835v1, Theorem 12.14 and Remark 12.16](https://arxiv.org/html/2610.26835v1#S12.Thmtheorem14), gives product estimates for a prescribed sextic family over fields containing μ₁₂; its z=0 ordinary fourth-moment case concerns two plain factors. Its displayed factors and finite masks are not the explicit metaplectic theta coefficient or the moving quadratic character on the same b-row above. It does not directly supply this joint moment. Its source and preprint proof are not independently checked here.
* [David–Dunn–Hamieh–Lin, arXiv:2306.11875v5](https://arxiv.org/abs/2306.11875v5), uses quartic Gauss sums and quadratic reciprocity over Q(i), with specific Type-I/II coefficients and ranges. It is a different field, metaplectic representation and kernel, so no bound for this sextic/cubic coupled moment follows merely by analogy.

No directly applicable mixed estimate with the needed power saving was located in this targeted search. This is not a claim that such a result does not exist.

## A quantitative generic benchmark

Consider only the squarefree-index subpiece of the completed theta sum (the q=1 term in the source expansion), and absorb the common phases in coefficients. Multiplicativity and the exact shared-prime zero masks give

    χ_n(b)χ_c(b)^3=χ_(n c³)(b)

for n,c squarefree. Each product `n c³` is sixth-free (prime exponents are 0,1,3,4), and the two exponents determine n,c uniquely. Its norm is at most `Z H³=Y^(53/50)`; the squared coefficient mass is `≪H Y^ε` for a centrally normalized n-block. The generic de Faveri Θ₆ bound then has exponent

    H · max{B, ZH³, B^(5/6)(ZH³)^(1/3),
                          B^(1/3)(ZH³)^(5/6)}
      = Y^[42907/33000+ε].

This is weaker than the above full Hölder exponent by `139/13200≈0.01053` even before accounting for the additional q³ terms in the completed source. The calculation neither bounds the full theta moment nor rules out cancellation in its actual coefficients. It shows that simple coefficient collapse followed by this arbitrary-coefficient sieve does not close the specified bottleneck.
