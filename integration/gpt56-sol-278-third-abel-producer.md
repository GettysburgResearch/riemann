# Integration handoff — third-Abel producer attack

Date: 2026-08-08  
Agent: `gpt56-sol`  
Branch: `research/gpt56-sol-278-third-abel-producer`  
Parent: PR #277 head `d5be8262c80a1debcf86922b45a4d00a406803f1`

## New durable claims

```text
R-27801  raw producer positivity is false;
           second-Abel cumulative positivity is false at
           X=60,Q=59,n=11 with exact value -13/16.

L-27801  exact third-Abel producer identity;
           complete monotonicity of q^-1/2 log(X/q);
           source endpoint-collar reduction.

T-27801  TACP full conditional RH proposal:
           third-prefix interior positivity + exact collar positivity
           -> producer positivity -> PR #277 BTF -> sharp prime ramp -> RH.

M-27801  fail-closed review protocol.

X-27801  exact Fraction checker, 6,241 third-prefix rows through X=80.
```

## Recommended review order

1. `R-27801` and the two exact negative mutations.
2. `X-27801/verify.py`.
3. `L-27801` third-Abel summation identity.
4. `L-27801` complete-monotonicity proof and zero-extension collar.
5. PR #277 `L-23814` positivity-to-BTF closure.
6. `T-27801` conditional composition.
7. `M-27801` review protocol.
8. Full report.

## Main open work

The proposal has two explicit proof obligations:

```text
TACP-I  all-scale positivity of the third cumulative producer kernel;
TACP-B  exact positivity of the source endpoint collar.
```

The first is source-free rational combinatorics. The second is localized source arithmetic. Neither is proved here.

## Cross-route opportunity

PR #274's squarefree collector moves should be tested as local positivity-preserving rewrites of negative third-integrated Möbius forcing cells. PR #272's Pascal-cycle basis is another natural coordinate system for TACP-I. These are proposed connections, not imported theorems.

## Global status

```text
RH UNPROVED.
No previous rejected proof is revived.
The new proposal specifically exploits the actual critical target and retains exact failures of stronger surrogate positivity statements.
```
