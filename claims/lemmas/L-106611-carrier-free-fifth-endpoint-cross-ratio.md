# L-106611 — The fifth-endpoint quotient is a carrier-free arithmetic cross-ratio

Claim ID: `L-106611`  
Status: **PROVED EXACT ALGEBRAICALLY ON REGULAR WINDOWS**  
Created: 2026-08-26  
Depends on: `L-106610`, `L-106514`, `T-106600`  
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
common Riemann–Siegel carrier are absent from the conclusion-facing
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

## 3. Exact oriented phase-angle mean

On a finite regular window, reduce common factors and write the quotient as

\[
U_{5,a_{\rm RS}}=\omega_0 B_+\overline{B_-}.
\]

Let \(\beta_-'\ge0\) be the boundary phase density of \(B_-\). The exact
oriented charge identity of `L-106514` becomes

\[
\boxed{
\|H_{U_{5,a_{\rm RS}}}\|_{\mathcal S_2}^2
=
\frac1{\pi}
\int_{\mathbb R}
\beta_-'(t)
\frac{
|h\,DH_5-(Dh)H_5|^2
}{
\omega(t)^2|C_0R_5|^2
}\,dt .
}
\tag{L-106611.4}
\]

This is the same adverse topological charge as before, but its boundary angle
is now a literal arithmetic Wronskian.

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
\tag{L-106611.5}
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
\tag{L-106611.6}
\]

The common factor \((i\omega)^5\) cancels from (L-106611.1). Both endpoints
therefore have the same exact Levinson form: a slowly varying real connection
and one carrier-cancelled derivative packet.

## 5. Scope

Equation (L-106611.4) does not bound the positive phase-weighted mean.
The denominator phase density is still conclusion-bearing and may
concentrate. The theorem removes the carrier and amplitude ambiguity; it does
not replace the required arithmetic mean-value estimate.
