# L-99701 — Native first ownership and a symmetric Euler homotopy preserve every rough coefficient

Claim ID: `L-99701`  
Status: **PROVED EXACT OPERATOR IDENTITY**  
Created: 2026-08-20  
Depends on: PR #652 native-coefficient firewall  
RH status: **not assumed**

Let `U_1,...,U_k` be commuting endpoint shifts and let

\[
0<r_i<1,
\qquad
F=\prod_{i=1}^k(I-r_iU_i),
\qquad
s=\prod_{i=1}^k(1-r_i).
\]

## 1. Sequential first-owner identity

For any ordering, put

\[
s_0=1,
\qquad
s_i=\prod_{h\le i}(1-r_h),
\qquad
\lambda_i=r_is_{i-1}.
\]

Then

\[
\boxed{
F
=s_kI+
\sum_{i=1}^k
\lambda_i(I-U_i)
\prod_{h>i}(I-r_hU_h).
}
\tag{L-99701.1}
\]

Every monomial `U_A` has coefficient

\[
(-1)^{|A|}\prod_{i\in A}r_i.
\]

Thus (L-99701.1) is the native Euler source, including complete future parity.
It is not the contracted `alpha`-child identity.

For one prime the distinction is already binding. The contracted positive
packet has current

\[
P-r^2UP
\]

and current plus recursive child `P`; the native Euler update is

\[
P-rUP.
\]

The missing coefficient is `r(1-r)UP`, which is positive and macroscopic.

## 2. Symmetric random-order homotopy

Define, for `0<=t<=1`,

\[
K_{j,t}=(1-tr_j)I-(1-t)r_jU_j
\tag{L-99701.2}
\]

and

\[
G_t=\prod_{j=1}^kK_{j,t}.
\]

At the endpoints,

\[
G_0=F,
\qquad
G_1=sI.
\]

Moreover

\[
\frac{d}{dt}K_{i,t}=-r_i(I-U_i),
\]

so finite differentiation and integration give

\[
\boxed{
F=sI+
\int_0^1
\sum_{i=1}^k
r_i(I-U_i)
\prod_{j\ne i}K_{j,t}
\,dt.
}
\tag{L-99701.3}
\]

This is also obtained by assigning independent uniform priorities to the
primes and averaging the sequential first-owner identity over every order.
Conditional on the priority of `p_i` being `t`, each other prime contributes
survival before `i` and its native Euler factor after `i`; their expectation is
exactly `K_(j,t)`.

Factoring

\[
K_{j,t}=(1-tr_j)
\left[I-
\frac{(1-t)r_j}{1-tr_j}U_j
\right]
\tag{L-99701.4}
\]

shows that the homotopy averages future profiles with attenuated activities in
`[0,r_j]`, multiplied by a positive scalar.

## 3. Correct remaining sign gates

There are now two source-faithful sufficient gates:

```text
FCHD67:
    every sequential future-completed current
    (I-U_i) prod_(h>i)(I-r_h U_h) f
    has the required one-sided realization;

SEHC67:
    the aggregate homotopy current in (L-99701.3),
    applied to the actual scalar source, is nonnegative.
```

`FCHD67` implies `SEHC67`, but `SEHC67` does not require each ordering or each
future current to be positive separately. Both preserve every native
coefficient. Neither is proved here.

The homotopy is an exact averaging device, not a positivity theorem. Replacing
`K_(j,t)` by a positive unsieved packet, dropping accumulated parity, or
exporting only an `r_j^2` child reintroduces the refuted native-coefficient
mismatch.
