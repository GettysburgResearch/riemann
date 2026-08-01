# T-15101 — A fixed exact-radical diagonal criterion implying the Riemann hypothesis

Claim ID: `T-15101`
Status: **PROPOSED SUFFICIENT CRITERION; proof below, imported CCM interfaces explicit**
Authoring agent: `gpt56-pro-10`
Created: 2026-07-30
Depends on: `L-15101`, `L-15102`, audited `L-14302`; Connes–Consani–Moscovici Proposition 5.7 and Theorem 5.10

## 1. Why this criterion is useful

The preceding positive route uses a moving prolate target `k_lambda` and asks
that the finite localized-Weil ground state approach it. This theorem supplies a fixed-reference baseline using one vector

```text
k=E(h),
h(x)=(pi/2)x^2(2pi x^2-3)exp(-pi x^2),
```

whose multiplicative Fourier transform is exactly `Xi` and which lies in the
radical of the **full** Weil form. Localization creates a residual because part
of this exact radical vector is omitted, and `L-15102` identifies that residual
exactly as a boundary-leakage functional.

This does not assert that the fixed projection is the optimal finite target.
By `L-15103`, the moving prolate target is naturally the exact reference plus a
finite corrector. The theorem remains a valid sufficient criterion and a
normalization baseline; the hybrid corrected target may be the route on which
the relative estimate is actually provable.

## 2. Finite spaces and weights

Let

```text
K=L2(R_+^*,d*u),       d*u=du/u.
```

For `lambda>1` and `N>=0`, let `V_(lambda,N)` be the CCM Fourier space of
functions supported on `[lambda^(-1),lambda]` and spanned by modes
`-N,...,N`. Let

```text
P_(lambda,N):K -> V_(lambda,N)
```

be the ordinary `L2` orthogonal projection and put

```text
p_(lambda,N)=P_(lambda,N)k.
```

The spaces are invariant under inversion `Gamma f(u)=f(u^(-1))`. Since `k` is
even, every `p_(lambda,N)` is even.

Let `A_(lambda,N)` be the self-adjoint matrix representing the restriction of
the full Weil form `QW` to `V_(lambda,N)`. For `0<tau<1/2`, let

```text
||f||_tau^2
 = integral_0^infinity |f(u)|^2
     (u^(2tau)+u^(-2tau)) d*u,
```

and let `M_(lambda,N,tau)` be the corresponding positive Gram operator on the
finite space.

For nonzero `p=p_(lambda,N)`, define

```text
v=p/||p||_2,
W_+=V_+ intersect v^perp,
mu=<Ap,p>/<p,p>.
```

Let `C_+` and `C_-` be the compressions of `A` to `W_+` and the odd subspace
`V_-`, respectively. Let `M_+` be the restriction of the Hardy Gram to `W_+`.

## 3. Boundary leakage

Define the finite boundary-leakage dual

```text
B(lambda,N,tau)
 = sup_(0!=w in W_+)
     |QW(k-p,w)|/||w||_tau.                              (T-15101.1)
```

Although its interpretation uses the omitted global vector, it is a finite
quantity. By `L-15102`,

```text
B(lambda,N,tau)
 = ||P_(W_+) A p||_(M_+^(-1)).                           (T-15101.2)
```

Thus it can be computed either from the finite Weil matrix and projected target
or from an independently evaluated boundary pairing.

## 4. Statement

Suppose there are sequences

```text
lambda_j -> infinity,
N_j       -> infinity,
tau_j     -> 1/2 from below,
```

and positive numbers `h_j,g_j`, with real upper endpoints `U_j>=mu_j`, such
that for every sufficiently large `j`:

```text
C_(+,j)-U_j I >= h_j M_(+,j),
C_(-,j)-U_j I >= g_j I.                                  (T-15101.3)
```

Assume also that

```text
t_j + B_j/h_j -> 0,                                      (T-15101.4)

t_j=||k-p_j||_(tau_j),
B_j=B(lambda_j,N_j,tau_j).
```

Then the Riemann hypothesis is true.

It is sufficient to replace the first term in (T-15101.4) by the explicit
upper bound from `L-15101`:

```text
t_j^2
 <= 2704 lambda_j^(7+2tau_j) exp(-2pi lambda_j^2)
      /[4pi-(7+2tau_j)/lambda_j^2]
    +2 lambda_j^(2tau_j) log(lambda_j) 382^2/(pi^2 N_j). (T-15101.5)
```

Consequently, once `lambda_j,tau_j` are fixed, the projection part has an
explicit finite cutoff. The genuinely new analytic condition is the relative
leakage estimate

```text
B_j/h_j -> 0.                                             (T-15101.6)
```

## 5. Proof

### Step 1 — the finite gates certify simple-even ground states

Apply audited `L-14302` to `A_j`, target `p_j`, Hardy norm `||.||_(tau_j)`, and
the two inequalities (T-15101.3). The lowest eigenvalue of `A_j` is simple,
and a normalized ground eigenvector `xi_j` is even. Moreover there is an
explicit nonzero scalar `c_j` for which

```text
||c_j xi_j-k||_(tau_j)
 <= ||k-p_j||_(tau_j)
    +||P_(W_+,j)A_jp_j||_(M_(+,j)^(-1))/h_j.              (T-15101.7)
```

By (T-15101.2), the right side is `t_j+B_j/h_j`, and hence tends to zero.

### Step 2 — weighted source convergence gives strip convergence

Write `u=exp(t)`. For `0<=sigma<tau<1/2`, Cauchy–Schwarz on the whole logarithmic
line gives

```text
sup_(|Im z|<=sigma)|hat(f)(z)|
 <= [pi/(4tau cos(pi sigma/(2tau)))]^(1/2)||f||_tau.       (T-15101.8)
```

The constant is independent of support. Fix a compact set in the open strip
`|Im z|<1/2`, choose `sigma<tau<1/2` containing it, and then take `j` large
enough that `tau_j>=tau`. Monotonicity of the weight in `tau` and
(T-15101.7) give

```text
hat(c_j xi_j) -> hat(k)=Xi
```

locally uniformly throughout the open strip.

### Step 3 — every finite transform has only real zeros

The finite ground state is simple and even. Under the CCM normalization,
Proposition 5.7 supplies the nonzero boundary normalization and Theorem 5.10
states that the Fourier–Mellin transform of `xi_j` is entire and has only real
zeros. Multiplying by `c_j` does not change those zeros.

### Step 4 — Hurwitz

If `Xi` had a nonreal zero in `|Im z|<1/2`, choose a closed disk around it that
is disjoint from the real axis and contained in the strip. Every finite
approximant is nonvanishing on the disk, while the approximants converge there
uniformly to the nonzero entire function `Xi`. Hurwitz's theorem gives a
contradiction. Therefore every zero of `Xi` in the strip is real, which is
exactly RH under `Xi(z)=xi(1/2+iz)`. QED.

## 6. Finite proof-producing form

At one level, all predicates are finite after directed primitive evaluation:

1. exact target coefficients `p_j` with a directed projection-tail bound;
2. rational Loewner enclosures for `A_j` and `M_j`;
3. exact rational bases of the even complement and odd sector;
4. robust LDL certificates for (T-15101.3);
5. a Schur or reciprocal-Hardy certificate for `B_j`;
6. a rational upper bound for `t_j+B_j/h_j`.

A sequence of isolated positive finite checks is not enough. The proof requires
one cofinal sequence whose final upper bounds tend to zero.

## 7. Exact remaining theorem

The RH problem has not disappeared. It is concentrated in the following
relative estimate:

```text
sup_(w in W_+, ||w||_tau=1)
  |QW(k-P_(lambda,N)k,w)|
    =o(h_(lambda,N,tau))                                 (T-15101.9)
```

along a sequence satisfying the parity-sector gates.

An absolute tail bound is not automatically sufficient: the coercivity `h` may
itself be superexponentially small. The needed estimate must exploit the exact
Fourier invariance and two moment cancellations of `h`, or an equivalent
relative prolate spectral separation.

## 8. Proof boundary

This theorem is a sufficient criterion, not a completed proof of RH. It
imports the CCM finite real-zero theorem and the exact identification
`hat(E(h))=Xi`; those normalizations require independent source review. No proof of (T-15101.9), and no cofinal production sequence satisfying it, is
claimed here. A proof using the moving prolate target may instead invoke
`L-15103` and `L-15104`; it must still establish the same dimensionless
residual/coercivity decay.
