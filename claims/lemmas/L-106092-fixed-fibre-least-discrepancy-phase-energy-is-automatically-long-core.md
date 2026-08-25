# L-106092 — Fixed-fibre least-discrepancy phase energy is automatically long-core

Claim ID: `L-106092`  
Programme aliases: `LFAM1.ROUGH_TAIL_LOCAL_MOMENT`, `LFAM2.FIXED_FIBRE_LONG_CORE`, `STRESS.LEAST_DISCREPANCY_LOCAL_CLOSURE`  
Status: **PROVED UNCONDITIONAL FIXED-FIBRE PHASE BOUND**  
Created: 2026-08-25  
Depends on: `L-106090--L-106091`; parent `L-102836`, `L-102956`, `L-102959`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Retain the notation of `L-106091`.  Put the opposite reduced core in one
octave

\[
D\le d<2D,
\]

and suppose its complete physical coefficient is

\[
z_d=
\frac{\delta_d}{g\,d\sqrt Q}\,v_d,
\qquad
|\delta_d|\le X^{o(1)},
\qquad
\|v_d\|\le1,
\tag{L-106092.1}
\]

after equal-product aggregation.  Boolean representation, carrier, shell and
finite incidence multiplicities are included in the \(X^{o(1)}\) factor.

## 1. Automatic long-core range

By the least-discrepancy orientation,

\[
P^-(d)>\ell.
\]

Since \(D\le d<2D\),

\[
D>\ell/2
\qquad\text{and}\qquad
1+\ell/D<3.
\tag{L-106092.2}
\]

## 2. Uniform phase estimate

The literal physical phase is

\[
e_\ell(-hQg^2d^2).
\]

The multiplier \(Qg^2\) is a unit modulo \(\ell\), so it merely permutes the
nonzero phase coordinates.  Applying the one-prime square-core estimate, or
equivalently the masked literal-product theorem, gives

\[
\sum_{h=1}^{\ell-1}\|F_h\|^2
\ll
\frac{X^{o(1)}}{g^2Q}
\left(1+\frac{\ell}{D}\right).
\tag{L-106092.3}
\]

Hence

\[
\boxed{
\sum_{h=1}^{\ell-1}\|F_h\|^2
\ll
\frac{X^{o(1)}}{g^2Q}.
}
\tag{L-106092.4}
\]

The bound is uniform in every anchor-dependent mask of modulus at most one,
including

```text
(d,c)=1;
P^-(d)>ell;
owner/core cleanliness;
Boolean factor and shell labels;
marked-67 and renewal strata.
```

## 3. Exact consequence for the family channels

By `L-106091.5`, both the untwisted rough tail and the sum of all
nonprincipal even channels are bounded by the same fixed-fibre source energy:

\[
\frac{\ell+1}{\ell-1}\|F_0\|^2
+
\frac{2\ell}{\ell-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}\|M_\eta\|^2
\ll
\frac{X^{o(1)}}{g^2Q}.
\tag{L-106092.5}
\]

Thus no local conductor, core-length, ramification or character-family-size
loss survives.

## Scope

This theorem closes every **fixed anchor/fixed opposite owner** rough-tail
packet.  It does not control the coherent sum over the anchor index

\[
(g,c,P,\text{owner allocation and source labels}).
\]

That remaining amplification is not a local phase problem.  A source-blind
sum of the fixed-fibre estimates is refuted in `R-106090`; the exact global
frontier is `T-106090`.
