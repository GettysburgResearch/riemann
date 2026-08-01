# L-16214 — Consecutive prolate triples form a polynomially conditioned exact-radical frame

Claim ID: `L-16214`  
Status: **PROVED FINITE FRAME THEOREM; UNIFORM DEFECT-RATIO INPUT OPEN**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: elementary singular-value perturbation; the two source constraints of `T-16201`

## 1. Purpose

`L-16211` proves that the complete projected arithmetic source range is the
finite CCM Fourier space at generic supports, but supplies no quantitative
right inverse. A global basis built by repairing every high prolate mode using
only modes 0 and 4 is badly conditioned: its coefficients contain ratios such
as `d_n/d_4`.

There is a local repair. Every three consecutive positive prolate modes contain
one exact-radical direction. These directions form a banded basis of the entire
two-constraint source space and, under the natural strong defect separation,
are a small perturbation of the ordinary first-difference frame.

## 2. Diagonal data and radical space

Let

```text
0<d_0<d_1<...<d_(M+1),                                   (L-16214.1)
```

and let all `q_j` be nonzero. In the prolate application,

```text
d_j=1-chi_(4j)(lambda),
q_j=e_(4j,lambda)(0).                                    (L-16214.2)
```

In coefficient coordinates `c`, the exact source constraints are

```text
sum_(j=0)^(M+1) q_j c_j=0,

sum_(j=0)^(M+1) d_jq_j c_j=0.                            (L-16214.3)
```

Denote this `M`-dimensional subspace by `R_M`.

Put

```text
x_j=q_jc_j.                                               (L-16214.4)
```

Then the constraints become

```text
sum x_j=0,
sum d_jx_j=0.                                            (L-16214.5)
```

## 3. Local triple vectors

For `0<=j<=M-1`, define the vector `v_j` in the `x` coordinates by

```text
v_j
 =(d_(j+2)-d_(j+1)) e_j
  -(d_(j+2)-d_j) e_(j+1)
  +(d_(j+1)-d_j) e_(j+2).                               (L-16214.6)
```

Both sums in (L-16214.5) vanish exactly. Hence `v_j` belongs to the radical
coefficient space.

Normalize by `d_(j+2)-d_j` and put

```text
r_j=(d_(j+1)-d_j)/(d_(j+2)-d_j),

w_j=(1-r_j)e_j-e_(j+1)+r_je_(j+2).                      (L-16214.7)
```

Thus

```text
w_j=(e_j-e_(j+1))+r_j(e_(j+2)-e_j).                     (L-16214.8)
```

## 4. Exact spanning theorem

The vectors

```text
w_0,...,w_(M-1)                                          (L-16214.9)
```

are linearly independent and form a basis of the space (L-16214.5).

Indeed, the first nonzero coordinate of `w_j` occurs at index `j` with
coefficient `1-r_j>0`. Successive elimination proves independence. There are
`M` vectors in an `M`-dimensional constraint space, so they span it.

Returning to the original coefficients gives the exact-radical sources

```text
u_j=diag(q_0^-1,...,q_(M+1)^-1) w_j.                    (L-16214.10)
```

## 5. Difference-frame comparison

Let `B_0` be the `(M+2) x M` matrix with columns

```text
e_j-e_(j+1),                                             (L-16214.11)
```

and let `B` have columns `w_j`. Then

```text
B=B_0+E,                                                  (L-16214.12)
```

where every column of `E` is `r_j(e_(j+2)-e_j)`.

The row and column sums give

```text
boxed:
||E||_op<=2r_*,
r_*:=max_j r_j.                                          (L-16214.13)
```

The singular values of `B_0` are explicit:

```text
s_k(B_0)=2sin(k pi/[2(M+1)]),
1<=k<=M.                                                  (L-16214.14)
```

Therefore Weyl's singular-value inequality gives

```text
boxed:
s_min(B)
 >=2sin(pi/[2(M+1)])-2r_*,                               (L-16214.15)

s_max(B)
 <=2+2r_*.                                               (L-16214.16)
```

In particular, if

```text
(M+1)r_*<=rho<pi/2,                                      (L-16214.17)
```

then

```text
s_min(B)>=c_rho/(M+1),
s_max(B)<=3,                                              (L-16214.18)
```

and the Euclidean frame condition number is `O(M)`.

## 6. Point-value scaling

Let

```text
q_min=min_j|q_j|,
q_max=max_j|q_j|.                                        (L-16214.19)
```

For the original coefficient frame `U=diag(q)^(-1)B`,

```text
boxed:
s_min(U)>=s_min(B)/q_max,

s_max(U)<=s_max(B)/q_min.                                (L-16214.20)
```

Thus

```text
boxed:
kappa(U)
 <=(q_max/q_min)
   (2+2r_*)/[2sin(pi/(2(M+1)))-2r_*].                    (L-16214.21)
```

If `q_max/q_min` grows polynomially in `M` and `(M+1)r_*->0`, the exact-radical
frame is polynomially conditioned.

For fixed-mode Hermite point values with indices `4j`, the ratio is expected to
be only polynomial by the central-binomial asymptotics. A production proof must
insert the uniform prolate-to-Hermite point-value estimate for the growing
schedule.

## 7. Defect-energy localization

Let `D=diag(d_0,...,d_(M+1))`. For a normalized local vector `w_j`,

```text
w_j^TDw_j
 =(1-r_j)^2d_j+d_(j+1)+r_j^2d_(j+2).                    (L-16214.22)
```

Since

```text
r_j<= (d_(j+1)-d_j)/(d_(j+2)-d_(j+1)),                  (L-16214.23)
```

strong adjacent separation makes the last term lower order and gives

```text
w_j^TDw_j=Theta(d_(j+1)).                                (L-16214.24)
```

Thus the local frame orders its directions by the next prolate defect rather
than importing the huge ratio `d_n/d_4` into a global repair.

## 8. Quadratic-log schedule

Let

```text
M_lambda=O((log lambda)^2)                               (L-16214.25)
```

as supplied by `L-16213`. A sufficient prolate input is

```text
boxed:
M_lambda r_*(lambda)->0,                                 (L-16214.26)

q_max(lambda)/q_min(lambda)
 <=M_lambda^C.                                           (L-16214.27)
```

Then the complete exact-radical coefficient frame has only polylogarithmic
condition number.

The fixed-index Fuchs hierarchy suggests much more:

```text
r_j approximately d_(j+1)/d_(j+2)
 =O(poly(j)/lambda^8).                                   (L-16214.28)
```

If this estimate is made uniform for `j<=M_lambda`, (L-16214.26) follows with a
large margin. It is recorded as motivation, not used in the finite theorem.

## 9. Consequence for gate 3

The algebraic and coefficient-conditioning parts of the growing source right
inverse are now explicit. The background is represented by local exact-radical
sources whose coefficient condition number is polynomial in the cutoff.

What remains is to transport this frame through:

1. the arithmetic map `E` and finite Fourier projection;
2. the omitted-tail metric;
3. the local Weyl scalarization.

The required lower bound is no longer an arbitrary background positivity
statement. It is a quantitative frame inequality for the banded basis
(L-16214.10).

## 10. Proof boundary

The finite frame theorem is exact. The uniform prolate defect-ratio estimate,
growing point-value comparison, and arithmetic-image frame bound are not proved.
No RH proof is claimed.
