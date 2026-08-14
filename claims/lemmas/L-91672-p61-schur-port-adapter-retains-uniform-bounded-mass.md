# L-91672 — The P61 Schur-port adapter retains a uniform bounded mass

Claim ID: `L-91672`  
Status: **PROVED EXACT NORMALIZATION ADAPTER**  
Created: 2026-08-14  
Depends on: `L-91316`  
RH status: **unproved**

The independent review of PR #447 correctly notes that `L-91316` was stated with `P_53` and the numerical shortcut

\[
\prod_{p\le53}(1+1/p)<9/2,
\]

whereas the corrected provenance route works at `P_61` and rough threshold `67`.

No structural theorem in `L-91316` depends on the value `9/2`. Its pointwise domination

\[
|\mathcal B_P(x)|<\frac89\mathcal V_P(x)
\]

holds for every squarefree finite `P`, and its critical-mass identity is

\[
\frac12\int_1^\infty\mathcal V_P(x)x^{-3/2}dx
=\prod_{p\mid P}\left(1+\frac1p\right).
\]

For

\[
P_{61}=\prod_{p\le61}p,
\]

one has exactly

\[
\prod_{p\le61}\left(1+\frac1p\right)
=
\frac{399441300081868800}{86204059532560853}
<\frac{14}{3}.
\]

Therefore

\[
\boxed{
\frac12\int_1^\infty|\mathcal B_{61}(x)|x^{-3/2}dx
<
\frac89\cdot\frac{14}{3}
=
\frac{112}{27}
<\frac{25}{6}.
}
\tag{L-91672.1}
\]

More sharply, the exact rational upper bound furnished directly by the product is

\[
\frac12\int_1^\infty|\mathcal B_{61}(x)|x^{-3/2}dx
<
\frac{355058933406105600}{86204059532560853}
\approx4.11881917547.
\tag{L-91672.2}
\]

Thus the `P_53` normalization mismatch identified in review is not a boundedness obstruction. The positive two-port theorem transports verbatim to `P_61`, with one changed absolute constant. The rough threshold is then `67`, matching the corrected provenance branch.

This adapter does **not** prove capacity-faithful placement of the shared port into the combined native root complement; that remains part of the live atomwise certificate of `L-91671`.

```text
P53 -> P61 port normalization adapter        PROVED EXACT
P61 port critical mass                       UNIFORMLY BOUNDED
old <9/2 numerical shortcut                  REPLACED
combined native placement                    OPEN / L-91671 PRODUCER
Riemann Hypothesis                           UNPROVEN
```
