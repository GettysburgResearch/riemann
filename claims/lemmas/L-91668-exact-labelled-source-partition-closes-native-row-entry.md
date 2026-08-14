# L-91668 — Rejected root normalization; superseded by the single-SHARP theorem

Claim ID: `L-91668`  
Status: **REJECTED — EXACT FACTOR-THREE NORMALIZATION ERROR**  
Reviewed failure: PR #457 at `e136fcf42fbab1195fc193e64ce4039d1a1d416c`  
Superseded by: `R-91659`, `L-91670`, `L-91671`, `T-91656`  
RH status: **unproved**

The historical theorem used

\[
w_\Psi=(1+\kappa_*)w_{a_*}+(2-\kappa_*)w_1
\]

and the separately normalized row profiles

\[
\mathcal Q_{j,a}(Y)=\frac{Q_Y(j)}{a\sqrt Y-1}.
\]

Each channel contributes its displayed positive coefficient times
`Q_Y(j)/sqrt(n)`. Since

\[
(1+\kappa_*)+(2-\kappa_*)=3,
\]

the cited observation is `3c_X`, not `c_X`. Equations formerly labelled
`L-91668.10--11` are false.

The source-ownership combinatorics in the historical file may still be useful,
but this file is not a valid native-row theorem and must not appear in a
conclusion-producing dependency graph.

The normative replacement uses

\[
w_\Psi=3w_{4/3},
\qquad
\mathcal H_{\Psi,j}(Y)=\frac{Q_Y(j)}{4\sqrt Y-3},
\]

so one source atom produces exactly one native row atom. See `L-91670`.
