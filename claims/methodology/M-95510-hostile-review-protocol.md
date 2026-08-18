# M-95510 — Hostile review protocol

1. Freeze PR #580 at `812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05`.
2. Reconstruct `A^2=D+X_cross` and the closed-sector identity
   `X_cross=S_H+E_H` before using one-sidedness.
3. Check that `X_cross>=-D`; no arithmetic hypothesis enters this lower bound.
4. Distinguish `O(log^A)`, `X^o(1)`, and a single fixed `O(X^epsilon)` bound.
   UOSACF requires every epsilon.
5. Apply the stable inverse only after checking its l1 mass `64/21`.
6. Verify Mellin convergence separately for each half-plane `Re s>delta>0`.
7. In L-95511, keep the `J_1` channel, real band endpoints, oddness,
   squarefreeness and `(d,ab)=1`.
8. In the squarefree expansion use `lcm(h^2,e)`, not the product `h^2e` unless
   coprimality has separately been established.
9. Treat moment compression as a rewriting theorem, not a cancellation bound.
10. Treat UOSACF and RH as open.
