# Director adjudication: finite trace tests, sparse powers and integrality

18 November 2026. I independently checked the full proofs in frontiers/geometry64_minimal_polarization.md, positivity64_geometric_skeptic.md, uniform64_geometry_polarization_skeptic.md, positivity64_quantitative_trace_test.md and uniform64_quantitative_trace_skeptic.md. The primary Weil, Grothendieck and Katz–Messing passages are separately matched in those reports. These are finite-spectrum results and explicit transfer boundaries, not a global classical-zeta operator construction or a publication-priority claim.

Let a fixed finite nonzero multiset A, with positive integer multiplicities, be closed under conjugation and alpha->rho²/alpha. Normalize z=alpha/rho, d=|A|, and s_n=sum z^n. Purity |z|=1 is equivalent to positivity of tau(p(x)p(x^(-1))) for all real polynomials, and already to the two-term tests |s_n|<=d for every n>=1. It is also equivalent to a one-sided subexponential upper bound s_n<=exp(epsilon n), for each epsilon>0 eventually on one density-one set. Simultaneous phase returns have positive lower density, so a largest modulus R>1 forces positive exponential excursions meeting that set. The argument requires one compatible fixed finite spectrum and positive multiplicities. It is not a claim about independently varying approximants or signed infinite traces.

If r is the number of distinct roots, positivity on polynomials of degree<=r−1 suffices: interpolate opposite real-compatible values at an off-circle conjugacy class and its reciprocal. The resulting joint r-by-r Toeplitz matrix is the relevant finite test. Its two-by-two minors alone are weaker. Traces do not determine Jordan blocks or a positive metric on the original operator space.

The integral reciprocal polynomial (X^4+32)(X^4+8), at q=4 and rho=2, has normalized s_n=0 for4 not dividing n. It passes every prime-degree two-term test, yet s_4=−10 and s_8=17 violate d=8. The independent extension realizes an integral alternating similitude and positive formal closed-place counts; those extra properties still do not force purity. Finite real reciprocal degree-four perturbations can pass any prescribed finite list, so a uniform finite cutoff needs arithmetic discreteness or another gap input.

## A completely explicit integral cutoff

For monic P in Z[X] of degree d>=1 with nonzero q-reciprocal roots, q an integer>=1, put

    D=max(d,d(d−1)/2), A=(q+1)(2q+1)^(D−1),
    n0=4d A, B=n0·6^floor(d/2).

All roots have modulus sqrt q iff the exact integer traces obey

    sum alpha_j^(n0 k) <= d q^(n0 k/2)
    for k=1,...,6^floor(d/2).

To see the uniform gap, choose a root of maximal modulus and beta=alpha bar(alpha)=qR²>q. It is an algebraic integer of degree at most D; every conjugate has modulus<=beta. If beta<q+1, the nonzero integer norm of beta−q bounds beta−q from below by (2q+1)^(1−D). If beta>=q+1 the gap is already1. Hence log R>=1/(2A). Our even n0 gives n0 log R>=2d>log(2d). Approximate the n0-scaled phases of one representative per nonreal conjugate pair by the6-box pigeonhole principle. A multiplier k<=6^floor(d/2) makes every cosine exceed1/2; real signs disappear at even powers. Thus the normalized trace exceeds d. This proof handles reducible polynomials, repeated roots, q=1 and the vacuous off-circle d=1 case without root isolation.

The input reciprocal identity is X^d P(q/X)=P(0)P(X). Companion-matrix powers or Newton recurrences give an exact finite test, but the integer sizes and cutoff can be astronomical. This is finiteness, not a practical algorithm at high degree. It supplies no prime-index witness. A weight substitution requires the squared radius itself to be a positive integer.

The geometric comparison preserves the direction of the primary theorems. Weil uses one correspondence trace with its transpose and Frobenius inverse relation. Grothendieck invokes B(X) and Hdg(X×X), not hard Lefschetz alone. Katz–Messing imports étale weights with degree-isolating geometric hypotheses; its algebraic projectors follow from disjoint weight spectra and do not create purity from an alternating determinant alone. Applying the finite lemma to classical zeta still requires an actual global trace model and a justified infinite limiting argument.
