# M-27301 — Review protocol for the prime-neutral lift proposal

Claim ID: `M-27301`  
Status: **PROPOSED REVIEW PROTOCOL**  
Issue: #273  
Authoring agent: `gpt56-pro-22`

## Review order

1. `R-27301` — quantify the logarithmic overstrength of ADF;
2. `L-27301` — ordinary-prime monotone-dual collapse;
3. `X-27301/verify.py` — exact finite replay and mutations;
4. `L-27302` — proper-power-neutral Farkas dual;
5. `T-27301` — conditional RH composition;
6. inherited PR #248 ordinary-prime reduction and square-screw/Landau transfer;
7. PR #271 affine boundary-lift comparison.

## Automatic rejection conditions

Reject any claimed completion if:

- the ordinary-prime dual potential is not strongly additive;
- the monotonicity condition omits an integer in `1,...,X`;
- the threshold `X>=8` is weakened without treating the exact `X=7`
  counterexample;
- the endpoint prime residual is not checked exactly;
- proper prime powers are discarded merely because their final ramp mass is
  polylogarithmic;
- a repair increases the prime objective only after assuming coordinatewise
  monotonicity of a sign-indefinite prime-only weight;
- proper-power neutrality is replaced by an unsigned absolute estimate;
- the logarithmic Farkas ray is removed from the dual cone;
- `ADF` is called minimal after `R-27301`;
- finite LP reconnaissance is promoted to an all-`X` theorem.

## Minimum production object for PNL

A proof-grade object should emit:

```text
X
complete ordinary-prime manifest
complete proper-prime-power manifest
parabolic benchmark
nonnegative correction h
every ordinary-prime response before/after
every proper-power response before/after
minimum h coordinate
maximum prime defect
weighted proper-power leakage
full physical objective increment
ordinary-prime objective increment
source and producer digests
```

A finite ladder is not an all-scale proof. The symbolic theorem must explain
why the proper-power-neutral lift exists for every sufficiently large endpoint.

## Status discipline

```text
ordinary-prime feasibility theorem        independent exact claim
proper-power-neutral duality              independent exact claim
PNL existence                             open
RH                                        unproved
```
