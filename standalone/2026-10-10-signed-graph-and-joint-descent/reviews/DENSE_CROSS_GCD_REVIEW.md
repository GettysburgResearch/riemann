# Independent review of the dense cross-gcd extension

**Verdict: PASS as a conditional whole-sector theorem, at the versions below.**

Date: 2026-10-10. Reviewer: signed-sector agent. This review independently checks the root-authored dense extension and its composition with the explicit graph-charge interface. The reviewer authored the companion graph manuscript; this document therefore is not an additional independent review of that companion. It is an AI-agent mathematical review, not human peer review or proof-assistant verification.

## Hash-bound objects

| Object | SHA-256 |
|---|---|
| DENSE_CROSS_GCD_SECTORS.md | 90af83fcd69cc95d2d56884e367f1a227828ca32c2cb03315ba5cf1d551f3d43 |
| ARBITRARY_GRAPH_SECTORS.md | ef3704340d3af629a6bbd97d575d35bb5570474e8973a99c600c76bf096c9f13 |
| check_graph_charges.py | 9b7e752cf98a3d3fd0f40fe89b1cacdf497a56249025cd7ff48c8827bc48e671 |
| graph_charge_checks.json | 54e7e19ed2aa739a9877b9340a3bfb39ab70c3533fa8fcef8d866fa4387fd569 |

The dense manuscript was read in full, its final corrections were reread, and its stated content hash was independently recomputed.

## Mathematical reconstruction

The companion's two-axis integrated estimate permits the two native second-moment axes to be on the same Hermitian side: after the exact mixed-sign Euler correction, row Cauchy bounds the absolute product of those two native factors. It does not require one factor from each side. Frozen shared-prime phases remain bounded row multipliers, including their nonunit-zero masks.

With both selected vertices on the left, the dense construction gives charges
\[
B=b-\tfrac12,\qquad A=\frac{k-2b}{k(k-2)}.
\]
For \(k\ge3\) and \(k/[2(k-1)]\le b\le1\), both are nonnegative. Their total is
\[
2kB+k(k-2)A=2b(k-1),
\]
whereas the total native vertex weight is \(1+2b(k-1)\). Thus, once all induced-subset constraints are verified, the analytic charge theorem gives precisely
\[
|\mathcal S_\Theta|\ll HD^{1+\epsilon}R^{2b(k-1)}.
\]
The normalization contains no missing square or factor of \(D\).

I independently recomputed every entry of the manuscript's twelve-corner table from
\[
F_r(n,t)=b(n+t)+r/2-1-t(nA+rB).
\]
All twelve identities are correct. For \(r=0\), every subset having a cross edge lies in \(1\le n\le k-2,\ 1\le t\le k\). For \(r=1,2\), the rectangle is \(0\le n\le k-2,\ 1\le t\le k\). Subsets without a cross edge are separately valid because they have at least two vertices of weight at least \(1/2\). Thus the rectangles cover every subset requiring a constraint.

For fixed \(r\), the slack is bilinear, so its minimum on the appropriate real rectangle occurs at a corner. The stated lower-endpoint identities at \(b_0=k/[2(k-1)]\) are correct:
\[
\begin{aligned}
b_0k-2&=\frac{(k-2)^2}{2(k-1)},\\
b_0(k-1+2/k)-2&=\frac{(k-2)(k-3)}{2(k-1)},\\
k(2b_0-1)-1&=\frac1{k-1},\\
b_0(k-2+2/k)-1&=\frac{(k-2)^2}{2(k-1)}.
\end{aligned}
\]
The remaining corners are zero, positive multiples of these quantities, or nonnegative multiples of \(1-b\). Consequently every induced-subset constraint holds for every integer \(k\ge3\) in the declared \(b\)-range. This is an all-order algebraic argument, not an extrapolation from the finite checker.

The diagonal cutoff follows from
\[
R^{2b(k-1)}\le D^{k-1}.
\]
At \(b=7/8\), this gives \(R\le D^{4/7}\), improving the connected-forest cutoff exponent by \(4/7-1/2=1/14\). The same \(b\) satisfies the dense witness's lower bound for every \(k\ge3\).

## Scope and endpoint checks

The theorem estimates a complete signed sector with every cross gcd at least \(D/R\), while permitting an arbitrary bounded multiplier on the shared incidence ideals. It does not permit a multiplier depending on free singleton ideals. The exact incidence and Euler identities precede the positive summation over shared labels, so the conclusion does not assume monotonicity of an arbitrary signed restriction.

The physical height retains fixed \(h>1\), \(H=D^h\), and the source's uniform shorter-scale native assumptions. The smaller pointwise exponent is explicitly conditional; the dense proof does not establish NM2 or PW. In particular, the \(4/7\) here is an arithmetic gcd-cutoff exponent, not a zeta zero-free boundary.

The final version correctly handles \(R=D\): all gcd thresholds are then automatic, and its upper bound reduces to the original two-axis cost. Pairwise-coprime tuples are outside the dense sector only when \(R<D\).

The corrected non-global-gcd example is compatible with the claimed range. Give the \(2k\) positions pairwise-coprime labels \(c_v\), of comparable norm \(L\), and let column \(v\) omit precisely \(c_v\). Then each column has scale \(D=L^{2k-1}\), every pairwise gcd has scale \(D^{(2k-2)/(2k-1)}\), and the full tuple gcd is one. This is an incidence-pattern illustration, not an additional analytic input.

No complementary moment estimate, full higher moment, sublinear cofinal defect, or new zero-free claim is supplied. If a below-diagonal complete sector is subsequently restricted by deleting a region controlled only at diagonal size, that separate diagonal error must still be retained, as stated in the companion.

## Finite diagnostics actually run

The reviewer ran the bound checker with isolated Python. It passed 964,909 exact finite predicates, including 1,044 dense corner identities, 58,104 dense subset symmetry classes for the declared orders \(3\le k\le24\), 88 lower-endpoint identities, and 22 negative controls below the dense witness's allowed \(b\)-range. The same report checks signed fourth-/sixth-moment incidence identities over all 49 two-prime zero/sixth-root phase assignments, native-axis discounts, and principal-zero preservation.

Those diagnostics do not evaluate genuine global characters, prove the analytic premises, authenticate an external theorem's proof, or certify an infinite moment estimate. They support the finite algebra reviewed above. An independent rerun of the checker and the separate review of the companion's analytic argument remain distinct records.

No mathematical correction remains for the hash-bound dense manuscript.
