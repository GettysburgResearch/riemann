# L-16217 — Exact radial-leakage normalization by the prolate defect

Claim ID: `L-16217`  
Status: **PROVED EXACT NORMALIZATION; UNIFORM TEMPLATE ESTIMATES SEPARATE**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Primary references: CCM equation (7.9); Dunster equations (1.19), (6.5)--(6.7)

## 1. Purpose

The positive route previously left open the amplitude conversion between:

- the CCM-normalized finite Fourier eigenfunction;
- Dunster's angular and radial PSWF normalizations;
- the concentration defect `d_n=1-chi_n`;
- and the omitted radial leakage used in the arithmetic tail.

The conversion is in fact forced exactly by unitarity. No asymptotic evaluation
of Dunster's constants `p_n^0(gamma),q_n^0(gamma)` is needed to identify the
amplitude relative to `sqrt(d_n)`.

## 2. Fourier convention and prolate eigenfunction

Use the unitary CCM Fourier convention

```text
(F f)(y)=integral_R f(x) exp(2 pi i x y) dx.              (L-16217.1)
```

Fix `lambda>1`, let `P_lambda` be restriction to `[-lambda,lambda]`, and let
`h_(n,lambda)` be a real even `L2(R)`-normalized function supported on that
interval such that

```text
P_lambda F h_(n,lambda)=chi_n(lambda) h_(n,lambda),       (L-16217.2)

0<chi_n(lambda)<1.                                       (L-16217.3)
```

For the positive Fourier modes used in the repository, `n` is divisible by
four and the eigenvalue is positive. Put

```text
d_n=1-chi_n.                                              (L-16217.4)
```

Define the Fourier leakage

```text
r_n=F h_(n,lambda)-chi_n h_(n,lambda).                    (L-16217.5)
```

Because (L-16217.2) holds on the support, `r_n` is supported almost everywhere
on `|x|>lambda`.

## 3. Exact defect norm

Unitarity and the eigenrelation give

```text
||r_n||_2^2
 =||Fh_n||_2^2+chi_n^2||h_n||_2^2
  -2chi_n Re<Fh_n,h_n>
 =1-chi_n^2.                                              (L-16217.6)
```

Evenness splits this equally between the two exterior rays:

```text
boxed:
int_lambda^infinity |r_n(x)|^2 dx
 =(1-chi_n^2)/2
 =d_n(1+chi_n)/2.                                        (L-16217.7)
```

Hence the exact positive-ray leakage amplitude is

```text
s_n(lambda)
 :=sqrt((1-chi_n^2)/2)
 =sqrt(d_n(1+chi_n)/2).                                  (L-16217.8)
```

In particular, at every fixed near-one mode,

```text
boxed:
s_n/sqrt(d_n)->1.                                        (L-16217.9)
```

This closes the requested normalization relative to `sqrt(d_n)`.

## 4. Scaled angular and radial functions

Put

```text
gamma=2 pi lambda^2,                                     (L-16217.10)

psi_n(t)=sqrt(lambda) h_(n,lambda)(lambda t),
|t|<=1.                                                   (L-16217.11)
```

Then `||psi_n||_(L2[-1,1])=1`. Let `Psi_n(z)` denote its entire radial
continuation, normalized by the finite Fourier identity

```text
integral_(-1)^1 psi_n(t) exp(i gamma z t) dt
 =(chi_n/lambda) Psi_n(z).                               (L-16217.12)
```

On `|z|<=1`, one has `Psi_n(z)=psi_n(z)`. Analytic continuation gives
(L-16217.12) for every complex `z`.

Changing variables in the full Fourier transform gives exactly

```text
(Fh_n)(lambda z)
 =chi_n lambda^(-1/2) Psi_n(z).                           (L-16217.13)
```

For real `z>1`, the source itself vanishes, and therefore

```text
r_n(lambda z)
 =chi_n lambda^(-1/2) Psi_n(z).                           (L-16217.14)
```

Combining (L-16217.7) and (L-16217.14) gives the exact radial norm identity

```text
boxed:
chi_n^2 integral_1^infinity |Psi_n(z)|^2 dz
 =(1-chi_n^2)/2.                                         (L-16217.15)
```

Thus

```text
boxed:
rho_(n,lambda)(z)
 :=chi_n Psi_n(z)/s_n,

||rho_(n,lambda)||_(L2(1,infinity))=1.                   (L-16217.16)
```

The functions `rho_(n,lambda)` are the canonical dimensionless radial leakage
profiles. Any CCM/Dunster asymptotic should be compared to these normalized
objects rather than to an independently guessed amplitude.

## 5. Exact conversion to Dunster's normalization

For order `m=0`, Dunster normalizes the angular PSWF by

```text
integral_(-1)^1 Ps_n^0(x,gamma^2)^2 dx=2/(2n+1).         (L-16217.17)
```

Consequently

```text
psi_n=sqrt((2n+1)/2) Ps_n^0.                             (L-16217.18)
```

Dunster's radial formula (6.5) reads

```text
Ps_n^0(z,gamma^2)
 =sqrt(q_n^0(gamma)/((2n+1)p_n^0(gamma)))
  [B_(n,gamma)(z)+E_(n,gamma)(z)],                        (L-16217.19)
```

where

```text
B_(n,gamma)(z)
 ={(z^2-1)(z^2-sigma_n^2)}^(-1/4)
  xi_n(z)^(1/2) J_0(gamma xi_n(z)),                       (L-16217.20)
```

and the pointwise error is bounded by the declared Dunster envelope times
`O(gamma^-1)`.

Multiplying (L-16217.19) by the factor in (L-16217.18) gives

```text
Psi_n(z)
 =sqrt(q_n^0(gamma)/(2p_n^0(gamma)))
  [B_(n,gamma)(z)+E_(n,gamma)(z)].                        (L-16217.21)
```

Substituting into the exact radial norm identity proves

```text
boxed:
[q_n^0(gamma)/(2p_n^0(gamma))]
 ||B_(n,gamma)+E_(n,gamma)||_2^2
 =(1-chi_n^2)/(2chi_n^2).                                (L-16217.22)
```

Equivalently,

```text
boxed:
sqrt(q_n^0/(2p_n^0))
 ={s_n/chi_n}/||B_(n,gamma)+E_(n,gamma)||_2.             (L-16217.23)
```

Thus Dunster's amplitude constants are not an additional unknown normalization:
their exact combination is determined by the concentration eigenvalue and the
norm of the dimensionless Bessel template plus its controlled error.

## 6. Bessel-template reduction

For `sigma=0`, one has

```text
xi(z)=sqrt(z^2-1),
B_(0,gamma)(z)=z^(-1/2)J_0(gamma sqrt(z^2-1)).            (L-16217.24)
```

The substitution `x=sqrt(z^2-1)` gives

```text
||B_(0,gamma)||_2^2
 =integral_0^infinity x J_0(gamma x)^2/(1+x^2) dx
 =I_0(gamma)K_0(gamma),                                  (L-16217.25)
```

where the last identity is the standard Hankel resolvent formula. Hence

```text
||B_(0,gamma)||_2^2
 =(2gamma)^(-1)(1+O(gamma^-2)).                           (L-16217.26)
```

For the polylogarithmic mode window of `L-16216`, Dunster's quantization gives
`sigma_n^2=O((n+1)/gamma)`. A uniform comparison of the transformed weight with
`(1+x^2)^(-1)`, together with an integrated Dunster-envelope estimate, would
therefore yield

```text
||B_(n,gamma)+E_(n,gamma)||_2^2
 =(2gamma)^(-1)
  [1+O((n+log gamma)/gamma)].                             (L-16217.27)
```

When (L-16217.27) is proved with directed constants, (L-16217.23) immediately
gives the completely normalized radial approximation

```text
rho_(n,lambda)
 =sqrt(2gamma) B_(n,gamma)
  +O_L2((n+log gamma)/gamma).                             (L-16217.28)
```

The exact amplitude theorem does not depend on this final template-norm estimate.

## 7. Consequences

1. The superexponential factor `sqrt(d_n)` is carried exactly by `s_n`.
2. No absolute error may be compared directly with `d_n`; all radial errors
   should first be divided by the exact leakage norm `s_n`.
3. The `p_n^0/q_n^0` normalization problem is replaced by one ordinary positive
   radial-template norm calculation.
4. The identity is uniform in the mode index wherever the finite Fourier
   eigenrelation is valid; it does not require fixed-index Fuchs asymptotics.

## 8. Proof boundary

- Equations (L-16217.6)--(L-16217.23) are exact.
- Dunster supplies the pointwise radial error with a broad uniform mode range.
- The uniform integrated envelope estimate in (L-16217.27) is not proved here.
- This lemma does not prove the arithmetic Poisson profile theorem or RH.
