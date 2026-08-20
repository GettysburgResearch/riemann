# R-100161 — Finite Euler-squaring positivity does not descend through a positive inverse

Status: **PROVED EXACT OPERATOR FIREWALL**  
Created: 2026-08-20  
RH status: **unproved**

PR #677 proves positivity of a finite Euler-squared completion

\[
A_Z=(I+67^{-1/2}S_{67})^2\prod_{p\le Z,\,p\ne67}(I+p^{-1/2}S_p)
\]

through a large corridor. A tempting adaptive strategy is to choose `Z=Z(X)` so that every endpoint `X` lies inside the proved corridor and then invert `A_Z` to recover the native scalar.

This does not preserve positivity.

For one prime factor, with `r=p^{-1/2}` and zero extension below one,

\[
\boxed{
(I+rS_p)^{-1}
=\sum_{k\ge0}(-r)^kS_p^k,
}
\]

where at every fixed endpoint the sum truncates finitely. The coefficients alternate in sign for every `r>0`. The squared 67 factor has the same obstruction:

\[
(I+rS_{67})^{-2}
=\sum_{k\ge0}(-1)^k(k+1)r^kS_{67}^k.
\]

Hence neither the one-prime inverse nor the finite product inverse is a positive operator on endpoint functions.

Consequently

```text
A_Z h >= 0 pointwise
```

does not imply

```text
h >= 0 pointwise
```

by a positivity-preserving desmoothing argument. Any successful adaptive finite-completion closure must exploit signed cancellation in the alternating inverse. That cancellation is precisely the critical arithmetic not supplied by the positivity corridor itself.

The infinite-completion route is separately forbidden by PR #677 because it changes the detector to `(1-67^(-2z))/zeta(2z)` and removes the original reciprocal-zeta poles.
