# R-104517 — Every nontrivial finite mixed-theta matrix is indefinite at the origin

Claim ID: `R-104517`  
Status: **EXACT REFUTATION OF THE STRONG MTSG FORMULATION**  
Created: 2026-08-23  
Depends on: `L-104531`, `L-104532`  
RH status: **unproved**

Let

\[
F_n(t)=\widehat g_n(t)
\]

be the positive theta-orbit Fourier transforms of `L-104531`, and let

\[
\mathcal T_{mn}(t)
=F_m'(t)F_n'(t)
-\frac12\bigl(F_m(t)F_n''(t)+F_n(t)F_m''(t)\bigr)
\]

be the mixed Turán entries of `L-104532`.

## 1. Exact origin matrix

Every `g_n` is even and strictly positive away from the origin. Put

\[
a_n=F_n(0)=\int_{\mathbb R}g_n(u)\,du>0,
\qquad
b_n=-F_n''(0)=\int_{\mathbb R}u^2g_n(u)\,du>0.
\]

Since `F_n'(0)=0`, one has

\[
\boxed{
\mathcal T_{mn}(0)=\frac12(a_mb_n+a_nb_m).
}
\tag{R-104517.1}
\]

For two distinct orbit labels `m,n`, the corresponding principal determinant is

\[
\boxed{
\det
\begin{pmatrix}
 a_mb_m & \frac12(a_mb_n+a_nb_m)\\
 \frac12(a_mb_n+a_nb_m) & a_nb_n
\end{pmatrix}
=-\frac14(a_mb_n-a_nb_m)^2.
}
\tag{R-104517.2}
\]

Thus positivity of the finite matrix would force the moment ratios `b_n/a_n`
to be identical for every orbit.

## 2. The actual orbit ratios are strictly ordered

For `u>=0`, write

\[
h_n(u)=n^{-1/2}\phi(u+\log n),
\]

so that `g_n(u)=u^2h_n(u)` on the positive half-line.  If `m>n`, put

\[
q=(m/n)^2>1,
\qquad
x=\pi n^2e^{2u}.
\]

The explicit orbit source gives

\[
\frac{h_m(u)}{h_n(u)}
=
\left(\frac mn\right)^2
\frac{2qx-3}{2x-3}
 e^{-(q-1)x}.
\tag{R-104517.3}
\]

Differentiating its logarithm yields

\[
\boxed{
\frac d{du}\log\frac{h_m}{h_n}
=
-\frac{12x(q-1)}{(2qx-3)(2x-3)}
-2x(q-1)
<0.
}
\tag{R-104517.4}
\]

Multiplication by the common factor `u^2` does not change this likelihood
ratio.  Hence the probability density proportional to `u^2h_m(u)` is strictly
smaller than the density proportional to `u^2h_n(u)` in monotone-likelihood-
ratio order. Since `u^2` is strictly increasing,

\[
\boxed{
\frac{b_m}{a_m}<\frac{b_n}{a_n}
\qquad(m>n).
}
\tag{R-104517.5}
\]

Therefore the square in (R-104517.2) is nonzero for every `m!=n`.

## 3. Verdict

For every `N>=2`, the finite mixed theta matrix

\[
\mathbf T_N(0)=[\mathcal T_{mn}(0)]_{m,n\le N}
\]

has a strictly negative `2 x 2` principal minor and is indefinite. Consequently

```text
"T_N(t) is PSD for every N,t"                 FALSE;
weighted diagonal dominance implying that PSD FALSE for the actual origin data;
all-ones scalar positivity                     still open and not refuted.
```

The stronger matrix version of `MTSG104560` must not remain a live proof target.
The only conclusion-facing object is the scalar all-ones quadratic form

\[
\mathbf1_N^T\mathbf T_N(t)\mathbf1_N.
\]

This refutation is source-specific: it uses the exact theta-orbit profiles, not
a generic two-frequency toy model.