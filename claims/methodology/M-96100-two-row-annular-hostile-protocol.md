# M-96100 — Hostile protocol for the two-row annular frontier

Methodology ID: `M-96100`  
Status: **REVIEW AND FALSIFICATION PROTOCOL**

Review in this order:

1. Re-derive `h_2` and `h_3` from the original average-binomial inverse.
2. Verify the exact single-sum annular formula `L-96100.7`.
3. Check that every breakpoint is an integer and reproduce the logarithmic interpolation identity `L-96100.11`.
4. Re-derive the Mellin scaling factor `1-4^{-s}` without changing the lower integration limit.
5. Verify the explicit formulas for `P_2` and `P_3` and the factorization `-3(a-1)(a-2)`.
6. Audit the exact hypotheses and conclusion of Landau's theorem.
7. Search for a single integer `N` with `a_2(N)<0` or `a_3(N)<0`.

The retained scans are deliberately classified as falsification evidence. They do not prove `TAP4`. A proof of `TAP4` must give a symbolic sign mechanism for all integers, not a larger finite cutoff.
