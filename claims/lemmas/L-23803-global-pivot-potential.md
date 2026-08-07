# L-23803 — Global pivot potential for the carry matrix

Claim ID: `L-23803`  
Title: An explicit carry potential has sharp initial mass eight and costs at most the row index on every row  
Status: **PROPOSED EXACT ELEMENTARY LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-23`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `D-23801`, `L-23802`  
Scope: source-free floor geometry; the final residual remains open

## 1. Potential

Define

\[
\boxed{
a(q)=2-64q^{-1/2}.}
\tag{L-23803.1}
\]

The finitely many negative weights are harmless. For every `n>=2`,

\[
\boxed{
\sum_{q=2}^na(q)\beta_{nq}\le n.}
\tag{L-23803.2}
\]

For the target ramp,

\[
\boxed{
\sum_{q=2}^Xa(q)w_X(q)
=8\sqrt X+O(\log^2X).}
\tag{L-23803.3}
\]

## 2. Continuum comparison

Let

\[
f(t)=K(1/t),
\qquad0<t\le1,
\]

where `K` is the kernel of `L-23802`. If

\[
A=\left\lfloor\frac nq\right\rfloor,
\qquad L=(A+1)q-n,
\]

then

\[
K(n/q)=\frac{AL}{n},
\qquad
\beta_{nq}=rac{A(L-1)}{n+1}.
\]

Hence

\[
\boxed{0\le\beta_{nq}\le f(q/n).}
\tag{L-23803.4}
\]

On

\[
I_A=\left(\frac1{A+1},\frac1A\right],
\]

one has

\[
f(t)=A[(A+1)t-1],
\]

an increasing affine ramp from zero to one. Also

\[
\int_0^1f(t)dt
=\int_1^\infty K(x)x^{-2}dx
=\frac12.
\tag{L-23803.5}
\]

## 3. Unweighted row sum

Put

\[
S_0(n)=\sum_{q=2}^n\beta_{nq},
\qquad M=\lfloor\sqrt n\rfloor.
\]

For `q<=M`, use `f(q/n)<=1`, contributing at most `M`.
For `q>M`, the quotient `floor(n/q)` takes at most `M` values. On each affine
ramp, the right grid sum of an increasing height-one function is at most `n`
times its integral plus one endpoint unit. Therefore

\[
S_0(n)
\le M+n\int_0^1f(t)dt+M
\le\frac n2+2\sqrt n.
\tag{L-23803.6}
\]

Thus

\[
2S_0(n)-n\le4\sqrt n.
\tag{L-23803.7}
\]

## 4. Square-root weighted row sum

Put

\[
S_{1/2}(n)=\sum_{q=2}^n\frac{\beta_{nq}}{\sqrt q}.
\]

For `n>=8`, restrict to

\[
\left\lceil\frac{3(n+1)}4\right\rceil\le q\le n.
\]

There are at least `n/8` such integers. On this range

\[
\beta_{nq}=rac{2q-n-1}{n+1}\ge\frac12,
\qquad q^{-1/2}\ge n^{-1/2}.
\]

Hence

\[
S_{1/2}(n)\ge\frac{\sqrt n}{16}.
\tag{L-23803.8}
\]

Direct calculation covers `2<=n<8`.
Combining (L-23803.7)--(L-23803.8) proves (L-23803.2).

## 5. Initial potential

Elementary integral comparison gives

\[
2\sum_{q=2}^Xq^{-1/2}\log(X/q)
=8\sqrt X+O(\log X),
\]

and

\[
64\sum_{q=2}^Xq^{-1}\log(X/q)
=O(\log^2X).
\]

This proves (L-23803.3).

## 6. Reduction to one final residual

Let `d` be any packing and `rho_d` its residual. Since

\[
w_X=B_X^Td+\rho_d,
\]

one has

\[
\sum_qa(q)w_X(q)
=
\sum_nd(n)\sum_qa(q)\beta_{nq}
+
\sum_qa(q)\rho_d(q).
\]

By (L-23803.2),

\[
\mathcal M_X(d)
\ge
8\sqrt X-O(\log^2X)
-
\sum_{q=2}^Xa(q)\rho_d(q).
\]

Because the negative `a(q)` terms only help, define

\[
\mathcal R_X^+(d)
=
\sum_{q=2}^X(a(q))_+\rho_d(q).
\]

Then

\[
\boxed{
\mathcal M_X(d)
\ge8\sqrt X-O(\log^2X)-\mathcal R_X^+(d).}
\tag{L-23803.9}
\]

For `d=d_X^gr`, the Greedy Residual theorem of `D-23801` therefore implies
mass eight with subpolynomial error.

## 7. Proof boundary

Closed here:

- the global row-potential inequality;
- the sharp initial mass-eight potential;
- reduction of greedy mass to one positive final residual.

Open:

- `mathcal R_X^gr=X^(o(1))`;
- RH.
