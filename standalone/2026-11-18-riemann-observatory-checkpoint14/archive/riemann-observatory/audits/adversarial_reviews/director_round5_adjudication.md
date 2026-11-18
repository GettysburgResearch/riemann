# Round-five mathematical adjudications

2026-11-17. These are scoped mathematical reconstructions, not complete-paper technical audits. The director independently checked the mechanisms below and read the named completed proofs/reviews. Primary source inputs retain their own access, version and verification limits. No RH resolution, unconditional new zero bound, record-bound or publication-novelty claim is made.

## Scalar taper extrema

Accepted THM-SCALAR62-M2 and THM-SCALAR62-FIXED-M. The all-degree M=2 result is a complete model proof. The director checked the exact elementary-symmetric energy expansion, the duplicated-label exchange, the with-replacement conditional variance factor, complement identities, m=5 coefficients and strict equality condition. The independent reviewer also reconstructed the imported small-degree cases in the same taper convention. Repeated phase values cause no failure because conditioning is on labels, not values. The fixed-M sufficient region follows by a valid n²d comparison of normalized monomial cross terms and a Schur/variance bound; it does not settle arbitrary m,M outside that region.

The exact Hessian formula was independently reconstructed from subset and weak-composition moments. The700 integer signs are a finite local result only. No global extremum or arithmetic transfer follows from that grid.

Evidence: scalar62_two_term_extremum.md; threshold62_scalar_two_term_review.md; scalar62_local_curvature.py/results. General all-M coalescence remains open in this investigation outside the stated sufficient regime.

## A certified shared-support Lagarias interval

Accepted the exact interval certificate in lagarias_shared_ca_latest62_round5.md and the independent lagarias_shared_ca_rt62_ca.md. At epsilon=log(14/13)/log13, the only global maximizers of sigma(n)/n^(1+epsilon) are55440 and720720. Prime-power increments strictly decrease with the exponent, and the first threshold decreases with the real prime base. Thus the certified comparison at17 excludes every larger prime; the global conclusion is not inferred from a finite prime enumeration. The sole tie at13 is algebraically exact. The director checked the multiplicative argument and the monotonicity proof of consecutiveness.

The endpoints have exact divisor sums232128 and3249792. A192-bit integer-directed replay and an independently implemented Decimal/divisor-pair replay give strictly positive Lagarias margins, respectively greater than9051 and143828. The already adjudicated global concavity theorem puts the smooth comparison above the common arithmetic support line throughout the closed interval. This covers665281 integers inclusively and adds665280 to the previous contiguous verification through55440, extending it through720720. Equality remains only at1. This is a finite certificate, not an infinite-tail argument or field-first computation claim.

## Shifted Möbius approximation, including the classical endpoint

Accepted LEM-LATEST62-W501, THM-LATEST62-W502 and OBS-LATEST62-W503 with their declared arithmetic inputs. Also accepted the classical q=1 extension in mertens_shifted_q1_latest62_round5.md after two complete independent source reconstructions. Let L=logN, phi(U)=sqrt(U/logU), epsilon_N=A/sqrt(LlogL), and P_N(s)=Sum_(n<=N)mu(n)n^(-s-epsilon_N). Assume RH and the stated uniform reciprocal-zeta inputs of Bui–Florea and Bui–Florea–Heycock, including |M(x)|<=K sqrt(x)exp(C phi(logx)). For every fixed A>C and real q>=1,

d_q(P_N)=O((logN loglogN)^(-1/4)),

and, with the separately adjudicated ratio slope,

d_q(P_N)^2~epsilon_N Sum_(distinct gamma)m_gamma[1-binomial(2m_gamma,m_gamma)/4^(m_gamma)]/(1/4+gamma²)^q.

The converse for any fixed A>0 and q>=1 holds even along an unbounded subsequence by the exact Hardy evaluation witness. The forward quantifier is A>C, not every A>0, moving A_N, or the equality edge A=C. Constants and usable finite thresholds remain unevaluated.

For q>1, the Abel endpoint and concave tangent bound, followed by Fourier Plancherel and the fixed-q Lindelöf multiplier, suffice. The director independently derived this argument before reading its final draft and checked its real-power Hardy extension. The Mertens envelope alone does not provide the q=1 multiplier estimate; a modulated bump is an explicit generic obstruction.

The classical endpoint needs the new uniform twisted Perron lemma, not that false generic multiplier step. The director read the candidate, stress addendum and both independent audits and checked all three height ranges. The first reciprocal moment is used only on full dyadic panels away from the twisted height. Near it, the pointwise Bui–Florea estimate is applied at a=min(U^(-1/2),w/(Ulogw)), w=log|t|. Its two optimization branches give the remainder sqrt(x)|t|^(1/2)exp(O(sqrt(U)/logU)); the other contour pieces give sqrt(x)|zeta(s)|exp(C_*phi(U)). Both new joins and the high connectors have explicit bounds. In particular the twisted lemma covers all|t|<=x^(3/4), including its central case when a fixed t falls below exp(phi(logx)) as x tends to infinity. It is therefore eligible for every x>=N in the Abel remainder, rather than only near its lower endpoint.

The constants C_* and C are not conflated. For the low/middle junction take T0=exp(sqrt(L)). The low supremum of log|zeta| is O(sqrt(L)/logL)=o(phi(L)), while the middle first contour term has tail factor exp(B1phi(L)-sqrt(L)/8). The second term loses only sqrt(L) in the norm. The exact C103 Proposition13 high-height proof applies to all0<epsilon<=1/2; only its Proposition14 has the old larger shift condition. This avoids circularly importing that condition. The total truncation is o(sqrt(epsilon_N)).

The director visually inspected the actual Bui–Florea Lemma2.2,(2.8), and BFH Theorem1.2,(1.4), and checked their parameter substitutions. The Bui–Florea copy is an accepted author manuscript, not a typeset publisher PDF. BFH's substantial reciprocal-moment theorem remains a declared external input; a full independent technical audit of its entire proof was not performed. Its separate inspected variance issue is not in the reciprocal-first-moment chain used here. This is a source-dependent conditional transfer, with priority unresolved. The array and two-piece decomposition already belong to Báez-Duarte/Balazard–de Roton. Comparing to one specific2010 upper bound is legitimate; claiming a current-best or new-to-literature bound is not yet justified.

Evidence: mertens_shifted_weighted_latest62_round5.md; threshold62_mertens_shifted_weighted_review.md; mertens_shifted_q1_latest62_round5.md; mertens_shifted_q1_latest62_stress_addendum_round5.md; threshold62_q1_twisted_perron_review.md; ratio62_q1_mertens_shifted.md; horizontal_ratio_slope_director_adjudication_round5.md.

## Retaining a horizontal denominator repairs the older density route

Accepted the local replacement proof in witness62_bgstb_section6.md, alongside the independently reconstructed thin-box repair in BGSTB_full_reading_formal62.md. A unit-height O(logT) zero count does not imply the microscopic O(1) vertical sum printed in arXiv2306.04799v1,(6.4). The synthetic countermodel is to that inference, not to actual zeta zeros or the theorem's conclusion. The printed Stieltjes signs/exponent also need their explicitly stated correction.

For the charged outer zero put m=logT|beta-1/2|>=1/2. Keep the horizontal denominator: for1<=d<=2m, exp(d)/(d²+v²)<=C exp(2m)/(1+m²+v²). The director checked this by q=2m-d and boundedness of exp(-q)(1+q)². Unit shells then contribute O(logT/(1+m²)). The missing saving survives as the integrable horizontal layer weight. Exact layer integration under the source's uniform density inputs proves S(T)=o(TlogT), so the theorem route can be repaired without the incorrect microscopic inference.

This does not establish a false-theorem finding. The author follow-up2501.14545v3 separately documents a correction to the published Theorem1 remainder. Its exact formula/version map was read; it does not verify the inaccessible journal treatment of original Section6. A repository cover linked to the journal does not turn the13-page arXiv-layout PDF into the journal version. Later weighted-density and horizontal-multiplicity refinements have their own proof records and remain separate until adjudicated. Older numerical consequences are not current-best claims.

## General positive-real boundary energy

Accepted OBS-HG501 below. For the compensated right-half-plane Herglotz representation, the small-translation cocycle energy is the sum of an explicit atomic gamma term and2ax from the linear term at infinity. The director checked two mathematically different proofs. One uses weighted Wiener/autocorrelation to discard the continuous measure, the contraction of exp(-z) on Re(z)>=0, and finite-atom gamma profiles. The other uses the exact Poisson identity, the modulus kernel K_epsilon(t)=log(1+epsilon²/t²), and F(u)=u-1+exp(-u); its cross defect is exactly(1-exp(-u))(1-exp(-v)). The continuous contribution is o(epsilon) by the L2 autocorrelation kernel. The squared normalized tail norm has limsup at most2ReG_tail(x), tending to zero after the small-epsilon limit. This permits infinite total measure with finite weighted mass and avoids an invalid unweighted infinite-measure Fourier integral.

The Gaussian boundary modulus is exp(-a epsilon²/2), with squared modulus exp(-a epsilon²); its difference from1 is second order. Its first-order energy is the2ax term in the interior Poisson identity. Finite-measure energy converges against bounded continuous tests; when its limit has a nonzero atomic part, convergence in total variation to that limit is impossible. Atomless measures instead have total energy tending to zero. With a>0 energy escapes to infinity, so a blanket general C_b test-convergence claim is not made. The xi specialization needs RH to identify its positive-real logarithmic derivative; this theorem supplies no RH implication by itself. Classical Herglotz/Wiener antecedents are credited and nonlinear-formula priority remains unresolved.

Evidence: witness62_herglotz_atomic_energy.md; threshold62_herglotz_atomic_energy_review.md; witness62_infinite_herglotz_energy.md; herglotz_atomic_energy_rt62_herglotz.md; ratio62_herglotzpriority.md.

## A specific xi-weighted spectral candidate has empty spectrum

Accepted OBS-XW501/502. Assuming RH, F(w)=xi(1/2+w) gives W_tau f=F(w)f(w+tau)/F(w+tau), a C0 contraction semigroup on ordinary right-half-plane H2. Every positive-time operator is compact, injective and quasinilpotent. The actual generator has maximal domain{f inH2:fprime-(Fprime/F)f inH2} and empty spectrum. This excludes this particular construction as a spectral list of zeta zeros; it does not rule out other Hilbert–Pólya operators or prove RH.

The director independently reconstructed the source-based compactness and resolvent proof. Besides the gamma/subpower estimate, the independent reviewer supplied a cleaner compactness input: Riemann–von Mangoldt guarantees at least c log|t| zeros in a sufficiently wide fixed ordinate window. The paired quotient contracts by a fixed factor at each of them, forcing uniform boundary decay. Truncated boundary output is Hilbert–Schmidt and the tail has norm tending to zero. Any nonzero eigenvalue contradicts the superexponential growth of F along a positive real ray and the Hardy evaluation bound. Compactness then gives spectral radius zero; a direct Bochner resolvent integral converges for every complex lambda. No unsafe logarithm of a semigroup spectrum is taken.

The generator domain follows in both directions by bounded evaluations and the pointwise identity d_tau W_tau f=W_tau(fprime-Gf), integrated as an H2 Bochner integral. Normalized evaluation kernels are outside that dense domain: their exact square-root displacement coefficient is positive by OBS-HG501, and a separate boundary-pole argument confirms the exclusion. A dense span outside a dense domain is not a contradiction. Operator-theoretic antecedents are documented in the independent source audit; the xi specialization's priority is not established.

Accepted the independently checked sharp norm addendum: log||W_tau||=-(tau/2)logtau+(tau/2)(1+log(2pi))+O(logtau). The director independently checked the uniform digamma/right-half-plane Dirichlet-series estimate and the adjoint evaluation-kernel lower bound. This is another obstruction to treating this particular semigroup as a self-adjoint spectral zero list. Evidence: ratio62_semigroup.md; xi_weighted_semigroup_rt62_xi_semigroup.md; xi_semigroup_norm_rt62_xi_semigroup.md. Priority remains unassessed.
