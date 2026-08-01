# T-16203 — One strict energy angle closes the floor and coupling gates

Claim ID: `T-16203`  
Status: **PROVED BLOCK-OPERATOR THEOREM; PRODUCTION ENERGY ANGLE OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: `L-15107`, `T-16202`

## 1. Purpose

The remaining global conditions were listed separately as

```text
mu_lambda-L_lambda=O(a_lambda d_4),
background gap >=c a_lambda d_8,
eta_lambda^2=o(g_source g_background).                   (T-16203.1)
```

The first and third conditions are not independent. A relative-energy
factorization of the source/background cross block simultaneously provides:

1. a global spectral floor;
2. the desired target-floor excess;
3. a complete target-complement gap;
4. a quantitative target/background correction bound.

It replaces the unnecessarily strong absolute condition `eta^2=o(g_Sg_B)` by
one invariant strict angle `kappa<1`.

## 2. Whitened block form

Work first in an ordinary Hilbert metric. Let

```text
H=S direct_sum B,                                        (T-16203.2)
```

where `S` is the repaired source sector and `B` is its background complement.
Let `p in S` be a unit target and write

```text
A-sigma I=
 [ S_0   X  ]
 [ X^*  B_0 ],                                           (T-16203.3)
```

with `S_0>=0` and `B_0>=0`.

Assume there is a contraction between the two energy spaces,

```text
boxed:
X=S_0^(1/2) C B_0^(1/2),
||C||<=kappa<1.                                          (T-16203.4)
```

In finite dimensions, range/kernel compatibility is included in this
factorization. Equivalently, one may certify the two Schur inequalities

```text
X B_0^dagger X^* <=kappa^2 S_0,
X^* S_0^dagger X <=kappa^2 B_0,                          (T-16203.5)
```

with the cross block vanishing on the corresponding kernels.

## 3. Global floor

For `x in S`, `y in B`, put

```text
s=||S_0^(1/2)x||,
b=||B_0^(1/2)y||.
```

Then

```text
2|<x,Xy>|<=2kappa s b<=kappa(s^2+b^2).                   (T-16203.6)
```

Therefore

```text
boxed:
A-sigma I
 >=(1-kappa)(S_0 direct_sum B_0)>=0.                     (T-16203.7)
```

In particular,

```text
boxed:
lambda_min(A)>=sigma.                                    (T-16203.8)
```

No independent global-floor computation is required once (T-16203.4) is
proved.

## 4. Target-floor excess

Define the source target excess

```text
mu_S=<S_0p,p>.                                           (T-16203.9)
```

Because the target has zero background component,

```text
mu_A=<Ap,p>=sigma+mu_S.                                  (T-16203.10)
```

Using the floor `L_A=sigma`,

```text
boxed:
mu_A-L_A<=mu_S.                                          (T-16203.11)
```

Consequently, the source estimate

```text
mu_S=O(a_lambda d_4)                                     (T-16203.12)
```

already proves the former gate

```text
mu_lambda-L_lambda=O(a_lambda d_4).                      (T-16203.13)
```

## 5. Complete target-complement gap

Let

```text
E_S=S intersect p^perp.                                  (T-16203.14)
```

Assume the diagonal source and background bounds

```text
<S_0x,x>
 >=(mu_S+g_S)||x||^2,
 x in E_S,                                                (T-16203.15)

<B_0y,y>
 >=g_B||y||^2,
 y in B.                                                  (T-16203.16)
```

Then (T-16203.7), followed by subtracting the target Rayleigh value, gives for
`x in E_S`, `y in B`

```text
<(A-mu_A I)(x+y),x+y>
 >=[(1-kappa)(mu_S+g_S)-mu_S]||x||^2

  +[(1-kappa)g_B-mu_S]||y||^2.                           (T-16203.17)
```

Hence the complete target-complement gap satisfies

```text
boxed:
g_full>=min{
 (1-kappa)g_S-kappa mu_S,
 (1-kappa)g_B-mu_S
}.                                                        (T-16203.18)
```

This is a direct Feshbach/energy-angle estimate; it does not introduce an
absolute cross norm.

## 6. Asymptotic corollary

Suppose

```text
mu_S<=C_0 a_lambda d_4,

g_S>=c_S a_lambda d_8,

g_B>=c_B a_lambda d_8,

kappa_lambda<=kappa_0<1,                                 (T-16203.19)
```

and

```text
d_4/d_8->0.                                              (T-16203.20)
```

Then, for all sufficiently large `lambda`,

```text
boxed:
mu_A-L_A=O(a_lambda d_4),                                (T-16203.21)

 g_full>=c_* a_lambda d_8,                               (T-16203.22)
```

where one may take any fixed

```text
c_*<(1-kappa_0)min(c_S,c_B).                             (T-16203.23)
```

Therefore

```text
boxed:
(mu_A-L_A)/g_full=O(d_4/d_8)=O(lambda^-8).               (T-16203.24)
```

The Rayleigh-floor identity `L-15107` then gives the required ground-line
convergence in every uniformly equivalent source Hardy metric.

Thus, after the repaired profile theorem, the original gates 2 and 4 collapse
to one production predicate:

```text
boxed:
The source/background energy angle stays strictly below one.              (T-16203.25)
```

Gate 3 remains the diagonal background lower bound.

## 7. Target/background correction

The factorization also gives a useful one-vector estimate. From

```text
X^*p=B_0^(1/2)C^*S_0^(1/2)p,
```

one has

```text
boxed:
||B_0^(-1/2)X^*p||^2
 <=kappa^2 mu_S,                                         (T-16203.26)
```

with the inverse interpreted on the support of `B_0`. Thus the actual target
coupling to the background is already controlled by the small target energy;
it need not be `o(sqrt(g_Sg_B))` in an ambient operator norm.

## 8. Metric form

Let `G>0` be the production Gram. Whiten by `G^(1/2)` and apply the theorem to

```text
Ahat=G^(-1/2)AG^(-1/2).                                  (T-16203.27)
```

All orthogonality, gaps, and square roots in the statement are then interpreted
in the `G` metric. The energy angle is invariant under simultaneous congruence.
A finite certificate may avoid irrational square roots by checking the Schur
forms in (T-16203.5) with rational Loewner enclosures.

## 9. Relation to the earlier absolute coupling gate

If

```text
|<x,Xy>|<=eta||x||||y||,
```

then `eta^2=o(g_Sg_B)` certainly makes the cross block harmless. It is not
necessary. For example, `X` may have ordinary norm of order one on high-energy
modes while satisfying (T-16203.4) with a fixed `kappa<1`.

The energy-angle condition measures cross coupling relative to the diagonal
energies that absorb it. It is the natural Schur/Feshbach invariant.

## 10. Proof boundary

The block theorem is exact. It does not prove the production inequalities
`S_0>=0`, `B_0>=0`, the background gap, or the strict energy angle for the CCM
localized-Weil matrix. Those are now the remaining global operator estimates.
No RH proof is claimed.
