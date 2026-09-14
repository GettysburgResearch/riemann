# R-106630 — Raw pairwise matching does not control a model-space defect

Claim ID: `R-106630`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-26  
RH status: **unproved**

Let \(\mathcal H=\mathbb R^2\), let

\[
v_1=(1,0)^T,
\qquad
v_2=(1,\epsilon)^T,
\qquad
u=(1,0)^T,
\qquad
\epsilon>0.
\]

Put

\[
E_-=(v_1\ v_2),
\qquad
E_+=(u).
\]

The denominator columns span all of \(\mathbb R^2\), while the numerator
column spans the first coordinate axis. Hence

\[
\boxed{
\operatorname{tr}\bigl(P_-(I-P_+)\bigr)=1.
}
\tag{R-106630.1}
\]

Nevertheless, the naive matching \(v_1\mapsto u\), \(v_2\mapsto u\) has raw
squared residual

\[
\|v_1-u\|^2+\|v_2-u\|^2=\epsilon^2\longrightarrow0.
\]

The denominator Gram is

\[
G_-=
\begin{pmatrix}
1&1\\
1&1+\epsilon^2
\end{pmatrix},
\]

and the exact generalized residual of `L-106630` is

\[
\boxed{
\operatorname{tr}
\left[
G_-^{-1}(E_--E_+X)^*(E_--E_+X)
\right]
=1
}
\]

for \(X=(1\ 1)\).

Thus an arbitrarily small unwhitened sum of pairwise distances can hide one
complete model-space direction. Any shallow-companion matching argument must
use the generalized Cauchy residual, a Takenaka--Malmquist orthonormalization,
or an exactly equivalent basis-invariant object.
