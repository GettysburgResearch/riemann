# X-12101 — Positive-anchor Christoffel moment ladder

## Purpose

PR #117 showed that adjoining the critical-line node `u=0` introduces one new
response moment and lifts the complete direct-xi half-line cone from degree 14
to degree 15.

X-12101 proves and tests the more general fact that **every positive anchor**
introduces one moment. Unlike the zero anchor, one positive anchor creates a
two-sided scalar gate. Several anchors form a Christoffel/Stieltjes ladder that
raises the complete response degree once per new direct-xi value.

For the PR #103 table:

```text
old nodes          16
old complete degree 14
m new anchors      m new direct-xi points
new complete degree 14+m
```

No new zero-count computation and no reevaluation of old primitives is needed.

## Exact checker

`verify.py` uses only Python integers and `fractions.Fraction`. It reconstructs:

1. signed divided differences of the one-anchor scalars;
2. every transformed moment through the recurrence
   
   ```text
   previous_k = new_(k+1) + w new_k;
   ```
3. the final `H0` and `H1` Hankel matrices;
4. exact fixed-vector quadratic forms;
5. exact unpivoted rational LDL pivots for positive controls;
6. the complete result digest.

It recomputes the final moments in increasing and decreasing anchor order and
requires exact equality. It rejects unordered or repeated anchors, Boolean
integers, zero or wrong-dimensional vectors, duplicate/decorative check IDs,
false claimed quadratics, and zero LDL pivots.

### Positive synthetic control

A five-atom positive measure supplies old moments through degree four and exact
one-anchor values at

```text
w = 1/2, 3/2.
```

After both transforms the checker proves the complete degree-six cone positive.
The retained verification digest is

```text
0423469c646627ca5d9c5c2d21bf67638c3e7f36cf8f350b5b92d0aedd2cb196.
```

### Negative synthetic control

The second anchor value is changed by exactly `1/100`. The exact vector

```text
(7064, -6917, 1497, -85)
```

then gives the `H0` square response

```text
-987306740595163 / 1734163200 < 0.
```

The retained verification digest is

```text
3e9234290746c786f22522d0577ac76d4f85c7d4591d7b7156d8dd2d9552d6dc.
```

These are algebraic controls, not Riemann-xi values.

## Reproduction

```bash
python experiments/X-12101-positive-anchor-ladder/verify.py \
  experiments/X-12101-positive-anchor-ladder/certificates/synthetic-positive.json

python experiments/X-12101-positive-anchor-ladder/verify.py \
  experiments/X-12101-positive-anchor-ladder/certificates/synthetic-negative.json

python -m unittest discover \
  -s experiments/X-12101-positive-anchor-ladder/tests -v

python -m compileall -q \
  experiments/X-12101-positive-anchor-ladder/verify.py \
  experiments/X-12101-positive-anchor-ladder/reconnaissance.py \
  experiments/X-12101-positive-anchor-ladder/tests
```

## Ordinary PR #103 reconnaissance

`reconnaissance.py` reads the committed directed old moment table and atomized
count profile, replaces the old intervals by midpoints, and evaluates new
completed-xi points using ordinary `mpmath` Riemann--Siegel arithmetic.

Default anchor packet:

```text
1/8, 3/16, 1/4, 3/8, 1/2, 3/4, 1
```

Example:

```bash
python experiments/X-12101-positive-anchor-ladder/reconnaissance.py \
  --dps 60 \
  --output /tmp/positive-anchor-scout.json
```

This is intentionally not part of the exact checker’s trust boundary.

## Candidate packets

### PA-1

```text
anchors       1
new points    1
final degree  15
```

At the current midpoint, the two scalar boundary distances are approximately
`4.05e-6` and `1.46e-5`. It is the cheapest positive-anchor proof control.

### PA-3

```text
anchors       1/8, 3/16, 1/4
new points    3
final degree  17
```

The scale-normalized midpoint minima are approximately `3.70e-11` and
`1.78e-10`. This is the recommended first joint directed packet.

### PA-7

```text
anchors       1/8, 3/16, 1/4, 3/8, 1/2, 3/4, 1
new points    7
final degree  21
matrix sizes  11 x 11, 11 x 11
```

The ordinary normalized minima are approximately `3.80e-13` and `2.67e-12`.
No negative midpoint was found.

## Required proof-grade continuation

A production branch should:

1. patch the reviewed completed-xi producer to emit the exact new anchors;
2. run at two directed precisions;
3. bind every point to the PR #103 ordinate and atomized count profile;
4. compute each one-anchor scalar by full and reduced contractions;
5. require overlap and precision nesting;
6. reconstruct the multi-anchor moments in two anchor orders;
7. freeze any negative direction to rational coordinates;
8. otherwise certify both matrices positive by exact LDL plus interval moats.

A strict negative response would be an RH-disproof nomination only after
independent completed-xi reproduction and review of the inherited response,
canonical-product, and count-deflation gates.

## Current classification

- `L-12101`: `PROPOSED`.
- `L-12102`: `PROPOSED`.
- exact synthetic checker: finite rational arithmetic.
- PR #103 anchor reconnaissance: `EMPIRICAL`.
- counterexample status: none.
