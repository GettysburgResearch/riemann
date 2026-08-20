# T-100600 — Implication-matrix hybrid frontier after type audit

Status: **EXACT OWNER/COMPLETION DECOMPOSITIONS RETAINED; TWO RENEWAL ARROWS WITHDRAWN; RH UNPROVEN**

This theorem records the corrected cross-branch implications after hostile reconstruction of the operator types.

## A. Largest-prime / cofactor-squaring chain — retained

Using PR #688 `L-100410` and corrected `L-100600--L-100602`,

\[
\boxed{
\text{minimal wavelet}
\to
\text{unique largest-prime owner}
\to
\text{finite cofactor squaring before collapse}
\to
\text{fully squared cofactor core at }Z=\sqrt X.
}
\]

The cofactor shifts must be unrestricted multiplicative shifts; the native degree-one Euler polynomial, not an artificial squarefree truncation of the shift, enforces squarefree support before completion.

This chain is a forward completion.  It does not positively recover the original unsquared cofactor packet.

## B. Divisor-renewal compositions — withdrawn

The former `L-100603` and `L-100604` treated a dilation monomial `S_df` or `U_df` as though it were the divisor restriction

\[
\sum_m\beta(dm)m^{-z}.
\]

These are distinct operations.  PR #671's positive divisor renewal therefore does not desquare a finite completion and does not factor a first-owner future monomial merely from its integer label.

Accordingly:

```text
HDRB100603     withdrawn as an established reduction;
ODSB100604     withdrawn as an established reduction;
FCHD67         still retains its complete future Euler profile.
```

## C. Double-owner localization — retained exactly

`L-100605` remains coefficient-exact:

\[
\mathcal D_{i,i}=-r_iU_i,
\qquad
\mathcal D_{i,j}=r_ir_jU_iU_j
\prod_{i<h<j}(I-r_hU_h),\quad i<j.
\]

Every nonempty Euler monomial occurs once, classified by its least and greatest selected prime.  The exact coboundary and balanced-squaring successor is PR #695.

## D. Corrected detector interfaces

The already-proved scalar and compact-wavelet detectors remain available once an independent source-faithful signed or negative-mass estimate is supplied.  No detector conclusion follows from the withdrawn dilation/restriction identifications.

## Exact boundary

```text
semantic implication matrix                   RETAINED
largest-prime ownership                       PROVED EXACT
cofactor finite-squaring identity              PROVED EXACT, TYPE REPAIRED
sqrt(X) cutoff geometry                       PROVED EXACT
largest-prime + divisor-renewal desquaring     WITHDRAWN
first-owner + divisor-renewal factorization    WITHDRAWN
double-owner bi-triangular decomposition       PROVED EXACT
balanced coboundary/homotopy successor         PR #695
Riemann Hypothesis                             UNPROVEN
```
