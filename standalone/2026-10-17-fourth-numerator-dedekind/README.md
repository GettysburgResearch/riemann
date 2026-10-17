# Fourth numerator moments and a proposed 10/11 Dedekind boundary

**Proposed source-composition mathematics; independent review is required.**
No accepted RH proof, native inverse-Mobius fourth moment, 17/24 theorem, or
infinite-order angular Hecke result is claimed. Fresh CT/DF body retrieval
failed during this pass; the exact #965 analytic interfaces are inherited,
not described as independently verified primary-source theorems.

## What actually changes

The proposed all-number-field boundary becomes **10/11**, improving the newly
published #965 proposal **91/100** by exactly **1/1100**. The excluded width
becomes 1/11, a factor 100/99 larger than 9/100. Against #959's 11/12 proposal,
the boundary gain is 1/132. This remains weaker numerically than the earlier
special-setting 7/8 result and does not approach the full critical line.

The new ingredient is a fourth moment of the L-functions in the NUMERATOR
of the actual CT Poisson expression:

 sum_{Na<=U}^{sixth-free} |L_F^S(1/2+it,psi chi_a)|^4
          << U^(7/6+epsilon)(2+|t|)^C.

The proof powers the complete AFE and uses the fixed-order sieve on BOTH
sixth-free indices. It removes sixth-power columns with their exact zero
masks; a prime may occur in both the residual ideal and its sixth-power root.
No reciprocal-L or new inverse-Mobius moment is assumed.

For any zero-selected row class of size U^nu, Holder gives

 sum_class |L| << U^(3nu/4+7/24+epsilon)(2+|t|)^C.

This beats the previous (nu+1)/2 exponent whenever nu<5/6. At nu=2/3 it saves
U^(1/24). The full good class still uses its second mean; replacing it by the
fourth mean would be worse. Other sparse classes keep individual convexity.

Combined with #965's subcritical reflected bound, this permits

 X=Y=Z^(5/11), growth f(Z)<<_e Z^(5/22+4e), shift b=15/22.

Twenty-seven disjoint classes, both principal remainders, small rows, all
horizontal/original-line tails, and the large-frequency tail are included.
Thus b+5/22=10/11; choose one fixed positive e per point to obtain the strict
half-plane. No boundary-line or e-uniform constant is asserted.

## Reading order

1. NUMERATOR_MOMENTS.md: exact sieve/AFE contracts; complete sixth-power removal;
   all fixed numerator moments and the zero-selected Holder estimate.
2. ZERO_FREE_COMPOSITION.md: scale curve, 27 classes, all contours and tails,
   actual Mellin normalization and descent to arbitrary number fields.
3. PARAMETERS.json and `python verify.py --details`: the complete rational
   thresholds, density detector monomials, and class exponent certificates.
4. SOURCES.md and VALIDATION.md: what was inspected, inherited, executed and
   not independently reviewed. CHECKS.json is finite bookkeeping, not a proof
   of the imported analysis.

The general numerator exponents are kappa_1=1, kappa_2=7/6, kappa_3=19/12,
and kappa_r=r/2 for r>=4. They are NOT the desired native 2r-th moments.
Their Holder envelope is explicitly priced; taking r to infinity does not
by itself improve the zero-free region toward 1/2.

## Publication discipline

This packet adds only standalone/2026-10-17-fourth-numerator-dedekind/ on top
of #965 at d58e3282a9379b6ae165681bc2e21e4f9fd18c26. It modifies no inherited
proof or integrated status. The parent supplies the essential M<1 reflection
reconstruction; that step is credited, not claimed as new here.

The numerical gain is small but is a genuine change of the proposed global
boundary, contingent on the stated analytic inputs and this new adapter.
The priority review is the sixth-free sieve/complete AFE interface, followed
by the subcritical parent and then the new class/contour comparison.
