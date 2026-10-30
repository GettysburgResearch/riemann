# A positive-moment barrier for the 125/144 target

This is an abstract feasibility model, not a counterexample produced by Möbius coefficients or by the signed Poisson core. It shows only that the stated inverse second moment, ordinary fourth moment and an additional pointwise θ-strip estimate cannot by themselves force the target saving.

Let Y be an integer and take Y abstract rows. For every `0≤r≤6/5`, define positive quantities

    |M_u(Y^r)|² = Y^max{0,5(r−1)/6},     |S_u|=1.               (1)

Then the all-row inverse second moment satisfies, with equality in exponent,

    Σ_u |M_u(Y^r)|² = Y^max{1,(1+5r)/6},                         (2)

matching the shape of the source sixth-free inverse bound for these lengths; and the ordinary fourth moment is `Σ_u |S_u|⁴=Y`. At `P=Y^(6/5)`, the model gives

    Σ_u |M_u(P)|² = Y^(7/6),                                    (3)

above both the `Y^(21/20+ε)` target for 125/144 and the `Y^(19949123/18750000+ε)` threshold for improving the staged θ boundary.

Even append the hypothetical uniform pointwise estimate expected from a fixed zero-free half-plane `Re s>θ=4369347/5000000`, namely `|M_u(Y^r)|²≪Y^[r(2θ−1)+ε]` for these fixed bounded r. Model (1) obeys it: for r≤1 its left exponent is 0, and for `1≤r≤6/5` its left exponent is at most 1/6 while the right exponent is at least `2θ−1>0.74`. At r=6/5 the hypothetical allowance is `Y^[(6/5)(2θ−1)+ε]≈Y^(0.8973+ε)` for each squared value. The pointwise hypothesis is stated here as an additional assumed bound; it is not deduced from the staged candidate without its separate semantic and uniform-Hecke bridge.

Thus no argument using only these numerical positive estimates and interpolation/Hölder between them can force a better exponent than (3): this admissible abstract data would satisfy every such inferred inequality. The model is not asserted to satisfy the actual arithmetic coefficient relations, Liu's stronger marked moments, any zero detector, or the signed dual identities. A successful attack can and must use more structure than the few inequalities displayed here, for example cancellation of the signed small-divisor core with all coupled masks and phases retained. The target and exact sixth-power extraction are in [the 125/144 reduction](../2026-10-29-target-125-144/README.md).
