# Normalized notation and convention hazards

| Symbol | Meaning | Scope / source hazard |
|---|---|---|
| ζ(s) | classical Riemann zeta | Not a generic L-function unless expressly stated |
| ξ(s) | (1/2)s(s−1)π^(−s/2)Γ(s/2)ζ(s) | Modern normalization; Riemann translation uses transformed variable and different scaling |
| ρ=β+iγ | distinct nontrivial zeta zero | Every sum specifies whether multiplicities enter; m_ρ is multiplicity |
| N(T) | positive-ordinate zeros up toT, counted with multiplicity | A density-one statement does not exclude sparse exceptional zeros |
| λ_n(F) | derivative at1 of s^(n−1)logF(s), divided by(n−1)! | A single root contributes1−(ρ/(ρ−1))^n. Reflection symmetry is needed to convert to1−(1−1/ρ)^n |
| H_n, σ(n), γ_E | harmonic sum, divisor sum, Euler constant | γ_E avoids confusion with a zero ordinate |
| ρ_a(x) | fractional part{1/(ax)} | E001 source notation; not a zeta zero |
| D(λ) | distance for continuous fractional-part dilation parameters≥λ | Burnol source, distinct from discrete d_N |
| d_N² | infimum weighted critical-line Dirichlet-polynomial squared error | Infimum/existence cannot silently be replaced by a prescribed Möbius coefficient array |
| E_N(θ) | optimal squared H² unit-circle error for Qθ | Every reported1/N rate is squared norm; norm rate1/sqrtN |
| L=N+m | maximum residual degree in polynomial models | Distinct from analytic window widthL=log(T/2pi) |
| φhat(r) | ∫φ(u)e^(−iur)du | AF source: Parseval factor2pi and grid2pi/L |
| N_+(K) | first-order graph eigenvalues in(0,K], multiplicity | Absolute-spectrum count doubles leading density; Endres–Steiner wording needs caution |
| E | number of finite graph channels | Fixed during each three-height count test; may grow with family indexK |
| Λ | de Bruijn–Newman heat parameter | Heat-sign/normalization source-specific; RH corresponds toΛ≤0 with Rodgers–Tao normalization |

Original notation is retained in paper records. No graph equivalence is inferred from matching symbol names.


## Completion and source-coordinate hazards recovered later

- Modern centered coordinatew=s−1/2 is different from the zero ordinate gamma=(rho−1/2)/i. In gamma coordinates Im gamma=1/2−Re rho. Functional-equation reflection preserves Re gamma and conjugates it.
- Countermodels normalizeF(0)=F(1)=1, soF is analogous to2xi. Their residue-one uncompletion isZ=pi^(s/2)F/[s(s−1)Gamma(s/2)] without1/2. Dividing by the usual xi prefactor1/2 doublesZ and its residue. Li derivatives ignore a multiplicative constant; uncompletion normalization does not.
- Riemann's1859 xi_R(t)=xi_mod(1/2+it). Thusxi_R(0)=xi_mod(1/2), whereasxi_R(i/2)=xi_mod(0)=1/2. Pair factors in these two coordinates differ by1+1/(4alpha²). Preserve the historical correction/source/branch notes before simplifying constants in the explicit formula.
- Knopp's variableu hasGamma(u) and reflection1/2−u. The standard variablet=2u hasGamma(t/2), but ordinary n^(-u) becomes generalized(sqrt n)^(-t). Ordinary integer support requires square-supported coefficients in theu series.
- sinc in the sine-Gram campaigns meanssin(pi x)/(pi x), with band[-1/2,1/2] and intensity1 after unfolding. AF's exp(i tau u) transform instead has sampling2pi/L. No theorem transfers without converting both conventions.
- In moment recordslambda_m(0) is the ordinary minimum-square Christoffel value. It bounds atom mass; the positive-halfline problem needs a globally valid one-sided polynomial or the stated canonical quadrature hypothesis. Lower/upper CDF bounds are separate quantities.


## Adaptive and finite-prefix coordinates

- In the adaptive approximation records, ||f||_*²=(2π)^(-1)∫|f(1/2+it)|²dt/(1/4+t²). Delta_N is the optimized unrestricted distance, while the source d_N additionally forces the polynomial multiplying zeta to vanish at1. Neither notation denotes the error of a prescribed coefficient array.
- For fixed primitiveχ, Delta_(N,χ) uses the same full Cauchy weight and all ordinary integersn≤N with arbitrary complex coefficients. It is unanchored. Signed ordinates are not assumed to pair; central zeros are counted once.
- The finite prefix cost c_m(b),0≤b<1, is a polynomial Gram quantity. Its Legendre coordinate is a=(1+b)/(1−b), its Bessel coordinate r=m²b/(1−b), and the natural sharper coordinate r*=m(m−1)b/(1−b). These are different from the source analytic widthL=logN or the good-height meshD.
- Phi(r)=I0(2sqrt r)²−I1(2sqrt r)² has Phi(0)=1. The finite large-regime asymptotic needsm→infinity andm sqrt b→infinity. Arithmetic b=b(N) uniformity is not implied by a finite m,b limit.
