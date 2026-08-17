# Q4 continuation: finite odd-core preconditioning

The passive state of PR #563 can be converted at the critical \(1/\sqrt n\)
normalization into a literal finite packet.

Applying

\[
(\varepsilon+\delta_2)^{*2}
\]

to the logarithmic Q4 source cancels the dyadic denominator created by the
reciprocal state and its derivative. Every odd squarefree core then occupies
only the six levels

\[
m,2m,4m,8m,16m,32m.
\]

The preconditioner is stably invertible in critical scale because its
half-scale coefficient is \(2^{-1/2}<1\).

The complete same-core diagonal is \(O(\log^3X)\). The remaining theorem is
only the deterministic cross correlation between distinct odd squarefree
cores. A top-band sign-replacement example proves that no fibrewise passive or
diagonal argument can supply that cancellation.
