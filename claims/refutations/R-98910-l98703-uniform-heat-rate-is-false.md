# R-98910 — `L-98703`'s uniform fractional heat rate is false

Claim ID: `R-98910`  
Status: **PROVED UNCONDITIONAL REFUTATION**  
Created: 2026-08-18  
Frozen target: `L-98703` at PR #613 head `f28aa51a6d6740067202611d8ebda4be2ef0a1c9`

`L-98703` asserts, uniformly in the Gaussian center,

\[
\int |\mathscr B_{\theta,T}(\tau)|^2w_{T,\tau_0}(\tau)\,d\tau
\le (1+T)^{O(1)}
\exp\{96\theta T+O(T^{3/4}\log^2T)\}.
\]

Take `tau_0=0` and any fixed `0<theta<1/192`. By `L-98910`, the same left side
is

\[
 c_\theta T^{-2\theta-1}e^{T/2}(1+o(1)),
 \qquad c_\theta>0.
\]

Since `96 theta<1/2` and the remaining exponent is `o(T)`, the claimed upper
bound is eventually strictly smaller than the proved lower asymptotic. This is
a contradiction.

Therefore `L-98703` is false as stated. The coefficient `96` cannot be repaired
by a larger finite constant independent of `theta`: for every such constant
`C`, taking `theta<1/(2C)` gives the same obstruction. The uncentered tunable
fractional-intensity strategy cannot exclude zeros arbitrarily close to the
critical line.
