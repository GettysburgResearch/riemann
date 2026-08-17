# R-96600 — No zero-safe finite shift filter can make the positive-source Green kernel one-signed

Claim ID: `R-96600`  
Status: **PROVED EXACT NO-GO THEOREM**  
Created: 2026-08-17  
RH status: **not assumed**

The positive occupancy source of the complete endpoint is convolved with

\[
k(t)=\left(1-{t\over2}\right)\mathbf1_{t\ge0},
\]

whose Laplace transform is

\[
\widehat k(s)={s-1/2\over s^2}.
\tag{R-96600.1}
\]

Let

\[
P(s)=\sum_{j=0}^Jc_je^{-h_js}
\]

be any finite real shift multiplier. Assume it is **zero-safe** for an RH consumer, meaning

\[
P(s)\ne0\qquad(\Re s>0).
\]

The filtered causal kernel

\[
g(t)=\sum_jc_jk(t-h_j)\mathbf1_{t\ge h_j}
\]

has

\[
\widehat g(s)=P(s){s-1/2\over s^2}.
\]

Since zero safety gives `P(1/2) != 0`,

\[
\widehat g(1/2)=0.
\tag{R-96600.2}
\]

If `g` were nonzero and one-signed, then its Laplace integral at the positive real point `s=1/2` would have the same strict sign and could not vanish. Therefore

\[
\boxed{
\text{every nonzero zero-safe finite-shift filter of }k
\text{ changes sign.}
}
\tag{R-96600.3}
\]

This rules out a tempting completion of `ACTQ_2`: compact support and a zero-safe multiplier cannot be combined with source-blind one-sign positivity by finite shifts. A successful annular producer must use arithmetic cancellation, a nonlinear state, or a matrix/Schur mechanism.
