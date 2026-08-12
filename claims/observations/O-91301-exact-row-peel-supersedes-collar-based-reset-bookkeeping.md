# O-91301 — Exact equality rows supersede collar-based reset bookkeeping

Claim ID: `O-91301`  
Status: **NORMATIVE LIFECYCLE / SCOPE CORRECTION**  
Created: 2026-08-12  
Depends on: `L-91112`, `L-91113`, `R-91101`, `L-91303`, `L-91306`  
RH status: **unproved**

## 1. Retained mathematics

`L-91303` proves a useful uniform Euler--Maclaurin expansion for the finite
equality seed and pins its continuum crossing to `c0 X+O(1)`.  `L-91306`
proves detailed asymptotics for the martingale-quantization collar and its top
endpoint ratio.

These statements remain useful diagnostics for approximate or discretized reset
implementations.

## 2. Superseded proof role

They are no longer load bearing for the preferred exact reset.

`L-91112` uses the exact equality rows and proves exact outer ordinary and
radix-four saturation, including the complete terminal annulus.  Consequently
no target/continuum error, quantization collar or terminal quotient collar is
present in that proof architecture.

Therefore the following historical description is superseded:

```text
the final reset gate is a bounded finite collar certificate.
```

## 3. Correct final interface

`L-91113` closes the full Boolean state of every prime through 53 and gives the
exact delayed rough-prime renewal.  `R-91101` proves that positivity of its
finite forcing does not imply positivity of the underlying `(L,R)` state by
coefficientwise inversion.

The final reset gate is instead:

```text
construct a capacity-faithful positive allocation of the delayed rough-prime
renewal, preserving coefficient-one score transfer and bounded additive debt.
```

## 4. Lifecycle

```text
L-91303 finite Euler correction       RETAINED DIAGNOSTIC / NOT LOAD BEARING
L-91306 collar localization           RETAINED DIAGNOSTIC / NOT LOAD BEARING
L-91112 exact equality-row peel        PREFERRED OUTER RESET
L-91113 Boolean forcing/renewal        PREFERRED ARITHMETIC INTERFACE
R-91101 rough-prime scope correction   NORMATIVE
RH                                    UNPROVED
```
