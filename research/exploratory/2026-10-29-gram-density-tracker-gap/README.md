# What the new Gram frame and conductor-box densities leave open

The [squarefree Gram moment](../2026-10-29-squarefree-gram-moment/README.md) and [powered-detector box bounds](../2026-10-29-fourth-moment-cyclic-box/README.md) are source-qualified density/linear-algebra deductions. Neither currently supplies a new individual zero-free region or an additional certified source for the formal tracker.

## A concrete source sufficient for the sixth-power extraction

At row scale Y and source-column scale P=Y^(6/5), let T be the actual masked sextic matrix and m the normalized Möbius vector, with one of the source's fixed common profiles. The [125/144 target](../2026-10-29-target-125-144/README.md) reduces an improved zeta boundary to

    ||Tm||² ≪ Y^(21/20+ε)                                      (1)

for every ε>0, with the exact primary-row, profile and mask conventions in that note. Let V be the spectral image supplied by the squarefree Gram result at H=P^(53/72−δ), and write Π for its orthogonal projection. Its theorem gives, source-conditionally,

    ||TΠm||² ≪ Y^(21/20−6δ/5+ε) (1+|t|)^B.                    (2)

Thus the quantitatively exact missing bound

    ||T(1−Π)m||² ≪ Y^(21/20+ε)                                  (3)

with the same source conventions is sufficient for (1), by the triangle inequality. If height is present, choose a common permitted height power only after fixing the polynomial order B and the target ε. A direct signed estimate for the cross term could give an alternative, but (2) by itself gives no such estimate. The general full-row sieve instead gives `||T(1−Π)m||²≪Y^(41/30+ε)`, which misses (3) by a power Y^(19/60). The current frame is a concrete low-dimensional portion of the source space, not a decomposition of T into its large and small spectral parts.

This is a genuine logical gap. In an abstract source space of dimension ≍P take any orthonormal frame of N≈H columns, choose a unit m orthogonal to its span, and let a rank-one operator T have right singular vector m and squared singular value Y^(41/30). Then the Gram is I, the frame overlap is zero, and the existing full-operator bound is saturated, while (1) fails. Here H/P=P^(−19/72−δ), so the profile span may be a vanishing fraction of the ambient dimension. This toy example has no claimed arithmetic realization; it shows why Gram conditioning and overlap do not alone furnish the missing source estimate.

## Why almost-all conductor density is not a fixed zeta strip

The box results count zeros across nontrivial Kummer characters with prescribed good ramification, for example labels `AB^(n−1)` with coprime squarefree A,B in fixed conductor boxes. They yield estimates `O(X^(R+ε))` with R>0 on exceptional labels, and their natural finite set of fixed characters can contain exceptions. In particular a bound of this form cannot by itself exclude a zero of any designated fixed character, including the trivial character underlying ζ_K. The box families also omit the sixth-power natural rows on which the sextic character becomes trivial; conductor ordering is different from the natural row ordering of (1). Converting a zero of ζ_K into many *nontrivial* box-family zeros would require a separate zero-propagation theorem, not supplied by the density bound. For the associated abelian extensions, ζ_L(s)=ζ_K(s)∏_(χ≠1)L_K(s,χ), with primitive all-place class-field characters χ, so a zero of ζ_K is indeed inherited by the full ζ_L, provided the nontrivial factors are holomorphic there. But the box statements control the relative quotient ζ_L/ζ_K and explicitly leave ζ_K itself out; consequently they provide no zero-free full ζ_L to exploit this identity.

For an all-natural-row sixth-order zero count, one can quantify the required gain. A ζ_K zero produces, after the fixed bad-prime and primitive-inducing conventions are matched, the same zero for rows `u=v⁶`; good prime v with Nv≈Y^(1/6) already give ≫Y^(1/6)/log Y such rows. Therefore a uniform all-row exceptional-count estimate with exponent strictly **below 1/6**, counting those imprimitive principal rows and including that zero's fixed height, would contradict its existence. A positive exponent at or above 1/6 does not produce the contradiction by this counting argument. The available conductor-box theorems neither reach this count nor apply to those rows. This is a sufficient count criterion, not an assertion that such an estimate holds or is needed by every possible proof.

The formal tracker has its own quantified global source, count-window, physical-contour and finite-height hypotheses; a source-qualified box density or a projection estimate must be converted into one of those exact interfaces before it can be used. No such conversion is shown here. In particular, the above conditional target is a mathematical reduction and is not a compiled Lean statement or tracker admission.

**Independent review.** Literature checked the exponents, complement gap, abstract rank-one example and sixth-power-row count, including nonvanishing of the finitely deleted Euler factors in Re(s)>0 and the exclusion of the pole at 1. The underlying source-qualified inputs remain as stated.
