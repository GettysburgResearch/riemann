# Four-adic annular hardening: the direct two-row Mellin--Landau successor

## Executive verdict

The `J_Lambda/P_Lambda/F_Lambda` distinction raised in PR #541 is decisive. The old annular endpoint consumer cannot be repaired by declaring exact native saturation: saturation gives `H=P_Lambda`, while the arithmetic gap `F_Lambda=J_Lambda-P_Lambda` remains.

The strongest successor bypasses the endpoint benchmark completely.

For each fixed row define

\[
 a_j(X)=c_X(j)-c_{X/4}(j).
\]

Its Mellin transform is

\[
 (1-4^{-s})\left[
 \frac{C_j}{s^2}
 +\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}
 \right].
\]

Only rows two and three are needed. Their cancellation polynomials cannot vanish simultaneously in `Re z>0`; the proof reduces to

\[
 -3(a-1)(a-2)=0,\qquad a=2^{-z},
\]

which is impossible there. Therefore positivity of the two annular rows for all endpoints directly implies RH by Landau, with no `J/P/F` identity, no full SHARP telescope, no prime-square moat, and no large-row asymptotic.

## What did not survive

The PR #535 four-block formula is not sufficiently derived to serve as a proof. The PR #537 `FRONTIER-CHAIN` groups by a fixed product while requiring three distinct logarithmic locations inside that same owner, so its stated convex packet transition does not compose.

Neither object is imported.

## Exact remaining frontier

The entire route is now reduced to

\[
 \mathrm{TAP4}:\quad
 a_2(N)\ge0,\ a_3(N)\ge0\qquad(N\in\mathbb Z_{\ge1}).
\]

Real endpoints add no difficulty: every unit cell is affine in `log X`.

A long-double Kahan scan covered every integer through `150,000,000` in both rows. A separate double scan reached `250,000,000`. No negative value was found. The full average-binomial inverse was also reconstructed at selected endpoints, and an unsmoothed-step mutation was rejected. These are strong falsification results, not a proof of the infinite theorem.

## Status

```text
normalization firewall                 proved
annular fixed-row transform            proved
exact two-row noncancellation          proved
direct TAP4 -> RH consumer              proved
TAP4 finite scan to 150m long double   passed
TAP4 symbolic all-integer proof         open
unconditional RH proof                  not obtained
Riemann Hypothesis                      unproved
```
