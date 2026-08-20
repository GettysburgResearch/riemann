# L-102002 — The valid conjunction is a same-occurrence joint min–max certificate

Claim ID: `L-102002`
Status: **PROVED ABSTRACT AND-GATE; COMPOSITE-OWNER IDENTIFICATION OPEN**
Created: 2026-08-21
Audited: 2026-08-21
Depends on: PR #691 `L-100616`; `L-102001`
RH status: **not assumed**

The double-owner framework supplies the finite-source joint coefficient

\[
\pi_{ij}=r_ir_jL_iR_j,
\]

which is the literal probability that `i,j` are the least and greatest
selected labels. Any valid first-owner/last-owner conjunction must preserve
this coefficient until after both estimates have been attached to the same
collar occurrence.

For a real physical observation, `L-100616` gives

\[
(OEf)_-
\le\sum_{i<j}\pi_{ij}(H_{ij})_-.
\tag{L-102002.1}
\]

Suppose two concrete nonnegative certificates on that same occurrence satisfy

\[
\boxed{(H_{ij})_-^2\le A_{ij}B_{ij}.}
\tag{L-102002.2}
\]

Then Cauchy--Schwarz on the joint min--max probability space gives

\[
\boxed{
(OEf)_-
\le
\left(\sum_{i<j}\pi_{ij}A_{ij}\right)^{1/2}
\left(\sum_{i<j}\pi_{ij}B_{ij}\right)^{1/2}.
}
\tag{L-102002.3}
\]

Equation (L-102002.2) requires a **product**, not a sum. Replacing its
right-hand side by `A_ij+B_ij` would not imply (L-102002.3).

The divergent one-sided marginal refutation `R-100616` does not apply to
(L-102002.3), because neither outside survival factor has been deleted.

## Relationship to the Vaughan coordinates

`L-102001` proves that each active outer divisor pair in the balanced Vaughan
form is parabolic and admits exact coordinates

\[
d=ga,\qquad e=gb,\qquad \mu^2(gab)=1.
\]

It does **not** construct a canonical map from one Vaughan divisor pair to one
prime-label min--max occurrence of `L-100616`. That map is precisely part of
the open composite-owner lifting problem.

Accordingly, the following is a target schema rather than a proved
specialization. After constructing a source-faithful occurrence index
`omega` that simultaneously records its prime min/max owners and its coupled
`(g,a,b)` divisor data, prove

\[
\boxed{
(\operatorname{collar}_{\omega})_-^2
\le
A_{\omega}^{\rm future}
B_{\omega}^{\rm cofactor}.
}
\tag{L-102002.4}
\]

Both certificates must be evaluated before summing over `omega`, and the
literal joint owner weight must remain attached.

## Exact boundary

```text
same-occurrence Cauchy--Schwarz AND-gate       PROVED EXACT
plus-to-product correction                     BINDING
Vaughan parabolic/gcd coordinates              PROVED IN L-102001
Vaughan pair -> prime min/max occurrence map   OPEN
future certificate on that occurrence          OPEN
cofactor certificate on that occurrence        OPEN
Riemann Hypothesis                              UNPROVED
```

No claim that the two open local certificates have been constructed is made
here.