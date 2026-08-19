# R-99240 — Fixed-row closure does not require a positive exact equality frame

Claim ID: `R-99240`  
Status: **PROVED METHOD REPLACEMENT / SCOPE FIREWALL**  
Created: 2026-08-19

The score/capacity route requires a same-row calibration with the correct
logarithmic loss. The fixed-row route is different.

For a fixed component row, it is unnecessary to prove that every
finite/continuum correction, activation-knot atom and Volterra boundary mode
has nonnegative source weight. It is enough to construct

\[
c_X(j)=d_X(j)+\mathfrak E_X(j)
\]

with \(d_X(j)\ge0\) and \(\mathfrak E_X(j)=O_j(1)\).

A bounded signed defect contributes a Mellin transform holomorphic in
\(\Re s>0\). It therefore cannot cancel a pole of
\(1/\zeta(s+\tfrac12)\). Landau applies to the nonnegative surrogate
\(d_X(j)\), not to the signed defect.

Consequently the following formerly load-bearing tasks are removed from this
route:

```text
positive signs of both Volterra nullspace anchors;
positive signs of every activation-knot atom;
exact 4sqrt(X) equality-score normalization;
ordinary/radix-four feasibility;
safe-point thinning;
prime-square subtraction.
```

The common-parent source and the fixed-row Mellin consumer remain
load-bearing. A defect growing like \(X^\theta\), \(\theta>0\), would only be
holomorphic for \(\Re s>\theta\) and would not close zeros arbitrarily close to
the critical line; boundedness or subpower growth is essential.
