# L-91329 — Fractional terminal endpoint atoms have a uniform positive response, closing the real-column top omission

Claim ID: `L-91329`  
Status: **PROPOSED COMPLETE EXACT FRACTIONAL-TERMINAL REPAIR — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91101`, `L-91115`, `L-91324-fractional-column-green-identity-and-continuous-reset.md`  
RH status: **unproved**

## 1. Purpose

The review on PR #405 correctly observed that the pointwise endpoint derivative
bound used in `L-91115` does not remain bounded below at every real column:
when `q` and the moving endpoint lie in the same final unit cell, that derivative
can approach zero.

The terminal omission does not need such a pointwise derivative bound. It can
be chosen as an exact sum of integer endpoint atoms. Each complete endpoint
atom has a uniform positive response at every real terminal column.

## 2. Endpoint atom and real-column response

Let

\[
 e_T=b_T-b_{T-1},\qquad T\ge3,
\]

and let

\[
 \overline\Gamma_T(q)=\overline v_q(e_T)
\]

be its response to the continuous Pascal column of `L-91324`, for real `q>0`.
The exact switching identity is

\[
 \overline v_q(F)
 =\sum_{j\ge1}
 \left[
  F(k_j)-F(k_j+1)
  +2\vartheta_j
   \left(
    \frac{F(k_j)}{k_j-1}-\frac{F(k_j+1)}{k_j}
   \right)
 \right],
\]

where

\[
 k_j=\lfloor jq\rfloor,
 \qquad
 \vartheta_j=\{jq\}.
\]

## 3. Monotonicity of the divided endpoint profile

For old nodes `1<x<=T-1`, write

\[
 e_T(x)=\alpha_T(\sqrt x-r_Tx),
\]

with

\[
 \alpha_T=2\log\frac{T}{T-1},
 \qquad
 T^{-1/2}<r_T<(T-1)^{-1/2}<1.
\]

The derivative of the divided profile is

\[
 \frac d{dx}
 \left[
  \frac{\sqrt x-r_Tx}{x-1}
 \right]
 =
 \frac{2r_T\sqrt x-x-1}
 {2\sqrt x(x-1)^2}<0,
\]

because `(x+1)/(2sqrt(x))>=1>r_T`. Therefore

\[
 \boxed{
 \frac{e_T(n)}{n-1}
 \text{ decreases strictly in }n.
 }
\]

Every fractional correction in the switching identity is consequently
nonnegative.

## 4. Uniform lower bound

### Theorem 4.1

For every integer `T>=14` and every real column

\[
 \frac T4<q<T,
\]

one has

\[
 \boxed{
 \overline\Gamma_T(q)
 >\frac{2}{5}T^{-3/2}.
 }
\]

### Case 1: `q>T-1`

Only the terminal breakpoint is active, and its switching contribution is at
least

\[
 e_T(T-1)=b_T(T-1).
\]

Put `m=T-1`, `x=1/m`. Then

\[
 e_T(T-1)
 =2\sqrt m
 \left[
  \log(1+x)-2\left(1-(1+x)^{-1/2}\right)
 \right].
\]

For `0<=x<=1`,

\[
 \log(1+x)\ge x-\frac{x^2}{2},
\]

and the alternating binomial bound gives

\[
 (1+x)^{-1/2}
 \ge1-\frac x2+\frac{3x^2}{8}-\frac{5x^3}{16}.
\]

Since `m>=13`, the bracket is at least

\[
 x^2\left(\frac14-\frac{5}{8m}\right)
 \ge\frac{x^2}{5}.
\]

Thus

\[
 e_T(T-1)\ge\frac{2}{5}m^{-3/2}
 >\frac{2}{5}T^{-3/2}.
\]

### Case 2: `q<=T-1`

Put

\[
 J=\left\lfloor\frac{T-1}{q}\right\rfloor.
\]

Because `q>T/4`, one has `J in {1,2,3}`. If one complete breakpoint has
`k_j=T-1`, its contribution already gives Case 1. Otherwise every complete
breakpoint has `k_j<=T-2`, and

\[
 e_T(k_j)-e_T(k_j+1)
 =\alpha_T
 \left[
  r_T-\frac1{\sqrt{k_j}+\sqrt{k_j+1}}
 \right].
\]

Using

\[
 \alpha_T>\frac2T,
 \qquad
 r_T>\frac1{\sqrt T},
\]

and `sqrt(k)+sqrt(k+1)>2sqrt(k)`,

\[
 e_T(k_j)-e_T(k_j+1)
 >\frac{2}{T^{3/2}}
 \left[
  1-\frac{\sqrt T}{2\sqrt{k_j}}
 \right].
\]

Moreover

\[
 q>\frac{T-1}{J+1},
 \qquad
 k_j>\frac{j(T-1)}{J+1}-1.
\]

For `T>=14`, the three possible sums admit the following elementary rational
bounds.

For `J=1`,

\[
 2\left[
  1-\sqrt{\frac{T}{2(T-3)}}
 \right]>\frac25.
\]

For `J=2`, use

\[
 \sqrt{\frac{3T}{T-4}}<\frac{41}{20},
 \qquad
 \sqrt{\frac{3T}{2T-5}}<\frac{34}{25}
\]

at the worst endpoint `T=14`; both ratios decrease with `T`. Hence the normalized
sum exceeds

\[
 2\left[2-\frac12\left(\frac{41}{20}+\frac{34}{25}\right)\right]
 =\frac{59}{100}>\frac25.
\]

For `J=3`, use

\[
 \sqrt{\frac{4T}{T-5}}<\frac52,
 \qquad
 \sqrt{\frac{2T}{T-3}}<\frac85,
 \qquad
 \sqrt{\frac{4T}{3T-7}}<\frac{13}{10}.
\]

The normalized sum exceeds

\[
 2\left[3-\frac12\left(\frac52+\frac85+\frac{13}{10}\right)\right]
 =\frac35>\frac25.
\]

All omitted fractional switching terms are nonnegative by Section 3. This proves
the theorem.

## 5. Exact discrete top omission

For integers `X`, `W` define

\[
 P_{X,W}=\sum_{T=X-W+1}^{X}e_T=b_X-b_{X-W}.
\]

On the top interval the complete positive equality density satisfies
`lambda_X(s)>=1`. Use the following hybrid positive lift there:

1. split the density as
   \[
   \lambda_X(s)=1+[\lambda_X(s)-1];
   \]
2. realize the unit component on every complete integer cell exactly by
   \[
   e_T=\int_{T-1}^{T}\dot b_s\,ds;
   \]
3. apply the positive martingale/B-spline quantizer only to the nonnegative
   remainder `lambda_X-1`.

Thus the full producer contains the exact packet `P_(X,W)` coefficientwise,
and deleting it leaves nonnegative endpoint weights. No assertion that the
canonical quantization of the unsplit density has endpoint weights at least one
is needed. The exact unit lift also creates no quantization collar.

If

\[
 X/4<q<X-W,
\]

then every `T` in the sum satisfies `T/4<q<T`. Therefore

\[
 \boxed{
 \overline v_q(P_{X,W})
 >\frac{2W}{5}X^{-3/2}.
 }
\]

If `q>=X-W`, every retained endpoint lies at most `X-W`, so the retained
producer has zero response in that terminal column.

Take

\[
 \boxed{W=100000.}
\]

Then

\[
 \frac{2W}{5}=40000>28836,
\]

which strictly dominates the complete fractional terminal error coefficient in
`L-91324-fractional-column-green-identity-and-continuous-reset.md`.

Thus the real-column terminal closure is valid after replacing the invalid
pointwise derivative import by this exact endpoint-atom omission.

## 6. Review disposition

The PR #405 reviewer was correct that the submitted pointwise argument was not
valid. The stronger conclusion that the real-column terminal closure remained
open is repaired by the theorem above.

```text
pointwise real-column derivative lower bound       FALSE
complete endpoint-atom real-column lower bound     PROPOSED COMPLETE
exact W=100000 discrete omission                    PROPOSED COMPLETE
fractional terminal overfill                        PAID WITH STRICT MARGIN
rough all-generation parity projection              STILL OPEN
Riemann Hypothesis                                  UNPROVEN
```
