# L-91841 — First-owner-restricted child operators are disjoint and mass-normalizable

Claim ID: `L-91841`  
Status: **PROVED EXACT SOURCE-PARTITION AND POSITIVE-INTEGRATION THEOREM**  
Created: 2026-08-15  
Primary inputs: `L-91688`, `L-91650`, `L-91674`, `L-91732`  
RH status: **unproved**

## 1. Restricted operators

Fix an ordered list of active rough primes

\[
p_1<p_2<\cdots<p_k,
\]

and a labelled rough monomial `m`. Define

\[
 R_j[m]
 =\mathbf1_{p_j\mid m}
  \prod_{h<j}\mathbf1_{p_h\nmid m},
\tag{L-91841.1}
\]

and

\[
 R_\infty[m]=\prod_{h\le k}\mathbf1_{p_h\nmid m}.
\tag{L-91841.2}
\]

The source-faithful child operator is

\[
\boxed{U_j^{(1)}=U_{p_j}R_j.}
\tag{L-91841.3}
\]

The restriction is part of the operator. It may not be dropped after grouping
by prime.

## 2. Exact first-owner partition

For every rough monomial,

\[
\boxed{R_\infty+\sum_{j=1}^kR_j=I,}
\qquad
\boxed{R_iR_j=0\quad(i\ne j).}
\tag{L-91841.4}
\]

Hence a monomial divisible by several rough primes enters exactly the child of
its first listed prime. Positive source integration and every linear typed
observation preserve (L-91841.4).

## 3. Fibrewise lists and provenance classes

On an endpoint fibre `s`, use its active list and attach the complete label

```text
(first-owner index, endpoint cell, P61 divisor, Hall edge/residual,
 source history, same-index placement).
```

Group only equal complete labels. If `M_b` is the actual target mass of one
nonzero aggregate child class and `M` is parent target mass, define

\[
 \widehat P_b=M_b^{-1}P_b,
 \qquad
 \beta_b=M_b/M.
\tag{L-91841.5}
\]

The pointwise target-mass inequality and Tonelli give

\[
\boxed{
 \sum_b\beta_b<\frac18.
}
\tag{L-91841.6}
\]

This is the mass-normalized hereditary coefficient list. It is not an
unweighted count of prime labels.

## 4. One-shot specialization

In the preferred PR #487 implementation, every `U_j^(1)` child remains an
internal colour of the one final physical row. The exported child family is
empty, so its coefficient sum is exactly zero. Equations (L-91841.1)--(L-91841.4)
still provide the source-provenance audit and prevent duplicate ownership.

## 5. Boundary

```text
least-prime rough owner                        exact
multiple-prime duplication                     impossible by R_i R_j=0
grouping by prime without source restriction   forbidden
actual-mass normalization                      exact by positive integration
recursive coefficient mass                     <1/8 when exported
PR #487 exported family                        empty
Riemann Hypothesis                             unproved
```
