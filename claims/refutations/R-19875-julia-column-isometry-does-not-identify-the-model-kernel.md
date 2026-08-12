# R-19875 — A Julia column isometry does not identify the de Branges–Rovnyak model kernel

Claim ID: `R-19875`  
Status: **EXACT OPERATOR-ORDER FIREWALL**  
Created: 2026-08-12  
Corrects the finite-stage kernel inference used in `T-19816`  
RH status: **unproved**

## 1. The two distinct defects

A local scalar Julia analysis column has the form

\[
 \mathcal J=
 \begin{pmatrix}M_m\\M_d\end{pmatrix}
\]

and the boundary identity

\[
 |m|^2+|d|^2=1
\]

gives

\[
 \boxed{
 M_m^*M_m+M_d^*M_d=I.
 }
\tag{R-19875.1}
\]

This is an **input-space column isometry**.

The de Branges–Rovnyak/model kernel of `m`, however, is the output defect

\[
 \boxed{
 I-M_mM_m^*.
 }
\tag{R-19875.2}
\]

The two defects occur in opposite operator order.  In general

\[
 I-M_m^*M_m\ne I-M_mM_m^*.
\tag{R-19875.3}
\]

Therefore (R-19875.1) does not imply

\[
 K_m(z,w)=d(z)\overline{d(w)}
\]

and does not by itself produce an observability Gram for `K_m`.

## 2. Exact one-line counterexample

Take the Hardy shift multiplier

\[
 m(z)=z,
 \qquad d(z)=0.
\]

Then

\[
 M_z^*M_z=I,
\]

so the column/input defect vanishes.  But

\[
 I-M_zM_z^*=|1\rangle\langle1|
e0,
\]

and the model space `K_z` is the nonzero one-dimensional constant space.

Thus even the simplest inner multiplier disproves the implication

```text
lossless multiplier column
    -> emitted scalar detail is the complete model kernel.
```

## 3. Consequence for the common-source construction

The local Euler Julia identities retained in the factorization programme are
valuable exact input Pythagorean identities.  They do not justify the step

\[
 K_{M_N}(z,w)
 =\sum_nD_n(z)\overline{D_n(w)}
\tag{R-19875.4}
\]

unless a complete row-coisometric colligation or an explicit observability
operator is constructed.

A valid finite-stage theorem must instead provide one of:

1. a unitary colligation whose transfer is `M_N` and whose state observability
   Gram is exactly `K_(M_N)`;
2. a direct source-ordered computation of every cross term in
   `I-M_(M_N)M_(M_N)^*`;
3. an explicit minimal Kolmogorov factorization of the asserted kernel.

Appending positive column defects, gamma rows, theta rows, Brownian rows and
delay rows orthogonally does not establish (R-19875.4) and may double count a
completed contribution.

## 4. Boundary with the valid product-model theorem

The abstract identity

\[
 K_{FG}=K_F\oplus F K_G
\]

for already-inner `F,G` remains valid, as do the bounded backward-shift and
rank-one resolvent formulas.  The present correction concerns only the earlier
arithmetic step that is supposed to manufacture `K_(FG)` from source columns.

```text
local Julia input Pythagoras                    RETAINED EXACT
abstract product-model decomposition            RETAINED EXACT
column defect = model/output defect              FALSE
finite arithmetic source Gram = K_(I_a)          NOT ESTABLISHED
row-coisometric/observability realization        OPEN
Riemann Hypothesis                               UNPROVEN
```
