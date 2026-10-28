# Factoring the principal correction through an infinite-type Hecke L-function

**Correction and review:** An earlier draft omitted the conjugation on the infinity-type character. The formula below uses the rendered source equation (7.6). Independent review corrected a further missing factor 1/(1−V) in the local identity; an independent internal recheck verified the corrected algebra and zero correspondence against the displayed source formulas; the source identity itself remains an imported input.

**Status:** Proposed analytic lemma, proposed, with corrected algebra checked internally subject to the stated source identity. Not a zero-free region for zeta.
**Scope:** The scalar residue-point factor from OpenAI's *The Quasi-Riemann Hypothesis*, equations (7.6), (7.11), (7.12), (7.17), and (10.1); see the [source PDF](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) and [preceding calculation](2026-10-28-principal-product.md).
**Inputs:** The local identities in the source, and the standard analytic continuation and functional equation of unitary Hecke L-functions. The source identities are assumed, not independently audited here.
**What was run:** Symbolic algebra with SymPy and the exact local estimates below; no numerical zero search or independent L-function proof.
**Novelty:** Unknown. This is a source-specific factorization and its consequences, not a literature priority claim.
**Smallest remaining gap:** An audit of the imported source local identity; no estimates are supplied for the full multivariable contours or other rows.

## Statement

Use the source's Eisenstein field F, finite set S of excluded prime ideals, and fixed finite-order Hecke character η with its ramified support in S. At its principal residue point let H_eta(s)=H_eta,1(s,1,1/6). For a nonzero ideal (a) coprime to the conductor of η, put

    ψ_eta((a)) = (conj(a)/|a|)^6 η((a))^6,

The six units of F make this independent of the generator. It is a unitary Hecke character with infinity type (-3,3), multiplied by the finite-order character η^6. Let L^S(v,ψ_eta) be its Hecke L-function with the Euler factors at S deleted.

For each σ0>1/2, define K_eta(s) by the product of the local K_p given below. It is holomorphic on Re(s)>1/2 and converges absolutely and uniformly on Re(s)≥σ0. Its tail obeys

    K_eta(s) = 1 + O_{σ0}(P0^{-c}),
    c = min(σ0, 1, 6σ0-3) > 0,

uniformly for Re(s)≥σ0 and η, provided S contains every prime of norm at most P0 as well as its defining bad primes. Therefore P0 can be fixed in terms of σ0 so that |K_eta(s)-1|≤1/2 on this half-plane. On Re(s)>2/3, where the source product and L Euler product converge absolutely,

    H_eta(s) = L^S(6s-3, ψ_eta) K_eta(s).

The right side analytically continues H_eta to Re(s)>1/2. For every admissible finite S, its zeros in Re(s)>1/2 correspond, with multiplicity, to zeros of L^S(v,ψ_eta) at v=6s-3. In Re(v)>0, the finite deleted Euler factors are nonzero, so these are also the zeros of the complete Hecke L-function.

## Proof

For p outside S set Q=Np, D=η(p)Q^{-s}, R=conj(α(p))^6η(p)^6 Q^{3-6s}. The source local identity specialized at u=1,w=1,z=1/6 is

    H_p(s) = 1 + [D(2/Q-1/Q²)-1/Q²
                     +(1-1/Q)² (R(1+1/Q-D)-D/Q)/(1-R)]/(1-D).

Here α(p) is p/|p| for the source's primary generator; the conjugation and cube in a_p=conj(α(p))^3η(p)^3 are visible in the source PDF, equation (7.6). Define K_p=(1-R)H_p where the latter expression is initially defined. Direct simplification gives the identity

    K_p - 1 = [D/Q + D/Q² - D/Q³ - R/Q + R/Q³ - 1/Q²] / (1-D).  (1)

Equivalently, putting v=1/Q, the local factor has the useful exact form

    K_p = (1-v²)(1-vR-(1-v)D)/(1-D).  (2)

For Re(s)>1/2, |R|<1 and |D|<1, so |vR+(1-v)D|<1; hence each K_p is nonzero there. The right side defines K_p holomorphically for Re(s)>0. For Re(s)≥σ0>1/2, |D|≤Q^{-σ0} and |1-D|≥1-2^{-σ0}, uniformly in η. Thus

    K_p-1 = O_{σ0}(Q^{-1-σ0} + Q^{-2} + Q^{2-6σ0})
          = O_{σ0}(Q^{-1-c}).

The number of ideals of norm at most x in this fixed quadratic field is O(x). Partial summation and the standard product estimate give the stated uniform tail, normal convergence, holomorphy, and nonvanishing after enlarging S. Since R=ψ_eta(p)Q^{-(6s-3)}, the source H-product factors as stated in the common absolute-convergence half-plane Re(s)>2/3. The identity theorem gives the continuation. Absolute local uniform convergence together with the nonvanishing of each K_p gives a nonvanishing K product on Re(s)>1/2, for every admissible finite S, and hence the zero correspondence. Deleted Euler factors cannot vanish when Re(v)>0.

## Consequence and limits

For every admissible finite S, the continued H_eta is zero-free for Re(s)>7/12 if and only if L(v,ψ_eta) is zero-free for Re(v)>1/2. The Hecke functional equation and conjugation make the latter condition equivalent to the generalized Riemann hypothesis for this particular infinite-type character. Thus this continuation alone cannot justify the zero-free contraction needed by the source all the way to 7/12 without a comparably strong new input. It also does not control other rows, the full multivariable contours, or the low estimate; no zeta zero-free conclusion follows.

## Conditional corollary from a claimed unitary-Hecke region

Assume the rank-one statement in Boyang Hu's [*A seven-eighths zero-free half-plane for unitary Weil L-functions*, version 1](https://hexagonmath.org/2610.00216v1): every unitary Hecke L-function of a number field has no zero in Re(v)>7/8, with its stated pole exceptions. This is a preprint claim; it has not been independently verified here. The character ψ_eta above is unitary and has a nonzero angular infinity type, so it is not a pure norm character and its L-function is entire. For every admissible finite S containing the bad primes associated with η, the continued principal correction satisfies

    H_eta(s) ≠ 0  for Re(s)>31/48,

because Re(6s-3)>7/8 there and K_eta is nonzero. This is a conditional statement about the scalar correction, not a new zero-free region for ζ or η. In particular Hu's claimed nonvanishing does not by itself supply the uniform quantitative bound |H_eta(s)|≥1/2 required by the original continuation proposition, nor the missing low or high estimates.

## A weaker multiplier hypothesis for the continuation criterion

The previous paragraph's failure to obtain |H_eta−1|≤1/2 does not itself block the continuation argument. Proposition 2.1 of the source remains valid if its condition (2.2) is replaced by: H_eta is holomorphic and zero-free on Re(s)>σ0, and is bounded on each closed strip 2≤Re(s)≤B, B>2. The other hypotheses and quantifiers remain unchanged.

Indeed, the proof uses the upper bound on H_eta only for convergence on Re(s)=2 and for shifting the defining Mellin integral to Re(s)=B. The stated strip bound, the uniformly bounded reciprocal Euler product for Re(s)≥2, and Gaussian decay yield the same arbitrarily rapid power decay as Z↓0. The two assumed large-Z bounds then make the Mellin transform holomorphic on the same extended half-plane. Fourier inversion identifies it with exp((s−5/6)^2)H_eta(s)/L^S(s,η) on Re(s)>1. Dividing by the nonvanishing H_eta, with no quantitative lower bound needed, supplies the holomorphic continuation of the reciprocal and the same contradiction. The bounds and thresholds may depend on η as in the source.

Our factorization supplies the new multiplier hypothesis at σ0=31/48 *conditional on Hu's stated unitary-Hecke theorem*: its nonvanishing was shown above. On every strip Re(s)≥2, Re(6s−3)≥9, so the absolute Euler product bounds |L^S(6s−3,ψ_eta)| by ζ_F(9), and K_eta is uniformly bounded. These facts apply to this particular H and are not new estimates for J_eta or f_eta. The original source's low exponent and high-row estimates do not meet the remaining criterion at this lower boundary without further work.


## Prior-art qualification

Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*, version 1](https://hexagonmath.org/2610.00216v1), Section 6.3, equations (6.14)–(6.15) and Lemma 6.1, records this same local rational-factor shape in a different number-field and fixed-infinity-type construction, and states nonvanishing of its principal factor for Re(s)>2/3. Equation (2)'s local convexity argument is also present there. This note's further extraction of an auxiliary Hecke L-function and the claimed zero correspondence in Re(s)>1/2 have not been checked against the remainder of Hu's paper or the broader literature; no novelty is asserted.
