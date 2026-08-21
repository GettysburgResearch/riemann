# L-103303 — The centered positive cubic compactifier is an exact autocorrelation Gram kernel

Claim ID: `L-103303`  
Status: **PROVED EXACT KERNEL FACTORIZATION**  
Created: 2026-08-21  
Depends on: PR #696 `L-102000`  
RH status: **not assumed**

Let `h=log a` and define

\[
b_\rho(t)=e^{\rho t}\mathbf1_{[0,h]}(t).
\]

PR #696 proves that the positive cubic compactifier satisfies, in logarithmic
coordinate,

\[
\mathcal K_{a,3}(e^u)
=48(b_0*b_{1/2}*b_1*b_{3/2})(u).
\tag{L-103303.1}
\]

After centering at the self-reciprocal exponent `3/4`,

\[
 e^{-3u/4}\mathcal K_{a,3}(e^u)
=48(b_{-3/4}*b_{-1/4}*b_{1/4}*b_{3/4})(u).
\tag{L-103303.2}
\]

Put

\[
f_h=b_{1/4}*b_{3/4}
\]

and let `(Rf)(u)=f(-u)`.  The box identities

\[
b_{-3/4}=e^{-3h/4}\tau_hRb_{3/4},
\qquad
b_{-1/4}=e^{-h/4}\tau_hRb_{1/4}
\]

give

\[
\boxed{
 e^{-3(v+2h)/4}\mathcal K_{a,3}(e^{v+2h})
=48e^{-h}(Rf_h*f_h)(v).
}
\tag{L-103303.3}
\]

Therefore

\[
\boxed{
\widehat{\mathscr K}_h(\gamma)
=48e^{-h}|\widehat f_h(\gamma)|^2\ge0,
}
\tag{L-103303.4}
\]

where the left side denotes the Fourier transform of the centered and shifted
kernel in (L-103303.3).

This is an explicit Gram factorization, stronger than pointwise positivity.
It supplies a same-occurrence Cauchy port for every arithmetic source which is
itself represented as a convolution square.  It does not by itself orient a
linear Möbius convolution: product geometry and ratio/autocorrelation geometry
must still be matched on the same source ledger.
