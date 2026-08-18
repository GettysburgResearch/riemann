# R-97900 — No fixed positive scalar-to-mass angle is an all-history Bellman cone

Claim ID: `R-97900`  
Status: **PROVED GENERIC MECHANISM-CLASS NO-GO THEOREM**  
Created: 2026-08-18  
Depends on: `L-97900`, divergence of the prime reciprocal sum  
RH status: **unproved**

## Theorem

Fix either the logarithmic `5:3` kernel `Q_*` or its scale-four annulus `A_*`.
There is no constant `eta>0` such that

\[
 F_{P_{61}Q}^K(X)\ge \eta M_{P_{61}Q}^K(X)
 \tag{R-97900.1}
\]

holds for every finite squarefree rough-prime product `Q` and every sufficiently
large endpoint `X`.

More strongly, for every `eta>0` there is a finite rough set `Q` and an `X_0`
such that

\[
 0<F_{P_{61}Q}^K(X)<\eta M_{P_{61}Q}^K(X)
 \qquad(X\ge X_0).
 \tag{R-97900.2}
\]

## Proof

By `L-97900`, the limiting ratio is

\[
 \kappa(P_{61})
 \prod_{p\in Q}{p-1\over p+1}.
 \tag{R-97900.3}
\]

Now

\[
 \log {p-1\over p+1}
 =\log\left(1-{2\over p+1}\right)
 \le-{2\over p+1}.
\]

The sum of reciprocals of the primes at least `67` diverges, so the product in
(R-97900.3) tends to zero as `Q` exhausts the rough primes. Choose a finite `Q`
for which the limit is below `eta/2`. The asymptotic in `L-97900` then gives
(R-97900.2) for sufficiently large `X`.

## Meaning

The repaired small-prime estimate

\[
 {1\over42}M_{P_{61}}^{A_*}\le F_{P_{61}}^{A_*}
\]

is a true base theorem. It cannot be propagated through arbitrary rough
histories by any Bellman argument that retains a fixed positive aperture.
The obstruction is structural, not a defect in the constant `1/42`.

This no-go theorem does **not** refute:

```text
scalar positivity F_P>=0;
the Euler-minus cone LBP67;
completed-parity Lorenz feasibility CPSL67;
the nonlocal current inequality NCBI67;
or RH.
```

It proves that a successful closure must use the unnormalized future quotient
profile, or an aperture that is allowed to decay with the actual installed
prime set.
