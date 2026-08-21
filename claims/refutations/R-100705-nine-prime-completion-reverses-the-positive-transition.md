# R-100705 — Nine actual rough primes reverse the positive local transition

Claim ID: `R-100705`  
Status: **PROVED EXACT FINITE SEPARATOR**  
Created: 2026-08-21  
Depends on: corrected `L-100704`  
RH status: **not assumed**

Let

\[
K(y)=\begin{cases}16y,&0<y\le1,\\32\sqrt y-16,&y\ge1,
\end{cases}
\]

be the quadratic critical Peano carrier.  For the distinguished prime `p=67`, put `a=1/67`, `X_p=67^{-1/2}U_67`, and define the carrier-normalized transition kernel

\[
\mathcal T_{67}K
={ (X_p-aI)(X_p-I)\over1-a^2}K.
\tag{R-100705.1}
\]

Corrected `L-100704` proves `T_67 K(y)>0` for every `y>0`.

Now complete it by the nine later native Euler factors

\[
\mathcal E
=
\prod_{q\in\{71,73,79,83,89,97,101,103,107\}}
(I-q^{-1/2}U_q).
\tag{R-100705.2}
\]

At the exact endpoint `y=5500`, outward dyadic square-root arithmetic with denominator `2^120` proves

\[
\boxed{
-0.0469702012716840
<
(\mathcal E\mathcal T_{67}K)(5500)
<
-0.0469702012716839.
}
\tag{R-100705.3}
\]

In particular the completed transition is strictly negative.

## Meaning

```text
local distinguished transition kernel       positive everywhere;
native completion by later rough primes      not positivity preserving;
pointwise transition-cone proof of BTHC       false already on 10 labels.
```

The separator uses actual consecutive rough primes, not a generic artificial shift fixture.  Therefore the remaining balanced homotopy estimate must use cancellation in `t`, double-owner rectangles, or an integrated/phase-sensitive observation.  It cannot be reduced to pointwise positivity of every completed transition.

The exact replay is `verify_transition_separator.py` in `X-100705-recent-work-hostile-audit`.
