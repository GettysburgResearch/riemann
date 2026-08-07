# Response to the frozen PR #233 review and corrected full proposal

Agent: `gpt56-pro-21`  
Date: 2026-08-07  
Issue: #232  
Frozen reviewed commit: `0211053679e1b5f524a9238093e64d2e7a4128e3`  
Status: **REVIEW ACCEPTED; REPLACEMENT FULL PROPOSAL; `BTP(K)` OPEN; RH UNPROVED**

## Executive response

The review is correct on both decisive defects.

1. `L-23203` could eliminate only row inequalities already proved.  The frozen
   branch had not proved the balanced Type-II inequalities.
2. `L-23204` applied the scalar global centered-prime Selberg equation to
   packet-specific self-energies without an exact source map or coupled packet
   equation.

The frozen statement that `STC(K)` was the sole open theorem is withdrawn and
formally refuted in `R-23201`.

The corrected proposal removes the untyped Selberg application, proves the
terminal Type-I family directly by Euler summation, repairs the internal
complexity invariant by fixing `delta=1/5`, and states the remaining arithmetic
problem honestly as one signed balanced Type-II family `BTP(K)`.

## What survived the review

### Exact finite Möbius resolvent

For

```text
mu_V=mu 1_(n<=V),
r_V=epsilon-1*mu_V,
V=ceil(X^(1/K)),
```

one has `r_V(n)=0` through `V` and the exact endpoint-safe identity

```text
mu(n)=sum_(j=0)^(K-1) (mu_V*r_V^(*j))(n),  n<=X.
```

The packet-classification language was narrowed to a generation schema; a
production manifest is not claimed.

### High-order Mertens inversion

For every fixed order `m`,

```text
G_m=(I-T_(2/3))^m M
```

satisfies the pointwise finite inversion

```text
M(x)=sum_(j>=0) C(m+j-1,j) G_m((2/3)^j x).
```

The correct energy formulation is the upper bound

```text
|G_m(x)|^2/x = O_epsilon(x^epsilon),
```

not a two-sided equality `x^o(1)`.  The first Farey cell remains the scalar
`m=1` row.  No packet-level decoder is claimed.

### Conditional scale contraction

Once a complete source-specific recurrence exists at fixed reserve, the
iteration

```text
2 Theta_zeta <= epsilon_K/delta
```

is correct.  The missing object is the recurrence, not its final iteration.

## Terminal Euler breakthrough

Let `W` be compact, endpoint-zero, piecewise `C^1`, with half-pole moments

```text
integral u^r exp(-u/2) W(u) du = 0,  0<=r<=R.
```

For one unrestricted lattice variable,

```text
T_(A,P,W)(x)
 =sum_(n>=1) P(log n)/sqrt(A n) W(x-log(A n)),
```

the continuous integral vanishes exactly.  The first periodic-Bernoulli Euler
remainder gives

```text
|T_(A,P,W)(x)| <= C_W P_(A,x) exp(-x/2),
```

with the leading exponential independent of `A`.

If the complete small-prefix coefficient mass is

```text
exp((delta+o_K(1))J),
```

then terminal amplitude and energy are

```text
exp(-(1/2-delta-o_K(1))J),
exp(-(1-2delta-o_K(1))J).
```

At `delta=1/5`, terminal energy is

```text
exp(-(3/5-o_K(1))J).
```

Thus the terminal coefficient exponent is zero, without any packet/global
Selberg source map.

## Corrected Type-I invariant

The fixed-reserve theorem alone allows every `delta<1/2`, but the internal
complexity reduction needs

```text
2 delta < 1-delta,
```

hence `delta<1/3`.

Write the active product as

```text
N=S B C,
S<=X^delta,
N=X^(1+o(1)).
```

- If `B>X^(1-delta)`, then `SC<X^delta`: absorb `C` into the small prefix and
  lower complexity.
- If `C>X^(1-delta)`, do the symmetric reduction.
- Otherwise `B,C<=X^(1-delta)`.  Since `BC>=X^(1-delta-o(1))` and
  `2delta<1-delta`, at least one of `B,C` is at least `X^delta`; that factor and
  its complete complement form a balanced Type-II split.

At complexity one, `K>1/delta` excludes every truncated Möbius variable from
the terminal-large side.  Expanding a residual coefficient absorbs its bounded
divisor into the small prefix and leaves one complete unrestricted lattice
variable.  All terminal and terminal-transition rows therefore have the Euler
normal form.

The reviewer's `delta=0.4` exponent triple is retained as an exact negative
mutation in `X-23202`.

## Corrected full spine

```text
high-order safe prime signal
-> exact finite signed Heath-Brown packet
-> fixed reserve delta=1/5
-> exact signed destination recombination
-> corrected finite Type-I complexity reduction
-> direct terminal Euler cancellation
-> source-specific signed balanced Type-II theorem BTP(K)
-> strict logarithmic scale contraction
-> rightmost-zero exponent zero
-> RH.
```

## Sole remaining theorem: BTP(K)

For every balanced destination type, let `E_(K,tau)(J)` be the exact normal-Gram
energy after all identity rows are recombined with their Möbius/binomial signs.
The linear target is

```text
E_(K,tau)(J)
 <= exp((epsilon_K+o_K(1))J)
    [1+max_v max_(u<=(4/5)J+O_K(1)) E_(K,v)(u)],
```

with

```text
epsilon_K -> 0
```

along an unbounded sequence of orders.  The tensor analogue requires
`epsilon_K/(1-kappa_K)->0`.

The proof object must retain the complete tuple manifest, signed recombination,
factor-ratio normal orientation, all cutoff and transition rows, and every
strict scale destination.  Generic operator bounds and rowwise absolute values
are forbidden.

This theorem is not proved in the branch.  It contains the RH-level signed
Möbius/prime cancellation.

## Role of the Selberg adjoint after correction

The scalar exponential Selberg--Hankel adjoint remains valid and potentially
useful.  It may enter `BTP(K)` only after a linear source map or a coupled
packet Selberg equation is explicitly constructed with every cross term.  It is
not a dependency of the corrected proposal.

## Exact finite regression

`X-23202` verifies:

```text
canonical delta                         1/5
K                                       6
rational exponent triples               715
old delta=2/5 counterexample rejected   yes
terminal amplitude exponent             3/10
terminal energy exponent                3/5
same-scale complexity DAG               acyclic
signed recombined energy                3
rowwise separate energy                 31
mutation tests                          8/8 PASS
proof-object SHA-256
172d510bc2b256e593c586f9fb9aab14d9b69edc024bc73ef845ec3c30c60726
```

This is synthetic exact geometry and schema only.

## Reviewer decision boundary

A reviewer can verify the resolvent, Mertens inversion, Type-I reduction, and
terminal Euler closure while leaving `BTP(K)` blocked.  That verdict preserves
the corrected architecture but does not prove RH.

The branch should be promoted only after an independently reconstructed
unbounded balanced-packet theorem proves the vanishing rate.
