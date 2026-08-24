# T-102850 — Only four-distinct-owner dispersion remains direct

Claim ID: `T-102850`  
Status: **MAJOR UNCONDITIONAL RENEWAL REDUCTION; RH UNPROVED**  
Created: 2026-08-24  
Base: PR #719  
RH status: **unproved**

`T-102840` reduced the physical restriction to nonzero additive-phase sectors
owned by the largest discrepancy prime. `L-102837` now removes every sector in
which the two semiprime owner pairs share one physical prime.

## 1. Shared owners are recursive, not terminal

If two owner pairs share their greatest prime `p`, both physical fields contain
`p^{-1/2}U_p`. Factoring it contributes `1/p` to the Gram form and leaves the
same defect problem on primes strictly below `p` and at scale `Y/p`.

The endpoint radial gauge is sublinear, so the full shared-owner contribution
obeys a decreasing-prime renewal. Its complete path mass is

\[
\prod_{p\le Y}(1+C/p)\ll_C(\log(2Y))^C.
\]

Hence a subpower estimate for the disjoint-pair sectors automatically gives a
subpower estimate for every shared-owner sector.

## 2. Four-distinct-owner normal form

The direct hard sector may be restricted to

\[
P=\{p,q\},
\qquad
Q=\{r,s\},
\qquad
|P\cup Q|=4.
\]

After cofactor completion, its physical products are

\[
N=pq\,a^2,
\qquad
M=rs\,b^2,
\]

with all four owners distinct and all core primes below the corresponding
second owner.

The largest discrepancy prime is simply the largest of the four owners. It
divides exactly one physical product and is absent from the other. Therefore
the zero-free additive-phase identity of `L-102835` applies without a shared
factor.

## 3. Exact final theorem

Define

```text
4QDSP102850:
  after exact carrier, source-region and gauge recombination, the coherent
  nonzero additive-phase sum over four-distinct-owner semiprime squareclasses
  has subpower logarithmic negative mass in the fixed ratio-eight outer
  observation.
```

Then

\[
\boxed{
\mathrm{4QDSP}_{102850}
\Longrightarrow
\mathrm{QDSP}_{102840}
\Longrightarrow
\mathrm{DPWNC}_{102749}
\Longrightarrow
\mathrm{OER}_{102780}
\Longrightarrow
\mathrm{RH}.
}
\]

All two-pair intersections of size one are absorbed by the renewal; equal pairs
and repeated physical-prime pairs were already closed.

## Exact boundary

```text
shared-largest-owner factorization       PROVED EXACT
shared-owner decreasing-prime renewal    PROVED POLYLOG
four-distinct-owner additive phases      CONSTRUCTED EXACTLY
four-owner coherent dispersion           OPEN / RH-BEARING
Riemann Hypothesis                       UNPROVED
```