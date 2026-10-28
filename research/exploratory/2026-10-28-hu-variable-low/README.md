# Variable-geometry low-side calculation for Hu's unitary probe

**Status:** Conditional low-side theorem, proposed for independent review; **no zero-free region is claimed**. The arithmetic source estimates and their source-level coefficient identities are imported rather than reproved.

**Source:** Boyang Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*](https://hexagonmath.org/2610.00216v1), v1, 13 October 2026, PDF SHA-256 `b5fbde36de299525e268318add0dfb913dc6d85a51b602dd914c243cb360b4ac`, §§3.1, 3.8, 4.8, 6.1–6.5. The parameter calculation follows the analogous [Xu–Sang](https://arxiv.org/abs/2610.15291v2), Proposition 3.1, but that proposition treats its own finite-order Eisenstein setting and is not itself an infinite-order, general-field input. Neither analytic source was independently audited.

## Candidate statement and hypotheses

Fix a number field `K` containing the twelfth roots of unity, a continuous unitary Hecke character `psi` in the precise fixed-target class of Hu §6, with a global norm twist removed and the orientation chosen as in his Proposition 3.2, and all Hu §6 arithmetic data, cutoffs, and normalizations. In particular the associated theta-period character must satisfy the nonzero angular condition of that proposition. Use Hu's same compensated expression (6.9) and its principal normalization (6.18)–(6.19). This is the scope of the source construction: no extension of the displayed low estimate to an arbitrary *unoriented* target or to a target with a norm twist still present is asserted here. A separate argument would need to show how conjugating the target and restoring a norm twist act on the physical expression and its bound; a zero-free result for an oriented family would likewise need its own conjugation and vertical-translation step. Let `b>0` and `1/6<=ell<=1/5`, and set

    lx=(1-b-ell)/2,  ly=(1+b-ell)/2,
    h=(1+b+3ell)/2,  X=Z^lx,  Y=Z^ly.

Assume `lx>ell` and `ly-ell>11b/6`. Use a fixed finite slot system of positive lengths summing to `ell`, with the source's disjoint nonnegative prime windows. The target calculation is

    |J_psi(Z)| <<_(psi,epsilon) Z^(lx/2+b/12+epsilon)
                    = Z^(C_b(B(ell))+epsilon),
    C_b(s)=s-(4+b)/6,   B(ell)=11/12-ell/4.

The exponent is independent of the fixed mesh and the constant may depend on the fixed target and fixed slot data. This theorem is conditional on Hu's arithmetic calibration and finite-sector identities in Proposition 3.1 and Theorem 3.5; his fixed-type reflection and seminorm bounds in Proposition 3.2; the additive Gram estimate Proposition 3.8; and the marked reflected-energy estimate Lemma 4.8, including the local coefficient, collision-mask, annular-tail and fixed-type uniformity assertions in its proof. It also uses the standard fixed-field prime-ideal theorem to bound the normalizer from below. These source claims are not independently reproved here. Proposition 3.8 is formulated for polynomially bounded variable `Q,Y`, with `P_a=Y^2/Q>=1`; Lemma 4.8 takes the row and completed lengths in bounded ranges, rather than requiring the specific lengths later substituted in Hu §6.5. The physical matching to those source hypotheses is spelled out below and is itself proposed for further review.

## Calculation for a single rescaled subset

For a subset `J` of slots let `d=sum_(i in J) ell_i`, so `0<=d<=ell`. Its tuple has prime-norm product `Z^(d+o(1))`. The corresponding rescalings have exponents

    X' ~ Z^(lx-d),  Y' ~ Z^(ly-d),
    M' = 1-ell-2d,  ell' = ell-d,
    M'+ell'-1 = -3d.

The hypotheses give `lx-d>0`, `ly-d>0`, and `M'>0`; moreover `P_a=Y'/X' ~ Z^b>=1`.

Apply the *full marked* Hu Lemma 4.8 to the same completed row including all surviving slots, using its actual row deficit, all conductor terms and the dual-tail condition. If the conductor reduction used in Hu §6.5 remains valid for these variable scales, its two post-ledger exponent branches have the forms

    M' - O/2 - Delta_H + o(1),
    M' + (1+3ell' - 2M' - 2Delta_H)/4 + o(1),

where `O>=-o(1)` and `Delta_H>=-o(1)`. Therefore the squared completed row norm is bounded by

    Z^(M'+L_ell(d)+epsilon),   L_ell(d)=(5ell+d-1)_+/4.

The exact scalar reduction under explicit retained-dyad and ledger hypotheses is proved in the companion [variable-energy lemma](../2026-10-28-variable-energy-lemma.md), with an explicit `5epsilon` error. The proof-critical physical interface remains: Hu's displayed (6.22) asserts the simplified fixed-parameter result, and it is not enough to substitute new numbers into it.

The conductor ledger has a geometry-independent support derivation, conditional on Hu's local identities. In (6.1), the row character is `chi_(c n^3)(m)` and the fixed unitary target is part of the completed-index background; there is no additional squarefree label or puncture indicator. Thus in (4.18) the natural physical specialisation has `f=1` and `rho=1`. In (6.9), each subset `J` rescales `X,Y,Z` and inserts the mark `D=p_(J^c)` without a new non-slot puncture in the completed row. Hu's Lemma 4.8 separates active marks into `z_a`, removes row collisions before reflection, and treats inactive marks as frozen row restrictions. Taking its coefficient and zero-extension claims as inputs, every moving non-slot prime in `A0` outside the residual squarefree row therefore divides the powerful row ideal `k_pow`; the `j=4` primes assigned to `N0` form a subproduct. For the corresponding squarefree ideals `n0 | a | rad(k_pow)`, each prime of `k_pow` has exponent at least two, so `N(a)^2 <= N(k_pow)` and `N(n0)<=N(a)`. Hence `2A0<=O+O(1/log Z)` and `N0<=A0`, independently of the chosen geometry. Fixed exceptional primes contribute only fixed logarithmic offsets. The target's unitary archimedean phase changes coefficients but not divisibility.

This establishes the scalar inequality and conditional conductor-support derivation, not an independent proof of Hu's coefficient and reflection identities. The common-profile and tail bounds must still apply to every rescaled tuple with its original masks and finite unit-sector decomposition.

For that matching, first freeze the slots in `J`, so their product fixes `X',Y'` and the additive row box. The surviving marked tuple uses the disjoint slots in `J^c`. In the notation of Hu (4.18), take `nu=conjugate(G) psi`, `f=1`, and `rho=1`: then `a0(c) nu(c)=gamma_2(c) vartheta(c)` and the cube coefficient is `vartheta(n)^3`, exactly as in (6.1). The group `Theta` in Hu §4 contains the finite Gauss character `G`, so this background belongs to `psi Theta`. The unitary factors `conjugate(psi)(p_i)` and the original fixed windows are bounded product-form slot coefficients, independent of the row and dual variables.

The companion [Gaussian separation](../2026-10-28-gaussian-slot-profile.md) decomposes the exact moving factor `P_G(N(c n^3)/(Z N(p_(J^c))))` into fixed annular completed profiles and slotwise norm phases, with weighted Fourier densities summable in the annulus and all frequencies. It preserves the original product mark, row collisions and zero-extension masks. On retained annuli the completed exponent is `1+ell'+theta_N`, with `|theta_N|` arbitrarily small; the companion note also supplies an absolute tail using fixed-field ideal counts, Hu's compact quotient and his positive norm section. In Hu's proof of Lemma 4.8 the inactive marks are frozen row restrictions and active collisions remain the displayed mask; after finite-sector separation his slot coefficient is independent of the row and dual variables, and his dual coefficient is independent of the row and slot variables. The Gaussian norm phases preserve those independence statements. These are explicit uses of the source's assertions, not a new proof of their finite local tables. The fixed number of subsets and logarithmically many retained annuli cost at most `Z^epsilon`.

For the additive term, Hu Proposition 3.8 bounds the squared norm by, up to the fixed height factor and a small loss,

    (Q0/Y') (1+P_a^(1/6)+P_a^2/Y'),  Q0 ~ X'Y'.

As `ly-d >= ly-ell > 11b/6`, the last term is bounded by `P_a^(1/6)`, and `P_a>=1` absorbs 1. Cauchy–Schwarz with Hu's `Q0^(-1/2)` prefactor yields, for this tuple,

    (X')^(1/2) P_a^(1/12) Z^(L_ell(d)/2+epsilon).

The tuple count contributes `Z^(d+epsilon)`, the explicit compensation coefficient contributes `Z^(-3d/2+epsilon)`, and `(X')^(1/2)` contributes `Z^(-d/2)` relative to the unrescaled scale. Thus the excess exponent is

    -d + (5ell+d-1)_+/8 <= -7d/8 <= 0,

because `5ell<=1`. Summing the fixed finite subsets gives the stated raw exponent. Dividing by the principal prime-window normalization costs only `Z^epsilon` if the fixed-field prime-ideal theorem supplies the positive window masses with the same exclusions and normalization as Hu §6.4.

## Unchecked gates and consequence

1. Independently review the source-specific application of Hu's Lemma 4.8 and its local identities to every rescaled tuple, including its `Td` tail restriction, zero extensions, and all fixed-type seminorm/height quantifiers. The conditional proof above uses those source claims; it does not independently verify Hu's finite local tables or theta reflection.
2. Independently review Hu's common row box and additive Gram conditions for *all* subsets, including `Q0/Y'`, finite local sectors, unit quotients, and constants uniform in slot mesh at the exponent level. The proof assumes the fixed source calibrations and the prime-normalization hypotheses stated above.
3. Rebuild the principal-row contours and the high-side nonprincipal row estimates for the **same** variable-geometry compensated probe. Hu §7–§8 use the specific fixed parameters `(ell,b)=(1/6,1/8)`. The low estimate alone does not supply the common high-side power saving or a zero-free theorem.
4. If the target is an arbitrary number field, justify descent for the full unitary family, including archimedean type and norm twists. Finally apply the signal-to-zero-free criterion with its noncancellation and pole conditions.

Hu Lemma 6.1 already states that the corresponding scalar principal Euler factor is holomorphic and nonzero on `Re(s)>2/3`; this observation is not a new intermediate result.

**What was run:** source-level coefficient matching and inequality checks using the referenced papers' displayed identities; an independent quantified proof of the scalar reflected-energy inequality, an ideal-divisibility proof of the conditional conductor ledger, and an exact Gaussian profile and tail calculation. No Lean build and no independent derivation of Hu's full reflected energy or the high-side estimates was performed. An independent review of the low-side source matching remains needed; the missing gate for a new nonvanishing result is item 3.
