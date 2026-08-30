# L-104536 — Associated-kernel hierarchy and exact sine-tail criterion

Claim ID: `L-104536`  
Status: **PROVED EXACT REFORMULATION**  
Created: 2026-08-23  
Depends on: `L-104531`, `L-104534`; classical Csordas associated-kernel theorem  
RH status: **not assumed**

Let

\[
\mathcal H_j(x)
=\int_{\mathbb R}y^{2j}\Phi(x+y)\Phi(x-y)\,dy
\qquad(j=0,1,2,\ldots)
\]

be the classical associated kernels of the Riemann theta source.

## 1. Exact three-kernel compression

Since `g(u)=u^2 Phi(u)`,

\[
\begin{aligned}
\mathcal K_2(x)
&=\int y^2(x+y)^2(x-y)^2
       \Phi(x+y)\Phi(x-y)\,dy\\
&=\int \bigl(x^4y^2-2x^2y^4+y^6\bigr)
       \Phi(x+y)\Phi(x-y)\,dy.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal K_2(x)
=x^4\mathcal H_1(x)
-2x^2\mathcal H_2(x)
+\mathcal H_3(x).
}
\tag{L-104536.1}
\]

This is a complete-source identity.  The three terms may not be estimated
separately before the polynomial cancellation is retained.

Strict logarithmic concavity of `Phi` implies, by the classical associated-
kernel theorem, that every `H_j` is an admissible even kernel.  Admissibility is
not positive definiteness; the coefficients in (L-104536.1) have mixed sign.

## 2. Tail primitive

Put

\[
\mathcal G_2(x)=\int_x^\infty\mathcal K_2(u)\,du,
\qquad
A_2=\mathcal G_2(0)=\int_0^\infty\mathcal K_2(u)\,du.
\]

The kernel is even, continuous, integrable and nonnegative. Integration by
parts gives, for `t!=0`,

\[
\begin{aligned}
\int_0^\infty\mathcal K_2(x)\cos(2tx)\,dx
&=A_2-2t\int_0^\infty\mathcal G_2(x)\sin(2tx)\,dx.
\end{aligned}
\tag{L-104536.2}
\]

Since

\[
\mathcal L_2(t)=8\int_0^\infty\mathcal K_2(x)\cos(2tx)\,dx,
\]

one obtains the exact equivalence

\[
\boxed{
\mathcal L_2(t)\ge0\ \text{for every real }t
\iff
\int_0^\infty\mathcal G_2(x)\sin(2tx)\,dx
\le\frac{A_2}{2t}
\quad(t>0).
}
\tag{L-104536.3}
\]

Thus the modular Gram lane may be attacked as one explicit one-dimensional
sine-tail inequality rather than an infinite theta-orbit matrix.

## 3. Source-visible expansion of the tail

Using (L-104536.1),

\[
\boxed{
\mathcal G_2(x)
=\int_x^\infty
\left[u^4\mathcal H_1(u)
      -2u^2\mathcal H_2(u)
      +\mathcal H_3(u)
\right]du.
}
\tag{L-104536.4}
\]

Every term is built from the same untruncated Jacobi source.  This is the
correct location for the recent second-level theta-concavity information and
for a Pólya/Dirichlet sine-transform argument.

## 4. Scope firewall

The following implications are invalid:

```text
all H_j admissible                 -> K_2 positive definite;
K_2 pointwise positive             -> K_2 positive definite;
individual theta-orbit Turán signs -> complete sine-tail inequality.
```

Equation (L-104536.3), or an equivalent complete-source Gram, is the actual
remaining theorem.