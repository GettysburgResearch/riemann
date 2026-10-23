# Independent assembly-interface audit of the shifted-center detector

23 October 2026. Reviewer: root agent. This is internal mathematical
review, not external peer review. I contributed the exact-formula adapter,
real-center remainder bound and Euler constants; those parts are not an
independent invention claim. The separate type-agent audit addresses them.

Reviewed source `SHIFTED_CENTER_FORD_DETECTOR.md`, SHA256
`a25dc862eb72cf29a4dc14b9d3dc71f15dce32cf89416106b1dd6a2e7012c024`,
and `verify_shifted_ford.py`, SHA256
`d8093aceece06c1f0b6314b571559cdd523eb3826887a357311ab60774b8cb9f`.

I checked the analytic chain S1--S20 against the exact compact-test
formula and Ford v5 Lemma 2.2, including its factor 1/(4eta) and strip
cotangent orientation. The right-line Fourier transform gives exactly
Lambda(n)n^(-sigma)/(n^(2eta)-1); no extra factor 2eta belongs in C.
The critical-line contribution is f0/(2eta) times J.

The shift sigma=1-lambda preserves the physical prime sum, the pole
W(-1), and the selected zero signal. Re((s-rho)/lambda)>=-1 licenses
the cubic F0 remainder for all nontrivial zeros. The local half-disc
minimum principle and the comparison

    r^-3 <= (2/eta^2) Re[1/(sigma+eta+iq-rho)]

outside the disc have exactly compatible local counting constants.
Retaining one selected zero while subtracting the full local count is
conservative. No density estimate or omission of high zeros is used.

The full-strip cotangent sum cannot be discarded solely from the local
minimum window. S12--S14 repair that defect by retaining every possible
wrong-sign far term and summing it with the explicit zero-count estimate.
At the real center, reflected zero pairs have positive rational parts;
the absolute F0 sum and E_f give the displayed cubic allowance. The
negative gamma constant and prime gain are distinct contributions.

I separately reconstructed the endpoint replacement in S20: combine
C-.805 first, then upper-bound its positive coefficient times lambda.
The selected ratio h/l-1 is independent of B. Every adverse term is
monotone in B, and the exact shifted critical envelope divided by
h0-2A decreases with l>=40 by the displayed derivative bound. This
proves an infinite-height implication, rather than interpolation from
sampled endpoints.

The Euler checker independently enumerated all prime powers to10000 and
bounded both infinite tails with Lambda(n)<=log n. Normal and -O runs
gave identical rational output. It proves C<.9 on lambda<=1/160 and
Z(1.48)<2. The high checker depends on the frozen rational kernel engine;
its W expansion is used only at 0<=z<=.1, as required. At R=4.72,L=52
the reported strictly positive margin is about .000294889.

No defect found in this chain. The global theorem still requires the
complete low rectangle, common-minimum gluing, imported finite RH
verification and the explicitly identified Revers preprint bound.
This audit makes no fixed-half-plane or RH claim.
