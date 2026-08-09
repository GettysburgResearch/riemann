# Exact Q4 aligned innovation bound derivation

For future stacking on PR #345, let `L=log 4` and use its compact current `q_circ` and actual innovation `i_circ=q_circ-L delta_4*b_4`.

On an aligned row `(4n,4j)`, `k=n-j`, the own compact current is

\[
Q_\circ
=\log\binom{4n}{4j}-4\log\binom nj-4L.
\]

The delayed gauge is exactly `L Y_4(n,j)`, hence

\[
I_\circ
=\log\frac{\binom{4n}{4j}}{\binom nj^4}
 -4L-LY_4(n,j).
\]

The binomial ratio lies between `1` and `(n+1)^4`, while

\[
|Y_4(n,j)|\le3\lfloor\log_4n\rfloor+1.
\]

Thus, for `n>=2`,

\[
|I_\circ(n,j)|\le21\log n.
\]

PR #342 gives, for `n>=12005^2` on the quarter-balanced cone,

\[
\Delta_4R\ge(\log2)n\log n.
\]

Using `log2>1/2`, `log n<=sqrt(n)`, and `sqrt(n)>=12005>882`,

\[
I_\circ^2\le441\log^2n<\Delta_4R.
\]

This closes the scalar aligned innovation inequality cofinally. It does not close the independent-frequency physical block.
