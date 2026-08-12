# R-91404 — One pole tangent does not make the three-scale delayed recurrence finite-index

Claim ID: `R-91404`  
Status: **EXACT SCOPE FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91404`, `L-91411`, `L-91412`  
RH status: **unproved**

## 1. The true one-scale statement

`L-91411` proves that for one completed phase tangent at one safe line,

```text
continuous source = positive gamma ladder - one pole channel,
```

and that the Hardy compression of the pole channel is rank one.

This is an exact and useful simplification.

## 2. The invalid extrapolation

It is not valid to conclude that the coefficient-one Cauchy recurrence, the
full delayed screw form, or the completed Green defect has only one negative
square.

There are three independent reasons.

### 2.1 The recurrence uses three scales

The recurrence applies the signed coefficients

\[
 \alpha_1=-1,
 \qquad
 \alpha_2=\frac{17}{16},
 \qquad
 \alpha_4=-\frac1{16}
\]

to the radial differential observations at `a,2a,4a`.  In the source
normalization of `L-91404`, the middle gamma ladder enters with the opposite
sign from the first and fourth ladders.  It is not removed by the one-scale
pole decomposition.

### 2.2 The radial derivative creates double-pole ports

The operator

\[
 (1-c\partial_c)
\]

acts on the rung parameter.  A simple Cauchy pole is therefore accompanied by
its parameter derivative.  The resulting resident Hardy port has rank at most
two per rung, not one, and there are countably many gamma rungs.

### 2.3 Delays create resident and leakage channels

Raw delays do not preserve `K_Theta`.  The exact delayed colligation is

\[
 S_\tau g=T_\tau g+M_\Theta R_\tau g.
\]

Even when the resident observation of one simple pole has rank one, the full
physical delayed source contains the compressed resident family, its leakage
cocycle, both orientations, and the bridge.  These pieces cannot be deleted by
counting the rank of the undelayed scalar Hankel block.

## 3. What is retained

The ladder/pole chart remains valuable because it:

```text
replaces the plastic long-jump continuum by one source-typed pole at one scale;
gives explicit rank-one evaluation formulas;
identifies exact safe xi weights;
provides a canonical input for finite Schur complements and source sampling.
```

The compensated packet theorem `L-91412` is the correct route from this local
chart to the full delayed source.

## 4. Rejection rule

Reject any argument of the form

```text
one-scale negative pole has rank one
 -> complete delayed screw form has one negative square
 -> at most one off-line zero pair
 -> RH.
```

The first implication is false.  The three-scale signs, parameter derivatives,
compressed-delay leakage, opposite orientation, and bridge are load bearing.

## 5. Exact boundary

```text
one-scale pole Hardy compression                    RANK ONE EXACT
one-scale gamma ladder                              COUNTABLE POSITIVE PORTS
three-scale radial recurrence                       NOT ONE-POLE
raw delay preserves model space                     FALSE
full delayed recurrence finite negative index       NOT ESTABLISHED
CPPD domination                                      OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
