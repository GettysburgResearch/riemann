# R-99420 — Generationwise calibration summation is an overcount

Claim ID: `R-99420`
Status: **PROVED EXACT COMPOSITION FIREWALL**
Created: 2026-08-19
RH status: **not assumed**

Let

\[
T=\begin{pmatrix}
0&1/3&0\\
0&0&1/4\\
0&0&0
\end{pmatrix},
\qquad
A=(2,-5,7).
\]

Then \(T^3=0\).  The exact local calibration is the coboundary

\[
C=A-AT.
\]

Therefore

\[
\boxed{
C(I-T)^{-1}=A.
}
\]

If instead one charges \(A\) independently at every generation, the result is

\[
A(I-T)^{-1}\ne A.
\]

Thus the geometric estimate for arbitrary local defects is safe but is not the
native equality-frame accounting.  The exact frame calibrations cancel between
parent and child.

A second firewall is structural.  If target, score, or different rows use
different child matrices \(T_a\), there is no common identity

\[
(A-AT)(I-T)^{-1}=A.
\]

Coordinatewise couplings therefore cannot be substituted for one typed
physical parent.
