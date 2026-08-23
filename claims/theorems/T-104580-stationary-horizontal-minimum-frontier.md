# T-104580 — Stationary horizontal-minimum frontier for the fixed-order Xi cascade

Claim ID: `T-104580`  
Status: **UNCONDITIONAL SOURCE IDENTITIES + CRITICAL-ONLY PROPORTION GATE**  
Created: 2026-08-23  
Depends on: `T-104540`, `L-104527`, `L-104537--L-104539`, `R-104519`  
RH status: **unproved**

## 1. Why this is a different target

The preceding modular routes sought the global sign

\[
\mathcal L_2(t)
=\Xi'''(t)^2-\Xi''(t)\Xi''''(t)\ge0
\qquad(t\in\mathbb R).
\]

That statement is sufficient but stronger than the fixed-order reverse-Rolle
application needs.  Conrey's theorem supplies a large set of **real zeros of
`Xi'''`**.  At those points only, the sign of `L_2` determines whether the
critical point generates a real `Xi''` crossing.

`L-104537` identifies this sign with horizontal modulus curvature:

\[
\mathcal L_2(c)
={1\over2}
\left.{d^2\over dh^2}|\Xi''(c-ih)|^2\right|_{h=0}
\qquad(\Xi'''(c)=0).
\tag{T-104580.1}
\]

Thus the direct fixed-order problem is a stationary horizontal
minimum problem for `Xi''`, sampled only at the real zeros of `Xi'''`.

## 2. Exact proportion conversion

Let `q` be the lower density, among Conrey's real `Xi'''` zeros, of points for
which `h=0` is a nonnegative local minimum of `|Xi''(c-ih)|`.  Then

\[
\boxed{
\alpha_2\ge(2q-1)\alpha_3.
}
\tag{T-104580.2}
\]

With the unconditional input `alpha_3>0.9873`, every theorem `q>1/2` gives an
explicit positive line proportion for `xi''` derived from the third derivative:

\[
\boxed{
\alpha_2>(2q-1)\,0.9873.
}
\tag{T-104580.3}
\]

This is strictly weaker than pointwise `LAG2XI104550` and makes the known
third-derivative theorem load bearing.

## 3. Proved bulk source theorem

Let

\[
\mathscr Z(z)=\int u^2\Phi(u)e^{zu}\,du.
\]

For every positive-Fourier weight `W` and every real horizontal shift `h`,
`L-104539` proves

\[
\boxed{
\int W(t)
\left[
 |\mathscr Z(h+it)|^2-|\mathscr Z(it)|^2
\right]dt\ge0.
}
\tag{T-104580.4}
\]

This is a nonlinear finite-shift theorem for the complete untruncated Riemann
source.  Its infinitesimal form is

\[
\int W(t)\mathcal L_2(t)dt\ge0.
\tag{T-104580.5}
\]

The real exponential family also satisfies exact midpoint log-convexity.
`R-104519` proves that neither result automatically continues to individual
stationary imaginary points.

## 4. Two corrected terminal gates

The new route separates source positivity from critical-point sampling.

```text
SHMIN104580 — stationary horizontal minima

A density q>1/2 of the real Xi''' zeros counted by Conrey satisfy

  |Xi''(c-ih)| >= |Xi''(c)|

for all sufficiently small real h (outside a zero-density degenerate set).
```

This gate alone implies (T-104580.3).

A more structural sufficient route is:

```text
CSAMP104580 — critical sampling of the positive bulk defect

Transfer the complete positive-Fourier horizontal-modulus theorem (T-104580.4)
to the Xi''' critical-point measure with a loss strictly below one half,
retaining the finite horizontal shift before h -> 0.
```

Then

\[
\boxed{
\mathrm{CSAMP104580}
\Longrightarrow
\mathrm{SHMIN104580}
\Longrightarrow
\alpha_2>0.
}
\tag{T-104580.6}
\]

A quantitative sampling loss gives the corresponding explicit constant in
(T-104580.3).

## 5. Analytic attack coordinates

The finite-shift quotient is

\[
\log { |\Xi''(c-ih)|^2\over |\Xi''(c)|^2 }.
\]

This is directly compatible with:

- horizontal-shift mollifiers in the Levinson--Conrey method;
- discrete moments sampled at derivative zeros;
- Beurling--Selberg or Carleson sampling for the real `Xi'''` zero set;
- the modular complete-source expansion of `T-104570`;
- adaptive theta truncation, because the finite shift is retained before the
  critical limit.

The route does not ask for positive definiteness of every mixed theta matrix,
a fixed orbit cutoff, or pointwise positivity away from derivative zeros.

## 6. Boundary

```text
bilateral variance determinant                 PROVED EXACT
horizontal-modulus curvature identity           PROVED EXACT
positive-Fourier weighted finite-shift defect    PROVED EXACT
real-to-imaginary generic continuation           FALSE
critical-only proportion conversion              PROVED EXACT
SHMIN104580                                      OPEN
CSAMP104580                                      OPEN
alpha_2 from alpha_3                             NOT YET ESTABLISHED
Riemann Hypothesis                               UNPROVED
```
