# L-24510 — Exact scalar-mode decomposition of the carry Green energy

Claim ID: `L-24510`  
Status: `PROPOSED COMPLETE — exact finite Hilbert-space algebra`  
Scope: firewall for `T-24503`  
Issue: #245  
Depends on: `L-24509`

Let `G_X>0` be the endpoint-projected divisor Dirichlet Gram, let

\[
\lambda_q=\Lambda(q),
\qquad
r_q=v_q(b_X^{(0)})-w_X(q),
\]

and put

\[
E_X=\lambda^TG_X\lambda>0,
\qquad
\delta_X=\lambda^Tr
=J_X(b_X^{(0)})-S_X.
\tag{L-24510.1}
\]

Define

\[
\boxed{
r_X^\perp
=r-\frac{\delta_X}{E_X}G_X\lambda.}
\tag{L-24510.2}
\]

Then

\[
\lambda^Tr_X^\perp=0.
\tag{L-24510.3}
\]

## Exact orthogonal decomposition

In the `G_X^{-1}` inner product, `G_X\lambda` is the Riesz vector of the scalar functional `r mapsto lambda^T r`. Hence (L-24510.2) is the exact orthogonal projection and

\[
\boxed{
\mathcal G_X:=r^TG_X^{-1}r
=
\frac{\delta_X^2}{E_X}
+
(r_X^\perp)^TG_X^{-1}r_X^\perp.}
\tag{L-24510.4}
\]

Both terms are nonnegative.

Since `L-24509` gives `E_X<=6`,

\[
\boxed{
\mathcal G_X\ge\frac{\delta_X^2}{6}.}
\tag{L-24510.5}
\]

Thus any subpower Green-energy theorem already contains the subpower prime-ramp discrepancy

\[
J_X(b_X^{(0)})-S_X=X^{o(1)}.
\]

Conversely, a proof of the scalar discrepancy alone does not automatically control the orthogonal term in (L-24510.4).

## Physical-space interpretation

The vector `G_X lambda` corresponds to the Dirichlet gradient of

\[
h_X(j)=\log j-\frac jX\log X.
\]

Therefore the first summand in (L-24510.4) is the component of the residual potential parallel to the explicit logarithmic chord. It is exactly the square-screw/prime-ramp mode, not a generic large-eigenvalue artifact.

## Consequence for proof claims

`T-24503` is a valid sufficient theorem, but GET must not be advertised as bypassing the scalar RH obstruction. The correct statement is:

```text
GET = scalar prime-ramp mode + orthogonal additive-function energy.
```

A useful new mechanism would have to control the scalar projection by arithmetic cancellation and the orthogonal energy by an independent coercive theorem. Bounding only the orthogonal term cannot prove RH.

## Review boundary

This lemma is finite linear algebra. It makes no estimate on either term and does not prove RH.
