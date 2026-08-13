# O-91301 — Lifecycle after the exact equality-row peel refutation

Claim ID: `O-91301`  
Status: **NORMATIVE LIFECYCLE / SCOPE CORRECTION**  
Created: 2026-08-12  
Corrected after: `R-91102`  
Depends on: `R-91102`, corrected `L-91112`, `L-91113`, `R-91101`, `L-91303`, `L-91306`  
RH status: **unproved**

## 1. Refuted shortcut

The load-bearing identity proposed in historical `L-91112`,

\[
 b_X^\star(m)
 =\int_m^X L(X/s)\partial_sb_s(m)ds,
\]

is false.  The integral produces the continuum Volterra seed, not the exact
finite Riemann-sum seed.  `R-91102` gives the exact counterexample `X=3,m=2`.

Therefore the claimed exact finite outer peel, terminal saturation and zero-debt
score split are withdrawn.

## 2. Retained finite route

`L-91303` and `L-91306` are again load bearing:

```text
L-91303  finite Euler correction, c0 X+O(1) splice, parity/knot packets;
L-91110  positive martingale quantization;
L-91111  positive width-three collar;
L-91306  terminal quotient localization;
L-91109  finite parity shadow;
L-91113  sixteen-prime Boolean forcing and delayed rough-prime renewal.
```

The continuum endpoint frame and the positive component-row formula retained in
corrected `L-91112` remain useful, but they do not identify the finite seed
exactly.

## 3. Two independent remaining gates

The corrected reset has two separate obligations:

1. **finite discretization/capacity lift:** transport the Euler correction,
   positive quantization collar and bounded terminal quotient cells through the
   three-integer divisor stencils and the finite parity shadow;
2. **delayed rough-prime allocation:** allocate the globally positive Boolean
   forcing between the current state and the contracted rough-prime copies of
   `(L,R)` with coefficient-one score transfer.

`R-91101` proves that the second cannot be replaced by coefficientwise inversion.
`L-91307` proves the rough renewal is critical and requires a mixed two-state or
explicit boundary-port allocation.

## 4. Lifecycle

```text
historical L-91112 exact finite peel        REFUTED
corrected L-91112 infinitesimal/component rows RETAINED
L-91303 finite Euler correction             LOAD BEARING
L-91110/L-91111 quantization/collar          LOAD BEARING
L-91306 terminal localization               LOAD BEARING
L-91113 Boolean forcing/renewal              LOAD BEARING
R-91101/R-91102 scope corrections            NORMATIVE
finite capacity lift                         OPEN
rough-prime mixed allocation                  OPEN / RH-BEARING
RH                                            UNPROVED
```
