# R-97401 — PR #565 consumes two incompatible parent types at its first rough-child step

Claim ID: `R-97401`  
Status: **EXACT STATEMENT-TO-USE REFUTATION OF THE SOURCE INTERFACE**  
Created: 2026-08-18  
Frozen target: PR #565 at `339e3367660f40c74795802a6f8170b15e19b13a`  
Frozen predecessor: PR #556 `L-96602` at `a4feca0457d310c72054f274040f93b0503f658b`  
RH status: **unproved**

## 1. The preceding statement

For the positive annular source `h_X`, `L-96602` proves
\[
h_X-p^{-1/2}A_ph_{X/p}
\]
is literally the restriction to source indices not divisible by `p`.  The
child is removed in the **same source channel**.  This is why the difference is
a positive packet.

## 2. The statement consumed in PR #565

`L-97101` replaces the child by the parity swap `S A_pP_{x/p}` and calls
\[
C_{x,p}=P_x-p^{-1/2}SA_pP_{x/p}
\tag{R-97401.1}
\]
a “positive nondivisible current.”  It simultaneously assigns to `P_x` the
complete canonical `P_61` marginals
\[
m(P_x)=M(x),\qquad f(P_x)=F(x).
\tag{R-97401.2}
\]

These requirements are incompatible.

* If `P_x` is the canonical `P_61` packet of (R-97401.2), its `p`-divisible
  subpacket is in the same channel.  The positive restriction is the unswapped
  difference from `L-96602`, not (R-97401.1).
* If `P_x` already contains the complete future rough source with the actual
  Möbius parity, then its `p`-divisible subpacket is swapped and (R-97401.1) may
  be a restriction.  But its mass and scalar are no longer the finite `P_61`
  quantities `M(x),F(x)`, so `L-97400`/`L-97100` cannot be applied to it.

## 3. One-atom exact witness

Let the canonical parent contain one even atom `e` and let
\[
p^{-1/2}A_pP_{x/p}=(e,0).
\]
Then the true same-channel restriction is zero, whereas
\[
(e,0)-S(e,0)=(e,-e)
\]
has a negative odd coordinate and is not in the positive paired-source cone.

## 4. Root-marginal mismatch

For one rough prime, the actual finite Euler scalar is
\[
F(x)-p^{-1/2}F(x/p).
\tag{R-97401.3}
\]
The low-child recombination used in PR #565 is
\[
\lambda(P-rSP_y)+\alpha SP_y=\lambda P,
\qquad \alpha=\lambda r.
\tag{R-97401.4}
\]
Its child coefficient cancels to zero.  Thus (R-97401.4) returns the canonical
parent marginal rather than the rough Euler coefficient `-r` in (R-97401.3).

Therefore PR #565's contraction arithmetic does not establish that its
recursively defined packet is the actual annular scalar
\[
5[c_X(2)-c_{X/4}(2)]+3[c_X(3)-c_{X/4}(3)].
\]
The repaired finite bias of `L-97400` does not fix this source-type mismatch.
