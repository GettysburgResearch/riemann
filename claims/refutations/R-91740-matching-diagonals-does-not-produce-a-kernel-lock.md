# R-91740 — Matching diagonals does not produce a kernel lock

Refutation ID: `R-91740`  
Status: **EXACT POLARIZATION FIREWALL**  
Created: 2026-08-13  
Depends on: `L-91740`  
RH status: **unproved**

Consider

\[
A=
\begin{pmatrix}
1&\rho\\
\rho&1
\end{pmatrix},
\qquad
C=
\begin{pmatrix}
1&-\rho\\
-\rho&1
\end{pmatrix},
\qquad 0<\rho<1.
\]

Both are positive semidefinite and have identical diagonals. But

\[
A-C=
\begin{pmatrix}
0&2\rho\\
2\rho&0
\end{pmatrix}
\]

has eigenvalues `+2rho` and `-2rho`.

Thus equality of every tested scalar diagonal, trace, or one-node norm does
not imply a positive kernel defect. The full polarized source/model kernel
must be compared before invoking the lurking-isometry theorem.

The moving-node scalar criterion is legal only after a canonical full-kernel
source lock has identified its scalar residual with the hyperbolic/auxiliary
output.
