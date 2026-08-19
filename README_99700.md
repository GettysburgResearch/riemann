# T99700 — Adaptive logarithmic-owner attack

This packet continues the exact scalar SHARP/owner frontier of PR #653.

**Scientific status:** new exact positive hierarchy and exact no-go theorem.
The Riemann Hypothesis remains unproved.

## Result

For
\[
\Lambda_k(n)=(\mu*(\log)^k)(n),
\]
every coefficient is nonnegative.  The complete family is an explicit graded
moment/Gram hierarchy.  For the 5:3 row source `q`, whose unsieved completion
`a=q*1` is coefficientwise positive,
\[
q*(\log)^k=a*\Lambda_k\ge0
\]
for every integer `k>=0`.

However, the duplicate-67 source
\[
\beta=(\delta_1-\delta_{67})*\mu
\]
defeats **every fixed logarithmic order**.  If `m` is a squarefree product of
exactly `k` primes, none equal to `67`, then
\[
(\beta*(\log)^k)(67m)=-k!\prod_{p\mid m}\log p<0.
\]
Thus no finite-order instruction of the form “differentiate/convolve until the
owner coefficients are positive” can close the global SHARP sign.

The exact positive inverse-renewal owner from PR #653 nevertheless supplies a
minus-one eigenfunction.  With
\[
g(n)=v_{67}(n)+1,\qquad a(n)=\beta(n)/g(n),
\]
and the owner law `P_n` of `L-99271`,
\[
\mathbb E_n[a(n/Q)]=-a(n).
\]
Hence `(-1)^t a(N_t)` is a stopped martingale.  Its Doob energy is exact, but
it is identically zero on every squarefree history with at most one factor
`67`.  A variance-only owner argument therefore has no coercivity on the main
Möbius parity sector.

The first non-degenerate square is phase-adaptive:
\[
\mathcal V_\gamma(n)
 =\mathbb E_n\left|
 a(n/Q)(n/Q)^{-i\gamma}+a(n)n^{-i\gamma}
 \right|^2.
\]
On the squarefree sector this is the explicit logarithmic-prime phase
dispersion
\[
\sum_{p\mid n}\frac{\log p}{\log n}|1-p^{i\gamma}|^2
\]
(with the exact doubled-67 owner weights when applicable).

## Boundary

```text
generalized von Mangoldt positivity            PROVED
graded owner Gram hierarchy                    PROVED
5:3 all-order positive completion              PROVED
every fixed-order duplicate-67 completion      REFUTED
minus-one owner martingale                      PROVED
untwisted variance coercivity                   REFUTED on native sector
phase-adaptive owner square                     PROVED EXACT DEFINITION/IDENTITY
global phase-owner Carleson estimate            OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
