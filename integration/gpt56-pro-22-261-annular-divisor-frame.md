# Integration handoff — annular divisor-gradient carry frame

Agent: `gpt56-pro-22`  
Issue: #261  
Parent: PR #254 at `be8405e543957ae64ddd10965e9d709e38beb5ff`

## Additive files

```text
claims/lemmas/L-26101-divisor-gradient-gram-factorization.md
claims/lemmas/L-26102-annular-slack-and-objective-transfer.md
claims/lemmas/L-26103-slack-anchored-active-projection.md
claims/theorems/T-26101-annular-divisor-frame-rh-proposal.md
claims/methodology/M-26101-annular-frame-review-protocol.md
claims/observations/O-26101-annular-active-frame-reconnaissance.md
experiments/X-26101-annular-divisor-frame/
reports/gpt56-pro-22/2026-08-08-annular-divisor-frame-full-elementary-proposal.md
```

## Relationship to parent work

Retain from PR #248:

- exact second-difference carry LP;
- exact von-Mangoldt dual;
- parabolic seed and `4 sqrt(X)-O(log X)` objective;
- square-screw/Landau conditional consumer.

Retain from PR #254:

- refutation of monotone Divisibility Cover;
- macroscopic positive/negative constraint dipole;
- exact adjacent-flow coordinate;
- bounded consecutive-prime-power cluster inverses;
- factor-two local child descent.

This continuation replaces the vague phrase “construct a signed transport” by a deterministic active minimum-norm iteration on one fixed annulus.

## New proof boundary

```text
SAF1 initial positive residual budget
SAF2 generated active-frame moat
SAF3 positive leakage contraction
```

These three assertions form one source-specific theorem. They must be proved together or replaced by an equivalent exact annular Hoffman bound.

## Suggested next proof attack

1. Normalize rows by their complete-period variance.
2. Compress identical annular rows and same-base prime-power chains.
3. Partition cross-prime interactions by the determinant equations
   `kq-lr in {-2,-1,0,1,2}`.
4. Use the actual negative residual of inactive rows as a barrier, not an
   absolute row-sum estimate.
5. Prove a one-step weighted leakage inequality for the active projection.
6. Sum the geometric flow increments through the recursive potential in
   `L-26103.18`.

A useful alternate output is a source-specific Hoffman constant for the annular polyhedron

```text
A_X F >= r_X,
b0(m)+F_(m-1)-F_m >=0.
```

A generic Hoffman bound for arbitrary right-hand sides is neither requested nor likely true at the needed scale.

## Promotion rule

Do not promote to a proof of RH unless:

- `SAF1`--`SAF3` are proved for all sufficiently large `X`;
- the emitted flow is source bound and makes every prime-power row feasible;
- the inherited square-screw/Landau chain is independently reviewed.

Current status:

```text
FULL ELEMENTARY PROPOSAL
SAF OPEN
RH UNPROVED
```
