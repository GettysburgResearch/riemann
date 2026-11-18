# Director adjudication: a sharper critical derivative tail

18 November 2026. I read the full analytic proof prime64_sharper_moments.md, reconstructed every strip, cutoff and summation estimate, inspected the entire check program and its integration callback, and read the independent analytic64_sharper_moments_skeptic.md. The independent replay and director run are version-pinned separately. No publication-priority claim is made.

Unconditionally, for T>=100, r=min(1/4,2/log T), the two-sided critical-line block satisfies

    sum_(T<|gamma|<=2T) |zeta'(rho)|²|2^(1−rho)−1|²
      <=3600 T log T/r³.

The local Hardy phase bound retains T^d instead of discarding it at horizontal offset d. It cancels the shifted polynomial coefficient growth. An Euler cutoff M=ceil(T/2), nonstationary Bernoulli modes and a centered Gaussian Gram bound give the Hardy strip norm<=68T log T. Cauchy gives derivatives. A cubic left cutoff has both value and derivative zero before the block, so Rolle provides the first stationary point without assuming a preceding zero in the interval. Its derivative is absolutely continuous across the two polynomial pieces. The exact strict-left/inclusive-right convention assigns dyadic boundary zeros once. Multiplicity contributes zero at a multiple zero and no separation is needed.

The source-free analytic tail follows by summing3600 log(T)/(T r³) on T=2^jY. Beyond logY>=8 it equals a positive explicit quartic with leading coefficient900 log^4Y/Y. At smaller Y the exact radius switch is retained. The analytic coefficient tail at100 is less than24958.591; adding the previously certified finite sum gives the full series upper bound24959. A complete sum through2·10^11 with width below0.00021 would suffice for a1% enclosure relative to the existing positive lower bound; that large sum was not computed.

The optional finite integral splice is rigorous rather than an integral of a nonholomorphic absolute value. On each polynomial cutoff piece the callback integrates the holomorphic square of the first or second derivative of the Hardy function times the cutoff. Its complex-strip guard enforces gamma log branches in their right half-planes and excludes the zeta pole, including on every analyticity request. On the real path these derivatives are real, so their squares are exactly the desired nonnegative integrands. Cauchy is applied to the certified real integrals afterward. Splitting at the cutoff and into widths<=50 avoids both derivative jumps inside a piece and nonfinite integration output.

The independent two-block FLINT replay bounds contributions from(100,200] and(200,400] by2.22 and2.13. Using the actual balls and the analytic tail starting at400 gives a tail below8248.95. With the certified finite sum,

    0.25253801685456458 < derivative-weighted critical series <8249.21.

This entire statement is unconditional for that critical-line series. RH is used only to identify it with the prime-array limit C_2. The result does not lower the different near-function tail B(Y) in the finite-N remainder. Its upper endpoint remains wide; continuous certificates lower the sufficient cost without pretending to compute the true constant.
