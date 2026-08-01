# L-16208 — Fixed low prolate source packets have a bounded moving Hardy Gram

Claim ID: `L-16208`  
Status: **PROVED FROM THE DECLARED UNIFORM PROLATE APPROXIMATION**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: CCM Lemma 7.2 fixed-mode `O(lambda^-2)` approximation; `L-16205`

## 1. Purpose

The factor

```text
2 lambda^(2tau)
```

in the ordinary-gap fallback is the norm of the Hardy weight over the **whole
support**. It is attained by arbitrary endpoint-concentrated vectors, not by the
fixed low prolate source packet that drives the positive route.

This lemma proves that, on any fixed packet of modes divisible by four, the
moving Hardy Gram converges to a finite positive limit for a suitable schedule
`tau_lambda->1/2`. Thus the relative trace-form bridge does not need the ambient
factor `lambda^(2tau)`.

## 2. Additive source assumptions

Fix a finite index set

```text
I subset {0,4,8,12,...}.                                  (L-16208.1)
```

Let `h_n` be the normalized Fourier-invariant Hermite functions. Let
`f_(n,lambda)` be even compactly supported sources on `[-lambda,lambda]`,
extended by zero, such that for every `n in I`

```text
sup_(|x|<=lambda)
 |f_(n,lambda)(x)-h_n(x)|
 <=C_n lambda^-2.                                         (L-16208.2)
```

This is the fixed-mode approximation supplied in the CCM outlook for the
prolate modes.

Define, on the multiplicative window,

```text
k_(n,lambda)(u)=E(f_(n,lambda))(u),
lambda^-1<=u<=lambda,                                    (L-16208.3)
```

and define the full Hermite source

```text
k_n(u)=E(h_n)(u),
0<u<infinity.                                             (L-16208.4)
```

## 3. Pointwise E-sum estimate

For every fixed integer `m>=3`, Hermite rapid decay and (L-16208.2) give,
uniformly for `lambda^-1<=u<=lambda`,

```text
boxed:
|k_(n,lambda)(u)-k_n(u)|
 <=C_(n,m) lambda^-1 u^-1/2.                             (L-16208.5)
```

The first contribution is the error in the at most `lambda/u` active prolate
terms; the second is the omitted Hermite tail beyond `lambda/u`.

## 4. Moving Hardy convergence

For `0<=tau<1/2`, put

```text
||g||_tau^2
 =integral_0^infinity |g(u)|^2
  (u^(2tau)+u^(-2tau))d*u.                               (L-16208.6)
```

Equation (L-16208.5) gives

```text
boxed:
||k_(n,lambda)-1_[lambda^-1,lambda] k_n||_tau^2
 <=C_n' lambda^(-1+2tau).                                (L-16208.7)
```

The harmless exact bound includes denominators `1+2tau` and `1-2tau` in the
smaller term; they may be absorbed for `tau` bounded away from zero.

Because `F h_n=h_n`, the Poisson identity gives

```text
k_n(u)=k_n(u^-1).                                         (L-16208.8)
```

Since `k_n` is rapidly decreasing as `u->infinity`, it is rapidly decreasing
as `u->0` as well. Therefore

```text
k_n belongs to the endpoint Hardy space tau=1/2.          (L-16208.9)
```

Let

```text
tau_lambda=1/2-delta_lambda,
delta_lambda>0,
delta_lambda->0,
delta_lambda log lambda->infinity.                        (L-16208.10)
```

Then

```text
lambda^(-1+2tau_lambda)
 =exp(-2delta_lambda log lambda)->0,                      (L-16208.11)
```

and the support tail of `k_n` also tends to zero in the moving Hardy norm.
Consequently

```text
boxed:
||k_(n,lambda)-k_n||_(tau_lambda)->0.                    (L-16208.12)
```

## 5. Gram convergence

Let `G_(lambda,tau)` be the Hardy Gram of the finite packet
`{k_(n,lambda):n in I}`, and let `G_*` be the endpoint Hardy Gram

```text
(G_*)_(mn)=<k_m,k_n>_(tau=1/2).                          (L-16208.13)
```

Then

```text
boxed:
G_(lambda,tau_lambda)->G_*                               (L-16208.14)
```

entrywise and in operator norm.

The map `E` is injective on the finite span of the declared Hermite sources:
from

```text
widehat(E(f))(z)=zeta(1/2-iz)M_f(z),                     (L-16208.15)
```

vanishing of `E(f)` forces the entire source Mellin transform to vanish away
from the discrete zeta-zero set, hence identically. Therefore `G_*` is positive
definite.

It follows that, for all sufficiently large `lambda`,

```text
boxed:
c_I G_0 <=G_(lambda,tau_lambda)<=C_I G_0,                (L-16208.16)
```

for any fixed positive coefficient Gram `G_0` on the packet and finite constants
`0<c_I<C_I<infinity`.

## 6. Proof of the pointwise estimate

Write

```text
E(f_(n,lambda))(u)-E(h_n)(u)
 =u^(1/2) sum_(j<=lambda/u)
   [f_(n,lambda)(ju)-h_n(ju)]

  -u^(1/2) sum_(j>lambda/u)h_n(ju).                      (L-16208.17)
```

The first sum is bounded by

```text
u^(1/2)(lambda/u)C_nlambda^-2
 =C_nlambda^-1u^-1/2.                                    (L-16208.18)
```

For `|h_n(x)|<=C_(n,m)(1+x)^-m`, the second sum is at most

```text
C_(n,m)u^(1/2)u^-m(lambda/u)^(1-m)
 <=C_(n,m)lambda^(1-m)u^-1/2,                            (L-16208.19)
```

which is smaller for `m>=3`. This proves (L-16208.5).

Squaring and integrating over `[lambda^-1,lambda]` gives

```text
C lambda^-2 integral_(lambda^-1)^lambda
 [u^(2tau-2)+u^(-2tau-2)]du
 <=C'lambda^(-1+2tau),                                   (L-16208.20)
```

proving (L-16208.7). The remaining statements follow from symmetry, rapid
decay, dominated convergence, and finite-dimensional Gram continuity. QED.

## 7. Corrected trace-form requirement

On the fixed repaired packet, replace the ambient condition

```text
lambda^(2tau)||R||_G/(a d_8)->0                          (L-16208.21)
```

by the source-specific condition

```text
boxed:
||R_S||_(G_(lambda,tau_lambda))/(a_lambda d_8)->0.       (L-16208.22)
```

Equivalently, after the exact tail factorization and normalization of
`L-16204`, it is enough that

```text
boxed:
(M_lambda-m_lambda)/(M_lambda+m_lambda)->0.              (L-16208.23)
```

No power of `lambda` appears.

This is not a weakening of the RH conclusion: `T-14301` only needs some schedule
`tau_lambda->1/2`. The slow schedule (L-16208.10) is fully sufficient for local
uniform convergence on every fixed compact substrip.

## 8. Proof boundary

The lemma proves the source Hardy-Gram control under the imported uniform
`O(lambda^-2)` fixed-mode approximation. It does not prove tail alias
suppression, normalized tail Weil scalarization, or the global background/floor
gates. No RH proof is claimed.
