# M-23803 — Reflected carry-sandwich review protocol

Methodology ID: `M-23803`  
Title: Fail-closed review of the Möbius-curvature and two-contact carry-sandwich closure  
Status: **PROPOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #238

## 1. Scope

The baseline carry sandwich is `L-23801`--`L-23803` and `T-23801`. The new
closing candidate is `D-23801`, `L-23806`, and `T-23803`.

The review should distinguish:

```text
finite carry/Legendre and LP algebra       exact review target
Mobius-curvature coordinate transform      exact review target
K=6/K=8 face dictionaries                  finite evidence
symbolic two-contact theorem                RH-bearing hinge
scale contraction and zero exclusion       conditional deduction
```

## 2. Frozen imports

Bind immutable source commits for:

```text
square-screw / Laplace transfer     PR #202
high-order complete-lattice Euler   PR #158
reflected Selberg identity          PR #226
first-cell Mertens decoder          PR #229
finite Mobius resolvent             PR #233
```

No imported full proposal status is inherited.

## 3. Exact finite replay

For every proposed packing or cover, reconstruct:

- `beta_(nq)` from floors;
- `B^T d` or `B^T e`;
- componentwise slack/excess;
- the Möbius profile `F`;
- curvature coefficients;
- the direct and divisor-reconstructed residual;
- entropy objectives and `4 sqrt(X)` intervals.

A solver or floating LP basis is never trusted.

## 4. Terminal-face manifest

At `K=6` and `K=8`, emit every recombined same-scale row with:

```text
both resolvent words
all Mobius/binomial signs
first-crossing destination
active packing and covering constraints
null-moment eliminations
frozen divisor coordinates
lower-scale contacts
remaining free endpoint contacts
first-cell mutation
```

For symbolic `K`, prove that every terminal row maps to one maximal affine
interval in each scalar obstacle and therefore has at most two free contacts.

## 5. Automatic rejection conditions

Reject the proposed closure if any of the following occurs:

1. a genuine three-contact same-scale face;
2. a balanced row removed by assumed `BTP(K)` or withdrawn `L-23203`;
3. an unannihilated interior row;
4. a reflected diagonal sent to an absolute-value error;
5. an omitted transition/cutoff surface;
6. packing and covering obstacle maps that cannot be paired;
7. failure to reproduce the first-cell Mertens coefficient;
8. proof only for finitely many packet orders;
9. an `o(sqrt X)` loss not sharpened to `X^o(1)`.

## 6. Production order

1. Audit `D-23801` and `X-23801-carry-envelope`.
2. Reconcile the exact sandwich and one-sided greedy certificates.
3. Export the complete `K=6` obstacle dictionary.
4. Search adversarially for a three-contact face.
5. Repeat at `K=8`.
6. Prove or reject the symbolic two-contact map.
7. Verify the first-cell mutation.
8. Only then promote `T-23803`.
