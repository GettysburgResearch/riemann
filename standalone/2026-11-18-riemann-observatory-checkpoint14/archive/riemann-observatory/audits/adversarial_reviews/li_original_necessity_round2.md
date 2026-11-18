# Independent reconstruction of Li's original necessity proof

Reviewer: li_advocate. Date:2026-11-17. Primary-source passage inspected: Xian-Jin Li, *The Positivity of a Sequence of Numbers and the Riemann Hypothesis*, J.Number Theory65(2)(1997),325–333, DOI10.1006/jnth.1997.2137, specifically Theorem1 and its proof pp.325–328. Access was the reproduced primary article text at https://paperzz.com/doc/7086946/--science-direct, whose mathematical extraction is degraded; a publisher-quality PDF was not obtained by this reviewer. This is a targeted source/proof reconstruction, not a whole-paper audit of the Dedekind part. The2007 Lagarias introduction is not substituted for the original proof.

## Original architecture independently checked

Use Li's normalization Ξ(s)=s(s−1)π^(−s/2)Γ(s/2)ζ(s), so Ξ(0)=Ξ(1)=1. It differs by a constant factor from the frequently used ξ; this does not alter Li derivatives. Put φ(z)=Ξ(1/(1−z))=1+∑_(j≥1)a_j z^j. Entire Ξ makes φ analytic in the open unit disk independently of RH.

The positive coefficients come from the theta-integral representation used in original Eq(1.2). With ψ(x)=∑_(n≥1)exp(−πn²x), the kernel

K_theta(x)=[x^(3/2)ψ'(x)]'
 =πx^(1/2)∑_(n≥1)n²(πn²x−3/2)exp(−πn²x)

is strictly positive for x≥1. The representation is

Ξ(s)=4∫_1^∞ K_theta(x)[x^((s−1)/2)+x^(−s/2)]dx.

Here is a direct coefficient reconstruction of the positivity step. Let u=z/(1−z), A=(logx)/2, b=x^(−1/2). The bracket after substituting s=1+u is exp(Au)+b exp(−Au). Its z^j coefficient, j≥1, is

∑_(n=1)^j binom(j−1,n−1)A^n[1+(−1)^n b]/n!,

strictly positive for x>1. Multiplying by the positive kernel and integrating proves a_j>0. This finite coefficient sum is consistent with the original Eqs(1.5)–(1.6). Differentiation/coefficient extraction under the integral is justified on every compact |z|≤r<1: the substituted s is bounded there, while the theta kernel decays exponentially in x and dominates every required polynomial/logarithmic factor.

Near0, the derivative definition gives φ'/φ=∑_(n≥1)λ_n z^(n−1). Comparing φ'=φ·(φ'/φ) gives

n a_n=∑_(j=1)^n λ_j a_(n−j), a_0=1.

If **every** λ_j≥0, then0≤λ_n≤n a_n for every n. Since ∑n a_n r^(n−1)=φ'(r)<∞ for every0≤r<1, the full logarithmic-derivative coefficient series is absolutely convergent throughout the disk. Denote it L(z). The local identity φ'=Lφ then holds throughout the disk by analytic continuation. The initial value φ(0)=1 and the analytic differential equation imply φ(z)=exp(∫_0^zL(w)dw), hence φ is zero-free there.

The Möbius map sends the disk exactly onto Re(s)>1/2. Thus no Ξ zero lies in that half-plane; functional symmetry excludes off-line zeros on the other side. This validates the original positive-coefficient domination argument. Pringsheim's theorem or an extremal finite-root argument is not needed for this proof route.

For the zero-sum convention, differentiating an individual log(1−s/ρ) at s=1 contributes1−(1−1/ρ)^(−n), whereas the original reflected formula uses the positive power. These coincide after pairing{ρ,1−ρ}, since w_(1−ρ)=1/w_ρ for w_ρ=1−1/ρ: the two terms merely swap within each finite pair. Pair contributions are O_n(|Imρ|^(−2)); the order-one zero count makes the paired series absolutely convergent. This is not an assertion of individual absolute convergence of the original genus-zero factors. The RH-to-positivity direction then gives line-pair contributions2[1−cos(nθ)]≥0. Neither direction supplies a finite-prefix criterion.

## Strengthening of the finite-prefix campaign

The campaign's generic countermodels retain even the original proof's positive-a_j structure. Let

F(s)=cosh(s−1/2)/cosh(1/2)·Q_T(s), T≥1/4,

where Q_T is the normalized quartet factor with roots1/4±iT,3/4±iT. For w=s−1/2,

Q_T(s)=[w^4+2(T²−1/16)w²+(T²+1/16)²]/D_T,

with D_T>0. All polynomial coefficients in w are nonnegative. Under s=1/(1−z), w=1/2+z/(1−z) has nonnegative Taylor coefficients. Hence Q_T composed with the Möbius map has nonnegative coefficients and constant1.

The composed normalized cosh has strictly positive coefficients: with u=z/(1−z), the coefficient of u^k is [exp(1/2)+(−1)^k exp(−1/2)]/[2cosh(1/2)k!]>0 for k≥1, and composition with u preserves positivity. Their product therefore has a_j>0 for every j≥1.

In particular the exact T=2 example already proved in `li_advocate.md` has all these positive a_j, the first11 Li coefficients positive, and λ_91<0. The arbitrary-N construction uses still larger T and retains the same property. These are real symmetric entire order-one examples with normalized endpoints and zeros confined to the critical strip; they lack ζ's arithmetic conditions.

This does not challenge Li's theorem. It identifies the precise indispensable quantifier: finitely many λ inequalities dominate only finitely many logarithmic-derivative coefficients. Even positivity of every a_j does not extend that domination to the unchecked tail or exclude zeros in the disk. No novelty is claimed for this elementary strengthening or for the known Li criterion.

Classification: original Theorem1 necessity independently reconstructed with no issue found in the inspected argument, subject to the stated degraded-source access limitation. The generic finite-prefix countermodel's additional positive-coefficient property follows by explicit polynomial/exponential algebra and awaits any further reviewer the parent chooses.
