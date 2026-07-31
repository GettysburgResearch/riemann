# R-15107 — Sobolev regularization is determinant-bearing data, not a neutral realization

Claim ID: `R-15107`  
Status: **PROVED SCOPE/INVARIANCE OBSTRUCTION**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15128`; the Sobolev-reference construction displayed in Shimizu v6 and retained abstractly in v8  
Scope: second independent audit of the July 2026 operator/determinant proposal  
Related counterexample candidates: none

## 1. The reference construction

The accessible full text of version 6 chooses a unitary Laguerre--Neumann chart

\[
 \mathcal W_R:H_{\alpha,+}\to L^2([0,1]^2),
\]

transports the Neumann regularizer to

\[
 A_R^{\rm ref}
 =\mathcal W_R^{-1}(I-\Delta_{N})\mathcal W_R,
\]

and then chooses an exponent

\[
 a_{\rm tr}>1/2
\]

to smooth the raw seam trace.  Version 8 still describes the construction as a
Sobolev-reference Schatten-four sandwich realization of a self-adjoint
Hilbert--Schmidt operator.

Such a choice can certainly manufacture Schatten decay.  It does not by itself
produce a canonical determinant: the smoothing exponent and the chart enter the
trace moments.

## 2. Exact finite model

Let

\[
 A=\operatorname{diag}(1,4),
 \qquad
 B=\operatorname{diag}(1,3),
\]

and, for `a>0`, put

\[
 S_a=(I+A)^{-a},
 \qquad
 K_a=S_a B S_a.
 \tag{R-15107.1}
\]

This is the finite-dimensional model of a symmetric form realized through a
Sobolev sandwich.

At `a=1`,

\[
 K_1=\operatorname{diag}(1/4,3/25),
\]

whereas at `a=2`,

\[
 K_2=\operatorname{diag}(1/16,3/625).
\]

Therefore

\[
 \boxed{
 \operatorname{Tr}(K_1^2)=\frac{769}{10000},
 \qquad
 \operatorname{Tr}(K_2^2)=\frac{392929}{100000000}.}
 \tag{R-15107.2}
\]

The regularized determinants have different zeros:

\[
 \det{}_2(I+iwK_1)=0
 \iff
 w\in\{4i,25i/3\},
\]

while

\[
 \det{}_2(I+iwK_2)=0
 \iff
 w\in\{16i,625i/3\}.
\]

Thus changing an admissible smoothing exponent changes the determinant in the
first nonlinear coefficient already.

## 3. Chart dependence

Now interchange the two reference eigenvectors while keeping the raw form `B`
fixed.  At `a=1` the resulting sandwich is

\[
 \widetilde K_1=\operatorname{diag}(1/25,3/4),
\]

whose zero set is

\[
 \{25i,4i/3\}.
\]

Hence a unitary identification followed by a non-scalar reference regularizer is
not a harmless change of coordinates unless the raw form and every comparison
map are transported covariantly so that the final operators are unitarily
conjugate.  Merely fixing a conventional enumeration does not prove such
invariance.

## 4. Consequence for a target determinant

Suppose two allowed reference choices produced operators `K` and `K_tilde` and
both were claimed to satisfy

\[
 e^{a+bw}\det{}_2(I+iwK)
 =\xi(1/2+w)
 =e^{\widetilde a+\widetilde bw}
  \det{}_2(I+iw\widetilde K).
\]

The scalar exponential affects only orders zero and one.  `L-15128` therefore
forces

\[
 \operatorname{Tr}(K^m)
 =\operatorname{Tr}(\widetilde K^m)
 \qquad(m\ge2).
 \tag{R-15107.3}
\]

The exact model above shows that this is not a generic consequence of Sobolev
realization.

Therefore one of the following must be supplied:

1. a theorem proving that the full realized operator is independent, up to
   unitary conjugacy, of every allowed reference/chart/exponent choice; or
2. one completely fixed choice together with the all-order arithmetic moment
   identity for that exact choice.

The paper's phrase `choose once and for all` supplies neither theorem.

## 5. Relation to the central-comparison gap

This obstruction is independent of the elementary fact that a Hilbert--Schmidt
self-adjoint determinant has critical-line zeros.  It explains why the central
comparison in `R-15106` is load bearing: it must remove every regularization
choice from the determinant moments or prove that the arithmetic ledger changes
covariantly with it.

In particular, the Sobolev sandwich proves only

\[
 K\in\mathfrak S_2.
\]

It does not prove

\[
 \det{}_2(I+iwK)=e^{-a-bw}\xi(1/2+w).
\]

## 6. Scope

The finite model does not prove that one particular fully specified Shimizu
operator cannot match `xi`. It proves that the regularization step is not
spectrally neutral and that a missing invariance/all-moment theorem cannot be
replaced by the existence of a convenient Schatten realization.
