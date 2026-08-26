# Outer-ray radial duality and critical-current reduction

## Outcome

The centered filtered-disk SDP has been solved explicitly.  Its constants are
sharp and encode one fixed extrapolation point:

```text
inner disk: |w|<=1/2;
outer conclusion ray: w=-8.
```

For `P(w)=C+2Bw+Aw^2`,

```text
Lorentz current = 4A-B = [P(-8)-P(0)]/16.
```

The three positive rays at `-1/2,0,1/2` are exactly the interpolation nodes:

```text
P(-8)=136 P(-1/2)+120 P(1/2)-255 P(0).
```

The radial gauge has an exact one-dimensional primal and compact SDP dual.  A
rank-one extreme of the dual is evaluation at `w=-8`; the generic polynomial
`1-4|w|^2` proves sharpness and prevents a source-free extrapolation theorem.

## Differential factorization

The outer-ray multiplier is

```text
(1/2)(s-1)(5s+3/2)m_Phi(s).
```

Thus the outer current is `(5/2)(D+3/10)` applied to the first-order critical
scale current `(D-1)H_Phi`.  The inverse of `D+3/10` is positive and causal,
so outer-ray negative mass controls critical variation with constant `4/3`.

The converse is false without arithmetic source structure.

## Exact frontier

The remaining theorem is no longer a matrix-cone, filter, or coordinate
problem.  It is the source-specific orientation of one fixed outer-ray
increment, equivalently the reverse-resolvent estimate for the native
completion-defect source.

```text
OER102780  open / RH-bearing
RH         unproved
```