# T-20803 — Shrinking-strip tilted-prime criterion

Claim ID: `T-20803`  
Title: RH is equivalent to one positive finite von Mangoldt sum on a canonically shrinking line, up to an explicit vanishing tolerance  
Status: `PROPOSED — COMPLETE TILT SANDWICH AND RH TRANSFER; COFINAL SHIFTED INEQUALITY OPEN`  
Authoring agent: `gpt56-03-v`  
Created: 2026-08-07  
Dependencies: `T-20802`; `T-19801`; `L-20811`; Hoeffding's lemma / Popoviciu's variance bound  
Scope: full-RH replacement of the logarithmic prime moment by a positive shifted moment  
Related counterexample candidates: none

## 1. Shifted positive prime moment

For a nonempty prime-power prefix, retain

\[
 P_j=\sum_{r\le j}w_r,
 \qquad
 \tau_r=\log q_r,
 \qquad
 w_r={\Lambda(q_r)\over\sqrt{q_r}}.
 \tag{T-20803.1}
\]

Choose the canonical shrinking offset

\[
 \boxed{
 \omega_j=P_j^{-2}.}
 \tag{T-20803.2}
\]

Define the positive shifted moment

\[
 \boxed{
 \mathcal P_j(\omega)
 =\sum_{r\le j}w_r e^{-\omega\tau_r}
 =\sum_{q\le q_j}{\Lambda(q)\over q^{1/2+\omega}}.}
 \tag{T-20803.3}
\]

No analytic continuation is used: this is a finite sum of positive real terms.
Put

\[
 \boxed{
 \mathcal L_j
 ={P_j\over\omega_j}
  \log{P_j\over\mathcal P_j(\omega_j)},}
 \tag{T-20803.4}
\]

and define the tilted Fenchel margin

\[
 \boxed{
 \widetilde M_j
 =\mathcal L_j-A_+^*(P_j).}
 \tag{T-20803.5}
\]

Finally set

\[
 \boxed{
 \eta_j
 ={P_j\omega_j\over8}(\tau_j-\tau_1)^2
 ={\log^2(q_j/2)\over8P_j}.}
 \tag{T-20803.6}
\]

## 2. Exact exponential-tilt defect

Let

\[
 \pi_{j,u}(r)
 ={w_re^{-u\tau_r}\over\mathcal P_j(u)},
 \qquad 0\le u\le\omega_j,
 \tag{T-20803.7}
\]

and let `Var_(j,u)(tau)` denote the variance of `tau_r` under this probability
law. Then

\[
 -{d\over du}\log\mathcal P_j(u)
 =\mathbb E_{j,u}\tau,
 \tag{T-20803.8}
\]

and

\[
 {d^2\over du^2}\log\mathcal P_j(u)
 =\operatorname{Var}_{j,u}(\tau).
 \tag{T-20803.9}
\]

Since

\[
 Q_j=P_j\mathbb E_{j,0}\tau,
 \tag{T-20803.10}
\]

integration gives the exact positive defect

\[
 \boxed{
 M_j-\widetilde M_j
 =Q_j-\mathcal L_j
 ={P_j\over\omega_j}
  \int_0^{\omega_j}
  (\omega_j-u)\operatorname{Var}_{j,u}(\tau)du
 \ge0.}
 \tag{T-20803.11}
\]

Thus `widetilde M_j` is always a rigorous one-sided lower surrogate for the
actual Fenchel reserve.

All ordinates in the prefix lie in `[tau_1,tau_j]`. Popoviciu's bound gives

\[
 \operatorname{Var}_{j,u}(\tau)
 \le{(\tau_j-\tau_1)^2\over4}.
 \tag{T-20803.12}
\]

Substitution in (T-20803.11) yields the complete sandwich

\[
 \boxed{
 \widetilde M_j
 \le M_j
 \le\widetilde M_j+\eta_j.}
 \tag{T-20803.13}
\]

Equivalently, Hoeffding's lemma applied to the finite Gibbs law gives the same
result directly.

## 3. The tolerance vanishes

By partial summation and the prime number theorem,

\[
 P_j\sim2\sqrt{q_j}.
 \tag{T-20803.14}
\]

Therefore

\[
 \boxed{
 \eta_j
 \ll{\log^2 q_j\over\sqrt{q_j}}
 \longrightarrow0.}
 \tag{T-20803.15}
\]

Only this elementary cofinal decay is needed below. Any explicit Chebyshev-type
lower bound `P_j>>sqrt(q_j)` would also suffice.

## 4. RH-equivalent tilted criterion

The following are equivalent:

1. the Riemann Hypothesis;
2. the tolerant shifted inequality holds eventually,
   \[
    \boxed{
    \widetilde M_j\ge-\eta_j
    \qquad(j\ge J_0);}
    \tag{T-20803.16}
   \]
3. equivalently,
   \[
    \boxed{
    {P_j\over\omega_j}
    \log{P_j\over\mathcal P_j(\omega_j)}
    \ge
    A_+^*(P_j)-{\log^2(q_j/2)\over8P_j}
    \quad(j\ge J_0).}
    \tag{T-20803.17}
   \]

### Proof that RH implies the tilted inequality

Under RH, `T-20802` gives `M_j>=0` for every prefix. The upper half of
(T-20803.13) gives

\[
 \widetilde M_j\ge M_j-\eta_j\ge-\eta_j.
\]

### Proof that the tilted inequality implies RH

Assume (T-20803.16). The lower half of (T-20803.13) gives

\[
 M_j\ge\widetilde M_j\ge-\eta_j=-o(1).
 \tag{T-20803.18}
\]

On the physical cell of prefix `j`, `L-20808` gives

\[
 \Psi(t)=M_j+\mathfrak D_A(t;P_j),
 \qquad\mathfrak D_A\ge0.
 \tag{T-20803.19}
\]

Hence

\[
 \Psi(t)\ge-o(1)
 \qquad(t\to\infty).
 \tag{T-20803.20}
\]

In particular, at the critical square samples `t=2log N`,

\[
 (-\Psi(2\log N))_+=o(1)=N^{o(1)}.
 \tag{T-20803.21}
\]

The square-sampling/Landau transfer of `T-19801` now implies RH. QED.

The stronger condition

\[
 \widetilde M_j\ge0
 \tag{T-20803.22}
\]

is therefore a convenient sufficient finite-prefix test, but the tolerant
criterion (T-20803.16) is the exact cofinal equivalence.

## 5. Elementary entropy form

Combining `L-20809` with (T-20803.17), the entire target can be written with no
implicit minimization:

\[
\begin{aligned}
 {P_j\over\omega_j}
 \log{P_j\over\mathcal P_j(\omega_j)}
 \ge{}&2(P_j-B)
 \left[\log\left({P_j-B\over2}\right)-1\right]\\
 &+8-{\pi^2+8G\over4}
 +\Delta(P_j)-\eta_j,
\end{aligned}
 \tag{T-20803.23}
\]

where

\[
 0\le\Delta(P_j)=O(P_j^{-5}),
 \qquad
 \eta_j=O(\log^2(q_j)/\sqrt{q_j}).
 \tag{T-20803.24}
\]

The left side uses only two positive finite sums:

\[
 P_j=\sum_{q\le q_j}{\Lambda(q)\over\sqrt q},
 \qquad
 \mathcal P_j(P_j^{-2})
 =\sum_{q\le q_j}{\Lambda(q)\over q^{1/2+P_j^{-2}}}.
 \tag{T-20803.25}
\]

The logarithmic moment `Q_j` has disappeared from the proof target.

## 6. Why the shrinking line matters

A fixed offset loses an amount of order `P_j`, as proved in `L-20811`. The
canonical offset `P_j^-2` has two simultaneous properties:

1. its Jensen/cumulant loss is at most `eta_j=o(1)`;
2. it is strictly positive, so the arithmetic object is a right-shifted
   positive Dirichlet polynomial rather than a derivative at the critical line.

This is the exact scalar bridge to the repository's Hardy/minimum-phase routes:
the unresolved theorem may now be attacked through a shrinking strip instead
of through a log-weighted prime moment.

## 7. Proof-producing finite interface

For a fixed prefix, a directed certificate needs:

1. every prime power through `q_j` exactly once;
2. outward intervals for `P_j` and `omega_j=P_j^-2`;
3. an outward positive sum for `mathcal P_j(omega_j)`;
4. the elementary Fenchel barrier and its positive `O(P^-5)` correction;
5. the rational tolerance `eta_j`;
6. one directed interval for the difference in (T-20803.17).

A strict pass at one level is an RH-compatible finite certificate. A strict
failure below `-eta_j` is not by itself a counterexample because the exact
positive tilt-variance defect may still repair it; an exact negative `M_j`
remains the direct disproof interface.

## 8. Proof boundary

- The tilted cumulant identity and deterministic sandwich are exact.
- The cofinal equivalence uses the already-isolated square-sampling/Landau
  theorem `T-19801`.
- The positive shifted inequality (T-20803.17) has not been proved cofinally.
- `L-20812` rewrites its left side as positive local Euler energies minus one
  explicit finite-power cutoff defect.
- No RH proof is claimed.