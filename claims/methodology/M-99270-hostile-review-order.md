# M-99270 — Hostile review order for the three-vulnerability hardening

Review in this order.

1. Derive `beta(n)` and its Dirichlet series directly.
2. Recompute the scalar Mellin transform without using any row theorem.
3. Prove `K_A(s)=(1-A^-s)/s` is zero-free in `Re(s)>0`.
4. Check the compact-removal step for eventual smoothed positivity.
5. Prove local uniform convergence of the negative-part transform from
   `M_-(X)=O_epsilon(X^epsilon)`.
6. Reconstruct the specialized Landau proof and finite-abscissa step.
7. Audit the positive real zeta sign and cancellation at `s=1/2`.
8. Verify `g(n)=v_67(n)+1`, `beta*g=epsilon`, and the renewal equation.
9. Verify the generalized von Mangoldt owner and its probability normalization.
10. Compile both finite producers and compare the `10^8` verdict, minimum, and
    final prefix intervals.
11. Confirm every global status flag remains false.

Immediate falsifiers:

```text
a zero of K_A in Re(s)>0;
a nonholomorphic negative-part correction in Re(s)>0;
a missing real-axis singularity in the scalar continuation;
a mismatch in beta*g=epsilon;
a negative owner weight or owner mass not equal to one;
a disagreement between the two 10^8 scanners;
a claim that finite positivity proves the global tail;
a claim that RH has been established.
```
