# M-100140 — Hostile review protocol

Review in this order:

1. Expand the Cauchy characteristic function and verify the `min(m,n)` kernel.
2. Reconstruct the coefficient-tail integral by finite Tonelli.
3. Check the signed Poisson square without complex conjugation.
4. Verify the logarithmic-variation bound for every shifted compact kernel.
5. Derive the RH Abel-summation tail estimate uniformly in the tail cutoff.
6. Check the subpower costs \(2^{M_L}\), \(y^{\tau_L}\), and the hockey-stick
   inverse mass.
7. Reconstruct the positive inverse and Landau implication from PR #659.
8. Verify the RH converse for OCE only on PR #660's frozen scalar and energy
   inputs.
9. Run the adjacent-block counterexample to every diagonal shortcut.
10. Do not label an RH-equivalent estimate as an independently proved lemma.

Immediate falsifiers:

```text
a missing conjugate in the positive Poisson norm;
a signed square represented as positive;
a coefficient-tail cutoff omitted;
a filter seminorm with power-sized growth;
a non-zero-safe inverse multiplier;
a diagonal estimate substituted for a tail estimate;
GPMOC or OCE marked proved by the finite replay;
RH marked established.
```
