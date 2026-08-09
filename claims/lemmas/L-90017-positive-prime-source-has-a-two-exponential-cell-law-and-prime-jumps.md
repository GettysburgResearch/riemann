# L-90017 — The positive prime source has a two-exponential cell law and prime jumps

Claim ID: `L-90017` (provisional branch range)  
Title: On every unit endpoint interval the positive occupancy source is an explicit two-exponential radical state, while its only discontinuities are positive prime activations; the endpoint derivative has the opposite prime jumps  
Status: **PROPOSED COMPLETE EXACT FINITE-STATE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: `L-90016`; PR #352 `T-90009`; finite summation by parts  
Scope: exact prime endpoint dynamics; no cofinal sign or RH conclusion

## 1. Finite arithmetic coordinates

Write

\[
 \ell(N)=\log\operatorname{rad}(N),
 \qquad
 L(N)=\sum_{m\le N}\ell(m),
\tag{L-90017.1}
\]

and define

\[
 P_1(N)=\sum_{p\le N}{\log p\over p},
\tag{L-90017.2}
\]

\[
\boxed{
 S_1(N)=(N+1)\ell(N)-L(N).
}
\tag{L-90017.3}
\]

The last coordinate is exactly the first radical-switching moment:

\[
 S_1(N)
 =\sum_{m\le N}m[\ell(m)-\ell(m-1)].
\tag{L-90017.4}
\]

It is signed; for example powers of two can make it negative.

Let

\[
 a(t)=A(e^t)
\]

and let `mathcal Q_P` be the positive prime occupancy source of `L-90016`.

## 2. Source at integer endpoints

`L-90016.20` gives exactly

\[
\boxed{
 \mathcal Q_{\mathbb P}(\log N)
 ={1\over\sqrt N}
 [NP_1(N)-L(N)+\ell(N)].
}
\tag{L-90017.5}
\]

This is the right-continuous value. If `N` is prime, the new column `q=N` activates with occupancy deficit one. Therefore

\[
\boxed{
 \mathcal Q_{\mathbb P}(\log N^+)
 -\mathcal Q_{\mathbb P}(\log N^-)
 =\mathbf1_{N\ {m prime}}{\log N\over\sqrt N}.
}
\tag{L-90017.6}
\]

Every existing occupancy sawtooth is continuous at both ends of each unit occupied interval, so there is no other jump.

## 3. Exact cell formula

Fix an integer `N>=2` and let

\[
 N<X<N+1,
 \qquad t=\log X.
\]

For a prime `p<=N`, the occupancy deficit has slope

\[
 {d\over dX}\Delta_p(X)
 =\begin{cases}
 -(1-p^{-1}),&p\mid N,\\
 p^{-1},&p\nmid N.
 \end{cases}
\tag{L-90017.7}
\]

Hence

\[
 {d\over dX}
 \sum_{p\le N}(\log p)\Delta_p(X)
 =P_1(N)-\ell(N).
\tag{L-90017.8}
\]

Using the endpoint value (L-90017.5) and (L-90017.3), the complete unnormalized source is

\[
\boxed{
 \sum_{p\le N}(\log p)\Delta_p(X)
 =X[P_1(N)-\ell(N)]+S_1(N).
}
\tag{L-90017.9}
\]

Therefore the positive source has the exact two-exponential form

\[
\boxed{
 \mathcal Q_{\mathbb P}(t)
 =e^{t/2}[P_1(N)-\ell(N)]
  +e^{-t/2}S_1(N),
 \qquad \log N<t<\log(N+1).
}
\tag{L-90017.10}
\]

Although the two coefficients may be signed, their displayed combination is positive because it equals the occupancy sum (L-90016.4).

Differentiating gives either of the equivalent state equations

\[
\boxed{
 \mathcal Q_{\mathbb P}'(t)
 =-\frac12\mathcal Q_{\mathbb P}(t)
  +e^{t/2}[P_1(N)-\ell(N)],
}
\tag{L-90017.11}
\]

or

\[
\boxed{
 \mathcal Q_{\mathbb P}'(t)
 =\frac12\mathcal Q_{\mathbb P}(t)
  -e^{-t/2}S_1(N).
}
\tag{L-90017.12}
\]

## 4. Endpoint derivative and curvature

From `L-90016.14`,

\[
 a'(t)={1\over2}M_0(t)-\mathcal Q_{\mathbb P}(t),
\tag{L-90017.13}
\]

where `M_0'=mathcal Q_P`. Consequently, on the open cell,

\[
 a''(t)
 ={1\over2}\mathcal Q_{\mathbb P}(t)
  -\mathcal Q_{\mathbb P}'(t).
\]

Using (L-90017.12),

\[
\boxed{
 a''(t)=e^{-t/2}S_1(N),
 \qquad \log N<t<\log(N+1).
}
\tag{L-90017.14}
\]

This independently recovers the second derivative of the radical-switching formula in `T-90009`.

Since `M_0` is continuous and the source has the jump (L-90017.6), the endpoint derivative has exactly the opposite jump:

\[
\boxed{
 a'(\log N^+)-a'(\log N^-)
 =-\mathbf1_{N\ {m prime}}{\log N\over\sqrt N}.
}
\tag{L-90017.15}
\]

All radical-switching increments cancel from the derivative jump. They act only through the smooth cell curvature `S_1(N)`; the impulses are purely prime.

## 5. Exact discrete derivative recursion

Put

\[
 V_N=a'(\log N^+).
\]

Integrating (L-90017.14) over the preceding logarithmic cell and applying (L-90017.15) gives

\[
\boxed{
\begin{aligned}
 V_N-V_{N-1}
 ={}&2S_1(N-1)
 \left({1\over\sqrt{N-1}}-{1\over\sqrt N}\right)\\
 &-\mathbf1_{N\ {m prime}}{\log N\over\sqrt N}.
\end{aligned}}
\tag{L-90017.16}
\]

Thus the stronger monotonicity problem is a completely explicit competition:

```text
smooth radical curvature accumulated over one cell
versus
one negative prime impulse at a prime endpoint.
```

No prime powers, zero sums, or continuous integrals are hidden in this recursion.

## 6. Three-state positive-source dynamics

Together, `L-90016` and this theorem give the exact state system

\[
\boxed{
 M_1'=M_0,
 \qquad
 M_0'=\mathcal Q_{\mathbb P},
 \qquad
 \mathcal Q_{\mathbb P}'
 ={1\over2}\mathcal Q_{\mathbb P}-e^{-t/2}S_1(N)
}
\tag{L-90017.17}
\]

on every open cell, with source jumps (L-90017.6). The RH-equivalent endpoint observable is

\[
\boxed{
 A(e^t)={1\over2}[M_1(t)-2M_0(t)].
}
\tag{L-90017.18}
\]

This is a finite-dimensional, positivity-preserving state description of the live endpoint criterion. The only unbounded arithmetic input is the explicit radical moment `S_1(N)` and the prime impulse stream.

## 7. Proof boundary

Closed exactly:

1. the integer source formula;
2. the two-exponential source law on every cell;
3. positive prime activation jumps;
4. the signed radical curvature;
5. the negative prime jumps of the endpoint derivative;
6. the exact discrete derivative recursion;
7. the three-state source dynamics.

Open:

1. a Lyapunov or comparison theorem forcing `M_1<2M_0`;
2. eventual negativity of the endpoint;
3. RH.