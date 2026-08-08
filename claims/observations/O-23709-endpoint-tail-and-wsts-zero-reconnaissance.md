# O-23709 — Endpoint-tail and zero-charge reconnaissance

Observation ID: `O-23709`  
Status: **FLOATING RECONNAISSANCE — NOT A PROOF CERTIFICATE**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Target: `T-23706`

## 1. Endpoint atoms

Using ordinary IEEE double precision, I evaluated the exact finite formulas of `L-23717` at representative endpoints.  For every listed endpoint, every weighted ordinary-prime suffix was nonpositive:

```text
T = 10, 20, 50, 100, 223, 500, 1000, 2000, 10000.
```

The largest suffix was always the final, tiny negative suffix near the largest prime below `T`; no positive `A_T(z)` was observed.

This is discovery evidence only.  The endpoint `T=223` is deliberately included because the analogous **complete prime-power** total is slightly positive there.  The ordinary-prime radical/squarefull distinction is therefore load bearing.

## 2. Dyadic WSTS shells

For

\[
Y=\lfloor X/2\rfloor,
\]

I evaluated the ordinary-prime shell charge from its direct finite definition.  The maximum positive weighted suffix was zero, to floating precision, at

```text
X = 100, 200, 500, 1000, 2000, 5000,
    10000, 20000, 50000, 100000,
    200000, 500000, 1000000.
```

The total weighted shell residual was strictly negative at every tested endpoint; representative values were approximately

```text
X=1,000       -0.75142024
X=10,000      -1.15924242
X=100,000     -1.60271854
X=1,000,000   -2.02504708
```

The final suffix near the largest prime was negative and approached zero from below.

## 3. One-crossing shell profile

At the tested dyadic endpoints the finite shell residual `s_(X,Y)(q)`, viewed on all integer columns, changed sign exactly once.  Representative last-positive/first-negative positions were

```text
X=1,000       141 / 142
X=10,000      1408 / 1409
X=100,000     14085 / 14086.
```

The ordinary-prime restriction inherited the same one-crossing order.  This suggests a stronger possible proof route:

```text
finite shell one-crossing
+ nonpositive total weighted shell mass
-> every weighted upper tail is nonpositive.
```

The total mass is itself RH-bearing and is not proved here.

## 4. Cumulative fifth-aligned shell

A separate floating scan of the cumulative fifth-aligned inverse state found

```text
minimum over integer endpoints through 1,000,000:
N=2, C(N)=0.963707068932...

negative integer endpoints: 0
C(1,000,000)=6.20202418308...
```

This supports the independent centered base-five route on the same branch.  It does not certify the cofinal sign or `CDHB(5)`.

## 5. Status boundary

None of the numbers above is directed interval arithmetic.  They may guide symbolic review and mutation selection only.  They prove neither `AWTO`, `WSTS`, `CDHB(5)`, nor RH.
