# M-15112 — High-order centered Type-II full RH proposal

Methodology ID: `M-15112`  
Title: Close the adjoint prime-energy route through a finite high-order Heath--Brown packet, rowwise null-mode centering, and vanishing-rate scale contraction  
Status: **FULL RH PROPOSAL — CENTERED PACKET ESTIMATE PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Review input: the verified-with-fixes post-review of PR #158 at `7902480c92a34e8ca5788e8e1e844ac3727e3a4e`  
Imported source: PR #216 frozen at `b76eef1b769584aa9d66d082bfc6634126f986a2`  
Dependencies: `L-15151`, `L-15154`--`L-15156`, `T-15121`, `T-15122`  
Scope: replacement full proposal; RH is not claimed proved

## 1. Review disposition

The latest review is accepted on its central point: an exact Vaughan or
Heath--Brown identity is not enough unless

1. every row retains exact source centering;
2. auxiliary Möbius/divisor/Type-I/Type-II rows form a closed system;
3. the closure occurs at a strict logarithmic scale contraction;
4. the coefficient loss is subexponential, or tends to zero relative to the
   contraction as the identity order increases.

The previous scalar adjacent-block recurrence is not used here.

## 2. Exact front door

For every finite order `K`, use the compact high-order safe window

\[
 H_K=H^{[K+1]}
 \tag{M-15112.1}
\]

of `L-15155`. Define the full-von-Mangoldt block

\[
 \mathcal B_{J,K}^{\Lambda}
 =\int_J^{J+1}
 \left|
  \sum_{n\ge2}{\Lambda(n)\over\sqrt n}
  H_K(x-\log n)
 \right|^2dx.
 \tag{M-15112.2}
\]

The window has no transform zero in the open counterexample strip. Therefore
`L-15151` identifies

\[
 \limsup_{J\to\infty}
 {\log(1+\mathcal B_{J,K}^{\Lambda})\over2J}
 \tag{M-15112.3}
\]

with the common rightmost-zero displacement `Theta_zeta` for every fixed `K`.

By `L-15154`, the ordinary-prime and full-von-Mangoldt blocks differ only by a
polynomial block error. Thus either source may be used in the arithmetic
construction without changing the exponent.

## 3. Exact finite packet

For endpoint `X=exp(J+O_K(1))`, take

\[
 V=X^{1/K}.
 \]

`L-15156` proves, coefficient by coefficient for `n<=X`,

\[
 \Lambda(n)
 =\sum_{j=1}^{K}(-1)^{j-1}{K\choose j}
 (\mu_V^{*j}*\log*1^{*(j-1)})(n).
 \tag{M-15112.4}
\]

Every factor tuple is assigned by one deterministic first-crossing rule to:

- a Type-I row with one small packet and one lower-complexity large word; or
- a Type-II row with two strict-fraction factor packets.

The complete finite row dictionary is `mathfrak T_K`.

## 4. Rowwise centering is now exact

The `j`-th row has pole order at most `j+1<=K+1`. The order-`K+1` boundary zeros
of `H_K` annihilate the entire inverse Laurent polynomial of every row.

Thus, for each `tau in mathfrak T_K`, one may subtract its own pole companion
`rho_tau` before any Cauchy--Schwarz, dispersion, or factor grouping. No
recombination hypothesis is required:

\[
 \mathcal B_{J,K}^{\Lambda}
 \le R_K\sum_{\tau\in\mathfrak T_K}E_{K,\tau}(J),
 \tag{M-15112.5}
\]

where every `E_(K,tau)` is a nonnegative self-energy of an independently
centered row.

This closes the rowwise-centering gap identified by the review.

## 5. Correct Type-II orientation

Every row energy is retained in the adjoint/normal form

\[
 \langle H_K,
  \mathcal P_\tau^*\chi_J
  \mathcal P_\tau H_K\rangle.
 \tag{M-15112.6}
\]

For a balanced split `(A,B)`, the two factor variables remain on opposite sides
of the Gram. The packet is never replaced by a product-dilation form.

PR #216's balanced semiprime identity is the ordinary-prime member of this
normal family. `L-15154` supplies the exact bridge to the full-von-Mangoldt
normal family used by the Heath--Brown identity.

## 6. Collective, not rowwise-total-variation, estimation

The binomial packet in (M-15112.4) contains cancellations of size comparable to
the source itself. The proposed proof is therefore constrained as follows.

### 6.1 Preserve signed packets

Rows sharing the same first-crossing factor split are combined with their exact
binomial coefficients before an absolute value is taken. A certificate records
the complete signed coefficient vector.

### 6.2 Type I

A Type-I row records:

1. a small packet supported at logarithmic scale at most `delta_K J+O_K(1)`;
2. a large coefficient word of strictly lower convolution complexity;
3. its exact polynomial pole companion;
4. a normal self-energy destination in the finite auxiliary vector.

The small packet may contribute a mildly exponential coefficient. It is not
required to be polynomial at fixed `K`; its rate is entered explicitly as
`epsilon_K`.

### 6.3 Type II

A Type-II row records two factor packets at scales

\[
 \alpha_{K,1}J+O_K(1),
 \qquad
 \alpha_{K,2}J+O_K(1),
 \]

with a strict tensor contraction

\[
 \theta_1\alpha_{K,1}+\theta_2\alpha_{K,2}<1.
 \tag{M-15112.7}
\]

The factor-ratio Gram is bounded by a tensor auxiliary energy, not by total
variation and not by the original prime block alone.

### 6.4 Smooth divisor/log rows

Rows involving unrestricted `1` and `log` factors retain their exact Laurent
polynomial companions. Any Euler--Maclaurin or divisor-row remainder is a named
auxiliary component. It is not silently declared polynomial.

## 7. Load-bearing centered packet estimate

For each fixed `K`, the proposed analytic theorem is:

> **CP(K).** The finite centered row vector of `L-15156` satisfies a linear or
> tensor scale-contraction recurrence with coefficient rate `epsilon_K`,
> contraction reserve `delta_K` (or `1-kappa_K`), and
> \[
> {\epsilon_K\over\delta_K}\to0
> \quad\text{or}\quad
> {\epsilon_K\over1-\kappa_K}\to0
> \qquad(K\to\infty).
> \tag{M-15112.8}
> \]

More explicitly, each component must satisfy either

\[
 E_{K,\tau}(J)
 \le
 e^{(\epsilon_K+o_K(1))J}
 \left[
 1+\max_{\upsilon}
 \max_{k\le(1-\delta_K)J+O_K(1)}
 E_{K,\upsilon}(k)
 \right],
 \tag{M-15112.9}
\]

or the tensor version of `T-15122`.

`CP(K)` is the sole unproved arithmetic theorem in this proposal.

## 8. Deduction of RH

Assume `CP(K)` for an unbounded sequence of orders `K` satisfying
(M-15112.8). `T-15122` gives

\[
 2\Theta_\zeta
 \le {\epsilon_K\over\delta_K}
 \quad\text{or}\quad
 2\Theta_\zeta
 \le {\epsilon_K\over1-\kappa_K}.
 \tag{M-15112.10}
\]

Letting `K` increase yields

\[
 \Theta_\zeta=0.
 \]

Hence every nontrivial zeta zero lies on the critical line:

\[
 \boxed{\mathrm{RH}.}
 \tag{M-15112.11}
\]

The window varies with `K`, but every window detects the same invariant because
its extra zeros lie only on the boundary lines.

## 9. Finite proof-object schema

A certificate for one order and block contains:

```text
K, X, V, window SHA-256
complete Lambda manifest
truncated Möbius manifest
exact Heath-Brown tuple rows
binomial signs and multiplicities
first-crossing Type-I/II partition
row Laurent companions
null-mode annihilation checks
centered normal Gram rows
auxiliary-energy type identifiers
factor-scale intervals
linear/tensor recurrence coefficients
coefficient exponent epsilon_K
scale reserve delta_K or kappa_K
```

The checker rejects:

- rowwise total variation before signed packet recombination;
- a pole companion outside the window null space;
- product-dilation/factor-ratio substitution;
- an undeclared auxiliary row;
- a missing prime-power or endpoint tuple;
- a scale destination exceeding the declared contraction;
- inference from finitely many `K` values to RH.

## 10. What is and is not completed

Completed exactly in this pass:

1. prime/full-von-Mangoldt polynomial block equivalence;
2. the correct normal-operator bridge;
3. high-order safe windows;
4. independent centering of every decomposition row;
5. the finite Heath--Brown tuple and multiplicity ledger;
6. a deterministic Type-I/Type-II partition;
7. a finite auxiliary-energy dictionary;
8. scalar, vector, and tensor scale-contraction composition theorems.

Still proposed:

\[
 \boxed{CP(K).}
 \]

Thus this is a robust full proposal with one explicit centered packet estimate
as its independent-review hinge. It is not a completed proof of RH.
