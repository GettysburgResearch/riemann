# L-104514 — Quantitative growing-box Hermite–Biehler entry for high Xi derivatives

Claim ID: `L-104514`  
Status: **PROVED FROM THE TILTED-FOURIER CONCENTRATION OF L-104504**  
Created: 2026-08-22  
Depends on: `L-104504`  
RH status: **not assumed**

Use the probability measure

\[
d\nu_n(u)=Z_n^{-1}u^{2n}\Phi(u)\,du
\]

and let `w_n` be its saddle. Write

\[
\sigma_n^2=\int(u-w_n)^2\,d\nu_n(u).
\]

The Laplace calculation of `L-104504` gives

\[
w_n=\tfrac12\log n+O(\log\log n),
\qquad
\sigma_n\asymp\sqrt{\frac{w_n}{n}},
\tag{L-104514.1}
\]

and, for every fixed `H`,

\[
\int e^{H|u-w_n|}|u-w_n|\,d\nu_n(u)
\ll_H\sigma_n.
\tag{L-104514.2}
\]

Let `T_n` satisfy

\[
T_n\sigma_n\longrightarrow0.
\tag{L-104514.3}
\]

Then uniformly on

\[
|\Re z|\le T_n,\qquad -H\le\Im z\le0,
\]

one has

\[
\frac{(-1)^n\Xi^{(2n)}(z)}
     {(-1)^n\Xi^{(2n)}(0)}
=
\cos(w_nz)+O_H(T_n\sigma_n)e^{w_n|\Im z|},
\tag{L-104514.4}
\]

and, by differentiating the same integral,

\[
\frac{(-1)^n\Xi^{(2n+1)}(z)}
     {w_n(-1)^n\Xi^{(2n)}(0)}
=
-\sin(w_nz)+O_H(T_n\sigma_n+\sigma_n/w_n)
e^{w_n|\Im z|}.
\tag{L-104514.5}
\]

Define the normalized companion

\[
\mathcal E_n(z)=
\frac{(-1)^n}
     {(-1)^n\Xi^{(2n)}(0)}
\left[
\Xi^{(2n)}(z)-\frac{i}{w_n}\Xi^{(2n+1)}(z)
\right].
\]

Equations (L-104514.4--5) give

\[
\mathcal E_n(z)
=
e^{iw_nz}
+
o(1)e^{w_n|\Im z|}.
\tag{L-104514.6}
\]

On the lower-half-plane part of the box,

\[
|e^{iw_nz}|=e^{w_n|\Im z|}.
\]

Rouché therefore yields

\[
\boxed{
\mathcal E_n(z)\ne0
\quad
(|\Re z|\le T_n,\ -H\le\Im z<0)
}
\tag{L-104514.7}
\]

for all sufficiently large `n`.

A concrete admissible scale is

\[
T_n=o\!\left(\sqrt{\frac{n}{\log n}}\right).
\tag{L-104514.8}
\]

This is a genuine Hermite–Biehler entry theorem, stronger than merely counting
real zeros of the high derivative. It does not descend the index to `Xi`.
