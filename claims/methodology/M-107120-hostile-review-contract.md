# M-107120 — Hostile review contract for the additive beta checkpoint

A review must independently verify:

1. the endpoint convention and the exact support `h<=(67-1)n` in `L-107120`;
2. the common-core change `n=ga`, `h=gr`, including squarefree and factor-67 exclusions;
3. preservation of the maximal horizon in the zero-abscissa comparison;
4. the Fourier normalization
   `widehat Lambda(t)=log(67) sinc^2(t log(67)/2)`;
5. the dyadic use of the classical Dirichlet-polynomial mean-value theorem;
6. uniformity of the tail estimate over all `Y<=X`;
7. that the retained low-frequency estimate is explicitly open;
8. that neither a fixed additive shift nor an endpoint value is substituted
   for the complete aggregate.

The replay checks finite grouping and reindexing algebra only. It does not
replay the classical mean-value theorem, the zero-abscissa theorem, the open
low-frequency estimate, or RH.
