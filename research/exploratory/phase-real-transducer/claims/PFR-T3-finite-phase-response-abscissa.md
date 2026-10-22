# PFR-T3 — Finite inverse-Poisson response and exact zero-height abscissa

Status: **PROVED EXACT FINITE-ZERO THEOREM**
RH status: **unproved**

Let

\[
P(z)=C\prod_j(z-a_j-ib_j)
\]

and `y>max b_j`.  Define

\[
V_{P,y}(x)=-\Im{P'\over P}(x+iy).
\]

With `hat f(t)=int f(x)e^{-itx}dx`,

\[
\widehat V_{P,y}(t)
=\pi e^{-y|t|}R_P(t),
\qquad
R_P(t)=\sum_j e^{b_j|t|}e^{-ia_jt}.
\]

If `P` has real coefficients and

\[
B(P)=\max_j|b_j|,
\]

then

\[
\int_0^\infty e^{-2\sigma t}|R_P(t)|^2dt<\infty
\quad\Longleftrightarrow\quad
\sigma>B(P).
\]

For `sigma>B(P)`,

\[
\mathcal E_P(\sigma)
=\sum_{j,k}{1\over2\sigma-b_j-b_k+i(a_j-a_k)}.
\]

Moreover, for a real polynomial the following are equivalent:

```text
all zeros real;
B(P)=0;
R_P bounded;
R_P positive definite;
E_P(sigma) finite for every sigma>0.
```

The result is finite and exact.  Extending it to a source-defined actual-Xi
window is open.
