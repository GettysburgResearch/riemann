# T-93271 - Peano/Hermite source-complete scale-innovation closure contract

Claim ID: `T-93271`
Status: **FULL UNCONDITIONAL CANDIDATE ARCHITECTURE; TWO EXPLICIT PRODUCERS OPEN**
Created: 2026-08-16
Depends on: `T-93270`, `L-93272`, `L-93273`, PR #379, and the reviewed centered-cubic criterion on PR #515
RH status: **unproved**

## Candidate architecture

The reset proof graph is

```text
positive three-stage factor-64 Peano source
    <-> positive Mellin smoothing
centered-cubic scale innovation
    <-> polynomially conditioned Schwartz transform
First-Hermite carrier field
    <-> exact Guinand-Weil zero-heat criterion.
```

The static arithmetic branch uses the exact balanced large-divisor Möbius form `B_C(X)` of `L-93273`. The carrier branch uses the finite-at-each-scale field `F_C(r,t)` of `L-93272`.

## Route A: centered cubic / Peano

If `SID_0` of (L-93273.4) holds, then the centered-cubic prime statistic has the required square-root/polylogarithmic bound. The reviewed Mellin criterion gives RH. Equivalently, one may prove the factor-64 prime bound of `T-93270` directly.

## Route B: First-Hermite heat

If `SID_H` of (L-93273.6) holds with the explicit normalization margin required by PR #379, then (L-93272.17) bounds the full First-Hermite prime polynomial below the gamma reserve. The first-Hermite scalar is nonnegative for every `q,t`; the terminal-pair theorem then gives RH.

## Interface audit

The composition does not use:

1. a block-count contradiction;
2. common-half-plane alignment as an upper bound;
3. source-blind positivity of second curvature;
4. absolute Gaussian prime domination;
5. a generic large sieve after absolute values;
6. Mertens square-root cancellation;
7. a macroscopic Selberg estimate;
8. a zero-free strip stronger than known unconditionally;
9. the factor-67 compiler.

The two open producers are not silently assumed. Either one would be RH-strength and must be proved by signed arithmetic dispersion.

## Exact boundary

```text
positive factor-64 source bank              PROPOSED COMPLETE EXACT
centered cubic / Peano positive dictionary  PROPOSED COMPLETE EXACT
cubic-to-First-Hermite transform            PROPOSED COMPLETE EXACT
source-blind positivity shortcut            REFUTED
absolute Gaussian shortcut                  REFUTED
SID_0 balanced Möbius dispersion            OPEN / RH-EQUIVALENT
SID_H carrier-resolved scale dispersion     OPEN / RH-EQUIVALENT
Riemann Hypothesis                          UNPROVED
```
