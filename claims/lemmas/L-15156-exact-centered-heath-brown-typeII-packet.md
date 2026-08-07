# L-15156 — Exact centered Heath--Brown Type-II packet

Claim ID: `L-15156`  
Title: A finite truncated Heath--Brown identity, high-order safe centering, and a deterministic first-crossing partition give a closed finite row dictionary for the normal prime-energy problem  
Status: **PROPOSED EXACT ALGEBRAIC CONSTRUCTION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15154`, `L-15155`  
Scope: exact finite decomposition and row schema; the final centered row estimates remain proposed in `M-15112`

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

## 3. Explicit row tuples

The `j`-th row expands over tuples

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

Fix once and for all the lexicographic ordering

\[
 d_1,\ldots,d_j,q,r_1,\ldots,r_{j-1}.
 \tag{L-15156.10}
\]

The tuple list, coefficient, endpoint convention, and ordering are all finite
and source-bindable.

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

Let `B=n/A`.

There are exactly two cases.

### Type II

If

\[
 A\le e^{(1-\delta_K)J+C_H}
 \quad\text{and}\quad
 B\le e^{(1-\delta_K)J+C_H},
 \tag{L-15156.14}
\]

retain the ordered factor split `(A,B)` as a balanced Type-II row.
Both factor groups live at a strict fraction of the output logarithmic scale,
up to the fixed support slack.

### Type I

Otherwise one group is smaller than

\[
 e^{\delta_KJ+C_H}
 \tag{L-15156.15}
\]

and the complementary group is declared the large Type-I variable.

The dichotomy is exhaustive by construction. There is no informal choice of a
“balanced” factorization after an estimate has been applied.

For fixed `K`, the identity row, stopping location, Type-I/II label, coefficient
word, and factor-group types range over a finite dictionary `mathfrak T_K`.

## 5. High-order rowwise centering

The Dirichlet series of the `j`-th identity row is

\[
 M_V(s)^j[-\zeta'(s)]\zeta(s)^{j-1}.
 \tag{L-15156.16}
\]

Its pole at `s=1` has order at most `j+1<=K+1`. Choose the high-order safe
window

\[
 H_K=H^{[K+1]}
 \tag{L-15156.17}
\]

from `L-15155`. Its block kernel annihilates every density

\[
 u^re^{u/2}du,
 \qquad0\le r\le K,
 \tag{L-15156.18}
\]

and also the corresponding polynomial constant-density modes at the second
boundary.

For each exact dictionary row `tau in mathfrak T_K`, let `rho_tau` be the
inverse Laurent polynomial of that row at the pole `s=1`. Then

\[
 \rho_\tau\in\mathcal N_{K+1},
 \tag{L-15156.19}
\]

and the centered row source is

\[
 d\nu_\tau=d\mu_\tau-d\rho_\tau.
 \tag{L-15156.20}
\]

By `L-15155`, every row may be centered independently, even though the Laurent
polynomials cancel only after the signed Heath--Brown rows are recombined.

This closes the rowwise-centering objection in the latest review.

## 6. Finite auxiliary row energies

For each row type `tau`, define

\[
 \boxed{
 E_{K,\tau}(J)
 =\iint K_{J,K+1}(u,v)
 d\nu_\tau(u)d\nu_\tau(v)\ge0.}
 \tag{L-15156.21}
\]

Let `R_K=|mathfrak T_K|`. The exact recombination and Gram Cauchy--Schwarz give

\[
 \boxed{
 \mathcal B_{J,K}^{\Lambda}
 \le R_K\sum_{\tau\in\mathfrak T_K}
 E_{K,\tau}(J).}
 \tag{L-15156.22}
\]

Here `B_(J,K)^Lambda` is the full-von-Mangoldt block energy for the safe window
`H_K`.

Thus the Type-II problem is not required to close under the single prime-block
family. It closes under the finite vector

\[
 \mathbf E_K(J)
 =(E_{K,\tau}(J))_{\tau\in\mathfrak T_K}.
 \tag{L-15156.23}
\]

The ordinary-prime energy has the same polynomial and subexponential status by
`L-15154`.

## 7. Exact destination of every row

The finite dictionary records, for every `tau`:

```text
identity order j
binomial sign and multiplicity
ordered coefficient word
large/small or balanced factor split
pole Laurent polynomial
centered source measure
output window H_K
source and factor support intervals
auxiliary energy component
```

Type-I rows are tagged by:

1. their small factor packet, supported below `exp(delta_K J+C_H)`;
2. the strictly lower convolution complexity of the large factor word.

Type-II rows are tagged by two factor packets whose logarithmic scales are at
most

\[
 (1-\delta_K)J+C_H.
 \tag{L-15156.24}
\]

Consequently a proposed estimate can be checked against the finite-vector or
tensor scale-contraction hypotheses of `T-15121`. No row is allowed to disappear
under the phrase “standard Type II.”

## 8. Exact open centered packet estimate

The remaining arithmetic assertion is now the following finite-family estimate.
For every fixed `K`, prove that each row satisfies either

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

or the tensor variant of `T-15121`, with

\[
 \log(1+a_{K,\tau}(J))=o(J),
 \qquad
 \log(1+b_{K,\tau\upsilon}(J))=o(J).
 \tag{L-15156.26}
\]

Equation (L-15156.25) is source-specific, centered row by centered row, and
strictly scale-contracting. Its proof is the Type-II analytic hinge of the new
proposal.

## 9. Proof boundary

Closed exactly:

- the finite Heath--Brown coefficient identity;
- the full tuple and multiplicity ledger;
- a deterministic Type-I/Type-II partition;
- rowwise high-order centering;
- a finite positive auxiliary-energy vector;
- exact row destinations and a proof-producing schema.

Open:

- the centered row estimates (L-15156.25)--(L-15156.26);
- the resulting RH conclusion.

Thus the Type-II bookkeeping and closure language are complete; the analytic
centered packet estimate remains the sole proposed arithmetic theorem.
