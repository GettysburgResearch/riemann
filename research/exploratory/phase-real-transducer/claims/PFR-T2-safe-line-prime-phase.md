# PFR-T2 — Safe-line centered-Xi phase is a real prime cosine field

Status: **PROVED EXACT ANALYTIC IDENTITY**
RH status: **unproved**

Let

\[
\mathcal X(z)=\xi(1/2+iz),
\qquad
\mathcal V_y(x)=-\partial_x\arg\mathcal X(x+iy).
\]

For `y>1/2` and `s=1/2+y+ix`,

\[
\mathcal V_y(x)=\Re{\xi'\over\xi}(s)
\]

and

\[
\mathcal V_y(x)
=\Re\left[{1\over s}+{1\over s-1}-{1\over2}\log\pi
+{1\over2}\psi(s/2)\right]
-\sum_{n\ge2}{\Lambda(n)\over n^{1/2+y}}\cos(x\log n).
\]

The series converges absolutely.  The identity uses only the functional
equation, conjugation, the completed logarithmic derivative, and the ordinary
Dirichlet series for `zeta'/zeta` in `Re(s)>1`.

This does not replace the xi-passivity criterion of Issue #39.  It identifies
the critical-strip flower phase with a safe real prime signal.
