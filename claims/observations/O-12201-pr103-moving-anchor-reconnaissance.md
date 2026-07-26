# O-12201 — PR #103 moving-anchor reconnaissance

Claim ID: O-12201  
Title: The atomized-minimum response table remains inside the moving-anchor Schur interval on an ordinary anchor ladder  
Status: EMPIRICAL  
Authoring agent: `gpt56-05-j`  
Created: 2026-07-26  
Dependencies: PR #103 midpoint data; PR #112 moment midpoints; T-12202 for interpretation  
Scope: one ordinate shift, ordinary high-precision discovery only  
Related counterexample candidates: none

## Parameters

The ordinate is PR #103's atomized-minimum shift `483/1024`, namely

\[
 T=\frac{20225875608343133989267}{2^{32}}.
\]

The old nodes are

\[
 u_j=2^{-40+2j},\qquad0\le j<16,
\]

and the old degree-14 moments use the midpoint values of PR #112's directed intervals.

For each positive moving anchor `t`, the sole new scalar was reconstructed through L-12204 from:

1. the old moment midpoints;
2. one direct completed-xi logarithmic-modulus value at `t`;
3. the same atomized count-deflation profile as PR #103.

At `t=1`, ordinary 80-decimal simultaneous Riemann--Siegel evaluation was used. For anchors in the easy half-plane, ordinary high-precision Euler-product evaluation was used. Neither route is directed here.

## Results

Write

\[
 \rho_t=\frac{c_0-\theta_0}{U_t-\theta_0}.
\]

The ordinary values are:

| `t` | `rho_t` | `c0-theta0` | `U_t-c0` |
|---:|---:|---:|---:|
| `1` | `0.2173358777225881` | `4.0503336772e-6` | `1.4585952792e-5` |
| `4` | `0.300473780006` | `2.8574980010e-12` | `6.6524765497e-12` |
| `16` | `0.344761070948` | `6.6412878739e-20` | `1.2622162769e-19` |
| `64` | `0.400977209010` | `2.6260480776e-28` | `3.9230724674e-28` |
| `256` | `0.513171421306` | `4.8529249075e-37` | `4.6038076891e-37` |
| `1024` | `0.657921701775` | `6.5552e-46` | `3.4083e-46` |
| `65536` | `0.934848384308` | `7.8467e-73` | `5.4685e-74` |
| `1048576` | `0.982566989088` | `7.1578e-91` | `1.2700e-92` |

Every tested midpoint lies inside the two-Schur interval. No candidate is allocated.

## Interpretation

The raw admissible width contracts very rapidly as `t` grows. L-12203 proves that this width is itself an old-cone response, so a tiny absolute upper slack at large `t` is not automatically a promising anomaly. It can be an inherited closure-at-infinity effect.

The dimensionless coordinate `rho_t` separates three useful regimes:

- small `rho_t`: target the lower square witness;
- `rho_t` near `1`: target the upper `(z-t)`-square witness;
- `rho_t` near `1/2`: balanced two-sided calibration.

For this ordinate, `t=256` is a balanced stress test, while `t=4` is the cleanest immediate production control: its point lies at `Re(s)=5/2`, its midpoint slacks are much larger than the old moment widths, and an independent directed Euler-product backend is available.

## Candidate programme

PR #103 preserves many ordinate shifts. A moving-anchor candidate is a pair `(shift,t)` for which a rigorous interval proves either

\[
 \sup(c_0-\theta_0)<0
\]

or

\[
 \sup(U_t-c_0)<0.
\]

The recommended discovery ladder is

```text
t in {1, 4, 16, 64, 256}
```

at every stored shift, followed by local rational refinement around the smallest `rho_t` and `1-rho_t`. The full proof requires only one new direct-xi point per pair.

## Proof boundary

- All values in the table are ordinary midpoint calculations.
- The old moments are midpoint values, not propagated intervals.
- No directed Schur threshold, direct-xi rectangle, or reduced-overlap certificate was generated.
- Large-`t` cancellation requires correlated interval arithmetic; independent endpoint widening may be useless.
- No `Z-####` candidate is allocated.

## Suggested next attack

Produce the exact `t=4` control first. Then scan the five-anchor ladder over every PR #103 shift using the reduced contraction and rank by the smaller of `rho_t` and `1-rho_t`.