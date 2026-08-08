# Integration handoff — balanced Möbius core and reflected proposal audit

## Base

Apply on top of PR #229 frozen head:

```text
2fc74c11b9929f694d8c13d060c9d55b99dc9621
```

The continuation also audits:

- PR #158 exact Heath–Brown/Möbius packet;
- PR #165 terminal Euler replacement;
- PR #226 reflected Selberg proposal;
- PR #233 corrected `BTP(K)` boundary.

## New files

```text
L-23005  deep-contour closure for complete free lattices
L-23006  exact finite inverse-zeta boundary tensor
L-23007  common principal part of all finite inverse orders
R-23003  generic tensor and moving-order barriers
R-23004  finite cross-order polarization no-go
R-23005  terminal face count does not close balanced Möbius core
O-23001  surviving balanced corner map
O-23002  repaired reflected-proposal target
O-23003  reflected Selberg normalization audit
X-23001  exact finite inverse/principal-part regression
X-23002  exact first-cell packet mutation regression
```

## Main integration decision

Do not promote PR #226 `L-9517/T-9509` as a complete proof.

The reflected Hermitian Selberg identity is valuable and should be retained after
fixing the generalized-von-Mangoldt sign typo. But the endpoint-face count
controls only terminal rows. The exact fixed-logarithm source and the strongest
Euler partition leave an all-truncated balanced packet with the full
rightmost-zero exponent. The corrected source theorem continues to require
`BTP(K)`.

The claimed automatic mutation

```text
fixed q0=2 packet -> Delta_(2/3)^K M
```

is not exported by the packet algebra. Exact regression `X-23002` shows that
the packet reconstructs `mu` for all orders while first and higher geometric
Mertens differences differ.

## Safe merge order

1. Preserve PR #229 as the gap/readiness audit.
2. Add `L-23005`--`L-23007` and `R-23003/R-23004` as independent exact/proposed
   boundary results.
3. Add `R-23005` before reviewing PR #226 as a proof.
4. Retain `L-9516` only after the sign and critical-packet normalization fixes.
5. Return the full problem to a source-specific reflected `BTP(K)` plus an exact
   first-cell decoder.

## Current status

```text
free-lattice and terminal sectors          proposed closed
finite inverse hierarchy                   exact algebra closed
reflected Hermitian Selberg identity       proposed exact after local fix
terminal endpoint count as sole hinge      rejected
balanced reflected BTP(K)                  open
first-cell packet decoder                  open
RH                                         unproved
```
