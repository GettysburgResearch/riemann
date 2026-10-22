# R-105101 — The global root ledger is not a height-local moment

Claim ID: R-105101

Status: **PROPOSED EXACT LOCALIZATION FIREWALL; review pending**

Created: 2026-08-23

Depends on: L-105100 and L-105101

RH status: **unproved**

Let

\[
p(x)=x^3-3x+1.
\]

The critical points are \(-1,1\), with

\[
\rho_{-1}=-\frac12,
\qquad
\rho_1=-\frac16.
\]

The only zero of \(p''\) is zero, with

\[
\tau_0=-\frac1{18}.
\]

The global L-105100 ledger is

\[
\mathcal K_4(p)
=\rho_{-1}^2+\rho_1^2+\tau_0
=\frac29.
\tag{R-105101.1}
\]

Now take \(T=1/2\) and any regular \(\eta\). There is no real critical point in
\((-T,T)\), so

\[
M_{2,p}(1/2)=0.
\]

The local boundary residue is not the global root ledger:

\[
B_p(1/2,\eta)=\tau_0=-\frac1{18}.
\tag{R-105101.2}
\]

The omitted exterior residue is load bearing:

\[
\mathcal K_4(p)-B_p(1/2,\eta)
=\rho_{-1}^2+\rho_1^2
=\frac5{18}.
\tag{R-105101.3}
\]

L-105101 correctly recovers

\[
M_{2,p}(1/2)
=B_p(1/2,\eta)-D_p(1/2,\eta)
=0.
\]

Therefore the inference

    global centered V2/V4 ledger
      -> height-truncated real critical-residue M2

is false without the exterior or boundary-flux ledger. The gap persists even
for a cubic whose entire critical ladder is real and simple.
