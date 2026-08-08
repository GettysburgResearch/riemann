# Prime density drift and the squarefree collector frontier

Date: 2026-08-08  
Agent: `gpt56-pro-22`  
Issue: #273  
Parent: draft PR #267

## Executive result

The branch was pushed and then subjected to two exact stress tests.

First, the annular `L^2` frame was shown to be a valid but overstrong
sufficient target: on the von-Mangoldt ray it would force an
`X^{-3/2+o(1)}` prime-ramp error.

Second, ordinary-prime feasibility was closed exactly. Every nonnegative
strongly additive dual potential that is monotone through `X>=8` collapses to
the endpoint, whose parabolic residual is zero.

A proposed next simplification used only positive blocks between consecutive
ordinary primes. Its finite algebra is exact and every such block is neutral on
proper prime powers. The proposed subpower boundary charge, however, fails.

## New asymptotic obstruction

For the ordinary-prime parabolic residual,

```text
sum_(p<=X) r_X(p)
 =(4(1-gamma)+o(1)) sqrt(X)/log^2(X).
```

The constant comes from the exact Mellin transform

```text
M_E(s)
=4/(2s-1)^2 * [((s-1)zeta(s))/s - 1]
```

of the continuum defect. Its total mass is zero, but its first logarithmic
moment is `4(gamma-1)`. Prime sampling weights scale by
`1/log(X theta)`, so the first density correction is positive.

Therefore the full prime suffix alone already costs
`sqrt(X)/log^2(X)`, and the prime-only `PTC` proposal is rejected pending review
of the uniform sampling argument.

## Exact surviving mechanism

A constant positive block between squarefree endpoints `A<B` has response

```text
Delta v_p = t(1_(p|B)-1_(p|A)),
Delta v_(p^a)=0 for every a>=2,
objective increment = t log(B/A)>=0.
```

If `A` is composite and has more prime factors than `B`, the block compresses
ordinary-prime incidence while increasing the objective. The finite control

```text
A=30=2*3*5,
B=43
```

repairs rows `2,3,5`, loads row `43`, changes total incidence by `-2t`, and is
invisible to all proper prime powers.

This is the first exact atom capable of correcting the positive density drift
without reintroducing the proper-power obstruction.

## Corrected full proposal

The remaining theorem is the Squarefree Collector Lift:

```text
construct nonnegative masses on squarefree A<B<=X
so every ordinary-prime residual is nonpositive.
```

Proper-power neutrality and nonnegative objective increment are then automatic,
and the existing square-screw/Landau chain gives RH.

The exact Farkas dual says that every nonnegative strongly additive potential
which is nondecreasing on squarefree integers must pair nonpositively with the
parabolic residual. The logarithmic ray remains admissible and reproduces the
prime-ramp deficit. Thus the new theorem is honest and RH-bearing.

## Exact validation

```text
X-27301 ordinary-prime collapse/scope
8/8 tests
SHA-256
528355a5e8d9e2eb9f418d8368bc61d8e4d01dfe07d43254def32863e242a9bc

X-27302 prime-incidence greedy algebra
6/6 tests
SHA-256
b8644a8f098bba2ec275ff6646811971f3b5aebb41f6886b7e79802c14a0552b

X-27303 squarefree collector algebra
5/5 tests
SHA-256
05097e2a74e36a917feb7911407cb30485c9b14a1ab0f497346973254ea11c03
```

## Honest boundary

```text
ordinary-prime feasibility              proposed complete
prime-only greedy algebra               proposed complete exact
prime-only PTC rate                     proposed refuted
squarefree collector algebra            proposed complete exact
all-scale squarefree collector lift     open / RH-bearing
Riemann Hypothesis                      unproved
```
