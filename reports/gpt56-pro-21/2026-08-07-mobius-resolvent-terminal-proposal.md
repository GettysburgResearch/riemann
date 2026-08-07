# Full proposal — Möbius resolvent terminal contraction

Agent: `gpt56-pro-21`  
Date: 2026-08-07  
Issue: #232  
Base: PR #158 at `9ee33527aef3acbb281ebad367aeb1e51652d006`  
Status: **FULL PROPOSAL; `STC(K)` OPEN; RH UNPROVED**

## Executive conclusion

The failed PR #231 proof tried to control every critical Farey cluster by one
uniform operator estimate. The first-cell decoder on PR #229 proves why that
cannot work: a single coherent row is exactly a fixed-ratio Mertens increment
and already carries the full RH burden.

The best review-efficient proposal is therefore not another generic
local-to-Bohr operator. It is:

```text
high-order compact safe prime window
-> exact finite centered Heath-Brown packet
-> fixed-reserve Type-I/Type-II partition
-> exact null-mode quotient
-> signed packet recombination
-> well-founded elimination of all nonterminal rows
-> finite terminal Selberg-Hankel certificates STC(K)
-> eta_K -> 0 at fixed scale reserve
-> rightmost-zero exponent zero
-> RH.
```

The new exact Möbius resolvent gives an independent scalar audit of the same
terminal arithmetic.

## New exact contributions

### Finite Möbius resolvent

With

```text
mu_V=mu 1_(n<=V),
r_V=epsilon-1*mu_V,
V=ceil(X^(1/K)),
```

one has `r_V(n)=0` through `V` and

```text
mu(n)=sum_(j=0)^(K-1) (mu_V*r_V^(*j))(n)
```

for every `n<=X`.

This is a finite inverse-zeta packet with no endpoint remainder.

### High-order first-cell hierarchy

For `c=2/3` and every fixed `m`,

```text
G_m=(I-T_c)^m M
```

satisfies

```text
M(x)=sum_(j>=0) C(m+j-1,j) G_m(c^j x),
```

pointwise as a finite sum. Hence square-root control of any one finite order is
equivalent to RH. The first critical Farey cell is the `m=1` row.

### Fixed reserve and terminal reduction

`L-15157` supplies one fixed `0<delta<1/2` independent of the identity order.
A finite scale/complexity induction eliminates all reduced-complexity packet
rows. Balanced rows route below `(1-delta)J+O_K(1)`. The only independent
arithmetic source is the explicit finite terminal Type-I family.

### Positive terminal adapter

For every terminal kernel, a finite positive mixture of the explicit Selberg
exponential adjoints gives an exact upper bound once the Loewner, forcing,
linear-reserve, and lower-scale residual ledgers pass. This is `STC(K)`.

## Why this is preferable to the other full proposals

- It retains the orientation-correct prime Gram of PR #216/#158.
- It uses the exact finite Heath-Brown tuple ledger already present on PR #158.
- It uses PR #158's fixed scale reserve, so only `eta_K -> 0` is needed.
- It incorporates the positive exponential adjoints of PR #229.
- It treats the first-cell Mertens increment as a mandatory test.
- It does not rely on the determinant divisibility asserted by PR #165.
- It does not retry the generic operator bound refuted on PR #231.
- It narrows the broad `CP(K)` obligation to one finite terminal family.

## Sole open theorem

For an unbounded sequence of orders `K`, construct source-bound certificates
for every terminal type such that

```text
T_K(J)
 <= exp((eta_K+o_K(1))J)
    [1+max_(u<=(1-delta)J+O_K(1)) M_K(u)]
```

for one fixed `delta>0`, with

```text
eta_K -> 0
```

or the tensor analogue.

A production certificate must include the actual positive exponential mixture,
kernel domination, Selberg forcing, linear transport reserve, transition
residuals, and the first-cell Mertens mutation.

This theorem is not proved in the current branch. It is the single review hinge.

## Exact regression

`X-23201` verifies:

```text
finite Möbius resolvent mismatches      0
geometric-difference inversion checks  1000
terminal kernel energy                  2
positive Hankel energy                  4
Selberg forcing minus reserve           4
complexity-DAG closed value             92
tests                                   6/6 PASS
proof-object SHA-256
611f6dcf0dc450e58209b078cf0596d634d8d01b4ccb58f28e57d16085aa1911
```

The regression is synthetic exact algebra only.

## Reviewer decision boundary

A reviewer can accept all exact algebra while rejecting `STC(K)`. Such a
verdict leaves the proposal structurally useful but does not prove RH.

The proposal should be promoted only after an independently reconstructed
unbounded terminal-certificate family proves `eta_K -> 0` and passes the
first-cell Mertens mutation.
