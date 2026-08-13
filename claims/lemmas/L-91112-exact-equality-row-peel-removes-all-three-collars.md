# L-91112 — Exact equality rows remove the target mismatch, terminal annulus, and quantization collar simultaneously

> **REFUTED / DO NOT USE.** `R-91102` gives the exact counterexample
> `X=3,m=2`. The Volterra integral in the original display (L-91112.11)
> generates the continuum seed `overline b_X^star`, not the finite Riemann-sum
> seed `b_X^star`. Consequently the claimed exact finite equality-row
> representation, outer saturation, terminal saturation, and zero-debt score
> split do not follow. The independently valid parts are retained below.

Claim ID: `L-91112` (provisional research range)  
Title: Historical proposed exact equality-row peel  
Status: **REFUTED BY `R-91102` — PARTIAL LEMMAS RETAINED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-12  
Depends on: PR #265 `L-26201/L-26204`; `L-91106/L-91107`  
Scope: the continuum infinitesimal-row and positive component-row formulas survive; the exact finite peel is false

## 1. Real endpoint rows

For real `s>=2`, retain the zero-extended parabolic seed

\[
 b_s(m)=2\sqrt m\left[
 \log\frac sm-2\left(1-\sqrt{m/s}\right)
 \right]\mathbf 1_{m\le s}.
\tag{L-91112.1}
\]

Put

\[
 A_s(m)=\frac{b_s(m)}{m-1},
 \qquad
 d_s(n)=(n+1)[A_s(n)-2A_s(n+1)+A_s(n+2)].
\tag{L-91112.2}
\]

For `s>=m`,

\[
 \dot A_s(m)
 =\frac{2}{m-1}\left(
 \frac{\sqrt m}{s}-\frac{m}{s^{3/2}}
 \right).
\tag{L-91112.3}
\]

## 2. Infinitesimal endpoint positivity — retained

For every integer `n>=2`,

\[
\boxed{
 \dot d_s(n)\ge0
 \qquad(s\ge n).
}
\tag{L-91112.4}
\]

For `n<s<n+1`, only `A_s(n)` is active and the sign is immediate. For
`n+1<s<n+2`, the boundary inequality from PR #265 gives the sign. For
`s>=n+2`, the exact derivative

\[
 C_s''(x)=
 \frac{
 3\sqrt s\,x^2+6\sqrt s\,x-\sqrt s-8x^{3/2}
 }
 {2\sqrt s\,x^{3/2}(x-1)^3}
\]

is positive on `[n,n+2]`, so the discrete second difference is positive.
This part of the original proposal is independent of the false finite/continuum
identification.

## 3. The load-bearing false identity

The original proposal asserted

\[
 b_X^\star(m)
 =\int_m^X L(X/s)\,\partial_s b_s(m)\,ds.
\tag{L-91112.11-FALSE}
\]

The right side is the continuum Volterra seed

\[
 \overline b_X^\star(m)=\sqrt X\,\mathscr B^\star(m/X),
\]

whereas the finite seed is the left Riemann sum

\[
 b_X^\star(m)=\sum_{r=m}^{X}d_X^\star(r).
\]

`R-91102` proves the discrepancy exactly at `X=3,m=2`. Therefore the
original displays claiming exact finite row integration and exact truncation
saturation are withdrawn.

## 4. Positive component-row identity — retained

Define

\[
 h_Y(m)=m^{-1/2}\log(Y/m)\mathbf1_{m\le Y},
 \qquad
 S_Y(n)=\sum_{m\ge n}h_Y(m),
\]

and

\[
 Q_Y(n)=(n+1)\Delta^2\left[\frac{S_Y(n)}{n-1}\right].
\]

Finite algebra gives

\[
\boxed{
\begin{aligned}
 Q_Y(n)={}&
 \frac{n+1}{n-1}[h_Y(n)-h_Y(n+1)]\\
 &+\frac{2(n+1)}{n(n-1)}h_Y(n+1)
 +\frac{2}{n(n-1)}S_Y(n+2)
 \ge0.
\end{aligned}}
\tag{L-91112.25}
\]

The exact finite equality row still has the valid decomposition

\[
\boxed{
 c_X(n)=
 \sum_{k\le X/n}
 \mu(k)k^{-1/2}Q_{X/k}(n).
}
\tag{L-91112.26}
\]

This is the correct row-level interface to the squarefree parity and delayed
rough-prime programmes.

## 5. Correct route after the refutation

The finite reset must retain the layers that (L-91112.11-FALSE) attempted to
remove:

```text
positive continuum factor-54 density                 L-91106/L-91107
positive martingale B-spline quantization             L-91110
positive width-three collar                           L-91111
finite Euler correction / quotient-knot atoms         L-91303
terminal quotient localization                        L-91306
parity-resolved rough-prime renewal                    L-91109/L-91113
```

## 6. Correct proof boundary

```text
infinitesimal real-endpoint row positivity          RETAINED
positive component-row formula Q_Y                 RETAINED
finite seed = continuum Volterra seed               FALSE
exact finite outer equality-row peel                FALSE
exact terminal-annulus saturation from that peel   FALSE
correct finite Euler/quantization route             OPEN BUT QUANTITATIVE
rough-prime capacity allocation                     OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVEN
```
