# R-105327 — Variance and centered flux are useful sufficient coordinates, not the sharp last-defect gates

Claim ID: `R-105327`  
Status: **BINDING INTEGRATION FIREWALL**  
Created: 2026-08-23  
Depends on: parent `R-105202--R-105203`, `L-105213--L-105218`; `L-105323--L-105325`  
RH status: **unproved**

## 1. Residue variance is not necessary for real-rootedness

`L-105323` proves, at a real-rooted finite level,

\[
\mathfrak C={1\over1+\operatorname{Var}(\alpha)}.
\]

This is an exact and useful coordinate. It is not the sharp sign condition.
The parent branch gives the exact real-rooted polynomial

\[
p(x)=x^5/5-7x^3-10x^2+8/5
\]

for which every critical residue is negative but

\[
R(1-\mathfrak C)>2.
\]

Thus any theorem demanding subunit cumulative normalized residue variance is
an optional strong sufficient theorem. It is not necessary even for elementary
complete real-rootedness and must not replace

\[
\boxed{\rho_c\le0\quad\text{at every real critical point}.}
\]

The sharp residue gate is `PRES105220`.

## 2. One centered winding moment is not all-packet Loewner positivity

`L-105325` compresses the zeroth and second root-moment leakage into one exact
centered contour scalar

\[
\Gamma_2
={1\over2\pi i}\int_{\partial\Omega}
(z^2-\lambda_F){(F'/F)'\over F'/F}\,dz.
\]

This is a genuine boundary coordinate and can support quantitative estimates.
It is not equivalent to positive semidefiniteness of the boundary Cauchy
Loewner kernel on every finite packet.

The parent four-point separator has all principal packets of size at most three
positive while its full fourth eigenvalue is negative. Therefore finitely many
scalar moments or bounded packet tests do not bootstrap abstractly to
all-packet positivity.

The sharp boundary gate remains `BRP105220`.

## 3. Exact complementary-block theorem

The parent Schur-complement identity gives, on every packet containing the real
critical nodes,

\[
\boxed{
\operatorname{ind}_-(\mathbb B_F)
=
\#\{c:\rho_c>0\}
+
\operatorname{ind}_-(\mathscr R_{F,\Omega}).
}
\]

There is no cancellation between the residue and boundary defects. Therefore:

- a small residue variance cannot repair one positive residue;
- a favorable centered weighted flux cannot repair one negative boundary
  square;
- high-tail coherence does not imply low-order `PRES`;
- one scalar boundary estimate does not imply low-order `BRP`.

## 4. Correct role of the `105320` coordinates

The new coordinates remain useful in four precise ways.

1. `L-105320` interprets negative residues, when present in the real-rooted
   cone, as spectral weights of the physical root-coupling vector.
2. `L-105323` proves that the complete first residue carrier is conserved up to
   an explicit degree factor; variance is the sole loss in the coherence API.
3. `L-105325` identifies a centered weighted moment of the same boundary
   current that appears in the Levinson/Loewner gate.
4. `L-105321--L-105322`, if their hostile analytic review succeeds, give a
   large terminal region where the residue pivots are uniformly negative.

These are producer coordinates and asymptotic controls for the sharp gates,
not replacements for them.

## 5. Normative conclusion graph

The conclusion-facing graph on this PR is therefore

\[
\boxed{
\mathrm{PRES105220}
\wedge
\mathrm{BRP105220}
\Longrightarrow
\mathrm{RH}.
}
\]

The variance-production statement `RVP105323` and centered weighted-flux
statement `CWLF105325` remain optional sufficient subprogrammes only after an
explicit implication to the corresponding sharp gate is proved. No such full
implication is claimed here.

```text
pointwise residue sign PRES105220             OPEN / SHARP
all-packet boundary Loewner PSD BRP105220      OPEN / SHARP
normalized residue variance                    EXACT COORDINATE / OVERSTRONG AS GATE
centered weighted winding flux                 EXACT COORDINATE / SCALAR ONLY
Riemann Hypothesis                             UNPROVEN
```
