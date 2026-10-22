# Full-problem attack — prime-power polygon domination

Date: 2026-08-07  
Agent: `gpt56-02-p`  
Frozen launch point: `main` at `a62f74c43a22ee1ed1d06db320ec0006cc91e30b`  
Parallel snapshots inspected during the pass: reverted commits `351c4445a2f6a3c02c33d022fe48dbe0c267aa4c`, `78eec318f654f2b14ec39279c57982320e342367`; draft PR #217 at `b315f74565fbf884564f2f877ae7888b6ee5bc13`; current main through `1f031dae04b2273803073ca047c4c98ba9452739`

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

## Constructive positive recurrence

Let `tau_F=(F*)'` be the explicit reference mass quantile and let
`nu_pp(A)=log q_j` on the mass cell `(A_(j-1),A_j]`. The polygon margin

```text
M_j=B_j-F*(A_j)
```

satisfies exactly

```text
M_j-M_(j-1)
 = integral_(A_(j-1))^(A_j) [nu_pp(A)-tau_F(A)] dA.
```

Thus every prime-power atom receives an equal amount of the continuous
archimedean mass, and its contribution is the barycentric transport surplus.
The positive target is a block transport or integrated-quantile majorization,
not a demand that every prime arrival have the correct sign.

A cofinal block partition proving

```text
sum_block Lambda(q)log(q)/sqrt(q)
 >= integral_matching_mass tau_F(A)dA
```

plus one finite initial and intra-block moat proves RH.

## Cross-route audit

### Phase-complete energy

Reverted draft `351c444...` proposed that the local `L2` growth exponent of one
compact pole-free prime signal is exactly `Theta_zeta`. Subject to review, this
is a valuable positive-energy equivalent and removes sparse phase cancellation
as an excuse. It does not prove the prime-only subexponential energy bound.

### Finite and centered notches

Reverted draft `78eec318...` and PR #217 construct finite and infinite
critical-line notch cascades. The centered product is a natural projector onto
the off-line residual, but the kernel uses the complete line-zero set. Its
positive endpoint remains the exact corrected-prime identity.

The audit found one load-bearing correction in `T-21701.19`: after defining

```text
R_infty=Q_infty-E_infty^known,
```

its Laplace transform must contain `-L E_infty^known`, or the theorem must define
an explicitly renormalized transform. As written, the displayed raw product is
incompatible with the preceding RH implication `R_infty=0`. The correction was
posted directly on PR #217; it does not reject the centered-product layer.

### Hausdorff saddle sector

PR #217 also proposes positivity of every fixed Hausdorff row for sufficiently
large column index. This is a genuine unconditional infinite sector if the
proof passes review. The uniform parabolic extension and moving transition
strip remain open, so fixed-row positivity does not close the full hierarchy or
the polygon margin.

### Semicircle–totient and one-Green work on current main

Current main added a proposed semicircle-smoothed totient observable whose
Mellin denominator poles are `rho-1`, a Bessel–Möbius decomposition, and an
unconditional completely monotone one-Green xi ratio.

These are useful global coordinates:

```text
semicircle error:
  finite Farey/totient observable with the same rightmost-zero exponent;

Bessel-Moebius form:
  direct harmonic-analysis representation of the RH-scale cancellation;

full one-Green ratio:
  unconditional positive arithmetic-archimedean convolution measure.
```

The one-Green positivity does not prove RH. The zero information survives only
after the canonical endpoint/pole-density channel is subtracted. Its arithmetic
factor satisfies

```text
-d/dq log[zeta(1+q)/zeta(1+s+q)]
 = sum Lambda(n)(1-n^-s)/n^(1+q),
```

so it is a safely damped Laplace average of the same prime-power measure used by
the polygon. A successful de-damping/variation-diminishing theorem could bridge
the positive one-Green measure to the undamped quantile transport, but no such
inverse-sign theorem is currently proved.

## Positive attack selected

Three routes remain serious rather than cosmetic:

1. **Block transport:** allocate intervals of the continuous reference mass to
   successive prime-power atoms and prove every cumulative barycentric block
   has nonnegative cost.
2. **Finite Euler curvature:** prove the sharp nonlinear inequality between the
   first two derivatives of the finite triangular Euler exponential at
   `s=1/2`.
3. **Selberg positive square / de-damping:** derive a one-sided convolution
   identity whose exact remainder is the polygon gap plus nonnegative squares,
   or transfer centered one-Green domination to the boundary without losing
   sign.

Generic Cauchy–Schwarz/log-convexity, phase-blind PNT bounds, and unconditional
full-kernel positivity miss the required barrier and cannot close the problem.

## Verification performed

- Independently differentiated the exact archimedean function and checked its
  strict convexity on the full post-first-prime half-line.
- Reconstructed the conjugate polygon and proved the two-sided Fenchel minimax
  identity.
- Derived the exact radial series and one-dimensional tangent formula.
- Derived the exact prime-quantile recurrence and block transport identity.
- Implemented `X-21501` with Fraction-only interval contraction, a rigorous
  geometric series tail, typed production bindings, and seven tests.
- Ran ordinary, explicitly non-directed normalization reconnaissance over all
  18,120 prime powers through `199999`. No negative vertex appeared; the
  smallest observed margin was about `0.02752057335` near `q=3089`. This is not
  a certificate and is not evidence for the cofinal theorem.
- Inspected the parallel phase-energy, finite-notch, centered-notch, Hausdorff,
  semicircle, Bessel–Möbius, and one-Green proposals and preserved their exact
  relation and proof boundaries in `O-21501/O-21502`.

## Honest frontier

This pass does not prove the polygon domination inequality. It does identify a
single full-strength target, a constructive positive transport recurrence, and
a finite counterexample search whose success would settle RH negatively. All
new theorem cards remain `PROPOSED` pending independent review.

## SERIOUS RESOLUTION PATH

Yes. The prime-polygon route is a serious resolution path because it is exactly
equivalent to RH, has a complete finite negative semidecision, and exposes a
positive theorem with no hidden packet-capture or phase quantifier.

The exact missing step is one cofinal proof of

```text
B_j - F*(A_j) >= 0.
```

A block transport, finite-Euler curvature theorem, exact Selberg square, or a
proof-grade de-damping transfer from the centered one-Green measure at this
threshold would finish the proof through `T-21501`. No RH claim is made without
that step.
