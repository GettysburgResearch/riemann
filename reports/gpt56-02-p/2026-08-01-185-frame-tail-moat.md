# Frame–tail moat audit after full complementary capture

Agent: `gpt56-02-p`  
Date: 2026-08-01  
Repository: `gfreund123/riemann`  
Branch: `agent/gpt56-02-p/156-sacrificial-count`

## Executive verdict

The requested cofinal inequality

```text
epsilon_lambda
< B_(T,lambda)+beta_lambda
< Sigma_lambda
```

has not been proved. More importantly, after the actual complement

```text
W_lambda=R_lambda^(perp_GC) intersect U_lambda
```

is known, this two-sided threshold is stronger than necessary and can fail on a
strictly positive finite packet.

The correct direct visible-block quantity is

```text
M_lambda
 =sup_(T,Z)[sigma_(Z,lambda)^2-B_(T,lambda)].
```

If `M_lambda>0`, the actual full complement has a positive harmonic Schur floor.
The radical endpoint belongs in the separate radical-row rate, not in the
visible lower bound.

## Exact scalar algebra

For one finite frame floor `sigma`, omitted-zero budget `B`, and radical endpoint
`epsilon`:

```text
exists beta>0:
  epsilon<B+beta<sigma
iff
  max(epsilon,B)<sigma.
```

The stronger Gaussian schedule

```text
epsilon<=beta/2,
B+beta<sigma
```

is feasible exactly when

```text
B+2epsilon<sigma.
```

The canonical choice is

```text
beta=epsilon+(sigma-B)/2.
```

## Direct restriction

The harmonic lower form satisfies

```text
S_U>=K_T^C-B_T G_C.
```

If the finite simple-line block frames the actual complement by

```text
K_Z^C|W>=sigma_Z^2 G_C|W,
K_T^C>=K_Z^C,
```

then directly

```text
S_U|W>=(sigma_Z^2-B_T)G_C|W.
```

No generalized-eigenvalue count or principal angle is required.

## Exact scope counterexample

For

```text
K_j=diag(1/j,1/j^2),
R=span(e1),
W=span(e2),
B_j=0,
```

one has

```text
epsilon_j=1/j>Sigma_j=1/j^2.
```

The requested beta interval is empty, but the complete form is strictly
positive and the direct visible floor is `1/j^2`.

## Quantitative routes

Two exact conditional routes were isolated.

### Collective compactness

If the normalized full-complement lifts lie in one compact nonzero family in a
topology controlling the complete simple-line evaluation energy, compactness
gives a positive minimum and Dini's theorem extracts one finite uniform frame.

### Rescaled simple-zero profiles

Positive density of simple critical-line zeros gives nonzero diffuse weak limits
for the measures

```text
(R log R)^-1 sum_(R<=gamma<=KR) delta_(gamma/R).
```

If

```text
sqrt(R) Fourier(Jw)(R x)
```

has a collectively compact nonzero holomorphic profile family, then analytic
uniqueness yields

```text
Sigma_R>=c log R
```

along a subsequence. The originally requested threshold would then follow from

```text
B_T+2epsilon=o(log R).
```

The same-end packet has the right scaling. The moving opposite-end phase and the
complete one-sided residual remain unproved.

## Exact replay

Passing control:

```text
sigma=1, B=1/10, epsilon=1/50
beta=47/100
threshold=57/100
counted margin=9/20
direct floor=9/10
```

Direct-only scope control:

```text
sigma=1/4, B=0, epsilon=1/2
requested interval empty
direct floor=1/4
```

Nine Fraction-only tests pass.

## Honest frontier

No production theorem proves

```text
M_lambda>0
```

cofinally, nor the profile/tail package that would imply the stronger displayed
threshold. Under false RH an off-line Xi-cardinal direction remains invisible at
all exact real zeros before localization and carries a fixed negative
Schur-corrected defect. Therefore the residual moat is the substantive
RH-bearing theorem, not finite scalar algebra.
