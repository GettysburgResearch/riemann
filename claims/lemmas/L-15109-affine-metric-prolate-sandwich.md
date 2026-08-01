# L-15109 — Affine shifts and source metrics preserve the prolate comparison

Claim ID: `L-15109`  
Status: **PROVED FINITE-DIMENSIONAL GENERALIZED-RAYLEIGH LEMMA**  
Authoring agent: `gpt56-pro-11`  
Created: 2026-07-31  
Depends on: `T-15102`, `L-15107`

## 1. Purpose

The actual CCM source-to-function map need not be an isometry, and the finite
localized Weil matrix may contain a large scalar background. Comparing raw
matrix entries with `I-K_lambda` would therefore be normalization-dependent and
potentially meaningless.

The correct bridge is an affine comparison of **forms in one common Gram
metric**. This lemma makes the shift and metric invariances explicit.

## 2. Generalized setup

Let `G` be positive definite and let `A,D,R` be real symmetric matrices. The
physical Rayleigh quotient is

```text
Rayleigh_A(x)=x^T A x/(x^T G x).                          (L-15109.1)
```

Suppose

```text
A=sigma G+a D+R,
a>0,                                                       (L-15109.2)
```

and the remainder has the Loewner enclosure

```text
-epsilon G <=R<=epsilon G.                                (L-15109.3)
```

Assume `D>=0` and let `p` be a nonzero target. Define its model Rayleigh value

```text
mu_D=p^T D p/(p^T G p),                                   (L-15109.4)
```

and its actual Rayleigh value `mu_A` analogously.

Let `E` be a `G`-orthogonal complement of the target inside the relevant source
constraint space. Suppose the model shifted complement obeys

```text
x^T(D-mu_D G)x>=g_D x^T G x
for every x in E.                                         (L-15109.5)
```

## 3. Floor and gap transfer

Then the actual global lower floor and target excess satisfy

```text
lambda_min(A,G)>=sigma-epsilon,                            (L-15109.6)

mu_A-(sigma-epsilon)
 <=a mu_D+2 epsilon.                                      (L-15109.7)
```

On the target complement,

```text
x^T(A-mu_A G)x
 >=(a g_D-2 epsilon)x^T G x.                              (L-15109.8)
```

Thus, whenever `a g_D>2epsilon`,

```text
boxed:
(mu_A-L_A)/g_A
 <=[a mu_D+2epsilon]/[a g_D-2epsilon],                    (L-15109.9)
```

with the certified choices

```text
L_A=sigma-epsilon,
g_A=a g_D-2epsilon.
```

The scalar shift `sigma` cancels completely.

## 4. Basis/congruence invariance

For every invertible coordinate change `S`, replace

```text
(A,G,D,R,p)
```

by

```text
(S^TAS,S^TGS,S^TDS,S^TRS,S^(-1)p_coordinates).
```

Every generalized Rayleigh value, Loewner statement, floor, gap, and ratio in
this lemma is unchanged. Therefore the comparison may be performed:

- in the orthonormal prolate source basis;
- in the CCM coefficient basis;
- or after exact rational Gram preconditioning;

provided the matrix, target, constraints, and Gram are transformed together.

## 5. Prolate consequence

Use the `0/4` target and complete constrained gap from `L-15106` and `T-15102`:

```text
mu_D=(8/11+o(1))d_4,
g_D=(176/211+o(1))d_8.                                   (L-15109.10)
```

If

```text
epsilon/(a d_8)->0,                                      (L-15109.11)
```

then

```text
(mu_A-L_A)/g_A
 =O(d_4/d_8)+O(epsilon/(a d_8))->0.                       (L-15109.12)
```

With the crude support Hardy conversion, the sufficient strengthened condition
is

```text
lambda^(2tau)
 [d_4/d_8+epsilon/(a d_8)] ->0.                           (L-15109.13)
```

A direct comparison in the Hardy Gram metric removes this artificial support
inflation.

## 6. Proof

From `D>=0` and `R>=-epsilon G`,

```text
A>=(sigma-epsilon)G,
```

which proves (L-15109.6). Also

```text
mu_A
 =sigma+a mu_D+r_p,
|r_p|<=epsilon,
```

so (L-15109.7) follows.

For `x in E`,

```text
x^T(A-mu_A G)x
 =a x^T(D-mu_DG)x
  +x^T R x-r_p x^T G x
 >=[a g_D-2epsilon]x^T G x,
```

proving (L-15109.8)--(L-15109.9). Congruence invariance is the elementary
identity

```text
(Sy)^T A(Sy)/(Sy)^T G(Sy)
 =y^T(S^TAS)y/y^T(S^TGS)y.
```

The asymptotic consequences are immediate. QED.

## 7. Production lesson

Do not compare the localized Weil matrix to `I-K_lambda` entrywise before:

1. identifying the exact transported source Gram;
2. removing an arbitrary scalar multiple of that Gram;
3. applying the same basis adapter to the target and constraints;
4. measuring the remainder in Loewner order relative to the same Gram.

This is the normalization-safe form of the missing trace-form theorem.
