# L-105622 — The current–Turán two-trace source matrix is positive at every frequency

Claim ID: `L-105622`  
Status: **PROVED EXACT MATRIX-VALUED FOURIER THEOREM**  
Created: 2026-08-25  
Depends on: `L-105620--L-105621`; `L-105260`  
RH status: **not assumed**

## 1. The matrix source

Retain

\[
j_h(\xi)=\widehat J_h(\xi),
\qquad
\lambda_2(\xi)=\Lambda_2(\xi).
\]

For every real frequency define

\[
\boxed{
\mathbb G_h(\xi)
=
\begin{pmatrix}
 e^{h\xi}j_h(\xi) & h\lambda_2(\xi)\\
 h\lambda_2(\xi) & e^{-h\xi}j_h(\xi)
\end{pmatrix}.
}
\tag{L-105622.1}
\]

The two diagonal weights are the natural upper/lower analytic trace gauges.
The off-diagonal entry is the common actual Turan exterior-square source before
choosing one analytic orientation.

## 2. Pointwise positive semidefiniteness

Let

\[
D_h(\xi)
=\operatorname{diag}(e^{h\xi/2},e^{-h\xi/2}).
\]

Then

\[
\boxed{
\mathbb G_h(\xi)
=D_h(\xi)
\begin{pmatrix}
 j_h(\xi)&h\lambda_2(\xi)\\
 h\lambda_2(\xi)&j_h(\xi)
\end{pmatrix}
D_h(\xi).
}
\tag{L-105622.2}
\]

The central matrix has eigenvalues

\[
j_h(\xi)\pm h\lambda_2(\xi).
\]

Both are nonnegative by `L-105620`. Hence

\[
\boxed{
\mathbb G_h(\xi)\succeq0
\qquad(\xi\in\mathbb R).
}
\tag{L-105622.3}
\]

Equivalently,

\[
\det\mathbb G_h(\xi)
=j_h(\xi)^2-h^2\lambda_2(\xi)^2
\ge0.
\tag{L-105622.4}
\]

The higher-chaos reserve gives the explicit factorization

\[
\begin{aligned}
\begin{pmatrix}j_h&h\lambda_2\\h\lambda_2&j_h\end{pmatrix}
={}&
\bigl(j_h-h\lambda_2\bigr)I
+h\lambda_2
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\end{aligned}
\tag{L-105622.5}
\]

where

\[
j_h-h\lambda_2\ge {h^3\over6}\Lambda_4.
\]

Thus the common mode is paid by the actual Turan source and the orthogonal
mode is paid by the higher exterior-square chaoses.

## 3. Arbitrary diagonal source phase

For any measurable real phase `theta(xi)`, put

\[
\mathbb G_{h,\theta}(\xi)
=
D_h(\xi)
\begin{pmatrix}
 j_h(\xi)&h e^{i\theta(\xi)}\lambda_2(\xi)\\
 h e^{-i\theta(\xi)}\lambda_2(\xi)&j_h(\xi)
\end{pmatrix}
D_h(\xi).
\]

The eigenvalues of the central matrix remain
`j_h plus-or-minus h lambda_2`. Therefore

\[
\boxed{
\mathbb G_{h,\theta}(\xi)\succeq0
}
\tag{L-105622.6}
\]

for every frequencywise phase. The source theorem is already uniform in every
phase which is diagonal in the coefficient coordinate.

## 4. Integrated two-trace Gram

For any nonnegative scalar weight `w(xi)` and any measurable vector field
`v(xi) in C^2`,

\[
\boxed{
\int_{\mathbb R}
 w(\xi)
 \langle\mathbb G_{h,\theta}(\xi)v(\xi),v(\xi)\rangle
 \,d\xi
\ge0.
}
\tag{L-105622.7}
\]

Thus every diagonal truncation, dyadic decomposition and source-owned unitary
change of the two-trace coefficient space preserves positivity.

## 5. Exact location of the physical obstruction

The physical phase

\[
U_h(a)=\overline{\Xi'(a+ih)}/\Xi'(a+ih)
\]

is multiplication in the spatial variable. In the Fourier source coordinate it
is convolution, not a diagonal phase `theta(xi)`. Therefore (L-105622.6) does
not directly apply. The physical obstruction is exactly the failure of that
convolution to commute with the diagonal contraction

\[
r_h(\xi)=h e^{-h\xi}\Lambda_2(\xi)/j_h(\xi).
\]

The theorem proves that the two traces, the reflected source and every
diagonal source phase are already compatible. Only the non-diagonal all-pass
collision and finite-window endpoints remain.

## 6. Scope

This is matrix-valued Fourier positivity, not pointwise positivity of a spatial
matrix. Fourier inversion does not preserve pointwise matrix order. No claim is
made that the variable Xi-prime phase is diagonal, that the physical Loewner
matrix is positive, or that RH follows.
