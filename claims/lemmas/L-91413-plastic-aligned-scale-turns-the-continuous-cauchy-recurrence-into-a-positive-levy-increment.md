# L-91413 — A plastic-aligned scale turns the continuous Cauchy recurrence into a positive Lévy increment

Claim ID: `L-91413`  
Status: **PROVED EXACT SIGN-ALIGNMENT AND SCALAR NORMAL FORM; PRIME SAMPLING GATE OPEN**  
Created: 2026-08-12  
Depends on: `L-91022`, `L-91404`, `L-91410`  
RH status: **unproved**

## 1. The two independent sign switches

Retain

\[
 B(u)=\frac1{1-e^{-2u}}-(1+e^u)
 =\frac{1+e^u-e^{3u}}{e^{2u}-1}.
 \tag{L-91413.1}
\]

Let `varpi` be the plastic constant,

\[
 \varpi^3-\varpi-1=0,
 \qquad
 \kappa=\log\varpi.
 \tag{L-91413.2}
\]

Then

\[
 B(u)>0\quad(0<u<\kappa),
 \qquad
 B(u)<0\quad(u>\kappa).
 \tag{L-91413.3}

\]

The dimensionless physical Cauchy residual is

\[
\boxed{
 R(s)=
 -\frac14(1+s)e^{-s}
 +\frac{17}{32}(1+2s)e^{-2s}
 -\frac1{16}(1+4s)e^{-4s}.
 }
\tag{L-91413.4}

The scale-`a` residual is

\[
 \mathfrak r_a(u)=aR(au).
 \tag{L-91413.5}
\]

## 2. The residual has exactly one positive switch

Write

\[
 R(s)=e^{-s}(1+s)\left[H(s)-\frac14\right],
 \tag{L-91413.6}
\]

where

\[
 H(s)=
 \frac{17}{32}\frac{1+2s}{1+s}e^{-s}
 -\frac1{16}\frac{1+4s}{1+s}e^{-3s}.
 \tag{L-91413.7}
\]

A direct differentiation gives the exact factorization

\[
\boxed{
 H'(s)=
 -\frac{s e^{-3s}}{32(1+s)^2}
 \left[
  (34s+51)e^{2s}-(24s+30)
 \right].
 }
\tag{L-91413.8}

For `s>0`, the bracket is larger than

\[
 (34s+51)-(24s+30)=10s+21>0.
\]

Hence `H` is strictly decreasing on `(0,infinity)`.  Since

\[
 H(0)=\frac{15}{32}>\frac14,
 \qquad
 \lim_{s\to\infty}H(s)=0,
\]

there is a unique

\[
 \boxed{
 \tau_*=1.164606978873629364392900917962\ldots
 }
\tag{L-91413.9}
\]

such that

\[
 R(s)>0\quad(0\le s<\tau_*),
 \qquad
 R(s)<0\quad(s>\tau_*).
 \tag{L-91413.10}
\]

This proves the one-switch property without numerical root counting.

## 3. The plastic-aligned safe scale

Define

\[
 \boxed{
 a_\diamond=\frac{\tau_*}{\kappa}
 =4.14156736075304695202012003297\ldots .
 }
\tag{L-91413.11}

This is an unconditional safe scale: `a_diamond>1/2`.  By construction,

\[
 \frac{\tau_*}{a_\diamond}=\kappa.
\]

Therefore the two sign switches coincide, and

\[
 \boxed{
 B(u)\mathfrak r_{a_\diamond}(u)\ge0
 \qquad(u>0),
 }
\tag{L-91413.12}

with equality only at the common switch.

More generally, for arbitrary `a>0`, the product can be negative only on the
single compact interval with endpoints

\[
 \kappa,
 \qquad
 \frac{\tau_*}{a}.
 \tag{L-91413.13}

Thus all continuous sign mismatch is localized to one explicit compact cell,
and that cell disappears at `a=a_diamond`.

## 4. The nonprime recurrence channel

Let

\[
 h_x(u)=\cos(xu)-\mathbf1_{u\le1/2}.
\]

The exact three-scale source calculation of `L-91404`, together with the base
measure identity of `L-91410`, writes the continuous-plus-drift but nonprime
part of the coefficient-one recurrence as

\[
\boxed{
 \mathcal A_a(x)
 =d_a
 -2a^{-4}\int_0^\infty
  h_x(u)e^{-u/2}B(u)\mathfrak r_a(u)du,
 }
\tag{L-91413.14}

where `d_a` is the explicit deterministic Nakamura connection assembled from
`lambda_sigma` and its radial derivative at the three scales.

Subtracting the value at `x=0` cancels both the connection and the compensation
indicator:

\[
\boxed{
\begin{aligned}
 \mathcal A_a(x)-\mathcal A_a(0)
 =2a^{-4}\int_0^\infty
 &(1-\cos(xu))\\
 &\times e^{-u/2}B(u)\mathfrak r_a(u)du.
\end{aligned}}
\tag{L-91413.15}

No prime or zero sum occurs in this identity.

## 5. Positive Lévy increment at the aligned scale

Define

\[
\boxed{
 d\omega_\diamond(u)
 =2a_\diamond^{-4}
  e^{-u/2}B(u)
  \mathfrak r_{a_\diamond}(u)du.
 }
\tag{L-91413.16}

By (L-91413.12), this is a positive measure.  Near zero it has the Lévy
behaviour

\[
 d\omega_\diamond(u)=O(du/u),
\]

so `(1-cos(xu))` makes the integral finite.  At infinity it decays
exponentially because `a_diamond>1/2`.

Equation (L-91413.15) becomes

\[
 \boxed{
 \mathcal A_{a_\diamond}(x)
 -\mathcal A_{a_\diamond}(0)
 =\int_0^\infty
  (1-\cos(xu))d\omega_\diamond(u)
 \ge0.
 }
\tag{L-91413.17}

Thus the complete nonprime recurrence channel is minimized at the zero
carrier.

Its polarized increment kernel has the explicit Lévy Gram

\[
\boxed{
 \mathcal L_\diamond(x,y)
 =\int_0^\infty
  (e^{ixu}-1)(e^{-iyu}-1)d\omega_\diamond(u)
 \succeq0.
 }
\tag{L-91413.18}

The real part of this kernel is the polarization of
`A_(a_diamond)(x)-A_(a_diamond)(0)`.

## 6. All prime residual coefficients have one sign

Since

\[
 \log2>\kappa,
\]

every prime-power atom lies to the right of the common switch.  Therefore

\[
 \mathfrak r_{a_\diamond}(\log n)<0
 \qquad(n\ge2).
\]

Define

\[
\boxed{
 c_n
 =-2a_\diamond^{-4}
  \frac{\Lambda(n)}{\sqrt n}
  \mathfrak r_{a_\diamond}(\log n)>0.
 }
\tag{L-91413.19}

The full scalar coefficient-one recurrence has the exact normal form

\[
\boxed{
 \mathcal R_\diamond(x)
 =\mathcal A_{a_\diamond}(0)
  +\sum_{n\ge2}c_n\cos(x\log n)
  +\int_0^\infty(1-\cos(xu))d\omega_\diamond(u).
 }
\tag{L-91413.20
}

Equivalently,

\[
\boxed{
 \mathcal R_\diamond(x)
 =\mathcal R_\diamond(0)
  +\int(1-\cos(xu))d\omega_\diamond(u)
  -\sum_{n\ge2}c_n(1-\cos(x\log n)).
 }
\tag{L-91413.21}

Every object in this formula is nonnegative except the final explicit prime
sampling decrement.

## 7. The new aligned arithmetic gate

The scalar recurrence at the aligned scale would follow from

\[
\boxed{
 \int_0^\infty
  (1-\cos(xu))d\omega_\diamond(u)
 \ge
 \sum_{n\ge2}c_n(1-\cos(x\log n))
 -\mathcal R_\diamond(0)
 }
\tag{L-91413.22}

for every real `x`.

The fully polarized strengthening is the sampling/Dirichlet-form inequality

\[
\boxed{
 \int_0^\infty
  |F(u)|^2d\omega_\diamond(u)
 \ge
 \sum_{n\ge2}c_n|F(\log n)|^2
 }
\tag{L-91413.23}

on the exact carrier/delay source range, with the finite anchor and connection
coordinates inserted according to `L-91412`.

This is a concrete continuum-versus-prime-log sampling theorem.  It has not
been proved.  It is stronger than the scalar gate and remains RH-bearing once
combined with the corrected form core.

## 8. Numerical diagnostics, not proof

The retained replay records

\[
 \mathcal R_\diamond(0)
 =0.0003991664044248951\ldots>0
\]

and verifies (L-91413.17) at several carriers to more than sixty decimal
places.  This is finite safe-line computation only; no all-carrier positivity
claim is made from it.

## 9. Exact boundary

```text
continuous density one-switch at log plastic          EXACT
Cauchy physical residual has one switch               EXACT
unique residual switch derivative factorization      EXACT
plastic-aligned safe scale                            EXACT
continuous sign mismatch vanishes there               EXACT
nonprime scalar channel is a positive Levy increment EXACT
all prime residual coefficients have one sign         EXACT
aligned full-packet sampling domination               OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
