# L-106611 — The fifth-endpoint quotient is a carrier-free arithmetic cross-ratio

Claim ID: `L-106611`  
Status: **CORRECTED EXACT ALGEBRA + CANONICAL/PHASE MAJORANTS ON REGULAR WINDOWS**  
Created: 2026-08-26  
Corrected: 2026-08-26  
Depends on: `L-106610`, corrected `L-106514`, `L-106660`, `T-106600`  
RH status: **not assumed**

Retain the notation of `L-106610` and use the explicit scale

\[
a_{\rm RS}=\omega^{-1}.
\]

## 1. Exact cross-ratio

The adaptive fifth-endpoint quotient is

\[
U_{5,a_{\rm RS}}
=
\frac{
(\Xi-i a_{\rm RS}\Xi')
(\Xi^{(5)}+i a_{\rm RS}\Xi^{(6)})
}{
(\Xi+i a_{\rm RS}\Xi')
(\Xi^{(5)}-i a_{\rm RS}\Xi^{(6)})
}.
\]

Substitution of (L-106610.4)--(L-106610.5) cancels every factor
\(Ae^{i\vartheta}\) and gives

\[
\boxed{
U_{5,a_{\rm RS}}
=
\frac{R_0C_5}{C_0R_5}.
}
\tag{L-106611.1}
\]

Thus the endpoint quotient is an arithmetic cross-ratio of four finite
zeta-derivative packets.

## 2. The amplitude connection cancels from the numerator

Directly,

\[
\begin{aligned}
R_0C_5-C_0R_5
&=2(H_0C_5-C_0H_5)\\
&=\frac{2i}{\omega}
\left[
H_0(D+q)H_5-(D+q)H_0\,H_5
\right].
\end{aligned}
\]

The two \(q\)-terms cancel. Since \(H_0=h\),

\[
\boxed{
R_0C_5-C_0R_5
=
\frac{2i}{\omega}
\left(
h\,DH_5-(Dh)H_5
\right).
}
\tag{L-106611.2}
\]

The complete Xi amplitude \(A\), its logarithmic derivative \(q\), and the
common Riemann--Siegel carrier are absent from the conclusion-facing
Wronskian.

Consequently,

\[
\boxed{
|1-U_{5,a_{\rm RS}}|^2
=
\frac{4}{\omega^2}
\frac{
|h\,DH_5-(Dh)H_5|^2
}{
|C_0R_5|^2
}.
}
\tag{L-106611.3}
\]

## 3. Correct canonical charge and optimized phase majorants

On a finite regular window, reduce common factors and write

\[
U_{5,a_{\rm RS}}=\omega_0B_+\overline{B_-}
\]

on the compactified real boundary. Let \(m_-=\deg B_-\), let
\(\beta_-'\ge0\) be the boundary phase density of \(B_-\), and let

\[
\mathcal O
=
\operatorname{tr}(P_{K_{B_-}}P_{K_{B_+}}).
\]

The exact adverse charge is the canonical-correlation defect

\[
\boxed{
\mathcal C_{5,\rm RS}
=
\|H_{U_{5,a_{\rm RS}}}\|_{\mathcal S_2}^2
=
m_- -\mathcal O.
}
\tag{L-106611.4}
\]

Define the complex cross trace directly from the physical quotient by

\[
\Delta_{5,\rm RS}
=
\frac1{2\pi}\int_{\mathbb R}
\beta_-'(t)U_{5,a_{\rm RS}}(t)\,dt.
\]

The corrected cross-Hankel inequality of `L-106514` and the phase optimization
of `L-106660` give

\[
\boxed{
\mathcal C_{5,\rm RS}
\le
m_- -|\Delta_{5,\rm RS}|
=
\min_{\theta\in\mathbb R}
\frac1{4\pi}\int_{\mathbb R}
\beta_-'(t)
|1-e^{i\theta}U_{5,a_{\rm RS}}(t)|^2\,dt.
}
\tag{L-106611.5}
\]

Taking the unrotated phase and using (L-106611.3) yields the fully explicit
Wronskian majorant

\[
\boxed{
\mathcal C_{5,\rm RS}
\le
\frac1{\pi}\int_{\mathbb R}
\beta_-'(t)
\frac{
|h\,DH_5-(Dh)H_5|^2
}{
\omega(t)^2|C_0R_5|^2
}\,dt.
}
\tag{L-106611.6}
\]

The earlier version of this file incorrectly wrote equality in
(L-106611.6). `L-106514` and `R-106640` prove that the phase mean can strictly
overpay the canonical charge. The optimized scalar in (L-106611.5) is sharper
and is exact for one principal channel, but it can also remain strict in
several channels.

## 4. Symmetric semiclassical normalization

Put

\[
\widetilde H_5=(i\omega)^{-5}H_5,
\qquad
q_5=q+5\frac{\omega'}{\omega}.
\]

Then

\[
\boxed{
C_5
=
(i\omega)^5
\frac{i}{\omega}(D+q_5)\widetilde H_5,
}
\tag{L-106611.7}
\]

\[
\boxed{
R_5
=
(i\omega)^5
\left[
2\widetilde H_5
-
\frac{i}{\omega}(D+q_5)\widetilde H_5
\right].
}
\tag{L-106611.8}
\]

The common factor \((i\omega)^5\) cancels from (L-106611.1). Both endpoints
therefore have the same exact Levinson form: a slowly varying real connection
and one carrier-cancelled derivative packet.

## 5. Scope

Equations (L-106611.5)--(L-106611.6) do not bound either positive
phase-weighted mean. The denominator phase density is still
conclusion-bearing and may concentrate. The theorem removes the carrier and
amplitude ambiguity and now retains the exact canonical/majorant distinction;
it does not supply the required Xi arithmetic estimate.
