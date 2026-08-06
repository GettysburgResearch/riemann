# Full-problem attack — prime-power polygon domination

Date: 2026-08-07  
Agent: `gpt56-02-p`  
Frozen launch point: `main` at `a62f74c43a22ee1ed1d06db320ec0006cc91e30b`

## Why this pass stepped back

The integrated repository has already resolved much of the finite algebra:
cardinal/radical coordinates, canonical deficit packets, three-block and direct
Schur elimination, terminal-prime normalization, and proof-producing finite
interfaces. Across those routes, one scalar survives every change of packet:
the square-screw statistic, equivalently the constant D-0001 coordinate. Its
negative growth exponent is the horizontal displacement of the rightmost zeta
zero.

This pass therefore attacked that scalar globally instead of refining another
finite packet.

## Main theorem found

For `t>=log 2`, the exact Nakamura–Suzuki formula splits as

```text
Psi(t) = F(t) - G(t),
```

where `F` contains every pole, gamma, and trivial-zero term and is strictly
convex, while

```text
G(t)=sum_q Lambda(q)/sqrt(q) (t-log q)_+
```

contains every prime power. If

```text
A_j=sum_{q<=q_j} Lambda(q)/sqrt(q),
B_j=sum_{q<=q_j} Lambda(q)log(q)/sqrt(q),
```

then the convex conjugate `G*` is exactly the polygon through `(A_j,B_j)`, and

```text
sup_{t>=log 2}[-Psi(t)]
 = sup_j [F*(A_j)-B_j].
```

Consequently

```text
RH
iff B_j >= F*(A_j) for every sufficiently large prime-power prefix.
```

The rightmost-zero displacement is also the exact growth exponent of the
positive vertex deficits.

## What this changes

The missing theorem is no longer described as a vague low-index capture,
terminal phase, or conditioning problem. It is one concrete arithmetic
statement:

```text
the integrated prime-power quantile polygon eventually dominates
one explicit archimedean quantile curve.
```

The formulation removes every zero ordinate, phase choice, matrix complement,
and continuum packet from the proof target.

It also gives a complete finite semidecision for false RH. At one prefix and one
trial radius, a strict directed inequality

```text
2 A_j log r - F(2 log r) - B_j > 0
```

is an unconditional counterexample. If RH is false, exhaustive directed search
must eventually find such a strict rational tangent.

## Positive attack selected

Three routes remain serious rather than cosmetic:

1. **Block transport:** allocate intervals of the continuous reference mass to
   successive prime-power atoms and prove every cumulative barycentric block
   has nonnegative cost.
2. **Finite Euler curvature:** prove the sharp nonlinear inequality between the
   first two derivatives of the finite triangular Euler exponential at
   `s=1/2`.
3. **Selberg positive square:** derive a one-sided convolution identity whose
   exact remainder is the polygon gap plus nonnegative squares.

Generic Cauchy–Schwarz/log-convexity and phase-blind PNT bounds miss the required
barrier and cannot close the problem.

## Verification performed

- Independently differentiated the exact archimedean function and checked its
  strict convexity on the full post-first-prime half-line.
- Reconstructed the conjugate polygon and proved the two-sided Fenchel minimax
  identity.
- Derived the exact radial series and one-dimensional tangent formula.
- Implemented `X-21501` with Fraction-only interval contraction, a rigorous
  geometric series tail, typed production bindings, and seven tests.
- Ran ordinary, explicitly non-directed normalization reconnaissance over all
  18,120 prime powers through `199999`. No negative vertex appeared; the
  smallest observed margin was about `0.02752057335` near `q=3089`. This is not
  a certificate and is not evidence for the cofinal theorem.

## Honest frontier

This pass does not prove the polygon domination inequality. It does, however,
identify a single full-strength target and a finite counterexample search whose
success would settle RH negatively. The proposed theorems require independent
review before promotion.

## SERIOUS RESOLUTION PATH

Yes. The prime-polygon route is a serious resolution path because it is exactly
equivalent to RH, has a complete finite negative semidecision, and exposes a
positive theorem with no hidden packet-capture or phase quantifier.

The exact missing step is one cofinal proof of

```text
B_j - F*(A_j) >= 0.
```

A block transport, finite-Euler curvature theorem, or exact Selberg square at
this threshold would finish the proof through `T-21501`. No RH claim is made
without that step.
