# Positive smooth Laplace kernels with finite Li-positive prefixes and off-line zeros

Campaign: li_advocate, round3. Date:2026-11-17. Status: explicit construction and self-contained analytic reconstruction; parent independent review pending. **Novelty is unassessed. No claim about RH or an arithmetic L-function is made.** The construction is a test family for arguments that use generic entire-function positivity and finitely many Li coefficients.

## The constructed family

Let γ be Euler's constant, H_13=1145993/360360, and

δ_* = H_13/2−γ−1.

The elementary bounds57/100<γ<59/100 imply

241/3603600 < δ_* < 72313/3603600 < 1/26.

These coarse bounds suffice; numerically δ_*≈0.0128512126. The code below certifies the γ bounds by harmonic/logarithmic integral-test enclosures, rather than treating decimal γ as exact.

Set δ_13=δ_* and δ_j=1/(2j) for j≥14. Define the locally uniformly convergent entire product

B_*(w)= [sinh(δ_*w)/(δ_*w)] · ∏_(j≥14) sinh(w/(2j))/(w/(2j)),

with the removable factors at0 assigned value1. For0≤a<1/2 put

C_a(w)=(cosh w+cosh a)/(1+cosh a),
M_a(w)=B_*(w)C_a(w),
F_a(s)=M_a(s−1/2)/M_a(1/2).

Then F_a is real entire, F_a(s)=F_a(1−s), F_a(0)=F_a(1)=1 and F_a(x)>0 for every real x. Every zero is in0<Re(s)<1. For a>0 it has the off-line zeros

s=1/2±a+iπ(2k+1), k∈Z.

Every F_a is of order exactly1 and infinite exponential type. It is the bilateral Laplace transform, up to the positive normalization M_a(1/2), of a strictly positive even C∞ probability density with double-exponential tails. Its positive-ordinate zero count, **with multiplicity**, is

N_a(T)=T/(2π)log(T/(2π))−T/(2π)+O(sqrt(T)).                    (P1)

Only the two displayed smooth main terms are matched. The Riemann–von Mangoldt O(logT) error, arithmetic explicit formula, Euler product and gamma factor are not supplied.

For every integer N≥1 an explicit parameter is

a_N=1/[10(N+88)5^N].

It satisfies0<a_N<1/2 and

λ_n(F_(a_N))>0, 1≤n≤N.                                      (P2)

Every Taylor coefficient of F_(a_N)(1/(1−z)) of positive degree is also strictly positive. Thus the countermodel retains positive smooth even Laplace kernels and the positive-coefficient structure of Li's original proof, as well as the stated entire order and zero-count main terms, while finite Li positivity does not exclude off-line zeros in this generic class.

## 1. Infinite convolution and entire moment-generating function

Let U_j be independent uniform random variables on[−δ_j,δ_j], j≥13. Their means are0 and ∑Var(U_j)=∑δ_j²/3<∞. Therefore their partial sums converge in L² and almost surely to X. One may use L² martingale convergence; alternatively Kolmogorov's maximal inequality on tails, a summable choice of variance-tail thresholds and Borel–Cantelli give an elementary Cauchy proof. No assertion of absolute convergence is made: ∑δ_j diverges.

For a symmetric uniform variable, E exp(wU_j)=sinh(δ_jw)/(δ_jw). On compact w-sets each factor is1+O(δ_j²), so the product converges locally uniformly and has no zeros other than the factor zeros. For real r,

E exp(rU_j)≤cosh(rδ_j)≤exp(r²δ_j²/2).

The last inequality follows termwise from(2k)!≥2^k k!. The same bound at2r gives uniform integrability of the partial-sum exponentials. Consequently B_*(w)=E exp(wX), initially by convergence in probability/UI and then for complex w by the identical argument or analyticity. Every exponential moment of |X| is finite, so differentiation under expectation is valid on compact w-sets.

The factor C_a is itself a probability MGF: an independent Y_a takes values−1,+1 with probability1/[2(1+cosh a)] each, and0 with probability cosh a/(1+cosh a). Hence M_a is the MGF of Z_a=X+Y_a. This explicitly supplies nonnegative kernel weights; multiplying by an arbitrary entire function would not have done so.

## 2. Smoothness, strict positivity and tails

The characteristic function of X is

φ_X(t)=sinc(δ_*t)∏_(j≥14)sinc(t/(2j)), sinc u=sin(u)/u.

For |t|≥28 retain only indices ceil|t|≤j≤floor(2|t|). Their arguments lie in[1/4,1/2]. Alternating Taylor bounds give

0<sinc u≤1−u²/7≤111/112 on that interval.

There are at least |t|/2 such indices. All remaining characteristic factors have modulus≤1. Thus

|φ_X(t)|≤exp(−|t|/224), |t|≥28.                              (P3)

Every polynomial times φ_X is integrable, so Fourier inversion gives a C∞ density p_X, with bounded derivatives. In fact it extends holomorphically to a fixed strip, but no entire-density claim is needed. Symmetry of X makes p_X even and probability makes it nonnegative.

Strict positivity requires an additional argument. The finite sum through j=J has a bounded continuous density positive inside(−A_J,A_J), where A_J=∑_(j=13)^Jδ_j; this is the elementary finite-uniform convolution property. Here A_J→∞, while the remaining independent tail has variance tending to0. Given any real x, choose J so A_J>|x|+1 and P(|tail|<1)>0 by Chebyshev. Convolution with the tail then gives p_X(x)>0. Continuity identifies this convolution density with the Fourier density everywhere, not only almost everywhere. It also proves that the support is all ofR.

The density of Z_a is the positive mixture

p_a(x)=[p_X(x−1)+p_X(x+1)]/[2(1+cosh a)]
       +[cosh a/(1+cosh a)]p_X(x),

hence remains even, strictly positive and C∞. Its characteristic function obeys(P3) because |C_a(it)|≤1.

A stronger tail statement is available. For r≥2 split the product at j≈r. For j≤r use log(sinh(rδ_j)/(rδ_j))≤rδ_j; for j>r use≤(rδ_j)²/2. This gives

log M_a(r)≤(r/2)logr+C r

with a fixed finite C, uniformly for0≤a≤1/2 after enlarging it. Chernoff with r=exp(2x−1−2C) yields

P(|Z_a|≥x)≤2exp(−c exp(2x))

for sufficiently large x and some c>0. Since p_a has a uniformly bounded first derivative, the usual Lipschitz-density estimate transfers this to p_a(x)≤C_1 exp(−c_1 exp(2|x|)) for large |x|: a density value m forces mass at least a constant times m² in a neighboring interval. Thus the kernel has genuinely fast tails, not merely finite moments. Constants are not optimized.

## 3. Exact order and positive-kernel representation

For |w|≤r, |M_a(w)|≤M_a(r). The preceding split gives logM_a(r)=O(rlog(r+2)), hence entire order≤1. Because p_a is positive everywhere, for every A>0 it assigns positive mass to[A,A+1]; therefore M_a(r)≥p_A exp(Ar), and lim_(r→∞)logM_a(r)/r=∞. Thus the type is infinite and the order is at least1, proving order exactly1. This argument does not infer growth solely from a numerical zero plot.

Evenness gives the explicitly positive cosh representation

F_a(s)= [2/M_a(1/2)]∫_0^∞p_a(x)cosh((s−1/2)x)dx.

The double-exponential tail justifies all compact analytic differentiation. If desired, substitute u=exp(2x) and set

W_a(u)=p_a((logu)/2)u^(−3/4)/[8M_a(1/2)], u≥1.

Then F_a(s)=8∫_1^∞W_a(u)u^(−1/4)cosh((s−1/2)logu/2)du, in the same positive-kernel shape as the original Riemann theta formula. W_a is strictly positive, smooth and exponentially decreasing in u. It is not asserted to be a theta series, to satisfy a Jacobi modular relation, or to have an arithmetic Gaussian-lattice expansion. Those omitted structures are substantive.

## 4. Exact zero count and calibration

For the unmodified product ∏_(j≥1)sinh(w/(2j))/(w/(2j)), positive zeros have ordinates2πjn. With X=T/(2π), the count is exactly

D(X)=∑_(j≥1)floor(X/j).

The elementary Dirichlet hyperbola identity D(X)=2∑_(j≤sqrtX)floor(X/j)−floor(sqrtX)² gives

D(X)=XlogX+(2γ−1)X+O(sqrtX).

Remove factors j=1,…,13, add δ_*, and then multiply by C_a. For a=0 its odd-π zeros are double; for a>0 they split into two equal-height off-line zeros. In either case the multiplicity count is exactly

N_a(T)=D(X)−∑_(j=1)^13floor(X/j)+floor(2δ_*X)+2floor(X+1/2).   (P4)

Since2δ_*=H_13−2γ−2, the linear coefficient is

(2γ−1)−H_13+2δ_*+2=−1,

proving(P1). The modified baseline alone has linear coefficient−3 before C_a contributes2X. This checks the sign and size of every correction.

More precisely, if Δ_D(X)=D(X)−XlogX−(2γ−1)X, then

N_a(T)−[XlogX−X]=Δ_D(X)+E(X), −2≤E(X)≤14.

Thus the construction retains the divisor remainder up to a bounded floor correction. It does not manufacture the finer Riemann–von Mangoldt remainder. Coincident factor zeros, including any unproved arithmetic property of γ, cause no problem because all counts use multiplicity; no irrationality of γ is assumed.

## 5. Initial Li positivity and a constructive parameter

At a=0 every zero is on Re(s)=1/2. The standard sine/cosh products express F_0 as a normally convergent product of normalized paired factors

[((s−1/2)²+τ²)/(1/4+τ²)],

with their actual multiplicities. The sum of τ^(−2) converges, either directly from the double product or from(P1). Therefore logarithmic derivatives near s=1 can be interchanged with the paired product. A line pair contributes2[1−cos(nθ_τ)]≥0, where θ_τ=2atan(1/(2τ)). Every n has a strictly positive contribution from a sufficiently high zero.

A uniform finite-prefix lower bound is simple. The retained j=14 factor has zeros τ=28πk. Choose k=ceil(N/(28π)); then N≤τ<N+88 using π<22/7. For1≤n≤N, nθ_τ≤1, θ_τ≥1/(2τ), and1−cosu≥u²/3 on[0,1]. Hence

λ_n(F_0)≥1/[6(N+88)²].                                     (P5)

Let η=cosha−1. Changing a only changes log(cosh(s−1/2)+cosha), up to constants that do not affect Li derivatives. On |s−1|≤1/4, Re(cosh(s−1/2)+1)>1, and for0≤a≤1/2 one has η≤a²<1/2. Thus

G_a(s)=log[1+η/(cosh(s−1/2)+1)]

is analytic there with |G_a|≤2η. Cauchy bounds its Taylor coefficient of(s−1)^k by2η4^k. The derivative definition gives

|λ_n(F_a)−λ_n(F_0)|≤8nη5^(n−1).                             (P6)

For a=a_N=1/[10(N+88)5^N], the right side for n≤N is strictly less than1/[12(N+88)²], since N≤5^(N−1). Combining(P5)–(P6) proves(P2) with a strict positive margin. This is an explicit rational choice, not an existence claim based on unperformed numerical continuity tests.

Finally the positive cosh integral implies every positive-degree Taylor coefficient of F_a(1/(1−z)) is strictly positive: write s−1/2=1/2+z/(1−z), expand the paired exponentials, and note exp(x/2)+(−1)^k exp(−x/2)>0 for x>0. Compact analytic domination follows from all exponential moments. This exactly retains the positive-coefficient ingredient of the original Li proof, while its infinite λ-positivity hypothesis is still absent.

## Reproducibility, provenance and limitations

`experiments/code/positive_kernel_round3.py` certifies δ_*>0 with exact integer/rational logarithmic enclosures, checks the explicit finite-prefix perturbation inequalities, and brackets(P4) with rigorous γ intervals at X=100,10^4,10^6,10^8. It does not pretend to evaluate the infinite kernel or all Li coefficients numerically. Divisor counts are exact hyperbola sums; intervals are reported where γ uncertainty leaves a floor undecided. The analytic proof supplies the asymptotic, smoothness and all-N assertions.

Primary divisor provenance inspected: Titchmarsh/Heath-Brown, *The Theory of the Riemann Zeta-Function*,2nd ed., §12.1, printed pp.312–313, Eqs12.1.1–12.1.2 and the hyperbola derivation, in the downloaded Rutgers scan. This was a targeted passage reading, not a whole-monograph audit. The count argument above is independently reproduced.

The classical infinite-convolution literature search located B.Jessen and A.Wintner, *Distribution functions and the Riemann zeta function*, Trans.AMS38(1)(1935),48–88, DOI10.1090/S0002-9947-1935-1501802-5. Direct AMS full-text attempts returned403; no audit of that article is claimed. Its bibliography is relevant provenance for infinite convolutions, not evidence that this exact model is new or already in that paper. Basic martingale/Fourier probability tools used above are standard external foundations, with their application explicitly reconstructed. Exact priority for the model/calibration remains unsearched.

This model has many repeated line zeros and divisor-type fluctuation. It supplies no Euler product, exact zeta coefficients, prime-side explicit formula, prescribed gamma factor, Poisson/Jacobi theta relation, or Riemann–von Mangoldt logarithmic error. It cannot be used to infer anything about RH's truth. Its useful conclusion is narrower: these generic positivity/order/density properties plus finitely many Li inequalities are insufficient, so a proposed certificate must identify the additional arithmetic or infinite-tail input it uses.
