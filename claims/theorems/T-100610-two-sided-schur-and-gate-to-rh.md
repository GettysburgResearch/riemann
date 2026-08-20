# T-100610 — First-owner and largest-owner Schur estimates form an exact AND-gate to RH

Claim ID: `T-100610`  
Status: **PROVED CONDITIONAL COMPOSITION; TWO COMPLEMENTARY ARITHMETIC ESTIMATES OPEN**  
Created: 2026-08-20  
Depends on: `L-100610--L-100612`; PR #676 `L-100002`  
RH status: **unproved**

This theorem gives a literal implication-matrix hyperedge: neither input is
replaced by the other, and the conclusion follows only after both are present.

## 1. Exact interval matrix

Let

\[
67\le p_1<\cdots<p_k,
\qquad
r_i=p_i^{-1/2},
\]

with the two labelled copies of `67` kept separate. Let `Psi` be the cubic
critical kernel of `L-100612`, and put

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

and define endpoint vectors

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

For `i<j`, define the physical interval entry

\[
\boxed{
A_{ij}^{(k)}(X)
=
\sqrt{r_ir_j}\,
\Delta_i\Delta_jE_{i+1:j-1}\Psi(X),
}
\tag{T-100610.4}
\]

and put `A_(ij)=0` for `i>=j`.

The two-ended hazard identity gives

\[
F_k(X)
=
\text{nonnegative root/singleton terms}
+
\sum_{i<j}a_iA_{ij}^{(k)}(X)b_j,
\tag{T-100610.5}
\]

because `L-100612` signs the root and singleton channels. Hence

\[
\boxed{
(F_k(X))_-
\le
\left|a^*A^{(k)}(X)b\right|.
}
\tag{T-100610.6}
\]

## 2. The two complementary Schur quantities

Define

\[
\mathcal R_k(X)
=
\sup_i\sum_{j>i}|A_{ij}^{(k)}(X)|,
\tag{T-100610.7}
\]

and

\[
\mathcal C_k(X)
=
\sup_j\sum_{i<j}|A_{ij}^{(k)}(X)|.
\tag{T-100610.8}
\]

The row quantity is the greatest-owner refinement of one fixed sequential
first-owner current. The column quantity is the least-owner refinement of one
fixed largest-prime current. Thus they are supplied by different producer
lanes in the repository.

The classical two-sided Schur test and (T-100610.3) imply

\[
\boxed{
(F_k(X))_-
\le
\|A^{(k)}(X)\|_{2\to2}
\le
\sqrt{\mathcal R_k(X)\mathcal C_k(X)}.
}
\tag{T-100610.9}
\]

## 3. The AND-gate statements

Define the uniform first-owner row condition

\[
\boxed{
\mathrm{FOCR100610}(Y):
\quad
\sup_k\int_1^Y\mathcal R_k(X)\frac{dX}{X}
=Y^{o(1)}
}
\tag{T-100610.10}
\]

and the uniform largest-owner column condition

\[
\boxed{
\mathrm{LOCR100610}(Y):
\quad
\sup_k\int_1^Y\mathcal C_k(X)\frac{dX}{X}
=Y^{o(1)}.
}
\tag{T-100610.11}
\]

Cauchy--Schwarz in `dX/X` gives

\[
\sup_k\int_1^Y(F_k(X))_-\frac{dX}{X}
\le
\left(
 \sup_k\int_1^Y\mathcal R_k(X)\frac{dX}{X}
\right)^{1/2}
\left(
 \sup_k\int_1^Y\mathcal C_k(X)\frac{dX}{X}
\right)^{1/2}.
\tag{T-100610.12}
\]

The duplicate-67 cubic source converges absolutely at every fixed endpoint.
Passing through finite prime truncations by Fatou therefore proves

\[
\boxed{
\mathrm{FOCR100610}
\quad\textbf{and}\quad
\mathrm{LOCR100610}
\Longrightarrow
\int_1^Y(\mathcal C_3(X))_-\frac{dX}{X}=Y^{o(1)}.
}
\tag{T-100610.13}
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
\tag{T-100610.14}

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

entrywise interval reductions:
  double-owner localization + finite interior squaring + positive divisor
  renewal + compact short-interval treatment.
```

The theorem proves the complete compositional interface from those two
arithmetic statements to RH. It does not assert either Schur estimate. Their
region-by-region reduction is recorded in `T-100611`.

```text
two-ended hazard identity                PROVED EXACT
two-ended Littlewood--Paley identity      PROVED EXACT
critical endpoint convexity               PROVED EXACT
two-sided Schur AND-gate                   PROVED EXACT
FOCR100610 row estimate                    OPEN
LOCR100610 column estimate                 OPEN
Riemann Hypothesis                         UNPROVED
```