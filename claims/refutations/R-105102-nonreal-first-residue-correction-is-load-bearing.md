# R-105102 — The nonreal first-residue correction is load bearing

Claim ID: R-105102

Status: **PROPOSED EXACT CARRIER FIREWALL; review pending**

Created: 2026-08-23

Depends on: L-105102

RH status: **unproved**

Let

\[
p(x)=x^5-x^3+x.
\]

Its derivative has no real zero because, with \(y=x^2\),

\[
p'(x)=5x^4-3x^2+1
=5\left(y-\frac3{10}\right)^2+\frac{11}{20}>0.
\tag{R-105102.1}
\]

Hence

\[
R_p=0,
\qquad
\mathcal M_{1,p}=0.
\tag{R-105102.2}
\]

The four critical points are simple: as a polynomial in \(y\),
\(5y^2-3y+1\) has discriminant \(-11\) and nonzero constant term. They are
also not zeros of \(p\). Indeed, a common nonzero root would make
\(y^2-y+1=0\) and \(5y^2-3y+1=0\); subtracting five times the first equation
forces \(y=2\), which fails the first equation.

The polynomial is centered and its root variance is \(V_2=2\). On an outer
regular contour, the exact first-residue charge is therefore

\[
\Phi_{1,p}=-\frac{V_2}{5^2}=-\frac2{25}.
\tag{R-105102.3}
\]

Every critical point is nonreal, so

\[
C_{1,p}=\Phi_{1,p}=-\frac2{25}.
\tag{R-105102.4}
\]

L-105102 gives the correct cancellation:

\[
\mathcal M_{1,p}=-\Phi_{1,p}+C_{1,p}=0.
\tag{R-105102.5}
\]

Dropping the nonreal correction would instead manufacture the false positive
carrier

\[
-\Phi_{1,p}=\frac2{25}>0
\]

despite the absence of even one real critical point. Boundary or complete-root
first-residue information alone therefore does not prove a real
residue-coherence carrier.
