# L-105372 — Corrected Christoffel capacity normal form for the boundary reserve

Claim ID: `L-105372`  
Status: **PROVED EXACT FINITE-DIMENSIONAL NORMAL FORM; SUPERSEDES L-105371**  
Created: 2026-08-23  
Depends on: `L-105370`  
RH status: **not assumed**

`L-105371` contained a malformed display delimiter in the scalar trace lane.
This file is the normative clean statement.

## 1. Abstract domination lemma

Let `A,C` be real symmetric `k by k` matrices with `A\succeq0` and
`C\succeq0`. Then

\[
\boxed{C\preceq A}
\tag{L-105372.1}
\]

if and only if

\[
\boxed{\operatorname{Ran}C\subseteq\operatorname{Ran}A}
\tag{L-105372.2}
\]

and

\[
\boxed{
\lambda_{\max}
\left(A^{\dagger/2}CA^{\dagger/2}\right)\le1,
}
\tag{L-105372.3}
\]

where `A^dagger` is the Moore--Penrose inverse. This follows by restricting to
`Ran A` and conjugating by the positive square root of `A` there.

## 2. Exact source-normalized capacity

For `a\in\{0,1\}`, use the source and critical matrices from `L-105370`:

\[
\mathsf A_k^{(a)}(F),
\qquad
\mathsf C_{k,\Omega}^{(a)},
\qquad
\mathsf S_{k,\Omega}^{(a)}
=
\mathsf A_k^{(a)}-
\mathsf C_{k,\Omega}^{(a)}.
\]

Assume first that `A_k^(a)` is positive definite and define

\[
\boxed{
\mathsf B_{k,\Omega}^{(a)}
=
\left(\mathsf A_k^{(a)}\right)^{-1/2}
\mathsf C_{k,\Omega}^{(a)}
\left(\mathsf A_k^{(a)}\right)^{-1/2}.
}
\tag{L-105372.4}
\]

Then

\[
\boxed{
\mathsf S_{k,\Omega}^{(a)}\succeq0
\iff
\lambda_{\max}
\left(\mathsf B_{k,\Omega}^{(a)}\right)\le1.
}
\tag{L-105372.5}
\]

For a singular source matrix, replace inverse square roots by pseudoinverse
square roots and add the range condition (L-105372.2).

## 3. Atomic frame representation

Let

\[
v_k(s)=(1,s,\ldots,s^{k-1})^T
\]

and define

\[
\boxed{
u_{c;k,a}
=\sqrt{W_cs_c^a}
\left(\mathsf A_k^{(a)}\right)^{-1/2}v_k(s_c).
}
\tag{L-105372.6}
\]

Then

\[
\boxed{
\mathsf B_{k,\Omega}^{(a)}
=
\sum_cu_{c;k,a}u_{c;k,a}^T.
}
\tag{L-105372.7}
\]

The boundary gate is exactly the operator-frame capacity bound

\[
\boxed{
\left\|
\sum_cu_{c;k,a}u_{c;k,a}^T
\right\|_{\rm op}
\le1.
}
\tag{L-105372.8}
\]

## 4. Christoffel leverage and a scalar sufficient lane

Define the source Christoffel leverage

\[
\boxed{
\mathcal K_{k,a}(s)
=s^a v_k(s)^T
\left(\mathsf A_k^{(a)}\right)^{-1}v_k(s).
}
\tag{L-105372.9}
\]

The normalized critical trace is

\[
\boxed{
\operatorname{tr}
\mathsf B_{k,\Omega}^{(a)}
=
\sum_cW_c\mathcal K_{k,a}(s_c).
}
\tag{L-105372.10}
\]

Since a positive matrix has operator norm at most its trace,

\[
\boxed{
\sum_cW_c\mathcal K_{k,a}(s_c)\le1
\Longrightarrow
\mathsf S_{k,\Omega}^{(a)}\succeq0.
}
\tag{L-105372.11}
\]

This trace criterion is sufficient but generally not necessary.

## 5. Necessary leverage bounds

Under exact domination, every individual atom obeys

\[
\boxed{W_c\mathcal K_{k,a}(s_c)\le1,}
\tag{L-105372.12}
\]

and the aggregate trace obeys

\[
\boxed{
\sum_cW_c\mathcal K_{k,a}(s_c)\le k.
}
\tag{L-105372.13}
\]

The interval between the sufficient threshold one and necessary threshold
`k` measures overlap among the normalized atomic feature directions.

## 6. Terminal capacity form

For each fixed `k,a`, the source matrix is independent of the window and the
critical matrix increases outward under the sharp residue sign. If the source
matrix is positive definite, `TAIR105360` is equivalently

\[
\boxed{
\limsup_{j\to\infty}
\lambda_{\max}
\left(
\mathsf B_{k,\Omega_{N_j}}^{(a)}
\right)
\le1
}
\tag{L-105372.14}
\]

along the terminal cofinal sequence. An `o(1)` excess over one is sufficient
before the inward limit, because the finite source matrix is fixed.

Thus the terminal boundary problem is asymptotic non-overfilling of each
finite source moment space by the critical residue atoms.

## 7. Scope

No source-matrix positivity, inverse bound, Christoffel estimate or critical
capacity estimate is proved for Xi. The scalar trace lane must not be promoted
to an equivalence. Singular source matrices require the exact range condition.
RH remains unproved.
