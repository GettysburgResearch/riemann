# O-91401 — Current boundary after compensated Green completion and atomic isolation

Observation ID: `O-91401`  
Status: **CURRENT FAIL-CLOSED PRODUCTION HANDOFF**  
Created: 2026-08-12  
RH status: **unproved**

## Exact advances

```text
prime full packet                     exact Wick-Green source;
short continuous channel              direct-translation compensation;
long continuous channel               positive endpoints minus production;
completed base measure                one scale-independent signed source;
gamma completion                      positive ladder minus one pole;
plastic-aligned scalar source         positive nonprime Levy increment;
full completed Green identity         connection + production - adverse ledger.
```

The source factorization is now complete across:

```text
carriers;
positive delays;
both Hardy orientations;
the bridge;
prime atoms;
short and long archimedean jumps;
deterministic connection coordinates.
```

## Hostile corrections made in the same pass

1. The prime safe mode split cannot be reused at the singular short-jump
   endpoint: its individual modes do not share the required no-jump trace.
   Corrected `L-91412` uses the direct physical translation orbit on the
   bounded short channel.
2. Plastic alignment does not yield a full Gram proof by continuous-to-atomic
   measure domination.  `R-91405` uses Fejer packets to isolate one prime atom
   while the continuous norm tends to zero.
3. The one-scale pole channel is rank one, but the three-scale radial
   recurrence is not a one-pole or finite-index problem; `R-91404` records the
   scale, derivative, delay and bridge obstructions.

## Exact remaining theorem

The completed delayed screw Gram has the explicit source identity

\[
 \mathbb K_a^{\rm del}
 =\mathcal C_a^\lambda+\mathcal P_a-\mathcal N_a.
\]

The live theorem is CPPD:

\[
 \boxed{
 \mathcal C_a^\lambda+\mathcal P_a
 \succeq
 \mathcal N_a.
 }
\]

The proof must use the connection and endpoint ports jointly.  Neither total
variation, one-scale rank counting, nor uncoupled continuum-to-prime sampling
can close the sign.

## Preferred attack order

1. Write the connection block in the gamma-ladder evaluation basis of
   `L-91411`.
2. Compute its Schur complement against the finite `C,J` compensation ports.
3. Keep prime production and prime endpoints coupled jump by jump; do not
   compare their measures separately.
4. Search for a contractive transfer from the adverse tuple
   `(U_prime,V_prime,C,J,D_long)` into
   `(D_prime,S_u f-f,C-J,U_long,V_long,delay leakage)`.
5. Use the plastic-aligned scale only to remove the continuous scalar sign
   mismatch, not as a substitute for the full transfer.
6. Test every proposed transfer against the Fejer atomic-isolation packets of
   `R-91405` and the three-scale ladder firewall of `R-91404`.

## Current exact boundary

```text
all source channels and full packet geometry             EXPLICIT
continuous Levy compensation                             CLOSED EXACTLY
prime/continuous/connection source identity              CLOSED EXACTLY
uncoupled aligned sampling                               REFUTED
one-pole finite-index shortcut                           REFUTED
CPPD coupled source contraction                          OPEN / RH-EQUIVALENT
Riemann Hypothesis                                       UNPROVED
```
