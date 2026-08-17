# M-97100 — Hostile review protocol for the root-Julia single-scalar packet

Review in this order:

1. Recompute the identity
   `6-3(1-2^-z)(2-2^-z)/zeta(z)=6(1-B_diamond(z))`.
2. Reconstruct the local factors of `G_diamond` and `B_diamond` at `2` and at odd primes.
3. Verify `g_diamond(2^e m)=2e+2^-e` and all four nonzero inverse fibres.
4. Check the generalized von Mangoldt coefficients and both channel-swap equations.
5. Check the exact energy constants `4149/1666` and `16/3`.
6. Reconstruct the parity counterexamples to PRs #559 and #556, including the terminal `(2521,66)`.
7. Verify `M_*(N)=6(1-B_diamond(N))` and the integer-knot recurrence.
8. Reject any argument which infers `RJTE` from coefficientwise PSD, logarithmic energy, or `a_* * g_diamond>=0` without an explicit trace-free boundary map.

Immediate falsifiers:

- one wrong dyadic coefficient;
- a negative `u_diamond^+` or `u_diamond^-`;
- a failure of the channel-swap identity;
- a terminal factor-67 proof that omits cumulative history parity;
- promotion of `RJTE` or RH by the exact replay.
