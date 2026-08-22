# L-104502 — Exact Riccati–Pick dictionary for the derivative ladder

Claim ID: `L-104502`  
Status: **PROVED EXACT**  
Created: 2026-08-22  
RH status: **not assumed**

Let

\[
F_k=F^{(k)}
\]

for a real entire function `F`, and define the negative logarithmic derivative

\[
\boxed{
h_k(z)=-{F_{k+1}(z)\over F_k(z)}.
}
\tag{L-104502.1}
\]

## 1. Laguerre defect is the Riccati derivative

The Laguerre defect

\[
\mathcal L_k
=F_{k+1}^2-F_kF_{k+2}
\]

satisfies

\[
\boxed{
\mathcal L_k(z)=F_k(z)^2h_k'(z).
}
\tag{L-104502.2}
\]

At a real simple zero `c` of `F_(k+1)` which is not a zero of `F_k`,

\[
h_k(c)=0,
\qquad
h_k'(c)=-{F_{k+2}(c)\over F_k(c)}.
\]

Therefore

\[
\boxed{
F_k(c)F_{k+2}(c)>0
\iff
h_k'(c)<0
\iff
\mathcal L_k(c)<0.
}
\tag{L-104502.3}
\]

Wrong extrema are exactly negative-slope real zeros of `h_k`.

## 2. Positive-residue form

Let

\[
Q_k(z)={F_k(z)\over F_{k+1}(z)}.
\]

At a simple zero `c` of `F_(k+1)`,

\[
\boxed{
\operatorname*{Res}_{z=c}Q_k(z)
={F_k(c)\over F_{k+2}(c)}.
}
\tag{L-104502.4}
\]

Hence a critical point is wrong exactly when this real residue is positive.
The factor-two conservation law of `L-104500` may therefore be read as an
exact count of positive derivative-ratio residues.

## 3. Exact Riccati recursion

The derivative ladder obeys

\[
\boxed{
h_{k+1}=h_k-{h_k'\over h_k}.
}
\tag{L-104502.5}
\]

Indeed,

\[
h_k-{h_k'\over h_k}
=-{F_{k+1}\over F_k}
 -{(F_{k+1}^2-F_kF_{k+2})/F_k^2
    \over -F_{k+1}/F_k}
=-{F_{k+2}\over F_{k+1}}.
\]

Thus downward reverse-Rolle transport is the inverse problem for one explicit
nonlinear Riccati map.  It is not an unspecified comparison between two zero
percentages.

## 4. Pick-kernel interpretation

Define the Pick kernel

\[
\boxed{
K_k(z,w)
={h_k(z)-\overline{h_k(w)}\over z-\overline w}.
}
\tag{L-104502.6}
\]

At a real regular point,

\[
K_k(c,c)=h_k'(c).
\]

Therefore every wrong extremum is a negative diagonal node of the confluent
Pick kernel.  If `h_k` is a Pick/Herglotz function, then `K_k` is positive
semidefinite and no wrong extremum occurs.

For a real-rooted polynomial or a suitable Laguerre–Pólya entire function,

\[
h_k(z)=-\sum_\rho {m_\rho\over z-\rho}
\]

is Pick in the upper half-plane, recovering the classical forward Rolle
mechanism.

## Scope firewall

Nonnegativity of finitely many diagonal values is not full Pick positivity, and
Pick positivity of a different safe-line function is not automatically
positivity of the derivative-ratio kernel (L-104502.6).

In particular, the repository's actual-Xi order-three Pick theorem is a useful
local precedent, but it does not by itself prove any all-derivative statement
for `h_k`.  The first new operator object required by the reverse-Rolle
programme is the source-locked kernel (L-104502.6) at the actual critical
points of the derivative ladder.
