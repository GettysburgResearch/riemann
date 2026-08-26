# R-105460 — The positive ratio-four half-kernel is TP2 but not TP3

Claim ID: `R-105460`

Status: **PROVED EXACT COUNTEREXAMPLE; BINDING HIGHER-MINOR FIREWALL**

Let

\[
L=\log2,
\qquad
a(u)=A(e^u),
\]

where \(A\) is the positive half-kernel of the common-mother factorization.
The exact formula from `L-103000` is

\[
a(u)=
\begin{cases}
2(e^{u/2}-1),&0<u<L,\\
2\sqrt2(1-e^{(u-2L)/2}),&L<u<2L,\\
0,&\text{otherwise}.
\end{cases}
\tag{R-105460.1}
\]

Its translation kernel \(K(u,x)=a(u-x)\) is `TP_2`.  It is not `TP_3`.

Take

\[
(u_1,u_2,u_3)
 =
 \left(\frac54L,\frac32L,2L\right),
\qquad
(x_1,x_2,x_3)
 =
 \left(0,\frac14L,\frac12L\right),
\]

and put \(t=2^{1/8}>1\).  Factoring \(2\) from every matrix entry gives

\[
\bigl(K(u_i,x_j)\bigr)_{i,j=1}^3
 =
 2
 \begin{pmatrix}
 t^4-t&t^4-1&t^3-1\\
 t^4-t^2&t^4-t&t^4-1\\
 0&t^4-t^3&t^4-t^2
 \end{pmatrix}.
\tag{R-105460.2}
\]

Direct expansion yields

\[
\boxed{
\det\bigl(K(u_i,x_j)\bigr)
 =
 -8t^4(t-1)^3(t+1)(t^4+1)<0.
}
\tag{R-105460.3}
\]

Hence \(K\) fails total positivity of order three.

## Consequence

The exact `TP_2` endpoint orientation remains valid.  However, no closure may
invoke any of the following without additional arithmetic input:

```text
TP3 of the positive half-kernel;
positivity of all 3-by-3 translated minors;
a source-blind higher-minor upgrade of the pair Plücker argument;
a PF-infinity or variation-diminishing claim for A.
```

This counterexample does not refute the finite prime-box Hodge index or the
Boolean/Wick configuration square.  It isolates the failure at physical
translation level, exactly where `F1VAR105460` remains open.
