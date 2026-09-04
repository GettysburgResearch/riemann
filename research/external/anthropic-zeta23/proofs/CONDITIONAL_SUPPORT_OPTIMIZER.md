# Conditional scalar optimizer beyond bandwidth one

**Status:** `CONDITIONAL THEOREM + CONVERGENT NUMERICAL RECONNAISSANCE`

The unconditional paper stops at normalized Fourier support `lambda<=1`. This note asks the exact next question: what scalar-window constant would the same inertia mechanism produce if the second trace were known with the GUE/pair-correlation form factor beyond one?

No such unconditional support extension is claimed.

## 1. Trace-extension hypothesis

Fix `lambda>0`. Assume that the same normalized finite compression exists and that its second moment for a window profile `v` on `I=[-1/2,1/2]` is governed by

```text
D_lambda(v)
 = int_I v(s)^2 ds
   + lambda int_I int_I min(lambda |s-t|,1) v(s)v(t) ds dt.
```

The associated rank efficiency is

```text
c_lambda(v)
 = lambda [int_I v]^2 / D_lambda(v).
```

The rank–trace certificate would then give the simple-on-line proportion

```text
H_lambda(v)=2-1/c_lambda(v).
```

For `lambda<=1`, the kernel never saturates and this is exactly the paper's functional

```text
D_lambda(v)=int v^2+lambda^2 int int |s-t|v(s)v(t).
```

The hypothesis is stated directly at the trace level. It should not be silently identified with a standard pair-correlation conjecture unless a proof establishes that implication in the off-line-zero setting.

## 2. Fredholm characterization

Define

```text
(T_lambda v)(s)
 = int_I min(lambda |s-t|,1)v(t)dt,
A_lambda = I+lambda T_lambda.
```

Whenever `A_lambda` is positive and invertible, the unconstrained maximizer of `c_lambda` is unique up to scale and satisfies

```text
A_lambda v = constant.
```

Equivalently,

```text
v is proportional to A_lambda^(-1) 1,
c_lambda^* = lambda <1,A_lambda^(-1)1>.
```

### Proof

The denominator is the quadratic form `<v,A_lambda v>` and the numerator is `lambda <1,v>^2`. Cauchy–Schwarz in the `A_lambda` inner product gives

```text
<1,v>^2
 = <A_lambda^(-1/2)1,A_lambda^(1/2)v>^2
 <= <1,A_lambda^(-1)1><v,A_lambda v>,
```

with equality exactly when `v` is proportional to `A_lambda^(-1)1`. `square`

The numerical solutions in the supplied range are positive, so the nonnegativity constraint on `v` is inactive there.

## 3. Recovery of the support-one cosine

For `lambda<=1`,

```text
(T_lambda v)''=2lambda v
```

in the interior. Differentiating `v+lambda T_lambda v=constant` twice gives

```text
v''+2lambda^2 v=0.
```

Evenness selects

```text
v(s)=cos(sqrt(2)lambda s).
```

Writing `theta=lambda/sqrt(2)`, one obtains

```text
c_lambda^*
 = sqrt(2) tan(theta)/(1+theta tan(theta)),
```

which is the Montgomery–Taylor constant at `lambda=1`.

## 4. Delay equation for lambda>1

Let

```text
K_lambda(x)=min(lambda |x|,1).
```

Its distributional second derivative is

```text
K_lambda''
 = 2lambda delta_0
   -lambda delta_(1/lambda)
   -lambda delta_(-1/lambda).
```

Extending `v` by zero outside `I`, the Fredholm equation therefore implies the interior delay equation

```text
v''(s)
 +2lambda^2 v(s)
 -lambda^2 v(s-1/lambda)
 -lambda^2 v(s+1/lambda)
 =0.                                                    (DE)
```

For `lambda<=1`, both shifted terms vanish in the interior and `(DE)` reduces to the cosine ODE. For `lambda>1`, arithmetic support crossing one appears analytically as a finite-range self-interaction.

## 5. Flat-window benchmark

For `v=1` and `lambda>=1`, direct integration gives

```text
c_lambda(flat)=lambda^2/(lambda^2+1/3),
H_lambda(flat)=1-1/(3lambda^2).
```

Thus even the unoptimized scalar model tends to `100%` if the trace hypothesis is available at arbitrarily large support.

## 6. Optimized numerical values

The supplied Gauss–Legendre/Nyström solver computes

```text
c_lambda^* = lambda w^T A_n^(-1) w
```

on successively refined quadrature grids. Representative 512-node values are:

| lambda | optimized c* | simple-on-line lower bound `2-1/c*` |
|---:|---:|---:|
| 1.000 | 0.7532967 | 0.6725018 |
| 1.040 | 0.7682846 | 0.6983989 |
| 1.250 | 0.8314042 | 0.7972156 |
| 1.700 | 0.9089246 | 0.8997988 |
| 2.000 | 0.9365796 | 0.9322851 |

Bisection on the converged discretization gives the approximate support thresholds:

| target proportion | lambda |
|---:|---:|
| 0.68 | 1.0111 |
| 0.70 | 1.0426 |
| 0.75 | 1.1357 |
| 0.80 | 1.2578 |
| 0.85 | 1.4296 |
| 0.90 | 1.7014 |
| 0.95 | 2.2606 |

These are conditional numerical values, not interval-certified theorem constants. The script reports multi-resolution convergence so that a later directed implementation has a clear target.

## 7. Strategic interpretation

The first support milestone is tiny but decisive:

```text
support 1.0000 -> 67.25%,
support about 1.0426 -> 70%.
```

Therefore a theorem that extends the usable trace asymptotic only about four percent beyond the present barrier would already produce a conspicuous new record through the same zero-side algebra.

Conversely, no amount of support-one scalar taper optimization can reach `70%`. The arithmetic problem and the linear-algebra problem are now cleanly separated.
