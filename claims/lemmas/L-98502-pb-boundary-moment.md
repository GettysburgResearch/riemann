# L-98502 — Exact first signed boundary moment of the finite-prime annular base

Claim ID: `L-98502`  
Status: **UNCONDITIONAL EXACT MELLIN ALGEBRA + DIRECTED FINITE SIGN CHECK**  
Created: 2026-08-18  
RH status: **not assumed**

Let
\[
Q_*(z)=6\zeta(z)-6+9\,2^{-z}-3\,4^{-z}
\]
and, for a prime cutoff \(B\),
\[
P_B(z)=\prod_{p\le B}(1-p^{-z}).
\]
The finite-prime annular base has Mellin transform
\[
\widehat b_B(s)=
\frac{1-4^{-s}}{s^2}
Q_*(s+\tfrac12)P_B(s+\tfrac12).
\tag{L-98502.1}
\]

At \(s=1/2\),
\[
\widehat b_B(s)=
\frac{a_B}{s-1/2}+\kappa_B+O(s-1/2),
\]
where
\[
\boxed{
a_B=12\prod_{p\le B}\left(1-\frac1p\right)>0
}
\tag{L-98502.2}
\]
and
\[
\boxed{
\frac{\kappa_B}{a_B}
=
\sum_{p\le B}\frac{\log p}{p-1}
+\gamma+\log4-\frac{35}{8}.
}
\tag{L-98502.3}
\]

The proof is direct differentiation:
\[
\frac{d}{ds}\log\frac{1-4^{-s}}{s^2}
\Big|_{s=1/2}
=\log4-4,
\]
the finite part of \(Q_*\) is
\[
6\gamma-\frac94,
\]
and
\[
\frac{P_B'(1)}{P_B(1)}
=
\sum_{p\le B}\frac{\log p}{p-1}.
\]

The retained directed evaluation proves
\[
\boxed{\kappa_{11}<0<\kappa_{13}}
\tag{L-98502.4}
\]
and hence \(\kappa_B>0\) for every cutoff \(B\ge13\), including \(B=61\).

Under the signed transfer of `L-98500`, \(\kappa_B\) is the zeroth boundary
moment:
\[
\kappa_B=
\int_0^\infty
\left[e^{-w/2}b_B(e^w)-a_B\right]dw.
\tag{L-98502.5}
\]
Thus the first continuum correction is
\[
\frac{\kappa_B}{\log z}\rho'(u).
\tag{L-98502.6}
\]

Since \(\rho'(u)<0\), the \(P_{61}\) correction is adverse but relative:
\[
\frac{\kappa_{61}\rho'(u)/\log z}{a_{61}\rho(u)}
=
O\!\left(\frac{\log(2u)}{\log z}\right).
\]
The cutoff \(B=11\) has the opposite first correction and is a useful
control-variate state, although it does not by itself prove the root scalar.
