# L-104501 — Exact complex reverse-Rolle transport with boundary winding

Claim ID: `L-104501`  
Status: **PROVED EXACT**  
Created: 2026-08-22  
Depends on: `L-104500`  
RH status: **not assumed**

Let `Omega` be a bounded conjugation-symmetric Jordan domain whose real slice
is the interval `(a,b)`.  Let `F` be holomorphic on a neighbourhood of the
closure of `Omega`, real on the real axis, and suppose:

1. `F` and `F'` have no zero on `partial Omega`;
2. the real zeros of `F'` in `(a,b)` are simple;
3. `F` and `F'` have no common real zero in `[a,b]`;
4. `F(a)F(b) != 0`.

Write:

\[
N_\Omega(F)=\#\{\text{zeros of }F\text{ in }\Omega\},
\]

counted with multiplicity,

\[
N_\mathbb R(F)=\#\{\text{real zeros of }F\text{ in }(a,b)\},
\]

and

\[
O_\Omega(F)=N_\Omega(F)-N_\mathbb R(F).
\]

Define the boundary winding

\[
\boxed{
W(F,F';\Omega)
=
{1\over2\pi i}
\int_{\partial\Omega}
\left({F'(z)\over F(z)}
      -{F''(z)\over F'(z)}\right)dz.
}
\tag{L-104501.1}
\]

By the argument principle,

\[
W(F,F';\Omega)=N_\Omega(F)-N_\Omega(F').
\tag{L-104501.2}
\]

Let `E(F;(a,b))`, `B_-`, and `B_+` be the exact wrong-extremum and endpoint
defects of `L-104500`.  Substituting the real reverse-Rolle count into
(L-104501.2) gives

\[
\boxed{
\begin{aligned}
O_\Omega(F)
={}&O_\Omega(F')
+2E(F;(a,b))\\
&+B_-+B_+
+W(F,F';\Omega)-1.
\end{aligned}
}
\tag{L-104501.3}
\]

This is an identity, not an inequality.

## Derivative-ladder form

Let `F_k=F^(k)`.  Suppose the hypotheses hold simultaneously through order
`r` on one common domain.  Put

\[
W_k=W(F_k,F_{k+1};\Omega),
\quad
E_k=E(F_k;(a,b)),
\quad
B_k=B_{k,-}+B_{k,+}.
\]

Iteration gives

\[
\boxed{
O_\Omega(F_0)
=
O_\Omega(F_r)
+
2\sum_{k=0}^{r-1}E_k
+
\sum_{k=0}^{r-1}(B_k+W_k-1).
}
\tag{L-104501.4}
\]

Every term is integer-valued and source-visible:

```text
O(F_r)       high-derivative off-real zeros;
2 E_k        wrong-extremum conjugate-pair charge;
B_k          real interval boundary mismatch;
W_k - 1      complex contour/boundary transport defect.
```

For a polynomial on a large disk containing every zero, `W_k=1` and the
endpoint defects vanish; (L-104501.4) reduces to `L-104500.5`.

## Xi specialization

Let

\[
\Xi(t)=\xi(1/2+it),
\qquad F_k=\Xi^{(k)}.
\]

A nonreal zero `t=gamma-i(beta-1/2)` of `Xi` is exactly an off-critical-line
zero `beta+i gamma` of `xi`.  On a conjugation-symmetric rectangle in the
`t`-plane, (L-104501.4) is therefore an exact accounting identity for the
critical-line defect.

The theorem shows why a global proportion cannot be descended by Rolle alone.
A successful Xi cascade must control both:

1. the wrong-extremum charges `E_k`;
2. the boundary/winding charges `B_k+W_k-1`.

Neither charge is permitted to disappear into an unspecified `O(1)` term when
the derivative order grows.
