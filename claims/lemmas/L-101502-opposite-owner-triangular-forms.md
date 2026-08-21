# L-101502: opposite owner triangularizations of a finite Euler correction

Let the commuting operators `U_1,...,U_k` and nonnegative scalars `r_i` be fixed. Put

```text
E = product_i (I-r_i U_i),
C = product_i (I+r_i U_i).
```

Then

```text
CE = product_i (I-r_i^2 U_i^2).
```

## Least-owner form

```text
(C-I)E
 = sum_i r_i U_i
   [product_(h<i)(I-r_h U_h)]
   (I-r_i U_i)
   [product_(h>i)(I-r_h^2 U_h^2)].
```

## Greatest-owner form

```text
(C-I)E
 = sum_i r_i U_i
   [product_(h<i)(I-r_h^2 U_h^2)]
   (I-r_i U_i)
   [product_(h>i)(I-r_h U_h)].
```

## Proof

Write

```text
A_i=I-r_i^2U_i^2,
B_i=I-r_iU_i.
```

Since `A_i-B_i=r_iU_iB_i`, telescope `product A_i-product B_i` once from the left and once from the right. The two displayed identities follow.

These are exact coefficient identities. Positivity or subpower control of either orientation is a separate arithmetic statement.
