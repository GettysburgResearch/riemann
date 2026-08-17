# L-96600 — Positive parity source and exact nonduplicating rough-prime hazard identity

For each squarefree `k`, retain a positive copy of the canonical packet with parity label `(-1)^omega(k)`. Signed row observation gives the exact native rows.

For ordered rough primes `p_i>=67`, put

```text
r_i=p_i^(-1/2)
s_i=product_(h<=i)(1-r_h)
lambda_i=r_i s_(i-1)
alpha_i=r_i lambda_i.
```

Then

```text
s_k+sum lambda_i=1
sum alpha_i<1/sqrt(67)<1/8
```

and for every labelled packet `P_Z`,

```text
P_Z
 =s_k P_Z
  +sum_i lambda_i(P_Z-r_i A_(p_i)P_(Z/p_i))
  +sum_i alpha_i A_(p_i)P_(Z/p_i).
```

The equality is source-level and coefficientwise. Parity/history labels commute with every term. No rough-density estimate is used.
