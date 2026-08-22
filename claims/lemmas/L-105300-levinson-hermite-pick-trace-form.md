# L-105300 — Levinson–Hermite–Pick trace form for one derivative descent

Claim ID: `L-105300`
Status: **PROVED EXACT AT FINITE-POLYNOMIAL SCOPE**
Created: 2026-08-23
Arithmetic class: exact algebra over the real coefficient field
RH status: not assumed

## 1. Setup

Let

\[
p(x)=x^n+a_{n-1}x^{n-1}+\cdots+a_0\in\mathbb R[x],\qquad n\ge2,
\]

be monic. Assume that `p` and `p'` are squarefree. Thus `p` has no common
zero with `p'`, every critical point of `p` is simple, and

\[
\rho_c:=\frac{p(c)}{p''(c)}\ne0
\qquad (p'(c)=0)
\tag{L-105300.1}
\]

is defined.

Put

\[
A_p:=\mathbb R[x]/(p'),
\qquad
q_p(x):=-p(x)\,(p''(x))^{-1}\pmod {p'(x)}.
\tag{L-105300.2}
\]

The inverse exists because `p'` is squarefree. Define the real symmetric
trace form

\[
\boxed{
\mathcal B_p(u,v)
:=\operatorname{Tr}_{A_p/\mathbb R}\bigl(q_puv\bigr).
}
\tag{L-105300.3}
\]

At a critical point `c`, one has

\[
q_p(c)=-\rho_c.
\tag{L-105300.4}
\]

Let

```text
G(p) = number of real critical points c with rho_c < 0;
E(p) = number of real critical points c with rho_c > 0;
C(p) = number of conjugate nonreal critical-point pairs.
```

The letters `G` and `E` denote Rolle-generating and wrong extrema,
respectively.

## 2. Exact local decomposition of the trace form

Since `p'` is squarefree, the real algebra `A_p` decomposes as a product of
one copy of `R` for every real critical point and one copy of `C` for every
nonreal conjugate pair.

On a real factor `c`, the form is the one-dimensional form

\[
(u,v)\longmapsto -\rho_cuv.
\tag{L-105300.5}
\]

It is positive exactly when `rho_c<0` and negative exactly when `rho_c>0`.

For a nonreal critical point `c` in the upper half-plane, write

\[
-\rho_c=a+ib.
\]

On the corresponding real two-dimensional factor `C`, in the basis `(1,i)`,
(L-105300.3) is

\[
2\begin{pmatrix}
 a&-b\\
 -b&-a
\end{pmatrix}.
\tag{L-105300.6}
\]

Its determinant is `-4(a^2+b^2)<0`, so it has signature `(1,1)`.
Consequently

\[
\boxed{
\operatorname{inertia}(\mathcal B_p)
=\bigl(G(p)+C(p),\ E(p)+C(p)\bigr).
}
\tag{L-105300.7}
\]

In particular,

\[
\operatorname{sig}(\mathcal B_p)=G(p)-E(p).
\tag{L-105300.8}
\]

## 3. Pick-kernel realization

Set

\[
R_p(z)=\frac{p(z)}{p'(z)},
\qquad
L_p(z)=\frac{p'(z)}{p(z)}.
\]

For a real rational function `R`, write

\[
K_R(z,w)=\frac{R(z)-\overline{R(w)}}{z-\overline w}.
\tag{L-105300.9}
\]

Since `R_p=1/L_p`,

\[
\boxed{
K_{R_p}(z,w)
=-\frac{K_{L_p}(z,w)}{L_p(z)\overline{L_p(w)}}.
}
\tag{L-105300.10}
\]

This is an exact congruence of finite-rank Hermitian kernels away from their
poles.

The partial fraction expansion is

\[
\frac{p(z)}{p'(z)}
=\frac zn-\frac{s_1}{n^2}
 +\sum_{p'(c)=0}\frac{\rho_c}{z-c},
\qquad s_1=\sum_{p(z_j)=0}z_j.
\tag{L-105300.11}
\]

Hence the coefficient matrix of `K_(R_p)` is congruent to

\[
\langle 1/n\rangle\oplus\mathcal B_p.
\tag{L-105300.12}
\]

Alternatively, the root partial fractions of `L_p` show directly that every
real root of `p` contributes one negative square to `K_(L_p)`, while every
nonreal conjugate root pair contributes one positive and one negative square.
The congruence (L-105300.10) reverses the signs. Therefore, if `r(p)` is the
number of real roots of `p`, counted with multiplicity (all are simple under
our assumptions), and `q(p)=(n-r(p))/2`, then

\[
\boxed{
\operatorname{inertia}(K_{R_p})=(r(p)+q(p),\ q(p)).
}
\tag{L-105300.13}
\]

Comparing (L-105300.7) and (L-105300.12) gives the exact reverse–Rolle count

\[
\boxed{
r(p)=1+G(p)-E(p).
}
\tag{L-105300.14}
\]

Equivalently,

\[
\boxed{
q(p)=E(p)+C(p).
}
\tag{L-105300.15}
\]

Thus the negative index of the antiderivative Pick kernel is exactly the
number of nonreal root pairs of `p`; decomposed at the derivative level, it is
wrong real extrema plus nonreal critical-point pairs.

## 4. Coefficient-computable matrix

Let `m=n-1`, let `X` be the multiplication-by-`x` matrix in the monomial basis

\[
1,x,\ldots,x^{m-1}
\]

of `A_p`, and let `Q=q_p(X)`. The matrix of the trace form is

\[
\boxed{
(B_p)_{ij}=\operatorname{tr}\bigl(QX^{i+j}\bigr),
\qquad 0\le i,j<m.
}
\tag{L-105300.16}
\]

Every entry is obtained from the coefficients of `p` by rational polynomial
arithmetic, extended Euclid modulo `p'`, matrix multiplication, and trace. No
critical point, root, contour, or floating-point factorization is required.

The augmented matrix

\[
\boxed{H_p=\langle1\rangle\oplus B_p}
\tag{L-105300.17}
\]

is nonsingular and satisfies

\[
\boxed{
\operatorname{sig}(H_p)=r(p),
\qquad
\nu_+(H_p)=\frac{n+r(p)}2,
\qquad
\nu_-(H_p)=\frac{n-r(p)}2.
}
\tag{L-105300.18}
\]

This is the finite, coefficient-exact low-order Levinson descent object.

## 5. Scope

The theorem is finite algebra. It does not yet construct a height-localized
`Xi` trace form, pass through canonical products, or prove an asymptotic
inertia estimate. Those are the analytic tasks isolated in `T-105300`.
