# Q4 aligned innovation simplification

A fresh audit of PR #345 gives an exact simplification which is useful but also a scope firewall.

For an aligned quarter-balanced row `(4n,4j)`, with `k=n-j` and `L=log 4`, the compact one-step current of `L-34401` satisfies

\[
\mathcal L_{4n,4j}(q_\circ)
=\log\frac{\binom{4n}{4j}}{\binom nj^4}-4L.
\]

The actual innovation is

\[
i_\circ=q_\circ-L\,\delta_4*b_4,
\]

and exact carry scaling gives

\[
\mathcal L_{4n,4j}(\delta_4*b_4)=Y_4(n,j).
\]

Hence

\[
\boxed{
I_\circ(n,j)
=\log\frac{\binom{4n}{4j}}{\binom nj^4}
 -4\log4-(\log4)Y_4(n,j).
}
\]

The aligned innovation is therefore prime-free. In particular it is only `O(log n)` because the binomial ratio is between one and `(n+1)^4` and `Y_4=O(log n)` explicitly.

Combined with PR #342's cofinal moat

\[
\Delta_4R\ge(\log2)n\log n,
\]

this proves scalar aligned-row innovation domination cofinally. It does **not** solve the independent-frequency physical block: the fact that the aligned carry row is prime-free is precisely why this scalar coordinate alone cannot be the all-zero pole frame.

A stacked proof with exact constants is being prepared separately; the remaining RH burden is the continuous/two-frequency Hermitian placement, not the aligned scalar arithmetic estimate.
