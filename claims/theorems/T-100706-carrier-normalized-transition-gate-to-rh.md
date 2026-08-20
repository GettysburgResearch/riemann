# T-100706 — Carrier-normalized transition packing is sufficient for RH

Claim ID: `T-100706`  
Status: **PROVED EXACT CONDITIONAL IMPLICATION; TRANSITION PACKING OPEN**  
Created: 2026-08-21  
Depends on: corrected `L-100703`, `L-100706`; centered-Bernstein negative-mass detector  
RH status: **unproved**

Fix a critical order `m>=3`.  Let `K_m` be the positive unsieved final critical Bernstein carrier and, for a finite prime-label multiset `Lambda`, use the carrier-normalized homotopy of `L-100706`:

\[
F_\Lambda(X)
=
\left(\prod_{\ell\in\Lambda}E_\ell\right)K_m(X),
\]

\[
P_\Lambda(X)
=
{C_\Lambda(1)\over C_\Lambda(0)}
\left(\prod_{\ell\in\Lambda}Q_\ell\right)K_m(X),
\]

and

\[
Z_\Lambda(X)
=
C_\Lambda(1)
\int_0^1
{d\over dt}N_{\Lambda,t}K_m(X)\,dt.
\tag{T-100706.1}
\]

Then exactly

\[
\boxed{F_\Lambda=P_\Lambda+Z_\Lambda.}
\tag{T-100706.2}
\]

`L-100706` proves

\[
P_\Lambda(X)\ge0.
\tag{T-100706.3}
\]

Therefore

\[
\boxed{(F_\Lambda(X))_-\le (Z_\Lambda(X))_-.}
\tag{T-100706.4}
\]

No completed carrier is placed inside an absolute value.

## Carrier-normalized transition packing

Define `CNTP100706` by

\[
\boxed{
\sup_\Lambda
\int_1^Y (Z_\Lambda(X))_-{dX\over X}
=Y^{o(1)},
}
\tag{T-100706.5}
\]

where `Lambda` ranges over initial finite labelled-prime truncations, with the two copies of `67` retained separately.

The complete native critical packet is obtained by finite-label exhaustion.  At every fixed endpoint the source converges absolutely after the critical carrier subtraction, and Fatou's lemma for the nonnegative functions `(F_Lambda)_-` gives

\[
\int_1^Y(F(X))_-{dX\over X}
\le
\liminf_\Lambda
\int_1^Y(F_\Lambda(X))_-{dX\over X}.
\]

Combining with (T-100706.4)--(T-100706.5) yields subpower logarithmic negative mass for the complete critical remainder.  The centered-Bernstein Mellin--Landau theorem then proves

\[
\boxed{\mathrm{CNTP100706}\Longrightarrow RH.}
\tag{T-100706.6}
\]

## Why the new gate is sharper

Every local derivative in `Z_Lambda` contains

\[
(X_p-p^{-1}I)(X_p-I),
\]

so it annihilates the critical half-order carrier before completion by the other labels.  The squared endpoint is positive and is never estimated negatively.  Thus `CNTP100706` asks only for the carrier-zero balanced transition term, unlike the earlier regional estimates which separately paid power-sized completed and transition carriers.

`R-100705` proves the integrand is not pointwise nonnegative after native completion, so (T-100706.5) is genuinely an integrated signed packing theorem.  It is not proved here.
