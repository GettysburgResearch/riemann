# Session report — the scalar positive-supersolution target is impossible

Agent: `gpt56-05-l`  
Date: 2026-07-31  
Issue: #154  
Branch: `agent/gpt56-05-l/154-nonlocal-barta-floor`

## Requested objective

Construct a cofinal family of positive functions `psi_a` satisfying

```text
ess inf b_(a,psi_a)^odd >= -2 epsilon_a,
a -> infinity,
epsilon_a -> 0.
```

Such a family would have completed the scalar signed-edge Barta route to RH.

## Result

The requested family does not exist.

For every positive admissible scalar `psi`, symmetry of the unsigned edge
measure gives

```text
integral (L_J psi)/psi
 = -1/2 double-integral
   (psi(x)-psi(y))^2/(psi(x)psi(y)) dJ
 <= 0.
```

Therefore

```text
ess inf b_(a,psi)^odd
 <= integral_0^1 W_a^odd(x) dx.
```

The right side is independent of `psi`.

Using the exact Suzuki decomposition from L-15401/L-15402,

```text
integral W_a^odd
 = A_arch(a)
   - 2 sum_(n<=exp(2a)) Lambda(n)/sqrt(n)
       (2-log(n)/a)
   - 32/a (cosh(a/2)-1)^2.
```

The archimedean term `A_arch(a)` is bounded above uniformly for `a>=1`, and the
prime term is nonpositive. Hence

```text
integral W_a^odd
 <= C - 32/a (cosh(a/2)-1)^2
 <= -exp(a)/a
```

for all sufficiently large `a`.

Consequently

```text
sup_(psi>0) ess inf b_(a,psi)^odd <= -exp(a)/a.
```

The desired `-o(1)` cofinal floor is impossible. With the prime number theorem,
the universal potential-mean obstruction is asymptotic to

```text
-16 exp(a)/a.
```

## Interpretation

The exact signed-edge representation remains valid. The obstruction enters only
when its nonnegative signed-edge remainder is discarded to form a scalar local
Barta floor.

The local term is independent of every edge sign. It therefore sees the odd
form as an unsigned Markov graph and loses the large frustration energy carried
by the cross-origin plus-squares. This is a structural no-go, not a poor choice
of spline or insufficient numerical precision.

## Artifacts

- `L-15403` — continuum mean obstruction and exponential no-go theorem;
- `R-15401` — formal retirement of the scalar cofinal target;
- `X-15402` — exact signed-graph regression and eight adversarial tests.

The finite control has

```text
potential mean = 29/9,
edge defect sum = -20/3,
Barta mean = 1,
Barta floor = 1.
```

Changing a cross edge from sign `-1` to sign `+1` leaves the local Barta values
unchanged exactly.

## Corrected critical path

A successful positive proof must retain phase/sign coherence globally. The
remaining credible routes are:

1. PR #152's generalized-prolate low-symbol packet plus the exact block Schur
   correction;
2. a matrix-valued or system ground-state representation that retains signed
   edge channels instead of collapsing them to one positive scalar function.

The supersolution branch should not spend additional computation fitting
positive scalar splines at large support.

## RH status

No proof or disproof of RH is claimed. The contribution closes one proposed
positive architecture by proving its final requested object impossible.
