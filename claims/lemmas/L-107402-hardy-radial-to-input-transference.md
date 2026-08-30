# L-107402 — Exact Hardy transference from radial Hankel weights to input multipliers

Claim ID: `L-107402`  
Programme aliases: `XI90.RADIAL_INPUT_TRANSFER`, `XI.HARDY_AVERAGE_REPAIR`  
Status: **PROVED EXACT OPERATOR IDENTITY AND ENTROPY RESERVE BOUND**  
Created: 2026-08-30  
Depends on: `R-106508`; elementary Hankel calculus  
Programme issue: #744  
RH status: **not assumed**

Let

\[
(H_kf)(x)=\int_0^\infty k(x+s)f(s)\,ds
\]

be a Hilbert–Schmidt Hankel operator, and let \(0\le r\le1\) be measurable.
Define its Hardy average

\[
\boxed{
(\mathcal Hr)(q)
=
\frac1q\int_0^q r(s)\,ds
\qquad(q>0).
}
\tag{L-107402.1}
\]

## 1. Exact typed transfer

Fubini and the change of variable \(q=x+s\) give

\[
\begin{aligned}
\|H_kM_r^{1/2}\|_{\mathcal S_2}^2
&=
\int_0^\infty\int_0^\infty
|k(x+s)|^2r(s)\,dx\,ds\\
&=
\int_0^\infty
|k(q)|^2\left(\int_0^qr(s)\,ds\right)dq.
\end{aligned}
\]

Therefore

\[
\boxed{
\|H_kM_r^{1/2}\|_{\mathcal S_2}^2
=
\int_0^\infty q(\mathcal Hr)(q)|k(q)|^2\,dq.
}
\tag{L-107402.2}
\]

Thus the radial source weight and the input model multiplier are not equal, as
`R-106508` correctly observed, but they are related exactly by the Hardy
operator. This closes the type mismatch at identity level.

## 2. Reserve tail

Put

\[
A_r=\int_0^\infty(1-r(s))\,ds,
\]

and assume \(A_r<\infty\). Then

\[
\boxed{
0\le1-(\mathcal Hr)(q)
=
\frac1q\int_0^q(1-r(s))\,ds
\le
\min\!\left(1,\frac{A_r}{q}\right).
}
\tag{L-107402.3}
\]

For a normalized model vector

\[
e_{a,y}(q)=\sqrt{2y}\,e^{-(y+ia)q},
\]

define \(x=2A_ry\). If \(0<x\le1\), splitting the integral at \(q=A_r\)
gives

\[
\boxed{
\langle e_{a,y},
(I-M_{\mathcal Hr})e_{a,y}\rangle
\le
x\left(2+\log\frac1x\right).
}
\tag{L-107402.4}
\]

For \(x>1\), the left side is at most one.

For a finite Blaschke product with pole depths \(y_1,\ldots,y_m\), the causal
model-space decomposition and (L-107402.4) yield

\[
\boxed{
\operatorname{tr}_{K_B}(I-M_{\mathcal Hr})
\le
\sum_{j=1}^m
\min\!\left[
1,\,
2A_ry_j
\left(2+\log_+\frac1{2A_ry_j}\right)
\right].
}
\tag{L-107402.5}
\]

If all \(2A_ry_j\le1\), concavity gives the aggregate bound

\[
\boxed{
\operatorname{tr}_{K_B}(I-M_{\mathcal Hr})
\le
X\left(2+\log\frac mX\right),
\qquad
X=2A_r\sum_jy_j.
}
\tag{L-107402.6}
\]

## 3. Xi applicability

For every fixed odd \(K\) and fixed \(h\), the actual-Xi current profile of
PR #765 satisfies an exponentially decaying high-frequency defect. Hence
\(A_r<\infty\), and the source radial multiplier has a rigorously typed input
model counterpart \(M_{\mathcal Hr}\).

The price is an explicit height-entropy term rather than the false equality
rejected in `R-106508`.

## Scope

This theorem repairs the radial/input type interface and prices the reserve.
It does not control the numerator/denominator phase collision or the forced
unit topological spectrum.
