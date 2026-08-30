# L-108401 — Rectangular shared-fibre Hellinger defect tensorizes into two one-sided defects

Claim ID: `L-108401`  
Status: **PROVED EXACT FINITE SOURCE THEOREM**  
Created: 2026-08-31  
Depends on: `L-107300` on PR #774; `L-108400`  
RH/GRH status: **not assumed**

Consider a source-authorized rectangular shared-fibre panel

\[
\Omega=X\times Y,
\qquad
r(i,j)=\bigl(r_R(j),r_L(i)\bigr).
\]

After the authorized history grouping, let

\[
\ell_x=\#r_L^{-1}(x),
\qquad
r_y=\#r_R^{-1}(y).
\]

The cell multiplicities factor exactly:

\[
n_{x,y}=\ell_xr_y.
\tag{L-108401.1}
\]

Put

\[
L=\sum_x\ell_x,\qquad
R=\sum_yr_y,
\]

and let

\[
\bar\ell={L\over|\mathcal S_L|},
\qquad
\bar r={R\over|\mathcal S_R|}.
\]

Define the one-sided Hellinger defects

\[
h_L^2=\sum_x(\sqrt{\ell_x}-\sqrt{\bar\ell})^2,
\qquad
h_R^2=\sum_y(\sqrt{r_y}-\sqrt{\bar r})^2.
\tag{L-108401.2}
\]

The bilateral defect from the uniform rectangular comparator is

\[
H^2
=
\sum_{x,y}
\left(\sqrt{\ell_xr_y}-\sqrt{\bar\ell\bar r}\right)^2.
\]

Then

\[
\boxed{
H^2
=
R h_L^2
+
L h_R^2
-
{1\over2}h_L^2h_R^2.
}
\tag{L-108401.3}
\]

### Proof

The one-sided Hellinger affinities are

\[
\sqrt{\bar\ell}\sum_x\sqrt{\ell_x}
=
L-\frac12h_L^2,
\]

\[
\sqrt{\bar r}\sum_y\sqrt{r_y}
=
R-\frac12h_R^2.
\]

Expanding the bilateral square and multiplying these affinities gives
(L-108401.3).

In particular,

\[
\boxed{
H^2\le Rh_L^2+Lh_R^2.
}
\tag{L-108401.4}
\]

Writing

\[
\eta_L={h_L^2\over L},
\qquad
\eta_R={h_R^2\over R},
\]

one has

\[
{H^2\over LR}
=
\eta_L+\eta_R-\frac12\eta_L\eta_R.
\tag{L-108401.5}
\]

Combining with `L-108400` gives the normalized positive-trace transport

\[
\boxed{
\operatorname{tr}Q(D)_+
\le
\operatorname{tr}Q(\bar D)_+
+
2LR
\sqrt{\eta_L+\eta_R-\frac12\eta_L\eta_R}.
}
\tag{L-108401.6}
\]

Thus the genuinely two-sided physical occupancy problem is reduced to two
one-sided square-root occupancy discrepancies.

## Scope

The theorem does not prove those discrepancies are small for the live native
source. It supplies the exact source geometry required to ask that question
without an artificial two-dimensional family-size loss.
