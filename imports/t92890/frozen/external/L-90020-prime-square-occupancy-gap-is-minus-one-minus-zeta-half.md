# L-90020 — The prime-square occupancy gap is exactly `-1-zeta(1/2)`

Claim ID: `L-90020` (provisional branch range)  
Title: The positive complete-prime-power occupancy source exceeds the prime-only source by a bank converging to `-1-zeta(1/2)`; this is exactly the source-level origin of the negative quadratic logarithmic drift  
Status: **PROPOSED COMPLETE UNCONDITIONAL ASYMPTOTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: `L-90016`; the prime number theorem in the form `theta(x)~x`; elementary zeta continuation on `(0,1)`  
Scope: source asymptotics and drift identification; no control of the RH-sensitive residual and no RH conclusion

## 1. Prime and complete prime-power sources

Retain

\[
 \mathcal Q_{\mathbb P}(t)
 =e^{-t/2}\sum_{p\le e^t}(\log p)\Delta_p(e^t)
\]

and

\[
 \mathcal Q_\Lambda(t)
 =e^{-t/2}\sum_{q\le e^t}\Lambda(q)\Delta_q(e^t).
\]

Their difference is the positive higher-prime-power source

\[
\boxed{
 \mathcal Q_{\rm pp}(t)
 :=\mathcal Q_\Lambda(t)-\mathcal Q_{\mathbb P}(t)
 =e^{-t/2}
  \sum_{\substack{p^a\le e^t\\a\ge2}}
  (\log p)\Delta_{p^a}(e^t)
 \ge0.
}
\tag{L-90020.1}
\]

The theorem is

\[
\boxed{
 \lim_{t\to\infty}\mathcal Q_{\rm pp}(t)
 =-1-\zeta(1/2)>0.
}
\tag{L-90020.2}
\]

## 2. Higher powers beyond squares vanish

Put

\[
 x=e^t,
 \qquad y=\sqrt x.
\]

Since `0<Delta_q<=1`, the contribution of exponents `a>=3` is at most

\[
 {1\over\sqrt x}
 \sum_{a\ge3}\vartheta(x^{1/a}),
\tag{L-90020.3}
\]

where `vartheta` is Chebyshev's prime theta function.

The elementary Chebyshev bound `vartheta(u)<<u` gives

\[
 \sum_{a\ge3}\vartheta(x^{1/a})
 \ll x^{1/3}+x^{1/4}\log x
 =o(\sqrt x).
\tag{L-90020.4}
\]

Hence

\[
\boxed{
 {1\over\sqrt x}
 \sum_{\substack{p^a\le x\\a\ge3}}
 (\log p)\Delta_{p^a}(x)=o(1).
}
\tag{L-90020.5}
\]

Only prime squares contribute to the limit.

## 3. Square occupancy becomes a fractional-part profile

For any integer `q` and real `x>=q`, write

\[
 r=x-q\lfloor x/q\rfloor.
\]

The sawtooth formula gives

\[
 \Delta_q(x)=\{x/q\}
\]

unless `0<=r<1`; in that exceptional unit interval,

\[
 0\le\Delta_q(x)-\{x/q\}\le1.
\tag{L-90020.6}
\]

For `q=p^2`, an exceptional prime has an integer multiple of `p^2` in the interval `[x-1,x]`. There are at most two possible integers `n` in that interval, and

\[
 \sum_{p^2\mid n}\log p\le\frac12\log n.
\]

Therefore

\[
\boxed{
 {1\over y}\sum_{p\le y}(\log p)
 \left[
  \Delta_{p^2}(x)-\{x/p^2\}
 \right]
 =o(1).
}
\tag{L-90020.7}
\]

Since `x=y^2`, define on `(0,1]`

\[
\boxed{
 f(u)=\{u^{-2}\}.
}
\tag{L-90020.8}
\]

Then

\[
 \{x/p^2\}=f(p/y).
\]

The function `f` is bounded and Riemann integrable: its discontinuities are the countable set `u=n^{-1/2}`, accumulating only at zero.

## 4. Prime-number-theorem Riemann sum

The PNT implies the weighted weak convergence

\[
 {1\over y}\sum_{p\le y}(\log p)\delta_{p/y}
 \Longrightarrow du
\]

on `[0,1]`. Therefore, for the bounded Riemann-integrable function (L-90020.8),

\[
\boxed{
 {1\over y}\sum_{p\le y}(\log p)f(p/y)
 \longrightarrow\int_0^1\{u^{-2}\}\,du.
}
\tag{L-90020.9}
\]

Combining (L-90020.5), (L-90020.7), and (L-90020.9),

\[
\boxed{
 \mathcal Q_{\rm pp}(\log x)
 \longrightarrow
 \int_0^1\{u^{-2}\}\,du.
}
\tag{L-90020.10}
\]

## 5. Evaluation of the constant

Substitute `v=u^{-2}`:

\[
 \int_0^1\{u^{-2}\}\,du
 ={1\over2}\int_1^\infty\{v\}v^{-3/2}\,dv.
\tag{L-90020.11}
\]

For `0<s<1`, finite summation by parts gives the standard continuation identity

\[
 \zeta(s)
 ={s\over s-1}
 -s\int_1^\infty\{v\}v^{-s-1}\,dv.
\tag{L-90020.12}
\]

At `s=1/2`,

\[
 {1\over2}\int_1^\infty\{v\}v^{-3/2}\,dv
 =-1-\zeta(1/2).
\tag{L-90020.13}
\]

Since `zeta(1/2)<-1`, the constant is strictly positive. This proves (L-90020.2).

## 6. The common critical source baseline

At integer endpoints, `L-90016.21` gives

\[
 e^{-t/2}\mathcal Q_\Lambda(t)
 =\sum_{q\le N}{\Lambda(q)\over q}
  -{\log(N!)\over N}+{\log N\over N},
 \qquad t=\log N.
\]

The classical formulas

\[
 \sum_{q\le N}{\Lambda(q)\over q}
 =\log N-\gamma+o(1)
\]

and Stirling's theorem give

\[
\boxed{
 e^{-t/2}\mathcal Q_\Lambda(t)
 \longrightarrow1-\gamma.
}
\tag{L-90020.14}
\]

Equation (L-90020.2) is lower order by a factor `e^{-t/2}`, so the prime source has the same critical baseline:

\[
\boxed{
 e^{-t/2}\mathcal Q_{\mathbb P}(t)
 \longrightarrow1-\gamma.
}
\tag{L-90020.15}
\]

Thus both sources are asymptotic to the neutral critical exponential `(1-gamma)e^(t/2)`. Their difference survives at constant order and is generated solely by prime squares.

## 7. Exact quadratic drift from the constant source gap

Let

\[
 F_\Lambda(X)=\sum_{q\le X}\Lambda(q)r_X(q),
 \qquad
 A(X)=F_{\mathbb P}(X),
\]

and put

\[
 H(X)=F_\Lambda(X)-A(X).
\]

By linearity of `L-90016.6`,

\[
 -H(e^t)
 =\int_0^t\left(1-{t-u\over2}\right)
  \mathcal Q_{\rm pp}(u)\,du.
\tag{L-90020.16}
\]

If

\[
 C_{\rm pp}=-1-\zeta(1/2),
\]

then (L-90020.2) and one elementary Cesaro estimate yield

\[
\boxed{
 H(e^t)
 ={C_{\rm pp}\over4}t^2+o(t^2).
}
\tag{L-90020.17}
\]

Therefore the prime-only endpoint differs from the complete prime-power endpoint by

\[
\boxed{
 -{C_{\rm pp}\over4}t^2
 ={1+\zeta(1/2)\over4}t^2,
}
\tag{L-90020.18}
\]

exactly the negative quadratic logarithmic coefficient found independently in PR #352 `L-90004`.

This identifies the drift without a prime-zeta pole calculation:

```text
prime squares
-> positive constant occupancy-source gap
-> universal one-sign-change Green kernel
-> negative log-squared prime-endpoint moat.
```

## 8. Significance

The prime-power moat is not merely an analytic cancellation among scaled prime-zeta copies. It has a positive physical source:

\[
 \mathcal Q_{\rm pp}(t)\ge0,
\]

and its leading constant is the elementary fractional-part integral

\[
 \int_0^1\{u^{-2}\}\,du.
\]

The RH-sensitive difficulty lies in the common critical baseline and its original-zero fluctuations. The deterministic favorable drift is entirely the prime-square source gap.

## 9. Proof boundary

Closed unconditionally, subject to review:

1. positivity of the prime-power source gap;
2. disappearance of powers `a>=3` after critical scaling;
3. PNT Riemann-sum reduction of squares;
4. evaluation of the constant as `-1-zeta(1/2)`;
5. the common `(1-gamma)e^(t/2)` source baseline;
6. recovery of the exact negative quadratic endpoint drift.

Open:

1. control of fluctuations around the common critical baseline;
2. the prime occupancy age bound;
3. RH.