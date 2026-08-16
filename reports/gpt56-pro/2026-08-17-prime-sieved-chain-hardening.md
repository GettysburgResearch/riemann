# Prime-sieved chain hardening: exact transport failures and the two-row Riesz frontier

Date: 2026-08-17  
Repository: `gfreund123/riemann`  
Base consumer: PR #542 at `ca5fb69c15cda29b3b589660f9be44ea2f440677`  
Compared packets: PR #537 at `2c2d4dd834ee61c54a6f8bdd7ba204a01896d593`; PR #548 at `7c7677e3dda318f8f8ccb813c4ca38f14448a538`; PR #549 at `4ef69785b84b3801627956c3f0c9cf0ce56299aa`  
Status: research hardening; RH unproved

## Executive result

The original finite-prime `FRONTIER-CHAIN` does require cross-product
transport.  A fixed-product cube can leave a negative coefficient at one knot,
so the submitted local convex-packet proof is invalid.

The later global-shadow attempts recognize that issue but do not close it.
Their positive bulk store is the \(P\)-rough term
\(C_j{\bf1}_{(n,P)=1}\), while the capacity proof sums every integer in a
multiplicative block.  The exact block \(P=30,[2,10)\) exposes a factor larger
than four between the claimed lower bound and the actual rough mass.

The direct fixed-row Mellin--Landau consumer from PR #542 survives and can be
sharpened: only rows \(2\) and \(3\) are needed, and their cancellation
numerators have no common zero in \(\Re z>0\).

The strongest honest successor is therefore the exact two-row criterion
`TRP23`, not another unverified reservoir theorem.

## Durable mathematics

1. Exact full-row coefficient dictionaries for rows \(2,3\).
2. Exact formulas in one universal Möbius Riesz state \(F(x)\).
3. Reduction of all real endpoints to integer knots.
4. Exact two-state recurrence for each row.
5. Exact two-row Mellin transform and noncancellation.
6. Eventual positivity of the two rows implies RH.

## What failed

### Fixed product

At \(j=3,P=6,n=24\), the same-knot residue is \(-1\).  No three-knot
butterfly can be made without mixing products.

### Global rough block

At \(P=30,p=5,u=2\), the declared rough block contains only \(7\):
\[
\sum_{\substack{2\le m<10\\(m,30)=1}}m^{-1/2}=7^{-1/2}<1/2,
\]
whereas the all-integer surrogate used by the proof is bounded below by
\(\sqrt2\log5>2\).

These are exact proof refutations, not numerical suspicions.

## Direct consumer and normalization

PR #541 correctly refuted the old native endpoint identification
\[
\langle Y_4,\Omega-\Xi\rangle=J_\Lambda-\mathcal H.
\]
The direct fixed-row consumer does not use that identity.  It uses the
reciprocal-zeta Mellin transform of each component row, so the normalization
correction is fully respected.

## First open theorem

\[
\boxed{
c_N(2)\ge0,\qquad c_N(3)\ge0
\quad\text{for every sufficiently large integer }N.
}
\]

This is `TRP23`.  The exact scalar forms and recurrence are in `L-96400`.
A proof would complete the direct Mellin--Landau route.  The present packet
does not claim that proof.

## Computational boundary

The retained checker performs only:

* exact rational coefficient and convolution identities;
* the two proof-scope counterexamples;
* exact rows-\(2,3\) cancellation algebra;
* small deterministic diagnostic scans.

It does not rerun a large prime scan and does not infer an infinite theorem
from diagnostics.
