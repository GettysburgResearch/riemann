# R-105320 — The raw archimedean Cauchy model is not a one-percent Xi model

Claim ID: `R-105320`  
Status: **PROVED ASYMPTOTIC FIREWALL**  
Created: 2026-08-23

Before Wick cancellation, normalize the reciprocal coefficients by

\[
a_L(N)=\sum_{m\ge1}L^{-m}\Lambda^{*m}(N).
\]

For primes,

\[
a_L(p)={\log p\over L}.
\]

The prime number theorem gives

\[
\sum_{p\le e^L}{a_L(p)^2\over p}
={1\over L^2}
\sum_{p\le e^L}{(\log p)^2\over p}
\longrightarrow{1\over2}.
\tag{R-105320.1}
\]

Thus the degree-one source alone has a fixed positive amount of normalized
Hilbert--Schmidt energy. It cannot be absorbed into a `1%` perturbation of a
purely archimedean identity or Cauchy-power model.

This does not refute the low-order Pick route. It refutes only the comparison
that omits the linear prime carrier. `L-105320` removes that carrier by an
exact zero-free congruence before the trace/HS estimate is taken.

A second firewall remains: the identity

\[
L W^2/(L-A_X)=e^{-x}/(1-x)
\]

is a frozen safe-line model. It is not, by itself, the actual entire Xi
contour formula. Promoting the model to Xi without proving `WXFER105320` is
invalid.
