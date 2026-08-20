# T-99580 — Exact IHR67 attack and sharp proof boundary

Claim ID: `T-99580`  
Status: **UNCONDITIONAL REDUCTION AND NO-GO; IHR67 REMAINS OPEN**  
Created: 2026-08-20  
Frozen base: PR #649 at `433fd3662f7b2e4ba384ce64f196380e88624090`  
RH status: **unproved**

The direct proof attempt establishes four exact conclusions.

1. `L-99580` identifies `mathfrak H_67` with the relative-persistence stop-loss
   transform of the actual duplicated-67 threshold source and with an exact
   critical finite-difference operator.
2. `L-99581` proves that every hypothetical right-half critical-strip zero
   forces arbitrarily large positive and negative values of `mathfrak H_67`.
3. `R-99580` refutes generic duplicate-label positivity by an exact six-label
   counterexample.
4. `R-99581` records why positive-real Mellin values and the positive inverse
   renewal do not supply the missing sign.

The remaining theorem is the source-specific prime-log transport
`PLSLC99580`, or an equivalent owner-Carleson/cancellation theorem, for the
exact measure of `L-99580`.

```text
relative-persistence identity             PROVED EXACT
critical finite-difference identity        PROVED EXACT
off-line zero -> two-sided oscillation     PROVED EXACT
generic duplicate-label positivity         FALSE
positive-symbol shortcut                   INVALID
positive-renewal shortcut                  INVALID
prime-log monotone transport               OPEN / RH-BEARING
IHR67                                      OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```

No finite scan or abstract positivity surrogate is represented as a proof of
IHR67.
