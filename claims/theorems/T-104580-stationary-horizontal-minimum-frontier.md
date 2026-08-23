# T-104580 — Stationary horizontal-minimum and critical-value frontier

Claim ID: `T-104580`  
Status: **UNCONDITIONAL SOURCE/WEIGHTED THEOREMS + THREE CRITICAL-ONLY GATES**  
Created: 2026-08-23  
Depends on: `T-104540`, `L-104527`, `L-104537--L-104541`, `R-104519`  
RH status: **unproved**

## 1. Why this is a different target

The preceding modular routes sought the global sign

\[
\mathcal L_2(t)
=\Xi'''(t)^2-\Xi''(t)\Xi''''(t)\ge0
\qquad(t\in\mathbb R).
\]

That statement is sufficient but stronger than the fixed-order reverse-Rolle
application needs. Conrey's theorem supplies a large set of **real zeros of
`Xi'''`**. At those points only, the sign of `L_2` determines whether the
critical point generates a real `Xi''` crossing.

`L-104537` identifies this sign with horizontal modulus curvature:

\[
\mathcal L_2(c)
={1\over2}
\left.{d^2\over dh^2}|\Xi''(c-ih)|^2\right|_{h=0}
\qquad(\Xi'''(c)=0).
\tag{T-104580.1}
\]

Thus the direct fixed-order problem is a stationary horizontal-minimum problem
for `Xi''`, sampled only at the real zeros of `Xi'''`.

## 2. Exact proportion conversion

Let `q` be the lower density, among Conrey's real `Xi'''` zeros, of points for
which `h=0` is a nonnegative local minimum of `|Xi''(c-ih)|`. Then

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

## 3. Proved complete-source bulk theorem

Let

\[
\mathscr Z(z)=\int_{\mathbb R}u^2\Phi(u)e^{zu}\,du.
\]

For every positive-Fourier weight `W` and every real horizontal shift `h`,
`L-104539` proves

\[
\boxed{
\int_{\mathbb R} W(t)
\left[
 |\mathscr Z(h+it)|^2-|\mathscr Z(it)|^2
\right]dt\ge0.
}
\tag{T-104580.4}
\]

This is a nonlinear finite-shift theorem for the complete untruncated Riemann
source. Its infinitesimal form is

\[
\boxed{
\int_{\mathbb R}W(t)\mathcal L_2(t)dt\ge0.
}
\tag{T-104580.5}
\]

The real exponential family also satisfies exact midpoint log-convexity.
`R-104519` proves that neither result automatically continues to individual
stationary imaginary points.

## 4. New unconditional weighted reverse Rolle

`L-104540` proves directly, with no Fourier or zero-density hypothesis,

\[
\boxed{
\sum_{\Xi'''(c)=0}^{\rm good}|\Xi''(c)|
-
\sum_{\Xi'''(c)=0}^{\rm wrong}|\Xi''(c)|
={1\over2}\int_{\mathbb R}|\Xi'''(t)|dt>0.
}
\tag{T-104580.6}
\]

Thus the Rolle-generating critical points already carry strictly more than
half of the complete **critical-value amplitude mass**. Equivalently, there is
an amplitude threshold at which good critical points outnumber wrong ones.

This is an unconditional Xi-specific converse to Rolle, but its weight cannot
be discarded for free.

`L-104541` gives the exact missing conversion. Let

\[
\rho_T=
{\sum_{|c|<T}\varepsilon_c|\Xi''(c)|
 \over
 \sum_{|c|<T}|\Xi''(c)|},
\]

where `epsilon_c=+1` at a good point and `-1` at a wrong point, and let `v_T`
be the coefficient of variation of the amplitudes `|Xi''(c)|`. Then

\[
\boxed{
{G_T\over R_3(T)}
\ge {1\over2}+{\rho_T-v_T\over2}.
}
\tag{T-104580.7}
\]

Consequently,

\[
\boxed{
\liminf_{T\to\infty}(\rho_T-v_T)\ge\eta>0
\quad\Longrightarrow\quad
\alpha_2\ge\eta\alpha_3>0.9873\eta.
}
\tag{T-104580.8}
\]

This route uses only first and second moments of the actual critical values;
it neither counts parent zeros nor assumes the desired orientation.

## 5. Three corrected terminal gates

The programme now has three strictly weaker alternatives to global pointwise
Laguerre positivity.

```text
SHMIN104580 — stationary horizontal minima

A density q>1/2 of the real Xi''' zeros counted by Conrey satisfy

  |Xi''(c-ih)| >= |Xi''(c)|

for all sufficiently small real h, outside a zero-density degenerate set.
```

This gate alone implies (T-104580.3).

```text
CSAMP104580 — critical sampling of the positive bulk defect

Transfer the complete positive-Fourier horizontal-modulus theorem (T-104580.4)
to the Xi''' critical-point measure with a loss strictly below one half,
retaining the finite horizontal shift before h -> 0.
```

```text
AMPREG104580 — critical-value amplitude regularity

Prove

  liminf (rho_T-v_T) > 0

for the amplitudes |Xi''(c)| at the real zeros of Xi'''.
```

The exact implications are

\[
\boxed{
\mathrm{CSAMP104580}
\Longrightarrow
\mathrm{SHMIN104580}
\Longrightarrow
\alpha_2>0,
}
\tag{T-104580.9}
\]

and independently

\[
\boxed{
\mathrm{AMPREG104580}
\Longrightarrow
\alpha_2>0.
}
\tag{T-104580.10}
\]

Quantitative sampling or amplitude margins give the explicit constants in
(T-104580.3) and (T-104580.8).

## 6. Analytic attack coordinates

The finite-shift quotient

\[
\log { |\Xi''(c-ih)|^2\over |\Xi''(c)|^2 }
\]

is directly compatible with:

- horizontal-shift mollifiers in the Levinson--Conrey method;
- discrete moments sampled at derivative zeros;
- Beurling--Selberg or Carleson sampling for the real `Xi'''` zero set;
- the modular complete-source expansion of `T-104570`;
- adaptive theta truncation, because the finite shift is retained before the
  critical limit.

The amplitude route is compatible with:

- first and second moments of `Xi''` sampled at the real zeros of `Xi'''`;
- the exact total-variation numerator in (T-104580.6);
- dyadic critical-value level sets;
- short-window normalization, where the common gamma envelope can be removed
  before estimating amplitude dispersion.

Neither route asks for positive definiteness of every mixed theta matrix, a
fixed orbit cutoff, or pointwise positivity away from derivative zeros.

## 7. Boundary

```text
bilateral variance determinant                 PROVED EXACT
horizontal-modulus curvature identity           PROVED EXACT
positive-Fourier weighted finite-shift defect    PROVED EXACT
critical-value weighted reverse Rolle            PROVED UNCONDITIONALLY
amplitude-bias -> count-bias conversion           PROVED EXACT
real-to-imaginary generic continuation           FALSE
critical-only proportion conversion              PROVED EXACT
SHMIN104580                                      OPEN
CSAMP104580                                      OPEN
AMPREG104580                                     OPEN
alpha_2 from alpha_3                             NOT YET ESTABLISHED
Riemann Hypothesis                               UNPROVED
```
