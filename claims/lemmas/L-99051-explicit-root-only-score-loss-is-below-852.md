# L-99051 — After score-isometric unfolding, the complete root-owned score loss is below 852

Claim ID: `L-99051`  
Status: **PROPOSED COMPLETE ELEMENTARY SCORE THEOREM**  
Created: 2026-08-19  
Depends on: `L-99022`, `L-99023`, `L-99050`  
RH status: **not assumed**

Put

\[
 W=10000,
 \qquad B=W+2=10002,
 \qquad K=\lfloor X/67\rfloor+1,
 \qquad
 \tau_K=\frac{\sqrt K}{\sqrt K+24}.
\]

Assume

\[
 X\ge X_0:=4B^2=400160016.
\tag{L-99051.1}
\]

## 1. Only two operations can lower literal score

By `L-99050`, compact Hall, the full finite causal tree, direct endpoint
integration, the retained inner cells, and optional exact cubature preserve the
literal physical-row score exactly. The only adverse operations are:

1. omission of the fixed top endpoint interval of width `B` before realization;
2. one scalar thinning by `tau_K` after the common row is assembled.

There is no arithmetic terminal debt, no quantization debt, and no finite-base
debt: the inner finite block is retained as part of the physical row.

## 2. Explicit top-omission score

For a real endpoint `s`, let

\[
 E(s)=\sum_{2\le m\le s}\frac{\log m}{\sqrt m}\log\frac sm
\]

be the literal score of the canonical component row. Away from activation
knots,

\[
 E'(s)=\frac1s\sum_{2\le m\le s}\frac{\log m}{\sqrt m}.
\tag{L-99051.2}
\]

For `s>=2`,

\[
 \sum_{2\le m\le s}\frac{\log m}{\sqrt m}
 \le\log s\sum_{m\le s}m^{-1/2}
 <2\sqrt s\log s,
\]

so

\[
 E'(s)<\frac{2\log s}{\sqrt s}.
\tag{L-99051.3}
\]

On the omitted interval `X-B<=s<=X`, one has `1<=X/s<2`, and the exact equality
density is

\[
 L(X/s)=2\sqrt{X/s}-1<2.
\]

Therefore the omitted literal score is below

\[
 4B\frac{\log X}{\sqrt{X-B}}
 <4\sqrt2 B\frac{\log X}{\sqrt X}.
\tag{L-99051.4}
\]

The function `log X/sqrt X` is decreasing for `X>=e^2`. At `X_0=4B^2`,
(L-99051.4) is at most

\[
 2\sqrt2\log(4B^2).
\]

The exact elementary bounds

\[
 \sqrt2<\frac32,
 \qquad
 e>\frac{27}{10},
 \qquad
 \left(\frac{27}{10}\right)^{20}>4B^2
\]

give `log(4B^2)<20`, and hence

\[
\boxed{
 \mathcal H(R_X^{\rm top})<60.
}
\tag{L-99051.5}

## 3. Explicit thinning cost

Since `K>X/67`,

\[
 4\sqrt X(1-\tau_K)
 =\frac{96\sqrt X}{\sqrt K+24}
 <96\sqrt{67}.
\tag{L-99051.6}
\]

Also

\[
 \sqrt{67}<\frac{33}{4},
\]

so

\[
\boxed{
 4\sqrt X(1-\tau_K)<792.
}
\tag{L-99051.7}

## 4. Final score

The unthinned equality-frame row has score `4sqrt X` by `L-99050.11`. Remove
the top packet and then thin once. Equations (L-99051.5)--(L-99051.7) give

\[
\begin{aligned}
 4\sqrt X-\mathcal H(d_X)
 &\le4\sqrt X(1-\tau_K)
   +\tau_K\mathcal H(R_X^{\rm top})\\
 &<792+60.
\end{aligned}
\]

Thus

\[
\boxed{
 \mathcal H(d_X)>4\sqrt X-852.
}
\tag{L-99051.8}

The elementary parabolic benchmark bound of `L-99025` now gives

\[
\boxed{
 J_\Lambda(X)-\mathcal H(d_X)
 <4\log X+852.
}
\tag{L-99051.9}

This is the complete score estimate. No local declared-score channel appears.
