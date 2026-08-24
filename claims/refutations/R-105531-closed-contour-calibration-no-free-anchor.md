# R-105531 — A holomorphic calibration cannot create a pole-count anchor

Claim ID: `R-105531`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-24

Let `Omega` be a regular closed contour and let `phi_i,phi_j` be holomorphic
inside it.  For every constant scalar `c`,

\[
\boxed{
\frac1{2\pi i}\int_{\partial\Omega}
 c\,\phi_i(z)\phi_j(z)\,dz=0.
}
\]

Thus an identity carrier which appears positive on one horizontal boundary
must cancel against the reflected horizontal boundary, vertical sides, or a
strip partial-index term unless the meromorphic Xi quotient itself supplies a
pole.  No source filter bank, outer factor, or endpoint taper may promote a
purely holomorphic constant carrier to a positive Pick matrix.

This firewall explains why `L-105530` closes the **local Hermitian source
algebra** but does not by itself prove `BANKREAL105530`.  The remaining signed
strip/companion flux is topological and conclusion-bearing, not a disposable
technical error.
