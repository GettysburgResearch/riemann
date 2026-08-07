# L-26104 — Polylogarithmic `L^2` budget for the parabolic seed residual

Claim ID: `L-26104`  
Title: The positive prime-power residual of the parabolic carry seed has `L^2` norm `O(log^(3/2) X)`  
Status: **PROPOSED COMPLETE ELEMENTARY PROOF**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261  
Depends on: PR #248 `L-24502`; `L-26101`  
Scope: proves `SAF1` in `L-26103`

## 1. Continuous seed and derivatives

Extend the parabolic seed to `1<=t<=X` by

\[
 b_X(t)
 =2\sqrt t\log\frac Xt-4\sqrt t+\frac{4t}{\sqrt X}.
 \tag{L-26104.1}
\]

Then

\[
 b_X(X)=0,
\]

\[
\boxed{
 b_X'(t)
 =\frac4{\sqrt X}
 +\frac{\log(X/t)-4}{\sqrt t},
}
\tag{L-26104.2}
\]

and

\[
\boxed{
 b_X''(t)
 =\frac{1-\frac12\log(X/t)}{t^{3/2}}.
}
\tag{L-26104.3}
\]

## 2. Periodic selector decomposition

The row `q=X` has

\[
 v_X(b_X^{(0)})=b_X(X)-b_{X+1}=0,
\]

so its positive residual is zero. It remains to treat `2<=q<=X-1`.

Let

\[
 \chi_q(t)
 =\sum_{k\ge1}\mathbf1_{[kq,kq+1)}(t).
 \tag{L-26104.4}
\]

On every full period of length `q`, this selector has mean `1/q`. Put

\[
 P_q(t)=\int_q^t\left(\chi_q(u)-\frac1q\right)du.
 \tag{L-26104.5}
\]

Because the positive part of one period has length one and the compensating slope is constant,

\[
\boxed{|P_q(t)|\le1.}
\tag{L-26104.6}
\]

Let

\[
 T_q=1+q\left\lfloor\frac{X-1}{q}\right\rfloor.
\]

For `q<=X-1`, one has `q<T_q<=X`. The intervals retained by `chi_q` correspond exactly to all nonzero terms in the finite constraint. If `q|X`, the omitted final term is

\[
 b_X(X)-b_{X+1}=0.
\]

Therefore

\[
 v_q(b_X^{(0)})
 =-\int_q^{T_q}b_X'(t)\chi_q(t)dt.
 \tag{L-26104.7}
\]

Split `chi_q=1/q+(chi_q-1/q)`. Since `b_X(t)>=0` on `[1,X]`, the mean contribution satisfies

\[
 -\frac1q\int_q^{T_q}b_X'(t)dt
 =\frac{b_X(q)-b_X(T_q)}q
 \le\frac{b_X(q)}q.
 \tag{L-26104.8}
\]

For the mean-zero contribution, integration by parts and (L-26104.6) give

\[
\begin{aligned}
 \left|
  \int_q^{T_q}b_X'(t)
  \left(\chi_q(t)-\frac1q\right)dt
 \right|
 &\le |b_X'(T_q)|
  +\int_q^{T_q}|b_X''(t)|dt.
\end{aligned}
 \tag{L-26104.9}
\]

The lower endpoint has no boundary term because `P_q(q)=0`.

## 3. Uniform pointwise residual bound

Put

\[
 L_q=\log(X/q)\ge0.
\]

Equations (L-26104.2)--(L-26104.3) imply

\[
 |b_X'(T_q)|
 \ll\frac{1+L_q}{\sqrt q},
 \tag{L-26104.10}
\]

and

\[
\begin{aligned}
 \int_q^X|b_X''(t)|dt
 &\le
 \int_q^X
 \frac{1+\frac12\log(X/t)}{t^{3/2}}dt\\
 &\ll\frac{1+L_q}{\sqrt q}.
\end{aligned}
 \tag{L-26104.11}
\]

Also

\[
 \frac{b_X(q)}q
 =\frac{2L_q-4}{\sqrt q}+\frac4{\sqrt X}
 \le\frac{2L_q+4}{\sqrt q}.
 \tag{L-26104.12}
\]

Combining (L-26104.7)--(L-26104.12), there is an absolute constant `C` such that

\[
\boxed{
 v_q(b_X^{(0)})
 \le C\frac{1+\log(X/q)}{\sqrt q}.
}
\tag{L-26104.13}
\]

Since the target `w_X(q)` is nonnegative, the positive residual obeys

\[
\boxed{
 (r_X(q))_+
 \le C\frac{1+\log(X/q)}{\sqrt q}.
}
\tag{L-26104.14}
\]

This bound holds for every integer `q>=2`, hence in particular for every prime power.

## 4. Polylogarithmic source norm

Summing over prime powers and enlarging to all integers,

\[
\begin{aligned}
 \|(r_X)_+\|_2^2
 &\le
 C^2\sum_{q=p^a\le X}
  \frac{(1+\log(X/q))^2}{q}\\
 &\le
 C^2\sum_{n=2}^{X}
  \frac{(1+\log(X/n))^2}{n}\\
 &\ll \log^3(2X).
\end{aligned}
 \tag{L-26104.15}
\]

Therefore

\[
\boxed{
 \|(r_X)_+\|_2
 \ll\log^{3/2}(2X)=X^{o(1)}.
}
\tag{L-26104.16}
\]

This proves `SAF1` unconditionally.

## 5. Consequence for the recursive proposal

The open `SAF` theorem in `L-26103` may now be reduced to:

```text
SAF2  generated active-frame moat;
SAF3  positive-leakage contraction.
```

Together with (L-26104.16), those two estimates produce a subpower cumulative flow through the recursive potential.

## 6. Proof boundary

This file uses only elementary calculus, a bounded primitive of a periodic selector, and an integral comparison. It does not prove the finite-annulus frame or leakage estimates and does not prove RH.