# L-102749 — Exact distinct-pair physical restriction of the Wick defect

Claim ID: `L-102749`  
Status: **PROVED EXACT REDUCTION; CROSS-PAIR ESTIMATE OPEN**  
Created: 2026-08-23  
Depends on: `L-102746--L-102748`; `T-102800--T-102810`  
RH status: **unproved**

Let \(\mathcal O_*\) be the fixed carrier-centered outer-ray observation of
`T-102780`, including the exact source-region and gauge recombinations already
frozen on PR #719.  The hard Wick current is

\[
 \mathcal J_{\rm Wick}(X)
 =\int_0^1(1-t)\,
 \mathcal O_*[RS L^2e^{-tL}](X)\,dt.
\]

Split

\[
 L^2
 =\sum_i x_i^2+2\sum_{i<j}x_ix_j.
\]

The diagonal term \(\sum_i x_i^2\) is polylogarithmic by `L-102601` and
`L-102743`.  Therefore

\[
 \boxed{
 \mathcal J_{\rm Wick}
 =\mathcal J_{\rm pair}+\mathcal J_{\rm diag},
 }
 \tag{L-102749.1}
\]

where

\[
 \boxed{
 \mathcal J_{\rm pair}(X)
 =2\int_0^1(1-t)
 \sum_{i<j}
 \mathcal O_*[RS x_ix_j e^{-tL}](X)\,dt,
 }
 \tag{L-102749.2}
\]

and

\[
 \int_1^Y|\mathcal J_{\rm diag}(X)|\frac{dX}{X}
 =Y^{o(1)}.
\]

## 1. Equal-product collapse

Retain the unordered pair \(\{i,j\}\) until all coefficients belonging to one
integer product have been combined.  By `L-102747--L-102748`, the complete
cost of:

```text
pair-owner multiplicity;
repeated-label diagonals;
same-product factor pairs;
free labelled pair energy
```

is \(Y^{o(1)}\).

## 2. Exact remaining operator

Write \(\mathcal J_{P,n}\) for the physical component with unordered owner
pair \(P\) and integer product \(n\).  After equal-product collapse, the only
uncontrolled term in the physical Gram form is

\[
 \boxed{
 \sum_{\substack{P\ne Q\\n\ne m}}
 \left\langle
 \mathcal J_{P,n},\mathcal J_{Q,m}
 \right\rangle,
 }
 \tag{L-102749.3}
\]

restricted by the fixed ratio-eight support of the centered outer kernel.

Define

```text
DPWNC102749:
  after exact carrier, region and gauge recombination, the distinct-product,
  different-unordered-pair physical restriction in (L-102749.3) has subpower
  logarithmic negative mass at the fixed outer ray.
```

Then

\[
 \boxed{
 \mathrm{DPWNC}_{102749}
 \Longrightarrow
 \mathrm{WNC}_{102743}
 \Longrightarrow
 \mathrm{OER}_{102780}
 \Longrightarrow
 \mathrm{RH}.
 }
 \tag{L-102749.4}
\]

This is a strict narrowing of `WNC102743`: the root, first chaos, pair diagonal,
equal-product multiplicity and free pair energy have all been removed.
