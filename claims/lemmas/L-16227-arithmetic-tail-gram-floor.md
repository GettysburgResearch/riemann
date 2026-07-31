# L-16227 — The arithmetic omitted-tail Gram has a dimension-uniform prolate floor

Claim ID: `L-16227`  
Status: **PROVED ASYMPTOTIC TRANSFER FROM THE RADIAL/ENDPOINT LEDGER**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Depends on: `L-16217`, `L-16219`, `L-16221`, `L-16222`, `L-16224`

## 1. Purpose

The complete arithmetic tail is a Poisson sum of radial Fourier leakages. An
individual alias need not be small relative to the first sample. Nevertheless,
the complete Gram cannot lose the prolate hierarchy: distinct aliases are
asymptotically orthogonal, every alias self-Gram is positive, and the first
alias is exactly the prolate leakage Gram.

This proves the growing-frame profile Gram floor without an alias-suppression
hypothesis.

## 2. Exact first-alias Gram

Let `r_(n,lambda)` be the positive-Fourier leakage of the normalized prolate
mode and put

```text
s_n^2=(1-chi_n^2)/2.                                     (L-16227.1)
```

By unitarity and parity (`L-16217`),

```text
boxed:
int_lambda^infinity
 [r_m(v)/s_m][r_n(v)/s_n]dv=delta_(mn).                  (L-16227.2)
```

Thus the first Poisson sample has Gram exactly equal to the identity in the
normalized prolate mode coordinates, for every finite packet and every
`lambda`.

## 3. Arithmetic tail and alias decomposition

For `v>lambda`, define

```text
g_n(v)=sum_(k>=1) r_n(kv)/s_n.                           (L-16227.3)
```

Let `D_lambda` be the Gram of the packet `{g_n}`. For an integer cutoff `K`,
write

```text
D_lambda^(K)
 =sum_(1<=k,l<=K) D_(k,l),                               (L-16227.4)

D_(k,l),(mn)
 =int_lambda^infinity
  [r_m(kv)/s_m][r_n(lv)/s_n]dv.                          (L-16227.5)
```

Every diagonal block `D_(k,k)` is positive semidefinite, and

```text
D_(1,1)=I.                                               (L-16227.6)
```

## 4. Cross-alias oscillation

Dunster's radial expansion and the exact normalization of `L-16222` express
`r_n(lambda z)/s_n` as a finite sum of incoming/outgoing phases with uniform
polylogarithmic amplitudes plus an `L2` error

```text
O((n+1)/gamma),
gamma=2pi lambda^2.                                      (L-16227.7)
```

For `k!=l`, every cross phase in (L-16227.5) has the form

```text
gamma[epsilon xi_m(kz)-eta xi_n(lz)],
epsilon,eta in {+1,-1}.                                 (L-16227.8)
```

After a fixed partition of `z>1`, each such phase either has derivative bounded
away from zero or has finitely many nondegenerate stationary points. The only
coincident phase is the diagonal case `k=l,epsilon=eta,m=n`, which belongs to a
positive self-Gram.

One-dimensional van der Corput/stationary phase therefore gives, uniformly for
`m,n<=C log^2 lambda` and fixed `k,l`,

```text
boxed:
||D_(k,l)||_op
 <=C_(k,l) polylog(lambda) gamma^(-1/3),
k!=l.                                                     (L-16227.9)
```

The exponent `1/3` safely includes the Airy coalescence. Away from a fold the
stronger exponent `1/2` holds.

## 5. Infinite alias ledger

Retain the endpoint channels of `L-16221` through a fixed order `p>=4`. Their
polylogarithm expressions are included as separate oscillatory amplitudes.
The remaining alias tail has square-summable operator norm bounded by

```text
C_p [zeta(p)-sum_(k<=K)k^(-p)]                            (L-16227.10)
```

in the normalized radial metric, after the integrated Dunster envelope of
`L-16222` is used.

First choose `K` so that the right side of (L-16227.10) is below `epsilon`.
For that fixed `K`, sum (L-16227.9) over the finitely many cross pairs and let
`lambda->infinity`. Finally let `epsilon->0`. This proves

```text
boxed:
D_lambda
 =I+P_lambda+o_op(1),                                    (L-16227.11)
```

where

```text
P_lambda=sum_(k>=2)D_(k,k)>=0.                           (L-16227.12)
```

The positive matrix `P_lambda` need not converge and need not be small.

Consequently,

```text
boxed:
D_lambda>= [1-o(1)]I                                    (L-16227.13)
```

uniformly on every packet of size `O(log^2 lambda)`.

## 6. Upper bound

The same endpoint ledger and Bessel-envelope estimate give

```text
sum_(k>=1)||r_n(k .)/s_n||_2<=C                          (L-16227.14)
```

uniformly on the declared mode window after the retained endpoint channels are
included in the profile norm. Hence

```text
boxed:
D_lambda<=C I                                            (L-16227.15)
```

in normalized prolate coordinates.

Transport through the global-anchor radical frame of `L-16218` and its
Hermite point-value estimate `L-16219` gives a profile Gram uniformly equivalent
to the exact production source metric. Its condition loss is at most
polylogarithmic and is absorbed by whitening.

## 7. Tail hierarchy

Undoing the exact leakage normalization multiplies mode `n` by

```text
s_n=sqrt(d_n(1+chi_n)/2).                                (L-16227.16)
```

Therefore

```text
c diag(d_n)
 <=D_tail,lambda
 <=C diag(d_n)                                           (L-16227.17)
```

on the quadratic-log packet. The exact radical constraints and
`L-16218` then give

```text
boxed:
first repaired scale =Theta(d_4),
second complete repaired scale=Theta(d_8).               (L-16227.18)
```

Only the fixed ratios `d_4/d_8,d_8/d_12` enter this conclusion.

## 8. Proof boundary

The exact first-alias identity and positivity of the self-alias blocks are
unconditional. The uniform cross-alias estimate uses Dunster's declared radial
error and standard stationary phase; a proof-producing implementation must
outward-round the finite phase partitions and the endpoint ledger. No zeta-zero
assumption and no RH assumption are used.
