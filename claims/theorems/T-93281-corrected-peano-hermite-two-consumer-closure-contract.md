# T-93281 - Corrected Peano-Hermite closure contract after safe-line centering and the two-row consumer

Claim ID: `T-93281`  
Status: **SOURCE-COMPLETE CANDIDATE ARCHITECTURE; TWO SIGNED PRODUCERS OPEN**  
Created: 2026-08-16  
Depends on: `L-93280--L-93284`, `T-93280`, PR #379, PR #520, PR #539  
RH status: **unproved**

The corrected programme has two independently understandable consumers.

## Route A - phase-locked carrier

```text
centered cubic field
 -> exact safe-line Plancherel formula
 -> phase-locked residue-completed synthesis
 -> signed covariance SCID_PL
 -> filtered First-Hermite inequalities
 -> terminal-pair theorem
 -> RH.
```

The raw `SID_H` norm is withdrawn. The complete remaining producer is the signed
covariance inequality (L-93282.9), not an unweighted scale norm.

## Route B - two-row Mellin-Landau

```text
positive 2,3-smooth reservoir
 + explicit large-prime three/four-knot packets
 -> LPTRP_23
 -> two fixed reciprocal-zeta Mellin transforms
 -> exact no-common-zero lemma
 -> Landau
 -> RH.
```

The direct consumer is complete conditional on `LPTRP_23`. The failed
same-product `FRONTIER-CHAIN` proof from PR #537 is not imported; PR #544's
scope correction is binding.

## No hidden RH-strength input

The packet proves unconditionally:

1. the safe-line Plancherel identity and logarithmic energy bound;
2. cancellation of the complete critical-boundary lattice by phase locking;
3. the residue-completed cubic/Hermite transform;
4. the exact two-row noncancellation theorem;
5. the smooth-reservoir/large-prime packet decomposition;
6. both conditional consumers.

It does not prove:

1. `SCID_PL`;
2. `LPTRP_23`;
3. RH.

Neither open producer is renamed as a technical lemma. A future complete proof
must close one of those two signed arithmetic statements.
