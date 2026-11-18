# Director adjudication: central drift and the omitted vertical normalization

18 November 2026. I read all six pages of arXiv2307.02027v1, SHA-256 `d833f2af1f426c36f72cfb43df6b67bb3b3bf50ac9324c5069bc7442768a72d9`, and reconstructed the regularization, the corrected criterion and the explicit examples. Independent source evidence is in geometry64_central_zero_scope.md, release64_central_extension_versions.md and the positivity64_operator_probability_notes.md complete reading. The exact PDF and official TeX agree. Public checks found only v1 and no accessible journal manifestation or correction; an author's forthcoming listing is not treated as a verified journal text.

## An undefined auxiliary drift, with an exact repair

Equation(2.6) uses the full completed function xi_F. Equation(2.7) defines B_F=i xi_F'/xi_F(1/2) while expressly allowing central order m0>0. That logarithmic derivative has a pole, so the displayed ordinary value is undefined. The later Hadamard product explicitly retains z^m0 and repeats the same substitution. No deflation convention appears. The paper's own weight18 example Delta E6 has central order1, as independently proved below, providing an unconditional mathematical witness. The issue is an exact versioned auxiliary definition, not an allegation that its intended GRH criterion is false.

Put J_F(s)=xi_F(s)/(s−1/2)^m0, extended through the center. Replace only the drift by

    b_F=i J_F'(1/2)/J_F(1/2)
       =i lim_(s->1/2)[xi_F'/xi_F(s)−m0/(s−1/2)].

Reflection makes b_F real. The exponent is then −m0 t²/2+i b_F t+sum_(gamma!=0)m_gamma(e^(−i gamma t)−1)/gamma². Its half-line transform still uses the FULL logarithmic derivative z^(-2)xi_F'/xi_F(1/2−iz), including the central i m0/z³ term. Dropping that pole as well would incorrectly remove the Gaussian component.

On GRH the triplet is Gaussian variance m0, uncompensated drift b_F and finite positive noncentral jump measure. In general this is a deterministic translation convolved with Gaussian and compound Poisson components. For the converse, infinite divisibility and uniqueness of the continuous logarithm give the Lévy–Khintchine exponent itself, whose growth is O(1+t²). The half-line transform is holomorphic for every Im z>0. Meromorphic identity excludes all upper poles and reflection excludes lower poles. This direct argument repairs the source criterion without assuming a separate cancellation bound on an exponential zero sum. The original classical-zeta article has m0=0 and is unaffected by this central regularization.

## Degree one already permits a central zero under the printed axioms

The source's §3 discussion omits vertical shifts from degree-one classification and expects a central zero only at degree>=2. Its S3, however, explicitly allows complex gamma shifts. Take a primitive nonprincipal chi and F_tau(s)=L(s+i tau,chi). It remains in the printed Selberg class: it is entire, its coefficients are chi(n)n^(-i tau), the Euler logarithm retains its bounds, gamma shifts become mu+i lambda tau, Q stays fixed and the new root number is omega Q^(-2i tau). Degree and primitivity do not change. A nonzero shift of zeta itself would move its pole and fail S2; the nonprincipal example is essential.

Use chi4 and let tau be an ACTUAL zero ordinate in the independently certified interval[6.02094890469,6.02094890471]. The two endpoint completed-beta signs at192bits bracket a genuine critical-line zero. Then F_tau(1/2)=0, unconditionally, at degree1. Its coefficients cannot be an unshifted character: nonzero values at3 and5 would make both tau log3/(2pi) and tau log5/(2pi) rational, contradicting unique factorization. This is an exact construction, not a nearby numerical evaluation. The primary degree-one classification in Perelli PartII Theorem6.3 and Kaczorowski–Perelli Theorem3 explicitly includes these shifts. Perelli's extra normalized condition theta_F=0 is absent from the six-page paper.

Thus the degree assertion needs a canonical-height normalization; primitivity alone does not repair it. The usual arithmetic central points of canonical automorphic L-functions remain meaningful. The corrected probabilistic criterion still applies to the larger class. The Gaussian-versus-jump split depends on the selected height when arbitrary vertical shifts are allowed; it is not an invariant distinction across the full printed class. The normalization qualification is recorded separately from the verified undefined-drift finding.

The weight18,22,26 examples also admit a positive result. On y>1, Delta(iy)>0, E4(iy)>0 and E6(iy)>0. The split Mellin formula for each sign-minus form gives Lambda_f(k/2+h)=integral_1^infinity f(iy)[y^(k/2+h)−y^(k/2−h)]dy/y. It has the strict sign of real h and a positive derivative at0. Hence these completed L-functions have exactly one real zero, at the center, and it is simple. This replaces the source's numerical observation for those examples with an analytic argument. It does not establish their GRH or locate nonreal zeros.

No whole-paper technical promotion is made for this source: other contextual estimates and source versions retain their individual scope. No external author message or public flag was sent. Further proposed sign issues in other manuscripts remain unadjudicated until their exact current versions and correction histories are checked.
