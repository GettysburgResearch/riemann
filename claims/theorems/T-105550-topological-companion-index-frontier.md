# T-105550 — Topological companion-index frontier

Claim ID: `T-105550`  
Status: **UNCONDITIONAL FINITE/REGULAR-WINDOW REDUCTION; 90% OPEN**  
Created: 2026-08-24  
Depends on: `L-105500`, `L-105550--L-105552`, `R-105550`  
RH status: **unproved**

## 1. Exact replacement of the omnibus flux

After reducing common `F,F'` factors, the companion

\[
E_\delta=F'+i\delta F
\]

has no real zero.  In the polynomial/global model,

\[
D=\#\{\text{distinct roots of }F\},
\quad
R=\#\{\text{distinct real roots of }F\}
\]

satisfy

\[
\boxed{R=D-2N_-(E_\delta).}
\tag{T-105550.1}
\]

The regular entire-window statement has only the literal endpoint bits of
`L-105500`.  Equivalently, `R` is the winding/Toeplitz index of the companion
Cayley ratio.

Thus the conclusion-bearing part of `MATRIXLERC105541` is topological: it is
the lower-half-plane partial index of the companion, not an arbitrary sum of
vertical, collar, and pole norms.

## 2. Ninety-percent normal form

For a cofinal sequence of regular Xi windows, let `D_T` be the reduced distinct
zero count and `N_-(T,delta)` the bad companion count.  Then

\[
\boxed{
N_0(T,2T)\ge D_T-2N_-(T,\delta)+O(1).
}
\tag{T-105550.2}
\]

Consequently the exact topological gate

\[
\boxed{
\mathrm{CPINDEX105550}:\qquad
N_-(T,\delta)<\left(\frac1{20}-o(1)\right)N(T,2T)
}
\tag{T-105550.3}
\]

implies more than ninety percent of the zeta zeros are on the critical line.
The count is independent of the fixed `delta>0` after common-factor reduction.

## 3. Energy plus separation lane

Let the compactified companion ratio factor as `B_+/B_-`.  By `L-105552`, a
sufficient quantitative lane is

```text
COMPSEP105550:
  all but o(N) bad companion zeros have a uniformly conditioned model-space
  kernel Gram and a uniform lower bound for |B_+| at those zeros;

HARDYENERGY105550:
  the corresponding Hankel Hilbert--Schmidt energy is below the separated
  rank threshold.
```

Together they imply `CPINDEX105550`.

`R-105550` proves that neither row may be removed.  Near-axis conjugate
cancellations can carry nonzero partial index/rank at arbitrarily small norm.
This is the precise obstruction which a direct winding theorem or a
source-owned companion-separation theorem must defeat.

## 4. Status

```text
reduced companion half-plane count          PROVED EXACT
Cayley winding / Toeplitz degree             PROVED EXACT
bad count = finite Hankel rank               PROVED EXACT
separated rank-energy conversion             PROVED EXACT
norm-only bad-count estimate                 REFUTED EXACT
CPINDEX105550                                 OPEN / RECORD-BEARING
COMPSEP105550 / direct winding estimate      OPEN
ninety percent for zeta                      UNPROVED
public record beaten                         NO
Riemann Hypothesis                           UNPROVED
```
