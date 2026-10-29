# Cubic mixed source moments and the scalar detector

**Result.** The displayed generic positive-moment consequences of [rStation paper 52 v5, Corollary 3.10 and Theorem 3.11](https://rstation.ai/problems/riemann_hypothesis/papers/52/v5), combined with the simultaneous inverse/ordinary detector alone, do not improve its published natural-row Theorem 5.7 by cutoff optimization. This is an exact statement about a relaxed scalar mechanism, not a lower bound for actual characters or zeros. The preprint and detector are treated as source inputs, not independently established here.

Work over the fixed Eisenstein family with principal finite background, its original masks, and nonprincipal inducing rows for the ordinary fourth and N2 moments. Let `δ=2σ−1∈(0,1)`. The source inverse moment N1, ordinary fourth, the one-ordinary product N2, and the mixed product M1 of Theorem 3.11 have length exponents

    I(r) = max{1,1/3+r} − δr,
    P(m) = 1 − 2δm,
    J(r,m) = max{1,2/3+r} − δ(r+m),
    K(r,m) = max{1,1/3+r+m} − δ(r+m).                          (1)

The detector supplies simultaneous saturated factors with `0≤r≤t`, `0≤m≤1/2`, `r+m≥t`, up to small losses. Each envelope is applicable only with the source's fixed common profiles, masks, frequency and height controls. The displayed positive estimates allow the smaller of (1); optimizing over actual character correlations could be stronger, but is not part of this calculation.

Put

    r*=4/[3(3−δ)],  m*=r*/2,
    R=1−δr*=(9−7δ)/(9−3δ).                                     (2)

The last expression is precisely paper 52 v5 Theorem 5.7's `D(σ)`. For every fixed detector cutoff `1/2≤t≤3/2`, there is an admissible pair at which **all four** envelopes in (1) are at least R:

* If `t≤r*`, take `r=m=t/2`. Then r≤1/3, r+m=t≤2/3, and `P=J=K=1−δt≥R`; also `I=1−δt/2≥R`.
* If `r*≤t≤3r*/2`, take `(r,m)=(r*,m*)`. The inverse, ordinary and M1 mixed envelopes all equal R. The N2 envelope is larger by `(1−δ)/[3(3−δ)]`.
* If `t≥3r*/2`, take `(r,m)=(t,0)`. Since `t≥3r*/2>2/3`, `I=K=1/3+(1−δ)t≥R`, `J≥K`, and `P=1≥R`.

All stated pairs satisfy `r≤t`, `m≤1/2` and `r+m≥t`; the `O(ε)` detector losses do not alter the limiting lower bound. The source's published Theorem 5.7 gives the matching upper density exponent by a different argument. Therefore these four scalar envelopes cannot produce a strict improvement simply by selecting another cutoff or combining their already displayed numerical bounds.

This does not rule out a better estimate using special Möbius cancellation, more refined joint moments, the source's exact inverse factorization, different character subfamilies, or stronger constraints on realizable detector witnesses. In particular, the lower-envelope witnesses above are hypothetical scalar pairs and do not assert the existence of any character attaining both large values.
