# T-107300 — Shared-fibre relative primitive trace frontier

Claim ID: `T-107300`  
Status: **EXACT FINITE RELATIVE OBJECT AND LIVE NATIVE DIAGNOSTIC; UNIFORM TRACE AND PRINCIPAL BINDING OPEN**  
Created: 2026-08-30  
Depends on: PRs #760 and #765; `L-107300--L-107302`,
`R-107300`  
RH/GRH status: **unproved**

## 1. What is now closed

For every source-authorized rectangular shared-fibre panel whose literal
coefficient has native rank-one form, the complete Wick scalar factors as

\[
\boxed{
\mathscr W_\iota(a,b)
=
E_L(a)E_R(b)
-
d_{\ell,\rho}\|a\|^2\|b\|^2,
}
\tag{T-107300.1}
\]

where \(E_L,E_R\) are the exact one-sided centered residue quadratic forms.

The source spaces have a canonical Frobenius-stable augmentation filtration,
and the bilateral source has four exact grades

\[
M\otimes M,\quad P\otimes M,\quad M\otimes P,\quad P\otimes P.
\tag{T-107300.2}
\]

Physical residue pushforward sees only \(M\otimes M\).  The other three
grades are the literal relative primitive object that carries the missing
diagonal information.  Source-aware Adams extraction acts on every grade
before pushforward.

This gives a finite, honest realization of the source algebra and its
physical shadow.  It is not merely a relabelling of the target quadratic
form: the object is the augmentation filtration of the independently
defined shared-fibre source map.

## 2. Live source evidence

On the source-locked one-hundred-history panel,

\[
\mathscr W_\iota=-660d_{\ell,\rho}.
\tag{T-107300.3}
\]

Only \(1/65\) of each one-sided coefficient energy lies in its mean channel.
Thus the actual native vector has a large primitive component.

The equal-history calibration has the opposite sign.  A global theorem must
therefore exploit signed source history and conductor recombination, not
support or rank alone.

## 3. Exact remaining gates

### `RECTGLUE107300`

Partition the complete cofinal live source in every shared fibre into
source-authorized native rectangles and an explicit omission vector \(e\).
Prove that the total signed defect from `L-107300.13` is within the available
subpower or fixed percentage budget.

### `PRIMTRACE107300`

Construct the uniform relative one-place object for the three primitive
grades and prove the signed source-aware Adams trace estimate, with conductor
or Betti complexity controlled before summing fibres.

### `PRINBIND107300`

Identify the resulting external-plus-diagonal trace with the frozen principal
physical detector, retaining endpoints, carrier, marked labels and the
literal diagonal.

The intended chain is

\[
\boxed{
\mathrm{RECTGLUE}_{107300}
\wedge
\mathrm{PRIMTRACE}_{107300}
\wedge
\mathrm{PRINBIND}_{107300}
\Longrightarrow
\text{the frozen principal cut}.
}
\tag{T-107300.4}
\]

The relevant frozen consumer may then give RH, but none of the three gates is
proved here.

## 4. Why this is progress over the previous frontier

The previous arbitrary-occupancy theorem left a choice between:

- a faithful source-algebra carrier of rank at least the live multiplicity;
- or an unspecified nonlinear sufficient statistic.

The native rank-one theorem identifies an exact small sufficient statistic:
two one-sided centered responses and two one-sided norms.  The augmentation
filtration supplies its Frobenius/Adams object and makes the omitted
information geometrically explicit.

The remaining difficulty is now signed rectangle gluing and uniform trace,
not reconstruction of an arbitrary coefficient vector.

## Exact status

```text
shared-conductor ontology                         RETAINED
live duplicate-cell occupancy                     RETAINED
native rectangular rank-one factorization         PROVED EXACT
mean/primitive Frobenius splitting                 PROVED EXACT
source-aware Adams compatibility                   PROVED EXACT
live 100-history primitive energy                 PROVED EXACT
residue-only rank-one sufficiency                  REFUTED
RECTGLUE107300                                     OPEN
PRIMTRACE107300                                    OPEN
PRINBIND107300                                     OPEN
RH / GRH                                           UNPROVED
```
