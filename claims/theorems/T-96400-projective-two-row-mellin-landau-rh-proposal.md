# T-96400 — Projective stopping-line two-row Mellin–Landau proposal

Claim ID: `T-96400`  
Status: **CANDIDATE COMPLETE UNCONDITIONAL RH PROPOSAL — INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-17  
Frozen base: PR #550 at `20646a78c3e8843001cb49ea0c9741f6d0d446f7`  
Depends on: `R-96400`, `L-96400`, `L-96401`, `L-96402`, and the exact frozen source/Hall inputs in the lock  
RH status: **proposed; not accepted**

## Statement

For every real `X>=1`, the canonical native component rows satisfy

\[
c_X(2)\ge0,\qquad c_X(3)\ge0.
\tag{T-96400.1}
\]

Consequently all nontrivial zeros of `zeta` lie on the critical line.

## Proof

`L-96400` builds one source-owned projective stopping-line transport.  Pending
rough incidences are refined, never observed twice.  At child endpoint below
`67`, `L-96401` terminalizes the incidence into a positive residual source and
a current-only nonnegative row bonus.  Every native source interval is used
exactly once, and the stabilized output equals the canonical native rows.
This proves (T-96400.1).

Assume a zero

\[
\rho,\qquad \frac12<\Re\rho<1.
\]

Set `s_0=rho-1/2`.  By `L-96402`, at least one of
`P_2(rho),P_3(rho)` is nonzero.  The Mellin transform of the corresponding
eventually nonnegative row has a nonreal pole at `s_0` on the line of its
rightmost singularities.

Landau's one-sign theorem forbids such a nonreal first singularity.  Hence no
zero lies to the right of the critical line.  The functional equation excludes
zeros to the left, proving the proposed RH conclusion.

## Independence from the endpoint compiler

No step uses:

```text
B_X or NEDB;
packing slack;
F_Lambda;
the PR #530 endpoint-to-RH consumer;
a J_Lambda-4sqrt(X) benchmark bridge;
ordinary/detail capacities;
a child-capacity promotion;
an activation-cell quantizer.
```

`R-96400` is retained to prevent the invalid packing/arithmetic conflation from
re-entering the proof.

## Review boundary

The Mellin algebra and no-common-zero calculation are exact.  The load-bearing
new theorem is the source-incidence equality and projective terminalization in
`L-96400`, together with the two-row terminal monotonicity in `L-96401`.
Until those are independently reconstructed, RH remains unproved.
