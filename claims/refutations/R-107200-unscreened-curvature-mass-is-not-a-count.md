# R-107200 — Unscreened negative-curvature mass is not a scale-free defect count

Claim ID: `R-107200`  
Status: **PROVED EXACT DILATION FIREWALL**  
Created: 2026-08-30  
RH status: **not assumed**

No universal dimensionless inequality of the form

\[
E_I(f)\le C\int_I(Q_f)_-(x)\,dx
\tag{R-107200.1}
\]

can hold for all regular real entire functions and intervals, where
\(E_I(f)\) is the number of simple wrong-sign extrema.

Take one fixture \(f\) with \(E_I(f)>0\), and for \(L>0\) put

\[
f_L(x)=f(x/L),
\qquad
I_L=L I.
\]

The critical-point pattern is carried bijectively from \(I\) to \(I_L\), so

\[
E_{I_L}(f_L)=E_I(f).
\]

On the other hand,

\[
Q_{f_L}(x)=L^{-2}Q_f(x/L),
\]

and therefore

\[
\boxed{
\int_{I_L}(Q_{f_L})_-\,dx
=
L^{-1}
\int_I(Q_f)_-\,dx.
}
\tag{R-107200.2}
\]

Letting \(L\to\infty\) contradicts (R-107200.1).

The Cauchy layer of `L-107200` is scale covariant: under the same dilation,
the screening parameter transforms as \(\varepsilon\mapsto\varepsilon/L\).
The denominator \(r_f^2+\varepsilon^2\) is therefore load-bearing, not a
technical smoothing that may be removed before the Xi estimate.
