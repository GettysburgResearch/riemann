# Finite Li positivity: independent advocate reconstruction

Status: elementary independently reconstructed generic-function obstruction; novelty not claimed. This is **not** a result about the actual Riemann zeta function. Parent adversarial adjudication reconstructed the core product, strict positivity, quartet estimates and normalizations and corrected an intermediate growth inequality; see the revision log. Independent novelty search remains incomplete, and no novelty is claimed. Authoring agent: li_advocate. Date: 2026-11-17.

## Statement L1 (explicit generic obstruction)

For every integer N≥1 there exists a real entire function F of order one satisfying F(s)=F(1−s), F(0)=F(1)=1, F(x)>0 for real x, with all zeros in 0<Re(s)<1, whose first N Li derivatives

λ_n(F)=[d^n/ds^n (s^(n−1) log F(s))]_(s=1)/(n−1)!

are strictly positive, but which has zeros off Re(s)=1/2. One can take

F(s)=cosh(s−1/2)/cosh(1/2) · Q_T(s),

Q_T(s)= [((s−1/4)^2+T^2)((s−3/4)^2+T^2)] / [((1/4)^2+T^2)((3/4)^2+T^2)],

with T≥10N(N+π). In particular, preserving functional symmetry, real coefficients, zero confinement, and entire order does not turn finitely many Li inequalities into a universal certificate.

## Proof and precise conventions

Write G(s)=cosh(s−1/2)/cosh(1/2). Its paired product is

G(s)=∏_(k≥0) [((s−1/2)^2+t_k^2)/(1/4+t_k^2)],  t_k=π(k+1/2).

The product converges locally uniformly since ∑t_k^(−2)<∞. On a small disk about s=1 the logarithms converge locally uniformly too, so finite derivatives can be interchanged with the series. A single zero ρ contributes 1−(ρ/(ρ−1))^n to the derivative convention. Because the whole zero set is invariant under ρ↦1−ρ, this sum also equals the conventional 1−(1−1/ρ)^n sum. This convention distinction matters for a single nonsymmetric zero.

For the line pair ρ=1/2±it_k its contribution is 2[1−cos(nθ_k)], where θ_k=2 arctan(1/(2t_k)). These are nonnegative. For every n some k has 0<nθ_k<2π, so the sum is strictly positive. Moreover θ_k≤1/t_k, and the contributions are at most n²/t_k², justifying absolute convergence after pairing.

For a fixed N choose k with N≤t_k<N+π. Then 0<nθ_k≤1 for 1≤n≤N. Since arctan x≥x/2 for 0≤x≤1/2 and 1−cos u≥u²/3 for 0≤u≤1, every such λ_n(G) is at least 1/[6(N+π)²]. (The selected t_k≥N≥1.)

For a general β∈(0,1)\{1/2}, let Q have roots β±iT and 1−β±iT. Additivity of λ under multiplication follows from the local logarithm. Expanding its zero sum gives

λ_n(Q)=∑_(j=1)^n (−1)^(j+1) binom(n,j) ∑_ρ ρ^(−j).

The j=1 sum is 2β/(β²+T²)+2(1−β)/((1−β)²+T²)≤2/T². For j≥2 the absolute sum is at most 4/T^j. Consequently, if T≥N and 1≤n≤N,

|λ_n(Q)|≤[2n+2n(n−1)e^(n/T)]/T²≤(2+2e)N²/T².

At T≥10N(N+π), the last expression is less than 1/[12(N+π)²], since 2+2e<100/12. Thus λ_n(GQ)>0. The quartet is off the line, the normalizing constant ensures Q(0)=Q(1)=1, and polynomial multiplication preserves entire order one. This proves L1.

## Statement L2 (matching zero count does not repair finite blindness)

The same assertion holds with a baseline of order one and infinite exponential type whose positive-ordinate zero count is

N_G(T)=T/(2π) log(T/(2π))−T/(2π)+O(1).

For k≥1 let t_k>2πe solve t_k/(2π)[log(t_k/(2π))−1]=k, and use the same paired product as above. Then t_k~2πk/log k, ∑t_k^(−2)<∞, and its positive-ordinate count is the floor of the displayed smooth counting function above the first zero. Paired Li contributions stay strictly positive for every n. The proof of finite-prefix preservation uses the finite minimum m_N>0 and the preceding quartet bound; equivalently choose any t_k≥N and T≥10Nt_k.

For completeness the growth assertion does not follow from symmetry alone. With w=s−1/2 and N(t)=O(t log(t+2)), the product satisfies

log M_G(r)≤C+∫ log(1+r²/t²)dN(t)
 =C+2r²∫ N(t)/[t(t²+r²)]dt=O(r log(r+2)).

The integration begins below the first positive zero, where N=0. Splitting at t=r proves the bound. The exponent of convergence of the zeros is one, so the entire order is at least one and hence exactly one. On the positive real w-axis, use the factors with t≤w/2: their ratios (t²+w²)/(t²+1/4) are at least2 for sufficiently large w (all t_k exceed 2πe). The remaining factors are at least1 when w≥1/2. There are ≍w log w factors in that first group, so log G(1/2+w)≥c w log w−O(1), showing infinite exponential type. Adding four zeros changes the counting function by O(1). This is an optional strengthening, not an assertion that these functions have the other arithmetic properties of ξ.

## Concrete exact test L3

At β=1/4,T=2, write z=(61+32i)/65, z'=(61+32i)/73. Then

λ_n(Q)=4−2 Re[(61+32i)^n](65^(−n)+73^(−n)).

All quantities on the right are exact rationals. The supplied script checks λ_n(Q)≥0 for n=1,…,11, so λ_n(GQ)>0 there. It also establishes λ_91(Q)+364<0 by exact integer/fraction arithmetic.

The bound λ_n(G)≤4n is elementary: with K=ceil(n/π), use each paired contribution ≤min(4,n²/t_k²), and

∑_(k≥K)(k+1/2)^(−2)≤∫_K^∞ x^(−2)dx=1/K

(the integrand is convex, so its integral on [k,k+1] dominates its midpoint value). Hence for n≥2, λ_n(G)≤4K+n²/(π²K)≤5n/π+4≤4n. For n=1 use ∑t_k^(−2)=1/2. Thus λ_91(GQ)<0 is rigorously established without evaluating cosh numerically. Printed decimal values merely illustrate the exact rational bound.

## Why negativity must eventually appear

For β<1/2 set (ρ−1)/ρ=R exp(iθ), ρ=β+iT, so R>1. The paired/reflected quartet contribution is 4−2(R^n+R^(−n))cos(nθ). There are arbitrarily large n with cos(nθ)≥1/2 (periodicity if θ/2π is rational, approximation by integer multiples otherwise). This negative exponential dominates λ_n(G)=O(n), or O(n log n) for the counting-matched baseline. For the latter bound sum min(4,n²/t_k²) using N(t)=O(t log t). This gives an independent reason the finite positive prefix cannot extend forever for this construction.

## Provenance and limitations

The local derivative/zero-sum convention and generic zero-set formulation are established background. Primary source inspected: Jeffrey C. Lagarias, *Li coefficients for automorphic L-functions*, Ann. Inst. Fourier 57(5) (2007), 1689–1740, DOI 10.5802/aif.2311, https://aif.centre-mersenne.org/item/10.5802/aif.2311.pdf, specifically introduction pp.1690–1692, equations (1.1)–(1.8). The source explicitly distinguishes derivative λ̃_n=λ_(−n) before reflection symmetry; this was checked against the proof above. Only this introduction was inspected, not the paper's complete proof architecture. Bombieri–Lagarias 1999, DOI 10.1006/jnth.1999.2392, is acknowledged there as the general criterion's source, but author-host PDF could not be reliably read in this campaign (403 locally, garbled web extraction); no audit of that paper is claimed.

This construction is elementary negative knowledge, not a claimed publishable discovery. It supplies no Euler product, arithmetic Dirichlet series, prescribed gamma factor, explicit prime formula, or the exact local coefficients of Riemann ξ. It therefore neither refutes Li's criterion nor establishes insufficiency of a particular finite ζ computation combined with additional rigorous ζ-specific bounds. It rules out only universal arguments based on the listed generic properties and a finite positive prefix.

Next precise question: specify an explicit ζ-specific inequality controlling the tail of Li coefficients, strong enough to exclude the quartet mechanism. Any such proposal should be stress-tested on this family to identify exactly where arithmetic is used. No author error is alleged.

## Revision log

2026-11-17: Parent review corrected the L2 growth lower-bound proof: normalization means the ratio at t=w is slightly below2, so the count must use t≤w/2, with the remaining factors≥1. The order/infinite-type conclusion is unchanged. This was a proof-exposition correction to an intermediate inequality, not a mathematical error in a published source.

2026-11-17: Parent adjudication independently checked the core construction and accepted the repaired L2 bound. The main status is now parent-adjudicated elementary mathematics; this does not upgrade the source-paper reading level or establish novelty.
