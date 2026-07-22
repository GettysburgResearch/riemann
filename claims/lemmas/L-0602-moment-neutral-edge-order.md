# L-0602 — Moment-neutral order of a newly admitted prime-power block

Claim ID: L-0602  
Title: Moment-neutral order of a newly admitted prime-power block  
Status: PROPOSED  
Authoring agent: `gpt56-01-a`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `D-0001`, `L-0601`  
Scope: exact local asymptotics of one prime-power contribution  
Related counterexample candidates: none

## Statement

For a real-even vector `v=(v_0,...,v_N)`, define

\[
 M_0(v)=v_0+\sqrt2\sum_{k=1}^{N}v_k,
 \qquad
 M_j(v)=\sqrt2\sum_{k=1}^{N}k^{2j}v_k\quad(j\ge1).
\]

Let `q=p^a`, put

\[
 \epsilon=1-\frac{\log q}{\log c}>0,
 \qquad w_q=\frac{\Lambda(q)}{\sqrt q},
\]

and let `P_q(c)` be the single `q`-block of the matrix. If

\[
 M_0(v)=M_1(v)=\cdots=M_s(v)=0,
\]

then, as `epsilon -> 0+`,

\[
 v^{\mathsf T}P_q(c)v
 =-w_q\frac{2(2\pi)^{4s+4}}{(4s+5)!}
 M_{s+1}(v)^2\epsilon^{4s+5}
 +O(\epsilon^{4s+7}).
\]

In particular, the first-order jump is absent on `M_0=0`; the first possible
new-prime term is then negative of order `epsilon^5`. If also `M_1=0`, the
first possible term is negative of order `epsilon^9`.

## Definitions

With the full symmetric coefficients of `D-0001`, write

\[
 T_v(t)=v_0+\sqrt2\sum_{k=1}^{N}v_k\cos(2\pi kt)
\]

and

\[
 K_v(\omega)=2\int_0^\omega T_v(t)T_v(\omega-t)\,dt.
\]

The finite source calculus gives the exact identity

\[
 v^{\mathsf T}P_q(c)v=-w_qK_v(\epsilon).
\]

## Proof

The Taylor expansion of the even trigonometric polynomial at zero is

\[
 T_v(t)=\sum_{j\ge0}
 \frac{(-1)^j(2\pi)^{2j}}{(2j)!}M_j(v)t^{2j}.
\]

Under the stated moment constraints, its first possible term is

\[
 T_v(t)=A t^{2s+2}+O(t^{2s+4}),
 \qquad
 A=\frac{(-1)^{s+1}(2\pi)^{2s+2}}{(2s+2)!}M_{s+1}(v).
\]

Substitution into the Volterra convolution gives

\[
 K_v(\epsilon)
 =2A^2\int_0^\epsilon
 t^{2s+2}(\epsilon-t)^{2s+2}\,dt
 +O(\epsilon^{4s+7}).
\]

The beta integral is

\[
 \int_0^\epsilon t^{2s+2}(\epsilon-t)^{2s+2}\,dt
 =\epsilon^{4s+5}
 \frac{((2s+2)!)^2}{(4s+5)!}.
\]

After cancellation of `((2s+2)!)^2`, this becomes

\[
 K_v(\epsilon)=
 \frac{2(2\pi)^{4s+4}}{(4s+5)!}
 M_{s+1}(v)^2\epsilon^{4s+5}
 +O(\epsilon^{4s+7}).
\]

Multiplication by `-w_q` proves the claim.

## Analytic domain audit

Everything is a finite Taylor expansion and an integral on a real compact
interval. No branch or convergence issue occurs.

## Dependency audit

The exact contraction `v^T P_q v=-w_qK_v(epsilon)` is the single-frequency
finite source calculus in the normalization of `D-0001`. The Taylor and beta
integral calculation is independent of zeta.

## Gap audit

- The lemma isolates only the newly admitted `q` term. It says nothing about
  the sign of the full derivative or full matrix.
- The `O(epsilon^(4s+7))` term can matter unless the edge offset is genuinely
  small and its coefficient is controlled.
- Moment-neutral searches deliberately suppress the strongest first-order
  prime-edge signal; this can make a coarse scan falsely look inactive.

## Adversarial tests

`X-0601` checks the exact matrix contraction against the endpoint integral and
verifies fifth- and ninth-order ratios at decreasing `epsilon`.

## Remaining uncertainty

The result is complete-looking but awaits independent review of the source
normalization and the exact contraction identity.

## Suggested next attack

Use offset ladders adapted to the first nonvanishing moment. A search in
`M_0=...=M_s=0` should not reuse the offset schedule of the unconstrained edge
search; its first signal is four powers later for every added constraint.
