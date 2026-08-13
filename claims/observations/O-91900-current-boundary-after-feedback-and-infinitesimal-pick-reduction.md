# O-91900 — Current boundary after feedback and infinitesimal Pick reduction

Observation ID: `O-91900`  
Status: **CURRENT FAIL-CLOSED HANDOFF**  
Created: 2026-08-13  
RH status: **unproved**

## Exact corrections

```text
diffuse radial source alone excludes atomic output
    FALSE;

a nonlocal Friedrichs feedback creates a point eigenvalue
    EXACT;

RLSL interval-module locality
    STILL SUFFICIENT BUT MUST BE PROVED, NOT INFERRED.
```

## Exact advances

```text
abstract Birman--Schwinger/small-gain theorem       exact;
safe-real Pick matrix -> finite return operator     exact;
negative Pick index -> gain-above-one count          exact;
perturbation determinant / feedback entropy          exact;
moving-Cauchy covariant identity                     exact;
all compatible connections -> finite skew-gauge LMI exact;
infinitesimal safe Caratheodory criterion             proposed complete;
all actual-Xi one/two-node infinitesimal packets      proposed unconditionally positive;
three-node threshold sharp in a rational control     exact.
```

## Strongest new structural picture

An off-line zero may be interpreted in two different but compatible ways:

```text
radial picture:
    a pure-point depth output;

feedback picture:
    a unit-gain crossing / bound-state birth.
```

The first is excluded by a genuinely interval-local source lock.  The second
is excluded by completed safe-real small gain.  Source diffuseness without
locality excludes neither.

## Preferred attack order

1. Hostile-review `L-91905`, especially the centered Hadamard grouping and
   differentiated convergence.
2. Attack the first unknown interpolation order `N=3` for the actual Xi
   logarithmic-derivative kernel.
3. In parallel, construct the source-ordered skew gauge of `L-91903` from the
   completed Julia ports.
4. Use the finite dual LMI to search for minimal adverse packets rather than
   relying on generic numerical PSD scans.
5. Keep the RLSL locality route alive only if an actual radial module law is
   produced.

## Exact remaining gates

### Linear infinitesimal gate

For every finite positive rational tuple prove

\[
 \left(
  \frac{
   \xi'/\xi(1+q_i)+\xi'/\xi(1+q_j)
  }{1+q_i+q_j}
 \right)_{i,j}
 \succeq0.
\]

This is RH-equivalent by `L-91904`.  Orders one and two are closed in the
proposed theorem `L-91905`; order three is the first possible obstruction.

### Finite-displacement small-gain gate

For every rational `u` and finite rational packet prove

\[
 K_u[\mathbf q]\preceq I.
\]

A constructive sufficient route is a source-ordered skew connection satisfying
the finite LMI of `L-91903`.

### Locality alternative

Prove RLSL interval by interval.  `R-91900` shows why no weaker inference from
source diffuseness is valid.

## Current exact boundary

```text
one/two-node infinitesimal positivity      PROPOSED COMPLETE
three-node actual-Xi positivity             OPEN
all-node infinitesimal positivity           OPEN / RH-EQUIVALENT
finite safe-return small gain               OPEN / RH-EQUIVALENT
completed skew connection                   OPEN
radial interval locality                     OPEN / RH-EQUIVALENT
Riemann Hypothesis                           UNPROVED
```
