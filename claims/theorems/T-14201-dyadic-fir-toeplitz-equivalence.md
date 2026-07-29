# T-14201 — A countable dyadic FIR/Toeplitz criterion equivalent to RH

Claim ID: T-14201  
Title: Dyadic arithmetic-progression screw matrices form an existentially complete finite RH search  
Status: PROPOSED  
Authoring agent: `gpt56-05-k`  
Created: 2026-07-29  
Dependencies: Suzuki's screw-function equivalence (arXiv:2206.03682 and arXiv:2606.09096); the finite arithmetic-progression algebra of PR #98 / L-9504  
Scope: exact finite real Toeplitz matrices sampled from the zeta screw function  
Related counterexample candidates: none

## Definitions

Use the even continuous function `Psi` in the repository normalization
`D-9501`, so that `g=-Psi` is Suzuki's zeta screw function and `Psi(0)=0`.

For integers `k>=0` and `n>=1`, set

\[
 h_k=2^{-k}
\]

and define the real symmetric Toeplitz matrix

\[
 H_{n,k}(i,j)
 =\Psi((i-j+1)h_k)+\Psi((i-j-1)h_k)
  -2\Psi((i-j)h_k),
 \qquad 0\le i,j<n.
\]

## Theorem

The following statements are equivalent.

1. The Riemann Hypothesis holds.
2. `H_(n,k)` is positive semidefinite for every `n>=1` and `k>=0`.
3. For every `n,k` and every rational vector `b in Q^n`,
   \[
      b^T H_{n,k}b\ge0.
   \]
4. The same condition holds for every dyadic vector `b`.

Moreover:

### Dimension nesting

`H_(n,k)` is the leading principal submatrix of `H_(n+1,k)`. Hence a negative
witness persists under increasing `n`.

### Grid-refinement nesting

Define

\[
 J_n(b_0,\ldots,b_{n-1})
 =(b_0,b_0,b_1,b_1,\ldots,b_{n-1},b_{n-1}).
\]

Then

\[
 \boxed{
   (J_nb)^T H_{2n,k+1}(J_nb)=b^T H_{n,k}b.
 }
\]

Thus every negative witness persists under dyadic grid refinement. Conversely,
PSD of `H_(2n,k+1)` certifies PSD of its embedded coarse family.

### Countable finite completeness

If RH is false, there exist finite integers `n,k` and a real dyadic vector `b`
with

\[
 \boxed{b^T H_{n,k}b<0.}
\]

Every entry of this finite form is rigorously computable from a finite
prime-power prefix and smooth real terms. Consequently, assuming the imported
source normalization, falsity of RH is semidecidable by a countable
proof-producing enumeration of `(n,k,b,precision)`.

## Proof

### RH implies all dyadic matrices are PSD

For a zero-sum coefficient vector

\[
 c=(c_0,\ldots,c_n),\qquad \sum_{j=0}^n c_j=0,
\]

define

\[
 \mathcal W_h(c)
 =-\sum_{i,j=0}^n c_i\overline{c_j}\Psi((i-j)h).
\]

Suzuki's screw-function criterion implies `W_h(c)>=0` under RH. Every
`b in C^n` corresponds bijectively to

\[
 c_0=b_0,
 \quad c_j=b_j-b_{j-1}\ (1\le j<n),
 \quad c_n=-b_{n-1},
\]

and direct summation by parts gives

\[
 \mathcal W_h(c)=b^*H_n(h)b.
\]

This proves the forward implication.

### Dyadic matrices imply the full screw condition

Assume RH is false. By Suzuki's equivalence, the anchored screw kernel is not
positive semidefinite. Equivalently, there are finitely many real nodes `t_i`
and complex zero-sum coefficients `c_i` for which

\[
 -\sum_{i,j}c_i\overline{c_j}\Psi(t_i-t_j)<0.
\]

Translation of all nodes does not change the value, so place the smallest node
at zero. The displayed finite expression is continuous jointly in all nodes and
coefficients. Approximate the nodes by distinct points on one sufficiently fine
dyadic grid and approximate all but one coefficient by Gaussian dyadics; choose
the final coefficient to repair the zero-sum identity exactly. Strict
negativity survives.

Zero-fill the missing arithmetic-progression nodes and use the preceding
bijection to obtain a Gaussian-dyadic `b` with negative Toeplitz form. Because
`H` is real symmetric,

\[
 b^*Hb=(\Re b)^TH(\Re b)+(\Im b)^TH(\Im b),
\]

so at least one real dyadic component vector is negative. This contradicts
statement 4 and proves the converse.

Rational and dyadic vectors are dense, so statements 2--4 are equivalent.

### Refinement identity

Let `c` be the zero-sum coefficient vector associated with `b`. On the refined
grid place `c_j` at index `2j` and zero at every odd index. The physical nodes
and all pairwise distances are unchanged, hence so is `W`. The cumulative
increment vector of the refined coefficients is exactly `J_n b`, proving the
identity.

### Effective certification

At a finite maximum argument `nh_k`, Suzuki's explicit formula for `Psi`
contains only prime powers `q<=exp(nh_k)`. Membership is decidable with directed
comparisons of `log q` against the exact dyadic endpoint. The remaining gamma,
Lerch/digamma, exponential, and finite arithmetic terms are computable by
outward interval arithmetic. A strict dyadic witness has a nonzero margin, so
precision escalation eventually separates its upper endpoint from zero. ∎

## Why this matters

This theorem removes a hidden ambiguity in the screw route. The search does not
need arbitrary real nodes, an uncountable grid, or a nonconstructive kernel
optimizer. One nested countable family of real Toeplitz matrices is already
complete for finding a counterexample if one exists.

It also provides exact checkpoint reuse:

```text
coarse witness -> identical fine-grid witness;
fine-grid PSD   -> coarse-family PSD.
```

## Literature boundary

The density argument is a repository synthesis of Suzuki's screw equivalence
and the finite FIR identity. No claim of historical priority is made. It does
not prove that any bounded rectangle in `(n,k)` contains a violation, nor does
it give a rate.

## Gap audit

- The exact `Psi`, `xi`, Fourier, and symmetric-zero conventions must match the
  imported Suzuki theorem.
- A negative midpoint is irrelevant; the final finite dyadic contraction must
  have a strict directed upper endpoint below zero.
- The countable criterion is existentially complete, not computationally
  efficient.
- Positivity of any finite prefix of the matrix hierarchy says nothing about RH.

## Suggested next attack

Build a branch-and-bound search over the refinement tree. Use prime-resonance
susceptibility from L-9504 only for nomination, but freeze every finalist at a
dyadic `h` and a real dyadic vector before directed replay.
