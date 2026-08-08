# L-23812 — Mixed one-third/half Pascal renewal producer

Claim ID: `L-23812`  
Title: One fixed rational balanced branching law reduces BCT to positivity of a single descending renewal sequence  
Status: **PROPOSED FULL-PROOF PRODUCER — GLOBAL SIGN OPEN**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23810`, `L-23809`  
Scope: explicit source-specific producer; finite reconnaissance is not proof

## 1. Fixed branching law

For every integer `n>=2`, put

\[
 j_3(n)=\max(1,\lfloor n/3\rfloor),
 \qquad
 j_2(n)=\lfloor n/2\rfloor.
 \tag{L-23812.1}
\]

Define a probability law on split rows by

\[
 \boxed{
 \pi_n
 =\frac{31}{32}\,\delta_{j_3(n)}
 +\frac1{32}\,\delta_{j_2(n)}.}
 \tag{L-23812.2}
\]

If the two children coincide, their weights are combined. Every retained split
is `1/5`-balanced:

\[
 \frac n5\le j\le\frac{4n}{5}.
 \tag{L-23812.3}
\]

The small rational halving component is not fitted into any theorem below; it
is part of the frozen producer submitted for review.

## 2. Critical target divergence

For

\[
 w_X(q)=q^{-1/2}\log(X/q),
 \qquad2\le q\le X,
 \tag{L-23812.4}
\]

define

\[
 U_X(m)=\sum_{k\le X/m}\mu(k)w_X(mk),
 \qquad
 R_X(m)=U_X(m)-U_X(m+1).
 \tag{L-23812.5}
\]

These are exact finite sums.

## 3. Descending renewal

Starting from `n=X` and descending to `2`, define

\[
 \boxed{
 d_X(n)=R_X(n)+
 \sum_{m=n+1}^{X}d_X(m)
 \bigl[\pi_m(n)+\pi_m(m-n)\bigr].}
 \tag{L-23812.6}
\]

Equivalently, the explicit parent recurrence is the sum of the following
channels.

For the one-third branch, a node `n` receives from all parents `m` satisfying

\[
 \lfloor m/3\rfloor=n
 \quad\text{or}\quad
 m-\lfloor m/3\rfloor=n.
 \tag{L-23812.7}
\]

For the halving branch, it receives from parents whose floor or ceiling half is
`n`. All multiplicities are retained, including the doubled central child.

Set

\[
 d_X(n,j)=d_X(n)\pi_n(j).
 \tag{L-23812.8}
\]

By `L-23810`, the recurrence gives identically

\[
 \partial d_X=R_X.
 \tag{L-23812.9}
\]

Hence, without approximation,

\[
 \boxed{
 \sum_{n,j}d_X(n,j)\chi_{n,j}(q)=w_X(q)
 \qquad(2\le q\le X).}
 \tag{L-23812.10}
\]

The only question is the sign of the scalar coefficients `d_X(n)`.

## 4. Mixed Pascal renewal theorem

The proposed theorem, abbreviated `MPR`, is

\[
 \boxed{
 d_X(n)\ge0
 \qquad
 (X\ge3,\ 2\le n\le X).}
 \tag{L-23812.11}
\]

Under MPR, (L-23812.8)--(L-23812.10) give a zero-slack BCT certificate in a
fixed `1/5`-balanced menu. Therefore `L-23809` yields

\[
 \sum_{p^a\le X}\frac{\Lambda(p^a)}{\sqrt{p^a}}
 \log\frac X{p^a}
 \ge4\sqrt X-O((\log X)^2),
 \tag{L-23812.12}
\]

and the square-screw/Landau transfer gives RH.

Thus MPR is a complete, explicit, finite-sign replacement for the general BCT
existence theorem.

## 5. Why both branches are retained

The two pure deterministic producers do not support a valid general proof.
Direct descending reconstruction finds negative coefficients for:

- pure halving at moderate endpoints;
- pure one-third splitting at substantially larger endpoints.

The failures are recorded as route-scope evidence in `R-23803`. The fixed mixed
law is therefore not a cosmetic averaging of two independently positive
solutions.

The small halving channel repairs a low-scale resonance of the one-third
renewal while retaining a dominant fixed-ratio `2/3` geometry. That same ratio
is the first Farey/Mertens firewall elsewhere in the repository, so a valid
proof of MPR must retain its coherent Möbius sign.

## 6. Quotient-layer structure

For fixed `Y=X/n`, the source term `R_X(n)` involves only

\[
 \mu(k),\qquad k\le Y.
 \tag{L-23812.13}
\]

Every incoming parent in (L-23812.6) has larger size and therefore a strictly
smaller quotient `X/m`. MPR is consequently a genuine quotient-layer induction:
new Möbius information enters only when `Y` crosses an integer, while all
renewal inputs have already been constructed on earlier layers.

This is a much smaller review target than arbitrary BCT. A production proof may
use:

1. a direct invariant for the quotient-layer reserve;
2. a finite-state `2`--`3` renewal cone;
3. Pascal four-cycle repair of each downward knot;
4. a reflected Selberg square specialized to the single renewal;
5. a source-specific high-order Euler estimate followed by an exact finite
   inner-layer induction.

## 7. Reconnaissance boundary

The branch contains two kinds of finite evidence.

1. A directed high-precision checker certifies the frozen recurrence through a
   modest finite endpoint.
2. A standard-library large scanner observes no negative coefficient at the
   endpoints
   \[
   10^6,\ 5\cdot10^6,\ 10^7,\ 2\cdot10^7,\ 5\cdot10^7,\ 10^8.
   \]

These computations are reconnaissance only. They do not prove (L-23812.11), do
not establish a cofinal rate, and must not be cited as RH evidence beyond the
finite tested levels.

## 8. Review firewall

A reviewer should attack MPR in this order.

1. Reconstruct the multiple-Möbius divergence `R_X`.
2. Verify every parent multiplicity in (L-23812.6).
3. Confirm the exact saturation identity (L-23812.10).
4. Search quotient-layer knots for a negative coefficient.
5. Require a symbolic reserve invariant; finite scans are insufficient.
6. Mutate the fixed `31/32,1/32` weights and the first fixed-ratio Mertens cell.
7. Reject any proof taking absolute values before the one-third and halving
   channels are recombined.

## 9. Proof boundary

Closed exactly:

- the fixed balanced branching law;
- the descending recurrence;
- exact zero-slack saturation conditional only on coefficient sign;
- MPR implies BCT and the full RH deduction.

Open and load bearing:

- MPR, equation (L-23812.11).

Accordingly this is a concrete full-proof producer, not a completed proof of
RH.
