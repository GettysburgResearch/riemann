# Prime-sieved row direct Mellin–Landau RH candidate

This standalone packet replaces the stale endpoint consumer of the parent prime-sieved proposal.

Core statement:

\[
c_X(j)\ge0\ \text{for every fixed row}
\quad\Longrightarrow\quad
\int_1^\infty c_X(j)X^{-s-1}dX
=\frac{C_j}{s^2}+\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}.
\]

No nontrivial off-line zeta zero cancels every `P_j`. Landau's theorem then gives the proposed RH conclusion.

```text
classification: complete unconditional proof candidate
accepted proof: no
RH established: no
```

Review `L-94200` first, then `L-96000`, `L-96001`, and `T-96000`.
