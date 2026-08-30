# T-105670 — Two-ended all-rank Cauchy translation frontier

**Claim ID:** `T-105670`  
**Status:** all-rank CTI proved at both height endpoints; intermediate contact open  
**Date:** 2026-08-31  
**RH:** unproved

For every finite Cauchy packet:

1. `L-105661` proves strict constant-one CTI for all sufficiently small
   positive translations;
2. `L-105670` proves strict constant-one CTI for all sufficiently large
   translations;
3. rank one and rank two satisfy CTI at every height;
4. the global sharp `32/27` theorem of `L-105660` remains valid at every rank
   and height.

The new large-height asymptotics are

\[
\mathcal T_H={\kappa_K\over H}+O_K(H^{-2}),
\qquad
\mathcal O_H={n\kappa_K\over H}+O_K(H^{-2}),
\]

so

\[
\boxed{
{\mathcal O_H\over\mathcal T_H}\longrightarrow n.
}
\tag{T-105670.1}
\]

Thus the twice-translated model space has `n` times the leading overlap needed
by the one-step current at the remote endpoint. The constant-one theorem is
not asymptotically tight there except in rank one.

Any counterexample to arbitrary-rank CTI must now be a rank-at-least-three
packet at a finite intermediate height satisfying the explicit stationary
contact system of `L-105671`.

## Revised finite theorem ladder

```text
rank one CTI                              PROVED ALL H
rank two CTI                              PROVED ALL H
all-rank CTI near H=0                     PROVED
all-rank CTI for H sufficiently large     PROVED
sharp all-rank 32/27 domination           PROVED ALL H
MLC105656                                 REFUTED
FNI105658                                 OPEN
intermediate stationary contact exclusion OPEN
arbitrary-rank CTI all H                  OPEN
```

The remaining finite problem is no longer an endpoint, confluent, scaling or
large-translation issue. It is precisely:

```text
ISC105670 — exclude a nonpositive solution of the two scalar contact
             equations L-105671.2 and L-105671.3 for a rank >=3 Cauchy packet.
```

If `ISC105670` is proved, then `CTI105655` follows for every finite packet.
The existing cofinal common-zero/endpoint passage and the separate pointwise
Xi localization remain required according to the strength of the desired
conclusion.

## Xi significance

The degree-zero physical phase-overlap defect is now paid:

```text
at first contact;
at every sufficiently remote translation;
in the physical prefactor region of L-105662;
at every height for packets of rank at most two.
```

Only an intermediate, genuinely multipacket collision can survive.

## Exact status

```text
large-translation Laguerre limit             PROVED
remote CTI constant one                       PROVED ALL RANKS
stationary-contact ledger                     PROVED EXACT
ISC105670                                      OPEN
cofinal Xi passage                            OPEN
pointwise Xi localization                     OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVEN
```