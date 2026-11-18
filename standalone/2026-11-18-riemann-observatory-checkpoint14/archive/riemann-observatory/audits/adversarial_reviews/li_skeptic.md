# Independent skeptic review: finite Li positivity

Reviewer: independent skeptic agent. Date: 2026-11-17. No advocate draft was read before this reconstruction. Status: **independently checked, with no issue found in the explicit finite-prefix construction**. This is an elementary obstruction in a broad class of entire functions, not a theorem about the arithmetic Riemann xi-function. No novelty is claimed.

## Proposition checked

For every integer N≥1 and every a>0, there is a real entire function F of order exactly one, positive on the real axis, satisfying F(s)=F(1-s), F(0)=F(1)>0, having zeros off Re(s)=1/2 within 0<Re(s)<1, and whose first N Li derivatives are strictly positive:

λ_n(F) = (1/(n−1)!) (d^n/ds^n)[s^(n−1) log F(s)] at s=1 >0, 1≤n≤N.

A local real logarithm near s=1 suffices. A multiplicative positive constant has no effect on λ_n. The construction also preserves simplicity of all zeros if the inserted quartet avoids the baseline zeros.

## Reconstruction from scratch

Let B(s)=cosh(a(s−1/2)), with zeros ρ_k=1/2+iγ_k and conjugates, γ_k=(k+1/2)π/a, k≥0. Its exact paired product is

B(s)/B(0) = product over k≥0 of [((s−1/2)^2+γ_k^2)/(1/4+γ_k^2)].

Each factor equals (1−s/ρ_k)(1−s/conj(ρ_k)). The paired factors differ from 1 by O_R(γ_k^−2) on every bounded s-domain, so the product and the local logarithmic derivatives used below converge locally uniformly away from zeros. No unaccounted exponential factor is introduced.

Define θ_k=2 arctan(1/(2γ_k))∈(0,π). Then

λ_n(B) = sum over k≥0 of 2[1−cos(nθ_k)].

This is absolutely convergent for each n: θ_k≤1/γ_k and 2(1−cos(nθ_k))≤n²/γ_k². Every summand is nonnegative. For any fixed n, sufficiently large k has 0<nθ_k<2π and hence a strictly positive summand. Thus λ_n(B)>0 for every n. Set m_N=min_{1≤n≤N} λ_n(B)>0.

Fix β∈(1/2,1), for example β=3/4, and T>0. Let

P_T(s)=[(s−β)^2+T²][(s−(1−β))²+T²], Q_T(s)=P_T(s)/P_T(0).

Then Q_T(0)=Q_T(1)=1, Q_T(s)=Q_T(1−s), and Q_T is positive on the real axis. Its four roots are β±iT and 1−β±iT, all off the critical line. For F_T=BQ_T, realness, symmetry, positivity on the real axis and order exactly one follow immediately.

For any root ρ, direct differentiation gives

λ_n(s−ρ)=1−[ρ/(ρ−1)]^n.

This follows, for example, from log[(1/(1−z))−ρ] = constant + log[1−(ρ/(ρ−1))z]−log(1−z), whose z^n coefficient is λ_n/n. This sign convention matters: the familiar sum 1−(1−1/ρ)^n uses reflection symmetry to replace the inverse powers. The quartet has that symmetry, so either formula agrees after summation.

Since every quartet root has |ρ−1|≥T,

|λ_n(Q_T)| ≤ (4n/T)(1+1/T)^(n−1).

Here |(1+u)^n−1|≤n|u|(1+|u|)^(n−1). Therefore the bound is at most (4N/T)(1+1/T)^(N−1) for 1≤n≤N. Choose T so this quantity is less than m_N. Then λ_n(F_T)≥m_N−bound>0 for every n≤N. The four off-line roots remain present. This completes the independent proof.

## Skeptical checks and scope limits

* The zero-sum sign issue is real and easily mishandled. It is harmless here because the zero multiset is invariant under ρ↦1−ρ. It would invalidate a rootwise identification without that symmetry.
* A normalized quartic times cosh is entire of order one, but is of finite exponential type and has a linear zero count. It does not have the xi-function's T log T zero count, Euler product, Dirichlet series, gamma factor, or prime explicit formula. The argument does **not** establish a finite-certification impossibility inside the class of genuine zeta or automorphic L-functions.
* It rules out an inference based solely on real entire order-one symmetry and finitely many positive Li derivatives. It does not rule out finite proofs using additional arithmetic identities or a theorem controlling all future coefficients.
* The constructed first N coefficients are positive, not equal to the actual xi-function's coefficients. Exact finite-jet matching would be a separate problem.
* T is allowed to depend on N. No claim is made that one fixed counterexample has all coefficients positive.
* Strict positivity of the baseline is proved for every n; it is not inferred from numerical samples.

## Numerical illustration and independent implementation

Run `python experiments/code/li_skeptic.py` from an environment containing mpmath and numpy. The script computes Li derivatives by a Taylor/Leibniz formula at 120 decimal digits, checks the two quartet formulas independently, and compares the baseline with a paired-zero sum using 100,000 positive zeros. For a=1, β=3/4, T=10000 and N=100:

* minimum baseline coefficient: 0.46211715726000975850231848364367254873028928033011;
* prefix perturbation bound: 0.040397946689046158138386915824707797013218017381455;
* minimum perturbed coefficient: 0.46211717726000967100231896020616987783186679803022.

Results are in `experiments/results/li_skeptic.json`. These are arbitrary-precision numerical checks, **not validated interval arithmetic**. The exact proof above does not depend on their correctness. For the independent zero sum with K pairs, its mathematical remainder is nonnegative and bounded by n²a²/[π²(K−1/2)] for K≥1. Floating-point summation itself is not enclosed by an interval in this experiment.

## Primary-source provenance and prior-art calibration

Bombieri and Lagarias, *Complements to Li's Criterion for the Riemann Hypothesis*, J. Number Theory 77 (1999), 274–287, DOI 10.1006/jnth.1999.2392. Author PDF: https://websites.umich.edu/~lagarias/doc/bombieri.pdf . Accessed 2026-11-17; an appended `?download=1` avoided a local HTTP 403. Its encoded text extraction was unreadable, so manuscript pages 3–5 were rendered and inspected as images. **Only Theorem 1, its proof and Corollary 1 were inspected in this reviewer track; this is not an independent full-paper audit.**

Theorem 1 treats arbitrary zero multisets under a summability hypothesis and uses inverse powers in its half-plane version. Corollary 1 restores the reflection/conjugation symmetries and the usual positive-power criterion. This supports the broad-class context and the requirement that positivity hold for every positive integer, but does not itself establish priority for the exact explicit counterexample above. The finite-prefix construction is best classified as an independently verified explanatory lemma, not a new research discovery. No published mathematical error is alleged.

## Concrete next step

Extend the obstruction to a precisely specified class preserving a Riemann–von Mangoldt counting main term and additional growth constraints, and determine which genuinely arithmetic property blocks such perturbations. Finite polynomial perturbations of a hypothetical on-line xi-like function preserve the leading zero-count asymptotic; however, making that conditional statement into an unconditional arithmetic example would require information not supplied here. A useful certification program must state its uniform tail-control hypothesis explicitly.
