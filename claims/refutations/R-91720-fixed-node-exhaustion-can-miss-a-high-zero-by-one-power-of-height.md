# R-91720 — A fixed-node exhaustion rate can miss a high zero by one full power of height

Refutation ID: `R-91720`  
Status: **EXACT RATE FIREWALL**  
Created: 2026-08-13  
Depends on: `L-91720`  
RH status: **unproved**

At any fixed node `eta`, a zero of fixed depth `x>0` and height `Y` contributes

\[
g_\eta(x+iY)
=
\frac{4\eta x}{Y^2}
+O_{\eta,x}(Y^{-4}).
\]

Therefore a fixed-node error estimate of size `O(1/Y)` is compatible with an
off-line zero at height `Y`; it is too large by one power.

The moving choice

\[
\eta\asymp Y
\]

changes the charge to

\[
g_\eta(x+iY)\asymp\frac{x}{Y}.
\]

Hence the node motion in `L-91720` is not cosmetic. It is required to make an
`o(1/Y)` cofinal arithmetic error conclusion-producing.

This refutation does not say that a fixed node is useless under exact
exhaustion. It isolates the rate loss in approximate schemes.
