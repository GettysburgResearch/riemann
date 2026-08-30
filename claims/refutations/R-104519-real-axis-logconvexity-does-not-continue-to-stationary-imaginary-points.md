# R-104519 — Real exponential-family log-convexity does not continue automatically to stationary imaginary points

Claim ID: `R-104519`  
Status: **EXACT COUNTEREXAMPLE / BINDING FIREWALL**  
Created: 2026-08-23  
RH status: **not assumed**

`L-104537` proves that every positive even source has a log-convex bilateral
Laplace transform on the real axis.  That fact alone does not imply the
stationary horizontal-minimum theorem needed on the imaginary axis.

Take the positive symmetric atomic source

\[
d\mu
={1\over2}(\delta_{1}+\delta_{-1})
+{1\over4}(\delta_{2}+\delta_{-2}).
\]

Its bilateral partition function is

\[
\mathscr Z(z)=\cosh z+\frac12\cosh 2z.
\tag{R-104519.1}
\]

For every real `x`,

\[
\mathscr Z(x)\mathscr Z''(x)-\mathscr Z'(x)^2
=\mathscr Z(x)^2\operatorname{Var}_{\mu_x}(u)>0.
\tag{R-104519.2}
\]

Thus the complete real exponential family is strictly log-convex.

At the stationary imaginary point `z=i pi`, however,

\[
\mathscr Z(i\pi)=-\frac12,
\qquad
\mathscr Z'(i\pi)=0,
\qquad
\mathscr Z''(i\pi)=1.
\]

Therefore

\[
\boxed{
\mathscr Z(i\pi)\mathscr Z''(i\pi)-\mathscr Z'(i\pi)^2
=-\frac12<0.
}
\tag{R-104519.3}
\]

Equivalently,

\[
|\mathscr Z(h+i\pi)|^2
<|\mathscr Z(i\pi)|^2
\]

for all sufficiently small nonzero real `h`.

This source is positive, even, compactly supported and has exact real-axis
midpoint log-convexity.  Hence none of the following is a valid closure:

```text
positive source;
real-axis variance positivity;
real-axis log-convexity;
evenness plus stationarity;
positive-Fourier averaged horizontal convexity.
```

A successful proof of `SHMIN104580` must use additional Riemann-source
structure or a critical-point sampling theorem.  It may not analytically
continue the real variance sign by a generic maximum principle.
