# T-100700 — Double-owner dual terminal closure matrix

Claim ID: `T-100700`  
Status: **UNCONDITIONAL STRUCTURAL ADVANCE; TWO TERMINAL ESTIMATES OPEN**  
Created: 2026-08-20  
Base: PR #691 at `c85123d6c25b5b2ade89ab30a736f9b18844a489`  
RH status: **unproved**

The live proof graph has many equivalent detectors but one recurring middle
problem: distinct squarefree cores interfere after physical collapse.
`L-100700--L-100704` replace the undifferentiated middle estimate by a
least/greatest-owner matrix with two mechanisms assigned to disjoint regions.

## Common producer

The native Euler source is decomposed exactly by the least and greatest
selected prime. `L-100700` proves the matching Hilbert-space inequality:
all interactions between different matrix blocks are removed before any
arithmetic estimate.

The matrix entries are

\[
\mathfrak D_{i,i}=(I-U_i),
\qquad
\mathfrak D_{i,j}=(I-U_i)(I-U_j)
\prod_{i<h<j}(I-r_hU_h),\quad i<j.
\]

## Route A — deterministic long-interval renewal

For `p_j/p_i>8`:

1. square only the interior primes before physical collapse;
2. keep both endpoint owners untouched;
3. expose each finite divisor sign;
4. use the positive divisor-renewal theorem on the remaining dilation
   transport.

`L-100702` proves the exact normal form. The only remaining sign is the
explicit native coefficient `beta(d)`. The terminal theorem is the long-block
one-sided estimate `LRNM100704` (or the stronger all-region `DORN100702`).

## Route B — centered short-interval moment energy

For the diagonal and `p_j/p_i<=8` blocks:

1. use the minimal ratio-eight ordinary-Mobius wavelet;
2. factor its activation zero;
3. remove the neutral root by the centered phase circle;
4. retain only `K_X=X^(o(1))` logarithmic moments;
5. apply the double-owner Hilbert inequality to the direct sum of those
   moments.

`L-100703` proves this exact root-free normal form. The terminal theorem is the
short-block energy estimate `SCME100704` (or the stronger all-block
`DOMC100703`).

## Combined closure

`L-100704` proves

\[
\boxed{
\mathrm{SCME100704}+\mathrm{LRNM100704}
\Longrightarrow RH.
}
\]

The combination is source-complete:

```text
diagonal and short blocks       counted in SCME;
long blocks                     counted in LRNM;
empty source                    zero for X>8;
no block                        counted twice;
no endpoint collar              discarded;
no positive inverse             used;
no root-containing square       imported.
```

## Exact boundary

```text
double-owner coefficient matrix             inherited exact
two-sided convex block decoupling            proved exact
endpoint Cauchy phase budget                 proved exact
interior squaring/renewal normal form        proved exact
centered moment double-owner form            proved exact
short-L2 + long-L1 gluing                     proved exact
SCME100704 short-block energy                open / RH-bearing
LRNM100704 long-block one-sided renewal      open / RH-bearing
Riemann Hypothesis                           unproved
```

This packet does not relabel either terminal estimate as a proof. Its advance
is that two genuinely different partial mechanisms now compose without an
untyped residual between them.
