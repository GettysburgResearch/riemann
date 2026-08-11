# L-91022 — The dyadic Cauchy detail has exact sixteenfold storage and a three-square residual

Claim ID: `L-91022`  
Status: **PROPOSED COMPLETE EXACT RATIONAL/PARAUNITARY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91010`, `L-91013`  
RH status: **unproved**

## 1. The dyadic detail profile

Put

\[
 n_a(u)=\frac{a^4}{(a^2+u^2)^2},
 \qquad
 d_a(u)=n_{2a}(u)-n_a(u).
 \tag{L-91022.1}
\]

On the critical line, `d_a(u)>=0`; `L-91010` gives its two-square
factorisation.  Write

\[
 x=\frac ua,
 \qquad y=x^2.
\]

Then

\[
 d_a(u)=\frac{16}{(4+y)^2}-\frac1{(1+y)^2}.
 \tag{L-91022.2}
\]

## 2. Exact sixteenfold delayed storage

At the doubled scale,

\[
 d_{2a}(u)
 =\frac{256}{(16+y)^2}-\frac{16}{(4+y)^2}.
 \tag{L-91022.3}
\]

Therefore

\[
\begin{aligned}
 d_a(u)-\frac1{16}d_{2a}(u)
 &={17\over(4+y)^2}-{1\over(1+y)^2}-{16\over(16+y)^2}\\
 &=\boxed{
 {y(378y^2+4401y+6048)
  \over
  (1+y)^2(4+y)^2(16+y)^2}
 }.
\end{aligned}
 \tag{L-91022.4}
\]

Hence

\[
 \boxed{
 d_a(u)\ge\frac1{16}d_{2a}(u)
 \qquad(a>0,\ u\in\mathbb R),
 }
 \tag{L-91022.5}
\]

with equality only at `u=0` and asymptotically at infinity.

The factor `16` is sharp: as `|u|/a->infinity`,

\[
 d_a(u)\sim15a^4u^{-4},
 \qquad
 d_{2a}(u)\sim240a^4u^{-4}=16d_a(u).
 \tag{L-91022.6}
\]

## 3. Exact three-square residual

Let

\[
 \Delta_a(u)=
 (u^2+a^2)(u^2+4a^2)(u^2+16a^2).
\]

Define

\[
\begin{aligned}
 r_{1,a}(u)&={\sqrt{6048}\,a^5u\over\Delta_a(u)},\\
 r_{2,a}(u)&={\sqrt{4401}\,a^4u^2\over\Delta_a(u)},\\
 r_{3,a}(u)&={\sqrt{378}\,a^3u^3\over\Delta_a(u)}.
\end{aligned}
 \tag{L-91022.7}
\]

Then (L-91022.4) is exactly

\[
 \boxed{
 d_a(u)
 ={1\over16}d_{2a}(u)
 +r_{1,a}(u)^2+r_{2,a}(u)^2+r_{3,a}(u)^2.
 }
 \tag{L-91022.8}
\]

Thus the normalized current detail returns at the doubled scale with
coefficient one and emits exactly three positive rational ports.

## 4. Coefficient-one normalization

Put

\[
 \widetilde d_a(u)=a^{-4}d_a(u),
 \qquad
 \widetilde r_{j,a}(u)=a^{-2}r_{j,a}(u).
\]

Since `(2a)^(-4)=a^(-4)/16`, (L-91022.8) becomes

\[
 \boxed{
 \widetilde d_a(u)
 =\widetilde d_{2a}(u)
 +\sum_{j=1}^3\widetilde r_{j,a}(u)^2.
 }
 \tag{L-91022.9}
\]

This is a literal coefficient-one delayed recurrence.

Iteration gives, for every integer `J>=1`,

\[
 \boxed{
 \widetilde d_a(u)
 =\widetilde d_{2^Ja}(u)
 +\sum_{j=0}^{J-1}\sum_{m=1}^3
  \widetilde r_{m,2^ja}(u)^2.
 }
 \tag{L-91022.10}
\]

For fixed real `u`, the terminal term tends to zero.  Hence the complete
critical-line detail has the exact all-generation frame expansion

\[
 \boxed{
 \widetilde d_a(u)
 =\sum_{j\ge0}\sum_{m=1}^3
  \widetilde r_{m,2^ja}(u)^2.
 }
 \tag{L-91022.11}
\]

## 5. Improved high-frequency cancellation

The original dyadic detail satisfies

\[
 d_a(u)=15a^4u^{-4}+O(a^6u^{-6}).
\]

The delayed leading term cancels exactly in the residual:

\[
 \boxed{
 d_a(u)-{1\over16}d_{2a}(u)
 =378a^6u^{-6}+O(a^8u^{-8}).
 }
 \tag{L-91022.12}
\]

Thus every recurrence step gains two powers of high-frequency decay.  This is
the rational-wavelet counterpart of higher Euler cancellation.

## 6. Physical residual kernel

With inverse Fourier convention

\[
 f^\vee(t)={1\over2\pi}\int_\mathbb R f(u)e^{iut}du,
\]

one has

\[
 n_a^\vee(t)={a\over4}(1+a|t|)e^{-a|t|}.
\]

Consequently the residual kernel in (L-91022.4) is

\[
 \boxed{
\begin{aligned}
 \mathfrak r_a(t)
 =a\Bigg[&-{1\over4}(1+a|t|)e^{-a|t|}\\
 &+{17\over32}(1+2a|t|)e^{-2a|t|}\\
 &-{1\over16}(1+4a|t|)e^{-4a|t|}\Bigg].
\end{aligned}
 }
 \tag{L-91022.13}
\]

It has zero integral and is the autocorrelation sum

\[
 \mathfrak r_a
 =\sum_{m=1}^3\varphi_{m,a}*\widetilde{\varphi_{m,a}},
 \tag{L-91022.14}
\]

where `Fourier(varphi_(m,a))=r_(m,a)`.  Therefore its complete
independent-frequency carrier matrix is positive semidefinite before any
arithmetic insertion.

## 7. Relation to the Q4 reserve law

The exact factor `16` is the same four-adic storage factor appearing in the
Q4 Kummer reserve programme.  Here it is not asymptotic: it is the sharp
pointwise coefficient selected by cancellation of the leading `u^(-4)` tail.
After the natural `a^(-4)` normalization it becomes coefficient one.

## 8. Boundary

Closed:

```text
sharp sixteenfold dyadic storage;
exact three-square residual;
coefficient-one normalized recurrence;
all-generation critical-line frame;
two extra powers of high-frequency cancellation per step;
explicit three-exponential physical residual kernel.
```

Open:

```text
prime-side positivity of the residual autocorrelation form;
source-complete physical realization of the three residual ports;
RH.
```
