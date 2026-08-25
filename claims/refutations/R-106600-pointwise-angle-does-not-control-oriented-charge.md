# R-106600 — Pointwise phase alignment does not control oriented Hankel charge

Claim ID: `R-106600`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-26  
RH status: **unproved**

For \(a>0\), let

\[
B_a(z)=\frac{z-ia}{z+ia},
\qquad
U_a=\frac1{B_a}.
\]

On the real line,

\[
U_a(t)=\frac{t+ia}{t-ia}\longrightarrow1
\]

for every fixed \(t\ne0\) as \(a\downarrow0\). Hence

\[
|1-U_a(t)|^2\longrightarrow0
\]

pointwise away from one point.

Nevertheless \(B_a\) has one upper-half-plane zero, and

\[
\boxed{\|H_{U_a}\|_{\mathcal S_2}^2=1}
\tag{R-106600.1}
\]

for every \(a>0\).

Indeed,

\[
\beta_a'(t)=\frac{2a}{t^2+a^2},
\qquad
|1-U_a(t)|^2=\frac{4a^2}{t^2+a^2},
\]

and therefore

\[
\frac1{4\pi}\int_{\mathbb R}
\beta_a'(t)|1-U_a(t)|^2\,dt
=
\frac1{4\pi}
\int_{\mathbb R}
\frac{8a^3}{(t^2+a^2)^2}\,dt
=1.
\]

The positive phase measure concentrates at the same rate as the boundary
angle disappears.

Consequently none of the following is a valid closure step:

```text
send the companion scale pointwise to zero;
minimize |1-U| without beta';
replace the oriented phase mean by unweighted convergence in measure;
infer small index from pointwise boundary alignment.
```

Any adaptive-scale proof must control the complete measure
\(\beta_a'(t)dt\), or an exactly equivalent model-space quantity.
