# L-100700 — Double-owner blocks are exact mixed coboundaries and every matrix rectangle telescopes

Claim ID: `L-100700`  
Status: **PROVED EXACT FINITE OPERATOR THEOREM**  
Created: 2026-08-20  
Depends on: PR #691 `L-100605`  
RH status: **not assumed**

Let `U_1,...,U_k` be commuting shifts, let `0<r_i<1`, and put

\[
 E_{a:b}:=\prod_{h=a}^{b}(I-r_hU_h),
 \qquad E_{a:b}:=I\quad(a>b).
\]

PR #691 defines the double-owner blocks

\[
 \mathcal D_{i,i}=-r_iU_i,
\]

and, for `i<j`,

\[
 \mathcal D_{i,j}
 =r_ir_jU_iU_jE_{i+1:j-1}.
\tag{L-100700.1}
\]

## 1. Mixed-coboundary identity

For every `i<j`,

\[
\boxed{
\mathcal D_{i,j}
=E_{i:j}-E_{i+1:j}-E_{i:j-1}+E_{i+1:j-1}.
}
\tag{L-100700.2}
\]

Indeed, factoring the common interior product gives

\[
\begin{aligned}
& E_{i+1:j-1}
\bigl[(I-r_iU_i)(I-r_jU_j)
 -(I-r_jU_j)-(I-r_iU_i)+I\bigr]\\
&\qquad =r_ir_jU_iU_jE_{i+1:j-1}.
\end{aligned}
\]

Thus the double-owner matrix is the two-dimensional discrete mixed derivative
of the interval Euler products.

## 2. Exact rectangle telescope

Let

\[
1\le a\le b<c\le d\le k.
\]

Summing (L-100700.2) first in `i` and then in `j` gives

\[
\boxed{
\sum_{i=a}^{b}\sum_{j=c}^{d}\mathcal D_{i,j}
=E_{a:d}-E_{b+1:d}-E_{a:c-1}+E_{b+1:c-1}.
}
\tag{L-100700.3}
\]

Every interior edge cancels. Only the four interval-Euler corner states remain.
This is a literal discrete Stokes theorem on the implication matrix.

## 3. Row and column boundary formulas

Including the diagonal block,

\[
\boxed{
\mathcal D_{i,i}+
\sum_{j=i+1}^{b}\mathcal D_{i,j}
=-r_iU_iE_{i+1:b}.
}
\tag{L-100700.4}
\]

Dually,

\[
\boxed{
\mathcal D_{j,j}+
\sum_{i=a}^{j-1}\mathcal D_{i,j}
=-r_jU_jE_{a:j-1}.
}
\tag{L-100700.5}
\]

Hence first-owner and largest-prime formulas are exactly the two boundary
traces of the same mixed-coboundary array.

## 4. Consequence for regional proofs

Any union of disjoint rectangular matrix regions may be evaluated by its
oriented boundary interval states. In particular:

- no bulk endpoint-collar term is independent;
- interfaces between adjacent regions cancel if the same interval state is used;
- regionwise absolute values destroy an exact coboundary cancellation and are
  not a source-faithful proof operation.

The remaining arithmetic is therefore a **boundary trace theorem**, not a
separate estimate for every interior block.

The exact verifier in `X-100700` checks (L-100700.2)--(L-100700.5) for every
rectangle on a five-label rational fixture.