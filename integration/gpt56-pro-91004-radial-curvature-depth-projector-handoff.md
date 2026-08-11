# Handoff — radial xi curvature and exact zero-depth projection

## Scope

Continuation of PR #393's single-safe-line Hausdorff/Pick programme.

```text
branch: research/gpt56-pro/91004-radial-curvature-depth-projector
base:   research/gpt56-pro/91001-safe-line-hausdorff-pick
RH:     UNPROVED
```

This packet does not assert the remaining prime-side sign.

## Review order

1. `claims/lemmas/L-91004-unit-disc-generator-is-peano-integral-of-radial-curvature.md`
2. `claims/theorems/T-91002-rh-is-radial-concavity-of-completed-xi-modulus.md`
3. `claims/lemmas/L-91005-radial-curvature-is-sharp-parabolic-depth-projector.md`
4. `claims/lemmas/L-91006-offline-pair-is-one-hyperbolic-pick-block.md`
5. `claims/lemmas/L-91007-classical-zero-free-regions-penetrate-the-unit-disc-annulus.md`
6. `claims/refutations/R-91002-unweighted-centre-averages-are-rh-blind.md`
7. `experiments/X-91004-radial-curvature-depth-projector/verify.py`
8. retained result and SHA ledger
9. `reports/gpt56-pro/2026-08-11-radial-curvature-depth-projector.md`
10. parent PR #393 `T-91001/L-91001/L-91003`

## Main dependency DAG

```text
completed xi functional equation
 -> radial product P_x(t)=xi(s_x+sqrt t)xi(s_x-sqrt t)
 -> J_x(t)=t d_t log |xi(s_x+sqrt t)|
 -> C_x(t)=-J_x''(t)

C_x Taylor jet at t=1
 <-> one-safe-line coefficients a_k(x)
 -> Hausdorff / beta-Hankel hierarchy
 -> unit-disc A_x(w)

C_x Peano integral
 <-> A_x(w)

RH
 -> C_x completely monotone
 -> J_x concave
 -> A_x Stieltjes/Pick

one off-line zero at depth y and ordinate gamma
 -> C_gamma(t)~-2my^2/(t-y^2)^3
 -> A_gamma(w)~-4my^2/[... (1-y^2-w)]
 -> negative rank-one Pick witness
 -> failure of radial concavity / real-ray positivity.
```

## Binary rejection tests

Reject or repair the packet if any of the following fails:

1. `P_x(t)` is not entire in `t` after using the xi functional equation.
2. The factor `1/(8r^3)` in the `Xcal` curvature formula is wrong.
3. The relation
   ```text
   a_k=4(-1)^k C_x^(k)(1)/(k+2)!
   ```
   has a sign or factor error.
4. The Peano identity does not reproduce the exact parent generator.
5. A distinct zero can cancel the matched pole at `t=y^2` or `w=1-y^2`.
6. The contour orientation in the depth-projector integral changes its sign.
7. The pair Pick matrix is not exactly
   ```text
   [[0,-R],[-conj(R),0]].
   ```
8. The use of the classical zero-free region does not control all zeros with ordinates far from the centre.
9. Any finite regression is presented as proving an analytic zero-sum statement.

## Exact statuses

```text
radial product and curvature formula                 PROPOSED COMPLETE
absolute zero-kernel expansion                       PROPOSED COMPLETE
safe-line jet / Peano identities                     PROPOSED COMPLETE EXACT
RH -> complete radial-curvature monotonicity          PROPOSED COMPLETE
matched off-line curvature blow-up                    EXACT
RH <=> radial concavity / real-ray positivity         PROPOSED COMPLETE
sharp finite-packet depth projector                   PROPOSED COMPLETE
one off-line pair = one hyperbolic Pick block         EXACT
unweighted centre average as RH consumer              REFUTED EXACTLY
zero-free region -> annular holomorphy past 3/4       PROPOSED COMPLETE
prime-side radial concavity                           OPEN / RH-EQUIVALENT
Riemann Hypothesis                                    UNPROVED
```

## Recommended next production theorem

Do not add another scalar criterion. Work on one of these source-facing statements:

1. a positive representation of `C_x(t)` for `0<t<1/4` from the prime side;
2. a variation-diminishing theorem for the generalized-Laguerre Euler filters of PR #393 that implies radial concavity;
3. a localized centre-frequency inequality that pays the negative hyperbolic Pick block without collapsing to the positive zero-frequency depth count;
4. a cofinal zero-free/Pick continuation from the unconditional annular sliver to radius one.

Any unweighted centre average is now known to be structurally blind.
