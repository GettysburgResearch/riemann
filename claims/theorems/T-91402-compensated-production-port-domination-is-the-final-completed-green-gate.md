# T-91402 — Compensated production-port domination is the final completed Green gate

Claim ID: `T-91402`  
Status: **FULL CONDITIONAL RH PROPOSAL / EXPLICIT OPERATOR DOMINATION OPEN**  
Created: 2026-08-12  
Corrected: 2026-08-12  
Depends on: corrected `T-91008`; `L-91409`--`L-91413`  
RH status: **unproved**

## 1. Purpose

The completed source is now explicit on the full fixed-scale packet:

```text
prime atoms;
short archimedean jumps;
long archimedean jumps;
deterministic connection;
causal and anti-causal orientations;
compressed delays;
one bridge.
```

`L-91409` factors the complete prime packet.  Corrected `L-91412` closes the
previously missing Lévy-compensated continuous packet using the direct physical
translation orbit at the singular short-jump endpoint and the safe mode split
on the long tail.  No prime sum, zero sum, carrier cross term, delay cross
term, orientation cross term, or bridge cross term is left without a source
coordinate.

The remaining theorem is no longer an embedding construction.  It is one
coefficient-one domination between two explicit positive Gram ledgers.

## 2. Positive production ledger

Let

\[
 \mathcal P_a
\]

be the direct-sum Gram of the following explicit source maps:

```text
prime jump production                  D_prime;
short translation production           S_u f-f;
short compensation production          C-J;
long continuous endpoint ports         U_long and V_long;
compressed-delay leakage;
reflected copies of every preceding port;
all corresponding bridge production coordinates.
```

Every summand is a Gram in a positive Hilbert space.  The prime and long-tail
mode formulas are those of `L-91409`; the short singular channel is the direct
translation source of corrected `L-91412`.

## 3. Endpoint and adverse-production ledger

Let

\[
 \mathcal N_a
\]

be the direct-sum Gram of

```text
prime endpoint ports                   U_prime and V_prime;
short compensation endpoints           C and J;
long continuous jump production        D_long;
reflected copies;
bridge endpoint coordinates.
```

Again every summand is positive.  The sign of the completed source is encoded
only by placing these ports on the right side of the comparison.

This is sharper than the total-variation subtraction of `R-91403`: the long
channel contributes positive endpoint reserve, and only its jump-production
port remains adverse.  Likewise the singular short channel does not carry two
independent uncentered endpoint norms; after the exact compensation its only
endpoint charges are the physical no-jump trace `C` and the finite connection
vector `J`.

## 4. Deterministic completed connection

Let

\[
 \mathcal C_a^\lambda
\]

be the finite carrier/delay/orientation/bridge connection obtained by applying
the six-pole resolvent functional of `L-91407` to Nakamura's drift and its
radial derivative, together with the finite compensation connection of
`L-91412`.

This is an explicit finite block assembled from safe values of

\[
 \frac{\xi'}{\xi},
 \qquad
 \left(\frac{\xi'}{\xi}\right)',
\]

and the rational residue coefficients of `Psi_a`.  No sign is assigned to it
by definition.

## 5. Exact completed Green identity

On every finite packet of the corrected fixed-scale delayed two-sided-plus-
bridge core,

\[
 \boxed{
 \mathbb K_a^{\rm del}
 =\mathcal C_a^\lambda
  +\mathcal P_a
  -\mathcal N_a.
 }
\tag{T-91402.1}

This is the packet-level combination of:

```text
L-91409  prime Wick-Green identity;
L-91410  completed source lock;
L-91412  corrected compensated continuous Wick-Green identity.
```

Equation (T-91402.1) is a source identity.  It does not assert positivity.

## 6. Completed Production-Port Domination

> **CPPD_a.**  At one fixed safe scale `a>1/2`, prove
> 
> \[
> \boxed{
> \mathcal C_a^\lambda+\mathcal P_a
> \succeq
> \mathcal N_a
> }
> \tag{T-91402.2}
> \]
> 
> on every finite carrier/delay/orientation/bridge packet, in the exact
> Guinand--Weil/Suzuki normalization.

The comparison must have coefficient one.  It may be proved directly, by an
explicit conservative Schur complement, or by a source-ordered contraction
from the adverse ports into the production-plus-connection reserve.

An existential square root of the already-unknown screw Gram is not CPPD.

## 7. Why CPPD proves RH

By (T-91402.1), CPPD gives

\[
 \mathbb K_a^{\rm del}\succeq0
\]

on every finite packet.  The corrected delayed form-core criterion of
`L-91034/T-91008`, subject to its declared review joints, then gives RH.

Conversely, under RH the zero-side Lévy Gram supplies an existential positive
factorization of `K_a^del`.  The open burden is the explicit arithmetic
production-port domination (T-91402.2).

## 8. Plastic-aligned specialization

At

\[
 a=a_\diamond
 =4.1415673607530469\ldots,
\]

`L-91413` proves that the continuous scalar nonprime channel is a positive
Lévy increment and that every prime residual coefficient has one sign.
The scalar shadow of CPPD becomes the explicit continuum-versus-prime-log
sampling comparison

\[
 \int(1-\cos(xu))d\omega_\diamond(u)
 \quad\text{versus}\quad
 \sum_{n\ge2}c_n(1-\cos(x\log n)).
\tag{T-91402.3}

The fully polarized form is a weighted sampling inequality on the exact
source range.  This aligned specialization is a preferred concrete attack,
not a proved conclusion.

## 9. Gamma-ladder reading

`L-91411` gives a second exact source chart:

```text
prime first chaos
+ positive gamma ladder
- one pole channel
```

at each safe tangent scale.  It may be used to construct the connection block
or a conservative realization of CPPD.  The three-scale recurrence still has
a nontrivial negative ladder after its scale signs are inserted, so the
one-pole statement alone does not prove (T-91402.2); see `R-91404`.

## 10. Binary rejection tests

Reject a claimed proof if it:

1. drops the short-jump Lévy compensation;
2. reuses the prime mode-split endpoint traces at `u=0` rather than the direct
   physical translation orbit;
3. treats the full long channel as negative after `L-91412` has split its
   positive endpoints from its adverse production;
4. replaces the signed completed source by total variation;
5. ignores arbitrary mixed delays or uses raw delay invariance of the model
   space;
6. omits one Hardy orientation or the bridge;
7. loses coefficient one;
8. proves only scalar diagonals;
9. uses numerical PSD scans as the all-packet theorem;
10. assumes the target screw Gram positive before constructing the source map.

## 11. Exact boundary

```text
prime packet factorization                            EXACT
continuous compensated packet factorization           EXACT
full completed source identity                        EXACT
positive production ledger                           EXPLICIT
adverse endpoint/production ledger                    EXPLICIT
deterministic connection                              EXPLICIT
CPPD coefficient-one domination                       OPEN / RH-EQUIVALENT
Riemann Hypothesis                                    UNPROVED
```
