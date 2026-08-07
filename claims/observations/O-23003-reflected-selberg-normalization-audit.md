# O-23003 — Reflected Selberg normalization audit

Claim ID: `O-23003`  
Status: **PROPOSED AUDIT / LOCAL FIX**  
Date: 2026-08-07  
Target: PR #226 `L-9516`

## 1. One sign typo

Let

\[
A(s)=\sum a(n)n^{-s},
\qquad B(s)=A(s)^{-1}=\sum b(n)n^{-s}.
\]

Because

\[
A'(s)=-\sum a(n)\log n\,n^{-s},
\]

the coefficients of

\[
-{A'(s)\over A(s)}
\]

are

\[
\boxed{\Lambda_A=b*(a\log),}
\]

not `-b*(a log)` as written in one sentence of `L-9516`.

The subsequent second-derivative identity is nevertheless correctly oriented:

\[
\boxed{
 b*(a\log^2)=\Lambda_A\log+\Lambda_A*\Lambda_A.}
\]

Indeed its Dirichlet series is

\[
{A''\over A}
 =-\left(-{A'\over A}\right)'
  +\left(-{A'\over A}\right)^2.
\]

## 2. Reflected subtraction survives the repair

For the two conjugate twists, the product logarithmic derivative is

\[
\Lambda_\times=\Lambda_++\Lambda_-.
\]

Subtracting the two individual second-derivative identities from the product
identity gives exactly

\[
\boxed{
 C_\times-C_+-C_-
 =2\Lambda_+*\Lambda_-.}
\]

On a real vertical line in the absolute-convergence half-plane this is

\[
2\left|\zeta'/\zeta(\sigma+it)\right|^2.
\]

Thus the Hermitian-square algebra is retained after correcting the local sign
typo.

## 3. Critical-line proof interface still required

The displayed Dirichlet-series derivation is initially valid for `sigma>1`.
Using it for the critical prime-Hardy block must be done through an exact finite
coefficient/window identity, with every endpoint and pole-model term retained,
or through a separately justified contour continuation.

Compact support of the ratio kernel makes such a finite identity plausible, but
it is not supplied merely by writing the absolutely convergent equality and
setting `sigma=1/2+alpha` with `alpha<1/2`.

A final packet must therefore bind:

1. the finite coefficient cutoff;
2. the autocorrelation Fourier convention;
3. pole and archimedean subtractions;
4. all contour residues if continuation is used;
5. the equality between the finite reflected forcing and the declared block
   energy.

This audit repairs, rather than rejects, `L-9516`.
