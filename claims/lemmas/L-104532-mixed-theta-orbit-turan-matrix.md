# L-104532 — Exact mixed theta-orbit Turán matrix

Claim ID: `L-104532`  
Status: **PROVED EXACT REDUCTION**  
Created: 2026-08-23  
Depends on: `L-104531`  
RH status: **not assumed**

Let

\[
F_n(t)=\widehat{g_n}(t),
\]

with `g_n` from `L-104531`.  Every `F_n` is real and even.  Define the symmetric mixed Turán entry

\[
\boxed{
\mathcal T_{mn}(t)
=
F_m'(t)F_n'(t)
-{1\over2}
\bigl(F_m(t)F_n''(t)+F_n(t)F_m''(t)\bigr).
}
\tag{L-104532.1}
\]

Absolute weighted convergence from `L-104531` gives

\[
\boxed{
\Xi'''(t)^2-\Xi''(t)\Xi''''(t)
=
\sum_{m,n\ge1}\mathcal T_{mn}(t),
}
\tag{L-104532.2}
\]

with locally uniform, indeed real-uniform, convergence after any fixed number of `t` derivatives.

## Source-side mixed kernels

Define

\[
\begin{aligned}
\mathcal K_{mn}(x)
={1\over2}\int_{\mathbb R}y^2\bigl[
&g_m(x+y)g_n(x-y)\\
+&g_n(x+y)g_m(x-y)
\bigr]dy.
\end{aligned}
\tag{L-104532.3}
\]

Every `K_mn` is real, even and symmetric in `(m,n)`, and

\[
\boxed{
\mathcal T_{mn}(t)=4\widehat{\mathcal K_{mn}}(2t).
}
\tag{L-104532.4}
\]

Moreover

\[
\mathcal K_2=\sum_{m,n\ge1}\mathcal K_{mn}.
\tag{L-104532.5}
\]

## Finite matrix form

For `N>=1`, let

\[
\mathbf T_N(t)=[\mathcal T_{mn}(t)]_{1\le m,n\le N},
\qquad
\mathbf 1_N=(1,\ldots,1)^T.
\]

Then

\[
\boxed{
\mathbf1_N^T\mathbf T_N(t)\mathbf1_N
=
(F^{(N)}{}')^2-F^{(N)}F^{(N)}{}'',
}
\tag{L-104532.6}
\]

where `F^(N)=sum_(n<=N)F_n`.

A sufficient source-faithful closure is therefore

```text
MTSG104560:
  every finite mixed theta-orbit matrix T_N(t) is positive semidefinite,
  uniformly under the strong cutoff exhaustion.
```

A weaker sufficient condition is weighted symmetric diagonal dominance: find positive weights `w_n(t)` such that

\[
w_n\mathcal T_{nn}
\ge
\sum_{m\ne n}w_m|\mathcal T_{mn}|
\quad\text{for every }n,t.
\tag{L-104532.7}
\]

Either condition implies

\[
\Xi'''(t)^2-\Xi''(t)\Xi''''(t)\ge0
\]

and hence the direct fixed-order transfer of `T-104550`.

The point of (L-104532.1--6) is that all independent-frequency cross terms are explicit.  No diagonal, trace or single-orbit positivity may be substituted for the common matrix.