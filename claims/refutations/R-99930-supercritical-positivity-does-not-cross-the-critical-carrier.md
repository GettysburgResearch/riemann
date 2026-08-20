# R-99930 — Supercritical positivity does not cross the last carrier

Claim ID: `R-99930`  
Status: **EXACT METHOD FIREWALL**  
Created: 2026-08-20  
RH status: **unproved**

The positivity of every `G_m`, `m>=2`, does not imply the sign of the critical
remainder `C_m`.

## 1. Differential ladder

Put

\[
 F_m(u)=e^{-mu/2}G_m(e^u).
\]

Because `S(1)=0`, there are no activation atoms, and distributionally

\[
 \boxed{F_m'(u)=2m e^{-u/2}F_{m-1}(u).}
 \tag{R-99930.1}
\]

Thus `F_2>=0` says only that the weighted primitive of `F_1` is nonnegative.
A signed density can have a nonnegative primitive while having arbitrarily many
negative subintervals.  For example, the step density

```text
q(u)= 1 on [0,1),
     -1 on [1,2),
      0 otherwise
```

has nonnegative cumulative integral everywhere, but its integral over `[1,2]`
is negative.  Smoothing the corners gives the same separator in `C-infinity`.

Consequently a finite-window scale difference of `F_2` is not certified by
`F_2>=0`.

## 2. Exact pole-lowering formula

For `a>1`, set

\[
 D_{\alpha,a}f(X)=f(X)-a^\alpha f(X/a).
\]

If `R_(m,0)=G_m` and

\[
 R_{m,k}=D_{(m-k+1)/2,a}R_{m,k-1},
\]

then, with `L=log a` and
`K_L(t)=e^(t/2) 1_[0,L](t)`, one has

\[
 \boxed{
 e^{-(m-k)u/2}R_{m,k}(e^u)
 =2^k\frac{m!}{(m-k)!}
  (K_L^{*k}*F_{m-k})(u).
 }
 \tag{R-99930.2}
\]

Hence `R_(m,k)>=0` for every `k<=m-2`, using `L-99930`.  The last
pole-cancelling step is

\[
 e^{-u/2}R_{m,m-1}(e^u)
 =2^{m-1}m!(K_L^{*(m-1)}*F_1)(u),
 \tag{R-99930.3}
\]

and has no sign supplied by the supercritical hierarchy.

## 3. Why positive Euler smoothing does not repair it

A positive dilation convolution has a strictly positive Mellin multiplier on
the positive real axis.  It cannot cancel the last positive-real carrier.
Any finite dilation filter which does cancel that carrier has total weighted
coefficient zero and is not positivity-preserving on the full cone of
nonnegative functions.

Therefore one cannot finish by any of the implications

```text
G_m >= 0 for all m>=2
  -> normalized G_2 monotone;

positive finite dilation smoothing
  -> cancellation of the last real carrier;

contracted alpha-child positivity
  -> native critical Euler sign.
```

The last critical remainder is a genuine arithmetic theorem, not an omitted
calculus step.