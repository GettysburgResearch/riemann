# R-91800 — A global kernel or entropy equality does not imply radial locality

Claim ID: `R-91800`  
Status: **EXACT PROVENANCE FIREWALL**  
Created: 2026-08-13  
Depends on: `T-91800`  
RH status: **unproved**

## 1. The tempting shortcut

Suppose one has a positive diffuse arithmetic source measure

\[
 d\mathsf A(r)=dr
 \qquad(0<r<1)
\]

and proves only its total mass

\[
 \mathsf A((0,1))=1.
\]

It is tempting to split this total scalar or total kernel as critical plus
stable and conclude that no atomic output remains.  This is invalid unless the
identity is local in the radial Borel algebra.

## 2. Exact scalar countermodel

Fix any

\[
 0<h<1
\]

and any depth

\[
 d\in(0,1).
\]

Define only the **global** output totals by

\[
 \mathsf C_{\rm total}=1-h,
 \qquad
 \mathsf H_{\rm total}=h.
\]

Then

\[
\boxed{
 \mathsf A((0,1))
 =\mathsf C_{\rm total}+\mathsf H_{\rm total}
}
\tag{R-91800.1}
\]

with every term nonnegative.  The hyperbolic total can be declared to come
from the atom

\[
 d\mathsf H(r)=h\,\delta_d(dr).
\]

No contradiction occurs because no interval-wise identity was specified.

The diffuse source has zero mass at `{d}`, while the output has mass `h`; the
global equality has forgotten spectral type.

## 3. Matrix version

Let `A0` be any positive definite matrix and choose

\[
 0\preceq H_0\preceq A_0.
\]

Set

\[
 C_0=A_0-H_0.
\]

Then

\[
 A_0=C_0+H_0
\]

is a perfectly valid global positive kernel equality.  One may attach `A0` to
a diffuse source measure and `H0` to a point mass at an arbitrary depth.  The
total Gram does not record this mismatch.

Thus neither full polarization nor positive global kernel order, by itself,
recovers radial provenance.

## 4. One dyadic grid is insufficient

Partition `(0,1)` into dyadic cells at one fixed resolution.  An atom at depth
`d` may be assigned to the diffuse source norm of the unique cell containing
`d`.  Compatibility on that one grid does not see the singularity.

To force spectral-type preservation one needs either:

```text
all rational intervals;
all translated dyadic grids with mesh tending to zero;
or an explicit L-infinity(dr)-module relation.
```

## 5. Relation to earlier firewalls

This is distinct from:

```text
R-91405: continuous carrier measure cannot dominate prime atoms;
R-91710: equality of total dyadic entropy does not identify generations;
PR #428: matching diagonals does not imply a positive kernel defect.
```

The present issue remains even after a positive global kernel lock: a global
isometry may rotate diffuse radial source mass into a point-depth model port.
Only interval naturality forbids that rotation.

## 6. Correct target

The valid conclusion-producing statement is `RLSL` from `T-91800`:

\[
 \mathsf A(I)
 =\mathsf C(I)+\mathsf S(I)+\mathsf H(I)+\mathsf E(I)
\]

for every radial interval `I`, with all terms positive and compatible under
refinement.

## 7. Exact boundary

```text
global positive equality kills atoms            FALSE
global full-polarization equality kills atoms   FALSE
one fixed dyadic grid kills atoms               FALSE
Borel interval locality kills atoms             EXACT
RLSL                                             OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```
