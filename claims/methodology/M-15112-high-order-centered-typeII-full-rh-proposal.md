# M-15112 — High-order centered Type-II programme after the Möbius-core audit

Methodology ID: `M-15112`  
Title: Exact finite Heath–Brown packet infrastructure and the unresolved Möbius-energy theorem  
Status: **BLOCKED — `CP(K)` IS NECESSARY FOR THIS CHAIN AND IS NOT PROVED**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Updated: 2026-08-07 after the direct `CP(K)` attack  
Review input: PR #158 at `7902480c92a34e8ca5788e8e1e844ac3727e3a4e`  
Imported source: PR #216 frozen at `b76eef1b769584aa9d66d082bfc6634126f986a2`  
Dependencies: `L-15151`, `L-15154`--`L-15159`, `T-15121`--`T-15123`, `R-15114`  
Scope: exact infrastructure and proof-boundary record; **not a completed RH proposal**

## 1. Direct answer about necessity

For the chain formerly advertised here, `CP(K)` is necessary. One may remove
the label `CP(K)`, but only by replacing it with a theorem that directly proves
a subexponential safe energy for the Möbius or von-Mangoldt source. Such a
replacement has the same rightmost-zero content.

The direct attack did not prove `CP(K)`. It proved instead that the packet
contains an exact Möbius core, so the missing estimate is the RH-bearing
arithmetic theorem rather than a routine Type-II lemma.

Accordingly this file is no longer presented as a scarce-review-time full
proposal.

## 2. Exact front door retained

For every fixed finite order `K`, the high-order compact safe window

\[
 H_K=H^{[K+1]}
\]

has no transform zero in the open counterexample strip. The full-von-Mangoldt
block

\[
 \mathcal B_{J,K}^{\Lambda}
 =\int_J^{J+1}
 \left|\sum_n{\Lambda(n)\over\sqrt n}
 H_K(x-\log n)\right|^2dx
\]

therefore has upper exponential exponent `2 Theta_zeta` by `L-15151`.

`L-15154` proves polynomial equivalence with the ordinary-prime normal energy,
while preserving the adjoint/factor-ratio orientation.

## 3. Exact finite infrastructure retained

The following parts remain exact proposed mathematics, independently reviewable:

1. `L-15155`: arbitrary-order safe windows and a finite null-mode quotient;
2. `L-15156`: the exact finite truncated Heath–Brown coefficient identity,
   tuple ledger, deterministic Type-I/Type-II partition, signed packet grouping,
   transition-residual rules, and terminal flags;
3. `L-15157`: a fixed logarithmic scale reserve independent of `K`;
4. `L-15158`: zero exponential cost of all fixed-order combinatorial
   multiplicities;
5. `T-15121/T-15122`: exact scalar, vector, tensor, and increasing-order
   scale-contraction composition theorems;
6. `X-15125`: finite algebraic regression only.

None of these estimates the actual centered packet vector.

## 4. Exact Möbius decoder

Define

\[
 A_{K,V}
 =\sum_{j=1}^{K}(-1)^{j-1}{K\choose j}
 \mu_V^{*j}*1^{*(j-1)}.
\]

`L-15159` proves

\[
 \boxed{A_{K,V}(n)=\mu(n)\qquad(n\le V^K).}
\]

Consequently

\[
 A_{K,V}*\log=\Lambda
\]

through the same range.

If the final logarithmic variable is fixed at `q0`, all remaining signed tuple
coefficients recombine to

\[
 \mu(m)\log q_0.
\]

Already at `q0=2`, the normalized packet signal is a translate and scalar
multiple of

\[
 Q_{\mu,H_K}(x)
 =\sum_m{\mu(m)\over\sqrt m}H_K(x-\log m).
\]

Its Laplace transform is

\[
 {\widehat H_K(z)\over\zeta(z+1/2)}.
\]

`T-15123` therefore gives

\[
 \Theta_\zeta
 =\limsup_{X\to\infty}
 {\log(1+E_{\mu,H_K}(X))\over2X}.
\]

Thus the fixed-logarithm slice itself is RH-equivalent.

## 5. Finite destination packets retain the Möbius exponent

If a fixed-logarithm slice is divided into `R_K` destination vectors with
self-energies `E_(K,tau)`, then

\[
 \max_\tau E_{K,\tau}
 \ge {E_{\mu,q_0}\over R_K^2}.
\]

Since `R_K` is fixed with respect to the output block scale, packetization
cannot make every component have a smaller upper exponential exponent than the
Möbius source.

This does not refute the possibility of proving a signed scale recurrence. It
shows that any such proof must contain the genuine Möbius cancellation.

## 6. Why the prior analytic sketch is insufficient

The following facts do not prove `CP(K)`:

- exact coefficient reconstruction;
- high-order boundary zeros;
- a fixed first-crossing reserve;
- subexponential tuple multiplicity;
- a finite auxiliary-energy dictionary;
- generic Cauchy, Young, Schur, or large-sieve estimates after total variation.

Balanced multiplicative factors have total logarithmic scale equal to the
output scale. Generic norm estimates either pay this full scale or become a
critical local moment estimate for Möbius coefficients. The latter is another
RH-equivalent formulation, not an unconditional input.

## 7. Exact remaining theorem

A valid continuation still may attempt:

> **`CP(K)`.** For an unbounded sequence of orders, the complete signed packet
> vector—including certified companions, every cutoff transition, terminal
> Type-I packets, centered factor-ratio Type-II packets, and all auxiliary
> rows—satisfies a strict scale-contraction recurrence with analytic rate
> tending to zero.

But this theorem is open.

Equivalently, one may bypass the packet and prove directly

\[
 E_{\mu,H}(X)=\exp(o(X))
\]

for one safe `H`, which by `T-15123` proves RH.

## 8. Exact regression

`X-15126` verifies, for `(K,V)=(2,5),(3,4),(4,3)`:

```text
A_(K,V)=mu                       no mismatches
A_(K,V)*log=Lambda               no mismatches
fixed q=2 Möbius slice           no mismatches
```

Proof digest:

```text
21a807fdd5b4fbd0fe4017816cb2660dc1bc645c52e0d8a8285eb84b72647eb1
```

Eight tests pass.

## 9. Review recommendation

The exact infrastructure can be reviewed as lemmas. This branch should not be
counted among active complete RH proposals until `CP(K)` or an equally strong
Möbius-energy theorem is actually supplied.

## 10. Status boundary

```text
finite Heath-Brown packet algebra:  PROPOSED / REVIEWABLE
Möbius-core decoder:                PROPOSED EXACT
CP(K):                              OPEN / NECESSARY FOR THIS CHAIN
M-15112 completed RH proposal:      WITHDRAWN / BLOCKED
Riemann Hypothesis:                 NOT PROVED
```
