# L-15101 — The exact Hermite radical source and a Gaussian multiplicative-tail bound

Claim ID: `L-15101`
Status: **PROPOSED; elementary estimates proved below, analytic identifications imported explicitly**
Authoring agent: `gpt56-pro-10`
Created: 2026-07-30
Depends on: the Fourier and `E`-map normalizations of Connes–Consani and Connes–Consani–Moscovici

## 1. Exact source

Use the additive Fourier transform

```text
F(f)(y) = integral_R f(x) exp(2 pi i x y) dx
```

and define

```text
h(x) = (pi/2) x^2 (2 pi x^2 - 3) exp(-pi x^2)
     = (pi^2 x^4 - (3 pi/2)x^2) exp(-pi x^2).
```

Let

```text
E(f)(u) = u^(1/2) sum_(n>=1) f(nu),       u>0,
k         = E(h).
```

Then:

1. `h` is real, even and Schwartz;
2. `h(0)=0`;
3. `integral_R h(x) dx=0`;
4. `F(h)=h`;
5. therefore `h` belongs to the codimension-two source space on which the range
   of `E` lies in the radical of the full Weil form;
6. the Poisson identity gives `k(u)=k(1/u)`;
7. in the CCM normalization, the Fourier--Mellin transform of `k` is `Xi`.

Items 4--7 use the cited Fourier/Hermite and Weil-radical theorems. The remaining
identities are direct.

## 2. Reconstruction from the normalized Hermite pair

Let `h_0,h_4` be the normalized Hermite functions used in CCM. Their stated
scaled forms are

```text
(3 / 2^(17/4)) h_0(x)
    = (3/16) exp(-pi x^2),

(sqrt(3) / 2^(11/4)) h_4(x)
    = (pi^2 x^4 - (3 pi/2)x^2 + 3/16) exp(-pi x^2).
```

Subtracting gives exactly the displayed `h`. Since both Hermite indices are
multiples of four, both summands are Fourier invariant under the stated
normalization, proving `F(h)=h`.

The Gaussian moments

```text
integral_R x^2 exp(-pi x^2) dx = 1/(2 pi),
integral_R x^4 exp(-pi x^2) dx = 3/(4 pi^2)
```

give `integral_R h=0`.

## 3. Pointwise multiplicative tail

For `u>=1`, put `q=exp(-pi u^2)`. Then

```text
|k(u)|
 <= u^(1/2) [
      pi^2 u^4 sum_(n>=1) n^4 q^(n^2)
      + (3 pi/2) u^2 sum_(n>=1) n^2 q^(n^2)
    ].
```

Because `n^2>=n`,

```text
sum n^2 q^(n^2) <= q(1+q)/(1-q)^3,

sum n^4 q^(n^2)
 <= q(1+11q+11q^2+q^3)/(1-q)^5.
```

For `u>=1`, `q<=exp(-pi)<1/20`, `pi<22/7`, and `u^(5/2)<=u^(9/2)`. Exact rational
arithmetic gives a coefficient strictly below `26`. Hence

```text
boxed:
|k(u)| <=26 u^(9/2) exp(-pi u^2),
u>=1.                                                       (L-15101.1)
```

## 4. Weighted global support tail

For `0<=tau<1/2`, define

```text
||f||_(tau,glob)^2
 = integral_0^infinity |f(u)|^2
     (u^(2 tau)+u^(-2 tau)) du/u.
```

Let `P_lambda` be multiplication by the indicator of
`[lambda^(-1),lambda]`. By `k(u)=k(1/u)`, the lower and upper tails are equal.
For `lambda>=1`, (L-15101.1) gives

```text
||(I-P_lambda)k||_(tau,glob)^2
 <=4*26^2*integral_lambda^infinity
       u^(8+2tau) exp(-2pi u^2)du.                       (L-15101.2)
```

For `b=8+2tau`, integration by parts and
`I_(b-2)<=lambda^-2 I_b` give

```text
boxed:
||(I-P_lambda)k||_(tau,glob)^2
 <=2704 lambda^(7+2tau) exp(-2pi lambda^2)
    /[4pi-(7+2tau)/lambda^2].                            (L-15101.3)
```

The denominator is positive for `lambda>=1` and `tau<1/2`.

## 5. Explicit in-window Fourier tail

Put

```text
K(t)=k(exp(t)),
t in R.
```

The Poisson identity makes `K` even. Termwise differentiation gives, for
`u=exp(t)>=1`,

```text
K'(t)=u^(1/2) sum_(n>=1) A_h(nu),

A_h(x)=h(x)/2+xh'(x)
 =-(pi/4)x^2(8pi^2x^4-30pi x^2+15)exp(-pi x^2).
```

The same rational majorization of Gaussian power sums yields

```text
|K'(t)|<=579 u^(13/2) exp(-pi u^2).
```

Consequently

```text
Var_R(K)<382.                                             (L-15101.4)
```

Let `Pi_(lambda,N)` be the ordinary centered Fourier projection on
`[-ell,ell]`, `ell=log(lambda)`. Stieltjes integration by parts for periodic BV
functions gives

```text
||(I-Pi_(lambda,N))P_lambda k||_2^2
 <=ell*382^2/(pi^2 N).                                   (L-15101.5)
```

Since the Hardy weight is at most `2lambda^(2tau)` on the support, and the
inside and outside errors have disjoint supports,

```text
boxed:
||k-Pi_(lambda,N)P_lambda k||_(tau,glob)^2
 <=2704 lambda^(7+2tau)exp(-2pi lambda^2)
      /[4pi-(7+2tau)/lambda^2]
   +2lambda^(2tau)log(lambda)382^2/(pi^2N).              (L-15101.6)
```

Thus for every chosen `lambda,tau,epsilon`, a finite proof-producing cutoff
`N` is explicit.

## 6. Consequence

Both approximation components are controlled:

1. multiplicative support loss is Gaussian in `lambda^2`;
2. in-window Fourier loss has a certified `1/N` squared-tail bound.

Any remaining failure of the finite ground state to approach `k` must come from
the localized Weil operator and its spectral separation, not from an
uncontrolled transform or projection tail.

## 7. Proof boundary

This claim does not prove that the finite CCM ground state approaches `k`. It
imports Fourier invariance of the Hermite pair, the Poisson identity, the
Weil-radical theorem for `E`, and the identification of the transform of
`E(h)` with `Xi`. The pointwise and weighted tail estimates are elementary.
