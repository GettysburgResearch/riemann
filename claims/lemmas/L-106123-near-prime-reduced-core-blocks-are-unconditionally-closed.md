# L-106123 — Fixed-fibre near-prime estimate; the former global conductor closure is retracted

Claim ID: `L-106123`  
Programme aliases: `LFAM1.NEAR_PRIME_REDUCED_CORES`, `LFAM2.LOCAL_CONDUCTOR_FIBRE`, `STRESS.FIXED_FIBRE_PHASE_BOUND`  
Status: **CORRECTED: FIXED-FIBRE ESTIMATE RETAINED; GLOBAL CONDUCTOR-FAMILY CLAIM RETRACTED BY `R-106123`**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Depends on: `L-106120--L-106124`; binding `R-106123`; `R-106131`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The first version observed correctly that, for a fixed pair of reduced cores
and their fixed least-prime conductors, the local bilateral phase energy is
paid in the long-core range. It then summed those positive fixed-fibre bounds
over all conductor pairs. `R-106123` proves that the latter promotion is
invalid.

## Retained local statement

For fixed

\[
c=\ell u,\qquad d=\rho v,
\qquad
\ell=P^-(c),\quad\rho=P^-(d),
\]

the complete owner packet satisfies the local two-phase estimate of
`L-106124`. In particular, when the rough cofactors `u,v` are bounded or when
one works on one declared fixed fibre, the phase conductor is paid by the
literal core coefficient.

This is a valid local theorem and may be used inside a global argument which
keeps the conductor assembly coherent.

## Retracted global statement

The source-dual positive moment squares each `(ell,rho)` fibre. Even when
`c=ell` and `d=rho`, the family contains power-many conductor pairs. A uniform
`O(1)` estimate per fibre does not imply a subpower sum over fibres.

Moreover, `R-106131` shows that the complete character atomic trace of one
fibre contains the additional factor

\[
(\ell-1)(\rho-1).
\]

Thus the old global near-prime conclusion and any claim that it pays the
complete mixed/double nonprincipal moment are withdrawn.

## Correct use

The local estimate remains available for:

```text
one fixed core/conductor fibre;
a source-coherent conductor amplifier before squaring;
the Wick-centered off-atomic traces of T-106140;
function-field complete shells with a separate global trace theorem.
```

It may not be summed source-blindly over least-prime conductors.

```text
fixed-fibre near-prime estimate          RETAINED
global positive conductor sum            RETRACTED
complete atomic diagonal                 NOT PAID
WCADD106140 / WCKUM106140                OPEN
Riemann Hypothesis                       UNPROVEN
```
