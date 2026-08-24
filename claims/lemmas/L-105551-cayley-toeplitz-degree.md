# L-105551 — Cayley degree as a Toeplitz/Hankel index

Claim ID: `L-105551`  
Status: **PROVED EXACT FOR RATIONAL UNIMODULAR SYMBOLS**  
Created: 2026-08-24  
Depends on: finite Blaschke factorization; Fourier coefficient identities  
RH status: **not assumed**

Let `u` be a rational unimodular function on the unit circle with no boundary
pole.  Write its reduced finite Blaschke factorization as

\[
u=\omega\,\frac{B_+}{B_-},
\tag{L-105551.1}
\]

where `omega` is unimodular and `B_+,B_-` have no common zero.  Let their
degrees be `n_+,n_-`.

Then

\[
\boxed{\deg u=n_+-n_-,}
\tag{L-105551.2}
\]

\[
\boxed{\operatorname{rank}H_u=n_-,\qquad
       \operatorname{rank}H_{\bar u}=n_+,}
\tag{L-105551.3}
\]

and

\[
\boxed{
\deg u=
\|H_{\bar u}\|_{\rm HS}^2-
\|H_u\|_{\rm HS}^2.
}
\tag{L-105551.4}
\]

The Toeplitz operator has

\[
\boxed{\operatorname{ind}T_u=-\deg u.}
\tag{L-105551.5}
\]

## Proof

The factorization proves (L-105551.2).  Since

\[
H_u=H_{\bar B_-}T_{B_+},
\]

`H_u f=0` exactly when `B_-` divides `B_+ f`.  Coprimality implies
`ker H_u=B_-H^2`, of codimension `n_-`; the range is finite-dimensional, so
`rank H_u=n_-`.  The conjugate statement is symmetric.

If `u_hat(k)` are the Fourier coefficients, then

\[
\|H_u\|_{m HS}^2=\sum_{k<0}(-k)|\widehat u(k)|^2,
\qquad
\|H_{\bar u}\|_{m HS}^2=\sum_{k>0}k|\widehat u(k)|^2.
\]

Because `|u|=1`, integration of `bar u u'` gives

\[
\deg u=\sum_{k\in\mathbb Z}k|\widehat u(k)|^2,
\]

which is (L-105551.4).  The Toeplitz index formula follows from the same
factorization.

For the compactified companion ratio of `L-105550`, `deg u` is the distinct
real-root count and `rank H_u` is the wrong-half-plane companion count.
