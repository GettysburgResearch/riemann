# L-105657 — Cauchy concavity is one vertical multipoint Schwarz--Pick kernel

Claim ID: `L-105657`  
Status: **PROVED EXACT EQUIVALENCE; THE FINAL KERNEL POSITIVITY REMAINS OPEN**  
Created: 2026-08-27  
Depends on: `L-105656`; finite model-space reproducing kernels  
RH status: **unproved**

Fix `H>0` and write

\[
x_j=\lambda_j+\frac H2,
\qquad
y_j=x_j+H=\lambda_j+\frac{3H}{2}.
\]

Let

\[
\Theta(z)
=
\prod_{k=1}^n
\frac{z-x_k}{z+\overline{x_k}}
\]

be the right-half-plane finite Blaschke product with zero packet `x_k`.

## 1. Projection kernel at the translated packet

The Hardy Gram at the zeros `x_j` is

\[
[k(x_i,x_j)]=G_H.
\]

The cross Gram between the zeros `x_i` and the translated points `y_j` is

\[
[k(x_i,y_j)]=G_{2H},
\]

while the Hardy Gram at the translated packet is

\[
[k(y_i,y_j)]=G_{3H}.
\]

The model space `K_Theta` is the span of the kernels at the zeros `x_j`.
Therefore the Gram of the projected translated kernels is

\[
\boxed{
[K_\Theta(y_i,y_j)]
=
G_{2H}G_H^{-1}G_{2H}.
}
\tag{L-105657.1}

On the other hand, the de Branges--Rovnyak kernel is

\[
K_\Theta(z,w)
=
\frac{1-\Theta(z)\overline{\Theta(w)}}
{z+\overline w}.
\]

Hence, with

\[
d_j=\Theta(y_j)
=
\prod_{k=1}^n
\frac{\lambda_j-\lambda_k+H}
{\lambda_j+\overline{\lambda_k}+2H},
\tag{L-105657.2}
\]

one has the exact residual identity

\[
\boxed{
G_{3H}-G_{2H}G_H^{-1}G_{2H}
=D^*G_{3H}D,
\qquad D=\operatorname{diag}(d_1,\ldots,d_n).
}
\tag{L-105657.3}

This is the complete interpolation residual; no matrix inversion remains
conceptually hidden.

## 2. Exact vertical Schwarz--Pick matrix

Since

\[
(G_{3H}-G_{4H})_{ij}
=
\frac{H}
{(\overline y_i+y_j)(\overline y_i+y_j+H)},
\]

`MLC105656` is equivalent to

\[
D^*G_{3H}D
\preceq
G_{3H}-G_{4H}.
\tag{L-105657.4}
\]

Entrywise, this is precisely the positivity of

\[
\boxed{
\mathbb V_H(i,j)
=
\frac{
\displaystyle {H\over\overline y_i+y_j+H}
-\overline{\Theta(y_i)}\Theta(y_j)
}
{\overline y_i+y_j}.
}
\tag{L-105657.5}
\]

Thus

\[
\boxed{
\mathbb V_H\succeq0
\Longleftrightarrow
\mathrm{MLC105656}
\Longrightarrow
\mathrm{CTI105655}.
}
\tag{L-105657.6}

The remaining finite theorem is one explicit multipoint Schwarz--Pick-type
kernel on the translated zero packet.

## 3. One-factor check

For one zero `x`,

\[
\Theta(x+H)=\frac{H}{2\operatorname{Re}x+H}.
\]

The single entry of (L-105657.5) is nonnegative exactly when

\[
\frac{H}{2\operatorname{Re}(x+H)+H}
\ge
\frac{H^2}{(2\operatorname{Re}x+H)^2},
\]

which reduces to

\[
4(\operatorname{Re}x)^2
+2H\operatorname{Re}x
+2H^2
\ge0.
\]

Hence the vertical kernel is positive in rank one, consistently with
`L-105654/L-105656`.

## 4. Why ordinary Schwarz--Pick is insufficient

The scalar inequalities

\[
|\Theta(y_j)|
\le
\left|\frac{y_j-x_j}{y_j+\overline{x_j}}\right|
\]

control only the diagonal of `mathbb V_H`.  They do not establish the complete
multipoint matrix.  A proof must retain all cross terms and confluent limits.
Likewise, determinant positivity or every two-point restriction does not by
itself imply all-packet positivity.

## 5. Scope

The lemma proves an equivalence, not the positivity of `mathbb V_H` in general.
It does not establish `CTI105655`, the cofinal Xi passage, the operator-level
phase theorem, or RH.
