# R-99720 — Labelled Littlewood–Paley energy does not automatically control the physical scalar

Claim ID: `R-99720`  
Status: **PROVED EXACT INTERFACE FIREWALL**  
Created: 2026-08-20  
RH status: **unproved**

Let `e_1,...,e_N` be orthonormal labelled source atoms and let the physical collapse map satisfy

\[
\mathcal C e_i=1.
\]

Then

\[
\boxed{\|\mathcal C\|_{\ell^2_N\to\mathbb C}=\sqrt N.}
\]

Indeed,

\[
\mathcal C\left(N^{-1/2}\sum_{i=1}^{N}e_i\right)=\sqrt N.
\]

Hence a polylogarithmic labelled-source square function cannot be pushed through the physical observation by source-blind Cauchy--Schwarz without paying the number of active labels.

A valid conclusion must use arithmetic structure fixed before the sign is observed, such as the first-owner filtration, endpoint localization, the zero-free SHARP box, prime-exchange detailed balance, and a cut/Carleson packing theorem for the live capacities.

This firewall prevents `L-99720/L-99721` from being misreported as a proof of OCE67 or RH.
