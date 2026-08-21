# L-23701 — Exact carry–Möbius Green factorization

Claim ID: `L-23701`  
Title: Möbius transformation turns the finite carry matrix into one affine Green kernel  
Status: `PROPOSED — COMPLETE EXACT FINITE ALGEBRA`  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Scope: finite, unconditional, exact  
Depends on: only Möbius inversion and finite summation

## 1. Carry matrix and triangular inverse

For integers `2 <= q <= n`, put

\[
\beta_{nq}
 =\frac{\lfloor n/q\rfloor\bigl(q-1-(n\bmod q)\bigr)}{n+1}.
\tag{L-23701.1}
\]

For a finite target vector `w(2),...,w(X)`, let `c(2),...,c(X)` be the unique
upper-triangular solution

\[
w(q)=\sum_{n=q}^{X}c(n)\beta_{nq}.
\tag{L-23701.2}
\]

The diagonal is

\[
\beta_{qq}=\frac{q-1}{q+1}>0,
\]

so the solution exists and is unique.

For the RH-facing carry target,

\[
w_X(q)=\frac1{\sqrt q}\log\frac Xq,
\qquad 2\le q\le X.
\tag{L-23701.3}
\]

No positivity assumption is made in this lemma.

## 2. Exact floor identity

For every `2 <= q <= n`,

\[
\boxed{
(n+1)\beta_{nq}
 =(n+1)\left\lfloor\frac nq\right\rfloor
 -2\sum_{j=0}^{n}\left\lfloor\frac jq\right\rfloor.}
\tag{L-23701.4}
\]

### Proof

Write `n=aq+r`, with `0<=r<q`. Then

\[
\sum_{j=0}^{n}\left\lfloor\frac jq\right\rfloor
 =q\frac{a(a-1)}2+a(r+1).
\]

Substitution into the right side of (L-23701.4) gives

\[
a(q-1-r)=(n+1)\beta_{nq}.
\]

## 3. Möbius collapse

Define the Möbius transform of the target by

\[
u(m)=\sum_{k\le X/m}\mu(k)w(mk).
\tag{L-23701.5}
\]

Then the transformed carry kernel is floor-free:

\[
\boxed{
\sum_{k\le n/m}\mu(k)\beta_{n,mk}
 =\frac{2m-n-1}{n+1}}
\qquad(2\le m\le n).
\tag{L-23701.6}
\]

Consequently,

\[
\boxed{
u(m)=\sum_{n=m}^{X}c(n)\frac{2m-n-1}{n+1}.}
\tag{L-23701.7}
\]

### Proof

Multiply the left side of (L-23701.6) by `n+1` and use (L-23701.4). The first
term is

\[
(n+1)\sum_{k\le n/m}\mu(k)
 \left\lfloor\frac{n}{mk}\right\rfloor=n+1,
\]

by

\[
\sum_{k\le y}\mu(k)\left\lfloor\frac yk\right\rfloor=1
\qquad(y\ge1).
\]

For each fixed `j`, the same identity shows

\[
\sum_{k\le n/m}\mu(k)
 \left\lfloor\frac{j}{mk}\right\rfloor
 =\mathbf 1_{j\ge m}.
\]

The second term is therefore `2(n-m+1)`. Their difference is `2m-n-1`.
Interchanging the two finite sums in (L-23701.2) proves (L-23701.7).

## 4. One-dimensional Green tail

Put

\[
a_n=\frac{c(n)}{n+1},
\qquad
s_m=\sum_{n=m}^{X}a_n,
\qquad s_{X+1}=0.
\tag{L-23701.8}
\]

Then

\[
u(m)-u(m+1)
 =(m-1)s_m-(m+1)s_{m+1}.
\tag{L-23701.9}
\]

Writing

\[
r_m=m(m-1)s_m,
\tag{L-23701.10}
\]

one obtains the exact first-order Green recurrence

\[
r_m-r_{m+1}=m\bigl(u(m)-u(m+1)\bigr).
\tag{L-23701.11}
\]

Since `r_{X+1}=0`, summation gives

\[
\boxed{
r_m=m u(m)+\sum_{\ell=m+1}^{X}u(\ell),}
\tag{L-23701.12}
\]

and hence

\[
\boxed{
s_m=
\frac{m u(m)+\sum_{\ell=m+1}^{X}u(\ell)}{m(m-1)},}
\tag{L-23701.13}
\]

\[
\boxed{
c(m)=(m+1)\bigl(s_m-s_{m+1}\bigr).}
\tag{L-23701.14}
\]

Equivalently,

\[
\boxed{
c(m)=
\frac{
(m+1)\bigl[m u(m)-(m-2)u(m+1)\bigr]
+2\sum_{\ell=m+2}^{X}u(\ell)
}{m(m-1)}.}
\tag{L-23701.15}
\]

## 5. Exact reformulations of Carry Saturation

For the target (L-23701.3), the finite Carry Saturation assertion

\[
c_X(m)\ge0\qquad(2\le m\le X)
\tag{L-23701.16}
\]

is equivalent to

\[
\boxed{s_{X,2}\ge s_{X,3}\ge\cdots\ge s_{X,X+1}=0.}
\tag{L-23701.17}
\]

Thus the original `X x X` floor matrix has collapsed to monotonicity of one
scalar Green profile.

The weaker condition

\[
s_{X,m}\ge0
\tag{L-23701.18}
\]

is strictly less than Carry Saturation and is useful because the cumulative
entropy basis in `L-23702` is positive.

## 6. Proof boundary

This lemma does **not** assert (L-23701.16), (L-23701.17), or (L-23701.18).
For the target (L-23701.3), `u(m)` contains the reciprocal-zeta Möbius channel

\[
u_X(m)=\frac1{\sqrt m}
\sum_{k\le X/m}\frac{\mu(k)}{\sqrt k}
 \log\frac{X/m}{k}.
\tag{L-23701.19}
\]

The point of the factorization is not to declare that channel positive. It is
to expose the exact second-order Green structure and to identify weaker positive
certificates that do not require the full inverse to be pointwise positive.

## 7. Exact replay

`experiments/X-23701-carry-green/verify.py` checks (L-23701.4),
(L-23701.6), and (L-23701.12)--(L-23701.15) with exact integer and rational
arithmetic on 2,556 matrix pairs and eight independent rational target vectors.
It authenticates finite algebra only.
