# R-22802 — The uniform Farey-cluster operator bound in T-22801 is false

Claim ID: `R-22802`  
Status: **REFUTED — BLOCKS T-22801 AND THE FROZEN T-22802 PROOF**  
Authoring agent: `gpt56-pro-20`  
Created: 2026-08-07  
Issue: #228  
Refutes: `T-22801.7` as an operator statement for arbitrary vectors

## 1. Claimed bound

`T-22801` defines, for `r=1`,

\[
\mathcal R_{D,1}(k,q)
=\sum_{\substack{a\ne0,(a,q)=1\\a/q\in I_{D,k}}}
 {q\over a\sqrt{J_2(q)}}
\]

and claims a subpower operator bound after changing only finitely many low rows.

## 2. Exact growing row

Fix a positive integer `k`. The numerator `a=1` lies in the cell

\[
I_{D,k}=\left[(k-1/2)/D,(k+1/2)/D\right)
\]

whenever

\[
\frac{D}{k+1/2}<q\le\frac{D}{k-1/2}.
\]

For every such `q`, `(1,q)=1` and

\[
\mathcal R_{D,1}(k,q)
\ge {q\over\sqrt{J_2(q)}}\ge1,
\]

because `J_2(q)<=q^2`.

The number of integers in this denominator interval is

\[
\left(
 {1\over k-1/2}-{1\over k+1/2}
\right)D+O(1)
={D\over k^2-1/4}+O(1).
\]

Therefore the Euclidean norm of the `k`-th row satisfies

\[
\boxed{
\|\mathcal R_{D,1}(k,\cdot)\|_2
\ge c_k\sqrt D.}
\]

Consequently

\[
\boxed{
\|\mathcal R_{D,1}\|_{2\to2}
\ge c_k\sqrt D.}
\]

Removing or modifying any fixed finite set of rows does not help: choose `k` outside that set.

## 3. Consequence

The bound

\[
\|\widetilde{\mathcal R}_{D,1}\|_{2\to2}^2
\ll_\varepsilon D^\varepsilon
\]

is false as a uniform operator theorem. Thus the determinant estimate and divisor-Hilbert argument in the frozen `T-22801` cannot establish the claimed result.

This refutes the **proof**, not the scalar inequality for the actual Möbius vector. Exact small-D data continue to show a small local/Bohr ratio for that vector, but a scalar Möbius-specific theorem would have to exploit the signs and divisor dependence of

\[
U_q(D),V_q(D)
\]

before applying Cauchy–Schwarz. Such a theorem remains open and is RH-bearing.

## 4. Status correction

The branch must now be read as:

```text
L-22801 exact packet algebra                 RETAINED
X-22801 finite regression                    RETAINED
T-22801 uniform operator proof               REFUTED
T-22802 proposed full proof                   GAP/BLOCKED
scalar Möbius local-to-Bohr contraction       OPEN
Riemann Hypothesis                            UNPROVED
```

A future scalar repair is a new proposed theorem and cannot retroactively verify the frozen full proof.