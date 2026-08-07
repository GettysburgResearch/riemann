# M-15112 — High-order centered Type-II full RH proposal

Methodology ID: `M-15112`  
Title: Close the adjoint prime-energy route through a finite high-order Heath--Brown packet, a certified null-mode quotient, and vanishing-rate scale contraction  
Status: **FULL RH PROPOSAL — CENTERED PACKET ESTIMATE `CP(K)` PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Updated: 2026-08-07 after packet-companion self-audit  
Review input: the verified-with-fixes post-review of PR #158 at `7902480c92a34e8ca5788e8e1e844ac3727e3a4e`  
Imported source: PR #216 frozen at `b76eef1b769584aa9d66d082bfc6634126f986a2`  
Dependencies: `L-15151`, `L-15154`--`L-15156`, `T-15121`, `T-15122`  
Scope: replacement full proposal; RH is not claimed proved

## 1. Review disposition

The latest review is accepted on its central point: an exact Vaughan or
Heath--Brown identity is not enough unless

1. every removed continuous companion is certified in an exact kernel null
   space;
2. all cutoff and shifted-boundary residuals remain visible;
3. auxiliary Möbius/divisor/Type-I/Type-II packets form a closed finite system;
4. signed binomial packets are recombined before absolute values;
5. the closure occurs at a strict logarithmic scale contraction;
6. the coefficient loss is subexponential, or tends to zero relative to the
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
polynomial block error. Thus either source may be used without changing the
exponent, provided the adjoint/normal orientation is retained.

## 3. Exact finite packet and partition

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

Every coefficient tuple has:

- an exact signed coefficient;
- a fixed variable order;
- a deterministic first-crossing Type-I/Type-II label;
- factor-scale intervals;
- a reduced-complexity or terminal Type-I flag;
- a finite auxiliary packet destination.

For fixed `K`, the combinatorial destination dictionary is finite. The actual
tuple manifest remains finite and source-bound at every block.

## 4. Exact null-mode mechanism, with cutoff residuals retained

The order-`K+1` boundary zeros of `H_K` annihilate every global pole density

\[
 u^re^{u/2}du,
 \qquad0\le r\le K,
\]

and the matching polynomial constant-density modes. Hence the Laurent principal
part of every **unpartitioned** Heath--Brown summand is in the exact Gram null
space.

For a finite first-crossing packet, however, truncated Möbius variables and
support cutoffs create shifted Heaviside boundaries and compact transition
pieces. They are not automatically global polynomial modes.

Accordingly, a packet companion may be subtracted only after a certificate
proves that it belongs to the declared null space. Every uncancelled transition
source remains inside the packet energy. The zero companion is always legal.

Thus `L-15155/L-15156` complete the null-space algebra and the companion
validation interface. They do **not** pre-prove useful packet companions or
small transition residuals; those are part of `CP(K)`.

## 5. Signed packet grouping and positive auxiliary energies

All tuple contributions sharing one destination type are first recombined across
all identity indices `j` with their exact signed binomial coefficients. Only
then is Gram Cauchy--Schwarz applied.

For each destination `tau`, let `nu_(K,tau,J)` be the complete signed packet
after subtracting a certified null companion, if one is supplied. Define

\[
 E_{K,\tau}(J)
 =\iint K_{J,K+1}(u,v)
 d\nu_{K,\tau,J}(u)d\nu_{K,\tau,J}(v)\ge0.
 \tag{M-15112.5}
\]

The exact recombination gives

\[
 \mathcal B_{J,K}^{\Lambda}
 \le R_K\sum_{\tau\in\mathfrak T_K}E_{K,\tau}(J).
 \tag{M-15112.6}
\]

This closes the **finite auxiliary-vector language** identified by the review.
It does not estimate any component.

## 6. Correct Type-II orientation

Every packet energy is retained in the adjoint/normal form

\[
 \langle H_K,
  \mathcal P_\tau^*\chi_J
  \mathcal P_\tau H_K\rangle.
 \tag{M-15112.7}
\]

For a Type-II split `(A,B)`, the factor variables remain on opposite sides of
the Gram. The packet is never replaced by a product-dilation channel.

PR #216's balanced semiprime identity is the ordinary-prime member of this
normal family. `L-15154` supplies the exact bridge to the full-von-Mangoldt
normal family used by the Heath--Brown identity.

## 7. Required analytic treatment of every packet class

### 7.1 Signed-packet preservation

Rows sharing a destination are combined with their exact binomial signs before
any total variation, Cauchy--Schwarz, or large-sieve step.

### 7.2 Reduced-complexity Type I

A reduced-complexity Type-I packet records:

1. a small factor packet at scale at most `delta_KJ+O_K(1)`;
2. a genuinely simpler large coefficient word;
3. an admissible null companion, if constructed;
4. every shifted-boundary transition residual;
5. a normal auxiliary-energy destination.

### 7.3 Terminal Type I

A terminal Type-I packet is not declared lower complexity. It must receive a
direct source-bound estimate or a genuine strict-scale destination in the
auxiliary system.

### 7.4 Type II

A Type-II packet records two factor groups at strict fractional scales. Its
factor-ratio Gram may be estimated by a tensor auxiliary energy, provided the
logarithmic scale weights satisfy the contraction condition in `T-15121`.

### 7.5 Divisor/log and cutoff rows

Rows involving unrestricted `1` and `log` factors retain their complete
transition ledger. Any Euler--Maclaurin, hyperbola-boundary, or cutoff remainder
is a named auxiliary component and may not be declared polynomial without a
proof.

## 8. Load-bearing centered packet estimate

For each fixed `K`, the proposed analytic theorem is:

> **CP(K).** The complete signed packet vector of `L-15156`, including useful
> companion construction, transition residuals, terminal Type-I rows, and all
> Type-II tensor packets, satisfies a linear or tensor strict-scale-contraction
> recurrence with coefficient rate `epsilon_K`, contraction reserve `delta_K`
> (or `1-kappa_K`), and
> \[
> {\epsilon_K\over\delta_K}\to0
> \quad\text{or}\quad
> {\epsilon_K\over1-\kappa_K}\to0
> \qquad(K\to\infty).
> \tag{M-15112.8}
> \]

A representative linear row bound is

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

with the tensor alternative of `T-15122` permitted.

`CP(K)` is the sole unproved arithmetic theorem in this proposal.

## 9. Deduction of RH

Assume `CP(K)` for an unbounded sequence of orders satisfying (M-15112.8).
`T-15122` gives

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

The window varies with `K`, but every finite window detects the same invariant
because all additional transform zeros remain on the boundary lines.

## 10. Finite proof-object schema

A certificate for one order and block contains:

```text
K, X, V, window SHA-256
complete Lambda and truncated-Mobius manifests
exact Heath-Brown tuple rows
signed binomial coefficient packets
first-crossing Type-I/II partition
Type-I terminal/reduced-complexity flags
certified null companions
uncancelled transition residuals
centered normal Gram packets
auxiliary-energy identifiers
factor-scale intervals
linear/tensor recurrence coefficients
coefficient exponent epsilon_K
scale reserve delta_K or kappa_K
```

The checker rejects:

- total variation before signed-packet recombination;
- a companion outside the declared null space;
- deletion of a transition or cutoff residual;
- product-dilation/factor-ratio substitution;
- an undeclared auxiliary or terminal Type-I packet;
- a missing prime-power or endpoint tuple;
- a scale destination exceeding the declared contraction;
- inference from finitely many orders to RH.

## 11. What is and is not completed

Completed exactly in this pass:

1. prime/full-von-Mangoldt polynomial block equivalence;
2. the correct normal-operator bridge;
3. arbitrary-order compact safe windows and their null-mode quotient;
4. the exact finite Heath--Brown coefficient, tuple, and multiplicity ledger;
5. a deterministic Type-I/Type-II partition;
6. signed destination-packet grouping;
7. a finite auxiliary-energy schema with terminal flags;
8. scalar, vector, tensor, and increasing-order scale-contraction composition.

Still proposed:

\[
 \boxed{CP(K),}
\]

including useful companion construction, transition estimates, terminal Type-I
bounds, centered Type-II packet estimates, and the vanishing coefficient-rate
limit.

Thus this is a robust full proposal with one explicit analytic packet theorem as
its independent-review hinge. It is not a completed proof of RH.
