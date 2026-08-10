# L-90026 — The factor-four block atom removes an independent geometric scale delay and admits a Gamma martingale

Claim ID: `L-90026` (provisional range; branch-qualified)  
Title: The positive factor-four endpoint detail is a probability law `Y`; the original endpoint atom is `Y` plus an independent geometric lattice delay, and centered `Y` is dominated by `Gamma(2,1/2)` in convex order  
Status: **PROPOSED COMPLETE EXACT PROBABILITY / CONVEX-ORDER THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-10  
Depends on: `L-90025`; the endpoint law of PR #353 `L-90022`; elementary stop-loss calculus  
Scope: exact continuum probability transport aligned with the first factor of the preferred factor-64 filter; no finite arithmetic martingale lift and no RH conclusion

## 1. The positive block law

Let

\[
 L=\log4,
 \qquad
 \eta_4(t)=\varrho(t)-\varrho(t-L),
\]

with causal zero extension. `L-90025` proves

\[
 \eta_4(t)>0\qquad(t>0).
\tag{L-90026.1}
\]

The critical endpoint law `V` of PR #353 has density

\[
 f_V(t)={1\over2}e^{-t/2}\varrho(t).
\tag{L-90026.2}
\]

Define

\[
\boxed{
 f_Y(t)=e^{-t/2}\eta_4(t),
 \qquad t\ge0.
}
\tag{L-90026.3}
\]

This is a probability density. Indeed, using

\[
 \widehat\eta_4(z)=(1-4^{-z})\widehat\varrho(z)
\]

and `widehat(varrho)(1/2)=2`,

\[
 \int_0^\infty f_Y(t)dt
 =\widehat\eta_4(1/2)
 =(1-4^{-1/2})2=1.
\tag{L-90026.4}
\]

Let `Y` denote the resulting nonnegative random variable.

## 2. Exact geometric-delay decomposition

The positive renewal identity of `L-90025` is

\[
 \varrho(t)=\sum_{j\ge0}\eta_4(t-jL),
\]

where only finitely many terms are active. Multiplying by
`(1/2)e^{-t/2}` gives

\[
 f_V(t)
 =\sum_{j\ge0}2^{-(j+1)}f_Y(t-jL).
\tag{L-90026.5}
\]

Let `J` be geometric on the nonnegative integers with

\[
\boxed{
 \mathbb P(J=j)=2^{-(j+1)}.
}
\tag{L-90026.6}
\]

Then

\[
\boxed{
 V\overset d=Y+LJ,
 \qquad Y\perp J.
}
\tag{L-90026.7}
\]

Equivalently,

\[
 \phi_J(s)={1\over2-4^{-s}},
\]

and therefore

\[
\boxed{
 \phi_Y(s)=(2-4^{-s})\phi_V(s)
 ={(2-4^{-s})s\zeta(s+1)\over(s+1)(2s+1)}.
}
\tag{L-90026.8}
\]

The factor `2-4^{-s}` has all zeros on `Re s=-1/2`. Thus stripping the geometric delay loses no zero in the RH-facing shifted half-plane.

Since `EV=3-gamma` and `EJ=1`,

\[
\boxed{
 \mathbb EY=3-\gamma-\log4.
}
\tag{L-90026.9}
\]

## 3. A sharp elementary density envelope

The block density obeys the global bound

\[
\boxed{
 f_Y(t)<{9\over4}e^{-t}
 \qquad(t\ge0).
}
\tag{L-90026.10}
\]

### Proof

Put `x=e^t`, `m=floor(x/4)`, and `n=floor x`. For `x>=4`, equation
`L-90025.6` gives

\[
 e^{t/2}\eta_4(t)
 =2(n-2m)-\sqrt x(S_n-S_m).
\tag{L-90026.11}
\]

Composite trapezoid convexity for `u^{-1/2}` gives

\[
 S_n-S_m
 \ge2(\sqrt n-\sqrt m)
 +{1\over2}\left({1\over\sqrt n}-{1\over\sqrt m}\right).
\tag{L-90026.12}
\]

Since `x>=n`, write `n=4m+r`, `0<=r<=3`, and put

\[
 z=\sqrt{n/m}.
\]

Then (L-90026.11)--(L-90026.12) give

\[
 e^{t/2}\eta_4(t)
 \le {2r\over z+2}-{1\over2}+{z\over2}.
\tag{L-90026.13}
\]

For fixed `r`, the right side increases with `z`, while
`z<=sqrt(4+r)`. Its largest possible value occurs at `r=3,m=1` and equals

\[
 {5\over2}\sqrt7-{9\over2}<{9\over4},
\]

because `10sqrt(7)<27`, equivalently `700<729`.

For `0<=t<L`, one has `m=0` and `n=1,2,3`. The three direct values of
`e^{t/2}eta_4(t)` are bounded above by their left cell endpoints; the largest is

\[
 5-\sqrt3-\sqrt{3/2}<{9\over4}.
\]

Thus `eta_4(t)<(9/4)e^{-t/2}`. Multiplication by `e^{-t/2}` proves (L-90026.10). ∎

## 4. Centered Gamma convex order

Let

\[
 G\sim\operatorname{Gamma}(2,1/2),
 \qquad
 C_Y=4-\mathbb EY=1+\gamma+\log4.
\tag{L-90026.14}
\]

Then

\[
\boxed{
 Y+C_Y\le_{\rm cx}G.
}
\tag{L-90026.15}
\]

The means agree, so it is enough to compare stop-loss transforms.

For thresholds `a<=C_Y`, nonnegativity of `Y` gives

\[
 \operatorname{SL}_{Y+C_Y}(a)=4-a.
\]

Exactly as in the Gamma-carry theorem, the Gamma stop-loss

\[
 \operatorname{SL}_G(a)=(a+4)e^{-a/2}
\]

is at least `4-a` for every `a>=0`, with equality at zero; thresholds below zero are automatic.

Now put `a=C_Y+b`, `b>=0`.

For `0<=b<=1`,

\[
 \operatorname{SL}_Y(b)\le\mathbb EY=4-C_Y.
\]

The elementary bounds

\[
 {57\over100}<\gamma<{58\over100},
 \qquad
 {69\over100}<\log2<{7\over10}
\]

give

\[
 {59\over20}<C_Y<3,
 \qquad
 \mathbb EY<{21\over20}.
\]

The Gamma stop-loss is decreasing on the positive axis, so

\[
 \operatorname{SL}_G(C_Y+b)
 \ge\operatorname{SL}_G(4)
 ={8\over e^2}>{16\over15}>{21\over20},
\]

where `e^2<15/2` follows from the standard exponential-series estimate already used in `L-33101`.

For `b>=1`, the density envelope gives

\[
 \operatorname{SL}_Y(b)
 \le{9\over4}e^{-b}.
\tag{L-90026.16}
\]

On the other hand

\[
 \operatorname{SL}_G(C_Y+b)
 =(C_Y+b+4)e^{-(C_Y+b)/2}.
\]

After multiplying by `e^b`, the left side of the desired comparison decreases in `b` and the right side increases. At `b=1`,

\[
 {9\over4}e^{(C_Y-1)/2}
 <{9\over4}e<{27\over4}
 <{159\over20}<C_Y+5.
\]

Thus the stop-loss inequality holds for all thresholds, proving (L-90026.15).

By Strassen's theorem there exists a martingale coupling

\[
\boxed{
 X\overset d=Y+C_Y,
 \quad Z\overset d=G,
 \quad \mathbb E[Z\mid X]=X.
}
\tag{L-90026.17}
\]

## 5. Strict critical moment margin

The exponential is strictly convex and the two laws are not equal. Therefore

\[
 \mathbb E e^{(Y+C_Y)/8}
 <\mathbb E e^{G/8}={16\over9}.
\tag{L-90026.18}
\]

The left side has the exact closed form

\[
\boxed{
 \mathbb E e^{(Y+C_Y)/8}
 =-{4\over21}
 (2-2^{1/4})e^{C_Y/8}\zeta(7/8).
}
\tag{L-90026.19}
\]

Hence the normalized critical propagation factor is

\[
\boxed{
 \rho_Y
 =-{3\over28}(2-2^{1/4})e^{C_Y/8}\zeta(7/8)<1.
}
\tag{L-90026.20}
\]

This closes the pure square-root state mode directly for the positive factor-four block atom aligned with the preferred factor-64 filter.

## 6. Meaning for the factor-64 route

The first factor `(1-S^2)` in the preferred filter is not merely an algebraic scale difference. Under critical probability normalization it performs the exact deconvolution

```text
endpoint atom V
=
positive block atom Y
+
independent geometric log-scale delay.
```

The block atom `Y`, after centering, has a state-dependent martingale transport to the sharp Gamma target and a strict critical moment margin. Thus the remaining two first-order detail filters in `L-90025.22` act on a probability state whose critical convex-order mode is already controlled.

The unresolved step is finite and source-specific: lift this martingale through the two detail filters while preserving the arithmetic carry/occupancy state. No positivity of the reciprocal-zeta independent deconvolution factor is assumed.

## 7. Proof boundary

Closed exactly, subject to review:

1. the block probability law `Y`;
2. the independent geometric-delay decomposition of the endpoint atom;
3. the zero-safe transform factor;
4. the global exponential density envelope;
5. centered convex-order domination by `Gamma(2,1/2)`;
6. the martingale coupling;
7. the strict critical square-root moment margin.

Still open:

1. a finite state-dependent lift through the remaining factor-64 detail filters;
2. the three-window occupancy inequality;
3. RH.
