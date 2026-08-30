# L-108402 — Frobenius-symmetric comparator plus Hellinger debt is a source-faithful live-fibre bound

Claim ID: `L-108402`  
Status: **PROVED EXACT COMPOSITION THEOREM**  
Created: 2026-08-31  
Depends on: `L-108400`, `L-108401`, PR #771 L-107304, PR #765 history recombination  
RH/GRH status: **not assumed**

For every retained shared-conductor fibre \(\iota\), let \(D_\iota\) be the
grouped live occupancy and let \(\bar D_\iota\) be a declared orbitwise
Frobenius-symmetric comparator. Put

\[
N_\iota=\operatorname{tr}D_\iota
=\operatorname{tr}\bar D_\iota
\]

and

\[
\mathfrak H_\iota
=
\|D_\iota^{1/2}-\bar D_\iota^{1/2}\|_{\mathcal S_2}.
\]

Then the complete positive shared-fibre trace obeys

\[
\boxed{
\sum_\iota\operatorname{tr}Q(D_\iota)_+
\le
\sum_\iota\operatorname{tr}Q(\bar D_\iota)_+
+
2\sum_\iota\sqrt{N_\iota}\,\mathfrak H_\iota.
}
\tag{L-108402.1}
\]

The first sum is now a symmetric complete-fibre object. When its physical
squareclass map is the complete twisted convolution of PR #771, it is
diagonalized by

\[
\widehat{A\star_2B}(\chi)
=
\widehat A(\chi)\widehat B(\chi^2),
\]

so no sum over conductor characters is introduced. The second sum is a
literal occupancy discrepancy.

For rectangular fibres, (L-108402.1) becomes

\[
\boxed{
\sum_\iota\operatorname{tr}Q(D_\iota)_+
\le
\sum_\iota\operatorname{tr}Q(\bar D_\iota)_+
+
2\sum_\iota N_\iota
\sqrt{
\eta_{L,\iota}
+\eta_{R,\iota}
-\frac12\eta_{L,\iota}\eta_{R,\iota}
}.
}
\tag{L-108402.2}
\]

This is the exact bridge between:

```text
native shared-fibre rectangles;
partial-Frobenius symmetry;
rank-free squareclass Plancherel;
literal physical positive trace.
```

No injectivity assumption and no arbitrary-coefficient carrier are used.

## Scope

The theorem leaves the arithmetic estimate of the Hellinger sum, the explicit
quadratic-resonant rows, incomplete live masks, endpoints and principal
binding open.
