# L-16204 — Tail scalarization is exactly a generalized spectral-diameter problem

Claim ID: `L-16204`  
Status: **PROVED FINITE-DIMENSIONAL SPECTRAL LEMMA**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: `L-16203`

## 1. Purpose

`L-16203` reduces the source-block comparison to scalarization of the Weil form
on the omitted tail space. This lemma identifies the exact best scalar and
remainder. On a fixed `0/4/8` source packet, the missing asymptotic theorem is
therefore only a two- or three-dimensional generalized eigenvalue-clustering
problem.

## 2. Setup

Let `D` be a positive-definite Hermitian tail Gram matrix and let `A` be the
Hermitian matrix of the Weil form on the same tail coefficient space. Define

```text
H=D^(-1/2) A D^(-1/2),                                   (L-16204.1)
```

and

```text
||R||_D=||D^(-1/2) R D^(-1/2)||_op.                     (L-16204.2)
```

The generalized eigenvalues of `(A,D)` are the ordinary eigenvalues of `H`.
Write

```text
m=lambda_min(H),
M=lambda_max(H).                                         (L-16204.3)
```

## 3. Exact best scalarization

Then

```text
boxed:
inf_(a in R)||A-aD||_D=(M-m)/2.                          (L-16204.4)
```

The unique best scalar when `M>m` is

```text
boxed:
a_*=(M+m)/2.                                             (L-16204.5)
```

If `m>0`, the scale-free optimal relative remainder is

```text
boxed:
inf_(a>0) ||A-aD||_D/a
 =(M-m)/(M+m)
 =(kappa-1)/(kappa+1),                                   (L-16204.6)
```

where `kappa=M/m` is the generalized condition number.

Consequently boundary scalarization is equivalent to

```text
boxed:
kappa(A,D)->1.                                           (L-16204.7)
```

The absolute size of the tail Gram does not enter this invariant.

## 4. Exact two-dimensional formula

In a `D`-orthonormal basis of a two-dimensional tail sector, write

```text
H=[[x,z],[conj(z),y]].                                    (L-16204.8)
```

Then

```text
boxed:
M-m=sqrt((x-y)^2+4|z|^2),                                (L-16204.9)

a_*=(x+y)/2,                                             (L-16204.10)

epsilon_*=(1/2)sqrt((x-y)^2+4|z|^2).                    (L-16204.11)
```

Thus the relative bridge is exactly the pair of statements

```text
(x-y)/(x+y)->0,
z/(x+y)->0,                                               (L-16204.12)
```

with `x+y` positive. In words:

1. the two normalized boundary tails have the same leading Weil energy;
2. their normalized cross-Weil pairing is lower order.

## 5. Coordinate-free two-dimensional invariant

No matrix square root is required. Let

```text
T=tr(D^(-1)A),
Delta=det(A)/det(D).                                      (L-16204.13)
```

Then

```text
(M-m)^2=T^2-4Delta,                                      (L-16204.14)

a_*=T/2,                                                 (L-16204.15)
```

and, when `T>0`,

```text
boxed:
epsilon_*/a_*=sqrt(T^2-4Delta)/T.                        (L-16204.16)
```

This supplies an exact rational proof interface for rational matrix enclosures:
certify `T>0` and a sufficiently small nonnegative upper bound for
`T^2-4Delta` relative to `T^2`.

## 6. Fixed-dimensional trace-variance certificate

For dimension `r`, put

```text
abar=tr(H)/r,
V=tr(H^2)-tr(H)^2/r
 =||H-abar I||_F^2.                                      (L-16204.17)
```

Then

```text
boxed:
||A-abar D||_D
 <=sqrt(V).                                               (L-16204.18)
```

Therefore a finite proof-producing sufficient condition for scalarization is

```text
abar>0,
lambda^(2tau) sqrt(V)/abar ->0.                          (L-16204.19)
```

When the dimension `r` is fixed, `V` is a finite polynomial/rational expression
in the entries of `A` and `D^(-1)` after directed enclosure.

## 7. Combination with the radical-tail factorization

Under `L-16203`,

```text
A=T_tail^* q T_tail,
D=T_tail^* T_tail.                                       (L-16204.20)
```

Thus `H` is simply the matrix of the Weil form in a `D`-orthonormal basis of
the omitted-tail range. The desired source-sector comparison follows if

```text
lambda^(2tau_lambda)
 [lambda_max(H_lambda)-lambda_min(H_lambda)]
 /[lambda_max(H_lambda)+lambda_min(H_lambda)] ->0.        (L-16204.21)
```

No `d_8` appears in (L-16204.21): it has already been factored into the tail
Gram `D`. Once `||D||_(G_S)=O(d_8)`, equations (L-16204.4)--(L-16204.6) and
`L-16203` recover

```text
lambda^(2tau)||R_S||_(G_S)/(a_* d_8)->0.                 (L-16204.22)
```

## 8. Proof

For self-adjoint `H`,

```text
||H-aI||_op=max{|M-a|,|m-a|}.                            (L-16204.23)
```

The maximum of the distances to the endpoints is minimized exactly at their
midpoint, with value half their separation. This proves
(L-16204.4)--(L-16204.5). If `m>0`, substituting the midpoint proves
(L-16204.6)--(L-16204.7).

The eigenvalues of (L-16204.8) give (L-16204.9)--(L-16204.11). The trace and
determinant are the sum and product of the generalized eigenvalues, proving
(L-16204.13)--(L-16204.16).

Finally,

```text
||H-abar I||_op<=||H-abar I||_F=sqrt(V),
```

which proves (L-16204.18)--(L-16204.19). The final statements follow by
substitution into `L-16203`. QED.

## 9. Production implication

The next analytic calculation should not start with the complete localized
matrix. It should construct the exact omitted-tail vectors for the target and
the first constrained mode, then evaluate only

```text
<tail_target,tail_target>,
<tail_target,tail_8>,
<tail_8,tail_8>,

q(tail_target,tail_target),
q(tail_target,tail_8),
q(tail_8,tail_8).                                        (L-16204.24)
```

These six pairings decide the optimal two-dimensional scalarization exactly.
A third source mode adds only the finite trace-variance criterion
(L-16204.17). This is the smallest falsifiable form of the remaining bridge.

## 10. Proof boundary

The spectral lemma is exact. It does not prove that the production normalized
tail Weil energies cluster, that the source tails have `d_8` Gram scale after
the arithmetic `E` map, or that the background block satisfies the gates in
`L-16201`. No RH proof is claimed.
