# L-16209 — Riemann--von Mangoldt gives universal high-frequency tail scalarization

Claim ID: `L-16209`  
Status: **PROVED ABSTRACT LOCAL-WEYL THEOREM; PROLATE PROFILE GATE OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: Riemann--von Mangoldt formula; `L-16204`, `L-16206`

## 1. Purpose

The omitted multiplicative prolate tails occupy a shrinking boundary layer in
logarithmic coordinates. Their Mellin transforms therefore probe zeta zeros at
a growing frequency scale `R_lambda`. On that scale, the zero counting measure
has the universal density

```text
(1/(2pi)) log(|gamma|/(2pi)).                             (L-16209.1)
```

The leading `log R_lambda` part is scalar. This lemma proves that the normalized
tail Weil matrix automatically scalarizes for every fixed packet whose rescaled
profiles have uniform mild regularity.

No RH assumption is used.

## 2. Zero parameters

Write every nontrivial zero, with multiplicity, as

```text
rho=1/2+i s_rho,
|Im s_rho|<1/2.                                           (L-16209.2)
```

The real part of `s_rho` is the ordinary zero ordinate. The positive-ordinate
count satisfies

```text
N(T)
 =T/(2pi) log(T/(2pi))-T/(2pi)+O(log(T+2)).              (L-16209.3)
```

The zero set is stable under conjugation and `rho->1-rho`.

## 3. Uniform profile class

Fix a packet size `r`. For every scale `R>=2`, let

```text
Phi_(j,R)(z), 1<=j<=r,                                   (L-16209.4)
```

be holomorphic on `|Im z|<=1/R` and suppose there is one integrable envelope
`W` such that, uniformly in `R,j` and `|y|<=1/R`,

```text
|Phi_(j,R)(x+iy)|
 +|partial_z Phi_(j,R)(x+iy)|
 <=W(x),                                                  (L-16209.5)
```

with

```text
integral_R W(x)^2[1+|log|x||]dx<infinity,

integral_R W(x)|W'(x)|[1+log(2+|x|)]dx<infinity          (L-16209.6)
```

in any equivalent absolutely-continuous envelope formulation. It is sufficient,
for example, that the profiles and their first derivatives are uniformly
`O((1+|x|)^(-2))` and uniformly bounded near zero.

Define the profile Gram

```text
D_R,(jk)
 =(1/(2pi)) integral_R
   conjugate(Phi_(j,R)(x)) Phi_(k,R)(x)dx.                (L-16209.7)
```

Assume

```text
D_R>=cI                                                       (L-16209.8)
```

for one `c>0` independent of `R`.

## 4. Scaled zero-side matrix

Define

```text
A_R,(jk)
 =(1/R) sum_rho
  conjugate(Phi_(j,R)(conjugate(s_rho)/R))
  Phi_(k,R)(s_rho/R).                                    (L-16209.9)
```

The sum is absolutely convergent under the profile assumptions.

Then

```text
boxed:
A_R=(log R)D_R+C_R+E_R,                                  (L-16209.10)
```

where

```text
C_R,(jk)
 =(1/(2pi)) integral_R
  conjugate(Phi_(j,R)(x))Phi_(k,R)(x)
  log(|x|/(2pi))dx                                       (L-16209.11)
```

and

```text
boxed:
||C_R||_op<=C,
||E_R||_op<=C log R/R.                                   (L-16209.12)
```

The constant depends only on the packet size and uniform profile envelope.

## 5. Generalized eigenvalue clustering

Let

```text
m_R=lambda_min(A_R,D_R),
M_R=lambda_max(A_R,D_R).                                 (L-16209.13)
```

Then

```text
boxed:
m_R=log R+O(1),
M_R=log R+O(1),                                          (L-16209.14)

(M_R-m_R)/(M_R+m_R)=O(1/log R)->0.                       (L-16209.15)
```

Thus the optimal scalarization criterion of `L-16204` holds universally.

The best scalar is

```text
a_R=(M_R+m_R)/2=log R+O(1),                              (L-16209.16)
```

and

```text
boxed:
inf_a ||A_R-aD_R||_(D_R)/a=O(1/log R).                  (L-16209.17)
```

## 6. Proof for real ordinates

First replace the complex zero parameters by their real ordinates and put

```text
H_R,(jk)(x)
 =conjugate(Phi_(j,R)(x))Phi_(k,R)(x).                   (L-16209.18)
```

For positive ordinates, Stieltjes integration gives

```text
(1/R) sum_(gamma>0) H_R(gamma/R)
 =(1/R) integral_0^infinity H_R(t/R)dN(t).                (L-16209.19)
```

Write

```text
N(t)=M(t)+S(t),

M(t)=t/(2pi)log(t/(2pi))-t/(2pi)+7/8,
S(t)=O(log(t+2)).                                        (L-16209.20)
```

Since

```text
M'(t)=(1/(2pi))log(t/(2pi)),                             (L-16209.21)
```

the main term, after `t=Rx`, is

```text
(log R)/(2pi) integral_0^infinity H_R(x)dx

 +(1/(2pi)) integral_0^infinity
   H_R(x)log(x/(2pi))dx.                                 (L-16209.22)
```

The negative ordinates give the corresponding negative-half-line integrals.
Together they are exactly `(log R)D_R+C_R`.

For the error term, Stieltjes integration by parts gives

```text
(1/R) integral H_R(t/R)dS(t)
 =-(1/R) integral_0^infinity S(Rx)H_R'(x)dx              (L-16209.23)
```

up to vanishing boundary terms. The uniform envelope and
`S(Rx)=O(log R+log(2+x))` imply `O(log R/R)`.

## 7. Off-critical horizontal displacement

For a zero parameter

```text
s_rho=gamma+i beta_tilde,
|beta_tilde|<1/2,                                        (L-16209.24)
```

Taylor's theorem and (L-16209.5) give

```text
Phi_(j,R)(s_rho/R)
 =Phi_(j,R)(gamma/R)+O(R^-1 W(gamma/R)).                 (L-16209.25)
```

The product error is `O(R^-1 W^2)`. Summing with the outer factor `1/R` and
using (L-16209.3) gives another `O(log R/R)`. Thus off-critical real parts do
not affect the leading scalarization, and (L-16209.10)--(L-16209.12) hold
without RH.

## 8. Generalized spectrum

Whiten by `D_R`. Equations (L-16209.10)--(L-16209.12) and (L-16209.8) give

```text
D_R^(-1/2)A_RD_R^(-1/2)
 =log R I+O_op(1).                                       (L-16209.26)
```

The min--max principle proves (L-16209.14). The remaining statements follow
from `L-16204`. QED.

## 9. Application to omitted logarithmic boundary tails

Let `T_(j,lambda)(x)` be omitted source tails in logarithmic coordinates,
centered at a boundary point `x_lambda`, and let `R_lambda->infinity`. Define
profiles by

```text
widehat(T_(j,lambda))(s)
 =R_lambda^(-1/2)e^(-is x_lambda)
  Phi_(j,R_lambda)(s/R_lambda).                           (L-16209.27)
```

Mellin Plancherel identifies their ordinary tail Gram with `D_R`, while the
zero-side Weil matrix is exactly `A_R` by `L-16206`. Therefore the normalized
tail Weil form scalarizes if:

1. the profiles satisfy the uniform envelope (L-16209.5)--(L-16209.6);
2. their Gram remains uniformly positive;
3. `R_lambda->infinity`.

For the Hermite boundary layer suggested by the fixed-mode prolate asymptotics,

```text
R_lambda asymptotic to lambda^2,                          (L-16209.28)
```

so the relative scalarization rate is `O(1/log lambda)`.

## 10. Consequence for the positive route

Combined with the source-specific Hardy control `L-16208`, the source-sector
remainder satisfies the corrected requirement

```text
||R_source,lambda||/(a_lambda d_8(lambda))->0             (L-16209.29)
```

as soon as the prolate omitted tails admit the uniform rescaled profile
representation. No factor `lambda^(2tau)` is required.

## 11. Proof boundary

The zero-measure theorem is complete. What remains unproved is the
prolate-specific uniform boundary-profile statement (L-16209.27)--(L-16209.28)
and the alias suppression of `L-16207`, together with the global floor and
background coupling gates. No RH proof is claimed.
