# R-102867 — The naïve four-owner quadratic-character lift collapses by reciprocity

Claim ID: `R-102867`  
Status: **PROVED EXACT CHARACTER FIREWALL**  
Created: 2026-08-24  
Depends on: `T-102870`; clean four-owner sector  
RH status: **not assumed**

Let

\[
N=pq\,a^2,
\qquad M=rs\,b^2
\]

belong to the clean sector, with `p,q,r,s` four distinct odd primes and with no
owner in the opposite square core. Put

\[
d=N-M.
\]

Then

\[
\left(\frac d p\right)
=\left(\frac{-rs}p\right),
\qquad
\left(\frac d q\right)
=\left(\frac{-rs}q\right),
\]

and

\[
\left(\frac d r\right)
=\left(\frac{pq}r\right),
\qquad
\left(\frac d s\right)
=\left(\frac{pq}s\right).
\]

Let

\[
\epsilon_\ell=\frac{\ell-1}{2}\pmod2.
\]

Quadratic reciprocity gives

\[
\boxed{
\prod_{\ell\in\{p,q,r,s\}}
\left(\frac d\ell\right)
=
(-1)^{(\epsilon_p+\epsilon_q)
(1+\epsilon_r+\epsilon_s)}.
}
\tag{R-102867.1}

The right side depends only on the four residue classes modulo `4`; it contains
no core or owner oscillation.

## Consequence

Inserting all four Legendre symbols into the physical cross term does not
create a new large-sieve direction. Their product is a rank-four residue-class
sign matrix. Applying a quadratic large sieve separately to both reciprocal
character factors and then multiplying the estimates merely destroys the
exact reciprocity cancellation and cannot be counted as independent savings.

A useful quadratic-character transform must therefore be combined with a
nontrivial additive/core phase or with the balanced Vaughan variables; the
four-character identity alone cannot prove `BQSP102870`.

The exact additive nonzero-phase identities of `L-102860--L-102865` remain
valid and are not refuted by this theorem.
