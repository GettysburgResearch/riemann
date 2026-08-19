# R-99250 — A raw endpoint cutoff is not the SHARP-kernel child measure

Claim ID: `R-99250`  
Status: **PROVED EXACT INTERFACE SEPARATOR; REPAIRED BY `L-99250`**  
Created: 2026-08-19  
Targets: an overly literal reading of the child-restriction sentence in PR #642

For

\[
dM_Y(t)=\mathbf1_{t\le Y}T(Y/t)\kappa_j(t)\frac{dt}{t},
\]

a raw cutoff to `t<=Z` has density `T(Y/t)kappa_j(t)`, whereas the true child
has density `T(Z/t)kappa_j(t)`.

At `Y=16`, `Z=4`, `t=4`, these densities are respectively

\[
5\kappa_j(4)
\quad\hbox{and}\quad
\kappa_j(4).
\]

Therefore

\[
\mathbf1_{t\le Z}M_Y\ne M_Z.
\]

The exact repair is the Radon–Nikodym derivative

\[
R_{Z\mid Y}(t)
=\mathbf1_{t\le Z}\frac{T(Z/t)}{T(Y/t)},
\qquad
M_Z=R_{Z\mid Y}M_Y.
\]

This correction does not refute the positive kernel or the full-row Fubini
identity of PR #642. It replaces one ambiguous source-interface sentence by a
literal one-parent construction and is used in `L-99250`.
