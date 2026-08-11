# R-90702 — The critical uniform-Pascal occupation is not monotone

Claim ID: `R-90702`  
Status: **EXACT FINITE REFUTATION — DIRECTED LOG/RADICAL CERTIFICATE**  
Created: 2026-08-11  
Depends on: the exact Green occupation `L-33109`; the variation reduction `L-90701`  
Scope: refutes direct use of the monotone-occupation corollary for the critical target; it does not refute the bounded-upward-variation route

## 1. Critical occupation

At endpoint `X`, put

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

\[
U_X(n)=\sum_{k\le X/n}\mu(k)w_X(nk),
\qquad
r_X(n)=U_X(n)-U_X(n+1),
\qquad
s_n=nr_X(n).
\]

The uniform-Pascal Green occupation of `L-33109` is

\[
M_n=s_n+\frac2{n+1}\sum_{m=n+1}^{X}s_m.
\tag{R-90702.1}
\]

The new factor-64 theorem `L-90701` pays the signed reward automatically if `M_n` is nonnegative and nonincreasing. The nonincreasing hypothesis is false even at a small endpoint.

## 2. Exact witness at `X=14`

For `X=14`, exact Möbius and Green algebra gives

\[
\boxed{
\begin{aligned}
M_7-M_6={}&-6w_{14}(6)+11w_{14}(7)-\frac{37}{7}w_{14}(8)\\
&-\frac1{28}\bigl(w_{14}(9)+w_{14}(10)+w_{14}(11)+w_{14}(13)\bigr)\\
&+\frac{167}{28}w_{14}(12)-\frac{309}{28}w_{14}(14).
\end{aligned}}
\tag{R-90702.2}
\]

The last term vanishes. The retained directed certificate uses

\[
\log x=2\sum_{j\ge0}\frac{1}{2j+1}
\left(\frac{x-1}{x+1}\right)^{2j+1}
\tag{R-90702.3}
\]

with an explicit geometric tail, and integer-square-root reciprocal bounds at denominator `10^70`. It proves

\[
\boxed{
0.0136042514164165115744643782240243913692
<M_7-M_6
<0.0136042514164165115744643782240243913693.
}
\tag{R-90702.4}
\]

Every other adjacent difference `M_(n+1)-M_n`, `2<=n<14`, is strictly negative. Hence the entire upward variation is exactly this one jump.

The same certificate gives

\[
1.9440684670534688605278440559916513789210
<M_2
<1.9440684670534688605278440559916721909477.
\tag{R-90702.5}
\]

Consequently

\[
\boxed{
\frac{V_+(M)}{M_2}<0.007<\frac34.
}
\tag{R-90702.6}
\]

Thus ordinary monotonicity fails, but the stable variation criterion of `L-90701` pays the factor-64 debt at the witness with enormous slack.

## 3. Corrected frontier

The route may not claim

```text
critical Green occupation is decreasing
-> apply the monotone-payment theorem directly.
```

The valid target is the weaker and stable statement

\[
V_+(M)\le\frac34M_2,
\]

or any sharper source-specific payment inequality. The first counterexample supports rather than refutes that target.

## 4. Exact boundary

```text
critical occupation monotonicity                 false
first exact witness                              X=14, step 6->7
variation gate at the witness                    holds with large slack
cofinal upward-variation theorem                 open / RH-bearing
factor-64 criterion and RH                       unproved
```
