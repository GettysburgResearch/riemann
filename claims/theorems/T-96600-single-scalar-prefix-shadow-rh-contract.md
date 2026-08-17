# T-96600 — A source-correct scalar prefix shadow would close the reciprocal-zeta route

Claim ID: `T-96600`  
Status: **CONDITIONAL CLOSURE CONTRACT — PRODUCER OPEN**  
Created: 2026-08-17  
RH status: **unproved**

Assume there is `N_0` such that

\[
\boxed{M_*(N)\ge0\qquad(N\ge N_0)}
\tag{T-96600.1}
\]

and `mathcal R_(N_0)>=0`. By `L-96600`,

\[
\mathcal R_{N+1}-\mathcal R_N
=M_*(N)\log(1+1/N)\ge0,
\]

so

\[
\mathcal R_X=5c_X(2)+3c_X(3)\ge0
\]

for every sufficiently large real `X`. The zero-safe fixed-row Mellin--Landau consumer of PR #551 then implies RH.

A sufficient all-prime induction is:

```text
SCPS — Source-Correct Prefix Shadow

For every finite initial prime product P, its next prime p, and every N,
M_P(N) >= p^(-1/2) M_P(floor(N/p)).
```

By `L-96601`, SCPS preserves nonnegativity at every sieve stage and yields (T-96600.1) after the finite active prime set is exhausted.

Neither (T-96600.1) nor SCPS is proved in this packet. The theorem records the exact complete producer interface and carries it through the independent reciprocal-zeta consumer without importing PR #552's failed transports.
