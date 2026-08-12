# L-91431 — The Brownian endpoint hyperbolic port has a sharp diagonal completion

Claim ID: `L-91431`  
Status: **PROVED EXACT SHARP COMPLETION / QUANTIFIED GREEN TARGET**  
Created: 2026-08-12  
Depends on: `L-91422`, `R-91430`, `L-91302`  
RH status: **unproved**

## 1. The real endpoint form

Retain

\[
 \mathcal H_F(z_1,z_2)
 =\Re(\overline{F(z_1)}F(z_2))
  +\Re(\overline{F(-z_2)}F(-z_1)).
\tag{L-91431.1}
\]

Define its four-point diagonal mass

\[
 \boxed{
 \mathcal D_F(z_1,z_2)
 =|F(z_1)|^2+|F(z_2)|^2
  +|F(-z_1)|^2+|F(-z_2)|^2.
 }
\tag{L-91431.2}
\]

## 2. Exact square completion

The elementary polarization identity gives

\[
\boxed{
\begin{aligned}
 \mathcal H_F+\frac12\mathcal D_F
 ={}&\frac12|F(z_1)+F(z_2)|^2\\
 &+\frac12|F(-z_1)+F(-z_2)|^2
 \ge0.
\end{aligned}}
\tag{L-91431.3}
\]

Equivalently,

\[
 \boxed{
 \mathcal H_F\ge-\frac12\mathcal D_F.
 }
\tag{L-91431.4}
\]

The coefficient `1/2` is sharp: both squares vanish whenever

\[
 F(z_2)=-F(z_1),
 \qquad
 F(-z_1)=-F(-z_2).
\]

The exponential witness in `R-91430` attains this equality.

## 3. Exact cost in the Stein identity

The endpoint term in `L-91422.9` carries the outer factor `1/2`. Therefore

\[
\boxed{
 \frac12\mathbb E[c_{\tau,u}\mathcal H_F]
 \ge
 -\frac14\mathbb E[c_{\tau,u}\mathcal D_F].
}
\tag{L-91431.5}
\]

Thus the **sharp endpoint reserve** required by this route is

\[
 \boxed{
 \mathfrak R_{\rm end}(F)
 =\frac14\mathbb E[c_{\tau,u}\mathcal D_F].
 }
\tag{L-91431.6}
\]

No generic boundary-triple existence statement remains at this joint: the
negative index, its exact diagonal majorant and its coefficient are explicit.

## 4. Completing the Beta–Jacobi cross current

Put

\[
 U=\mathcal D_\beta\mathcal P_u
   =\tau_u(Z_1)-\tau_u(Z_2),
 \qquad
 V=\mathcal D_\beta\mathcal A_F,
\]

and let `W_beta>0` be the conditional carré-du-champ density of
`L-91302/L-91422` on the nondegenerate Beta reservoir. For every `eta>0`,
Young's identity gives pointwise

\[
\boxed{
 \Re(U\overline V)
 \ge-\frac12\left(
   \eta W_\beta|V|^2
  +\eta^{-1}W_\beta^{-1}|U|^2
 \right).
}
\tag{L-91431.7}
\]

Indeed the difference between the right quadratic expression and
`-2 Re(U overline(V))` is

\[
 \left|
  \sqrt{\eta W_\beta}\,V
  +\frac{U}{\sqrt{\eta W_\beta}}
 \right|^2.
\]

Consequently the current term of `L-91422.16` is bounded below by one half of
an explicit native Jacobi energy plus one explicit potential energy.

## 5. A fully quantified sufficient closing theorem

Brownian reflection positivity follows if, for every exponential polynomial
`F`, one proves an identity or domination of the form

\[
\boxed{
 \mathfrak R_\theta(F)
 \ge
 \frac12\mathbb E\left[
  \eta^{-1}W_\beta^{-1}
  |\mathcal D_\beta\mathcal P_u|^2
 \right]
 +\mathfrak R_{\rm end}(F),
}
\tag{L-91431.8}
\]

while the resident positive Beta–Jacobi bulk supplies

\[
 \frac12\eta\mathbb E[
  W_\beta|\mathcal D_\beta\mathcal A_F|^2].
\tag{L-91431.9}
\]

Here `R_theta` is the exact theta boundary/bulk reserve in the normalization of
PR #401. Equations (L-91431.6)--(L-91431.9) state the missing theorem with every
coefficient fixed.

This is a sufficient target, not a proof that the theta reserve dominates it.
The freedom in `eta` may be optimized pointwise or after conditioning on the
Gamma reservoir.

## 6. Correct frontier

```text
endpoint form signature                             EXACT / (2,2)
sharp endpoint diagonal completion                  EXACT
sharp endpoint reserve coefficient                  EXACT / 1/4
Beta current Young completion                       EXACT
theta reserve >= potential + endpoint reserve       OPEN
Brownian reflection / complete Pick positivity      OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVEN
```
