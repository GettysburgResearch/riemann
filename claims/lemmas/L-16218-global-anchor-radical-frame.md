# L-16218 — A global two-anchor frame removes the uniform Fuchs-window gate

Claim ID: `L-16218`  
Status: **PROVED FINITE ALGEBRA AND ASYMPTOTIC TRANSFER**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Depends on: monotonicity of the positive prolate defects; fixed ratios
`d_4/d_8,d_8/d_12`; a growing-window point-value bound

## 1. Purpose

`L-16214/L-16215` constructed a local consecutive-triple radical frame. Its
conditioning estimate used a uniform Fuchs approximation for every defect up to
mode `O(log^2 lambda)`.

That strong input is unnecessary. The two radical constraints can be solved by
two global anchor coordinates. The resulting frame has an exact dimension-only
condition bound and uses no adjacent defect ratio. The complete low hierarchy
then needs only the fixed ratios `d_4/d_8` and `d_8/d_12`.

## 2. Abstract radical coordinates

Let

```text
d_0<d_1<...<d_H,                                         (L-16218.1)
q_j!=0,                                                   (L-16218.2)
```

and let the source coefficient vector be `c=(c_0,...,c_H)`. Put

```text
x_j=q_j c_j.                                              (L-16218.3)
```

The two exact source-radical conditions are

```text
sum_(j=0)^H x_j=0,
sum_(j=0)^H d_j x_j=0.                                   (L-16218.4)
```

Use coordinates `0` and `H` as anchors. For `1<=j<=H-1`, define

```text
A_j=(d_H-d_j)/(d_H-d_0),
B_j=(d_j-d_0)/(d_H-d_0),                                 (L-16218.5)

w_j=e_j-A_j e_0-B_j e_H.                                 (L-16218.6)
```

Then

```text
A_j+B_j=1,
d_j-A_jd_0-B_jd_H=0,                                    (L-16218.7)
```

so every `w_j` satisfies both constraints exactly.

## 3. Exact basis and singular values

The vectors

```text
w_1,...,w_(H-1)                                           (L-16218.8)
```

form a basis of the complete codimension-two radical space: the `j`th free
coordinate of `w_j` is one and all other free coordinates vanish.

Let `W:C^(H-1)->C^(H+1)` be their synthesis matrix and write

```text
A=(A_1,...,A_(H-1))^T,
B=(B_1,...,B_(H-1))^T.                                   (L-16218.9)
```

For every free coefficient vector `z`,

```text
||Wz||_2^2
 =||z||_2^2+|A^Tz|^2+|B^Tz|^2.                          (L-16218.10)
```

Therefore

```text
boxed:
s_min(W)>=1.                                             (L-16218.11)
```

Since `0<=A_j,B_j<=1` and `A_j^2+B_j^2<=1`,

```text
||A||_2^2+||B||_2^2<=H-1,                                (L-16218.12)
```

and hence

```text
boxed:
s_max(W)<=sqrt(H).                                       (L-16218.13)
```

No defect-spacing estimate occurs.

## 4. Return to the original source coefficients

Let

```text
Q=diag(q_0,...,q_H),                                     (L-16218.14)
```

and define the original coefficient frame

```text
U=Q^(-1)W.                                                (L-16218.15)
```

Put

```text
q_min=min_j|q_j|,
q_max=max_j|q_j|.                                        (L-16218.16)
```

Then

```text
s_min(U)>=1/q_max,
s_max(U)<=sqrt(H)/q_min,                                 (L-16218.17)
```

so

```text
boxed:
kappa(U)<=sqrt(H) q_max/q_min.                           (L-16218.18)
```

For the even Hermite point-value scale

```text
|Q_(2m)(0)|^2/|Q_0(0)|^2=binomial(2m,m)/4^m,             (L-16218.19)
```

Wallis bounds give, on the modes `0,4,...,4H`,

```text
q_max/q_min=O(H^(1/4))                                   (L-16218.20)
```

whenever the finite prolate point values are uniformly comparable to their
Hermite limits. Thus

```text
boxed:
kappa(U)=O(H^(3/4)).                                     (L-16218.21)
```

For `H=O((log lambda)^2)`, this is only

```text
O((log lambda)^(3/2)).                                   (L-16218.22)
```

This improves the `O((log lambda)^(5/2))` bound from the local-triple frame and
removes every growing-window defect-ratio hypothesis.

## 5. The tail-susceptibility gates need only fixed Fuchs ratios

Now restore the positive-prolate labels `n=0,4,8,...,4H`. Assume only the
point-value upper bound

```text
q_(4j)^2<=C(j+1)^(-1/2),                                 (L-16218.23)
```

uniformly for `0<=j<=H`. Then

```text
sum_(j=0)^H q_(4j)^2<=C' sqrt(H+1).                       (L-16218.24)
```

Since the concentration defects increase with mode,

```text
boxed:
d_4 sum_(j>=2) q_(4j)^2/d_(4j)
 <=C' sqrt(H) d_4/d_8,                                   (L-16218.25)

boxed:
d_8 sum_(j>=3) q_(4j)^2/d_(4j)
 <=C' sqrt(H) d_8/d_12.                                  (L-16218.26)
```

The fixed-index Fuchs ratios give

```text
d_4/d_8=Theta(lambda^-8),
d_8/d_12=Theta(lambda^-8).                               (L-16218.27)
```

Consequently, on the quadratic-log schedule,

```text
boxed:
H=O((log lambda)^2)
 =>
(L-16218.25),(L-16218.26)->0.                            (L-16218.28)
```

Thus the rank-one constrained mode-4/mode-8 hierarchy of `T-16201` survives the
entire growing packet using only fixed-mode Fuchs information.

## 6. What uniform asymptotics remain necessary

The growing packet still needs a point-value comparison of the form

```text
c(j+1)^(-1/4)
 <=|q_(4j)|/|q_0|
 <=C(j+1)^(-1/4),                                        (L-16218.29)
```

for `j<=O(log^2 lambda)`. This is an angular/Hermite approximation problem, not
a concentration-eigenvalue problem. `L-16219` supplies a direct
harmonic-oscillator route to it.

The general Fuchs formula

```text
d_n~2^(3n+1)sqrt(pi)gamma^(n+1/2)e^(-2gamma)/n!
```

need no longer be proved uniformly over the growing frame. Only its three fixed
specializations controlling `d_4/d_8` and `d_8/d_12` enter the low hierarchy.

## 7. Strategic consequence

The prior missing item

```text
uniform Fuchs asymptotics for n=O(log^2 lambda)
```

is removed from the RH-critical gate list. It is replaced by:

```text
uniform Hermite point-value comparability on that window,
fixed-index defect ratios for modes 4,8,12.                (L-16218.30)
```

The former is polynomial-scale and may be obtained from the differential
operator; the latter is already a fixed-mode asymptotic question.

## 8. Proof boundary

- The frame, singular-value bounds and susceptibility reductions are exact.
- The uniform point-value comparison is proved separately only after the domain
  and labeling gates in `L-16219` are accepted.
- No arithmetic tail-profile scalarization or RH conclusion is asserted here.
