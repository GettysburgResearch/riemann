# Independent review of the late quartic square-period draft

Reviewed 18 October 2026 by the theta research agent, independently of the draft author and the root review. This is an internal mathematical reconstruction, not external referee acceptance.

Source: workspace `QUARTIC_SQUARE_PERIOD_LATE_DRAFT.md`, intended publication name `quartic/ALL_SQUARE_INDICES.md`, actual-byte SHA256
`b6fdd7d7a57d3feb6d35270f88f22a62d68c05654556c344da344cbaf3d912a6`.

I read the complete draft, rebuilt its identities, and checked the imported formulas against the primary David--Dunn--Hamieh--Lin article, arXiv:2306.11875v2 (10 May 2025), especially (3.4)--(3.12), (4.34)--(4.38), and the diagonal constant-term formula following (4.22). I also independently viewed Suzuki's original 1983 printed page 114: Theorem 3 states full fourth-power periodicity without a coprimality hypothesis, whereas the immediately following Theorem 4 explicitly imposes one. The draft correctly attributes periodicity as classical.

## Reconstruction

* The finite Gauss-square codec retains the angular Hecke character epsilon, inert primes, and the literal zero cases. Its moving-numerator version is used only for squarefree moduli with the prescribed shared-prime convention.
* Splitting moduli in the two-ray system gives terminal CRT exponents 12j+2 and 12j+8, hence H2 and H0 respectively. The local terminal factors are G and a_pi conjugate(G); the ray matrix is -J in the nontrivial class. Thus AB=q^(3-4z). The one legally coprime fourth-power identity at j=1 forces A h2=q^-1 h0 and then B h0=q^-1 h2, proving the displayed complete even-valuation recurrence without repeatedly stripping a noncoprime prime.
* The unrestricted shared-prime decomposition m=d^2 r produces precisely L(2s-1,chi^2)/L(s,chi conjugate(epsilon) delta_kappa). Choosing chi=epsilon delta_kappa gives (10); the fixed bilinear I/diag choices suffice whenever the base vector is nonzero.
* Section 4a removes that unproved first-coefficient assumption. The direct own-cusp diagonal scattering residue is nonzero. If every nonconstant base-cusp Fourier coefficient vanished, the entire automorphic function would be C y^(3/4), contradicted by the lower lambda^4 unipotent (or C=0). Thus a fixed nonzero base index exists. The moving-numerator quadratic character xi_a and the chosen chi_a cancel exactly, giving (10a), with only fixed deleted Euler factors.
* The scalar K_(1/4)^2 Mellin integral and the Fourier prefactor N(nu)^(1/8) give exactly C(s) and N(nu)^(.25-s/2). Therefore the squareclass exponent is N(m)^(.5-s), and the target variable is s. The extra fixed-base radial factor is entire and nonzero.
* The Gaussian spatial reflection preserves the quartic multiplier on the stated congruence group. This establishes the central-weight compatibility asserted in the draft; it does not construct the full compensated period. An ordinary integral angular Hecke twist of the Fourier index contributes type 2k on nu=nu_a m^2, leaving type 2k-1 in the root m; hence this simple twist cannot make the displayed squarefree piece principal. This does not exclude a separately constructed Weil or descent kernel. The even scalar archimedean representation does not automatically implement the root-index angular twist; no contrary adapter is asserted.
* The quadratic local Ramanujan scattering ratio has the stated normalization. It cannot be counted again as a separate reciprocal-L division after seed-one unfolding.

## Scope

No blocking error was found at the stated arithmetic and Fourier-mode Mellin scope. The draft explicitly leaves squareclass selection, all ramified and unit classes, global cusp regularization, a legal angular adapter, a complete analytic estimate, and numerator cancellation open. Torus orthogonality selects all equal indices rather than squares. The zero inheritance statement is conditional on controlling the actual reciprocal target; the extra Hecke numerator may cancel a zeta zero. Square summability of formal replica coefficients does not establish a bounded operator.

This review does not certify a new zero-free region, a Riemann-hypothesis proof, a full global unfolding, or global norm bounds for an infinite squarefree Fourier filter. The primary-source full periodicity also does not by itself identify a single adelic right translate or control a regularized period on growing levels.

Final conductor qualification (18 October 2026): the general character
in (9) is unramified outside the deleted set S; otherwise S must include
every conductor prime and all sums must be prime to that enlarged S.
This prevents chi^2 from restoring an Euler factor when its primitive
conductor shrinks. Both reviewing agents and the rational agent
confirmed this restriction. The actual target characters already
satisfy the stated S/S_a condition; (10), (10a), and the damped target
are unchanged. The raw source binding above includes this correction.
