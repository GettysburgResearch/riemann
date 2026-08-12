# L-91334 — An interleaved positive reset cocycle does not require completed-state tensorization

Claim ID: `L-91334`  
Status: **PROVED ABSTRACT RESET-INDUCTION THEOREM; RIEMANN ONE-STEP TYPED RESET OPEN**  
Created: 2026-08-12  
Depends on: `R-91329`, `T-91101`  
RH status: **unproved**

## 1. Raw and controlled states

Let `C` be a positive state cone and let

\[
 w:C\to\mathbb R
\]

be the conclusion-relevant scalar observation. For each rough label `p`, let

\[
 M_p
\]

be the raw signed state operation and

\[
 N_p:C\to C
\]

a positive controlled operation satisfying

\[
 \boxed{wN_p=wM_p.}
\tag{L-91334.1}
\]

No product identity is assumed.

## 2. One-step typed reset hypothesis

Suppose that for every typed positive state `u in C`, one has a positive one-step decomposition

\[
 \boxed{
 \mathfrak S(u)
 =\mathfrak O_p(u)
  +\mathfrak A_p\mathfrak S(N_pu)
  +\mathfrak Z_p(u),
 }
\tag{L-91334.2}
\]

where:

- `mathfrak S(u)` is the source/target measure represented by the current state;
- `mathfrak O_p(u)` is the positive current-generation output;
- `mathfrak A_p` is the positive affine scale lift to the parent coordinates;
- `mathfrak Z_p(u)` is positive unused slack;
- all three terms have disjoint source provenance or are otherwise charged exactly once.

Assume also a one-step score inequality

\[
 \boxed{
 \mathfrak L(u)
 \le\mathfrak L(N_pu)+E_p(u),
 }
\tag{L-91334.3}
\]

with the declared endpoint contraction and debt bounds.

Equation (L-91334.1) is the scalar compatibility check for one operation. Equation (L-91334.2), not a raw matrix product equality, is the load-bearing typed statement.

## 3. Tree induction

Define the controlled child state recursively by

\[
 u_{j+1}=N_{p_j}u_j.
\]

Apply (L-91334.2) to `u_0`. Then apply it to the child measure `mathfrak S(u_1)`, and continue. Positivity and linearity give, at every finite depth `k`,

\[
\boxed{
\begin{aligned}
 \mathfrak S(u_0)
 ={}&\sum_{j=0}^{k-1}
  \mathfrak A_{p_0}\cdots\mathfrak A_{p_{j-1}}
  \mathfrak O_{p_j}(u_j)\\
 &+\mathfrak A_{p_0}\cdots\mathfrak A_{p_{k-1}}
  \mathfrak S(u_k)\\
 &+\text{a positive sum of transported slack measures}.
\end{aligned}}
\tag{L-91334.4}
\]

Every source atom is charged once because that property is part of the one-step typed decomposition and is inherited by induction.

Similarly,

\[
 \boxed{
 \mathfrak L(u_0)
 \le\mathfrak L(u_k)+
  \sum_{j=0}^{k-1}E_{p_j}(u_j).
 }
\tag{L-91334.5}
\]

This is the coefficient-one reset recursion.

## 4. Why the review counterexample does not contradict the induction

The counterexample in `R-91329` proves

\[
 wN_qN_p\ne wM_qM_p.
\]

The induction above never asserts that equality. At the second step it uses

\[
 wN_q u_1=wM_q u_1,
 \qquad u_1=N_pu_0,
\]

not an identity comparing the controlled trajectory with the uncorrected raw trajectory from `u_0`.

Thus the exact non-tensorization result invalidates the submitted source-partition proof, but it does not logically force every valid reset proof to use the raw multiprime product.

## 5. Riemann scope

For PR #399, the positive matrices `N_p` and the one-step identity are available. What is not yet available is a complete proof of (L-91334.2) in the actual endpoint/block/Schur coordinates, including:

```text
positive source typing of the controlled state;
one-use physical target capacity;
branch-local realization of the SHARP-null correction;
ordinary and radix-four endpoint rows;
and the exact score orientation.
```

The four-state route of `L-91327` is one possible construction of this missing typed reset. The one-prime Hall corridor of `L-91335` provides another concrete local input. Neither is completed here.

## 6. Proof boundary

```text
raw completed-product tensorization                NOT REQUIRED ABSTRACTLY
one-step controlled-cocycle induction              EXACT
positive all-depth measure partition from typed steps EXACT
coefficient-one score induction from typed steps   EXACT
Riemann one-step typed reset identity               OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVEN
```
