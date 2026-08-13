# T-91405 — Same-endpoint projection of every unmatched branch gives a tail-index-preserving factor-54 resolution proposal

Claim ID: `T-91405`  
Status: **PROPOSED COMPLETE RH COMPOSITION — INDEPENDENT ADVERSARIAL REVIEW REQUIRED**  
Created: 2026-08-13  
Depends on: finite root entry `L-91413/L-91414`; exact least-prime partition `L-91335/L-91336`; common child extraction `L-91410/L-91411`; same-endpoint physical projection `L-91415/L-91416`; packet cone `L-91412`; packet envelope `L-91406/T-91401`; endpoint-score RH criterion  
Mandatory firewalls: `R-91102`, `R-91303`–`R-91310`, `R-91401`–`R-91404`  
RH status: **proposed, not established**

## 1. Root entry

Use the fixed small-prime forcing exactly once. `L-91413/L-91414` place it in
the canonical positive packet cone and identify its two diagonal coordinates
with the actual rough renewal kernels `m^-1` and `m^-1/2`.

All later packets retain their tail-prime indices. No excluded prime is ever
reintroduced.

## 2. Exact branch partition

At one source point, let `Q_infty` and `H_j` be the exact survival and
least-prime branch matrices. Put

\[
\alpha_j=\min(h_j^X,h_j^Y).
\]

Decompose each actual branch at its child endpoint as

\[
H_jIu=\alpha_jIu+(H_j-\alpha_jI_4)Iu.
\tag{T-91405.1
}

The first term is the canonical recursive child. The second term stays at that
same child endpoint and is current-generation material. The survival packet
stays at the parent endpoint.

All packets in (T-91405.1) are positive in the hidden coordinates, and

\[
\sum_j\alpha_j\le1.
\tag{T-91405.2
}

## 3. Positive realization of all nonrecursive packets

Apply `L-91415` separately:

- to `Q_infty Iu` at the parent endpoint;
- to `(H_j-alpha_j I_4)Iu` at the exact endpoint `X/p_j`.

Every output is a positive physical `(L,R)` packet with exact target. Its score
deficit is bounded by its positive `X^-` mass, and its physical mass is bounded
by the original hidden mass. `L-91416` gives the direct nonnegative component
rows for those positive equality/reserve measures.

The canonical recursive child `alpha_j Iu` requires no projection and retains
the tail index `j+1`.

Thus no unmatched mode mass is moved between endpoints, and the PR #431 branch
counterexample is respected rather than denied.

## 4. Target, row and mass decomposition

Let `P_current` denote the sum of the projected survival packet and all projected
branch excesses. Let `P_j` be the canonical recursive children.

The source and target measures decompose exactly. Every current row is
nonnegative, and child row packets use the exact affine pushforward. The score
need not decompose exactly because `L-91415` clips an out-of-cone score; its
complete shortfall is instead charged to the local debt.

For the additive hidden/packet mass,

\[
\boxed{
\sum_jm(P_j)\le m(P),
}
\tag{T-91405.3
}

and the total local score deficit plus the fixed finite physical corrections is
at most

\[
\boxed{C_{\rm fin}m(P).}
\tag{T-91405.4
}

Every child endpoint satisfies

\[
X_j\le X/59<c_0X
\]

after the one-time finite root block.

## 5. Exact packet recurrence

Homogeneity and subadditivity of the packet deficit yield

\[
\boxed{
\Delta_X(P)
\le C_{\rm fin}m(P)+\sum_j\Delta_{X_j}(P_j).
}
\tag{T-91405.5
}

This recurrence uses actual restricted child packets. It contains neither an
undefined scalar `theta_j` nor a replacement of a child by a native packet.

Applying `T-91401` gives

\[
\boxed{
\Lambda(X)=O(\log X)=o(\log^2X).
}
\tag{T-91405.6
}

## 6. RH endpoint

The native root packet has uniformly bounded normalized mass, and the resident
endpoint theorem bounds the RH-sensitive prime scalar by its packet deficit.
Equation (T-91405.6) would therefore imply RH.

## 7. Review-critical obligations

A complete proof review must still reconstruct:

1. the measure-level source interpretation of `L-91336`;
2. the exact target/row covariance when a canonical child is placed at `X/p_j`;
3. the equality/reserve row realization and the uniform finite debt constant in
   `L-91415/L-91416`;
4. one-use summation before quantization/collar/port charges;
5. the bounded root mass and exact sign of the endpoint-score RH criterion.

Until these are independently verified:

```text
PR #431 counterexamples                    VERIFIED
same-endpoint branch excess projection      PROVED EXACT
canonical child mass ledger                 PROVED EXACT
packet recurrence                           PROVED ABSTRACTLY
finite physical producer interfaces         REVIEW REQUIRED
full RH composition                         PROPOSED / NOT VERIFIED
Riemann Hypothesis                          UNPROVED
```
