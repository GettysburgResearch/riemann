# Independent check of the degree4,M2 coalescence maximum

Reviewer:equivalences. Date:2026-11-17. I reconstructed the residual coefficients and Newton-identity bound from semantic_skeptic's statement before reading its saved proof. I then compared `proposals/independent_campaigns/coalescence_maximum_semantic_round3.md`§1. This review concerns that finite case and its exact positive-gap identity, not the general maximum conjecture or the numerical search.

Let Q=product_(j=1..4)(1-q_jz),|q_j|=1,M=2,p=4. Common rotation permits productq=1; reciprocal b1=S=sumq, so A=1+Sz/16. Set a=e2, which is real under this normalization; e3=conjugateS. Direct multiplication gives residual coefficients

15S/16, S²/16−a, conjugateS−aS/16, |S|²/16−1, −S/16.

Thus, with v=|S|²,u=Re(S²), the squared norm is exactly

1+225v/128+v²/128+a²(1+v/256)−au/4.

I checked the cross terms separately: the second and third residual rows each contribute−au/8; the constant row contributes−v/8. Their totals give the displayed coefficients. No sign convention on Q roots enters the norm after common rotation.

Newton p2=sumq_j²=S²−2a gives |p2|²=v²+4a²−4au<=16, hence au>=a²+v²/4−4. Since a²<=36,v<=16, the proposed upper polynomial is

29+243v/128−7v²/128.

Its derivative is at least19/128 on[0,16]; its endpoint is363/8. Equality in v<=16 forces all q_j to coincide. Common rotation removes the temporary product1 restriction, so this proves the claimed finite maximum for all four unit roots, including every collision configuration.

The exact gap identity in the saved proof also checks algebraically. Its three summands expand to

44.375−225v/128+7v²/128−a²(3/4+v/256)−|p2|²/16,

where44.375=355/8. Substitution of |p2|²=v²+4a²−4au gives363/8 minus the original exact energy. Equivalently the identity is

(16−|e1|²)(131−7|e1|²)/128
 +(36−|e2|²)(3/4+|e1|²/256)
 +(16−|sumq_j²|²)/16.

All factors have the stated nonnegative ranges. I have not independently rerun the proposed100 rational checks; the proof uses exact algebra and does not require numerical evidence.

Classification: **Independently checked with no issue found in the inspected portion.** Fixed m4,M2 only; no general-m or general-M maximum, historical novelty, arithmetic transfer or RH conclusion.
