# L-91688 — Rough-prime deletion gives an exact first-owner reservoir partition

Claim ID: `L-91688`  
Status: **PROVED EXACT SOURCE/COORDINATE ALGEBRA — POSITIVE NATIVE THINNING REMAINS OPEN**  
Created: 2026-08-14  
Frozen parent: PR #470 at `89af3206ea1894884613e1188b5ab9a6a4cd74f0`  
Primary input: `L-91379`  
RH status: **unproved**

## 1. Canonical rough lift

Let

\[
 P=P_{61},\qquad
 \mathcal R=\{m\ge1:P^-(m)\ge67\},
\]

and let `N_X` denote any native endpoint datum whose ordinary, radix-four,
score, row and boundary coordinates are linear under same-index multiplicative
placement. Its canonical finite-Euler rough lift is

\[
 \boxed{
 \mathfrak D_X
 =\sum_{m\in\mathcal R}m^{-1/2}N_{X/m},
 }
 \tag{L-91688.1}
\]

with causal zero extension in every coordinate. For the component row this is
exactly `L-91379.2`; the corresponding response and score identities are
`L-91379.3--.5`.

For a rough prime `p`, define

\[
 (A_pF)_X=p^{-1/2}F_{X/p},
 \qquad
 \Pi_p=I-A_p.
 \tag{L-91688.2}
\]

## 2. One prime deletes exactly its divisible reservoir

Reindexing `m=pu` gives

\[
 A_p\mathfrak D_X
 =\sum_{\substack{m\in\mathcal R\\p\mid m}}
  m^{-1/2}N_{X/m}.
 \tag{L-91688.3}
\]

Consequently

\[
 \boxed{
 \Pi_p\mathfrak D_X
 =\sum_{\substack{m\in\mathcal R\\p\nmid m}}
  m^{-1/2}N_{X/m}.
 }
 \tag{L-91688.4}
\]

This is an identity in the labelled source space and hence in every linear
physical coordinate. No sign of the native summands is asserted.

For a terminal leaf `X=py`, equation (L-91688.4) specializes to the Hall-free
raw residual of `L-91685`:

\[
 D_{P,py}-p^{-1/2}D_{P,y}
 =\sum_{p\nmid m}m^{-1/2}c_{py/m}.
 \tag{L-91688.5}
\]

Thus the raw residual is literally the `p`-free rough slice, while the exact
child is the `p`-divisible slice.

## 3. Ordered finite deletion

Let `p_1,...,p_k` be distinct rough primes and put

\[
 F_0=\mathfrak D_X,
 \qquad
 F_i=\Pi_{p_i}F_{i-1},
 \qquad
 C_i=A_{p_i}F_{i-1}.
 \tag{L-91688.6}
\]

Induction using (L-91688.3) proves

\[
 \boxed{
 F_i
 =\sum_{\substack{m\in\mathcal R\\
 p_h\nmid m\;(1\le h\le i)}}
 m^{-1/2}N_{X/m},
 }
 \tag{L-91688.7}
\]

and

\[
 \boxed{
 C_i
 =\sum_{\substack{m\in\mathcal R\\
 p_h\nmid m\;(h<i),\ p_i\mid m}}
 m^{-1/2}N_{X/m}.
 }
 \tag{L-91688.8}
\]

The supports in (L-91688.7)--(L-91688.8) are pairwise disjoint. Telescoping
`F_(i-1)=F_i+C_i` gives

\[
 \boxed{
 \mathfrak D_X=F_k+\sum_{i=1}^kC_i.
 }
 \tag{L-91688.9}
\]

Every rough monomial is owned exactly once: by the first listed prime dividing
it, or by the residual if no listed prime divides it.

If the list contains every rough prime which can occur on the finite support of
the coordinate being tested, then only `m=1` remains and

\[
 \boxed{
 F_k=N_X,
 \qquad
 \mathfrak D_X=N_X+\sum_iC_i.
 }
 \tag{L-91688.10}
\]

This recovers the native datum and partitions the complete rough reservoir
without duplicating one atom or one physical column.

## 4. Exact consequence for SONTR

PR #470 proves that the unthinned raw current is natively infeasible on an
unbounded family. The present theorem does not contradict that separator.
Instead it identifies the exact source variable on which thinning must act:

```text
native m=1 slice;
first-owner rough slices C_i;
no unlabelled or duplicated reservoir remainder.
```

Therefore the source-owned native thinning theorem may be formulated without
an existential provenance search. It must choose, inside the explicit
first-owner slices, how much is current, how much is recursive, and how the
zero-cost `Y_4` repair cone is used. Its remaining obligations are positivity,
subcritical recursive mass, native capacity and bounded weighted slack.

## 5. Verification and boundary

`X-91688` checks the deletion and first-owner identities coefficientwise on an
exact three-prime exponent box. The proof above is general and does not depend
on that finite regression.

```text
rough-reservoir source ownership             CLOSED EXACTLY
arbitrary ordered first-owner partition      CLOSED EXACTLY
ordinary/detail/score coordinate identities  CLOSED BY LINEARITY
positive current after thinning              OPEN / SONTR
recursive coefficient mass <1/8              OPEN IN THIS ROUTE
native one-use capacity and Y4 slack          OPEN / NRCT
Riemann Hypothesis                            UNPROVEN
```
