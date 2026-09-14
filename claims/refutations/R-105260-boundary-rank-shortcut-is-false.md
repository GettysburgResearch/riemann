# R-105260 — Pole count alone does not bound a vertical boundary matrix

Claim ID: `R-105260`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-24

A tempting shortcut is to say that changing a contour through a strip containing \(m\) poles changes the compressed matrix by rank at most \(m\), and therefore that a vertical boundary integral is automatically low rank. The second assertion is false.

Take the entire scalar \(R(z)=1\), with no poles, and observations

\[
\phi_j(z)=z^j,\qquad 0\le j<d.
\]

On the segment \([0,1]\), the boundary moment matrix is

\[
M_{ij}=\int_0^1x^{i+j}\,dx=\frac1{i+j+1}.
\]

This is the \(d\times d\) Hilbert matrix and is positive definite, hence has full rank \(d\), despite the absence of any pole.

Residue rank controls the difference of complete closed-contour residue forms. It does not by itself control one open vertical or horizontal piece. `EDGEFLUX105260` therefore remains a genuine analytic statement; it cannot be declared \(o(N)\) solely from a boundary-strip zero count.
