# T-91313 — Explicit one-sided endpoint-deficit consumer

Claim ID: `T-91313`  
Status: **PROVED RESIDENT CONDITIONAL CONSUMER**  
Created: 2026-08-14  
Depends on: `L-91377/L-91378`; the resident endpoint/WSTS implication  
RH status: **conditional on the producer input**

## 1. Exact benchmark and physical slack

By `L-91377`, the native benchmark is

\[
 J_\Lambda(X)=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log\frac Xn.
\]

Let `d_X>=0` be a finite physical row satisfying every native radix-four
capacity

\[
 \Xi_{d_X}(q)\le\Omega_X(q).
\]

By `L-91378`, its exact endpoint deficit is

\[
\boxed{
 \Delta_X(d_X)
 :=J_\Lambda(X)-\mathcal H(d_X)
 =\sum_qY_4(q)[\Omega_X(q)-\Xi_{d_X}(q)]\ge0.
}
\tag{T-91313.1}
\]

Positive radix-four renewal reconstructs ordinary feasibility.

## 2. Correct sign orientation

The resident endpoint dual inequality has the one-sided form

\[
\boxed{
 F_\Lambda(X)\le\Delta_X(d_X).
}
\tag{T-91313.2}
\]

Therefore the producer must give an **upper** bound on the nonnegative weighted
slack. A lower bound has the wrong orientation.

## 3. RH implication

If

\[
\boxed{
 \Delta_X(d_X)=o(\log^2X),
}
\tag{T-91313.3}
\]

then

\[
\limsup_{X\to\infty}
 \frac{F_\Lambda(X)}{\log^2X}\le0.
\tag{T-91313.4}
\]

The resident endpoint/WSTS theorem, including its deterministic prime-square
moat and Landau converse, then excludes every zero with real part greater than
one half and implies RH.

It is not necessary to prove an absolute two-sided estimate for `F_Lambda`; the
one-sided upper bound is exactly what the endpoint criterion consumes.

In particular, either a coefficient-one factor-67 recurrence or the
subcritical target-mass recurrence of `T-91312` supplies (T-91313.3), provided
it is established for the exact native packet.

```text
native benchmark and capacities           EXACT / L-91377
endpoint deficit = positive detail slack  EXACT / L-91378
producer upper bound orientation          EXACT
sub-log-squared native slack -> RH         RESIDENT CONDITIONAL
native producer                            OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVEN ABSENT PRODUCER
```
