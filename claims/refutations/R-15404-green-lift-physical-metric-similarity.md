# R-15404 — A lifted contraction need not contract the physical output metric

Claim ID: `R-15404`  
Title: The Green-lift similarity obstruction in the Volterra endpoint argument  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: `L-15423`; elementary finite-dimensional Hilbert-space algebra  
Scope: the metric jump in the endpoint Green-lift route  
Related counterexample candidates: none

## Refuted inference

The following implication is false without a metric-identification theorem:

```text
C E = I,
||K||_lift <= 1,
T = C K E
    =>
||T||_physical <= 1.
```

It remains false even when:

- `C` is invertible, so there is no closed-fiber or endpoint-kernel issue;
- `E=C^-1` is the unique right inverse;
- `K` is unitary;
- all Euler--Lagrange orthogonality conditions on `ker C` are vacuous.

## Exact two-dimensional counterexample

Take the lifted and physical vector spaces to be `R^2` with their ordinary
Euclidean norms, and define

\[
 C=\begin{pmatrix}2&0\\0&1\end{pmatrix},
 \qquad
 E=C^{-1}=\begin{pmatrix}1/2&0\\0&1\end{pmatrix},
 \tag{R-15404.1}
\]

\[
 K=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
 \tag{R-15404.2}
\]

Then

\[
 CE=I,
 \qquad
 K^*K=I.
 \tag{R-15404.3}
\]

However,

\[
 T=CKE
 =\begin{pmatrix}0&2\\1/2&0\end{pmatrix},
 \tag{R-15404.4}
\]

so

\[
 T^*T
 =\begin{pmatrix}1/4&0\\0&4\end{pmatrix},
 \qquad
 \boxed{\|T\|_{\rm physical}=2>1.}
 \tag{R-15404.5}
\]

Thus pointwise or lifted multiplier contractivity does not survive a
non-isometric similarity transform.

## Quotient metric restores exact contractivity

The minimum-lift quotient norm induced by `C` is

\[
 \|y\|_q^2
 =\|Ey\|_2^2
 ={1\over4}|y_1|^2+|y_2|^2.
 \tag{R-15404.6}
\]

In this metric,

\[
 \|Ty\|_q^2
 ={1\over4}|2y_2|^2+|y_1/2|^2
 =\|y\|_q^2.
 \tag{R-15404.7}
\]

Hence `T` is an exact quotient isometry while being a factor-two expansion in
the physical Euclidean metric.

This is precisely the distinction isolated in `L-15423`.

## General finite-dimensional formula

For a surjective matrix `C`, the minimum-norm lift is

\[
 E=C^*(CC^*)^{-1},
 \tag{R-15404.8}
\]

and the quotient Gram on the output is

\[
 \boxed{G_q=(CC^*)^{-1}.}
 \tag{R-15404.9}
\]

A pre-existing physical Gram `G_phys` agrees with the quotient metric iff

\[
 \boxed{G_{\rm phys}=(CC^*)^{-1}.}
 \tag{R-15404.10}
\]

For a general right inverse and physical metric, the correct condition remains

\[
 \boxed{
 G_{\rm phys}-T^*G_{\rm phys}T\succeq0,}
 \tag{R-15404.11}
\]

or the equivalent compressed Green commutator in `L-15423`.

## Consequence for the current Volterra route

The displayed facts

```text
|kappa(s,u)| <= 1,
C E = I,
Euler--Lagrange orthogonality in the trace fiber
```

do not by themselves prove contraction in the physical branch `L2` metric.
One must additionally prove that the Green lift is minimum-norm for the exact
physical plus-profile metric, or prove the physical commutator LMI directly.

This does not refute a correctly proved endpoint Green theorem. It refutes only
the silent replacement of the Green quotient metric by the physical output
metric.

## Gap audit

- The counterexample has no nontrivial kernel, so adding closed-fiber density
  does not repair the implication.
- `K` is exactly unitary; approximation error is irrelevant.
- The quotient theorem of `L-15423` survives unchanged.
- A source-specific Volterra identity may still prove the physical metric
  equality; that identity is the remaining positive target.
