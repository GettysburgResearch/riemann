# M-27203 — Dyadic Commutator Debt review protocol

Claim ID: `M-27203`  
Status: **FAIL-CLOSED REVIEW PROTOCOL**  
Created: 2026-08-08  
Applies to: `L-27207`, `L-27208`, `T-27203`, `X-27206`

## Review order

1. Reconstruct the multiples-Möbius divergence from the target columns.
2. Verify the even scaling \(w_{2Y}(2q)=2^{-1/2}w_Y(q)\).
3. Verify the pair identity
   \[
   r_{2Y}(2a)+r_{2Y}(2a+1)=2^{-1/2}r_Y(a).
   \]
4. Reconstruct \(T_n\), \(E_n=T_{n+1}-T_n\), and their boundaries.
5. Verify that the unmatched coefficient is exactly \(w_{2Y}(2)\).
6. Replay every carry column of the proposed upper flow.
7. Split doubled-edge capacity into its exact even and odd parts.
8. Verify the lower debt, upper debt, and the factor \(1/2\).
9. Verify every cycle coordinate against the complete balanced basis.
10. Audit the cofinal excess bound without using a finite trend.

## Automatic rejection

Reject a certificate upon any:

- missing bottom charge;
- omitted odd node;
- wrong commutator sign;
- use of endpoint \(2Y+1\) in the exact \(2Y\) identity without its forcing;
- use of \(\beta_{2n,2q}=\beta_{nq}\) in place of the correct split identity;
- unbalanced correction edge;
- omitted cycle;
- unweighted negative-edge count substituted for capacity debt;
- absolute values before the odd leakage and commutator are recombined;
- one-frequency reflected identity substituted for a physical block;
- finite evidence promoted to DCD.

## Source firewalls

Every production object must retain:

- the dyadic signed source;
- the bottom charges \(2,3\);
- the exact \(2/3\) fixed-ratio Mertens projection;
- the same-sign Möbius hypercube mutation;
- the directed ternary negative mutation;
- the explicit prime-ramp dual potentials of `L-27206`.

## Status boundary

`X-27206` verifies finite algebra only. The DCD bound is not certified by that experiment, and RH is not claimed.
