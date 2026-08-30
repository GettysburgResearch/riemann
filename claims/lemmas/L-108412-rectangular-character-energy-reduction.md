# L-108412 — Rectangular occupancy debt is two one-sided character energies

Claim ID: `L-108412`  
Status: **PROVED EXACT FINITE SOURCE THEOREM**  
Created: 2026-08-31  
Depends on: `L-108401`, `L-108410`  
RH/GRH status: **not assumed**

Let `l_x>=0` on a finite left residue group `X` and `r_y>=0` on a finite
right residue group `Y`. Put

\[
L=\sum_x l_x,
\qquad
R=\sum_y r_y,
\qquad
n_{x,y}=l_xr_y.
\]

Let `h_L^2`, `h_R^2` be the one-sided Hellinger debts from the respective
uniform or orbitwise-uniform comparators, and put

\[
\eta_L={h_L^2\over L},
\qquad
\eta_R={h_R^2\over R}.
\]

`L-108401` gives the exact bilateral identity

\[
\boxed{
{H_{X\times Y}(n)^2\over LR}
=
\eta_L+\eta_R-{1\over2}\eta_L\eta_R.
}
\tag{L-108412.1}
\]

Define the one-sided nonprincipal character energies

\[
\mathcal V_L
={1\over L^2}
\sum_{\chi\ne1}|\widehat l(\chi)|^2,
\qquad
\mathcal V_R
={1\over R^2}
\sum_{\psi\ne1}|\widehat r(\psi)|^2.
\tag{L-108412.2}
\]

By `L-108410`,

\[
\eta_L\le\mathcal V_L,
\qquad
\eta_R\le\mathcal V_R.
\]

Consequently

\[
\boxed{
{H_{X\times Y}(n)^2\over LR}
\le
\mathcal V_L+\mathcal V_R.
}
\tag{L-108412.3}
\]

Combining with the positive-trace stability theorem `L-108400`, the live
rectangular positive trace differs from its symmetric comparator by at most

\[
\boxed{
2LR\sqrt{\mathcal V_L+\mathcal V_R}.
}
\tag{L-108412.4}
\]

Thus the bilateral physical restriction problem has become two one-sided
character-variance estimates. There is no two-dimensional occupancy rank or
atom-multiplicity tax.

## Global sufficient ledger

For grouped live fibres `iota`, define

\[
\mathfrak V_{\rm rect}(X)
=
2\sum_\iota
N_\iota
\sqrt{\mathcal V_{L,\iota}+\mathcal V_{R,\iota}}.
\tag{L-108412.5}
\]

After adding the live-mask total-variation payment from `L-108410.6`, a
subpower bound for (L-108412.5) implies `FROBHELL108400`.

PR #771 diagonalizes the complete squareclass pushforward and identifies the
explicit quadratic resonance set. Hence every term in (L-108412.2) is now a
source-typed multiplicative-character coefficient. The number-field estimate
remains open.
