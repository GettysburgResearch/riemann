# Independent review of the short-cube raw gain

Reviewer: `/root/audit_formalization`, an independent analysis agent in this research pass. Date: 2026-10-10.

**Verdict:** the exact cube regrouping, norm bounds, and two optimized regimes pass this scoped mathematical review. The corollary gives a source-conditional mean-square improvement for the literal raw two-axis Gauss polynomial over squarefree dual rows, with q=f=1. It does not prove an unrestricted-row moment or a new zero-free boundary.

## Exact bindings

| Role | File in research authoring directory | Bytes | SHA-256 |
|---|---|---:|---|
| Reviewed corollary | `theta/SHORT_CUBE_RAW_GAIN.md` | 7,560 | `8d97d0a4e6a0eef6ca0178e0dca7ff6e2cd059d594eba1e45fee47d57563cc40` |
| Required new completed estimate | `theta/PRUNED_COUPLED_MEAN_SQUARE.md` | 22,426 | `411d7b28c0dabc97807d21683d731126e742d16424b1809787c87849dfb9e8d1` |

The publication may copy these exact bytes to its packet root. The finite arithmetic interface was compared directly with PR #918 `INTERFACE_COMPARISON.md`, Lemma 2.1 and (3.10), at commit `cfa102748b26f840ccc4b963a660711424db0ec3`. The classical squarefree-row sieve and the companion's pinned analytic dependencies remain inputs. This is agent mathematical review, not numerical testing, Lean verification, peer review, or a new independent proof of those imported analytic theorems.

## 1. Literal inverse and long-part regrouping

The inverse coefficient is \(\mu(h)\lambda(h)^3\chi_h(k)^3/Nh\), and the completed child has the original outer mask \((a,h)=1\). On expanding its physical cube index b, that mask combines with \((a,b)=1\) to give exactly \((a,hb)=1\). Neither \((h,b)=1\) nor \((n,hb)=1\) may be inserted, and neither is inserted here.

The product of character factors is \(\chi_{hb}(k)^3\), including its zero on nonunits. Thus grouping by d=hb gives exactly
\[
c_R(d)=\sum_{h\mid d,\,Nh>R}\mu(h).
\]
The new d need not be squarefree. Its coefficient has the stated divisor bound, and physical support makes the entire rearrangement finite. The normalized child uses \(B/(Nd)^3\); no square-root factor is missing. This is an exact long-part identity rather than a replacement by independent signs.

## 2. Short and long norms

At \(B_h=D/(Nh)^3\), the three completed terms are
\[
HD,\qquad H^2D^{5/12}(Nh)^{7/4},\qquad
H^{4/3}D^{2/3}(Nh)^2.
\]
The companion is uniform for the required original outer mask. After multiplying norm-level terms by \(1/Nh\), the sums are respectively harmonic, of size \(R^{7/8}\), and of size R. This verifies every exponent in (2.2); no arithmetic label count is replaced by a divisor count.

For fixed d, the raw column an is squarefree, so grouping it gives a row-independent divisor-bounded coefficient even though d has arbitrary powers. The ordinary squarefree-row sieve applies at column length \(D^2/(Nd)^3\). In the long-part norm, the three summations have weights \((Nd)^{-1}\), \((Nd)^{-5/2}\), and \((Nd)^{-2}\). On finite physical support, these give respectively a logarithm, \(R^{-3/2}\), and \(R^{-1}\). Squaring proves (2.4).

The row-dependent exterior characters are contractions in both estimates. Adding short and long norms gives (2.5) with the displayed harmless constant and small-power losses. Bounded nonempty endpoint scales are covered by fixed support constants.

## 3. Optimization checked

For \(1\le H\le D^{19/44}\), take \(R=D^{4/15}H^{-4/15}\). The third and fourth terms are \(D^{6/5}H^{4/5}\). The second becomes \(D^{53/60}H^{23/15}\), whose comparison with that target is exactly \(H\le D^{19/44}\). The remaining terms are smaller in the stated range.

For \(D^{19/44}\le H\le D^{19/24}\), take \(R=D^{1/3}H^{-8/19}\). The second and fourth terms are \(DH^{24/19}\). The third becomes \(D^{4/3}H^{28/57}\); it is below the target exactly when \(H\ge D^{19/44}\). The remaining terms are smaller throughout this interval. Both cutoffs lie in \([1,D^{1/3}]\), and the expressions agree at the junction.

At \(H=D^{1/2}\), the cutoff is \(D^{7/57}\) and the resulting exponent is \(31/19\). The ordinary squarefree-row envelope supplies only exponent 2 for this same normalized raw object in that regime. The note therefore establishes a quantitative improvement of a specified actual raw mean square, conditional on the companion inputs.

## 4. Scope retained

The argument uses the full completed estimate on short cube labels and the classical estimate on the rest. It does not require every shortened child to satisfy the companion's diagonal-size range. That is a legitimate improvement over merely demanding a uniform bound for every child.

The theorem is still restricted to squarefree dual rows and q=f=1. It neither provides the growing A2 auxiliary/exclusion adapter nor reaches the initial fourth-moment transformed height near \(D^{3-\theta}\). The physical-row moment and its signed off-diagonal estimates remain open. No numerical zeta boundary follows from this corollary alone.
