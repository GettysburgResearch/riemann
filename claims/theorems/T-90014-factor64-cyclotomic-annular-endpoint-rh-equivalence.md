# T-90014 — A zero-safe factor-64 annular inequality with fixed margin is equivalent to RH

Claim ID: `T-90014` (provisional range; branch-qualified)  
Title: The radix-two cyclotomic filter gives a seven-scale integer criterion on `[N,64N]`, retains every off-line zero, and is uniformly negative under RH  
Status: **PROPOSED COMPLETE RH EQUIVALENCE / FIXED-MARGIN THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90019`, `T-90008`; Landau's one-sign theorem  
Scope: factor-64 fixed-annulus criterion; no unconditional proof of its sign

## 1. Criterion

Define

\[
\begin{aligned}
 \mathcal V_{64}(X)={}&\sqrt2 A(X)-A(X/2)-\sqrt2 A(X/4)\\
 &+(1-\sqrt2)A(X/8)+A(X/16)\\
 &+\sqrt2 A(X/32)-A(X/64).
\end{aligned}
\tag{T-90014.1}
\]

Then the following are equivalent:

1. RH;
2. `V_64(X)<0` for every sufficiently large real `X`;
3. `V_64(X)` is eventually one-signed;
4. there exists `epsilon>0` such that
   \[
   \begin{aligned}
   \sqrt2 A_{64N}-A_{32N}-\sqrt2 A_{16N}
   +(1-\sqrt2)A_{8N}\\
   +A_{4N}+\sqrt2 A_{2N}-A_N
   \le-\epsilon
   \end{aligned}
   \]
   for every sufficiently large integer `N`.

Moreover RH implies

\[
\boxed{
 \mathcal V_{64}(X)<-0.01
}
\tag{T-90014.2}
\]

for every sufficiently large `X`.

## 2. RH-side fixed margin

`L-90019` proves that the unscaled filter has deterministic moat

\[
 C_{64}
 =3(1+\zeta(1/2))(1-1/\sqrt2)(\log2)^2<-0.194
\]

and exact unit-circle norm

\[
 \max_{|y|=1}|P_{64}(y)|<4.
\]

Under RH, the complete critical-line zero series is therefore bounded by

\[
 4(\log\xi)''(1/2)<0.185.
\]

Hence

\[
\boxed{
 \limsup_{X\to\infty}\mathcal U_{64}(X)<-0.009.
}
\tag{T-90014.3}
\]

Multiplication by `sqrt(2)` gives

\[
\boxed{
 \limsup_{X\to\infty}\mathcal V_{64}(X)<-0.012.
}
\tag{T-90014.4}
\]

This proves (T-90014.2).

## 3. Converse

The Mellin multiplier is

\[
 \sqrt2 P_{64}(2^{-z}).
\]

Its roots in the scale variable are

```text
1, 1, sqrt(2), -1, exp(2 pi i/3), exp(-2 pi i/3).
```

Every root has modulus at least one. If `rho` is a hypothetical nontrivial zero with `Re rho>1/2`, then

\[
 |2^{-(\rho-1/2)}|<1,
\]

so the pole at `rho-1/2` survives. The filtered transform has no singularity on the open positive real axis.

If `V_64(e^t)` were eventually one-signed, Landau's one-sign theorem would force a positive-real singularity at the abscissa of convergence in the presence of that off-line pole. This contradicts the pole audit. Thus eventual one-sidedness implies RH.

Together with Section 2, items 1--3 are equivalent.

## 4. Integer-scale form

At `X=64N`, all seven scales are integers:

\[
\boxed{
\begin{aligned}
 \mathcal V_{64}(64N)={}&\sqrt2 A_{64N}-A_{32N}
 -\sqrt2 A_{16N}\\
 &+(1-\sqrt2)A_{8N}+A_{4N}
 +\sqrt2 A_{2N}-A_N.
\end{aligned}}
\tag{T-90014.5}
\]

The bounded-step interpolation of `L-90004.24` shows that a fixed eventual margin on the aligned integer sequence extends to the real half-line. Conversely RH supplies a margin exceeding `0.01`. Hence item 4 is equivalent to the first three.

`L-90019` identifies the exact arithmetic support:

\[
\boxed{N<m\le64N.}
\tag{T-90014.6}
\]

## 5. Strategic consequence

The conclusion-producing statement is now the fixed factor-64 inequality

\[
\boxed{
\begin{aligned}
 \sqrt2 A_{64N}-A_{32N}-\sqrt2 A_{16N}
 +(1-\sqrt2)A_{8N}\\
 +A_{4N}+\sqrt2 A_{2N}-A_N<0
 \qquad(N\gg1).
\end{aligned}}
\tag{T-90014.7}
\]

It is supported on `[N,64N]`, has a strict RH-side margin, and cannot miss any off-line zero. Proving it unconditionally would prove RH.

## 6. Proof boundary

Closed, subject to independent review:

1. RH implies a fixed negative margin;
2. eventual one-sign implies RH;
3. real and aligned-integer fixed-margin forms are equivalent;
4. exact factor-64 support;
5. zero-safety of every cyclotomic dressing root.

Still open:

1. unconditional proof of (T-90014.7);
2. RH.

Replay: `experiments/X-90018-factor64-cyclotomic/verify.py`.
