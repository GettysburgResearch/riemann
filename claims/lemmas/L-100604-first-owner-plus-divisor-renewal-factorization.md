# L-100604 — First-owner decomposition plus divisor renewal factors all future structure positively

Claim ID: `L-100604`
Status: **PROVED EXACT FACTORIZATION; OWNER-SIGN ESTIMATE OPEN**
Depends on: PR #652 `L-99601`; PR #671 `L-99961`
RH status: **not assumed**

Consider the exact sequential first-owner identity

\[
\prod_i(I-r_iU_i)f
=s_kf+\sum_i\lambda_i(I-U_i)\prod_{h>i}(I-r_hU_h)f.
\]

Fix an owner index `i` and expand the future Euler product. Each future monomial corresponds to a divisor label `d` composed only of primes `p_h`, `h>i`. After applying any compact physical kernel, the contribution of the divisor-restricted source is exactly of the form covered by PR #671:

\[
B_d(z)=\beta(d)B(z)G_d(z),
\]
with every coefficient of `G_d` nonnegative.

Therefore the future-completed owner current admits an exact expansion

\[
\boxed{
\Delta_i^{\rm fut}f
=\sum_d \beta(d)\,\mathcal P_{i,d}f,
}
\]
where every operator `P_(i,d)` is a positive dilation renewal of one common owner-frozen base packet. The owner difference `(I-U_i)` remains outside this positive future transport.

Equivalently, after the first-owner coefficient `lambda_i` is included,

\[
\boxed{
\prod_i(I-r_iU_i)f
=s_kf+\sum_i\lambda_i\sum_d\beta(d)
 (I-U_i)\mathcal P_{i,d}f.
}
\]

All future-prime combinatorics have been moved into positive operators. The only signs left are:

1. the explicit divisor coefficient `beta(d)`;
2. the explicit owner difference `(I-U_i)`.

No unknown sign is hidden in the future completion.

## Subpower transport

For each fixed Mellin line `sigma>1/2`, PR #671 gives

\[
\|\mathcal P_{i,d}\|_{\sigma}\ll_{\sigma,\varepsilon}d^\varepsilon.
\]

Thus any subpower one-sided estimate for the owner/divisor coefficient packet survives the future renewal with only subpower loss.

## Matrix consequence

The original nonlocal gate `FCHD67` is strictly reduced to `ODSB100604`:

> prove a subpower logarithmic one-sided bound for the explicit owner-difference/divisor-sign packet before positive renewal.

This is a narrower gate than `FCHD67`: future-prime source structure is no longer part of the unknown estimate.

The theorem does not claim `ODSB100604` proved.