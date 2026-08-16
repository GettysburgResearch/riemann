# R-95180 — Positive scalar projection retains the scale-four principal pole

Claim ID: `R-95180`  
Status: **PROPOSED COMPLETE EXACT FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `L-95180/L-95182`; `L-93263`  
Scope: fixed positive scalar projections of the two-channel reciprocal state

## 1. Pole orders

At `s=1`,

\[
G_4(s)=\zeta(s){1-4^{-s}\over1-4^{1-s}}
\]

has a pole of order two: zeta contributes one pole and `1-4^{1-s}` contributes a second. The reciprocal `A_4=1/G_4` has a zero of order two.

For fixed nonnegative constants `r_+,r_-`, not both zero, the scalar projection of the positive channels is

\[
r_+U_4^+(s)+r_-U_4^-(s)
=(r_++r_-)G_4(s)+(r_+-r_-)A_4(s).
\tag{R-95180.1}
\]

Since `r_++r_->0`, the double pole of `G_4` survives. The vanishing `A_4` term cannot cancel it.

Therefore

\[
\boxed{
\text{every nonzero fixed positive scalar projection retains the double real pole.}
}
\tag{R-95180.2}
\]

## 2. Consequence

Positive source ownership and polylogarithmic `1/n` flux mass do not imply the centered Q4 curvature estimate. The principal channel must be removed by a nonlocal operation which is not a fixed positive scalar functional.

The following are invalid completion steps:

```text
sum the two positive channels and differentiate;
choose one fixed positive channel combination;
apply an absolute-value estimate before centering;
drop the Hardy/unit boundary;
infer centered curvature from positive Peano mass alone.
```

## 3. Unit-boundary firewall

A logarithmic derivative has Dirichlet coefficient zero at the unit, while a normalized reciprocal state has coefficient one. No source-free causal convolution can recover the reciprocal from its logarithmic derivative. The unit/Hardy boundary must remain an explicit input of any passive or Schur realization.

## 4. Boundary

```text
positive projection retains double pole    EXACT
positive mass -> centered curvature         FALSE AS AN INFERENCE
unit boundary removable                     FALSE
nonlocal centered extraction                OPEN
Riemann Hypothesis                          UNPROVED
```
