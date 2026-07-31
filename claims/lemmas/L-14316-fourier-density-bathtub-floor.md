# L-14316 — Fourier-density bathtub floor

Claim ID: `L-14316`  
Status: `PROPOSED`  
Author: `gpt56-02-m`  
Created: 2026-07-31  
Dependencies: Plancherel, Cauchy--Schwarz, the exact Suzuki multiplier normalization in `L-14311`  
Related candidates: none

## Statement

Let `T=[-L/2,L/2]`, extend `w in L2(T)` by zero, and use

```text
hat(w)(xi)=integral_T w(x) exp(i xi x) dx,
||w||^2=(1/(2 pi)) integral |hat(w)|^2.
```

For a measurable real symbol `s`, put

```text
q_s(w)=(1/(2 pi)) integral s(xi)|hat(w)(xi)|^2 dxi.
```

Whenever `(G-s)_+` is integrable,

```text
q_s(w)/||w||^2
>= G-L/(2 pi) integral (G-s(xi))_+ dxi.                 (1)
```

Therefore

```text
inf q_s(w)/||w||^2 >= B_L(s),
B_L(s)=sup_G [G-L/(2 pi) integral (G-s)_+].             (2)
```

For Suzuki's scaled interval `[-1,1]`,

```text
B_2(s)=sup_G [G-(1/pi) integral (G-s)_+].               (3)
```

## Proof

Cauchy--Schwarz gives `|hat(w)(xi)|^2 <= L ||w||^2`. Hence

```text
p_w(xi)=|hat(w)(xi)|^2/(2 pi ||w||^2)
```

is a probability density with `p_w <= L/(2 pi)`. Since
`s >= G-(G-s)_+`, integration against `p_w` gives (1). Taking the supremum over
`G` gives (2).

## Bathtub interpretation

If all Paley--Wiener correlations are discarded and only

```text
p>=0, integral p=1, p<=L/(2 pi)
```

is retained, the bathtub principle gives

```text
B_L(s)
= L/(2 pi) * inf_(|E|=2 pi/L) integral_E s(xi) dxi.
```

Thus `B_2(s)` is the average of the lowest `pi` units of symbol measure. It is
the strongest lower bound using only the exact symbol and the support-length
pointwise density cap.

## Weighted low-packet consequence

Let `d_G=(G-s)_+` and

```text
D_G=P_T F^-1 M_(d_G) F P_T.
```

Then `D_G` is positive trace class,

```text
Tr(D_G)=L/(2 pi) integral d_G,
A_s >= G I-D_G.
```

Consequently

```text
inf spectrum(A_s) >= G-Tr(D_G),
# {eigenvalues below G-epsilon}
<= L/(2 pi epsilon) integral d_G.
```

This is a weighted version of `L-14311`: it charges integrated deficit rather
than the measure of a binary bad set.

## Finite directed certificate

For disjoint rational cells `I_j`, directed bounds `s>=L_j` on each cell, and a
tail gate `s>=G` outside their union,

```text
integral (G-s)_+ <= sum_j |I_j|(G-L_j)_+.
```

Using `333/106 < pi` on `[-1,1]`,

```text
q_s(w)
>= [G-(106/333) sum_j |I_j|(G-L_j)_+] ||w||^2.         (4)
```

The right side is concave piecewise linear in `G`; its finite optimum occurs at
the tail floor or a cell lower bound. `X-14309` verifies (4) with exact rational
arithmetic.

## Suzuki specialization

Let `s_a` be the exact real multiplier for Suzuki's scaled localized Weil form,
with the signs and Fourier normalization independently audited from equations
(4.5)--(4.6). Then the localized ground value satisfies

```text
mu_a >= B_2(s_a).                                      (5)
```

This is a direct ambient floor. It requires no prolate eigenfunction, low-block
Schur complement, ground-state parity, or convergence to a conjectural target.

## Boundaries

- The abstract theorem is exact.
- Applying (5) still requires a proof-grade complete symbol and analytic tail.
- A midpoint plot is not a deficit-integral certificate.
- A negative finite lower bound says nothing about RH.
- No cofinal estimate `liminf B_2(s_a)>=0` is currently proved.

The new proof-oriented observable is the average of the lowest `pi` units of
frequency-symbol measure, not the sampled symbol minimum.
