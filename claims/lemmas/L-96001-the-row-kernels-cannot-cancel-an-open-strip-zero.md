# L-96001 — No open-strip zeta zero is cancelled by all component-row Mellin kernels

Claim ID: `L-96001`  
Status: **PROPOSED COMPLETE ANALYTIC NONCANCELLATION LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-96000`  
RH status: **not assumed**

Let

\[
 P_j(z)=A_jj^{-z}-B_j(j+1)^{-z}-C_j\sum_{m=1}^{j+1}m^{-z},
\]

with the coefficients of `L-96000`.

## 1. Asymptotic at a zeta zero

Fix `z` with `0<Re(z)<1`, `z!=1`, and suppose `zeta(z)=0`. Euler--Maclaurin gives

\[
 \sum_{m=1}^{j+1}m^{-z}
 =\frac{(j+1)^{1-z}}{1-z}+\frac12(j+1)^{-z}+O_z(j^{-\Re z-1}).
\tag{L-96001.1}
\]

Using

\[
 A_j=1+\frac2{j-1},\qquad B_j=1-C_j,\qquad C_j=\frac2{j(j-1)},
\]

and expanding the two neighboring powers yields

\[
 \boxed{
 P_j(z)=-\frac{z(z+1)}{1-z}\,j^{-z-1}+O_z(j^{-\Re z-2}).
 }
\tag{L-96001.2}
\]

The leading coefficient is nonzero for every nontrivial zeta zero, because such a zero is not `0`, `-1`, or `1`.

## 2. Consequence

There exists `J(z)` such that

\[
 \boxed{P_j(z)\ne0\qquad(j\ge J(z)).}
\tag{L-96001.3}
\]

Thus every nontrivial open-strip zero survives in the Mellin transform of every sufficiently large fixed component row.

## 3. Multiplicity

If `z` is a zero of multiplicity `m`, then `1/zeta(s+1/2)` has a pole of order `m` at `s=z-1/2`. For any `j>=J(z)`, (L-96001.3) leaves that pole nonremovable.

## 4. Review firewall

The proof does not assume a uniform effective bound for `J(z)`. Landau's argument needs only one fixed row after a hypothetical zero has been chosen. No zero-density estimate, zero-free strip, Mertens bound, or RH-strength prime estimate enters.

```text
finite cancellation polynomial          explicit
large-j leading coefficient             nonzero
effective uniform j                      not required
off-line zero survives some fixed row    proved
```
