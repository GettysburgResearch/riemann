# L-92300 — The safe Xi impedance has a universal fractional-string scaling limit

Claim ID: `L-92300`  
Status: **PROPOSED COMPLETE SAFE-AXIS ASYMPTOTIC — REVIEW REQUIRED**  
Created: 2026-08-14  
Depends on: the standard completed-xi formula; Stirling in sectors; absolute Euler convergence  
RH status: **unproved**

Put

\[
 \Xi(z)=\xi\!\left(\frac12+z\right),
 \qquad
 F(z)=\frac{\Xi'(z)}{\Xi(z)},
 \qquad
 p(t)=\frac{F(\sqrt t)}{\sqrt t},
 \qquad
 Z(t)=\frac1{p(t)}.
\]

The square root is the principal branch on

\[
 \Omega=\mathbb C\setminus(-\infty,0].
\]

## 1. Uniform safe-sector asymptotic

Let `K` be a compact subset of `Omega`.  Then there is `delta_K>0` such that

\[
 \Re\sqrt u\ge\delta_K
 \qquad(u\in K).
\]

For `x` sufficiently large and `u in K`, the point

\[
 s=\frac12+x\sqrt u
\]

lies in the absolute Euler half-plane.  From

\[
 \frac{\xi'}{\xi}(s)
 =\frac1s+\frac1{s-1}-\frac12\log\pi
  +\frac12\psi(s/2)+\frac{\zeta'}{\zeta}(s)
\]

and sectorial Stirling,

\[
 \boxed{
 F(x\sqrt u)
 =\frac12\log\frac{x\sqrt u}{2\pi}
  +O_K(x^{-1}).
 }
 \tag{L-92300.1}
\]

The Euler term is exponentially small on `K`; the displayed error is dominated
by the rational and digamma remainders.

Let

\[
 \ell_x=\log\frac{x}{2\pi}.
\]

Then

\[
 \boxed{
 \frac{2x}{\ell_x}p(x^2u)
 =u^{-1/2}
  \left(1+\frac{\log u}{2\ell_x}
  +O_K\!\left(\frac1{x\ell_x}\right)\right).
 }
 \tag{L-92300.2}
\]

In particular,

\[
 \boxed{
 \frac{2x}{\ell_x}p(x^2u)
 \longrightarrow u^{-1/2}
 }
 \tag{L-92300.3}
\]

locally uniformly on `Omega`.

## 2. The drifting complete-Bernstein exponent

Define

\[
 \boxed{
 \alpha_x=\frac12-\frac1{2\ell_x}.
 }
 \tag{L-92300.4}
\]

For `x` large enough, `0<alpha_x<1`.  Since

\[
 u^{-\alpha_x}
 =u^{-1/2}\exp\!\left(\frac{\log u}{2\ell_x}\right),
\]

(L-92300.2) sharpens to

\[
 \boxed{
 \frac{2x}{\ell_x}p(x^2u)
 =u^{-\alpha_x}
  \left[1+O_K(\ell_x^{-2})+O_K((x\ell_x)^{-1})\right].
 }
 \tag{L-92300.5}
\]

Taking reciprocals gives

\[
 \boxed{
 \frac{\ell_x}{2x}Z(x^2u)
 =u^{\alpha_x}
  \left[1+O_K(\ell_x^{-2})+O_K((x\ell_x)^{-1})\right].
 }
 \tag{L-92300.6}
\]

Thus the first correction to the half-power limit does not point out of the
complete-Bernstein cone: it merely moves along the passive power family
`u^alpha`, `0<alpha<1`.

## 3. Derivative convergence

Local uniform convergence on `Omega`, together with Cauchy's formula, gives
locally uniform convergence of every fixed derivative.  If

\[
 A_k(t)=\frac{(-1)^k}{k!}p^{(k)}(t),
 \qquad
 c_k(\alpha)=\frac{(\alpha)_k}{k!},
\]

then for every fixed `k`,

\[
 \boxed{
 \frac{2x^{2k+1}}{\ell_x}A_k(x^2u)
 =c_k(\alpha_x)u^{-\alpha_x-k}
  +O_{K,k}(\ell_x^{-2})+O_{K,k}((x\ell_x)^{-1}).
 }
 \tag{L-92300.7}

At the coarser limiting scale,

\[
 \frac{2x^{2k+1}}{\log x}A_k(x^2u)
 \longrightarrow
 \frac{\binom{2k}{k}}{4^k}u^{-k-1/2}.
\]

## 4. Homogeneous Krein-string interpretation

For `0<alpha<1`,

\[
 \boxed{
 u^\alpha
 =\frac{\sin(\pi\alpha)}{\pi}
  \int_0^\infty\frac{u}{u+s}s^{\alpha-1}\,ds.
 }
 \tag{L-92300.8}

Hence the renormalised Xi impedance converges to the impedance of the
homogeneous fractional Krein string of exponent `1/2`, and its first correction
is the same string with the slowly drifting exponent `alpha_x`.

The corresponding limiting admittance is `u^(-alpha_x)`.

## 5. Meaning

The high safe axis is universally passive to every fixed differential order,
regardless of RH.  A possible off-line zero of ordinate comparable with `x`
becomes, after the scaling `t=x^2u`, a pole lying only `O(1/x)` away from the
negative-real cut.  It is therefore invisible on compact subsets of `Omega`
in the limit.

This is the all-order safe-axis analogue of the finite-bandwidth limitation in
Claude's Gabor compression: fixed-complexity tests see the universal passive
background, while a sparse off-line pair survives only in a shrinking boundary
layer.

## 6. Exact boundary

```text
sectorial xi logarithmic-derivative asymptotic      PROPOSED COMPLETE
half-power admittance/impedance scaling              PROPOSED COMPLETE
drifting exponent alpha_x                            EXACT FIRST CORRECTION
all fixed derivative limits                         PROPOSED COMPLETE
homogeneous fractional-string representation         EXACT
uniform control up to growing derivative order       OPEN / NEXT CLAIMS
complete Bernstein property at finite x              OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
