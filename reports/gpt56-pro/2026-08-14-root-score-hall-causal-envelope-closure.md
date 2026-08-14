# Root score-Hall causal-envelope closure

**Date:** 2026-08-14  
**Branch:** `research/gpt56-pro/91683-root-score-hall-causal-closure`  
**Base:** PR #462 at `8642e062b6c6f5a4c7d443a1ee5a6e9ecf3e4706`  
**Status:** candidate complete proof architecture; independent reconstruction required  
**Riemann Hypothesis:** unproved

## Executive result

The previous direct-row proposal failed because it applied no-upward Hall to stopped one-prime leaves. PR #456 gives an exact counterexample at `(p,y,py)=(67,13,871)` and an infinite counterfamily. This successor removes that operation completely.

Hall is instead applied once at the root, only on the certified quotient window

\[
1\le x\le c_0^{-1}<54.2192.
\]

The fixed-window score Hall transport uses one set of coefficients simultaneously in the native score, SHARP target, and every component row. It gives:

\[
\text{signed score}=	ext{positive residual score},
\]

\[
\text{signed target}=	ext{positive residual target}+	ext{positive slack},
\]

\[
\text{signed row}=\text{positive row bonus}+	ext{positive residual row}.
\]

Applying the exact native response maps yields, at every physical integer column,

\[
\Gamma(B_X;q)+\Gamma(R_X\widehat Z_X;q)=w_X(q),
\]

\[
\Xi(B_X;q)+\Xi(R_X\widehat Z_X;q)=\Omega_X(q).
\]

This is the explicit simultaneous root ledger missing from the coordinatewise-complement proposal.

## Endpoint-frame interface

`L-91674` proves that deterministic fixed-window Hall, positive endpoint integration, common-parent pushforward, same-index child transport, ordinary responses, radix-four responses, and one global positive quantizer commute on their stated hypotheses.

The signed detail identity is obtained by applying the two ordinary maps at `q` and `4q` before subtraction. No positivity of a signed detail map on arbitrary rows is assumed.

All current rows are summed before the positive quantizer, finite/continuum mismatch correction, safety factor, top omission, and terminal taper are applied. Each is charged once. The analytic endpoint-density and finite correction estimates remain the principal frozen-input review burden.

## Causal recursion

After root entry, no further Hall theorem is used. The exact causal identity is

\[
P_X=s_kP_X+
\sum_i\lambda_i(P_X-r_iU_{p_i}P_{X/p_i})+
\sum_i\alpha_iU_{p_i}P_{X/p_i},
\]

with

\[
s_k+\sum_i\lambda_i=1,
\qquad
\sum_i\alpha_i<1/8.
\]

Every causal difference is nonnegative in target, component rows, ordinary capacities, and radix-four capacities, and has uniformly bounded positive debt. Same-index child placement uses the actual arithmetic coefficient exactly once.

The homogeneous packet envelope therefore gives a uniform equality-deficit bound. Combining it with

\[
J_\Lambda(X)<4\sqrt X+4\log X
\]

yields a candidate native loss `O(log X)`, hence `o(log^2 X)`. The finite dual and frozen endpoint criterion then give the proposed RH implication.

## Replay

```bash
cd experiments/X-91673-root-score-hall-common-normalization
python3 verify.py --json results/verification.json
```

Expected:

```text
PASS_ROOT_SCORE_HALL_COMMON_NORMALIZATION_ALGEBRA
```

The retained replay checks 1,074 fixed-window Hall endpoint inequalities, 1,431 normalized-row cells, the stopped-leaf firewall, exact score/target/row identities, response commutation, finite endpoint integration, same-index scaling, and one global quantizer identity.

## Exact boundary

```text
stopped-leaf Hall                              FALSE / REMOVED
fixed-window root score Hall                   DIRECTED EXACT
simultaneous root target/score/row ledger       EXACT
native ordinary/detail root normalization       EXACT
formal endpoint-frame intertwining              EXACT
analytic endpoint realization                   FROZEN / RECONSTRUCT
causal reset and mass <1/8                      EXACT
packet envelope                                 EXACT CONDITIONAL
native O(log X) loss                            CANDIDATE COMPLETE
Riemann Hypothesis                              UNPROVEN
```
