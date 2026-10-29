# Aggregating the moving divisor after the second Poisson transformation

**Status.** A source-qualified partial bound for the [61/72 dual correlation](2026-10-29-61-72-dual-correlation/README.md), conditional on the Poisson/phase/fibre identities and the all-row inverse estimate (10.2) in [rStation paper 5 v3](https://rstation.ai/problems/riemann_hypothesis/papers/5/v3). Those substantial imported inputs are not independently proved here. The range `Nd<Y^(1/5)` remains open, so this is not a new inverse moment or zero-free region. Independent review requested.

Use `P=Y^(6/5)` and the fixed-sector conventions of the [low-dual note](2026-10-29-low-dual-theta-bound.md). Let `Nd≈D₀`, `Nk≈K` with good squarefree `k|d`, and let `Ng≈G` be the auxiliary squarefree projector dyad. Fix `d′=d/k`, its ray class, the finite ray classes needed for k and g, and the logarithmic Fourier modes of all smooth kernels. The residual theta column length is `D≈P/(D₀G)`, while the original dual row v has length H. Its square polynomial is

    S_(v,g,k)=Σ_(n good sf, (n,d′)=1)
      C_{−1}(n)ν(n) χ_n(v)χ_n(g)^4χ_n(k)^5 U(Nn/D)/sqrt(Nn). (1)

All zero extensions are literal: `χ_n(k)^5` itself enforces the missing `(n,k)=1`. The outer constraints `(k,d′)=(g,kd′)=1` can be discarded only after a nonnegative square and Cauchy. The original common-g row mask is likewise discarded at that point. Separating the physical kernel before this Cauchy produces common profiles and row/label phases of modulus one; fixed ray sectors cost only a constant.

Apply paper 5 §10.2–§10.3, now taking v, not vk, as its original row and g as its label. The extra `χ_n(k)^5` is multiplicative. Upon the source's common-divisor extraction `n=s a`, its common factor becomes the bounded outer mask `|χ_s(k)|²`; its residual factor `χ_a(k)^5` stays inside the inverse polynomial. For the new Poisson frequency r one has the exact identity, including zeros,

    χ_a(k)^5 overline(χ_a(r)) = overline(χ_a(kr)).          (2)

The output inverse-row ideal t=kr therefore satisfies `Nt≲K R₀`, where `R₀=D²G²/H` up to a small tail loss. The fixed puncture in the residual inverse polynomial is `Q=d′s`, since (2) retains the k zero mask. The cited source's complete coprime projector, finite-ray phase expansion and divisor-weighted Cauchy are performed before enlarging this positive t-sum. Its frequency-fibre bound (10.9), together with `k|t`, gives only `τ_K(t)^{O(1)}` possible representations, absorbed in an arbitrarily small power. It is crucial that this is a count for fixed **t**, so no extra factor K is inserted. For fixed d′, source internal divisor dyads and Fourier modes, the inverse coefficient and norm profile are independent of k after (2); finite-seminorm losses are integrated against the source's rapidly decaying Fourier measure.

The nonzero-frequency contribution for this fixed d′ is therefore bounded by

    (H/D)(YD₀KGH)^ε [K R₀ + (K R₀)^(1/6) D^(5/6)].       (3)

This is paper 5 (10.10) with its normalized label sum multiplied by G, summed over k through t=kr, and the all-row inverse input (10.2), including the allowed puncture `d′s`. The original theta diagonal costs `≪K G H (YD₀KGH)^ε`; principal-frequency restoration and the rapidly decaying tail are treated separately by the cited source. These bounds are for the sum of positive squares after kernel separation, and thus control the corresponding signed physical piece by Cauchy.

The physical outer factor is `(Y/P)/(GK)`, and there are `≪(D₀/K)^(1+ε)` possible d′. The nonnegligible physical frequencies have `H≤H₀=Y^ε P²K/(Y D₀²)`. The expression in (3), after multiplication by the physical outer factor, is nondecreasing in H; on putting H=H₀ one has `K R₀=Y` up to small powers. The entire localized dyad is bounded by

    ≪ Y^ε [ P/D₀ + Y/K + (Y^(1/6)/K)(P/(D₀G))^(5/6) ].   (4)

Thus if `D₀≥Y^(1/5)` all three terms are `O(Y^(1+ε))`, uniformly over the feasible good K,G dyads. Fixed bad-prime divisors form finitely many harmless sectors. For `D₀≤Y^(7/10)` the artificial principal residual pair `r₁=r₂=1` lies outside the residual column support; the generic source sieve already covers the complementary larger-gcd range, as in the low-dual note. Summing the logarithmically many dyads gives source-qualified `O(Y^(1+ε))` control of the entire portion with original common gcd `Nd≥Y^(1/5)`.

The remaining `Nd<Y^(1/5)` includes d=k=1. In particular, the first term in (4) is as large as `P=Y^(6/5)` there. The argument has used positivity and discarded coupled masks, and provides no cancellation between those parts. The asserted partial bound relies on the source theorem and the stated aggregation and does not bound the full all-row moment.
