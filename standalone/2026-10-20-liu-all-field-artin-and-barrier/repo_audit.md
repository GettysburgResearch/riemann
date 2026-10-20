# Repository comparison for the 20 October 2026 Liu import

Status: source and scope audit of the integrated entry points and selected
latest research sources; not an independent review of every analytic
argument in the repository. No historical theorem or status is promoted.

## Relevant observed state

The latest fetched PR inventory ended at #1008. The main-branch README,
STATUS, RESULTS and research/integrated/CURRENT_RESULTS still describe
the September 6 A/B/C/D integration as the accepted baseline. The later
quasi-Riemann work is on open research branches. Main explicitly says
RH is unproved and branch existence does not constitute mathematical
acceptance.

The most useful comparisons are:

| Object | Observed source | Scope and consequence of the new import |
|---|---|---|
| Earlier all-field compositions | #968 `14f544fb4293ffb59942ff8d345ab9d6da67025c`; #969 `6542781188469e8a23dadf9d419b3d5cf4d11de7`; later history in #1007 | Source-qualified proposed bounds such as 10/11, 49/54 and 271/300. Liu's reported B_flat is numerically stronger for the same all-field finite-order Hecke scope. This does not validate or invalidate the older component proofs. |
| Amplified decimal deduction | #1005 `d3b3d19573b8dc47ac6e37abd108d54982e9e5f1` | The exact 0.87488666 corollary assumes Xu-Sang's analytic framework and concerns Eisenstein-field finite-order Hecke functions and Dirichlet functions. Liu's B_flat is about 1.296e-8 smaller and has all-number-field scope. The old rational certificate remains a valid source-qualified calculation. |
| Direct-estimate floor | #1005 correlated/DIRECT_ESTIMATE_FLOOR.md | Exact lower floor 13/15 for the specified free-length direct recipe. Liu's §15.3 independently contains the same floor in a positive linear combination of low constraints. This is not a bound on actual zeros. |
| Joint numerator attempts | #1005 native/JOINT_NUMERATOR_CLOSURE.md | Existing marginal fourth moments and arbitrary intermediate numerator contours are no better than min(E_pointwise,E_averaged). The note does not itself prove that optimization of the combined envelope has the same optimum as either separate system. |
| Failed 0.87 model | #1004 `8e7375cd75909cc7dc3548c44e4d08c8adb4c034` | Positive exponent obstruction at a=25/36 for its explicitly stipulated model. It is not a universal 0.87 impossibility theorem. |
| Complete-source/quartic sprint | #1006 `0c838d130f275efb6e8ddb81dab42462b4ce9454` | No new zero-free boundary. Its .874 consumer needs a complete U^(6/5+epsilon) mixed mean. The stated available corner consequence is U^(11/8), leaving U^(7/40). |
| Actual quadratic-family convergence | #1003 `669b6a01f4d4858ae1ef806b07547be95c08c935` | Full-L approximation on compacts in Re(s)>1/2 is a family convergence result. At a hypothetical ordinary-zeta zero the scalar residual stays exactly one. Liu's wider family scope does not erase that obstacle. |
| Editorial manuscript | #1007 `ae22a228691fc7e571f97d4c80a8c6585c5fb656` | The 49-page survey preserves those conditional/proposed distinctions; it is an editorial account, not another independent proof. |

## Exact barriers that must guide the next attack

For free lengths lx,ly,ell, set M=lx+ly, b=ly-lx,

    k=max(0,(1+3ell-2M)/4,M+ell-1,(3ell-1)/2),
    G=max(0,b/12,b-ly/2).

The direct recipe has

    B_low=5/6+lx/6-ell/6+G+k/2 >= 13/15.

Consequently even a perfect nonprincipal bound cannot obtain 5/6 by
this unchanged recipe. With unchanged principal exponent, the direct
side alone needs at least an additional 1/30 power saving for 5/6 and
11/30 for 1/2. This makes a genuinely different signed average or a new
principal extraction more valuable than further positive moment orders.

For the twist-safe mixed fourth-moment proposal, with capacity z(v),
the #1005 exact identity is

    J-K=(P_m-R)/4 + (q/2)|z(m)-z(v)| >= 0.

The proposed joint moment is dominated by the existing numerator-only
moment plus the count. At the binding short witness R=P_m, the
numerator crossing length v_c equals the already-large plain detector
length m. Any improvement there must retain a genuinely stronger signed
inverse/plain correlation; reapplying the same plain moment repeats
binding information.

Liu §20 explicitly excludes class-by-class hybrid numerators, unequal
lengths and stronger analytic inputs from its refined-system optimality
claim. The present packet closes classwise mixing and unequal lengths for
the four explicit optimistic endpoints with the full direct majorant; see
beyond_free_length_barrier.md. It does not exclude new analytic estimates
or arbitrary new unequal-length contour constructions. Every local Euler
condition, shorter row range and common margin remains part of the source
contract for a successful new tuple.

## Quartic scope trap and a concrete normalization consequence

The Gaussian quartic construction has the complete identity

    sum (...) = C_B L_F^(S_a)(2s-1+eta,epsilon^2)/zeta_F^(S_a)(s),

where epsilon(c)=(-1/c)_4 c/|c|. This epsilon has a genuinely
infinite-order angular infinity type. Liu's finite-order Hecke theorem
does not apply to epsilon^2. The previously proved eta>=2-2B
numerator-protection threshold therefore remains the safe Euler-product
threshold. Finite extensions do not make that nonzero infinity type
finite order. The complete squareclass selector, angular realization
and weighted period estimate remain unconstructed.

For the zero-angular Kubota coefficient only, the new theorem does
allow division by zeta_F(4v-3) in Re(v)>(3+B_flat)/4. Its reflected
partner has denominator zeta_F(5-4v), giving the common band

    (3+B_flat)/4 < Re(v) < (5-B_flat)/4.

This is a direct source-qualified normalization consequence, not a
smaller zero-free boundary: changing variables 4v-3 returns precisely
the imported B_flat. Nonzero angular modes need their own theorem.

## What was actually read

The root README, STATUS, RESULTS and CURRENT_RESULTS; full #1005
UNIFORM_BOUNDARY, DIRECT_ESTIMATE_FLOOR, JOINT_NUMERATOR_CLOSURE and
PRINCIPAL_CORRELATIONS_AND_QUARTIC; full #1006 README and
COFINAL_HILBERT_FILTER; full #1004 REPORT; selected current PR bodies
for #968, #969, #971, #976, #977 and the recent #1001-#1008 series;
Liu's live HTML §15.3, §19 and §20. The source files fetched for this
audit retain their observed full commit identities above. No full
historical proof replay, entire repository validator, native theta
rebuild or human referee review was performed by this audit.
