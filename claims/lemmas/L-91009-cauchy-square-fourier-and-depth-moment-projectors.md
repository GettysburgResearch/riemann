# L-91009 — Cauchy-square soft counts have exact Fourier and depth-moment projectors

Claim ID: `L-91009`  
Status: **PROPOSED COMPLETE EXACT FINITE-PACKET THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91008`  
RH status: **unproved**

## 1. Line atom

Let

\[
 n_{a,0}(u)=\frac{a^4}{(a^2+u^2)^2},
 \qquad a>0,
\]

and use the Fourier convention

\[
 \widehat f(\xi)=\int_{\mathbb R}f(u)e^{-i\xi u}\,du.
\]

Then

\[
 \boxed{
 \widehat n_{a,0}(\xi)
 =
 \frac{\pi a}{2}
 (1+a|\xi|)e^{-a|\xi|}.
 }
 \tag{L-91009.1}
\]

In particular,

\[
 \boxed{
 \int_{\mathbb R}n_{a,0}(u)\,du
 =\frac{\pi a}{2},
 \qquad
 \int_{\mathbb R}u^2n_{a,0}(u)\,du
 =\frac{\pi a^3}{2}.
 }
 \tag{L-91009.2}
\]

## 2. Reflected pair inside the radial threshold

For a reflected pair of depth \(d\), put

\[
 n_{a,d}(u)
 =
 2\Re\frac{a^4}{[a^2-(d+iu)^2]^2}.
\]

When \(0<d<a\), contour translation across the pole-free strip gives

\[
 \boxed{
 \widehat n_{a,d}(\xi)
 =
 \pi a
 (1+a|\xi|)e^{-a|\xi|}
 \cosh(d\xi).
 }
 \tag{L-91009.3}
\]

When \(d>a\), closing on the opposite side gives zero total mass and zero
second moment. Away from the threshold \(d=a\),

\[
 \boxed{
 \int_{\mathbb R}n_{a,d}(u)\,du
 =
 \pi a\,\mathbf 1_{\{d<a\}},
 }
 \tag{L-91009.4}
\]

and

\[
 \boxed{
 \int_{\mathbb R}u^2n_{a,d}(u)\,du
 =
 \pi a(a^2-d^2)\mathbf 1_{\{d<a\}}.
 }
 \tag{L-91009.5}
\]

The threshold is singular; no value at \(d=a\) is asserted.

## 3. Exact squared-depth defect

A critical-line atom saturates the identity

\[
 a^2\int n_{a,0}
 -
 \int u^2n_{a,0}
 =0.
\]

A reflected pair satisfies

\[
 \boxed{
 a^2\int_{\mathbb R}n_{a,d}(u)\,du
 -
 \int_{\mathbb R}u^2n_{a,d}(u)\,du
 =
 \pi a d^2\,\mathbf 1_{\{d<a\}}.
 }
 \tag{L-91009.6}
\]

Consequently, for a finite packet whose atoms share one ordinate \(\gamma\),
and for \(a\) larger than every active depth,

\[
 \boxed{
 \begin{aligned}
 &a^2\int_{\mathbb R}\mathcal N_{Z,x}(a)\,dx\\
 &\quad-
 \int_{\mathbb R}(x-\gamma)^2
 \mathcal N_{Z,x}(a)\,dx
 =
 \pi a
 \sum_{\text{right pairs}}m_\rho d_\rho^2.
 \end{aligned}
 }
 \tag{L-91009.7}
\]

Thus the first two centred moments recover the complete squared horizontal
depth of the packet exactly.

## 4. Fourier signature and the Zeta23 block

For a finite packet and \(a\) larger than all its depths, translation by each
ordinate gives

\[
 \boxed{
 \begin{aligned}
 \widehat{\mathcal N}_{Z,a}(\xi)
 ={}&
 \frac{\pi a}{2}(1+a|\xi|)e^{-a|\xi|}\\
 &\cdot\left[
 \sum_{\text{line}}m_\gamma e^{-i\gamma\xi}
 +
 2\sum_{\text{right pairs}}
 m_\rho\cosh(d_\rho\xi)e^{-i\gamma_\rho\xi}
 \right].
 \end{aligned}
 }
 \tag{L-91009.8}
\]

After division by the explicit positive Cauchy envelope, the line block has
weight one and an off-line reflected pair has the hyperbolic weight
\(2\cosh(d\xi)\). This is exactly the signature geometry underlying the
finite Zeta23 rank-trace compression:

```text
critical-line atom       rank-one positive phase;
off-line reflected pair  one hyperbolic signature block.
```

The soft count therefore gives a direct scalar bridge between the radial
curvature route and the Zeta23 finite-compression architecture.

## 5. Differentiating recovers the PR #394 depth projector

Since

\[
 \partial_a n_{a,d}=4a^3 c_{a,d},
\]

differentiating (L-91009.4) and (L-91009.5), away from \(a=d\), gives

\[
 \int_{\mathbb R}c_{a,d}(u)\,du
 =
 \frac{\pi}{4a^3}\mathbf 1_{\{d<a\}},
\]

and

\[
 \int_{\mathbb R}u^2c_{a,d}(u)\,du
 =
 \left(
 \frac{3\pi}{4a}
 -
 \frac{\pi d^2}{4a^3}
 \right)\mathbf 1_{\{d<a\}}.
\]

The first identity is precisely the sharp parabolic depth projector of
`L-91005`.

## 6. Firewall

The unweighted mass in (L-91009.4) counts a reflected pair positively and with
the same total two-zero mass as two line zeros. Therefore neither the soft-count
mass nor the unweighted centre average can prove RH. The conclusion-producing
information is the **pointwise monotonicity**, a signed localisation, or a
nontrivial frequency/depth statistic such as (L-91009.6).
