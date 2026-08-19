# Survival-resolvent Bellman hardening of the score-free Hall route

## Executive result

The direct-integral score-free Hall candidate has one subtle all-depth problem:
its causal identity contains a surviving copy of the parent packet. A naïve
source-tree estimate either counts leaves or replaces actual rough primes by a
deterministic factor-67 chain.

The correct move is algebraic: solve the exact defect identity for the parent
by dividing by the killed survival mass. This produces a discounted Markov
kernel and an optional-stopping theorem for literal-score debt.

Combined with target exactness of compact Hall, it gives two sharp constants:

\[
M_{\rm root}<16,\qquad D_{\rm arithmetic}<32.
\]

The old physical root bound was `<3020`; the old sourcewise score estimate was
`<3600`. The new estimates are smaller and, more importantly, apply to the
actual variable rough-prime tree.

## 1. Target exactness is a mass identity

For one compact quotient fibre, Hall target conservation gives
`m(P_x)=Psi(x)`, not merely `m(P_x)<=even supply`. With endpoint density
`dnu(x)=2L(x)dx/x`, the total root mass is

\[
M_{67}=\int_1^{67}2L(x)\Psi(x)\frac{dx}{x}.
\]

On each arithmetic cell both factors are affine in `sqrt(x)`, so the integral
reduces to a closed expression involving rational Möbius prefixes, square
roots, and one logarithm. The exact directed replay gives

```text
15.7134406686557167269450969040578439770772...
< M_67 <
15.7134406686557167269450969040578439770773...
```

## 2. The Bellman transform

For packet defect `delta=S-H`, exact causal linearity gives

\[
\delta(P)=s_k\delta(P)+\sum_i\lambda_i\delta(C_i)
+\sum_i\lambda_ir_i\delta(P_i).
\]

After division by `1-s_k=sum lambda_i`,

\[
\delta(P)=\sum_i\pi_ir_i\delta(P_i)+\sum_i\pi_i\delta(C_i).
\]

Every current difference has nonpositive debt. Positive debt therefore
propagates through a Markov kernel with factor at most `1/sqrt(67)` on every
transition. This is the exact point at which self-survival ceases to obstruct
the proof.

## 3. Terminal theorem without computation

At `1<=Y<67`, literal entropy is nonnegative and

\[
5\sqrt Y-3\le2(4\sqrt Y-3).
\]

Thus terminal debt is at most twice target mass. Target mass is nonexpansive
along every child. Optional stopping gives debt at most twice initial target
mass. Integrating against the root gives `<32`.

## 4. Complete chain

The remainder of `T-99020` is unchanged:

```text
compact score-free Hall
 -> residual-only causal realization
 -> direct positive endpoint integration
 -> one exact physical row
 -> one all-column thinning and terminal omission
 -> literal score >=4sqrt(X)-O(1)
 -> J_Lambda-H=O(log X)
 -> F_Lambda=o(log^2 X)
 -> prime-square moat
 -> Mellin-Landau
 -> RH candidate.
```

## 5. Hostile tests

The packet rejects:

- omitting division by `1-s_k`;
- permitting positive score debt on a current difference;
- recursively exporting the Hall row bonus;
- replacing actual child masses by source counts;
- using a deterministic `67` path as a substitute for actual rough primes.

## Status

The new algebra and root-mass computation are exact. Their composition with
`T-99020` is a strengthened full proof candidate, not an accepted proof of RH.
