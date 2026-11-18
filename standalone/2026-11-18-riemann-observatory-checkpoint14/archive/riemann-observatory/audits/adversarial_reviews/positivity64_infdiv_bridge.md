# Finite positivity tests for the Nakamura–Suzuki criterion

17 November 2026. Source basis is the complete five-page arXiv v1, especially Theorems 1.1–1.2, Lemma 2.2 and the appendix. The entire-function countermodel below preserves the hypotheses used by the transform argument. Publication priority is unassessed. [Inspected primary text](https://arxiv.org/abs/2306.08317v1)

## Exact criterion and the role of positivity

Write $E(z)=\xi(1/2-iz)$. The even real function $g_\zeta$ is defined arithmetically in equation (1.5). By (1.7) and the appendix,
$$
g_\zeta(t)=\sum_\gamma \frac{m_\gamma}{\gamma^2}(e^{-i\gamma t}-1),
$$
where the sum runs over distinct zeros of $E$ and $m_\gamma$ is the multiplicity. The order-one property gives `Σ mγ/|γ|² < ∞`. The strip bound on imaginary parts gives absolute convergence uniformly on compact real $t$-intervals. Under RH the measure `Σ (mγ/γ²) δ₋γ` is finite and positive, and $e^{g_\zeta}$ is its compound Poisson characteristic function. In particular it is infinitely divisible, so every $e^{c g_\zeta}$, $c>0$, is a characteristic function.

The converse in §2 uses only $g_\zeta(t)\le0$ for every $t$, which follows from the characteristic-function bound `|eᵍ|≤1`. The one-sided transform for `Im z > 1/2` equals
$$
 \int_0^\infty g_\zeta(t)e^{izt}\,dt
 =\frac{1}{z^2}\frac{\xi'}{\xi}(1/2-iz)=\frac{i}{z^2}\frac{E'(z)}{E(z)}.
$$
An everywhere nonpositive $g_\zeta$ has a singularity on the positive imaginary axis if its Laplace abscissa is positive, by the fixed-sign Laplace singularity theorem cited in the source. The logarithmic derivative is regular there, since ξ has no positive real zeros. The transform is therefore holomorphic throughout the open upper half-plane, ruling out a zero of $E$ there. Evenness then rules out a lower-half-plane zero. Thus global $g_\zeta\le0$, global positive definiteness of $e^{g_\zeta}$, and infinite divisibility of its characteristic law are each equivalent to RH. For positive definiteness, use the continuity of $g_\zeta$, $g_\zeta(0)=0$, and Bochner’s theorem. [Primary text, §§1–3](https://arxiv.org/pdf/2306.08317v1)

## Countermodel for bounded sign tests and prescribed finite Bochner matrices

Fix a real bound $H>0$, any finite collection of grids of distinct real points `t₁,…,tᵣ` and any $a\in(0,1/2)$. Choose $b>0$ so that `e^{ib tᵢ}` are distinct within each grid. The exclusions on $b$ form a countable set. Use the even, real-entire model
$$
 E_0(z)=\frac{\sin(\pi z/b)}{\pi z/b}
       \frac{\sin(\pi z/(b\sqrt2))}{\pi z/(b\sqrt2)},\qquad
 E_T(z)=E_0(z)\left(1-\frac{z^2}{(T+ia)^2}\right)
                  \left(1-\frac{z^2}{(T-ia)^2}\right),\qquad T>a.
$$
Both have order exactly one. Both equal 1 at zero and are strictly positive on the imaginary axis, where each sine quotient is a positive hyperbolic sine quotient and the polynomial is an absolute square. The coordinate change `Ξ_T(s)=E_T(i(s−1/2))` thus gives a real-entire function satisfying `Ξ_T(s)=Ξ_T(1−s)`, positive on the real axis. All zeros are in `|Im z|≤a`, equivalently `|Re(s)−1/2|≤a`. The added simple quartet `±(T±ia)` can be placed beyond any fixed height. The same Hadamard logarithmic-derivative identity holds for the associated $g_T$ by termwise integration for `Im z>a`, since $E_T$ has even genus-one factorization and the inverse-square zero sum converges.

For $g_0$ use the same inverse-square weights as in (1.7). It is always nonpositive and strictly negative for every real $t\ne0$, since the two sine lattices have no common nonzero period. A single pair of zeros yields $g_0(t)\le-c_0 t^2$ near zero for some $c_0>0$. Continuity and strict negativity then give $g_0(t)\le-c_H t^2$ on `|t|≤H` for some $c_H>0$. The quartet perturbation is
$$
 q_T(t)=g_T(t)-g_0(t)=4\Re\frac{\cos((T+ia)t)-1}{(T+ia)^2}.
$$
If $A+iB=(T+ia)^{-2}$, then $A>0$, $A=O(T^{-2})$, and `|B|=Oₐ(T⁻³)`. Using `|sin(Tt)|≤T|t|`, one obtains the upper bound
$$
 q_T(t)\le 4A(\cosh(at)-1)+4|B|T|t|\sinh(a|t|)
          \le C_{a,H}T^{-2}t^2 \quad (|t|\le H).
$$
Consequently $g_T\le0$ on the entire prescribed interval for sufficiently large $T$, including at the origin. At `t=2πn/T`, however, the quartet contributes `4A(cosh(at)−1)`, which grows without bound as $n\to\infty$, while $g_0$ is bounded by absolute summability. Hence $e^{g_T}$ eventually exceeds 1 along that sequence.

On each prescribed grid `[g₀(tᵢ−tⱼ)]` is strictly positive on the zero-sum vector subspace. In its quadratic form the constant terms vanish, leaving the sum of positive weights times `|Σ uᵢ exp(inb tᵢ)|²` and the corresponding contributions of the other zeros. The first $r$ positive multiples of $b$ already give strict positivity by the Vandermonde matrix in `exp(ib tᵢ)`. The perturbation $q_T$ tends to zero entrywise on each grid, so this strict conditional positivity persists simultaneously across the finite collection for sufficiently large $T$.

To see the result for every positive power, let `Gᵢⱼ=g_T(tᵢ−tⱼ)` and anchor at the first point. Then `Bᵢⱼ=Gᵢⱼ−Gᵢ₁−G₁ⱼ+G₁₁` is positive semidefinite by the zero-sum condition. Schur powers show that the entrywise exponential `[exp(c Bᵢⱼ)]` is positive semidefinite for every $c>0$. Positive diagonal conjugation gives `[exp(c Gᵢⱼ)]≥0` on the same grid. This verifies all positive powers on every prescribed grid, jointly with the sign bound on `[−H,H]`, for an $E_T$ having four off-axis zeros. The construction uses functional symmetry, order one, the zero strip and the transform identity. The zeta Euler product and the arithmetic formula (1.5) supply additional assumptions outside the model.

## Finite-order Taylor tests at the origin

The small-time expansion is unconditional. Under RH it implies that the associated probability law has infinite variance. For $0<t<\log2$ the prime sum in (1.5) vanishes. The Hurwitz–Lerch contribution is
$$
 A(t)=\frac14\sum_{n\ge0}
 \frac{e^{-2t(n+1/4)}-1}{(n+1/4)^2},
 \qquad A'(t)=-\frac12\sum_{n\ge0}
 \frac{e^{-2t(n+1/4)}}{n+1/4}.
$$
The derivative series for positive $t$ differs from `−(1/2)Σ_{n≥1}e^(−2tn)/n` by $O(1)$ as $t\downarrow0$. Indeed the reciprocal difference is summable and the exponential shift makes an $O(t\log(1/t))$ difference. Using `Σ e^(−2tn)/n=−log(1−e^(−2t))` and integrating from zero gives
$$
 g_\zeta(t)=-\tfrac12|t|\log(1/|t|)+O(|t|),\qquad t\to0.
$$
The other terms in (1.5) are $O(|t|)$ near zero. If $e^{g_\zeta}$ is a characteristic function, its even probability law cannot have a finite first absolute moment, since `1−Re φ(t)≤|t| E|X|` would contradict this asymptotic. In particular ordinary moment-Hankel certificates formed from finitely many Taylor derivatives at zero lack the necessary differentiability. Compact-time finite differences still exist and fall within the finite-grid obstruction. [Primary text, equation (1.5)](https://arxiv.org/pdf/2306.08317v1)

## Prime-torus compatibility

The HLZ application concerns the normalized two-sided high tail of the measure with weights `|ζ′(ρ)|²/|ρ|²`, under RH. Nakamura–Suzuki uses the full measure with weights `mγ/γ²` inside a Lévy exponent on the ordinary real line. Multiple zeros illustrate the weight difference exactly. They contribute $m_\gamma/\gamma^2>0$ to the latter and zero to the derivative-weighted former. The fixed-character HLZ limit also assigns the coefficients `((n+1)n)^−1/2` at `log((n+1)/n)→0`, whereas the coefficient at zero is 1. It admits no continuous extension to an ordinary real-line characteristic function. The uniform growing-block estimate remains a conditional estimate of these same tail coefficients and so does not change that obstruction. [Director prime-torus adjudication](director_hlz_prime_torus_round9.md) · [Uniform growing-block review](uniform64_hlz_third_review.md)

There is a precise group-theoretic compatibility. For $c>0$, raising each limiting prime-torus Fourier coefficient to power $c$ simply changes the $p$-coordinate Poisson radius from `p^−1/2` to `p^−c/2`. The product Poisson measure is therefore infinitely divisible on the compact prime torus. Its roots retain the discontinuity on real frequencies approaching zero, and no real-line root or real-line characteristic function with those coefficients results.

## A sufficient next estimate

The fixed-sign argument only requires eventual sign. For a finite cutoff $U$, the integral over $[0,U]$ is entire in the transform variable, so removing it introduces no singularity. If $g_\zeta$ has either sign for all $t\ge U$, apply the fixed-sign Laplace theorem to its tail, or to the negative of its tail. Holomorphy on the positive imaginary axis again forces the abscissa to be nonpositive and then rules out off-axis zeros. Consequently, a failure of RH would force arbitrarily late strictly positive and strictly negative values of $g_\zeta$.

The transform proof gives an alternate precise target that makes no sign assumptions. It suffices to show `|gζ(t)|=Oε(e^(εt))` as $t\to\infty$ for every $\varepsilon>0$. Indeed the one-sided transform then converges absolutely and is holomorphic for every `Im z>0`, so the same logarithmic-derivative identity excludes poles there without the fixed-sign Laplace argument. Conversely RH makes $g_\zeta$ bounded by absolute summability of the Lévy weights. Thus this subexponential bound is itself equivalent to RH and isolates the required large-time cancellation in (1.5). The countermodel’s arithmetic progression explicitly violates it, even with any prescribed collection of finite tests certified. A finite certificate would require additional arithmetic input that controls the long-time remainder in (1.5).
