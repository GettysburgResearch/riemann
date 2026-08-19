# T-99440 — Quantitative three-interface hardening and corrected closure frontier

Claim ID: `T-99440`  
Status: **CORRECTED CONDITIONAL PROGRAMME — RH UNPROVED**  
Created: 2026-08-20  
Base: PR #649 at `433fd3662f7b2e4ba384ce64f196380e88624090`

Put

\[
W_X=5c_X(2)+3c_X(3),
\qquad
r=67^{-1/2},
\]

and define

\[
\mathfrak H_{67}(X)=W_X-rW_{X/67}.
\]

PR #649 proves:

1. \(W_X\) is one fixed zero-free Mellin witness;
2. eventual \(\mathfrak H_{67}(X)\ge0\) implies eventual \(W_X\ge0\);
3. eventual \(W_X\ge0\) implies RH by the fixed-row Mellin–Landau consumer.

`R-99440` proves that the positive causal current supplies only

\[
W_X-r^2W_{X/67},
\]

and the difference

\[
r(1-r)W_{X/67}
\]

is of order \(\sqrt X\) on the canonical positive row. It has a positive-real
Mellin pole and cannot be absorbed by the bounded-defect or calibration-
coboundary mechanisms.

Therefore the corrected conclusion-facing chain is exactly

\[
\boxed{
\mathrm{IHR67}
\Longrightarrow
W_X\ge0\ \text{eventually}
\Longrightarrow
\mathrm{RH},
}
\]

where

\[
\mathrm{IHR67}:
\qquad
W_X-67^{-1/2}W_{X/67}\ge0
\quad\text{eventually}.
\]

The following are not substitutes for IHR67:

```text
positive causal parent decomposition;
Radon–Nikodym child ownership;
alpha-child mass contraction;
bounded fixed-row calibration;
calibration coboundary telescoping.
```

They close source and composition interfaces but do not supply the missing
half-order sign.

Scientific status:

```text
three-point vulnerability audit        COMPLETE
two interfaces repaired                EXACT
one invalid composition                REFUTED QUANTITATIVELY
IHR67                                  OPEN / RH-BEARING
Riemann Hypothesis                     UNPROVEN
```
