# T-97100 — Parity-safe root-Julia closure contract for the unique single scalar

Claim ID: `T-97100`  
Status: **CONDITIONAL CLOSURE CONTRACT — ONE EXPLICIT PRODUCER OPEN**  
Created: 2026-08-17  
RH status: **unproved**

The following chain is unconditional except at the boxed producer:

1. The unique scalar is `mathcal R_X=5c_X(2)+3c_X(3)`.
2. Its Mellin numerator factors as `-3(1-2^(-z))(2-2^(-z))` and does not vanish at an open-strip zero.
3. `L-97100` identifies its complete coefficient state with `6(delta_1-b_diamond)`.
4. `L-97101--L-97102` construct a positive coefficient-one two-channel Julia compiler which is covariant under every cumulative parity swap.
5. `L-97103` identifies its derivative prefix with `6[1-B_diamond(N)]`.

Therefore
\[
\boxed{
\mathcal B_\diamond(N)
=
\sum_{n\le N}\frac{b_\diamond(n)}{\sqrt n}
\le1
\quad(N\ge N_0)
}
\tag{T-97100.1}
\]
plus one verified nonnegative starting value implies eventual `mathcal R_X>=0`, and hence RH by the direct Mellin--Landau consumer.

A source-facing equivalent is:

> **Parity-covariant Julia trace extraction.** Construct a boundary functional on the positive channel process `Sigma_diamond` whose off-diagonal value is `B_diamond(N)` and whose normalized diagonal is one.

The positive compiler, parity covariance, martingale, and logarithmic energy are proved. The normalized trace-free boundary functional is not.

## Disposition of the compared routes

```text
PR #559 finite source bookkeeping             retained
PR #559 terminal scalar promotion             rejected by parity
PR #556 local annular reserve                  retained
PR #556 global annular promotion               rejected by parity
PR #561 parity theorem and no-go               retained
root-Julia positive channel                    proved here
RJTE trace-free extraction                     open / RH-bearing
Riemann Hypothesis                             unproved
```
