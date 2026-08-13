# T-91404 — Tail-index-preserving canonical regeneration restores a packet-valued factor-54 resolution proposal

Claim ID: `T-91404`  
Status: **PROPOSED COMPLETE RH COMPOSITION — INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-13  
Depends on: finite positive entry `L-91113/L-91340/L-91341`; hidden lift and exact branch partition `L-91335/L-91336`; aggregate regeneration `L-91410`; positive packet cone `L-91343`; packet deficit `L-91406/T-91401`; finite producer and endpoint-score RH consumer  
Mandatory firewalls: `R-91102`, `R-91303`–`R-91310`, `R-91401`–`R-91403`  
RH status: **proposed, not established**

## 1. Why this proposal is different

The construction does not:

```text
use historical L-91350.2 or X-91127;
identify one mode-dependent branch with an r-scaled child;
replace a restricted packet by a scalar copy of a native packet;
reintroduce P_53 or P_61 on a tail child;
or require a Hall selector to commute with the prime tree.
```

The prime-tail index remains part of every child state.

## 2. Entry into the canonical positive packet cone

After the fixed finite small-prime block is absorbed, the resident finite
producer supplies a canonical positive `(L,R)` packet. Its target, endpoint
score and every exact component row are represented in one positive packet
cone. The normalized root mass is uniformly bounded on the fixed reset window.

This entry theorem is used only at the root of the arithmetic construction. It
is not reapplied to a tail child.

## 3. Exact tail-index reset

At one source point of a canonical positive packet, use the exact least-prime
survival and branch coefficients for the currently admissible tail primes.
Apply `L-91410` pointwise.

If

\[
 \alpha_j=\min(h_j^X,h_j^Y),
 \qquad
 \Theta=\sum_j\alpha_j,
\]

then the parent canonical packet decomposes exactly as

\[
 \boxed{
 P=P_{\rm current}+\sum_jP_j,
 }
\tag{T-91404.1}
\]

where

\[
 P_{\rm current}=(1-\Theta)P,
 \qquad
 P_j=\alpha_jP
\]

before the exact child affine pushforward. The child `P_j` is placed at its
actual endpoint `X/p_j` and carries the next admissible prime index.

The equality is pointwise in the positive source measure. Hence

\[
 \boxed{
 m(P_{\rm current})+\sum_jm(P_j)=m(P).
 }
\tag{T-91404.2
}

Every child endpoint satisfies

\[
 X/p_j\le X/59<c_0X
\]

after the finite root block.

## 4. Current packet

The current packet is a positive restriction of a canonical positive packet.
The positive packet cone is closed under restriction, addition, row evaluation,
ordinary/radix-four response and the one-use endpoint quantizer.

Therefore the current packet has a capacity-faithful realization with local
debt

\[
 \boxed{
 \Delta_X(P_{\rm current})
 \le C_{\rm fin}\,m(P_{\rm current}),
 }
\tag{T-91404.3
}

where `C_fin` is the fixed finite-window collar, omission and endpoint-port
constant. No mode-dependent hidden remainder requires separate physical typing:
`L-91410` proves that the aggregate remainder is canonical exactly.

## 5. Child packets

Each child is an actual positive restricted packet, not a preferred normalized
shape. Feasible child packings are pushed to the parent coordinate by the exact
affine covariance and summed before the single quantization/collar operation.

The child packets retain their tail-prime indices. The same pointwise
regeneration is applied recursively using only primes still admissible in that
child. Thus the reset never reintroduces an excluded prime.

## 6. Packet-valued recurrence

Subadditivity of the exact packet deficit gives

\[
 \boxed{
 \Delta_X(P)
 \le C_{\rm fin}m(P)+\sum_j\Delta_{X/p_j}(P_j).
 }
\tag{T-91404.4
}

Together with (T-91404.2), this is precisely the producer hypothesis of the
packet-envelope consumer `T-91401` with contraction `c=1/59`.

Consequently the worst normalized packet loss satisfies

\[
 \Lambda(X)\le C_{\rm fin}+\Lambda(X/59+C_0)
\]

and therefore

\[
 \boxed{
 \Lambda(X)=O(\log X)=o(\log^2X).
 }
\tag{T-91404.5
}

## 7. RH endpoint

The normalized native root packet has bounded mass, and the resident endpoint
criterion bounds the RH-sensitive prime scalar by its endpoint packet deficit.
Equation (T-91404.5) therefore supplies the required `o(log^2 X)` bound and
would imply RH.

## 8. Adversarial reconstruction obligations

The proposal is complete only if a reviewer verifies at one frozen commit:

1. the finite small-prime entry really yields the canonical positive packet
   cone used in Section 2;
2. `L-91336` is a source-measure partition, not merely a scalar state identity;
3. the child affine pushforward preserves the exact packet target, score and
   row coordinates;
4. positive restrictions have the uniform local-debt bound (T-91404.3);
5. all current and child measures are summed before collar, omission and port
   costs are charged;
6. the mass in (T-91404.2) is exactly the bounded normalization used by
   `T-91401` and by the root endpoint criterion;
7. the endpoint-score-to-RH implication has the stated sign.

Until those interfaces are independently reconstructed:

```text
PR #431 counterexamples                    VERIFIED / FENCED
aggregate canonical regeneration           PROVED EXACT
prime-tail index retention                 PROVED EXACT
packet-valued recurrence                    PROVED ABSTRACTLY
finite positive entry and local debt        RESIDENT / REVIEW REQUIRED
full RH composition                         PROPOSED / NOT VERIFIED
Riemann Hypothesis                          UNPROVED
```
