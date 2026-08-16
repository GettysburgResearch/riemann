# L-94100 — Positive parabolic endpoint atoms have strictly positive radix-four detail

Claim ID: `L-94100`  
Status: **PROVED EXACT ALL-SCALE CALCULUS / DISCRETE INEQUALITY**  
Created: 2026-08-16  
Builds on: the endpoint atoms of `L-26201`; the exact carry coefficient of `L-24502`  
RH status: **unproved**

## 1. Endpoint atoms and physical responses

For real `Y>=2` and integer `m>=2`, put

\[
 b_Y(m)=2\sqrt m\left[
  \log\frac Ym-2\left(1-\sqrt{\frac mY}\right)
 \right]\mathbf1_{m\le Y},
 \tag{L-94100.1}
\]

\[
 A_Y(m)=\frac{b_Y(m)}{m-1},
 \qquad
 d_Y(n)=(n+1)\Delta^2A_Y(n).
 \tag{L-94100.2}
\]

For an integer `T>=3`, define the endpoint atom

\[
 a_T=d_T-d_{T-1}.
 \tag{L-94100.3}
\]

The positivity needed below can be checked directly. Extend `A_Y` to real
`1<x<Y` and put

\[
 C_Y(x)=\partial_{\log Y}A_Y(x)
 =\frac{2(\sqrt x-x/\sqrt Y)}{x-1}.
\]

A direct differentiation gives

\[
 C_Y''(x)=
 \frac{3\sqrt Yx^2+6\sqrt Yx-\sqrt Y-8x^{3/2}}
 {2\sqrt Yx^{3/2}(x-1)^3}>0
 \qquad(Y\ge x>1),
\tag{L-94100.4}
\]

because its numerator is at least
`√x(3x+1)(x-1)`. Hence every interior discrete second difference of
`C_Y` is positive. Integrating over `log(T-1)<log Y<log T` proves
`a_T(n)>0` for `n<=T-3`. The entering boundary is also positive: with
`m=T-1`, `a=sqrt(m/(m+1))`, and `b=sqrt((m-1)/(m+1))`, positivity at the
only nontrivial boundary row reduces exactly to

\[
 (m-1)b(1+a)>(m-2)a(1+b),
\]

whose difference is
`b(1+a)-(m-2)/[(m+1)(a+b)]>0`. Finally
`a_T(T-1)=T A_T(T-1)>0`, and rows at or above `T` vanish. Therefore

\[
 \boxed{a_T(n)\ge0\qquad(n\ge2).}
\tag{L-94100.5}
\]

For `n=qk+r`, `0<=r<q`, direct block counting in the average-binomial row gives

\[
 \beta_{nq}=\frac{k(q-1-r)}{n+1}.
 \tag{L-94100.6}
\]

Define the ordinary and radix-four responses of one atom by

\[
 \Gamma_T(q)=\sum_na_T(n)\beta_{nq},
 \tag{L-94100.7}
\]

\[
 \Delta_T(q)=\Gamma_T(q)-2\Gamma_T(4q).
 \tag{L-94100.8}
\]

The theorem is

\[
 \boxed{
 \Delta_T(q)>0\quad(2\le q<T),
 \qquad
 \Delta_T(q)=0\quad(q\ge T).
 }
 \tag{L-94100.9}
\]

Thus each positive endpoint atom lies in the native radix-four detail cone,
not merely in the ordinary carry cone.

## 2. A sharp square-root harmonic inequality

Write

\[
 S_N=\sum_{k=1}^N\frac1{\sqrt k},
 \qquad S_0=0,
 \qquad M=\left\lfloor\frac N4\right\rfloor.
\]

We first prove

\[
 \boxed{
 S_N-S_M
 \le
 \frac{2(N-2M)}{\sqrt{N+1}}
 \qquad(N\ge1).
 }
 \tag{L-94100.10}
\]

The cases `N=1,2,3` are immediate. For `N>=4`, define

\[
 H(x)=2\sqrt x+\frac1{2\sqrt x}-\frac1{24x^{3/2}}.
\]

For integer `n>=2`, put `s=sqrt(n)+sqrt(n-1)`. Direct rationalization gives

\[
 H(n)-H(n-1)-\frac1{\sqrt n}
 =
 \frac{2(7s^4-3)}
 {3s(s-1)^3(s+1)^3(s^2+1)^3}>0.
 \tag{L-94100.11}
\]

Hence

\[
 S_N-S_M\le H(N)-H(M).
 \tag{L-94100.12}
\]

For `N=4M`, put

\[
 u=\sqrt{4M+1}+2\sqrt M.
\]

Another direct rationalization gives

\[
 \frac{4M}{\sqrt{4M+1}}-[H(4M)-H(M)]
 =
 \frac{2u^6-28u^4+15u^2-3}
 {3u(u-1)^3(u+1)^3(u^2+1)}>0.
 \tag{L-94100.13}
\]

Indeed `u^2>14`, so both
`u^4(2u^2-28)` and `15u^2-3` are positive.

The remaining residue classes follow one term at a time. From the `4M` case,

\[
 S_{4M+1}-S_M
 \le\frac{4M}{\sqrt{4M+1}}+\frac1{\sqrt{4M+1}}
 =\sqrt{4M+1}<\sqrt{4M+2}.
\]

The passages `4M+1 -> 4M+2` and `4M+2 -> 4M+3` reduce after squaring to

\[
 a^2+a-1>0
 \quad(a=4M+2),
\]

and

\[
 a^2+a-4>0
 \quad(a=4M+3),
\]

respectively. This proves (L-94100.10).

## 3. A signed scale-four increment inequality

For `eta>=0`, define

\[
 f_k(\eta)=\frac1{\sqrt{k+\eta}+\sqrt k},
\]

and, with `M=floor(N/4)`,

\[
 F_N(\eta)=
 \sum_{k=1}^Nf_k(\eta)
 -2\sum_{h=1}^Mf_{4h}(\eta).
 \tag{L-94100.14}
\]

Put

\[
 g_k(\eta)=-f_k'(\eta)
 =\frac1{2\sqrt{k+\eta}(\sqrt{k+\eta}+\sqrt k)^2}.
\]

For fixed `eta`, `g_k(eta)` decreases with `k`. On each complete block of four,

\[
 g_{4h-3}+g_{4h-2}+g_{4h-1}+g_{4h}
 \ge4g_{4h}.
\]

Therefore

\[
 F_N'(\eta)
 =-\sum_{k=1}^Ng_k(\eta)+2\sum_{h=1}^Mg_{4h}(\eta)
 \le0.
 \tag{L-94100.15}
\]

At `eta=0`,

\[
 F_N(0)=\frac12(S_N-S_M).
\]

Combining with (L-94100.10),

\[
 \boxed{
 F_N(\eta)
 \le\frac{N-2M}{\sqrt{N+1}}
 \qquad(\eta\ge0).
 }
 \tag{L-94100.16}
\]

For integers `q>=2`, put

\[
 D_q(N)=\sum_{k=1}^N
 [\sqrt{kq+1}-\sqrt{kq}].
\]

Since

\[
 D_q(N)=\frac1{\sqrt q}\sum_{k=1}^Nf_k(1/q),
\]

(L-94100.16) gives

\[
 \boxed{
 D_q(N)-2D_{4q}(M)
 \le
 \frac{N-2M}{\sqrt{(N+1)q}}.
 }
 \tag{L-94100.17}
\]

This signed inequality is the scale-four input needed below. Notice that it
controls the negative coefficients at multiples of `4q`; no termwise absolute
majorant is used.

## 4. Positivity on one integer endpoint interval

Fix `T>=3` and `q<T`. On the open interval `T-1<Y<T`, put

\[
 N=\left\lfloor\frac{T-1}{q}\right\rfloor,
 \qquad
 M=\left\lfloor\frac{T-1}{4q}\right\rfloor
 =\left\lfloor\frac N4\right\rfloor,
 \qquad
 B=N-2M.
\]

Away from the one possible entering boundary term, write \(V_Y(q)=C_{d_Y}(q)\). Differentiating the
ordinary carry response with respect to `log Y` gives

\[
 \partial_{\log Y}V_Y(q)
 =\frac{2N}{\sqrt Y}-2D_q(N).
 \tag{L-94100.18}
\]

Consequently the base radix-four derivative is

\[
 \frac{2B}{\sqrt Y}
 -2[D_q(N)-2D_{4q}(M)].
 \tag{L-94100.19}
\]

If `q` does not divide `T-1`, then `(N+1)q>=T>Y`; (L-94100.17) makes
(L-94100.19) strictly positive.

If `4q` divides `T-1`, the missing entering endpoint contributes

\[
 -[2\sqrt T-2T/\sqrt Y]>0
\]

to the detail derivative, so positivity again follows.

It remains to consider

\[
 q\mid T-1,
 \qquad 4q\nmid T-1.
\]

Then `N=4M+r` with `r in {1,2,3}`. The missing entering endpoint contributes

\[
 2\sqrt T-2T/\sqrt Y<0.
\]

Let

\[
 D=D_q(N)-2D_{4q}(M).
\]

The last coefficient in `D` is positive. Applying (L-94100.17) to the first
`N-1` terms gives

\[
 D
 \le
 [\sqrt T-\sqrt{T-1}]
 +\frac{B-1}{\sqrt{T-1}}
 =
 \sqrt T-\frac{T-B}{\sqrt{T-1}}.
 \tag{L-94100.20}
\]

Thus the complete detail derivative is

\[
 2(\sqrt T-D)-\frac{2(T-B)}{\sqrt Y}>0
 \qquad(T-1<Y<T),
 \tag{L-94100.21}
\]

because `1/sqrt(Y)<1/sqrt(T-1)`.

## 5. Integrate to obtain the endpoint atom

The physical response is continuous at every activation: a newly entering seed
has value zero at its endpoint. Therefore integrating the strictly positive
detail derivative across `T-1<Y<T` gives

\[
 \Delta_T(q)>0
 \qquad(2\le q<T).
\]

If `q>=T`, every average-binomial response of `a_T` vanishes by triangular
support, proving the second part of (L-94100.9).

## 6. Diagonal response

Since `4q>=q+1` at `T=q+1`, the detail diagonal equals the ordinary diagonal:

\[
 \boxed{
 \Delta_{q+1}(q)=\Gamma_{q+1}(q)
 =2\sqrt q\left[
 \log\left(1+\frac1q\right)
 -2\left(1-\left(1+\frac1q\right)^{-1/2}\right)
 \right].
 }
 \tag{L-94100.22}
\]

The elementary bound already proved for this expression gives

\[
 \boxed{
 \frac1{5q^{3/2}}
 \le\Delta_{q+1}(q)
 \le\frac1{2q^{3/2}}.
 }
 \tag{L-94100.23}
\]

## 7. Boundary

```text
endpoint row atom a_T                         nonnegative
ordinary response Gamma_T                     positive below diagonal
radix-four detail Delta_T                     strictly positive below diagonal
q/4q formed from one row                      exact
activation-cell approximation                 absent
Möbius child realization                      absent
Target-Lorenz tail                            absent
Riemann Hypothesis                            unproved
```
