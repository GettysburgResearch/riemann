# L-15156 — Exact centered Heath--Brown Type-II packet

Claim ID: `L-15156`  
Title: A finite truncated Heath--Brown identity and deterministic first-crossing partition give a source-bound Type-I/Type-II packet dictionary, with exact null-mode centering interfaces  
Status: **PROPOSED EXACT ALGEBRAIC CONSTRUCTION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Updated: 2026-08-07 after self-audit of finite-cutoff companions  
Dependencies: `L-15154`, `L-15155`  
Scope: exact finite decomposition, partition, and centering schema; the useful packet companions and analytic packet estimates remain proposed in `M-15112`

## 1. Truncated Möbius polynomial

Fix an integer identity order

\[
 K\ge2.
 \tag{L-15156.1}
\]

For a finite arithmetic endpoint `X>=2`, put

\[
 V=X^{1/K}
 \tag{L-15156.2}
\]

and define

\[
 \mu_V(n)=\mu(n)\mathbf1_{n\le V}.
 \tag{L-15156.3}
\]

Let `1` denote the constant-one arithmetic function and let `log(n)=log n`.
Dirichlet convolution is written `*`.

## 2. Exact finite Heath--Brown identity

For every integer `n<=X`,

\[
 \boxed{
 \Lambda(n)
 =\sum_{j=1}^{K}
 (-1)^{j-1}{K\choose j}
 \left(
  \mu_V^{*j}*\log*1^{*(j-1)}
 \right)(n).}
 \tag{L-15156.4}
\]

### Proof

Let

\[
 M_V(s)=\sum_{n\le V}{\mu(n)\over n^s}
 \]

and put

\[
 R_V(s)=1-\zeta(s)M_V(s).
 \tag{L-15156.5}
\]

The coefficient of `R_V` is zero for every integer `n<=V`: all divisors of
such an `n` occur in the truncated Möbius sum. Therefore every nonzero
coefficient of `R_V^K` is supported on an integer greater than `V^K=X`.

On the other hand,

\[
 1-R_V(s)^K
 =\sum_{j=1}^K(-1)^{j-1}{K\choose j}
  [\zeta(s)M_V(s)]^j.
 \tag{L-15156.6}
\]

Multiplication by

\[
 -{\zeta'\over\zeta}(s)
 \]

turns the `j`-th summand into the Dirichlet series of

\[
 \mu_V^{*j}*\log*1^{*(j-1)}.
 \]

Since the factor `R_V^K` has no coefficient at `n<=X`, coefficient comparison
gives (L-15156.4). QED.

This is an exact finite identity, not an asymptotic Vaughan approximation.

## 3. Explicit coefficient tuples

The `j`-th summand expands over tuples

\[
 \mathbf t=(d_1,\ldots,d_j;
             r_1,\ldots,r_{j-1};q)
 \tag{L-15156.7}
\]

with

\[
 d_i\le V,
 \qquad
 d_1\cdots d_jr_1\cdots r_{j-1}q=n.
 \tag{L-15156.8}
\]

Its coefficient is

\[
 \boxed{
 c_{K,j}(\mathbf t)
 =(-1)^{j-1}{K\choose j}
  \mu(d_1)\cdots\mu(d_j)\log q.}
 \tag{L-15156.9}
\]

Fix once and for all the variable ordering

\[
 d_1,\ldots,d_j,q,r_1,\ldots,r_{j-1}.
 \tag{L-15156.10}
\]

For fixed `K`, the **combinatorial types** of coefficient word and stopping
position form a finite dictionary. The actual tuple list at block `J` is finite
but depends on the endpoint `X` and therefore is not asserted to be independent
of `J`.

## 4. Deterministic Type-I/Type-II partition

Let the compact window have support width `C_H`. At output block `J`, every
nonzero tuple satisfies

\[
 e^{J-C_H}\le n\le e^{J+C_H}.
 \tag{L-15156.11}
\]

Fix

\[
 0<\delta_K<{1\over2K}.
 \tag{L-15156.12}
\]

Traverse the ordered variables in (L-15156.10) and stop at the first partial
product `A` satisfying

\[
 A\ge e^{\delta_KJ}.
 \tag{L-15156.13}
\]

If no partial product crosses before the final variable, stop at the final
variable. Put

\[
 B=n/A.
\]

There are exactly two declared cases.

### Type II

If

\[
 A\le e^{(1-\delta_K)J+C_H}
 \quad\text{and}\quad
 B\le e^{(1-\delta_K)J+C_H},
 \tag{L-15156.14}
\]

retain the ordered factor split `(A,B)` as a Type-II packet. Both factor groups
live at a strict fraction of the output logarithmic scale, up to the fixed
support slack.

### Type I

Otherwise one factor group is smaller than

\[
 e^{\delta_KJ+C_H}.
 \tag{L-15156.15}
\]

It is declared the small Type-I packet and the complementary group the large
variable.

A Type-I packet receives one of two additional flags:

1. `reduced-complexity`, when removing the small packet strictly lowers the
   remaining convolution word;
2. `terminal`, when the small packet is trivial or the complementary word has
   not decreased in complexity and must therefore receive an independent
   direct estimate.

The partition is exhaustive and deterministic. No term is assigned to a
convenient factorization after an estimate has been applied.

## 5. What high-order centering proves exactly

The unpartitioned `j`-th Heath--Brown summand has Dirichlet series

\[
 M_V(s)^j[-\zeta'(s)]\zeta(s)^{j-1}.
 \tag{L-15156.16}
\]

Its Laurent principal part at `s=1` has order at most `j+1<=K+1`. Choose

\[
 H_K=H^{[K+1]}
 \tag{L-15156.17}
\]

from `L-15155`. Its block kernel annihilates every global pole density

\[
 u^re^{u/2}du,
 \qquad0\le r\le K,
 \tag{L-15156.18}
\]

and the corresponding polynomial constant-density modes at the second boundary.

Therefore the **global Laurent principal part** of every unpartitioned
Heath--Brown summand lies in the exact null space of the Gram.

This statement must not be confused with a full estimate for a finite partition
packet. Truncating Möbius factors and imposing first-crossing cutoffs creates
shifted Heaviside boundaries and compact transition pieces. Those are not in
general global polynomial densities. For a partition packet `tau`, a proposed
companion `rho_tau` is admissible only after a certificate proves

\[
 \rho_\tau\in\mathcal N_{K+1}.
 \tag{L-15156.19}
\]

Once that membership is proved, `L-15155` gives exact invariance under
subtraction of `rho_tau`. Any remaining cutoff or transition source must stay in
the centered packet and be estimated; it may not be discarded as a null mode.

Thus the high-order null quotient closes the **algebraic centering mechanism**.
Constructing useful packet companions and bounding their transition residuals
remain part of the analytic packet theorem `CP(K)`.

## 6. Signed packet grouping before Gram bounds

Let `mathfrak T_K` be the finite set of destination types consisting of:

```text
first-crossing position
Type-I / Type-II label
Type-I reduced-complexity / terminal flag
ordered factor-word types
factor-scale intervals
window and cutoff type
```

For one output block, combine **all** tuple contributions across all
Heath--Brown indices `j` having the same destination label, with their exact
signed binomial coefficients, before applying Cauchy--Schwarz. Denote the
resulting signed source packet by

\[
 d\mu_{K,\tau,J}.
 \tag{L-15156.20}
\]

If an admissible companion `rho_(K,tau,J) in N_(K+1)` has been supplied, put

\[
 d\nu_{K,\tau,J}
 =d\mu_{K,\tau,J}-d\rho_{K,\tau,J}.
 \tag{L-15156.21}
\]

Otherwise take `rho=0` and retain the whole source.

Define the packet self-energy

\[
 \boxed{
 E_{K,\tau}(J)
 =\iint K_{J,K+1}(u,v)
 d\nu_{K,\tau,J}(u)d\nu_{K,\tau,J}(v)\ge0.}
 \tag{L-15156.22}
\]

Exact recombination and Gram Cauchy--Schwarz give

\[
 \boxed{
 \mathcal B_{J,K}^{\Lambda}
 \le R_K\sum_{\tau\in\mathfrak T_K}E_{K,\tau}(J),}
 \tag{L-15156.23}
\]

where `R_K=|mathfrak T_K|` is finite for fixed `K`.

The grouping requirement is load-bearing: separating the `j`-summands by total
variation before forming the packets may spend the signed binomial cancellation
and is not licensed by this lemma.

The ordinary-prime energy has the same polynomial and subexponential status by
`L-15154`.

## 7. Exact destination ledger

For every packet type `tau`, the source-bound dictionary records:

```text
all contributing identity indices j
signed binomial coefficient vector
ordered coefficient words
first-crossing positions
Type-I/II label and Type-I terminal flag
factor support intervals
admissible null companion, if any
uncancelled transition residual
output window H_K
auxiliary self-energy identifier
```

Type-II packets have two factor groups whose logarithmic scales are at most

\[
 (1-\delta_K)J+C_H.
 \tag{L-15156.24}
\]

Reduced-complexity Type-I packets have a small group below
`delta_K J+O_K(1)` and a strictly simpler large word. Terminal Type-I packets
are retained as separate auxiliary components requiring a direct bound.

Consequently every coefficient tuple has a declared destination. This is a
proof-producing schema, not an analytic estimate.

## 8. The exact open centered packet theorem

For every fixed `K`, `CP(K)` must prove all of the following.

### 8.1 Companion and transition ledger

For every packet, either:

1. construct a source-bound companion in `N_(K+1)` and retain all transition
   residuals; or
2. take the zero companion and estimate the complete packet.

### 8.2 Signed-packet preservation

All `j`-summands assigned to the same packet are recombined with their exact
signed coefficients before any absolute value or Gram Cauchy--Schwarz step.

### 8.3 Closed auxiliary estimates

Each packet must satisfy a linear or tensor recurrence in the finite auxiliary
system. A linear target is

\[
 \boxed{
 E_{K,\tau}(J)
 \le a_{K,\tau}(J)
 +\sum_{\upsilon\in\mathfrak T_K}
 b_{K,\tau\upsilon}(J)
 \max_{k\le(1-\delta_K)J+C_H}
 E_{K,\upsilon}(k),}
 \tag{L-15156.25}
\]

with the terminal Type-I packets either included in the sum with a genuine
strict-scale destination or bounded by an explicitly declared source term.
The tensor alternative is the one in `T-15121/T-15122`.

### 8.4 Coefficient rates

The coefficient rates must satisfy the quantitative condition in `T-15122`,
for example

\[
 {\varepsilon_K\over\delta_K}\longrightarrow0.
 \tag{L-15156.26}
\]

Equations (L-15156.25)--(L-15156.26), including companion construction and
signed packet preservation, are the Type-II analytic hinge.

## 9. Proof boundary

Closed exactly:

- the finite Heath--Brown coefficient identity;
- the complete tuple and multiplicity ledger;
- a deterministic first-crossing Type-I/Type-II partition;
- the high-order null-mode space;
- the rule for admissible packet companions;
- signed packet grouping before Gram bounds;
- a finite positive auxiliary-energy schema;
- an exact destination or terminal flag for every tuple.

Open:

- construction of useful companions for the cutoff packets;
- control of their shifted-boundary transition residuals;
- direct estimates for terminal Type-I packets;
- the centered packet recurrences and coefficient-rate limit;
- RH.

Thus the Type-II bookkeeping and review interface are complete. The analytic
centered packet theorem remains the sole proposed arithmetic completion.
