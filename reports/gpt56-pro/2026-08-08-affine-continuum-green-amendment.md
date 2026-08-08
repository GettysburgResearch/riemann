# Affine–continuum amendment to the Green–Skorokhod carry proposal

Date: 2026-08-08  
Agent: `gpt56-pro`  
Issue: #260  
PR: #270  
Status: **PROPOSED / NO RH PROOF CLAIM**

## Reason for the amendment

PR #270 originally isolated the clipped Green obstacle debt `GDS/CCD`. Two
newer exact developments sharpen the proof boundary:

1. PR #271 gives a prime oversupport affine lift of any signed feasible carry
   state;
2. PR #265 proves that the continuum parabolic defect is tail-majorized by its
   slack.

The present amendment imports those facts without merging their branches and
reconciles them with PR #270's source-bound Green and Möbius–Poisson ledgers.

## Exact new result 1: one Green edge is enough

Let `b^(0)>=0` be the parabolic benchmark and let `b^G` be the canonical signed
Green equality state. Put

```text
C_X^G=max_m (b_m^(0)-b_m^G)_+.
```

`L-26204` proves exactly

```text
prime ramp >= J_X(b^(0))-C_X^G log X.
```

The proof adds one constant block ending at a prime `Y in (X,2X)`. Every old
prime-power response is preserved, the physical vector becomes nonnegative, and
the only new response is the boundary charge `C_X^G` at `Y`.

The same scalar dominates the prefix Skorokhod construction:

```text
J_X(b^(0))-L_X^down <= 2 C_X^G log X.
```

Thus the affine charge is a strictly simpler proof consumer than the full
clipped contact recurrence. It does not remove the logarithmic dual ray; that
ray gives the exact lower firewall

```text
C_X >= [J_X(b^(0))-prime ramp]_+/log X.
```

## Exact new result 2: the continuum charge is zero

PR #265 proves for the continuum defect `E` that

```text
integral_0^1 E =0,
integral_a^1 E <=0 for every a.
```

`L-26205` converts this into an explicit quantile coupling between positive
defect and negative slack, supported on ordered pairs `u<=v`. Integrating the
positive incidence blocks

```text
-delta_u+delta_v
```

cancels the complete signed continuum defect. Every block is positive in the
physical carry coordinate and gains the logarithmic objective.

Therefore the continuum analogue of the least affine charge is exactly zero.
The remaining obstruction is finite divisor incidence, quotient-cell
boundaries, and the coherent Möbius scalar—not continuum mass or sign geometry.

## Exact regression

`X-26202-affine-green-comparison` uses only integers, `Fraction`, and formal
prime-log vectors. It verifies:

```text
prime oversupport lift
8 preserved old prime-power rows
one new boundary charge
formal objective identity
prefix Skorokhod residual
contact-debt identity
4/4 fail-closed mutations
```

Retained digest:

```text
92df3a4acca946b1ccb0e4ac3b036a7e2fb8a5ed3618074a5b90338a053f1048
```

## Corrected single hinge

The hardened proposal now asks for `FAGD`:

```text
start from the canonical Green equality;
perform source-bound signed quotient-cell/divisor transport;
keep every prime-power constraint feasible;
leave maximum downward displacement <=X^epsilon;
finish with one affine oversupport prime.
```

A proof-facing recurrence is

```text
C_X
 <= C log^A(2X)
    +sum_beta omega_beta C_(Y_beta),
Y_beta <=(X+1)/2,
sum_beta omega_beta <=1.
```

It gives `C_X=polylog(X)`, the critical prime-ramp lower bound, and RH.

This recurrence remains open.

## Mandatory mutations

The production proof must preserve:

- the logarithmic/von-Mangoldt dual ray;
- the exact fixed-ratio Mertens shell;
- PR #269's dyadic two-contact source and odd-column leakage;
- the rank-`K` same-sign Möbius cube;
- the complete all-integer Green extension;
- every quotient-cell and incidence-block boundary.

## Final status

```text
PR #270 pushed and mergeable                    YES
new affine/Skorokhod comparison                 PROPOSED EXACT
new continuum zero-charge transport             PROPOSED EXACT
new exact finite replay                         PASS 4/4 mutations
FAGD finite arithmetic deformation              OPEN / RH-BEARING
unconditional proof of RH                       NO
```

The branch should be reviewed as a serious full proposal with one explicit
source-specific finite theorem, not as a claimed unconditional proof.
