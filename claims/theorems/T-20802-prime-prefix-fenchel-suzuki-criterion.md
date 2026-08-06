# T-20802 — Prime-prefix Fenchel–Suzuki criterion

Claim ID: `T-20802`  
Title: The global zeta-screw minimum is exactly the infimum of one convex Fenchel barrier over prime-power prefixes  
Status: `PROPOSED — COMPLETE EQUIVALENCE; COFINAL PRIME-MOMENT INEQUALITY OPEN`  
Authoring agent: `gpt56-03-u`  
Created: 2026-08-07  
Dependencies: `D-9501`; `L-9503`; Suzuki's pointwise screw criterion for RH  
Scope: a direct full-problem reduction with no matrix, zero census, support mesh, or asymptotic interpolation  
Related counterexample candidates: none

## 1. Prime-power data and smooth term

List the prime powers in strictly increasing order,

\[
 2=q_1<q_2<\cdots,
 \qquad
 \tau_j=\log q_j,
 \qquad
 w_j={\Lambda(q_j)\over\sqrt{q_j}}>0.
 \tag{T-20802.1}
\]

Use the exact normalization of `D-9501`.  Write the screw function on the
positive half-line as

\[
 \boxed{
 \Psi(t)=A(t)-\sum_{\tau_r\le t}w_r(t-\tau_r),
 }
 \tag{T-20802.2}
\]

where `A` is the complete pole/gamma/trivial-zero term from `L-9503`.  Put

\[
 \tau_1=\log2,
 \qquad
 P_j=\sum_{r\le j}w_r,
 \qquad
 Q_j=\sum_{r\le j}w_r\tau_r,
 \tag{T-20802.3}
\]

with `P_0=Q_0=0`.

By `L-9503`,

\[
 A''(t)>0\qquad(t\ge\tau_1).
 \tag{T-20802.4}
\]

Define the constrained convex conjugate

\[
 \boxed{
 A_+^*(p)=\sup_{t\ge\tau_1}\{pt-A(t)\},
 \qquad p\ge0,
 }
 \tag{T-20802.5}
\]

and the prime-prefix Fenchel margins

\[
 \boxed{
 M_j=Q_j-A_+^*(P_j),
 \qquad j\ge0.
 }
 \tag{T-20802.6}
\]

Finally let

\[
 m_{\rm init}=\inf_{0\le t\le\tau_1}A(t).
 \tag{T-20802.7}
\]

This is one fixed compact archimedean gate, independent of all primes beyond
`2`.

## 2. Exact global-minimum identity

One has the exact equality

\[
 \boxed{
 \inf_{t\ge0}\Psi(t)
 =\min\left\{
 m_{\rm init},
 \inf_{j\ge0}M_j
 \right\}.
 }
 \tag{T-20802.8}
\]

Consequently Suzuki's pointwise criterion gives

\[
 \boxed{
 \mathrm{RH}
 \iff
 m_{\rm init}\ge0
 \ \text{and}\ 
 M_j\ge0\quad\text{for every }j\ge0.
 }
 \tag{T-20802.9}
\]

Equivalently, after the one fixed initial gate is closed,

\[
 \boxed{
 \mathrm{RH}
 \iff
 Q_j\ge A_+^*(P_j)
 \quad\text{for every prime-power prefix }j.
 }
 \tag{T-20802.10}
\]

A single directed strict inequality

\[
 Q_j<A_+^*(P_j)
 \tag{T-20802.11}
\]

is therefore a finite unconditional RH-disproof witness, subject only to the
`D-9501` source-normalization audit and independent reproduction of the finite
prime-power and archimedean intervals.

## 3. Proof

For each `j>=0`, define the complete affine prefix extension

\[
 F_j(t)=A(t)-P_jt+Q_j
       =A(t)-\sum_{r\le j}w_r(t-\tau_r),
 \qquad t\ge\tau_1.
 \tag{T-20802.12}
\]

Let `N(t)` be the number of prime powers with `tau_r<=t`.  Then

\[
 F_{N(t)}(t)=\Psi(t).
 \tag{T-20802.13}
\]

More strongly, every other prefix lies above the actual screw value.  If
`j<N(t)`, then

\[
 F_j(t)-\Psi(t)
 =\sum_{j<r\le N(t)}w_r(t-\tau_r)\ge0.
 \tag{T-20802.14}
\]

If `j>N(t)`, then

\[
 F_j(t)-\Psi(t)
 =\sum_{N(t)<r\le j}w_r(\tau_r-t)\ge0.
 \tag{T-20802.15}
\]

Thus

\[
 F_j(t)\ge\Psi(t)
 \qquad\text{for every }j,t.
 \tag{T-20802.16}
\]

It follows that

\[
 \inf_j\inf_{t\ge\tau_1}F_j(t)
 \ge
 \inf_{t\ge\tau_1}\Psi(t).
 \tag{T-20802.17}
\]

Conversely, at every `t` the active prefix satisfies (T-20802.13), so

\[
 \inf_j\inf_{t\ge\tau_1}F_j(t)
 \le
 \inf_{t\ge\tau_1}\Psi(t).
 \tag{T-20802.18}
\]

Hence the two infima are equal.  By the definition of the constrained conjugate,

\[
 \inf_{t\ge\tau_1}F_j(t)
 =Q_j-\sup_{t\ge\tau_1}\{P_jt-A(t)\}
 =M_j.
 \tag{T-20802.19}
\]

Adding the compact interval `[0,tau_1]`, where no prime-power term has yet
entered, proves (T-20802.8).  The evenness of `Psi` and Suzuki's criterion now
prove (T-20802.9)--(T-20802.10).

If one `M_j` is negative, choose its unique constrained minimizer `t_j`.
Equation (T-20802.16) gives

\[
 \Psi(t_j)\le F_j(t_j)=M_j<0,
 \tag{T-20802.20}
\]

so this prefix is a genuine finite counterexample witness even when `t_j` lies
outside the deposition cell of `q_j`.  No cell-membership hypothesis is needed.
QED.

## 4. Why this is a full-problem reduction

The theorem removes all of the following from the logical frontier:

- interpolation between prime-power knots;
- a sampled support mesh;
- eigenvectors, matrices, and Schur complements;
- certified zero ordinates or a moving verified height;
- the need to guess which cell contains the global minimum.

The entire RH content is one scalar inequality for each finite pair of cumulative
prime moments `(P_j,Q_j)` against one fixed explicit convex function `A_+^*`.
The quantifiers are still cofinal: any finite positive scan, however long, is
not a proof of (T-20802.10).

## 5. Relation to existing global routes

- `T-19801/T-19804` sample or average the same `Psi`; (T-20802.8) instead computes
  its exact global infimum through prime prefixes.
- `T-15404` detects an off-line zero through one pole-annihilating Laplace
  window; the present theorem is the real-side convex-dual formulation.
- `L-19810/L-19811` isolate the same obstruction as a positive anti-causal
  strip energy.  A proof of (T-20802.10) would force that energy to vanish for
  every offset.
- `L-9503` supplied one convex minimization per physical cell.  The new prefix
  domination (T-20802.14)--(T-20802.16) is what permits all cells to be replaced
  by one discrete Fenchel sequence.

## 6. Proof-producing finite interface

For one prefix `j`, a directed certificate needs only:

1. the complete duplicate-free prime-power manifest through `q_j`;
2. directed intervals for `P_j` and `Q_j`;
3. a directed root or Fenchel certificate for the minimizer of
   `A(t)-P_jt` on `[log2,infinity)`;
4. one outward interval for `M_j`.

`L-20808` gives an exact Bregman/transport recurrence, and `L-20809` replaces the
implicit Fenchel barrier by an elementary entropy expression plus an explicit
`O(P_j^-5)` enclosure.

## 7. Proof boundary

- The global-infimum and Fenchel identities are exact.
- The initial compact gate is fixed and noncofinal; it should be closed once by
  directed interval arithmetic.
- No proof that every `M_j` is nonnegative is supplied here.
- Therefore this theorem is a direct full-RH attack surface, not a proof of RH.
