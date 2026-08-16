# M-94200 — Adversarial review protocol for the four-adic endpoint-packing proposal

Reject the proposal at the first occurrence of any of the following:

1. A negative endpoint atom or a nonpositive radix-four response below the diagonal.
2. Different coefficients in the row, ordinary `q`, ordinary `4q`, detail or score coordinates.
3. Use of the first-crossing estimate on a residual that is not the live greedy residual.
4. A residue class invalidating either normalized cross-ratio inequality in `L-94200`.
5. Failure of the least-minimizer cancellation.
6. Substitution of a smooth surrogate for the exact sparse von Mangoldt dual `Y_4`.
7. Reversal of the one-sided endpoint-deficit inequality.
8. Cancellation of an off-critical Mellin pole by the explicit pole-subtraction term.
9. A prime-square moat with the wrong sign or only linear size.
10. Treating finite decimal replay as proof of the all-scale first-crossing theorem.

Preferred reconstruction: derive every square-root block identity symbolically, then use exact rational interval arithmetic only as a regression check.
