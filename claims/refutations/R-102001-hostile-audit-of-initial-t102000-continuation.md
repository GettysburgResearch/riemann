# R-102001 — Hostile audit of the initial T-102000 continuation

Claim ID: `R-102001`
Status: **BINDING CORRECTION RECORD**
Created: 2026-08-21
RH status: **unproved**

The first continuation after `T-102000` contained five errors or overstatements.
They are corrected on the same branch and must not be reconstructed from the
superseded commits.

## 1. Missing squarefree gcd constraint

The displayed gcd sum in the first `L-102001` ranged over arbitrary `g,a,b`
with only `(a,b)=1`. That introduced spurious nonsquarefree gcd terms. The
correct condition is

\[
\mu^2(gab)=1.
\]

See audited `L-102001.9`.

## 2. Sum in place of the required product

The first `L-102002.4` displayed

\[
\operatorname{collar}_-^2\le A+B.
\]

The Cauchy AND-gate requires

\[
\operatorname{collar}_-^2\le AB.
\]

The abstract gate is correct only in the product form. Moreover, no canonical
map from a Vaughan divisor pair to a prime min--max occurrence has yet been
constructed.

## 3. Reversed right-survival telescoping

The first `L-102003` used the wrong sign in

\[
R_j-R_{j-1}=r_jR_j.
\]

For a finite truncation,

\[
\sum_{j=J}^{k}r_jR_j=1-R_{J-1},
\]

not `R_(J-1)`. Consequently, for a fixed least owner, greatest-owner mass
beyond every fixed power tends to the full least-owner mass. Joint survival
prevents a divergent marginal norm but does not suppress supercritical width.

## 4. False endpoint constant

The first `L-102004` claimed the auxiliary estimate

\[
\Delta_p\Psi(X)\le128\sqrt X.
\]

On the deep branch the leading coefficient approaches `192`, so the estimate
is false. Audited `L-102004` replaces it with the exact safe uncentered bound
and the stronger conclusion-relevant fact

\[
\|\Delta_{p_i}\Delta_{p_j}(\Psi-192\sqrt{\cdot})\|_\infty\le256.
\]

## 5. Off-by-one unsquared depth

With `Z=sqrt(T)`, two unsquared primes above `Z` already have product greater
than `T`. The first `L-102007` incorrectly placed the automatic threshold at
depth three. Audited `L-102006--L-102007` place it at depth two and retain the
squared-core factor in the threshold condition.

```text
initial gcd display                         CORRECTED
initial same-occurrence certificate         CORRECTED
supercritical survival suppression          REFUTED
512 / endpoint-128 amplitude claim          REFUTED
unsquared depth-three boundary              CORRECTED TO DEPTH TWO
Riemann Hypothesis                          UNPROVED
```
