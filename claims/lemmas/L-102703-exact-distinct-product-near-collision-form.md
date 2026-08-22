# L-102703 — Exact distinct-product near-collision form

Claim ID: `L-102703`  
Status: **PROVED EXACT REDUCTION; OFF-DIAGONAL ESTIMATE OPEN**  
Created: 2026-08-22  
Depends on: `L-102702`; PR #715 common mother  
RH status: **unproved**

Write

\[
\phi(u)=\Phi_*(e^u)
\]

and define its autocorrelation

\[
R_\Phi(h)
=
\int_{\mathbb R}\phi(u)\phi(u+h)\,du.
\]

Since \(\operatorname{supp}\phi\subset[0,\log16]\),

\[
\boxed{R_\Phi(h)=0\qquad(|h|\ge\log16).}
\tag{L-102703.1}
\]

For

\[
H_{\rm def}(e^u)
=
\sum_n\frac{\delta(n)}{\sqrt n}\phi(u-\log n),
\]

finite Fubini gives

\[
\boxed{
\|H_{\rm def}\|_{L^2(du)}^2
=
\sum_{n,m}
\frac{\delta(n)\overline{\delta(m)}}{\sqrt{nm}}
R_\Phi(\log(n/m)).
}
\tag{L-102703.2}
\]

The diagonal \(n=m\) is \(Y^{o(1)}\) on every horizon by `L-102702`.
All pairs with \(n/m\notin[1/16,16]\) vanish exactly.

Therefore the only unproved term is

\[
\boxed{
\mathcal N_\Phi(Y)
=
\sum_{\substack{n\ne m\\n,m\le16Y\\1/16<n/m<16}}
\frac{\delta(n)\overline{\delta(m)}}{\sqrt{nm}}
R_\Phi(\log(n/m)).
}
\tag{L-102703.3}
\]

Define

```text
HDNC102703:
  the positive part of the physical off-diagonal energy N_Phi(Y)
  is Y^o(1) on logarithmic horizons.
```

If `HDNC102703` holds, then

\[
\int_1^Y|H_{\rm def}(X)|^2\frac{dX}{X}=Y^{o(1)}.
\]

Cauchy--Schwarz gives subpower logarithmic \(L^1\), hence subpower negative
mass. PR #718's fixed Mellin--Landau consumer then yields RH.

## Relation to the balanced occupancy frontier

Equations `L-102700--L-102701` identify `HDNC102703` with the root-free
half-divisor physical occupancy operator in PRs #696 and #707, now specialized
to the native-completion defect and the fixed common mother.

The source amplitudes, same-product multiplicity, unit/root coordinate,
squared source and higher prime-power terms have all been removed or bounded.
Only distinct-product physical overlap remains.
