# T-15123 — Möbius safe-energy rightmost-zero criterion

Claim ID: `T-15123`  
Title: Every compact zero-free safe filter turns the Möbius source—and hence a fixed Heath–Brown logarithmic slice—into a positive energy with exponent equal to the rightmost zeta-zero displacement  
Status: **PROPOSED EXACT TRANSFER THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15151`, `L-15155`, `L-15159`; standard reciprocal-zeta growth on a fixed zero-free half-plane  
Scope: exact identification of the RH-bearing packet; no proof that its exponent vanishes

## 1. Möbius safe signal

Let `H` be a compact real function whose bilateral Laplace transform satisfies:

1. sufficient vertical decay for `L-15151`;
2. no zero in
   \[
   0<\operatorname{Re}z<\frac12.
   \]

Every high-order window `H^[m]` of `L-15155` has these properties.

Define

\[
 \boxed{
 Q_{\mu,H}(x)
 =\sum_{n\ge1}{\mu(n)\over\sqrt n}
  H(x-\log n).}
 \tag{T-15123.1}
\]

At every real `x` the sum is finite.

For `Re z>1/2`, direct integration and absolute convergence give

\[
\begin{aligned}
 \mathcal LQ_{\mu,H}(z)
 &=\widehat H(z)
   \sum_{n\ge1}{\mu(n)\over n^{z+1/2}}\\
 &=\boxed{
 {\widehat H(z)\over\zeta(z+1/2)}.}
\end{aligned}
 \tag{T-15123.2}
\]

## 2. Pole geometry

A nontrivial zero `rho` of zeta produces a pole at

\[
 z=\rho-\frac12.
 \tag{T-15123.3}
\]

Because `widehat H` has no zero in the open counterexample strip, no zero with

\[
 \operatorname{Re}\rho>\frac12
\]

is canceled. The pole of zeta at `s=1` becomes a zero of `1/zeta`, not a
singularity. Trivial-zero poles lie to the left of the relevant half-plane.

Put

\[
 \Theta_\zeta
 =\sup_{\zeta(\rho)=0}
  \left(\operatorname{Re}\rho-\frac12\right).
 \tag{T-15123.4}
\]

Then the rightmost nonremovable pole of (T-15123.2) in `Re z>0` has real part
`Theta_zeta`.

## 3. Uniform Hardy bound

Fix `sigma>Theta_zeta`. The reciprocal zeta function is analytic on

\[
 \operatorname{Re}(z+1/2)\ge\frac12+\sigma.
\]

On a fixed zero-free half-plane it has a standard finite-order vertical bound;
on sufficiently large real part it is uniformly bounded by the absolutely
convergent Euler product. The compact piecewise-smooth safe windows used here
supply at least two inverse powers of `|Im z|`. After filling finitely many
removable points in a compact rectangle,

\[
 \sup_{u\ge\sigma}
 \int_{\mathbb R}
 \left|{\widehat H(u+it)\over
              \zeta(1/2+u+it)}\right|^2dt
 <\infty.
 \tag{T-15123.5}
\]

This is the `H2` hypothesis of `L-15151`.

## 4. Energy exponent

Define

\[
 E_{\mu,H}(X)
 =\int_{-\infty}^{X}|Q_{\mu,H}(x)|^2dx.
 \tag{T-15123.6}
\]

Applying `L-15151` to (T-15123.2) gives

\[
 \boxed{
 \Theta_\zeta
 =\inf\left\{\sigma>0:
   \int_{\mathbb R}e^{-2\sigma x}
   |Q_{\mu,H}(x)|^2dx<\infty
  \right\}}
 \tag{T-15123.7}
\]

and

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}
 {\log(1+E_{\mu,H}(X))\over2X}.}
 \tag{T-15123.8}
\]

Consequently

\[
 \boxed{
 \mathrm{RH}
 \iff
 E_{\mu,H}(X)=\exp(o(X)).}
 \tag{T-15123.9}
\]

The same statement holds for unit-block energies after taking their cumulative
sum.

## 5. Heath–Brown fixed-logarithm slice

Let `K,V,X=V^K` be as in `L-15159`, and fix `q0>=2`. On every output block whose
compact support stays within `q0*m<=X`, equation (L-15159.11) gives

\[
 Q_{K,V;q_0,H}(x)
 ={\log q_0\over\sqrt{q_0}}
 Q_{\mu,H}^{(X/q_0)}(x-\log q_0).
 \tag{T-15123.10}
\]

As the block scale and coefficient endpoint grow together, the truncation is
irrelevant on the declared compact support. Translation and multiplication by
a fixed nonzero constant do not change an upper exponential energy exponent.
Therefore the fixed-`q0` packet, already for `q0=2`, detects the same value
`Theta_zeta`.

## 6. Consequence for a packet system

For every fixed `K`, let the fixed-`q0` source be partitioned into the finite
destination dictionary of `L-15156`. By (L-15159.15), at least one destination
self-energy is at least `R_K^(-2)` times the Möbius-slice energy. Hence

\[
 \boxed{
 \max_{\tau}
 \limsup_{J\to\infty}
 {\log(1+E_{K,\tau}(J))\over2J}
 \ge\Theta_\zeta.}
 \tag{T-15123.11}
\]

The reverse aggregate bound follows from Gram Cauchy–Schwarz. Thus finite
packetization does not move the rightmost-zero exponent into a harmless
combinatorial coefficient.

## 7. Status of `CP(K)`

For the chain in `M-15112`, `CP(K)` is necessary unless it is replaced by
another theorem that directly proves the subexponential Möbius energy in
(T-15123.9). The label `CP(K)` is not logically necessary for every conceivable
proof of RH, but no weaker completed theorem currently replaces it in this
proposal.

In particular, the exact algebraic construction of the packet does not by
itself make the analytic packet estimate routine. The estimate contains a
complete RH-equivalent Möbius source.

## 8. Proof boundary

Closed here, subject to the stated standard reciprocal-zeta vertical bound:

- the Möbius Laplace transform;
- its pole geometry;
- the weighted and cumulative energy exponent;
- the fixed-logarithm Heath–Brown slice transfer;
- the finite-packet exponent lower bound.

Open:

- subexponential Möbius safe energy;
- `CP(K)`;
- RH.
