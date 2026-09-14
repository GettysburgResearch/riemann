# L-106660 — Phase optimization turns the cross-Hankel trace into a sharp scalar majorant

Claim ID: `L-106660`  
Status: **PROVED EXACT FOR FINITE INNER FUNCTIONS**  
Created: 2026-08-26  
Depends on: corrected `L-106514`  
RH status: **not assumed**

Let \(B_+,B_-\) be finite upper-half-plane inner functions, normalized at
infinity, and let

\[
U=\omega_0B_+\overline{B_-},
\qquad |\omega_0|=1.
\]

Write

\[
B_-(t)=e^{i\beta(t)},
\qquad
\beta'(t)\ge0,
\qquad
m_-=\frac1{2\pi}\int_{\mathbb R}\beta'(t)\,dt.
\]

Let

\[
\mathcal O
=
\operatorname{tr}(P_{K_{B_-}}P_{K_{B_+}})
\]

be the positive canonical overlap and define the physical complex cross trace

\[
\boxed{
\Delta_U
=
\frac1{2\pi}\int_{\mathbb R}\beta'(t)U(t)\,dt.
}
\tag{L-106660.1}
\]

Absorbing \(\omega_0\) into the cross-Hankel trace, corrected `L-106514` gives

\[
\boxed{
|\Delta_U|\le\mathcal O.
}
\tag{L-106660.2}
\]

The exact adverse canonical charge is

\[
\boxed{
\mathcal C(U)
=
\|H_U\|_{\mathcal S_2}^2
=
m_- -\mathcal O.
}
\tag{L-106660.3}
\]

## 1. Exact phase minimization

For every constant phase \(\theta\in\mathbb R\), put

\[
\mathcal A_\theta(U)
=
\frac1{4\pi}\int_{\mathbb R}
\beta'(t)|1-e^{i\theta}U(t)|^2\,dt.
\]

Expanding the square and using (L-106660.1) gives

\[
\boxed{
\mathcal A_\theta(U)
=
m_- -\operatorname{Re}(e^{i\theta}\Delta_U).
}
\tag{L-106660.4}
\]

Therefore

\[
\boxed{
\min_{\theta\in\mathbb R}\mathcal A_\theta(U)
=
m_- -|\Delta_U|.
}
\tag{L-106660.5}
\]

Combining (L-106660.2)--(L-106660.5) gives the optimized scalar majorant

\[
\boxed{
\mathcal C(U)
\le
m_- -|\Delta_U|
=
\min_{\theta\in\mathbb R}
\frac1{4\pi}\int_{\mathbb R}
\beta'(t)|1-e^{i\theta}U(t)|^2\,dt.
}
\tag{L-106660.6}
\]

Its exact overpayment is

\[
\boxed{
m_- -|\Delta_U|-\mathcal C(U)
=
\mathcal O-|\Delta_U|
\ge0.
}
\tag{L-106660.7}
\]

Thus the old unrotated phase mean can always be improved without altering the
all-pass quotient, its winding, or its Hankel charge. The minimizing phase is
one constant per regular window; no pointwise phase choice is permitted.

## 2. Equality and phase dispersion

For one principal channel, the trace-norm inequality is saturated, so

\[
|\Delta_U|=\mathcal O
\]

and (L-106660.6) is exact. More generally, equality holds precisely when the
active cross-Hankel channels saturate the trace inequality with a common
phase. The slack \(\mathcal O-|\Delta_U|\) is therefore a scalar measure of
principal-channel phase dispersion.

Several channels can cancel in \(\Delta_U\) while retaining positive overlap.
Consequently the optimized scalar is a majorant, not a replacement for the
canonical defect. `R-106660` records both the exact one-pole calibration and
a two-channel strictness fixture.

## 3. Carrier-free fifth-endpoint specialization

For the mesoscopic Riemann--Siegel packet of `L-106620--L-106612`,

\[
U_{5,j}=\frac{R_{0,j}C_{5,j}}{C_{0,j}R_{5,j}}.
\]

Reduce common factors and split the denominator inner factor by height,

\[
B_{-,j}=B_{-,j}^{\rm sh}B_{-,j}^{\rm deep}.
\]

The shallow canonical charge uses the complete numerator factor but only the
shallow denominator factor. Define its derived all-pass symbol

\[
U_{5,j}^{\rm sh}
=
\omega_{0,j}B_{+,j}\overline{B_{-,j}^{\rm sh}},
\]

where the harmless constant is chosen consistently with the reduced packet.
Let \(m_{-,j}^{\rm sh}=\deg B_{-,j}^{\rm sh}\), let
\(\beta_{-,j}^{\rm sh\,\prime}\) be its phase density, and put

\[
\Delta_j^{\rm sh}
=
\frac1{2\pi}\int
\beta_{-,j}^{\rm sh\,\prime}(t)U_{5,j}^{\rm sh}(t)\,dt.
\]

Then

\[
\boxed{
\mathcal C_j^{\rm sh}
\le
m_{-,j}^{\rm sh}-|\Delta_j^{\rm sh}|.
}
\tag{L-106660.8}
\]

The full packet determines every factor in this expression. The shallow
symbol is not obtained by simply retaining the deep co-analytic factor: that
factor has already been paid separately by the height ledger. Unlike the
unrotated complete-Wronskian formula, the minimizing phase generally replaces
a numerator difference \(D-N\) by \(D-e^{i\theta}N\); the common Xi amplitude
remains absent after inner-factor reduction.

## Scope

The lemma proves no favorable Xi lower bound for \(|\Delta_j|\). It replaces a
matrix overlap by one stronger scalar target and corrects the stale equality
in the earlier `L-106611`. The remaining scalar estimate is conclusion-bearing.
