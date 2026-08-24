# R-106020 — Phase cardinality is nonintrinsic, but the quadratic root is not a new core channel

Claim ID: `R-106020`  
Status: **PROVED EXACT TWO-PART FAMILY FIREWALL**  
Created: 2026-08-24  
Depends on: `L-106020--L-106022`; PR #719 `R-102867`  
RH status: **unproved**

## A. The phase-cardinality loss is not intrinsic

For a square-supported physical packet modulo an odd prime `p`, ordinary
Cauchy gives

\[
\left\|\sum_{h=1}^{p-1}F_h\right\|^2
\le(p-1)\sum_{h=1}^{p-1}\|F_h\|^2.
\]

But the Ramanujan identity and `L-106020` give the strictly stronger theorem

\[
\boxed{
\left\|\sum_{h=1}^{p-1}F_h\right\|^2
\le{p-1\over p+1}
\sum_{h=1}^{p-1}\|F_h\|^2.
}
\tag{R-106020.1}
\]

Thus a factor of order `p` in a fixed-packet estimate is a basis-blind Cauchy
loss, not an unavoidable source cost. Previous estimates using that Cauchy
step remain valid but are nonsharp and must not be treated as lower bounds on
the true difficulty.

## B. Deleting the quadratic root deletes the principal leverage

Under the Gauss--Mellin transform,

\[
\eta=\chi^2.
\]

Both

\[
\chi=1
\qquad\text{and}\qquad
\chi=\kappa_p
\]

map to `eta=1`. For a fixed owner product `P`, their core transforms differ
only by the scalar sign `kappa_p(P)` and therefore have equal norm.

Consequently the exact untwisted contribution to the square-phase energy is

\[
{1+p\over p-1}\|F_{\eta=1}\|^2,
\]

where the `1` is the principal Gauss weight and the `p` is the quadratic Gauss
weight.

A theorem controlling only characters with `chi^2 != 1` does not control the
native core field. Conversely, counting the quadratic character as an
independent oscillatory core direction is false. Across four owner primes the
corresponding product of quadratic signs collapses by the reciprocity identity
in PR #719 `R-102867`.

## Consequence

A viable owner-conductor family argument must retain the full
principal/quadratic root fibre and the nonprincipal even characters in one
source-faithful moment, or add a genuinely independent core family. It may not:

```text
pay phase cardinality by generic Cauchy;
discard the quadratic root as one exceptional member;
claim nonquadratic moment bounds automatically individualize the native field;
reuse the collapsed four-Legendre product as an independent large-sieve axis.
```

The remaining coherent family moment is stated in `T-106020`.