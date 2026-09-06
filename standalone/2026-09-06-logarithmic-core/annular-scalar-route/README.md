# Alternative: one finite prime-power sum per square scale

**PROPOSED COMPLETE REDUCTION PROOFS; independent review required. RH and the
terminal unbounded arithmetic inequality remain unproved.**

This continuation does not extend the previous full-window sign beyond length
one. It constructs a different exact route without growing Schur matrices.
A fixed positive autocorrelation filter removes the complete safe prime-tail
constant and all earlier prime powers. Its remaining source is a nonnegative
weighted sum in the factor-16 annulus [X/4,4X]. One-sided Landau transfer and
an unconditional interpolation bound permit sampling only X=m^2.

For integer m>=2 set

 B_m = sum_(m^2/4<n<=m^2)(64n-m^6/n^2)Lambda(n)
       +sum_(m^2<n<=4m^2)(64m^6/n^2-n)Lambda(n).

The complete proposed theorem is

 RH iff B_m >= (135/2)m^4-48m^3 for every sufficiently large m.

Under RH the inequality holds for every m>=2 with normalized margin >1/10.
Every coefficient on the left is nonnegative and rational. The terminal test
uses no zeros, gamma/zeta evaluations, omitted prime tail, or numerical matrix.
It is still an RH-equivalent arithmetic assertion, not a proved estimate.

The positive filter is (65/64)W(x)-[W(x-log4)+W(x+log4)]/8. Its multiplier
has no zero in the RH-sensitive strip. The computed scalar comparison constant
is between 1/25 and 1/20, and the entire remaining gamma correction is between
zero and 1/10. These bounds justify the rational slack 1/4.

A source-level countermodel also explains why a naive extension rule fails:
one can preserve the actual kernel on any prescribed finite interval, preserve
P2=-zeta'(2)/zeta(2) exactly, and keep a nonnegative source satisfying a PNT
asymptotic, yet lose global positivity. The model has a continuous tail, NOT
the actual integer prime-power measure. Literal arithmetic remains essential.

Read PROOF.md for every quantifier, the one-sided Laplace argument, the exact
finite-boundary correction, and the square-sampling estimate. SOURCES.md compares
Suzuki and the older #352 annular route: no claim of external novelty or
annulus minimality is made. This is not a contradiction of #352's restricted
factor-64 optimization, which uses a different scalar and different constraints.

The checker independently encloses the scalar constant, runs finite exact
identities, and verifies the new scalar inequality only for m=2,...,64. This
is not an unbounded test or a full-window positivity certificate. The accepting
arithmetic is integer/Fraction with outward 160-bit dyadic log enclosures.

    python -B validate.py
    python -B verify.py --check result.json
    python -B -O verify.py --check result.json
    python -B test_rejections.py
    python -B -O test_rejections.py

No inherited research, review, canonical, formal, or workflow file is changed.
The first open theorem is exactly the displayed eventual lower bound.
