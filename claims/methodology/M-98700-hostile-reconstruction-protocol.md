# M-98700 — Hostile reconstruction protocol for T-98700

Claim ID: `M-98700`  
Status: **REVIEW METHODOLOGY**

A reviewer should proceed in this order:

1. Recompute the Euler factors of `G_diamond`, `B_diamond`, and the fractional
   half powers.
2. Verify coefficientwise nonnegativity of `Q_theta` and `S_theta` and the
   factorization `1-B=2S(Q-S)`.
3. Reconstruct the atomwise Tao Gram and verify every source label under one
   and two prime updates.
4. Reconstruct the safe-line Gaussian Mellin identity, branch choice, and
   zero-safe dyadic numerator.
5. Verify the Hankel-contour asymptotic for a branch pole of arbitrary
   multiplicity and the local `tau`-energy separation.
6. Rebuild the finite generalized-prime Fock space in `L-98703` and check that
   the reflected heat kernel, parity, and Weyl translation act on the stated
   spaces.
7. Check the trace estimate, especially the `96 theta T` first-chaos term and
   the `T^(3/4)log^2T` terminal term.
8. Check that the finite-cutoff embeddings are source-covariant and that weak
   limits preserve the exact off-diagonal heat packet.
9. Reproduce the `N=26` overshoot and verify that no independent pointwise port
   is used.
10. Check the theta-versus-delta constants in the final contradiction.

Immediate falsifiers include:

- a missing source atom in the direct limit;
- a nonpositive finite Gram block;
- a trace term with fixed positive linear rate independent of `theta`;
- a pole/main mode surviving the Weyl subtraction;
- a branch-contour contribution with a smaller exponential rate than claimed;
- a hidden invocation of an RH-equivalent Mertens or prime-carrier estimate.
