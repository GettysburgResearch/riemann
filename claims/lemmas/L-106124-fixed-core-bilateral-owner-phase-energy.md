# L-106124 — Fixed-core bilateral owner-phase energy is locally paid

Claim ID: `L-106124`  
Programme aliases: `LFAM1.FIXED_CORE_OWNER_ENERGY`, `LFAM2.LOCAL_BI_KUMMER_LARGE_SIEVE`, `STRESS.CONDUCTOR_FIBRE_ESTIMATE`  
Status: **PROVED UNCONDITIONAL LOCAL FIBRE THEOREM; GLOBAL CONDUCTOR SUM EXPLICITLY OPEN**  
Created: 2026-08-25  
Depends on: `L-106120--L-106122`; binding correction `R-106123`; parent `L-102958--L-102959`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Fix one complete reduced-core fibre

\[
 (g,c,d),
 \qquad
 \ell=P^-(c),
 \qquad
 \rho=P^-(d),
 \qquad
 (c,d)=1.
\]

Parent ratio-eight comparability restricts the two semiprime owner products to

\[
 P\ll d,
 \qquad
 Q\ll c.
\tag{L-106124.1}
\]

Let `(a_{P,Q})` be arbitrary Hilbert-valued coefficients on those ranges,
with any declared clean-incidence mask.

## 1. Exact local energy estimate

Put

\[
 F_{h,k}
 =
 \sum_{P,Q}a_{P,Q}
 e_\ell(-hQd^2)e_\rho(kPc^2).
\]

Since `d` is a unit modulo `ell` and `c` is a unit modulo `rho`, complete
additive orthogonality gives a residue-cell Gram.  An interval of length
`O(c)` contains at most `O(1+c/ell)` integers in one residue modulo `ell`, and
similarly on the other side.  Therefore

\[
\boxed{
 \sum_{h=0}^{\ell-1}
 \sum_{k=0}^{\rho-1}
 \|F_{h,k}\|^2
 \ll
 (\ell+c)(\rho+d)
 \sum_{P,Q}\|a_{P,Q}\|^2.
}
\tag{L-106124.2}
\]

The estimate is Hilbert-valued and stable under arbitrary coefficient deletion.
Because `ell<=c` and `rho<=d`,

\[
 \sum_{h\ne0,k\ne0}\|F_{h,k}\|^2
 \ll cd\sum_{P,Q}\|a_{P,Q}\|^2.
\tag{L-106124.3}
\]

## 2. Literal physical fibre

For the bilateral Boolean source,

\[
 a_{P,Q}
 ={\gamma_{P,Q}\over g^2cd\sqrt{PQ}},
 \qquad
 |\gamma_{P,Q}|\le X^{o(1)}.
\]

The semiprime reciprocal sums are polylogarithmic, so

\[
 \sum_{P,Q}\|a_{P,Q}\|^2
 \ll {X^{o(1)}\over g^4c^2d^2}.
\]

Hence

\[
\boxed{
 \sum_{h\ne0,k\ne0}\|F_{h,k}\|^2
 \ll {X^{o(1)}\over g^4cd}.
}
\tag{L-106124.4}
\]

After the local tensor source-dual weight is inserted, one fibre costs

\[
\boxed{
 g^2\ell\rho
 \sum_{h\ne0,k\ne0}\|F_{h,k}\|^2
 \ll {X^{o(1)}\over g^2}{\ell\rho\over cd}
 \le {X^{o(1)}\over g^2}.
}
\tag{L-106124.5}
\]

## 3. Exact limitation

Equations (L-106124.2)--(L-106124.5) are local in `(ell,rho,c,d)`.  The
bilateral moment is a positive sum over all least-prime conductor fibres.
`R-106123` gives the exact prime-core fixture showing that there may be
power-many fibres even when each one costs `O(1)`.

Therefore the theorem does not imply any of:

```text
near-prime global closure;
subpower sum over ell and rho;
BTPP106122, BTPN106122 or BTNN106122;
BCI102990;
RH.
```

The local theorem is nevertheless useful: every successful global family or
trace estimate needs only recover cancellation/orthogonality across the
varying conductor fibres.  All owner-product and fixed-core multiplicities
inside one fibre are already paid.

## Scope

This file is the corrected durable replacement for the local part of the first
`L-106123`.  The global statement in that file is retracted by `R-106123`.
