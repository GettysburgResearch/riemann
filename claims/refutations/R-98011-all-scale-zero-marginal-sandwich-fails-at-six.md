# R-98011 — The all-scale zero-marginal target sandwich fails at `X=6`

Claim ID: `R-98011`  
Status: **PROVED EXACT FINITE COUNTEREXAMPLE**  
Created: 2026-08-18  
Depends on: `L-98011`  
RH status: **unproved**

The eventual statement `ZMTS67` must not be strengthened to every endpoint.

At the complete squarefree source with `X=6`, the positive-scalar even atoms satisfy `k<X/2=3`. The only such even-parity index is `k=1`, so

\[
T_E^+=t_6(1)=4\sqrt6-3.
\]

The odd-parity active indices are `2,3,5`, hence

\[
T_O=t_6(2)+t_6(3)+t_6(5),
\]

where

\[
t_X(k)={4\sqrt X\over k}-{3\over\sqrt k}.
\]

Subtracting gives

\[
\boxed{
T_E^+-T_O
=-{2\sqrt6\over15}-3
+{3\over\sqrt2}+\sqrt3+{3\over\sqrt5}.
}
\tag{R-98011.1}
\]

This is strictly positive. Indeed,

\[
{3\over\sqrt2}>2,
\qquad
\sqrt3>{5\over3},
\qquad
{3\over\sqrt5}>{4\over3},
\qquad
\sqrt6<{5\over2},
\]

so

\[
T_E^+-T_O
>5-3-{1\over3}={5\over3}>0.
\tag{R-98011.2}
\]

Therefore

\[
T_E^+>T_O,
\]

and by `L-98011` the Lorenz dual decreases immediately to the right of `lambda=0`; zero is not its minimizer.

This does not affect the eventual closure programme. It proves that `ZMTS67` needs an explicit finite initial range and cannot be used as a hereditary all-state Bellman premise.

```text
all-scale ZMTS67                         FALSE
finite counterexample                    X=6
sufficiently-large ZMTS67                OPEN
upper sufficiently-large sandwich        PROVED BY L-98013
remaining target-root sign               OPEN / RH-BEARING
```
