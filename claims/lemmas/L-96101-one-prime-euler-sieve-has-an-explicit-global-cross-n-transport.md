# L-96101 — One Euler prime has an explicit global cross-n transport for the discrete-tail row

Claim ID: `L-96101`  
Status: **PROVED UNCONDITIONAL ONE-PRIME THEOREM**  
Created: 2026-08-16  
Depends on: `L-96100`  
RH status: **unproved**

## 1. Statement

Let `j>=2` and let `p>=2` be an integer. For the discrete-tail conjugated row

\[
 G_j(Y)=\sum_{n\ge1}q_j(n)\Psi(Y/n),
 \qquad
 \Psi(u)=\sqrt u\log u\,\mathbf1_{u\ge1},
\]

put

\[
 \mathfrak S_{p,j}(Y)=G_j(Y)-G_j(Y/p).
\tag{L-96101.1}
\]

Then

\[
 \boxed{
 \mathfrak S_{p,j}(Y)\ge0
 \qquad(Y>0).
 }
\tag{L-96101.2}
\]

The proof genuinely moves mass between different products. It is not a
fixed-product divisor-cube proof.

## 2. Exact coefficient ledger

The coefficient of `Psi(Y/n)` in (L-96101.1) is

\[
 q_j^{(p)}(n)=q_j(n)-\mathbf1_{p\mid n}q_j(n/p).
\tag{L-96101.3}
\]

Besides nonnegative coefficients, the only negative entries are

\[
 q_j^{(p)}(j+1)=-B_j,
\tag{L-96101.4}
\]

and

\[
 q_j^{(p)}(pj)=C_j-A_j=-\frac{j+2}{j}.
\tag{L-96101.5}
\]

The relevant positive entries are

\[
 q_j^{(p)}(j)=A_j,
\tag{L-96101.6}
\]

and

\[
 q_j^{(p)}(p(j+1))=C_j+B_j=1.
\tag{L-96101.7}
\]

All remaining coefficients are either `C_j` or zero. This remains true when
`p` divides `j` or `j+1`, because the corresponding quotient is then below
`j` and has coefficient zero.

## 3. Pay the first shoulder by monotonicity

Write

\[
 K_x(t)=e^{(x-t)/2}(x-t)_+.
\]

For fixed `x`, `K_x` is decreasing. Spend `B_j` units of the positive atom at
`j` against the negative atom at `j+1`:

\[
 B_j\bigl[K_x(\log j)-K_x(\log(j+1))\bigr]\ge0.
\tag{L-96101.8}
\]

The unused mass at `j` is

\[
 A_j-B_j=(j+1)C_j.
\tag{L-96101.9}
\]

## 4. Pay the transported edge by one convex packet

Reserve

\[
 \frac2j
\]

units of the remaining atom at `j`, and use the complete unit atom at
`p(j+1)`. Their total mass is

\[
 \frac2j+1=\frac{j+2}{j},
\]

which is exactly the magnitude of the negative atom at `pj`.

Let

\[
 \bar t
 =\frac{(2/j)\log j+\log(p(j+1))}{1+2/j}.
\]

The inequality

\[
 \bar t\le\log(pj)
\tag{L-96101.10}
\]

is equivalent to

\[
 j\log\left(1+\frac1j\right)\le2\log p.
\tag{L-96101.11}
\]

Now

\[
 j\log\left(1+rac1j\right)<1
 \le2\log2\le2\log p,
\]

so (L-96101.10) holds.

By convexity of `K_x`, followed by its monotonicity,

\[
 \frac2jK_x(\log j)
 +K_x(\log(p(j+1)))
 \ge
 \frac{j+2}{j}K_x(\bar t)
 \ge
 \frac{j+2}{j}K_x(\log(pj)).
\tag{L-96101.12}
\]

This pays (L-96101.5) exactly.

## 5. No reservoir overdraw

After the two payments, the residual mass at `j` is

\[
 A_j-B_j-\frac2j
 =\frac4{j(j-1)}
 =2C_j>0.
\tag{L-96101.13}
\]

Every other residual coefficient is nonnegative. Therefore (L-96101.8) and
(L-96101.12), plus the unused positive atoms, form a complete one-use
cross-`n` decomposition of (L-96101.1). This proves (L-96101.2).

## 6. Why this does not iterate for free

The proof spends `2/j` units of the same edge atom at `j`. Repeating this
one-prime packet independently for `r` primes would demand `2r/j` units and
would double-spend the edge once `r` is large. The theorem is therefore a
valid first Euler step, not a proof of the full initial-prime product.

A multi-prime theorem must replace repeated edge spending by a globally owned
rough-reservoir transport. That is the exact open problem in `M-96100`.

```text
one prime / one integer dilation          VERIFIED
cross-n ownership                         explicit
shoulder and transported-edge payments    exact
unused edge reserve                        2 C_j
parallel repetition                       forbidden / overdraws
full initial-prime product                 OPEN
Riemann Hypothesis                         UNPROVED
```
