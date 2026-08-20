# T-100610 — First-owner and largest-owner energies form an exact AND-gate to RH

Claim ID: `T-100610`  
Status: **PROVED CONDITIONAL COMPOSITION; TWO COMPLEMENTARY LONG-COLLAR ENERGIES OPEN**  
Created: 2026-08-20  
Depends on: `L-100610--L-100615`; PR #676 `L-100002`  
RH status: **unproved**

This theorem gives a literal implication-matrix hyperedge: neither input is
replaced by the other, and the conclusion follows only after both are present.

## 1. Exact centered interval matrix

Let

\[
2\le p_1\le\cdots\le p_k,
\qquad
r_i=p_i^{-1/2},
\]

be the first `k` labels of the complete cubic Euler source: one labelled copy
of every prime and one additional labelled copy of `67`. Equal labels occur
only for the two copies of `67`; they remain distinct commuting coordinates.

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

Define

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
\sum_{i<j}
|a_i|\,|\widetilde A_{ij}^{(k)}(X)|\,|b_j|.
}
\tag{T-100610.9}
\]

The carrier subtraction is binding: placing absolute values around the raw
matrix would force the arithmetic estimates to pay a known positive
`sqrt(X)` term.

## 2. The two complementary survival-weighted energies

Define the first-owner row energy

\[
\boxed{
\mathfrak R_k(X)
=
\sum_i a_i^2
\sum_{j>i}|\widetilde A_{ij}^{(k)}(X)|
}
\tag{T-100610.10}
\]

and the largest-owner column energy

\[
\boxed{
\mathfrak C_k(X)
=
\sum_j b_j^2
\sum_{i<j}|\widetilde A_{ij}^{(k)}(X)|.
}
\tag{T-100610.11}
\]

These are not source-blind row/column suprema. Their weights

\[
a_i^2=r_iL_i^2,
\qquad
b_j^2=r_jR_j^2
\]

are exactly the first-owner and reversed-owner Littlewood--Paley weights.

Apply Cauchy--Schwarz to the set of pairs `(i,j)`, with measure
`|widetilde A_(ij)|`:

\[
\begin{aligned}
\left(
 \sum_{i<j}|a_i||\widetilde A_{ij}||b_j|
\right)^2
&\le
\left(
 \sum_{i<j}|\widetilde A_{ij}|a_i^2
\right)
\left(
 \sum_{i<j}|\widetilde A_{ij}|b_j^2
\right)\\
&=
\mathfrak R_k(X)\mathfrak C_k(X).
\end{aligned}
\]

Therefore

\[
\boxed{
(F_k(X))_-
\le
\sqrt{\mathfrak R_k(X)\mathfrak C_k(X)}.
}
\tag{T-100610.12}
\]

This is the exact two-sided owner estimate. It avoids the unnecessary
multiplicity and inactive-prime divergence of unweighted Schur suprema.

`L-100612--L-100613` prove that every entry with empty interior or endpoint
ratio at most eight is already nonnegative. `L-100615` enlarges that positive
region asymptotically to `p_j<=p_i^A` for every `A<e^(3/4)`. Such entries may
be removed before forming the residual matrix. `L-100614` additionally shows
that every fully active remaining entry has zero centered residual. Thus
`mathfrak R_k` and `mathfrak C_k` need contain only supercritical,
partial-activation collars.

## 3. The AND-gate statements

Define

\[
\boxed{
\mathrm{FOCR100610}(Y):
\quad
\sup_k\int_1^Y\mathfrak R_k(X)\frac{dX}{X}
=Y^{o(1)}
}
\tag{T-100610.13}
\]

and

\[
\boxed{
\mathrm{LOCR100610}(Y):
\quad
\sup_k\int_1^Y\mathfrak C_k(X)\frac{dX}{X}
=Y^{o(1)}.
}
\tag{T-100610.14}
\]

Cauchy--Schwarz in `dX/X` gives

\[
\sup_k\int_1^Y(F_k(X))_-\frac{dX}{X}
\le
\left(
 \sup_k\int_1^Y\mathfrak R_k(X)\frac{dX}{X}
\right)^{1/2}
\left(
 \sup_k\int_1^Y\mathfrak C_k(X)\frac{dX}{X}
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

This is a genuine conjunction, not a renamed one-statement criterion.

## 4. Why both sides are logically necessary for this mechanism

For a nonnegative matrix `K_(ij)`, the first factor in pairwise
Cauchy--Schwarz controls multiplicity in the least-owner direction and the
second controls multiplicity in the greatest-owner direction. A one-column
matrix and its transpose show that either weighted side alone can remain
bounded while the bilinear collapse grows like a square root after the endpoint
vectors are rescaled to unit norm. Thus the conjunction is not cosmetic.

## 5. Relationship to the live routes

```text
FOCR100610:
  sequential first-owner / ODSB100604 row geometry with its exact hazard
  weights;

LOCR100610:
  largest-prime / HDRB100603 column geometry with its reverse-hazard weights;

remaining entries:
  supercritical partial-activation intervals after explicit positive carrier
  subtraction, with finite interior squaring and positive divisor renewal
  available before physical collapse.
```

The theorem proves the complete compositional interface from those two
arithmetic statements to RH. It does not assert either owner energy. Their
region-by-region reduction is recorded in `T-100611`.

```text
two-ended hazard identity                    PROVED EXACT
two-ended Littlewood--Paley identity          PROVED EXACT
critical endpoint convexity                   PROVED EXACT
ratio-eight/power-width interval positivity   PROVED
positive carrier subtraction                  PROVED EXACT
survival-weighted two-owner AND-gate           PROVED EXACT
FOCR100610 long-collar row energy              OPEN
LOCR100610 long-collar column energy           OPEN
Riemann Hypothesis                             UNPROVED
```