# L-99322 — The target-aligned lift closes the actual fixed-row identity modulo the bounded calibration ledger

Claim ID: `L-99322`  
Status: **PROPOSED COMPLETE COMPOSITION THEOREM — ACTUAL LEDGER REVIEW REQUIRED**  
Created: 2026-08-19  
Depends on: `L-99320/L-99321`; PR #641 `L-99240/L-99241`; PR #638 boundary
audit; PR #632 random-key theorem  
RH status: **not assumed**

Fix one row \(j\ge2\).

## 1. Positive source part

Apply `L-99321` on every retained compact endpoint fibre in the exact root
source registry. Integrate the target-aligned row source over the positive
retained endpoint measure, and resolve only residual \(\alpha\)-children.

Let \(D_X(j)\) be the sum of all current and terminal observations. Then

\[
\boxed{D_X(j)\ge0.}
\tag{L-99322.1}
\]

The construction is literal:

```text
one target Hall flow at each target parameter;
one positive row atom eta_j(t);
one random-key child partition;
one owner for every micro-source;
only alpha-children recurse.
```

The normalized-row Hall bonus of PR #636 is not used. It is replaced by the
target factorization in `L-99321`.

## 2. Exact signed calibration

Define \(C_Y(j)\) at a typed node as the exact difference between the finite
native row contribution and the retained positive source contribution. It
contains, with actual signs:

1. retained-cell finite/continuum discrepancy;
2. activation-knot atoms;
3. the two homogeneous Volterra boundary modes;
4. finitely many anchored low-endpoint cells;
5. source-owned omissions not assigned to the positive target tree.

This definition gives the exact local identity

\[
\boxed{
E_Y(j)=J_Y(j)+(E_YT_Y)(j)+C_Y(j).
}
\tag{L-99322.2}
\]

The target-aligned lift proves that \(J_Y(j)\) and \(E_YT_Y(j)\) arise from
one source. PR #638 proves that the distributional boundary ledger has only
finitely many knot atoms and two homogeneous modes. PR #641 gives

\[
|C_Y(j)|\le B_j
\tag{L-99322.3}
\]

uniformly in the endpoint and provenance label.

## 3. Resolution

The child operator is nilpotent at a fixed root. Therefore

\[
\boxed{
c_X(j)=D_X(j)+\mathfrak E_X(j),
}
\tag{L-99322.4}
\]

where

\[
D_X(j)=J_X(I-T_X)^{-1}s_X\ge0
\]

and

\[
\mathfrak E_X(j)=C_X(I-T_X)^{-1}s_X.
\]

Only \(\alpha\)-children recurse and their total coefficient is below \(1/8\).
The compact root mass is finite, so

\[
\boxed{
|\mathfrak E_X(j)|\le K_j<\infty
}
\tag{L-99322.5}
\]

uniformly in \(X\).

## 4. Repaired interface

The actual identity required by PR #641 is now explicit:

```text
finite native row
=
target-aligned positive current
+ target-aligned positive children
+ signed source-owned calibration.
```

No calibration term is asserted positive. No Volterra anchor is promoted into
the positive source. The row identity is formed before Mellin transformation.

## 5. Reconstruction boundary

The sole imported arithmetic assertion is the target-only compact Hall/root
source ledger at its frozen scope. A failure there rejects the candidate.
There is no longer an independent component-row, normalized-profile,
endpoint-nesting, or row-coupling obligation.
