# T-101100 — Exact disposition of the requested CV/XD proof programme

Claim ID: `T-101100`  
Status: **SUBSTANTIAL UNCONDITIONAL HARDENING; CV, XD AND RH REMAIN OPEN**  
Created: 2026-08-21  
Base: PR #694 at `e6d923c1069f5a481abdf0769ca6d870a8b5ae4b`  
RH status: **unproved**

The requested programme contained two proposed terminal moves.

## CV move

```text
finite small-prime squaring
+ depth-one large-prime collar
+ one-sided variation
-> CV.
```

`L-101100` proves the literal completed collar is pointwise nonnegative, so its
negative variation is exactly zero.

`R-101100` proves that this does not imply the fixed CV scalar: finite
desmoothing is signed, and the adaptive cutoff produces an `X`-dependent
Mellin multiplier.

Thus

```text
literal completed collar variation       PROVED, ZERO
completed collar -> fixed CV              FALSE WITHOUT SIGNED DESMOOTHING
fixed CV                                  OPEN / RH-EQUIVALENT
```

## XD move

```text
largest-prime short/long split
+ short energy
+ long one-sided estimate
-> XD.
```

PR #694 proves the long estimate in the stronger eventual-positivity form and
refutes the proposed short energy.

`L-101101` proves the exact repair: the prime carrier lies in the antisymmetric
coordinate `(-1,+1)`; projection onto `(1,1)` cancels it and returns exactly
the minimal wavelet. Any regional absolute norm taken first is power-lossy.

Thus

```text
long-sector one-sided estimate           PROVED
short-sector SCME                        FALSE
carrier-preserving projection            PROVED EXACT
full XD after projection                 OPEN / RH-EQUIVALENT
```

## Common interface

`L-101102` gives the exact bridge

\[
\boxed{
\mathscr D h_\beta
=
(I-67^{-1/2}S_{67})D G_\mu.
}
\]

Therefore both requested routes meet at one signed, carrier-preserving
desmoothing/cross-core interface:

```text
positive completed source
    -> signed desmoothing on the literal SHARP source
    -> carrier-annihilating dyadic derivative
    -> physical minimal wavelet.
```

A valid closure must control that complete signed chain before absolute values.
The already-proved positive collar and eventual-positive long sector are two
sides of it; neither can be detached from its cancellation partner.

## Exact status

```text
literal squared-core collar negative variation    PROVED ZERO
long XD sector negative variation                  PROVED ZERO EVENTUALLY
finite-completion desmoothing                      SIGNED / OPEN
short/long carrier-preserving covariance           OPEN
SHARP-to-wavelet derivative bridge                 PROVED EXACT
CV                                                  OPEN / RH-EQUIVALENT
XD                                                  OPEN / RH-EQUIVALENT
Riemann Hypothesis                                  UNPROVED
```
