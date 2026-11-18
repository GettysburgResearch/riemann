# PAPER-A001 — Guth–Maynard: large values and zero density

**Source:** Larry Guth and James Maynard, *New large value estimates for Dirichlet polynomials*, arXiv:2405.20552v2 (7 April 2026); first version 31 May 2024. Published Annals of Mathematics 203 (2026), issue 2, 623–675. [arXiv](https://arxiv.org/abs/2405.20552v2), [publisher](https://annals.math.princeton.edu/2026/203-2/p06). Accessed 17 November 2026. PDF downloaded; whole-work L1 is **not** claimed. Inspected §§1–3, §4.1, definition (7.2), §13.1–13.2. Version differences not exhaustively compared.

## Results and notation

For coefficients |b_n|≤1 and 1-separated t_r∈[0,T] satisfying |Σ_{N≤n≤2N} b_n n^{it_r}|≥V, Theorem 1.1 gives

R ≤ T^{o(1)}(N²V^{-2}+N^{18/5}V^{-4}+TN^{12/5}V^{-4}).

The useful improved range is around V=N^{3/4}; the statement does not uniformly supersede every previous large-value estimate. Theorem 1.2 (p2) counts zeros with Reρ≥σ and |Imρ|≤T and gives, in the critical strip,

N(σ,T) ≤ T^{15(1−σ)/(3+5σ)+o(1)}.

Combining Ingham for σ≤7/10 produces the envelope T^{30(1−σ)/13+o(1)}. These are asymptotic estimates with unspecified o(1) and implied effectiveness; they are not ready-made explicit numerical bounds. For each fixed ε>0, Corollary 1.3 treats x^{17/30+ε}≤y≤x^{0.99}; translating a density exponent to primes also uses a Vinogradov–Korobov zero-free region and a version with logarithmic losses controlled near σ=1 (§13.2, (13.3)). Omitting those extra inputs would overstate what follows from the displayed fixed-σ theorem alone.

## Proof architecture and inspected checks

Large values → top singular value of M_W, entries w(n/N)n^{it} (§4 Lemma4.1) → trace moments and Poisson decomposition into S1,S2,S3 → cancellation along affine transformations in S3 → Proposition3.1 → subdivision and separated-subset reduction → Theorem1.1. Zero detector splits Type I/II zeros; raising Dirichlet polynomials to bounded powers and balancing with the mean-value theorem yields Theorem1.2 (§13.1 pp48–50). Fixed coefficients may acquire divisor-bound T^{o(1)} losses under powers; these cannot be ignored in an explicit computation.

Independent exact arithmetic checks: at σ=3/4 the density exponent is 5/9; at σ=7/10 it is 9/13; at σ=4/5 it is 3/7. The exponent algebra in §13.1 is compatible with the stated envelope. This is not an audit of the difficult S3 estimate.

## Precise frontier

The authors identify their envelope bottleneck in the final remark of §13.1, p50: σ=7/10, detector length N=T^{5/13}, apply the square (length T^{10/13}), subdivide into T1=T^{12/13}, |W|≈T1^{2/3}, E(W)≈|W|^{5/2}≈|W|⁴/T1. S1 and S2 are tight there, so within this proof an improvement must improve S3. Here R(v)=Σ_{t∈W}|v|^{it}, (7.2); a difficult concentration is near rationals of numerator/denominator size T1^{1/3}. This is a concrete transplant target for incidence/additive-combinatorial tools, not evidence such a transplant works.

**Next task:** reproduce Proposition9.1 and its sharpness example, isolate the exact S3 loss at these scales, then either prove a power saving under a precisely quantified exclusion of rational concentration or construct a near-extremizer. A result only for generic W does not prove a universal large-value theorem.

**Limitation:** this density theorem does not imply the BGSTB strong-density assumption needed for their conditional 61.7% simplicity theorem; see CONN-A001. No claim of an error or new theorem.
