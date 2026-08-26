# T-102930 — Primewise flat gauge and sparse endpoint owner normal form

Claim ID: `T-102930`  
Status: **MAJOR UNCONDITIONAL SOURCE/GUAGE REDUCTION; RH UNPROVED**  
Created: 2026-08-25  
Base: PR #719  
RH status: **unproved**

`T-102920` proved that the scalar completion-temperature path is a flat gauge
on one fixed detector-bearing source. `L-102901--L-102904` strengthen this to
an independent temperature coordinate at every labelled prime.

## 1. Infinite-dimensional flatness

For every real or complex temperature vector,

\[
\boxed{
\sigma_{\mathbf t}*\sigma_{\mathbf1-\mathbf t}
=\Gamma_{1/2}.
}
\]

Every coordinate connection is flat and all mixed curvatures vanish. The two
labels at `67` remain distinct.

## 2. Canonical default and sparse exceptions

The unique local energy-minimizing and first-chaos-balanced value is

\[
t_p=1/2.
\]

A finite source-owned set of owner, discrepancy, activation, or boundary
labels may instead use endpoint temperatures `0` or `1`. The complete tensor
energy changes by only

\[
\exp\!\left(O\!\left(\sum_{p\in S}1/p\right)\right),
\]

and hence by at most a power of `log Y` on a finite horizon.

At an endpoint, the selected prime has one unique unsquared placement and one
unique squared placement between the complementary factors. Thus no critical
owner is split between two factor histories.

## 3. Endpoint-color normal form

Writing

\[
M=(E+C)/2,
\qquad D=(E-C)/2,
\]

one has

\[
EC=M^2-D^2,
\qquad
D^2=\frac14x^2(1-x)^2.
\]

Every nonempty endpoint-color Walsh variance begins at squared activity. The
only critical mean coordinate is the arithmetic midpoint square. Its transfer
to the geometric midpoint square is a two-sided subcritical gauge beginning at
order `p^-1`.

## 4. Consequence for the two live coordinates

In the stopped-current coordinate, all external owner and internal discrepancy
primes may be assigned endpoint gauges. Only the undistinguished core remains
midpoint-polarized.

In the temperature-zero coordinate, the same operation leaves the scalar
transition zero unchanged because the complete product source is unchanged.

Thus `SGIC102890` and `CTZD102897` may both be reconstructed in the following
normal form:

```text
sparse source-owned critical labels:
  endpoint temperatures, unique factor placement;

undistinguished arithmetic core:
  midpoint temperature, minimum energy;

all endpoint-color variance:
  squared/higher-prime-power polylog ledger;

remaining conclusion-bearing object:
  the carrier-recombined physical orientation of the arithmetic midpoint core.
```

Call that final normal-form interface `PCOI102930`. It is not a third
independent criterion: it is a source/gauge-normalized form of the existing
`SGIC102890` / `CTZD102897` endpoint difficulty.

## Exact boundary

```text
primewise complementary factorization       PROVED EXACT
coordinate flatness and zero curvature       PROVED EXACT
unique local energy minimizer                PROVED
sparse endpoint energy cost                  PROVED POLYLOG
unique endpoint owner placement              PROVED EXACT
Walsh variance begins at squared activity     PROVED EXACT
owner/gauge ambiguity                         REMOVED
PCOI102930 midpoint-core orientation          OPEN / RH-BEARING
SGIC102890                                    OPEN / RH-BEARING
CTZD102897                                    OPEN / RH-EQUIVALENT
Riemann Hypothesis                            UNPROVED
```

`R-102873` is binding: the primewise gauge cannot orient the physical product
source-blindly.
