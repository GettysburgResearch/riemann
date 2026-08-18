# T-97910 — Two sharpened factor-67 large-prime frontiers imply RH

Claim ID: `T-97910`  
Status: **UNCONDITIONAL REDUCTIONS; TWO ALTERNATIVE SIGNED ESTIMATES OPEN**  
Created: 2026-08-18  
Depends on: `L-97910/L-97911/L-97912`; PR #590; fixed annular Mellin-Landau consumer  
RH status: **unproved**

Fix `0<kappa<1/2` and

\[
 Z=(\kappa\log X\log\log X)^2.
\]

The exact normalized root scalar admits two complementary source-faithful
representations.

## A. Largest-prime owner form

\[
 U_{\rm full}(X)=U_Z(X)-\mathfrak I_{Z,H}(X)-\mathfrak T_{Z,H}(X),
\tag{T-97910.1}
\]

where `L-97910` proves `U_Z(X)>0`, `L-97911` proves
`mathfrak I_{Z,H}=o(U_Z)` whenever `H^2 log Z=o(log X)`, and

\[
 \mathfrak T_{Z,H}(X)=
 \sum_{Z<p\le Xe^{-H}}\frac1p
 \sum_{\substack{v\ \mathrm{squarefree}\\
                  Z<P^-(v),\ P^+(v)<p}}
 \frac{\mu(v)}v\,U_Z(X/(pv))
\tag{T-97910.2}
\]

retains the literal largest-prime owner.

The one-sided **Expanded-Strip Balanced Large-Prime Estimate** `ESBLP67` is

\[
 \boxed{
 \mathfrak T_{Z,H}(X)\le U_Z(X)-\mathfrak I_{Z,H}(X).
 }
\tag{T-97910.3}
\]

## B. Positive-Euler-main/product-boundary form

For every `beta<1-2kappa`,

\[
 U_{\rm full}(X)=\mathfrak M(X)
 +\mathfrak E_{\kappa,\beta}^{\le}(X)
 +\mathfrak R_{\kappa,\beta}(X),
 \qquad
 \mathfrak E_{\kappa,\beta}^{\le}=o(1/\log X).
\tag{T-97910.4}
\]

where

\[
 \mathfrak M(X)\asymp\frac1{\log X}
\]

is explicitly positive and every history in `mathfrak R` has product
`v>X^beta` and child scale `X/v<X^{1-beta}`.

Thus for every fixed `delta` with `0<delta<1`, taking `kappa<delta/2` confines this error
representation to child scale below `X^delta`. The corresponding **Almost-Full-Product Boundary Remainder** estimate
`AFPBR67` is the exact one-sided inequality

\[
 \boxed{
 \mathfrak R_{\kappa,1-\delta}(X)
 \ge-\mathfrak M(X)
       -\mathfrak E_{\kappa,1-\delta}^{\le}(X).
 }
\tag{T-97910.5}
\]

A stronger but sometimes more convenient sufficient form replaces the final
term by any explicit upper bound for its absolute value.

Either estimate is exactly sufficient:

\[
 \boxed{
 \mathrm{ESBLP}_{67}\ \text{or}\ \mathrm{AFPBR}_{67}
 \Longrightarrow U_{\rm full}(X)\ge0
 \Longrightarrow\mathcal A_X\ge0
 \Longrightarrow\mathrm{RH}.
 }
\tag{T-97910.6}
\]

The last implication is the exact annular `5:3` Mellin-Landau consumer.

## Composition firewall

`L-97911` makes the terminal strip small relative to `U_Z`, whereas
`L-97912` works at the much finer final Euler-main scale `1/log X`. The packet
does **not** assert that the two localizations may simply be intersected; doing
so requires an additional source-level estimate. They are alternative exact
frontiers, not silently identified formulations.

## Exact progress

```text
complete all-depth cube for every c<1/4 in
  Z=c(log X log log X)^2                       PROVED POSITIVE
terminal owner strip with
  H=o(sqrt(log X/log Z))                       CLOSED RELATIVE TO U_Z
nonconstant error from products v<=X^(1-delta) POWER-SAVING
product-boundary child scale <X^delta          EXACT LOCALIZATION
largest-prime ownership                        EXACT
ESBLP67 owner Type-II                          OPEN / RH-BEARING
AFPBR67 almost-full-product boundary           OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVEN
```
