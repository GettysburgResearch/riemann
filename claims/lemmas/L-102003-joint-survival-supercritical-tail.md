# L-102003 — Exact finite joint-tail law and the supercritical-survival no-go

Claim ID: `L-102003`
Status: **PROVED EXACT FINITE-TRUNCATION IDENTITY; EARLIER SUPPRESSION CLAIM WITHDRAWN**
Created: 2026-08-21
Audited: 2026-08-21
Depends on: PR #691 `L-100616`
RH status: **not assumed**

The joint least/greatest-owner law must be interpreted first on a finite label
set. Let the ordered labels be `1,...,k`, put

\[
r_i=p_i^{-1/2},\qquad
L_i=\prod_{h<i}(1-r_h),\qquad
R_j^{(k)}=\prod_{j<h\le k}(1-r_h),
\]

and

\[
\pi_{ij}^{(k)}=r_ir_jL_iR_j^{(k)}.
\]

For `j>=1`,

\[
R_{j-1}^{(k)}=(1-r_j)R_j^{(k)},
\qquad
R_j^{(k)}-R_{j-1}^{(k)}=r_jR_j^{(k)}.
\tag{L-102003.1}
\]

Therefore, for every `J>i`,

\[
\boxed{
\sum_{j=J}^{k}\pi_{ij}^{(k)}
=r_iL_i\bigl(1-R_{J-1}^{(k)}\bigr).
}
\tag{L-102003.2}
\]

The earlier version had the telescoping sign reversed. The right tail is not
bounded by `r_i L_i R_J`.

## Fixed least owner: supercritical widths retain full mass

Fix `i` and any finite threshold index `J>i`, for example the first index with

\[
p_J>p_i^A
\]

for a fixed `A>1`. Since

\[
\sum_{h\ge J}r_h=\sum_{h\ge J}p_h^{-1/2}=\infty,
\]

one has

\[
R_{J-1}^{(k)}\longrightarrow0
\qquad(k\to\infty).
\]

Hence

\[
\boxed{
\sum_{j=J}^{k}\pi_{ij}^{(k)}
\longrightarrow r_iL_i.
}
\tag{L-102003.3}
\]

Thus, conditional on a fixed least owner `i`, asymptotically all of its
finite-truncation pair mass has greatest owner beyond every fixed power of
`p_i`. Joint survival prevents an artificial divergent marginal norm, but it
does **not** suppress the supercritical-width region.

## Large least owners do have small total mass

The left survival telescopes in the opposite direction:

\[
L_{i+1}=(1-r_i)L_i,
\qquad
L_i-L_{i+1}=r_iL_i.
\]

Consequently, if `I` is the first index with `p_I>=P`,

\[
\boxed{
\sum_{i=I}^{k}r_iL_i
=L_I-L_{k+1}
\le L_I,
}
\tag{L-102003.4}
\]

and `L_I->0` as `P->infinity`. This only removes rows whose **least** owner is
large. It gives no saving for the finitely many low least-owner rows, which
carry essentially full mass into arbitrarily wide intervals by
(L-102003.3).

## Infinite-source firewall

For the infinite Bernoulli family, every fixed right survival product is zero
because `sum p^-1/2` diverges. Individual finite min--max atoms therefore lose
their mass to a greatest owner escaping to infinity. One may not define an
infinite pair law by simply inserting the zero infinite products and then
infer a useful tail estimate.

```text
earlier right-tail suppression claim       FALSE
finite joint min--max identity             PROVED EXACT
large least-owner mass vanishes            PROVED
fixed least-owner supercritical mass       ASYMPTOTICALLY FULL
collar amplitude/sign estimate             STILL OPEN
Riemann Hypothesis                         UNPROVED
```
