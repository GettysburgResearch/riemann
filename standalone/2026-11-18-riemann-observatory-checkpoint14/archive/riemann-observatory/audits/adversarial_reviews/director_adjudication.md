# Director adjudication of scoped mathematical claims

2026-11-17. These are scoped claim reviews, not certification of entire papers or publication novelty. Advocate/skeptic records retain their independent starting points. Level3 below applies only to reconstructed elementary claims.

## Finite Li-prefix obstruction — scoped Level3

Proposer: proposals/independent_campaigns/li_advocate.md. Independent skeptic: li_skeptic.md. Adjudicator independently checked additivity of the local logarithmic derivative; the reflected-root change between rho/(rho−1) and (rho−1)/rho; positive paired cosh terms; the explicit quartet binomial bound; and preservation of order and real symmetry. For n≤N,T≥N the quartet bound (2+2e)N²/T² and baseline bound 1/[6(N+pi)²] give strict positivity at T≥10N(N+pi). The weaker skeptic bound O(N/T) also suffices for existence; the advocate bound is stronger through conjugate cancellation. No contradictory conclusion.

The zero-count-matched canonical product is also sound after a small proof repair: normalized factors for t≤w are not each ≥2. Use t≤w/2, and all remaining factors≥1 for w≥1/2. This proves log G≥c w log w and infinite exponential type. Upper growth follows by Stieltjes integration with N(t)=O(t log t); exponent of convergence1 supplies matching order. The count main term is matched only to O(1); arithmetic explicit formulas, gamma factor and Euler product are absent. The conclusion is a generic-class obstruction, not insufficiency of every conceivable finite zeta-specific certificate.

Finding class: independently checked with no issue found in the inspected portion. No novelty or RH advance claimed.

## Repeated-root smoothing — scoped Level3

Proposer: multiplicity_adapted_smoothing.md. Independent reconstruction: toy_advocate.md. Adjudicator verifies Parseval, equivalence of residual constraints sum c_k=1 and sum k c_k=0 to divisibility by(1−z)², and the normal-equation solution c_k=alpha+beta k. Substituting the displayed sums yields alpha=2(2L+1)/[(L+1)(L+2)] and beta=−6/[(L+1)(L+2)], L=N+2. The norm equals alpha. Independently multiplying BCF's triangular coefficient(n+1)(1−n/N) by(1−z)² yields residual(2/N)sum_{k=1}^N z^k−z^{N+1}, norm²=1+4/N. This is outside BCF Theorem2's simple-root hypothesis. No error in that theorem follows.

Relative window for the optimum is quadratic; coefficients are cubic. That distinction and N versus L=N+2 matter.

Finding class: independently checked with no issue found. This reconstructs a finite polynomial exercise and explains a real obstacle to naive multiplicity transfer.

## Finite graph complexity — scoped Level3

Proposer: spectral_counting_barrier.md. Independent reconstruction: graph_skeptic.md. Adjudicator checks −iU*U'=diag(l_j)>0, including compressed derivatives at degeneracies, determinant total phase, and floor conventions counting(0,t]. The exact identity N(t)=Lt/(2pi)+F(0)−F(t),0≤F<E, gives D=N(4K)−3N(2K)+2N(K)=3F(2K)−F(4K)−2F(K), hence |D|<3E. The Riemann–von Mangoldt main term has D=K log2/pi+O(logK). For a different graph at each K, accuracy o(K) at all three heights therefore needs E_K≥[log2/(3pi)+o(1)]K. This uses one fixed boundary unitary within each graph's three evaluations. Energy-dependent scattering, infinite graphs, different operators and narrow windows are outside the conclusion.

Finding class: independently checked with no issue found. The quantitative consequence is reconstructed here; literature novelty has not been established.

## Exact Lagarias finite certificate — two implementations and mathematical review

Director code plus independent Fraction implementation for selected cases and review of all-case lower-bound logic. At n≥1, directed harmonic lower bound≥1, so exp and log approximations are nonnegative and monotone. Positive Taylor and atanh truncations give rigorous lower bounds; exact integer arithmetic gives5039 strict inequalities and equality at1. This independently reproduces a known finite dependency, not the infinite criterion or RH.

## Clustered roots — independent director reconstruction, not full Level3

For residual evaluations at1 and e^{i theta}, Gram diagonal d=L+1 and off-diagonal S=sum_{k=0}^L e^{ik theta}; inverse yields error(2d−2ReS)/(d²−|S|²). Riemann sums at theta=c/L give F(c)=(2−2sin(c)/c)/(1−(2sin(c/2)/c)²). Taylor expansions give F(0)=4 and oscillatory decay gives F(c)→2 as |c|→∞. This formula is not asserted to interpolate monotonically or remain between2 and4: e.g. c slightly above2pi gives F(c)<2. The noncommutation of fixed-distinct and coalescing limits is genuine. This is a two-reconstruction scoped check; it has not received a separately commissioned third full reconstruction.

## Cluster nonuniformity — additional independent reviews complete

Independent coefficient reconstructions are now in cluster_skeptic.md and cluster_advocate.md. Director independently checks reciprocal a_n=sum_{j=0}^n q^j, the second-difference residual, and its boundary coefficient−(sum_{j=1}^N q^j)/N. Therefore the exact squared error is[2N+2ReS+|S|²]/N². At theta=c/N, S/N→∫_0^1e^{−icx}dx and the limit is sinc(c/2)². It is positive except the nonzero2pi integer resonances. The optimizer has O(1/N) *squared* error at fixedc, with the Gram formula checked above. This scoped statement now has independent advocate, skeptic and director reconstruction, qualifying as a fourth Level3 elementary claim group. It illustrates failure of uniformity; it is not a counterexample to BCF's fixed-polynomial theorem.

## Exterior-integral frame repair — scoped Level3

Independent proof: af_boundary_repair.md. Third reconstruction: frame_third_review.md. Director checks the unweighted frame inequality exactly: Parseval and the support interval of lengthL give ∫|sum c_k φhat(τ−alpha_k)|²≤2piL||c||². The ν logarithmic tail contributes PSD trace O(d/T³) because every sample lies in[T,2T] and φhat(r)=O(r^−2). Squared tail R(delta)=∫_delta^∞|φhat|² satisfies R(0)=O(L),R(delta)≪min(L,1/delta,1/delta³) in the appropriate ranges. Summing grid distanceskh splits into harmonic k≤O(L) and cubic k>O(L) sums, yielding J≪BLlogL. Hence |E2|≤2||Hν||J≪B²L²logL; normalized by a²L⁴ this is O(TlogL/L²), dominated by printed E1 estimate O(TlogL/L). The displayed Proposition5.2 remainder is recovered. This is a fifth scoped independently checked elementary claim group, not complete validation of the source's main theorem or formalization. No novelty claim is made. Preserve the printed coarser bound and the replacement proof separately so future reviewers can check the exact dependence.

## Uniform compact-gap remainder — sixth scoped Level3 group

The second research pass converted the earlier fixed-c limit into an explicit uniform theorem. Advocate: uniform_cluster_remainder.md; independent skeptic: uniform_cluster_skeptic.md. Director independently reconstructed a stable divided-difference Gram proof before reading the drafts. With L=N+2, B=12+C², and E_N the *actual* two-root polynomial optimum, for all N≥0 and |c|≤C,

|L E_N(c/L)−F(c)|≤38 B²/L,

F(c)=(2−2sin(c)/c)/(1−(2sin(c/2)/c)²), F(0)=4.

At every finite-L alias c=2pi*j*L the polynomial has a double root, so use its genuine derivative-constraint optimum; the raw two-evaluation quotient is undefined. This finite-L convention was an adversarially identified repair to the initial statement.

Independent proof checks: g_c(x)=(e^{icx}−1)/(ic),g_0=x has |g|≤x and Lipschitz constant1. Its continuous Gram determinant v=(1−sinc²(c/2))/c² satisfies v≥1/(12+c²). The latter follows from sinc²x≤1/(1+x²/3), proved by the alternating-series bound for x²≤3/2 and sin²≤1 thereafter. Normalized endpoint quadrature errors are ≤1/(L+1) for g and≤2/(L+1) for|g|²; thus variance error≤3/(L+1). For L≥6B inversion is stable with v_L≥1/(2B); ratio and normalization errors give(2B²+5B)/L. For2≤L<6B, E≤1 and F≤B/3 give the global38B² bound, including aliases. The skeptic's independent two-variable-kernel proof yields the stronger18B² constant, which is consistent; the public master statement retains the conservative38B². Neither constant is claimed sharp.

This is a complete elementary uniform-remainder argument in a finite polynomial model. Historical novelty and arithmetic transfer are unestablished. It partially completes the first research task; next work is multi-cluster constants and arithmetic grouped residues, not repeating the same two-root limit.

## Original Hardy source reading — scope check

Director independently viewed and read the original French scans pp1012–1014 after the source agent located them. The t^(2p) factor in equation3 is visible in the original. Under eventual sign, monotone convergence applies to the positive tail when alpha approaches pi/2; finite-interval convergence is ordinary dominated convergence. Endpoint theta flatness can be checked by Poisson summation on y=i*pi+w, Re(w)>0, with shifted half-integer dual Gaussian and Re(1/w)→infinity along the source path. Then the odd/even moment sign contradiction is valid. This is a scoped reconstruction; Cahen's and Bohr–Riesz's original dependencies were not audited. Whole-work status remains Level1, not a completed Level2 paper audit.
