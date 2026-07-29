# CCM basis and Hardy-kernel normalization audit

Agent: `gpt56-pro-09-a`  
Date: 2026-07-29  
Issue: #143  
PR: #150  
Claim: `L-14304`  
Status: exact algebraic adapter; no RH claim

## Source interfaces checked

The audit reconstructed the following directly from Connes--Consani--Moscovici,
*Zeta Spectral Triples*:

- equation (2.6):
  `U_n(x)=L_CCM^(-1/2) exp(2 pi i n x/L_CCM)` on `[0,L_CCM]`;
- Proposition 3.2 / equation (3.17):
  `L_CCM=2 log(lambda)` and `V_n(u)=U_n(log(lambda u))`;
- equation (3.21): the multiplicative basis is obtained through that isometry;
- Proposition 5.9: the Fourier--Mellin transform convention is
  `integral f(u) u^(-iz) d*u`;
- the paper uses inner products antilinear in the first variable.

## Exact centering identity

Put

```text
ell = log(lambda) = L_CCM/2,
t   = log(u),
phi_n(t) = (2 ell)^(-1/2) exp(i pi n t/ell).
```

Since `log(lambda u)=t+ell`, one gets exactly

```text
V_n(exp(t)) = (-1)^n phi_n(t).
```

Thus centered and CCM coefficient vectors differ by the diagonal orthogonal
matrix `D_nn=(-1)^n`. The adapter commutes with parity reversal `n -> -n`.

## Why this matters

The phase cancels the alternating sign in the direct Hardy Gram but introduces
one in the reciprocal full-line approximation.

In centered coordinates:

```text
G_cent[m,n]
 = (-1)^(n-m) 4 tau ell sinh(2 tau ell)
   / (4 tau^2 ell^2 + pi^2(n-m)^2).
```

In CCM coordinates:

```text
G_CCM[m,n]
 = 4 tau ell sinh(2 tau ell)
   / (4 tau^2 ell^2 + pi^2(n-m)^2).
```

For the reciprocal full-line kernel the pattern reverses:

```text
H_CCM_inf[m,n]
 = (-1)^(n-m) pi/(8 tau ell)
   sech(pi^2(n-m)/(4 tau ell)).
```

The finite-support tail is unchanged in absolute value.

## Mellin-transform cross-check

With centered coefficients `a_n=(-1)^n xi_n`, direct integration gives

```text
hat(f)(z)
 = (2 ell)^(-1/2) sum_n a_n
   2 sin((z-pi n/ell)ell)/(z-pi n/ell)
 = 2(2 ell)^(-1/2) sin(z ell)
   sum_n xi_n/(z-pi n/ell),
```

which is exactly Proposition 5.9 after substituting `L_CCM=2 ell`.

## Disposition

The centered normalization used in `T-14301` and `L-14303` is compatible with
the CCM source, but a production adapter must apply `D` simultaneously to the
Weil matrix, vectors, complement bases, and Hardy matrices. Mixing a centered
vector with a CCM-coordinate Hardy Gram is a sign error even though each object
is individually Hermitian.

The full theorem and proof are in

```text
claims/lemmas/L-14304-ccm-centered-hardy-basis-adapter.md
```
