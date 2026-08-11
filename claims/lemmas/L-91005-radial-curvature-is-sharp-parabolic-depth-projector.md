# L-91005 — Radial curvature is an exact parabolic projector onto zero depth

Claim ID: `L-91005`  
Status: **PROPOSED COMPLETE EXACT CONTOUR/FOURIER THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91004`  
RH status: **unproved**

## 1. Line kernel and Fourier transform

For `t>0`, put `a=sqrt(t)` and

\[
 K_t(u)=\frac{u^2}{(t+u^2)^3}.
\tag{L-91005.1}
\]

Its Fourier transform, in the convention

\[
 \widehat K_t(\ell)=\int_{\mathbb R}K_t(u)e^{-i\ell u}\,du,
\]

is

\[
 \boxed{
 \widehat K_t(\ell)
 =\frac{\pi}{8a^3}
 \left(1+a|\ell|-a^2\ell^2\right)e^{-a|\ell|}.
 }
\tag{L-91005.2}
\]

Indeed

\[
 K_t(u)=(u^2+a^2)^{-2}-a^2(u^2+a^2)^{-3},
\]

and differentiating the standard Cauchy transform

\[
 \int_{\mathbb R}\frac{e^{-i\ell u}}{u^2+a^2}\,du
 =\frac\pi a e^{-a|\ell|}
\]

gives (L-91005.2).

In particular

\[
 \boxed{
 \int_{\mathbb R}K_t(u)\,du
 =\frac\pi{8t^{3/2}}.
 }
\tag{L-91005.3}
\]

## 2. One reflected off-line pair

For depth `d>=0`, define

\[
 K_{t,d}^{\rm pair}(u)
 =-2\Re\frac{(d+iu)^2}{[t-(d+iu)^2]^3}.
\tag{L-91005.4}
\]

This is exactly the radial-curvature contribution of a right-side reflected pair whose ordinate differs from the centre by `u`.

### Theorem 2.1 (sharp depth projector)

For `d != sqrt(t)`,

\[
 \boxed{
 \int_{\mathbb R}K_{t,d}^{\rm pair}(u)\,du
 =\frac\pi{4t^{3/2}}
 \mathbf1_{\{d<\sqrt t\}}.
 }
\tag{L-91005.5}
\]

### Proof

Put

\[
 f_t(z)=\frac{z^2}{(t-z^2)^3}.
\]

The integral in (L-91005.5) is `-2 Re` of the integral of `f_t` on the vertical line `Re(z)=d`. The integrand is `O(|z|^-4)`. If `0<=d<a`, shift the line to the imaginary axis without crossing a pole. There

\[
 -2f_t(iu)=\frac{2u^2}{(t+u^2)^3},
\]

and (L-91005.3) gives `pi/(4a^3)`.

If `d>a`, shift the line to `Re(z)->+infinity`. The integral tends to zero, and there is no pole between the original line and infinity. Equivalently, shifting from the imaginary axis across the third-order pole at `z=a` cancels the value in the first case. This proves (L-91005.5). `square`

For `d<a`, the complete Fourier transform is also explicit:

\[
 \boxed{
 \widehat K_{t,d}^{\rm pair}(\ell)
 =2\cosh(d|\ell|)\widehat K_t(\ell).
 }
\tag{L-91005.6}
\]

It follows by shifting the two conjugate vertical lines to the imaginary axis before taking the real sum.

## 3. Finite zero packets

Let `Z` be a finite multiset invariant under conjugation and reflection about the critical line. Let `C_(Z,x)(t)` be its radial curvature, with one line kernel per critical-line zero and one pair kernel (L-91005.4) per right-side reflected pair. Then

\[
 \boxed{
 \frac{8t^{3/2}}\pi
 \int_{\mathbb R}\mathcal C_{Z,x}(t)\,dx
 =N_{0}(Z)
 +2N_{<\sqrt t}^{\rm off}(Z),
 }
\tag{L-91005.7}
\]

where `N_0` counts line zeros with multiplicity and `N_<sqrt(t)^off` counts right-side reflected pairs of depth less than `sqrt(t)`, again with multiplicity.

Thus the centre integral is a sharp cumulative projector in horizontal depth. It does not merely weight deeper zeros less; it includes a reflected pair with its full two-zero mass until the threshold `t=d^2`, and then removes it exactly.

## 4. Zeta interpretation and localization boundary

For the full zeta zero set, the unweighted integral over all centres and all ordinates diverges. Formula (L-91005.7) is therefore applied first to finite ordinate packets or after multiplying by a smooth centre window. Standard local zero counting then permits passage to the complete sum, with boundary errors determined by the variation scale of the window.

The Fourier formula (L-91005.2) shows the corresponding prime-side bandwidth. At radial height `a=sqrt(t)`, prime logarithms are weighted by

\[
 \left(1+a\log n-a^2(\log n)^2\right)e^{-a\log n}.
\tag{L-91005.8}
\]

As `t` decreases, the depth projector sharpens toward the critical line while the required prime range grows. This is the precise scalar version of the bandwidth barrier in the Zeta23 compression programme.

## 5. Boundary

Established here:

```text
exact Fourier transform of the line curvature kernel;
exact centre integral of one line zero;
sharp 0-or-2 depth projector for one off-line reflected pair;
finite-packet cumulative depth count;
explicit radial bandwidth/depth duality.
```

Not established here:

```text
uniform short-window passage as t->0;
all-depth prime-side trace control;
Riemann Hypothesis.
```
