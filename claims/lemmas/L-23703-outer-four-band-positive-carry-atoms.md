# L-23703 — Outer four-band positive carry atoms

Claim ID: `L-23703`  
Title: Every endpoint supplies four unconditional nonnegative carry bands  
Status: `PROPOSED — COMPLETE ELEMENTARY PROOF`  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Scope: finite, unconditional  
Depends on: `L-23701`

## 1. Endpoint target

For an integer endpoint `T>=2`, put

\[
w_T(q)=\frac1{\sqrt q}\log\frac Tq,
\qquad 2\le q\le T,
\tag{L-23703.1}
\]

and let `c_T(n)` be its exact triangular carry inverse. Define

\[
u_T(m)=\sum_{k\le T/m}\mu(k)w_T(mk).
\tag{L-23703.2}
\]

By `L-23701`,

\[
c_T(m)=
\frac{
(m+1)[m u_T(m)-(m-2)u_T(m+1)]
+2\sum_{\ell=m+2}^{T}u_T(\ell)
}{m(m-1)}.
\tag{L-23703.3}
\]

## 2. Only four Möbius values enter outside the fifth layer

If `5m>T`, then `floor(T/m)<=4`, and

\[
u_T(m)=m^{-1/2}F_r\!\left(\log\frac Tm\right),
\qquad r=\left\lfloor\frac Tm\right\rfloor,
\tag{L-23703.4}
\]

where

\[
F_r(L)=\sum_{k\le r}\frac{\mu(k)}{\sqrt k}(L-\log k).
\tag{L-23703.5}
\]

Only

\[
\mu(1)=1,
\quad \mu(2)=-1,
\quad \mu(3)=-1,
\quad \mu(4)=0
\tag{L-23703.6}
\]

occur.

Since `m^{-1/2}=T^{-1/2}e^{L/2}`, monotonicity of `u_T(m)` as `m` increases is
equivalent to monotonicity of

\[
g_r(L)=e^{L/2}F_r(L)
\tag{L-23703.7}
\]

as `L` increases.

For `r=1,2`, both `F_r` and `F_r'` are positive, so `g_r'>0`.
For `r=3,4`, put

\[
C=1-\frac1{\sqrt2}-\frac1{\sqrt3}<0,
\qquad
D=\frac{\log2}{\sqrt2}+\frac{\log3}{\sqrt3}.
\tag{L-23703.8}
\]

Then

\[
F_r(L)=CL+D
\qquad(\log3\le L<\log5),
\tag{L-23703.9}
\]

and

\[
e^{-L/2}g_r'(L)=C\left(1+\frac L2\right)+\frac D2.
\tag{L-23703.10}
\]

The right side decreases with `L`, and at `L=log5` it is

\[
\boxed{
C\left(1+\frac12\log5\right)
+\frac12\left(
 \frac{\log2}{\sqrt2}+\frac{\log3}{\sqrt3}
\right)>0.0488.}
\tag{L-23703.11}
\]

Thus `g_r'(L)>0` throughout the complete outer region. At each quotient boundary
`L=log r`, the newly entering summand in (L-23703.5) vanishes, so the profile is
continuous across the bands.

It follows that

\[
\boxed{u_T(m)\ge u_T(m+1)\ge0\qquad(5m>T).}
\tag{L-23703.12}
\]

## 3. Outer positivity

Every term in (L-23703.3) is nonnegative under (L-23703.12), because

\[
m u_T(m)-(m-2)u_T(m+1)
 =m(u_T(m)-u_T(m+1))+2u_T(m+1)\ge0.
\]

Therefore

\[
\boxed{c_T(m)\ge0\qquad(5m>T).}
\tag{L-23703.13}
\]

This is exactly the complete outer four-fifths theorem. The proof stops at
`5m=T` because `mu(5)=-1` enters there.

## 4. Four positive quotient-band atoms

For `r=1,2,3,4`, define

\[
I_{T,r}
 =\left\{n:\left\lfloor\frac{T}{r+1}\right\rfloor<n
 \le\left\lfloor\frac Tr\right\rfloor\right\}
\tag{L-23703.14}
\]

and

\[
a_{T,r}(n)=c_T(n)\mathbf1_{n\in I_{T,r}}.
\tag{L-23703.15}
\]

Then every `a_{T,r}` is nonnegative. Its carry coverage and entropy score are

\[
\Gamma_{T,r}(q)=\sum_{n=q}^{T}a_{T,r}(n)\beta_{nq},
\tag{L-23703.16}
\]

\[
\mathcal H_{T,r}=\sum_{n=2}^{T}a_{T,r}(n)G_n.
\tag{L-23703.17}
\]

Both are finite, explicit, prime-free except for the equivalent factorial
expression for `G_n`.

The complete outer block reconstructs the target exactly on its own top shell:

\[
\boxed{
\sum_{r=1}^{4}\Gamma_{T,r}(q)=w_T(q)
\qquad(T/5<q\le T).}
\tag{L-23703.18}
\]

For smaller `q`, the same block produces a positive spill. The role of the phase
renewal theorem in `T-23701` is to combine the four bands at many endpoints so
that all spills remain below the global target while the entropy mass reaches
the sharp constant.

## 5. Why band splitting is load-bearing

Keeping the four bands tied to a single common endpoint weight loses a fixed
amount in the continuum renewal. Allowing independent nonnegative weights for
`r=1,2,3,4` gives four distinct activation phases

\[
0,\ \log2,\ \log3,\ \log4
\quad\bmod\log5.
\]

This is the smallest source-specific enlargement suggested by the exact outer
proof: it adds no unproved carry coefficients and no Möbius value beyond
`mu(4)`.

## 6. Proof boundary and replay

The theorem proves positivity of every atom. It does not prove that a
near-saturating global combination exists.

`X-23701` checks the exact algebra used by the proof and certifies the scalar
transcendental gate (L-23703.11) by rational enclosures for logarithms and square
roots. The asymptotic phase renewal is not tested by that exact checker.
