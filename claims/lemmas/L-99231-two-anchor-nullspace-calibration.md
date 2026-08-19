# L-99231 — Two positive anchors calibrate the complete Volterra nullspace

Claim ID: `L-99231`  
Status: **PROVED EXACT CONDITIONAL CONE THEOREM**  
Created: 2026-08-19  
Depends on: `L-99230`  
RH status: **unproved**

Assume two current-owned positive anchored packets have homogeneous equality
observables

\[
\phi_j(x)=u_j\sqrt x+v_jx,
\qquad j=0,1.
\]

Put

\[
M=
\begin{pmatrix}
u_0&u_1\\
v_0&v_1
\end{pmatrix}.
\]

If `det M != 0`, the unique coefficients matching the boundary modes of
`L-99230` are

\[
\boxed{
\begin{pmatrix}c_0\\c_1\end{pmatrix}
=
M^{-1}
\begin{pmatrix}A_a\\B_a\end{pmatrix}.
}
\tag{L-99231.1}
\]

Suppose:

1. `d(Vf)>=0`, including every activation-knot atom;
2. `c_0,c_1>=0`;
3. each kernel packet and anchor carries one common typed feature vector
   containing target, literal score, every ordinary/radix-four response, and
   every future child label.

Then

\[
\boxed{
P_f
=
c_0P_0+c_1P_1
+
\int P_t\,d(Vf)(t)
}
\tag{L-99231.2}
\]

is a positive exact equality-frame realization of `f` in every listed
coordinate.

Conversely, a negative knot atom or a negative component of
`M^{-1}(A_a,B_a)^T` is a finite separating certificate for this two-anchor
mechanism.

The theorem reduces the equality-frame audit to:

```text
directed smooth density on every activation cell;
all derivative-jump atoms;
one nonzero 2x2 anchor determinant;
two nonnegative anchor coefficients;
one common typed feature measure.
```
