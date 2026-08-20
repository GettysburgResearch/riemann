# T-100610 — First-owner and largest-owner Schur estimates form an exact AND-gate to RH

Claim ID: `T-100610`  
Status: **PROVED CONDITIONAL COMPOSITION; TWO COMPLEMENTARY LONG-COLLAR ESTIMATES OPEN**  
Created: 2026-08-20  
Depends on: `L-100610--L-100614`; PR #676 `L-100002`  
RH status: **unproved**

This theorem gives a literal implication-matrix hyperedge: neither input is
replaced by the other, and the conclusion follows only after both are present.

## 1. Exact interval matrix

Let

\[
2\le p_1\le\cdots\le p_k,
\qquad
r_i=p_i^{-1/2},
\]

be the first `k` labels of the complete cubic Euler source: one labelled copy
of every prime and one additional labelled copy of `67`. Equal labels occur
only for the two copies of `67`; they remain distinct commuting coordinates.
The finitely many labels below `67` may equivalently be frozen into the base
colour of the rough-prime routes, but they are included here so that the limit
is literally the full duplicate-67 cubic scalar.

Let `Psi` be the cubic critical kernel and put

\[
F_k(X)=\prod_{i=1}^{k}(I-r_iU_i)\Psi(X).
\tag{T-100610.1}
\]

Use the survival factors

\[
L_i=\prod_{h<i}(1-r_h),
\qquad
R_i=\prod_{h>i}(1-r_h),
\]

and endpoint vectors

\[
a_i=\sqrt{r_i}L_i,
\qquad
b_j=\sqrt{r_j}R_j.
\tag{T-100610.2}
\]

By `L-100611`,

\[
\|a\|_{\ell^2}\le1,
\qquad
\|b\|_{\ell^2}\le1.
\tag{T-100610.3}
\]

For `i<j`, write

\[
H_{ij}^{(k)}(X)
=
\Delta_i\Delta_jE_{i+1:j-1}\Psi(X).
\tag{T-100610.4}
\]

`L-100614` supplies the exact nonnegative carrier

\[
M_{ij}^{(k)}(X)
=
192\sqrt X
(1-p_i^{-1/2})(1-p_j^{-1/2})
\prod_{i<h<j}(1-p_h^{-1})
\ge0
\tag{T-100610.5}
\]

and the collar-only residual

\[
\widetilde H_{ij}^{(k)}=H_{ij}^{(k)}-M_{ij}^{(k)}.
\tag{T-100610.6}
\]

Define the centered physical interval matrix

\[
\boxed{
\widetilde A_{ij}^{(k)}(X)
=
\sqrt{r_ir_j}\,\widetilde H_{ij}^{(k)}(X),
\qquad i<j,
}
\tag{T-100610.7}
\]

and put `widetilde A_(ij)=0` for `i>=j`.

The two-ended hazard identity, cubic endpoint positivity, and
`M_(ij)>=0` give

\[
F_k(X)
=
\text{nonnegative root/singleton/carrier terms}
+
\sum_{i<j}a_i\widetilde A_{ij}^{(k)}(X)b_j.
\tag{T-100610.8}
\]

Hence

\[
\boxed{
(F_k(X))_-
\le
\left|a^*\widetilde A^{(k)}(X)b\right|.
}
\tag{T-100610.9}
\]

This carrier subtraction is binding: placing absolute values around the raw
matrix would force the arithmetic estimates to pay a known positive
`sqrt(X)` term.

## 2. The two complementary Schur quantities

Define

\[
\widetilde{\mathcal R}_k(X)
=
\sup_i\sum_{j>i}|\widetilde A_{ij}^{(k)}(X)|,
\tag{T-100610.10}
\]

and

\[
\widetilde{\mathcal C}_k(X)
=
\sup_j\sum_{i<j}|\widetilde A_{ij}^{(k)}(X)|.
\tag{T-100610.11}
\]

The row quantity is the greatest-owner refinement of one fixed sequential
first-owner current. The column quantity is the least-owner refinement of one
fixed largest-prime current.

The two-sided Schur test and (T-100610.3) imply

\[
\boxed{
(F_k(X))_-
\le
\|\widetilde A^{(k)}(X)\|_{2\to2}
\le
\sqrt{
 \widetilde{\mathcal R}_k(X)
 \widetilde{\mathcal C}_k(X)
}.
}
\tag{T-100610.12}
\]

`L-100612--L-100613` prove that every entry with an empty interior or endpoint
ratio at most eight is already nonnegative. Such entries may be removed before
forming the residual matrix. `L-100614` additionally shows that every fully
active long entry has zero centered residual. Thus the Schur matrix contains
only long partial-activation collars.

## 3. The AND-gate statements

Define the uniform first-owner row condition

\[
\boxed{
\mathrm{FOCR100610}(Y):
\quad
\sup_k\int_1^Y
\widetilde{\mathcal R}_k(X)\frac{dX}{X}
=Y^{o(1)}
}
\tag{T-100610.13}
\]

and the uniform largest-owner column condition

\[
\boxed{
\mathrm{LOCR100610}(Y):
\quad
\sup_k\int_1^Y
\widetilde{\mathcal C}_k(X)\frac{dX}{X}
=Y^{o(1)}.
}
\tag{T-100610.14}
\]

Cauchy--Schwarz in `dX/X` gives

\[
\sup_k\int_1^Y(F_k(X))_-\frac{dX}{X}
\le
\left(
 \sup_k\int_1^Y\widetilde{\mathcal R}_k(X)\frac{dX}{X}
\right)^{1/2}
\left(
 \sup_k\int_1^Y\widetilde{\mathcal C}_k(X)\frac{dX}{X}
\right)^{1/2}.
\tag{T-100610.15}
\]

The duplicate-67 cubic source converges absolutely at every fixed endpoint:
for `n>X`, the kernel has size `O(X/n)`, so the tail is dominated by
`X sum n^(-3/2)`. Passing through finite labelled-prime truncations by Fatou
therefore proves

\[
\boxed{
\mathrm{FOCR100610}
\quad\textbf{and}\quad
\mathrm{LOCR100610}
\Longrightarrow
\int_1^Y(\mathcal C_3(X))_-\frac{dX}{X}=Y^{o(1)}.
}
\tag{T-100610.16}
\]

The centered-cubic Mellin--Landau theorem of PR #676 now yields

\[
\boxed{
\mathrm{FOCR100610}
\ \wedge\ 
\mathrm{LOCR100610}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-100610.17}
\]

This is a genuine conjunction, not a renamed one-statement criterion.

## 4. Why both sides are logically necessary for this mechanism

A matrix with one nonzero column and `N` unit entries has row Schur bound one
but operator norm `sqrt(N)`. Its transpose has column Schur bound one and the
same unbounded norm. Therefore neither a row estimate nor a column estimate
alone controls physical collapse. Their conjunction is exactly what removes
the power-sized multiplicity exhibited by the source-blind collapse
counterexamples.

## 5. Relationship to the live routes

```text
FOCR100610:
  sequential first-owner / ODSB100604 row geometry;

LOCR100610:
  largest-prime / HDRB100603 column geometry;

remaining entries:
  long partial-activation intervals after explicit positive carrier
  subtraction, with finite interior squaring and positive divisor renewal
  available before physical collapse.
```

The theorem proves the complete compositional interface from those two
arithmetic statements to RH. It does not assert either Schur estimate. Their
region-by-region reduction is recorded in `T-100611`.

```text
two-ended hazard identity                 PROVED EXACT
two-ended Littlewood--Paley identity       PROVED EXACT
critical endpoint convexity                PROVED EXACT
ratio-eight interval positivity            PROVED EXACT
positive carrier subtraction               PROVED EXACT
two-sided collar Schur AND-gate             PROVED EXACT
FOCR100610 long-collar row estimate         OPEN
LOCR100610 long-collar column estimate      OPEN
Riemann Hypothesis                          UNPROVED
```