# Positive Bessel kernels with exactly four off-line zeros

Campaign: li_advocate, round3. Date:2026-11-17. Status: independent analytic reconstruction; parent review pending. Novelty is unassessed. The Bessel base and its spectral interpretation are classical. This is a generic-function obstruction and test fixture, **not a statement about RH or an arithmetic L-function**.

## Exact construction and stronger retained properties

Set c=2π,a=1/4, f(u)=exp(−c cosh(2u)), and

A(w)=∫_R exp(wu)f(u)du=K_(w/2)(c),
Q_T(w)=[(w−a)²+T²][(w+a)²+T²]
      =w⁴+2(T²−a²)w²+(T²+a²)²,
F_T(s)=A(s−1/2)Q_T(s−1/2)/[A(1/2)Q_T(1/2)].

For T≥32 this is real entire of exact order1 and infinite exponential type, symmetric under s↦1−s, positive on the real axis, and normalized F_T(0)=F_T(1)=1. It has a strictly positive even C∞ double-exponentially decreasing Laplace kernel. **All its zeros are simple. Exactly four zeros are off the critical line:** s=1/4±iT,3/4±iT. Every other zero lies on Re(s)=1/2.

Its positive-ordinate zero count, with multiplicity, is

N_T(U)=U/(2π)log[U/(2πe)]+O(1), U→∞.                       (B1)

In particular the error is O(1), stronger than merely O(logU), but no prime-side explicit formula or arithmetic completion is inferred. For every integer N≥1 the explicit choice

T_N=10N(8N²+50)                                             (B2)

makes λ_n(F_(T_N))>0 for1≤n≤N. T may be increased further to exceed any prescribed finite zero-verification height, preserving these bounds. Every positive-degree Taylor coefficient of F_T(1/(1−z)) is positive as well.

The missing arithmetic condition is demonstrated, not merely listed: dividing F_T by the standard Riemann completion produces a function growing like a positive constant times s^(7/4) as real s→+∞. It cannot be an ordinary Dirichlet series absolutely convergent in any right half-plane.

## 1. Bessel identity, domain and entire order

DLMF10.32.9 gives K_ν(c)=∫_0^∞exp(−c coshv)cosh(νv)dv for c>0. Substitution v=2u gives exactly the displayed bilateral integral, with no missing factor2. The double-exponential decay allows differentiation in w and integration by parts to every finite order, uniformly on compact w-sets; A is even, real entire and positive for real w.

For |w|≤r, |A(w)|≤A(r). Since cosh(2u)≥exp(2|u|)/2,

A(r)≤(2/c)^(r/2)Γ(r/2), r>0,

after extending the corresponding positive gamma integral to0. Thus logM_A(r)=O(rlogr) and the order is at most1. The strictly positive kernel has mass on arbitrarily distant intervals, so A(r)≥p_L exp(Lr) for every fixed L>0 with p_L>0. Therefore logA(r)/r→∞. The order is exactly1 and the exponential type is infinite. Polynomial multiplication and positive normalization retain both facts.

## 2. All complex order zeros are imaginary: a genuine self-adjoint argument

On L²(0,∞) take the Dirichlet Schrödinger operator

H=−d²/dx²+c²exp(2x), y(0)=0,

defined by its closed positive quadratic form. The increasing confining potential gives compact resolvent: on a bounded interval use Rellich compactness, and outside it the potential bounds the L² tail uniformly. The eigenvalues E_j are positive, discrete and simple.

If K_ν(c)=0, then y(x)=K_ν(c expx) solves

Hy=−ν²y.

The fixed-order large-positive-argument asymptotic K_ν(z)~sqrt(π/(2z))exp(−z), or direct differentiation of its convergent integral, puts y in the operator domain, including the Dirichlet condition and rapid decay. Self-adjointness forces −ν² to be real positive. Hence ν is purely imaginary and nonzero. In fact E_j>c², so |Imν|>c. This excludes **all** complex off-axis order zeros, not merely a numerical selection of real ν-zeros.

Conversely each eigenfunction is proportional to the unique decaying K solution, so all eigenvalues occur this way. Simplicity as an entire-function zero also follows: write y(x,E)=K_(i sqrtE)(c expx), analytic in E because K is even in its order. At an eigenvalue E_0, differentiating(H−E)y=0 and applying the Lagrange identity gives

∫_0^∞y(x,E_0)²dx=−y_x(0,E_0)y_E(0,E_0).

The derivative y_x(0,E_0) is nonzero by ODE uniqueness and the integral is positive; hence y_E(0,E_0)≠0. Since E↦ν has nonzero derivative there, the zeros in ν and w are simple. The four zeros of Q_T are simple and have nonzero real parts, so they cannot coincide with a Bessel zero. This proves the all-simple assertion for F_T.

## 3. Rigorous O(1) zero count without relying on WKB precision

For fixed c>0, the exact I-Bessel series and connection formula give

I_(iτ)(c)=(c/2)^(iτ)/Γ(1+iτ) · A_c(τ),
A_c(τ)=∑_(k≥0)(c²/4)^k/[k! (1+iτ)_k],
K_(iτ)(c)=−π Im I_(iτ)(c)/sinh(πτ), τ>0.

Since |(1+iτ)_k|≥τ^k,

|A_c(τ)−1|≤exp(c²/(4τ))−1,
|A_c'(τ)|≤[c²/(4τ²)]exp(c²/(4τ)).

The derivative estimate follows by differentiating each denominator and bounding the sum of k reciprocal factors by k/τ; the resulting series is absolutely uniformly dominated on every sufficiently large τ range. Thus A_c is nonzero for all sufficiently large τ and its principal argument is O(1/τ), with derivative O(1/τ²).

Stirling's log-gamma/digamma expansions then give a continuous phase

θ(τ)=τlog(c/2)−Im logΓ(1+iτ)+argA_c(τ)
    =−τlog[2τ/(ec)]−π/4+O(1/τ),
θ'(τ)=log[c/(2τ)]+O(1/τ²)<0

for all sufficiently large τ. The K zeros are exactly θ(τ)∈πZ there. Monotonicity gives one zero per phase crossing, so

# {0<τ_j≤R}=R/π log[2R/(ec)]+O(1).

The finite initial segment changes only the bounded constant. As w=2iτ, the positive w-ordinate count is U/(2π)log[U/(ec)]+O(1). At c=2π this is precisely the two smooth Riemann–von Mangoldt terms. Multiplication by Q_T adds2 positive-ordinate zeros at heightT, hence only a bounded change. Endpoints do not affect the O(1) assertion.

The primary2021 physical treatment uses a quasiclassical quantization approximation. It supplies context and the ODE connection, but its numerical/WKB precision claim is **not** used as a rigorous premise for(B1). The exact series bounds and monotone phase above provide the needed justification independently.

## 4. Multiplying by Q_T retains a strictly positive kernel

Repeated integration by parts gives the kernel

g_T=f''''+2(T²−a²)f''+(T²+a²)²f,

whose bilateral Laplace transform is A(w)Q_T(w). All boundary terms vanish by double-exponential decay, including at complex w on compact sets. Put x=cosh(2u)≥1. Exact differentiation gives

f''/f=4c²(x²−1)−4cx≥−4c>−28,
f''''/f=16[c⁴(x²−1)²−6c³x(x²−1)+c²(7x²−4)−cx].

For x≥2, the first two terms in brackets have nonnegative sum because c>6 and x²−1≥x; the remaining terms have positive sum. For1≤x≤2, discard the positive terms and bound the negative ones to obtain

f''''/f≥−576c³−32c>−197792,

using6<c<7. Hence for T≥32,

g_T/f≥T⁴−56T²−197792>0.

At32 the final polynomial is793440; its derivative4T(T²−28) is positive thereafter. This proves kernel positivity on the entire real line, not only on a plotted compact range. The kernel is even and C∞, and its derivatives are polynomials in hyperbolic functions times f, retaining double-exponential decay. Normalizing by its positive mass gives a strictly positive even probability density if desired; normalizing its Laplace transform at w=1/2 gives F_T as defined.

## 5. An explicit finite Li-positive prefix

The order-one even baseline with all simple imaginary w zeros has the canonical product

A(w)=A(0)∏_j(1+w²/γ_j²),

where γ_j=2sqrt(E_j)>0 and ∑γ_j^(−2)<∞. Hadamard permits only a linear exponential factor; evenness forces its linear coefficient to vanish. Thus the normalized baseline in s has a normally convergent paired zero product and its Li coefficients are sums of2[1−cos(nθ_j)]≥0. Infinitely many zeros make each coefficient strictly positive.

For an explicit uniform lower bound, choose j=N²+1. The comparison exp(2x)≥4x² gives

E_j≥2c(4j−1),

using the odd half-line harmonic oscillator eigenvalues. The j-dimensional trial space of sine modes on[0,1], extended by0, gives

E_j≤π²j²+c²e².

Both are standard min–max form comparisons and require no information about ζ. Consequently

N≤γ_j<8N²+50=:G_N,

using π<4,c<7,e<3. The single paired factor at γ_j therefore supplies

λ_n(baseline)≥1/(6G_N²), 1≤n≤N,

by θ_j=2atan(1/(2γ_j)), nθ_j≤1, θ_j≥1/(2γ_j), and1−cosu≥u²/3 on[0,1].

The added quartet has s-roots1/4±iT,3/4±iT. Its Li contribution, for T≥N, is bounded by

|λ_n(Q_T)|≤(2+2e)N²/T²<8N²/T², 1≤n≤N.

This follows by expanding the symmetric zero sum: the first reciprocal sum is≤2/T² and the higher sums are bounded in absolute value by4/T^k. Normalization constants do not affect Li derivatives. At the explicit T_N in(B2), the perturbation is less than1/(12G_N²). The baseline margin therefore remains positive. Increasing T only improves the bound and kernel positivity, so any fixed finite-height zero check can simultaneously be preserved.

The positive Laplace kernel also gives all positive-degree Taylor coefficients of F_T(1/(1−z)): write s−1/2=1/2+z/(1−z) and expand paired exponentials under the positive even integral. This is the original Li positive-coefficient structure; positivity of the unchecked infinite Li tail is still absent.

## 6. An explicit failure of the ordinary Dirichlet-series axiom

Define the putative uncompleted function using exactly the standard Riemann completion,

L_model(s)=F_T(s)/[(1/2)s(s−1)π^(−s/2)Γ(s/2)].

For real ν→+∞, the exact gamma integral for K gives

K_ν(2π)~(1/2)Γ(ν)π^(−ν).

For example, the relative error is bounded byπ²/(ν−1) for ν>1 using0≤1−exp(−π²/t)≤π²/t in the gamma integral. With ν=s/2−1/4 and Q_T(s−1/2)~s⁴, gamma-ratio Stirling yields

L_model(s)~C_T s^(7/4), C_T>0.

Thus it is unbounded on the positive real axis. An ordinary Dirichlet series∑a_n n^(−s) absolutely convergent in a right half-plane instead tends to its finite coefficient a_1 as real s→∞, by dominated convergence. Hence L_model cannot be such a series. This precise obstruction shows why the generic countermodel does not meet ζ's arithmetic axioms, despite its strong analytic similarities.

For each fixed σ>1/2, its off-line zero count is O(1). This is compatible with asymptotic density upper bounds that allow finitely many exceptional zeros; it is not a claim to reproduce every published numerical constant or every other ζ property.

## Source fidelity, reproducibility and scope

Inspected official identities: DLMF10.25.1–3 (equation, I series, fixed-order decaying K solution),10.27.3–4 (evenness and connection formula),10.32.9–10 (integrals). The fixed positive argument c avoids all argument-branch cuts. The count's gamma/digamma Stirling input is classical and explicitly separated from the rigorous I-series bounds.

Actual primary papers accessed: Krynytskyi–Rovenchak, arXiv2103.01732v2, SIGMA17(2021),057, DOI10.3842/SIGMA.2021.057, all7 pages substantively read; and R.B.Paris, arXiv2204.09306v1, pp.1–4 inspected for the exact I expansion and phase approach. The latter is a partial-source inspection, not a whole-paper reading. Local copies/hashes and records are preserved; copyrighted PDFs/full extracted text are excluded from distribution. The underlying order-zero and spectral phenomena are established prior mathematics, not newly attributed to this campaign.

`experiments/code/bessel_countermodel_round3.py` supplies exact polynomial differentiation checks, the global positivity threshold and finite-prefix margin inequalities. A separate output records nonvalidated high-precision Bessel/phase/growth observations. Neither numerical agreement nor the WKB approximation replaces the analytic proof. Parent independent review and a complete priority search remain outstanding before any publication-level novelty claim.
