# L-106444 — Endpoint companion barycenter and off-line-pair ledger

Claim ID: `L-106444`  
Status: **PROVED EXACT FOR REAL POLYNOMIALS; SYMMETRIC CANONICAL-PRODUCT PASSAGE IS FORMAL**  
Created: 2026-08-25  
Depends on: Hermite--Biehler index identity `L-105280`; `L-106440`  
RH status: **not assumed**

Let `p` be a real monic polynomial of degree `n>K`, with root sum

\[
S=\sum_{p(z)=0}z,
\]

and let `K` be even.  Put

\[
D_K(z)
 =(p+i\lambda p')(p^{(K)}-i\lambda p^{(K+1)}).
\]

## 1. Exact complex barycenter

The root sum of the first factor is

\[
S-i\lambda n.
\]

The root sum of the second factor is

\[
{n-K\over n}S+i\lambda(n-K).
\]

Therefore

\[
\boxed{
\sum_{D_K(z)=0}z
 =\left(2-{K\over n}\right)S-i\lambda K.
}
\tag{L-106444.1}

For every centered or even polynomial, `S=0`, so

\[
\boxed{
\sum_{D_K(z)=0}\operatorname{Im}z=-\lambda K.
}
\tag{L-106444.2}

The conjugate numerator of the endpoint all-pass symbol has barycenter
`+i lambda K`.  The cancellation is independent of the degree and of every
other coefficient of `p`.

## 2. Exact half-plane counts

Let `q_j` be the number of nonreal conjugate pairs of `p^(j)`.  Thus

\[
R_j=\deg(p^{(j)})-2q_j.
\]

The Hermite--Biehler index formula gives

\[
\begin{array}{c|cc}
&\text{upper zeros}&\text{lower zeros}\\ \hline
p+i\lambda p'&q_0&n-q_0\\
p^{(K)}-i\lambda p^{(K+1)}&(n-K)-q_K&q_K.
\end{array}
\tag{L-106444.3}

Consequently

\[
\boxed{
N_+(D_K)-N_-(D_K)
 =-K+2(q_0-q_K)
 =R_K-R_0
 =-\operatorname{wind}U_{0,K}.
}
\tag{L-106444.4
}

Thus the endpoint all-pass defect is literally the excess of upper-half-plane
denominator companions.  The high endpoint contributes only its already-known
off-line-pair count `q_K`; the remaining excess is the parent off-line count.

## 3. Shallow-excess consequence

Write the upper heights as `u_j>0` and the absolute lower heights as
`ell_j>0`.  Equation (L-106444.2) is

\[
\boxed{
\sum_j u_j-\sum_j\ell_j=-\lambda K.
}
\tag{L-106444.5}

For every `h>0`,

\[
\boxed{
h\,\#\{j:u_j\ge h\}
 \le\sum_j\ell_j-\lambda K.
}
\tag{L-106444.6}

Hence a large positive half-plane-count excess can occur only through a large
population of upper companion zeros below the chosen height or through a
compensating lower-depth budget.  This makes the remaining signed-tail theorem
a quantitative near-real companion-zero problem rather than an unspecified
contour loss.

For Xi canonical-product truncations chosen symmetrically, `S=0`; the formulas
pass to every finite regular window with the usual endpoint ledger.  No
uniform lower bound on the companion heights is claimed.