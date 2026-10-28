# Variable-length bound for a reflected-energy exponent

**Status:** Exact elementary inequality, proposed for independent review. Its potential application to Hu's fixed-infinity-type construction is conditional on matching all physical quantities and hypotheses; it does not itself prove a zero-free region.

**Source and scope:** The scalar expression `E` below is the reflected-energy upper exponent in Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*](https://hexagonmath.org/2610.00216v1), equations (4.19)–(4.20). The fixed-length argument in Hu's Proposition 6.2 and the variable-length calculation in Xu–Sang, [arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), Section 3, motivate the hypotheses. This is an algebraic lemma for the displayed exponent, not an independent derivation of Hu's energy estimate or a complete verification that the hypotheses hold for its physical rows.

## Lemma

Let `epsilon >= 0`, `ell >= 0`, `0 <= d <= ell`, and set

    ell_prime = ell - d,    M = 1 - ell - 2d.

Let `O,H,A,N,R,S,z,v,q` be nonnegative real numbers, and let `Delta,theta` be real. Suppose

    H = M - O - Delta,     Delta >= -epsilon,
    2A <= O + epsilon,     N <= A,     z <= ell_prime,
    |theta| <= epsilon.

Define

    T = 2H + 2A + 2z - 1 - ell_prime - theta - N - 3R,
    y = v + 3q,
    u = min(v,z,(v+z)/3),
    E = O/2 + max(H,v+q) - S - R + z - u - q - (T-y)_+/2.

Assume the retained-dyad condition `y <= T + epsilon`. Then

    E <= M + max(0, 5ell + d - 1)/4 + 5epsilon.

Here `x_+ = max(x,0)`. No inequality on `ell` beyond nonnegativity is needed for this estimate.

## Proof

The identity `M + ell_prime - 1 = -3d` and the hypotheses give

    T - (H - 3d)
      = -O - Delta + 2A - 2(ell_prime-z) - N - 3R - theta
      <= 3epsilon.

Because `v,q >= 0`, `v+q <= y <= T+epsilon <= H-3d+4epsilon <= H+4epsilon`. Thus the maximum in E is at most `H+4epsilon`.

If `u=z`, the nonpositive terms `-S-R-q-(T-y)_+/2` may be discarded. As `O >= 0` and `Delta >= -epsilon`,

    E <= O/2 + H + 4epsilon <= M + 5epsilon.

If `u` is not equal to `z`, the definition of the minimum implies `u >= v/2`: this is immediate when `u=v`, and when `u=(v+z)/3 < z` it follows from `v<2z`. Consequently

    u + q + (T-y)_+/2 >= y/4 + (T-y)_+/2 >= T/4.

The last inequality holds both for `y <= T` and for `y >= T`. Therefore

    4(E-M-4epsilon)
       <= 1 + ell_prime - 2M + 2z - 2Delta - 2A + N - R - 4S + theta
       <= 1 + 3ell_prime - 2M + 3epsilon
       = 5ell + d - 1 + 3epsilon.

The first inequality substitutes the definition of T and `H=M-O-Delta`; the second uses `z<=ell_prime`, `N<=A`, nonnegativity, and the bounds on `Delta` and `theta`. Combining the two cases proves the stated bound.

## First-stage values and application boundary

For `ell = 10027/60000` and `0 <= d <= ell`, one has `5ell < 1`, so

    max(0,5ell+d-1)/4 <= d/4.

If a physical row estimate has exactly the above E and satisfies the lemma's scale and retention hypotheses on every retained dyad, it therefore has exponent at most `M + d/4 + 5epsilon`. In the candidate low-side calculation, taking the square root and retaining the separate tuple/compensation factor `Z^(-d)` gives an extra exponent at most `-7d/8` before losses.

The unresolved interface is important: Hu's Lemma 4.8 is a dyadic estimate with fixed conductors, unit classes, profiles, small boundary scales and a retention parameter. Before using this scalar lemma, one must establish the specific `2A<=O+epsilon` and `N<=A` comparisons for the actual marked prime slots and all fixed-infinity-type rows; map `M`, `ell_prime` and `theta` to the varied physical scales; cover discarded dyads with the stated tails; and check uniformity and the common profile. The scalar inequality alone supplies none of those analytic assertions.

## Exact support lemma for the conductor ledger

Let `k_pow` be a nonzero integral ideal whose prime valuations are all at least two. Let `a` and `n0` be squarefree ideals with `n0 | a | rad(k_pow)`. Then

    N(a)^2 <= N(k_pow),        N(n0) <= N(a).

This follows prime by prime, since every prime in `a` occurs at least twice in `k_pow`; the second inequality is divisibility. Thus if the three lengths `O,A,N0` are their *actual* base-Z log norms, then `2A <= O` and `N0 <= A` exactly, with no dependence on the geometry or archimedean type. If `O` is instead a dyadic center with `N(k_pow) <= C Z^O`, the first inequality becomes `2A <= O + log(C)/log(Z)`; analogous fixed support constants give the expected `O(1/log Z)` terms. A fixed finite set of extra exceptional primes only changes these bounds by a fixed additive log-norm, provided it is explicitly isolated before the dyadic counting.

The source identification needed to invoke this lemma is concrete. Hu's Lemma 4.8 calls `A0` the active **nonresidual** radical and separates active slot length `z_a`; in the one-probe physical row the target multiplies the completed index as a fixed unitary background, and a puncture is a separately specified indicator. If the physical specialisation really has trivial squarefree label and no moving non-slot puncture, then all non-slot active primes outside the residual squarefree row lie either in `k_pow` or a fixed exceptional set. The `N0` terms are selected divisibility terms among those same active primes. Under precisely this support identification, the ideal lemma establishes the two ledger inequalities for every geometry; unitary archimedean phases change coefficients, not ideal divisibility. They must not be used to move a changing prime into a fixed exceptional set. Hu §6.5 asserts the resulting ledger, while the exact no-moving-puncture and support match for the proposed rescaled probe remains an analytic-source check rather than a conclusion of the algebra alone.

More specifically, in Hu's displayed equation (6.1), the row character is `chi_(c n^3)(m)` and there is no separate `chi_(c n^3)(f)^4` label or puncture indicator. Thus the natural specialisation of (4.18) has `f=1` and `rho=1`, with the fixed unitary target absorbed into `nu`. Equation (6.9) replaces `X,Y,Z` by `X/p_J,Y/p_J,Z p_(J^c)` and supplies the mark `D=p_(J^c)`; it does not insert a further non-slot puncture in (6.1). Hu's Lemma 4.8 explicitly treats active marks through `z_a`, removes tuples meeting the row before reflection, and treats inactive marks as separate frozen row restrictions. With those source assertions taken literally, the moving non-slot active primes contributing to `A0` are therefore supported on `k_pow`, and the `j=4` terms contributing to `N0` form a subproduct. These are local support and divisibility facts independent of `b`, `ell`, and `d`; the separate common-profile, annular and uniform-tail gates still require checking. This paragraph uses Hu's coefficient and zero-extension claims rather than independently rederiving their finite local tables.

**What was checked:** The displayed algebra and an exact symbolic expansion of the second-branch numerator. No computation of physical row norms and no replay of Hu's theta estimate was performed.
