# L-103003 — Owner endpoint determinants become common-mother Wronskians

Claim ID: `L-103003`  
Status: **PROVED EXACT PLÜCKER/WRONSKIAN IDENTITY**  
Created: 2026-08-25  
Depends on: `L-102701`; `L-103001--L-103002`; PR #730 `T-105440--L-105451`  
RH status: **not assumed**

Let `mu=(mu_n)` and `nu=(nu_n)` be finitely supported real source sequences on positive physical locations. Define their two common-mother half-fields

\[
F_\mu^-(X)=\sum_n\mu_n A_-(X/n),
\qquad
F_\mu^+(X)=\sum_n\mu_n A(X/n),
\]

and similarly for `nu`.

Form the antisymmetric endpoint determinant

\[
\mathcal P_{\mu,\nu}(X)
=F_\mu^-(X)F_\nu^+(X)
-F_\mu^+(X)F_\nu^-(X).
\tag{L-103003.1}
\]

Bilinearity and the antisymmetry of the Wronskian kernel give the coefficient-exact expansion

\[
\boxed{
\mathcal P_{\mu,\nu}(X)
=
\sum_{n<m}
\Delta_{n,m}(\mu,\nu)
\mathcal W_{n,m}(X),
}
\tag{L-103003.2}
\]

where

\[
\boxed{
\Delta_{n,m}(\mu,\nu)
=
\mu_n\nu_m-\mu_m\nu_n
}
\tag{L-103003.3}
\]

is the literal two-by-two Plücker minor of the source columns.

This identity occurs before a physical norm or negative part. It is compatible with the source-exact radial owner decomposition and the endpoint/Plücker rectangles of PR #730: every antisymmetric owner endpoint pair is observed through the fixed kernel `mathcal W` and carries its own source minor `Delta`.

## 1. Monotone-ratio sign criterion

Assume `nu_n>0` on the common support.

If

\[
n\longmapsto {\mu_n\over\nu_n}
\]

is nondecreasing, then for `n<m`,

\[
\Delta_{n,m}(\mu,\nu)\le0.
\]

Since `mathcal W_{n,m}<=0` by `L-103001`,

\[
\boxed{
\mathcal P_{\mu,\nu}(X)\ge0
\quad\text{for every }X.
}
\tag{L-103003.4}
\]

If the ratio is nonincreasing, the sign is reversed:

\[
\boxed{
\mathcal P_{\mu,\nu}(X)\le0.
}
\tag{L-103003.5}
\]

Thus a monotone-likelihood ordering of the two literal endpoint source measures gives a pointwise physical sign theorem.

## 2. Exact inversion support

For arbitrary source sequences, split the minors according to whether their sign agrees with the declared physical order. By `L-103002`, every order-concordant minor has a fixed sign after observation. Only the minors whose sign violates the monotone-ratio order can contribute adversely.

This turns the former abstract owner/Plücker orientation problem into a concrete source question:

```text
which literal Boolean/Hodge endpoint minors invert their physical product order?
```

No source-blind positivity of those minors is asserted here.