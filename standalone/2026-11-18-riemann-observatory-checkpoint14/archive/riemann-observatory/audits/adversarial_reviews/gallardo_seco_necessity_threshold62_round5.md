# Independent necessity review for the shifted weighted closure threshold

2026-11-17. Reviewer threshold_review_62. This note derives the separating functional in the source domain norm and checks the proposed parameter witness. It is a scoped technical review for adjudication. Priority unassessed.

## Source statement and domain

I visually inspected a fresh render of p. 26 of the local publisher PDF, including Theorem 5.5 and equation (29). The theorem takes `α∈[−3,−2]` and `1≤a<(1−α)/2`, and asserts an equivalence between the stated weighted closure and zero-freeness for `Re s>(−1−α)/2`. The source p. 3 gives `||f||²_{D_β}=Σ_{n≥0}(n+1)^β|[z^n]f|²`. Page 21 defines `T_a f=f'−af/(1−z)`. Page 25 gives the Noor generator `h_k=(1−z)^{-1}log((1+z+⋯+z^{k−1})/k)`. The log is the analytic branch real on `(0,1)`, and `(1−z)^c` uses the power branch positive there. The polynomial inside the log has no zeros in the disk. [Publisher PDF](../../sources/logarithmic_riesz_round3/gallardo_seco2025.pdf)

Put `t=(−1−α)/2`, `β=α+2=1−2t`, `c=a−1`, `b=t−c>0`, and `u=(1−z)^{-c}`. The power has coefficients `O_c((n+1)^{c−1})` for `c>0`. Expand the generator log as `log(1−z^k)−log(1−z)−log k` and divide by `1−z`. Its coefficients are `H_n−H_{⌊n/k⌋}−log k`, where `H_0=0`, and are `O_k((n+1)^{-1})`. The last bound follows for `n≥k` from `H_j=log j+γ+O(1/j)`, `⌊n/k⌋≳n/k`, and `log(n/(k⌊n/k⌋))≤(n−k⌊n/k⌋)/(k⌊n/k⌋)`. For `uh_k` split the convolution with the coefficients of `h_k` into `j≤n/2`, where the power coefficient is `O_c((n+1)^{c−1})` and the harmonic sum gives a logarithm, and `j>n/2`, where the generator coefficient is `O_k((n+1)^{-1})` and the sum of the power coefficients is `O_c((n+1)^c)`. Thus `[z^n](uh_k)=O_{c,k}((n+1)^{c−1}log(n+2))`. Both `u` and `uh_k` belong to `D_β` because `β+2c−2=−1−2b<−1`. If `c=0`, membership follows from the constant target and the direct bound on the generator.

## Separating functional directly on the domain

For `s=σ+iτ` with `σ>b`, define
\[
\Lambda_s(f)=\frac{1}{s\Gamma(s)}
\int_0^1(-\log r)^{s-1}(1-r)^c\bigl((1-r)f'(r)-af(r)\bigr)\,dr .
\]
The powers in this integral use the real logarithms of their positive bases, in particular `|(-log r)^{s−1}|=(-log r)^{σ−1}`. Here `σ>0`, so `sΓ(s)=Γ(s+1)` is finite and nonzero. On `0≤r≤1/2` the coefficient Cauchy–Schwarz estimates for `f` and `f'` are uniform, from convergence of the polynomially weighted geometric series at `r=1/2`. Thus near zero the integral is bounded by a constant times `||f||_{D_β}∫_0^{1/2}(-log r)^{σ−1}dr`, finite by `x=−log r`.

For `1/2<r<1`, coefficient Cauchy–Schwarz gives `|f(r)|≲(1−r)^{-t}||f||_{D_β}` and `|f'(r)|≲(1−r)^{-t−1}||f||_{D_β}`. In the squared evaluation bounds use sums with weights `(n+1)^{−β}` and `n²(n+1)^{−β}`. Bounding the geometric terms by exponentials gives their orders `(1−r)^{−2t}` and `(1−r)^{−2t−2}`; the derivative shift in the geometric exponent costs a bounded factor on this radial interval. Since `−log r≍1−r`, the integrand is bounded by `C_s||f||_{D_β}(1−r)^{σ−b−1}`. This proves absolute convergence and continuity for the exact strict half-plane `σ>b` used by the argument. No operator inverse is needed.

To compute values put `h=(1−z)^c`, so the integral is the radial transform of `g=hT_af` with bracket `(1−r)g(r)`. Because `a=c+1`, the analytic product rule gives
\[
hT_a(uv)=v'-v/(1-z)=((1-z)v)'/(1-z).
\]
For `v=1` the image is `−f_0`, where `f_0=1/(1−z)`. For `v=h_k` the image is `R_k=Σ_{n≥1}r_k(n)z^{n−1}`, with `r_k(n)=n−k⌊n/k⌋`. Indeed the log derivative is `1/(1−z)−kz^{k−1}/(1−z^k)`. After division by `1−z`, the coefficient at `z^{n−1}` is `n−k⌊n/k⌋`. This checks equation (29) and the target sign independently.

For any `g=Σ_{n≥1}q_nz^{n−1}` with bounded coefficients, insertion of the series in its radial transform is legitimate. The sum of the absolute integrands without the log factor is bounded by `sup_n|q_n|(1−r)Σ_{n≥1}r^{n−1}=sup_n|q_n|`. The remaining factor `(-log r)^{σ−1}` is integrable on `(0,1)` for all `σ>0`. Substituting `x=−log r` in each term proves that the radial transform is
\[
\frac1s\sum_{n\ge1}q_n(n^{-s}-(n+1)^{-s}).
\]
Complex powers use the real logarithm of the positive integers. For `f_0` this telescopes to `1/s`. For `R_k` its locally uniformly convergent series for `σ>0` can be evaluated first for `σ>1` by using `r_k(n)−r_k(n−1)=1−k1_{k\mid n}`. The absolutely convergent Dirichlet series there is `(1−k^{1−s})ζ(s)/s`. Continuation to `σ>0` is legitimate. The difference of adjacent powers is `s∫_n^{n+1}x^{-s−1}dx`, giving local uniform convergence, and the apparent pole at `s=1` cancels through `1−k^{1−s}`. Therefore for every nontrivial zero `ρ` with `Re ρ>b`, the bounded functional satisfies
\[
\Lambda_\rho(u)=-1/\rho,\qquad \Lambda_\rho(uh_k)=0\quad(k\ge2).
\]
In particular the distance from the target to the span is at least `1/(|ρ| ||Λ_ρ||)>0`. The resulting condition is zero-freeness in the strict open half-plane `Re s>b`. This separation gives no exclusion for zeros on its boundary.

## Why the strict evaluation bound matters

The integral on polynomials has an additional check at the boundary. For `Re s>0`, let `I_{d,n}=∫_0^1(-log r)^{s−1}(1−r)^d r^n dr` with `d≥0`. Substitution `v=−n log r` and dominated convergence give `n^{s+d}I_{d,n}→Γ(s+d)`. The inequality `n(1−exp(−v/n))≤v` gives the integrable majorant `v^{σ+d−1}e^{-v}`. Hence
\[
n^{s+c}\Lambda_s(z^n)\longrightarrow
\frac{(s+c-a)\Gamma(s+c)}{s\Gamma(s)}
=\frac{(s-1)\Gamma(s+c)}{s\Gamma(s)}.
\]
This follows by applying the same asymptotic to `nI_{c+1,n-1}−aI_{c,n}`. If `σ=b` and `s≠1`, the constant is nonzero. Bounded extension from polynomials would require square summability of the values on the normalized monomials, and the squared values are comparable to `n^{-2b−2c−β}=1/n`. Thus this functional has no bounded extension on that boundary for `s≠1`. The exceptional point `s=1` on the boundary is possible only at `b=1`, where `(α,a)=(−3,1)`; on polynomials one then has `Λ_1(f)=−f(0)` by integration of the derivative of `(1−r)f(r)`. This point is not a zeta zero.

## Allowed parameter witness and the two closure norms

For `(α,a)=(−3,7/4)`, the source permits `a<2`. Then `t=1`, `c=3/4`, and `b=1/4`. The half-plane printed in Theorem 5.5 is `Re s>1`, which is zero-free by absolute convergence of the Euler product. The Riemann–von Mangoldt count in Titchmarsh Theorem 9.4 gives a nontrivial zero, and §2.12 gives the reflection `ρ↦1−conj(ρ)`. At least one of the two has real part at least `1/2`, strictly above `b=1/4`. Its separation proves failure of the target closure at this allowed parameter pair. This requires neither a numerical zero location nor a bounded inverse at the critical operator endpoint. [Titchmarsh PDF](../../sources/equivalence_round2/titchmarsh1986.pdf)

In ordinary `D_{−3}`, the same remainder span does approximate `f_0`. The separately reviewed Bergman proof puts `1` in the closed Noor span in `D_{−1}`. The bounded map `T_1:D_{−1}→D_{−3}` takes `1` to `−f_0` and `h_k` to `R_k`. Its boundedness is the derivative coefficient estimate and the prefix Hardy estimate with exponent `t=1`. In the pulled-back norm `||g/h||_{D_{−3}}`, both `f_0` and all `R_k` are present. Their coefficients are bounded, so multiplication by `u` makes them `O_k((n+1)^c)`, whose squared `D_{−3}` norms are finite at `c=3/4`. The radial transform in this range is continuous for `σ>1/4` by the direct coefficient estimate `|(g/h)(r)|≲||g/h||_{D_{−3}}(1−r)^{-2}`. The resulting integral has boundary exponent `σ−1/4−1`, with the same near-zero bound as above. Its values on `f_0` and `R_k` give the same strict separation in the pullback norm. Thus this arithmetic span itself distinguishes the two closures. [Bergman review](noor_critical_bergman_skeptic_round4.md) [Bounded operator proof](gallardo_seco_operator_impact_advocate_round4.md)

The independent sufficiency review with the same `b=t−c` is recorded separately. [Sufficiency review](gallardo_seco_sufficiency_threshold62_round5.md)
