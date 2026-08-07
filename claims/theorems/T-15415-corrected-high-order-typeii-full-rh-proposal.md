# T-15415 — Corrected full RH proposal after the Farey refutation

Claim ID: `T-15415`  
Title: Exact high-order inverse-zeta packets, terminal Euler closure, and one balanced Type-II scale-contraction theorem would prove RH  
Status: **FULL PROPOSAL — ONE BALANCED TYPE-II THEOREM OPEN; RH NOT CLAIMED PROVED**  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `R-15407`, `L-15447`, `L-15449`, `L-15450`; PR #158 at `9ee33527aef3acbb281ebad367aeb1e51652d006`; PR #216 at `b76eef1b769584aa9d66d082bfc6634126f986a2`; PR #229 at `3060b12e6b610e4756c8e97795fbdb52978e6f06`; PR #233 at `0211053679e1b5f524a9238093e64d2e7a4128e3`  
Scope: replacement proof architecture; no generic Farey operator estimate

## 1. Status correction

The frozen Farey determinant proposal `L-15448/T-15414` is rejected by
`R-15407`. The present theorem does not repair or reuse:

- the false translation `(a,b)->(a+kq,b+kv)`;
- the nonexistent odd--odd telescoping;
- the unsupported determinant-row multiplicity;
- the generic local-to-Bohr operator bound.

Instead it returns to the prime/inverse-zeta source before the Möbius signs are
lost and uses an exact finite coefficient identity.

This file is a **full proof proposal**, not a completed proof. Its only
independent arithmetic hinge is stated explicitly in Section 7.

## 2. Safe global front door

For each integer `K>=2`, take the compact high-order safe window

\[
H_K=H^{[K+1]}
\tag{T-15415.1}
\]

of PR #158 `L-15155`. Its Laplace transform has order-`K+1` zeros at the two
boundary points `0` and `1/2`, and no zero in

\[
0<\Re z<\frac12.
\]

Define the complete von-Mangoldt block energy

\[
\mathcal B_{J,K}^{\Lambda}
=
\int_J^{J+1}
\left|
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
H_K(x-\log n)
\right|^2dx.
\tag{T-15415.2}
\]

The safe-filter Hardy transfer of PR #158/PR #216 gives, for every fixed `K`,

\[
\boxed{
\Theta_\zeta
=
\limsup_{J\to\infty}
\frac{\log(1+\mathcal B_{J,K}^{\Lambda})}{2J},}
\tag{T-15415.3}
\]

where

\[
\Theta_\zeta
=
\sup_{\zeta(\rho)=0}
\left(\Re\rho-\frac12\right).
\]

Thus

\[
\mathcal B_{J,K}^{\Lambda}=e^{o(J)}
\quad\Longrightarrow\quad RH.
\tag{T-15415.4}
\]

The ordinary-prime block has the same exponential status by `L-15154`.

## 3. Exact finite source identities

At endpoint `X=e^{J+O_K(1)}`, use either of the following exact packets.

### Heath--Brown packet

For

\[
V=\lceil X^{1/K}\rceil,
\]

PR #158 `L-15156` gives, coefficientwise through `X`,

\[
\boxed{
\Lambda
=
\sum_{j=1}^{K}
(-1)^{j-1}{K\choose j}
\mu_V^{*j}*\log*\mathbf1^{*(j-1)}.}
\tag{T-15415.5}
\]

### Möbius resolvent packet

PR #233 `L-23201` gives, coefficientwise through `X`,

\[
\boxed{
\mu
=
\sum_{j=0}^{K-1}\mu_V*r_V^{*j},
\qquad
r_V=\varepsilon-\mathbf1*\mu_V.}
\tag{T-15415.6}
\]

Both are finite exact inverse-zeta identities. Every tuple retains its actual
Möbius/binomial sign.

The differential bridge `L-15447` identifies the prime and analytic-totient
carriers without asserting a norm equivalence. The first-cell decoder on PR
#229 is retained as a mandatory scalar audit.

## 4. Fixed-reserve packet geometry

Fix once and for all

\[
0<\delta<\frac12,
\qquad
K>\delta^{-1}.
\tag{T-15415.7}
\]

Use the deterministic first-crossing partition of `L-15157`.

1. **Balanced Type II:** both factor groups lie below
   \[
   (1-\delta)J+O_K(1).
   \]
2. **Type I:** one factor group has product at most
   \[
   e^{\delta J+O_K(1)}.
   \]

All tuples with the same destination are recombined with their exact signed
coefficients before any Cauchy--Schwarz, total variation, or divisor bound.

Give every Type-I large coefficient word the complexity rank equal to its
number of unresolved nontrivial variables. `L-15450` proves that every
same-scale Type-I transition lowers this rank. Therefore the packet graph is
acyclic.

## 5. Terminal rows are closed

After finite complexity elimination, every terminal row has:

- one small product `A<=e^(delta J+O_K(1))`;
- one unrestricted large integer variable;
- one polynomial logarithmic coefficient of degree at most `K`;
- the common window `H_K`.

The terminal signal is therefore a finite sum of

\[
\sum_{n\ge1}
\frac{P_A(\log n)}{\sqrt{An}}
H_K(x-\log(An)).
\tag{T-15415.8}
\]

`L-15449` proves that the continuous lattice main term vanishes exactly by the
half-pole moments and that the first Euler remainder is `e^(-x/2)` uniformly in
`A`. The fixed-order divisor ledger then gives

\[
\boxed{
E_{K,\rm terminal}(J)
\le
\exp\left[-(1-2\delta-o_K(1))J\right].}
\tag{T-15415.9}
\]

Thus terminal Type-I packets, their truncated-Möbius boundaries, and their
first-crossing transitions have rate zero; in fact they decay exponentially.

This is the new theorem-level advance over PRs #158 and #233.

## 6. Reduced-complexity rows

Every nonterminal Type-I row is eliminated by finite induction on complexity.
After substitution, it contributes only:

1. balanced Type-II packets at the current output block;
2. declared auxiliary energies at scale at most
   `(1-delta)J+O_K(1)`;
3. the exponentially small terminal rows from (T-15415.9);
4. finite initial/source terms.

The finite tuple multiplicities, binomial coefficients, and divisor words have
zero exponential rate by PR #158 `L-15158`.

No unnamed Type-I or cutoff family remains.

## 7. Sole surviving arithmetic theorem

For fixed `K`, let

\[
E_{K,\tau}(J)\ge0
\]

be the signed, centered normal energy of one balanced packet type. The exact
remaining theorem is:

> **BTP(K) — Balanced Type-II packet theorem.** Every balanced packet in the
> complete signed dictionary satisfies a closed linear or tensor recurrence
> whose physical destinations are at strict fractional logarithmic scales,
> whose coefficient exponent is `epsilon_K`, and for which
> \[
> \boxed{
> \varepsilon_K\longrightarrow0}
> \tag{T-15415.10}
> \]
> along an unbounded sequence of orders. In the tensor formulation the exact
> requirement is
> \[
> \varepsilon_K/(1-\kappa_K)\to0.
> \tag{T-15415.11}
> \]

A representative linear form is

\[
\boxed{
E_{K,\tau}(J)
\le
\exp\{(\varepsilon_K+o_K(1))J\}
\left[
1+
\max_{\upsilon}
\max_{u\le(1-\delta)J+O_K(1)}
E_{K,\upsilon}(u)
\right].}
\tag{T-15415.12}
\]

The balanced theorem must be proved for the actual source-specific normal
packets. It is not a theorem for arbitrary Farey vectors or arbitrary Dirichlet
polynomials.

### Required mechanism

The preferred construction combines:

1. the centered Selberg equation
   \[
   \mathscr L\nu+\nu*\nu=R;
   \]
2. the square-preserving differenced version of PR #219;
3. the positive exponential Hankel adjoints of PRs #229/#219;
4. the factor-ratio normal Gram of PRs #216/#222;
5. exact signed Heath--Brown recombination before Cauchy;
6. strict lower-scale routing of every radial, cutoff, and factor-boundary
   residual.

The cotangent/Mertens first-cell coordinate must be recovered from the final
system. A purported proof of BTP(K) that fails the fixed-ratio Mertens mutation
is incomplete.

## 8. Deduction from BTP(K) to RH

Assume BTP(K) for an unbounded sequence of orders satisfying
(T-15415.10), or its tensor version.

The scale-contraction theorems `T-15121/T-15122`, together with the terminal
closure and finite complexity elimination, give

\[
\limsup_{J\to\infty}
\frac{\log(1+\mathcal B_{J,K}^{\Lambda})}{J}
\le
\frac{\varepsilon_K}{\delta}
\tag{T-15415.13}
\]

in the linear case, or the corresponding tensor quotient. Letting `K` tend to
infinity yields

\[
\Theta_\zeta=0.
\]

By (T-15415.3),

\[
\boxed{RH.}
\tag{T-15415.14}
\]

The deduction from BTP(K) is complete. BTP(K) itself is not proved in this
file.

## 9. Why this proposal survives the frozen review

The proposal does not use any of the rejected operations.

```text
noncoprime Bezout chains        not used
cotangent-row telescoping       not asserted
generic Farey operator norm     explicitly forbidden
rowwise ell1 before Mobius      explicitly forbidden
undefined endpoint allocation   replaced by exact source packets
finite ladder to global claim   not used
```

The first Farey cell is not deleted or treated as a low-dimensional nuisance.
It is a fail-closed audit coordinate that the balanced system must control.

## 10. What is stronger than the neighboring proposals

PR #158 left all of `CP(K)` open: terminal rows, transition rows, companions,
and balanced Type II.

PR #233 reduced the programme to a terminal Selberg--Hankel certificate family
`STC(K)` but did not construct that family.

`L-15449/L-15450` close the terminal family directly and show

\[
\eta_K=0.
\]

The replacement frontier is therefore strictly smaller:

\[
\boxed{
\text{only the signed balanced Type-II normal-energy theorem remains.}}
\tag{T-15415.15}
\]

## 11. Review and rejection protocol

A reviewer should freeze the new head and check, in order:

1. the Euler discrepancy identity and uniform `A` cancellation in `L-15449`;
2. the terminal complexity normal form in `L-15450`;
3. the complete packet dictionary and source signs inherited from PR #158;
4. absence of hidden terminal cutoffs;
5. the exact formulation of BTP(K);
6. every proposed balanced packet inequality and strict scale destination;
7. the first-cell Mertens mutation;
8. the final Hardy transfer.

A defect in Sections 1--4 of this list reopens the terminal theorem. Failure to
prove BTP(K) leaves the proposal incomplete. Neither outcome revives the frozen
Farey proof.

## 12. Exact status

```text
frozen Farey proof                    REJECTED
exact arithmetic / Mellin spine       PRESERVED
terminal Type-I family                PROPOSED CLOSED BY L-15449/L-15450
balanced Type-II theorem BTP(K)       OPEN
full proof architecture               PROPOSED
Riemann Hypothesis                     NOT YET PROVED
```
