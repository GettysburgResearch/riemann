# L-91105 — The safe Xi Pick matrix is exactly a Cayley anticommutator

Claim ID: `L-91105`  
Status: **EXACT FINITE-MATRIX IDENTITY**  
Created: 2026-08-11  
Depends on: PR #398 safe-real Pick criterion  
RH status: **unproved**

## 1. Centered safe coordinate

Put

\[
M(r)=\frac{\xi(\frac12+r)}{\xi(\frac12)},
\qquad r\in\mathbb R,
\]

and fix

\[
0<a<\frac12.
\]

For every safe real coordinate `r>a+1/2` define

\[
 d_a(r)=\frac{M(r-a)}{M(r+a)}
 =\frac{\xi(\frac12+r-a)}{\xi(\frac12+r+a)},
\tag{L-91105.1}
\]

and its Cayley impedance

\[
\boxed{
 \ell_a(r)=\frac{1-d_a(r)}{1+d_a(r)}
 =\frac{M(r+a)-M(r-a)}{M(r+a)+M(r-a)}.
}
\tag{L-91105.2}
\]

The relation with PR #398 is `u=2a` and

\[
 r=q+\frac{1+u}{2}.
\]

Thus the moving half-plane becomes the fixed right half-plane `Re r>0`, and the Cauchy denominator is independent of `a`.

## 2. Exact Cayley congruence

Take finitely many positive nodes `r_1,...,r_N` and put

\[
 C_{ij}=\frac1{r_i+r_j},
 \qquad
 D=\operatorname{diag}(d_a(r_i)),
 \qquad
 L=\operatorname{diag}(\ell_a(r_i)).
\tag{L-91105.3}
\]

Then

\[
 D=(I-L)(I+L)^{-1}.
\]

Because `L` is diagonal,

\[
\begin{aligned}
 (I+L)(C-DCD)(I+L)
 &=(I+L)C(I+L)-(I-L)C(I-L)\\
 &=2(LC+CL).
\end{aligned}
\]

Therefore

\[
\boxed{
 C-DCD
 =2(I+L)^{-1}(LC+CL)(I+L)^{-1}.
}
\tag{L-91105.4}
\]

Since `I+L` is invertible on the safe real line,

\[
\boxed{
 C-DCD\succeq0
 \iff
 LC+CL\succeq0.
}
\tag{L-91105.5}
\]

Entrywise, the remaining matrix is

\[
\boxed{
 (LC+CL)_{ij}
 =\frac{\ell_a(r_i)+\ell_a(r_j)}{r_i+r_j}.
}
\tag{L-91105.6}
\]

Thus the final safe Pick problem is exactly a positive-real/Carathéodory kernel problem for the scalar impedance `ell_a`.

## 3. Cross-multiplied kernel

Let

\[
 A_i=M(r_i+a),\qquad B_i=M(r_i-a).
\]

Then diagonal congruence by `diag(A_i)` gives

\[
\boxed{
 C-DCD\succeq0
 \iff
 \widetilde K_a[\mathbf r]\succeq0,
}
\tag{L-91105.7}
\]

where

\[
\boxed{
 \widetilde K_a(r,s)
 =\frac{M(r+a)M(s+a)-M(r-a)M(s-a)}{r+s}.
}
\tag{L-91105.8}
\]

This form contains no quotient and no possible denominator cancellation. It is the preferred Brownian/theta port kernel.

## 4. Infinitesimal endpoint

Taylor expansion at `a=0` gives

\[
 \ell_a(r)
 =a\frac{M'(r)}{M(r)}+O_r(a^3).
\tag{L-91105.9}
\]

Equivalently, with `u=2a`,

\[
 \frac{\ell_{u/2}(r)}u
 \longrightarrow
 \frac12\frac{\xi'(\frac12+r)}{\xi(\frac12+r)}.
\tag{L-91105.10}
\]

Hence the finite horizontal transport is a nonlinear integration of the endpoint Xi Loewner kernel. The safe Pick route of PR #398 and the theta Green--Cayley anticommutator of PR #202 are the same noncommutative obstruction in different coordinates.

## 5. Strategic meaning

The old target was a difficult difference of two Cauchy Grams. The exact Cayley move replaces it by:

> Construct a positive-real realization of `ell_a`.

A passive state-space or Dirichlet-to-Neumann realization of `ell_a` automatically factors every finite matrix (L-91105.6), and PR #398 then supplies global Schur continuation and RH.

No positivity of (L-91105.6) is asserted here.
