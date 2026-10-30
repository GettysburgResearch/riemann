# Independent review of the dynamics lane

Reviewer: positivity lane. Date: 30 October 2026.  
Target: `swarm/dynamics/report.md`, read after the mathematical draft was complete and before two requested wording clarifications were applied.

**Outcome: no blocking mathematical error found in the reviewed core arguments.** This is an argument review, not a formal proof check or a global novelty determination.

## Checks performed

- **Quartet classification:** checked the factorization at the starting parameter, the Robin boundary-value argument excluding nonreal zeros there, the critical values, and the uniform localization near large sine zeros. The stated Rouché argument prevents nonreal roots entering from infinity during continuation.
- **Prescribed finite zeros and LP derivatives:** checked the product construction and the identity for the derivative of a polynomial times an analytic function. Each first-order factor preserves the Laguerre–Pólya class by multiplication, differentiation and removal of the explicit real-root factor.
- **Jensen gate:** checked the confluent-hypergeometric coefficients, Laguerre parameter, differential equation and increasing Sonin energy. The first positive critical value supplies the controlling integration-constant constraint.
- **Asymptotic constants:** independently computed `G'''(-pi^2/4) = 2/pi^3`, which yields the reported critical-point correction `-3*pi^2/(16d)`, threshold correction `pi^3/(32d)`, and detection scale `T^2/(4 delta^2)` for this model.
- **Root-flow density bound:** checked the pairwise rational inequality, including its nonnegative numerator, and integrated the resulting differential inequality for squared maximal imaginary part. The time-persistent density hypothesis is essential and is correctly retained.
- **Heat-bath law:** checked the Hermite heat representation, modified Jacobi coupling, interlacing count and imaginary-axis sign change. These give the exact collision time `a^2/(4m+2)`.

## Requested clarifications

1. The reusable integration gate must explicitly assume degree exactly `N` and positive leading coefficient `gamma_(n+N) > 0`. With a negative leading coefficient, the displayed critical-value inequalities reverse. The model and actual-xi setting already have the intended positive coefficients.
2. In the finite-prefix disk estimate, name the scaled argument `w = -z^2/K^2` to avoid confusion with the unscaled variable of the polynomial multiplier.

The author accepted both wording changes. No shared files were edited by this reviewer.

The review does not turn the model constructions or finite Sturm checks into an actual-xi descent theorem. The missing source-specific critical-value inequality remains open.
