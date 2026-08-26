# L-106514 — The denominator phase-angle statistic is a sharp majorant, not the all-pass charge

Claim ID: `L-106514`  
Status: **CORRECTED EXACT INEQUALITY; THE PREVIOUS EQUALITY IS REFUTED**  
Created: 2026-08-25  
Corrected: 2026-08-26  
Depends on: `L-106507`, `L-106512`; finite inner Hankel identities  
RH status: **not assumed**

Let \(B_+,B_-\) be finite upper-half-plane inner functions canonically
normalized by

\[
B_+(\infty)=B_-(\infty)=1,
\qquad
U=\frac{B_+}{B_-}=B_+\overline{B_-}
\]

on the compactified real boundary.  Write

\[
B_-(t)=e^{i\beta(t)},
\qquad
\beta'(t)\ge0,
\qquad
\frac1{2\pi}\int_{\mathbb R}\beta'(t)\,dt=m_-.
\]

The earlier version of this claim incorrectly identified one complex
cross-Dirichlet trace with the positive canonical-correlation overlap.  They
are different quantities.

## 1. The two exact cross quantities

Put

\[
\Delta(B_+,B_-)
=
\frac1{2\pi i}\int_{\mathbb R}\frac{B_+'(t)}{B_-(t)}\,dt.
\tag{L-106514.1}
\]

For simple denominator zeros this is

\[
\Delta(B_+,B_-)
=
\sum_{B_-(b)=0}\frac{B_+'(b)}{B_-'(b)},
\]

with the standard confluent residue formula at multiple zeros.  In general
\(\Delta\) is complex.

Let

\[
\mathcal O(B_+,B_-)
=
\operatorname{tr}(P_{K_{B_-}}P_{K_{B_+}})
=
\left\|G_-^{-1/2}CG_+^{-1/2}\right\|_{\mathrm F}^2.
\tag{L-106514.2}
\]

This is real and nonnegative.  The exact adverse all-pass charge remains

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
=
m_- - \mathcal O(B_+,B_-).
}
\tag{L-106514.3}
\]

## 2. Cross-Hankel trace-norm inequality

On the disk, or after the standard conformal unitary from the half-plane, let

\[
H_\pm=H_{\overline{B_\pm}}.
\]

For finite inner functions these are partial isometries with initial
projections \(P_\pm=P_{K_{B_\pm}}\).  Their final spaces are the images of
\(K_{B_\pm}\) under the same fixed boundary reflection
\(f\mapsto \bar z\,\overline f\).  Hence the singular values of
\(H_-^*H_+\) and \(P_-P_+\) are the same principal correlations
\(s_1,\ldots,s_r\).

The Fourier-coefficient trace identity gives

\[
\Delta(B_+,B_-)=\operatorname{tr}(H_-^*H_+)
\]

up to the harmless conjugation convention for the Hilbert-space inner
product.  Since \(H_-^*H_+=P_-(H_-^*H_+)P_+\), cyclicity followed by von
Neumann's trace inequality gives

\[
\begin{aligned}
|\Delta|
&=
\left|\operatorname{tr}\!\left(P_+P_-H_-^*H_+\right)\right|\\
&\le
\sum_{\nu=1}^r s_\nu(P_+P_-)\,
                    s_\nu(H_-^*H_+)\\
&=
\sum_{\nu=1}^r s_\nu^2
=
\mathcal O(B_+,B_-).
\end{aligned}
\tag{L-106514.4}
\]

Thus

\[
\boxed{
\operatorname{Re}\Delta
\le |\Delta|
\le \mathcal O.
}
\tag{L-106514.5}
\]

This is the exact missing inequality in the previous argument.

## 3. Correct oriented phase-angle statement

Since

\[
\beta'=\frac1i\frac{B_-'}{B_-},
\]

integration of the derivative of \(B_+/B_-\) on the compactified boundary
gives the exact complex identity

\[
\frac1{2\pi}\int_{\mathbb R}\beta'(t)U(t)\,dt
=
\Delta(B_+,B_-).
\tag{L-106514.6}
\]

Therefore the positive denominator phase statistic is

\[
\mathcal A_-(U)
=
\frac1{2\pi}\int_{\mathbb R}
\beta'(t)\bigl(1-\operatorname{Re}U(t)\bigr)\,dt
=
m_- - \operatorname{Re}\Delta.
\tag{L-106514.7}
\]

Combining (L-106514.3), (L-106514.5), and (L-106514.7) yields the corrected
sharp majorization

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
\le
\mathcal A_-(U)
=
\frac1{4\pi}\int_{\mathbb R}\beta'(t)|1-U(t)|^2\,dt.
}
\tag{L-106514.8}
\]

The nonnegative overpayment is exactly

\[
\boxed{
\mathcal A_-(U)-\|H_U\|_{\mathcal S_2}^2
=
\mathcal O(B_+,B_-)-\operatorname{Re}\Delta(B_+,B_-).
}
\tag{L-106514.9}
\]

It is a cross-Hankel phase-alignment slack.  It need not vanish even for one
simple pole pair.

## 4. Endpoint Wronskian majorant

For the odd endpoint quotient of `L-106501`,

\[
|1-U_{K,\lambda}|^2
=
\frac{4\lambda^2\mathcal L_K^2}
{(F^2+\lambda^2F'^2)
 ((F^{(K)})^2+\lambda^2(F^{(K+1)})^2)}.
\]

If \(\beta_{K,\lambda}'\) is the phase density of the reduced denominator
inner factor, then

\[
\boxed{
\|H_{U_{K,\lambda}}\|_{\mathcal S_2}^2
\le
\frac{\lambda^2}{\pi}\int_{\mathbb R}
\beta_{K,\lambda}'(t)
\frac{\mathcal L_K(t)^2}
{(F^2+\lambda^2F'^2)
 ((F^{(K)})^2+\lambda^2(F^{(K+1)})^2)}\,dt.
}
\tag{L-106514.10}
\]

Thus the phase-angle estimate remains a valid conclusion-facing sufficient
condition, but it is generally stronger than the exact canonical-correlation
gate.

Applying the same argument to \(U^{-1}\) also corrects the former Dirichlet
identity to

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
+
\|H_{U^{-1}}\|_{\mathcal S_2}^2
\le
\|B_+-B_-\|_{\mathcal D}^2.
}
\tag{L-106514.11}
\]

## 5. Binding one-pole check

Take

\[
B_-(z)=\frac{z-i}{z+i},
\qquad
B_+(z)=\frac{z-1-i}{z-1+i}.
\]

Then

\[
\mathcal O=\frac45,
\qquad
\|H_U\|_{\mathcal S_2}^2=\frac15,
\]

while

\[
\Delta
=
\frac{B_+'(i)}{B_-'(i)}
=
\frac{12}{25}-\frac{16}{25}i
\]

and hence

\[
\mathcal A_-(U)=1-\operatorname{Re}\Delta=\frac{13}{25}.
\]

Therefore the old equality would assert \(1/5=13/25\).  The corrected
inequality \(1/5<13/25\) is strict.

## 6. Scope

```text
canonical defect = m_- - model overlap              PROVED EXACT
complex cross-Dirichlet scalar Delta                 PROVED EXACT
|Delta| <= model overlap                             PROVED EXACT
canonical defect <= denominator phase mean           PROVED EXACT
phase mean = canonical defect                        REFUTED
endpoint phase mean remains a sufficient majorant    PROVED
favorable Xi estimate                                NOT PROVED
```
