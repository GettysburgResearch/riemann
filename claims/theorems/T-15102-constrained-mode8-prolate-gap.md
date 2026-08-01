# T-15102 — The full constrained positive-prolate complement is asymptotically mode 8

Claim ID: `T-15102`  
Status: **PROVED PROLATE-MODEL THEOREM; FIXED-MODE ASYMPTOTICS IMPORTED**  
Authoring agent: `gpt56-pro-11`  
Created: 2026-07-31  
Depends on: `L-15105`, `L-15106`

## 1. Purpose

The statement “mode 8 is the next constrained direction” is not enough. The
actual complement contains every positive-Fourier mode `8,12,16,...`, and an
infinite high-mode combination could in principle exploit the integral
constraint more cheaply than the single mode 8.

This theorem rules out that loophole in the pure prolate model.

## 2. Setup

Let

```text
D e_n=d_n e_n,
0<d_0<d_4<d_8<d_12<...,
```

on the positive Fourier branch `n=0,4,8,...`. Let

```text
l_n=integral e_n,
p=l_4 e_0-l_0 e_4,
s=l_0^2+l_4^2.
```

Define the complete constrained complement

```text
E_lambda
 ={v: <v,p>=0 and integral v=0}                          (T-15102.1)
```

inside the closed positive-Fourier span, and put

```text
gamma_lambda
 =inf_(0!=v in E_lambda) <Dv,v>/||v||^2.                 (T-15102.2)
```

## 3. Exact finite-lambda lower bound

Define the tail leverage

```text
K_tail(lambda)=sum_(n>=8, n divisible by 4) l_n^2/d_n.   (T-15102.3)
```

Then

```text
gamma_lambda
 >= d_8/[1+d_8 K_tail/s].                                (T-15102.4)
```

This bound already controls the **entire** constrained complement.

## 4. Exact mode-8 upper vector

The vector

```text
v_8
 =e_8-(l_8/s)(l_0 e_0+l_4 e_4)                          (T-15102.5)
```

belongs to `E_lambda`. Hence

```text
gamma_lambda
 <= [d_8+(l_8^2/s^2)(d_0l_0^2+d_4l_4^2)]
    /[1+l_8^2/s].                                        (T-15102.6)
```

## 5. Asymptotic limit

Assume the standard fixed-mode prolate limits:

```text
d_4/d_8 ->0,
d_8/d_12 ->0,
l_4^2/l_0^2 ->3/8,
l_8^2/l_0^2 ->35/128.                                    (T-15102.7)
```

Then

```text
boxed: gamma_lambda/d_8(lambda) -> 176/211.              (T-15102.8)
```

Let `mu_lambda` be the `0/4` target Rayleigh quotient from `L-15106`, and set

```text
g_lambda=gamma_lambda-mu_lambda.                          (T-15102.9)
```

Since `mu_lambda/d_8->0`,

```text
boxed: g_lambda/d_8(lambda) ->176/211.                   (T-15102.10)
```

Thus no hidden lower positive mode, no infinite high-mode tail, and no exact
integral correction changes the first complement scale: it is mode 8 with a
nonzero limiting constant.

## 6. Pure-prolate residual/gap ratio

Combining `L-15106` and `L-15105` gives

```text
beta_lambda/g_lambda
 ~ [22155*sqrt(6)/(3964928*pi^4)] lambda^(-8)             (T-15102.11)
```

or numerically

```text
beta_lambda/g_lambda
 ~1.4051173084095943e-4 * lambda^(-8).                   (T-15102.12)
```

Therefore the desired target/gap ratio is completely closed in the pure
prolate angle model.

## 7. Proof

Write a constrained vector as

```text
v=a(l_0e_0+l_4e_4)+z,
z perpendicular to span{e_0,e_4}.
```

The first constraint `<v,p>=0` forces exactly this low-mode direction. The
integral constraint then gives

```text
a=-integral(z)/s.                                        (T-15102.13)
```

Put

```text
T=sum_(n>=8) d_n |z_n|^2.
```

The low-mode energy is nonnegative, so `<Dv,v> >= T`. Also

```text
||z||^2 <= T/d_8,
|integral(z)|^2 <= K_tail*T
```

by the spectral ordering and weighted Cauchy--Schwarz. Therefore

```text
||v||^2
 =||z||^2+|integral(z)|^2/s
 <=T(1/d_8+K_tail/s),
```

which proves (T-15102.4).

For the asymptotic lower bound, monotonicity of the defects and Parseval give

```text
d_8 K_tail
 <=l_8^2+(d_8/d_12) sum_(n>=12)l_n^2
 <=l_8^2+2*lambda*d_8/d_12.                              (T-15102.14)
```

The last term tends to zero because `d_8/d_12=Theta(lambda^-8)`. Thus

```text
liminf gamma/d_8
 >=1/[1+(35/128)/(11/8)]
 =176/211.                                                (T-15102.15)
```

The vector (T-15102.5) satisfies both constraints. Its quotient is exactly
(T-15102.6). The low-mode energy in its numerator is `o(d_8)`, so

```text
limsup gamma/d_8
 <=1/[1+(35/128)/(11/8)]
 =176/211.                                                (T-15102.16)
```

This proves (T-15102.8). The shifted result and (T-15102.11) follow from
`mu/d_8->0`, `beta/d_4->2sqrt(6)/11`, and
`d_4/d_8~105/(4096*pi^4)lambda^-8`. QED.

## 8. Proof boundary

- The finite inequalities (T-15102.4) and (T-15102.6) are exact.
- The asymptotic constant imports the fixed-mode Fuchs and Hermite limits.
- The theorem concerns the pure prolate concentration defect operator. It does
  not yet prove that the complete CCM localized-Weil complement is a relatively
  small perturbation of this model.
