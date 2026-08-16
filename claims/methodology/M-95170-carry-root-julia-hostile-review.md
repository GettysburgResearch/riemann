# M-95170 — Hostile review protocol for the carry root-Julia successor

Review in this order:

1. `R-95170`: check the continuous endpoint interpolation, the fixed-row Mellin transform, the no-common-zero algebra, and the exact use of Landau.
2. `L-95171`: recompute `g_2`, `b_2`, `Lambda_2`, both channel-swap identities, and PSD of every matrix carry current.
3. `L-95172`: verify the Markov normalization, alternating martingale, support table, and constants `25/12` and `4`.
4. `T-95170`: treat TFSE as open. Reject any reading that silently identifies matrix positivity with scalar CRCTP positivity.

Immediate falsifiers:

```text
an alpha<1/2 with all inverse rows eventually one-signed;
a common right-half-plane zero of E_2 and E_3;
a negative u_2^+ or u_2^- coefficient;
a failed coefficient-one channel identity;
a carry row with a non-PSD matrix sum;
a hidden charge of the full trace in TFSE;
an omitted unit/root boundary;
a claim that the finite replay proves TFSE or RH.
```

The finite verifier authenticates exact algebra only. It does not authenticate Hardy's theorem, Landau's theorem, the inherited Cycle-Debt consumer, TFSE, or RH.
