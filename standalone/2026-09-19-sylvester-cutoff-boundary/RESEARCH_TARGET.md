# Proposed arithmetic-cutoff covariance target

## Existing consumer

PR #848 has reduced one version of the all-scale problem to controlling the native distinct-product covariance after exact coalescing. The present packet does not replace that target.

The proposed change is **where the covariance is decomposed**.

Instead of starting from product coefficients (z(d)=(c*c)(d)) and immediately bounding
[
sum_{d
e e} z(d)z(e)langle kappa_d,kappa_eangle,
]
first expand the native (z(d)) through the cutoff-boundary representation inherited from Möbius inversion.

## Boundary classes

For a chosen least-prime assignment, classify a boundary atom by
[
eta=(ell,d),qquad Y/ell<dle Y,qquad ell=P^-(n), dmid n/ell^{v_ell(n)}.
]

Natural exact invariants for a pair (eta,eta'):
- (ell=ell') or not;
- (g=gcd(d,d'));
- (L=operatorname{lcm}(d,d'));
- overlap of multiplicative boundary windows;
- parity (mu(d)mu(d'));
- whether the corresponding product fibres coalesce to the same (z(r));
- shared-prime count outside (ell,ell').

The first candidate theorem should be a signed **block** inequality over one such class, not pairwise negativity.

## Target shape A: summably small positive excess

Find an exact partition (mathcal P_Y) of boundary-atom pairs such that
[
C_Y=sum_{Binmathcal P_Y} C_Y(B)
]
and prove
[
sum_{B} C_Y(B)_+
le
(log Y)^A,F_Y^{1-eta_Y},
]
or another bound that feeds the established #848 subquadratic recursion with a nonsummable cumulative gain.

The exponent/gain must be stated in the coordinates already consumed by #848; no new surrogate criterion should be introduced.

## Target shape B: negative main blocks + controlled exceptional geometry

A potentially more realistic form is:
[
C_Y
=
C_Y^{mathrm{generic}}
+
C_Y^{mathrm{shared}}
+
C_Y^{mathrm{edge}},
]
where
[
C_Y^{mathrm{generic}}le0,
]
and the shared-prime / edge pieces satisfy an explicit subpower or polylogarithmic upper bound.

This is suggested by the exact fact that boundary atoms live in thin multiplicative windows and, for least-prime assignment, each fixed-(ell) support is an antichain.

## Falsification controls

Every proposed inequality must be tested against:

1. the generic balanced fake-prefix counterfamily already in #848;
2. the bounded-completion fake source with quadratic covariance;
3. randomized squarefree sign patterns with the same marginal support but without exact divisor inversion;
4. a control preserving the antichain property but scrambling divisibility incidence.

A theorem that survives only because it assumes generic norm smallness is not source-specific enough.

## Computational reconnaissance

Useful finite experiments:
- decompose the existing exact (C_Y) for the square ladder (Y=3,15,255,ldots) by boundary classes;
- report signed mass, positive mass, and cancellation ratio separately;
- identify which classes dominate the positive excess;
- compare literal Möbius, sign-scrambled, incidence-scrambled and fake-prefix controls;
- preserve exact rational arithmetic where feasible.

Finite sign patterns are reconnaissance, not evidence for an all-scale theorem.

## Success criterion

A successful continuation produces a uniform arithmetic inequality that cannot hold for the known nonnative counterfamilies and that plugs directly into the already-proved scalar recursion of #848.

Anything weaker should be labelled diagnostic rather than progress toward RH.
