# Hereditary numerator moments and a proposed 633/700 Dedekind boundary

Status: PROPOSED complete deductions and analytic composition from named
unconditional source inputs; independent mathematical review is required.
No RH/GRH, missing native inverse-Mobius moment, OPEN-L or signed-covariance
hypothesis is assumed. No accepted theorem, Lean verification or RH proof is
announced. Main and integrated scientific status are unchanged.

Read HEREDITARY_MOMENTS.md, DENSITY.md, COMPOSITION.md and SOURCES.md, in that order.

## The new organizing idea

An exceptional subset containing R rows should not automatically pay the full
family's U-row moment. On a complete coefficient dyad of length V, combine the
actual R-row triangle bound with DF's full sieve:

 sum_E |P_chi|^2 << V^(1-2y) min(R V, K(U,V)).

The minimum is between two valid bounds for the SAME full dyad, not an
independence assumption or a replacement of U by R inside the sieve kernel.
Complete sixth-power columns and every original nonunit mask remain.

The resulting selected-moment formula works for every fixed order and every
fixed interior strip. For |E|<=U^(2/3), one explicit gain is

 sum_E |L(3/4+it)|^6 << U^(5/6+eta)(2+|t|)^C,
 sum_E |L(1/4+it)|   << U^(17/18+eta)(2+|t|)^C.

Using these hereditary norms for BOTH L and its mollifier in the shifted zero
detector gives an exceptional-character exponent 5/7 at Re(s)=3/4, improving
#971's 395/552 by 5/3864. This component does not require CT's theta theory.
Moving the detector line and the full-family fourth moment were already in
#966/#968/#969/#971 and are explicitly credited.

## Complete global composition, with inherited qualifications

Adopt #965's proposed subcritical reflected reconstruction and #970's recovered
enlarged local domain. Use X=Y=Z^(149/350), with the diagonal XY term retained.
The full physical pairing has growth 149/700. The exact finite table uses
112 thresholds and 113 exhaustive classes; fourth, sixth and eighth selected
moments are used where they improve the bounds. Both principal remainders,
small norms, horizontal/original-line tails and the infinite large range remain.
The actual Mellin shift is 121/175, giving the proposed strict boundary

                    633/700 = 121/175 + 149/700.

This is 1/420 to the left of the recovered 68/75 proposal. The excluded width
is 67/700. It is not an improvement of the reported special-setting 7/8 result,
an infinite-order angular Hecke theorem, or a bound for the critical native
source. No worldwide novelty or optimality claim is made for these methods.

## Recovery and reproducibility

The missing nineteen-file 68/75 packet was published unchanged in #970 before
this new research. This packet adds readable new files on that recovery branch;
it does not overwrite the historical proof or promote its review status.

    python verify.py
    python -O verify.py
    python verify.py --details
    python run_mutations.py
    python verify_manifest.py

The verifier derives the full rational density/moment/contour certificate from
strata.tsv. Exploration used numerical optimization, but neither an optimizer
nor floating point occurs in the checker. The written interval proof and rational
Bernstein budgets, not sampled numerical trends, justify the finite parameters.
SOURCES.md discloses fresh DF/BGL access and FAILED fresh CT body retrieval.
VALIDATION.md separates execution evidence from unverified analytic foundations.
