# L-23703 — Bounded contagion rank implies the balanced Type-II recurrence

Claim ID: `L-23703`  
Title: A complete four-way contagion decomposition with absolute resonance rank `C_0` gives `BTP(K)` with coefficient exponent `C_0/K`  
Status: **PROPOSED EXACT COMPOSITION LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #237  
Dependencies: `L-23701`, `L-23702`; terminal Euler closure and fixed-reserve scale recurrence from PRs #158/#233/#235

## 1. Hypotheses

Fix `K` and one balanced source packet.  Assume a complete `BCT(K)` certificate
partitions its Hermitian local Gram into pieces of the four classes of
`L-23702`.

Assume:

1. exact-collision pieces contribute their already-recombined Bohr diagonal;
2. every free-lattice piece has energy `exp(-cJ+o_K(J))` for some fixed `c>0`;
3. every strict-scale piece is bounded by a declared auxiliary energy at scale
   at most `(1-delta)J+O_K(1)`;
4. every resonance face has rank at most `C_0`, independent of `K`;
5. after its `C_0` free coordinates are fixed, its source contraction is bounded
   by one declared lower-scale auxiliary energy with coefficient
   `exp(o_K(J))`;
6. the number of face types and all fixed-order divisor multiplicities are
   `exp(o_K(J))`.

The coefficient estimates are applied only after exact signed product
recombination.

## 2. Resonance enumeration

Each free coordinate of a rank-`r` face ranges over at most

\[
 \exp\{J/K+o_K(J)\}
\]

source values.  Hence the number of assignments on that face is at most

\[
 \exp\{(r/K+o_K(1))J\}.
 \tag{L-23703.1}
\]

For `r<=C_0`, summing the fixed-coordinate contractions gives

\[
 E_{\rm face}(J)
 \le
 \exp\{(C_0/K+o_K(1))J\}
 \left[
  1+
  \max_\upsilon
  \max_{u\le(1-\delta)J+O_K(1)}E_{K,\upsilon}(u)
 \right].
 \tag{L-23703.2}
\]

No arbitrary-vector operator norm is used; the enumeration is over the actual
source coordinates retained by the certificate.

## 3. Complete packet estimate

The exact collision, Euler, and lower-scale classes are absorbed into the same
right-hand side.  The finite number of classes and packet types contributes only
`exp(o_K(J))`.  Therefore every balanced type satisfies

\[
 \boxed{
 E_{K,\tau}(J)
 \le
 \exp\{(\varepsilon_K+o_K(1))J\}
 \left[
  1+
  \max_\upsilon
  \max_{u\le(1-\delta)J+O_K(1)}E_{K,\upsilon}(u)
 \right],}
 \tag{L-23703.3}
\]

with

\[
 \boxed{
 \varepsilon_K={C_0\over K}.}
 \tag{L-23703.4}
\]

This is the linear balanced Type-II theorem `BTP(K)`.

A tensor certificate is also allowed, but then the exact weighted scale sum must
remain strictly below one.  The bounded-rank enumeration factor is still
`C_0/K` and cannot repair a critical tensor weight equal to one.

## 4. Increasing order

Because `C_0` is absolute,

\[
 \varepsilon_K\longrightarrow0.
 \tag{L-23703.5}
\]

For a fixed scale reserve `delta>0`, the scale-contraction theorem gives

\[
 2\Theta_\zeta
 \le {C_0\over K\delta}.
 \tag{L-23703.6}
\]

Letting `K` tend to infinity forces

\[
 \Theta_\zeta=0.
\]

The result does not use a growing-order window at one physical scale.  For each
fixed `K`, the limit `J->infinity` is taken first, so the pole-sensitivity
barrier for `K=K(J)` is not invoked.

## 5. Why this is not endpoint counting by assertion

Equation (L-23703.4) follows only after a `BCT(K)` object has proved that every
same-scale balanced face either propagates or has rank at most `C_0`.  Merely
listing terminal faces, or invoking finite complexity induction, does not
satisfy the hypothesis.

The rank theorem must apply to the balanced source itself and must survive the
first-cell/Mertens firewall.  A single `Omega(K)`-rank face returns
`epsilon_K=Omega(1)` and blocks the RH conclusion.

## 6. Proof boundary

The counting and scale-contraction composition are exact under the stated
source-specific hypotheses.  The missing theorem is precisely `BCT(K)` of
`L-23702`, including the absolute rank bound.
