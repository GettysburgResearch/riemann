# Third adjudication: the Bessel quartet and log-concavity certificate

Reviewer: `/root/corpus`. Date: 2026-11-17. Classification: **independently checked with no issue found in the inspected construction**. This adjudication concerns the displayed generic entire function and its finite Li prefixes, not RH, an arithmetic L-function, the entirety of any cited paper, or priority/novelty.

Reviewed drafts:

* `proposals/independent_campaigns/bessel_finite_offline_countermodel_round3.md`;
* `audits/adversarial_reviews/positive_kernel_bessel_skeptic_round3.md`, including its log-concavity addendum;
* `experiments/code/positive_kernel_bessel_logconcavity_skeptic_round3.py`.

The two drafts were read before this adjudication, so independence here means an independent mathematical reconstruction and a differently organized exact verification, not a blinded review. The derivative reconstruction below does not use the drafts' stored second/fourth derivative formulas. Its final comparison with their polynomial is performed only after reconstructing that polynomial independently.

## Statement actually checked

Put `c=2π`, `a=1/4`, `f(u)=exp(-c cosh(2u))`,

\[
 A(w)=\int_{\mathbb R} f(u)e^{wu}\,du=K_{w/2}(c),\qquad
 Q_T(w)=((w-a)^2+T^2)((w+a)^2+T^2),
\]
\[
 F_T(s)=\frac{A(s-1/2)Q_T(s-1/2)}{A(1/2)Q_T(1/2)}.
\]

For every real `T>=32`, the following conclusions survive this review: the function is real entire of order one and infinite type, symmetric under `s -> 1-s`, with `F_T(0)=F_T(1)=1`; it has a strictly positive, even, smooth, strictly log-concave kernel with double exponential tails; all zeros are simple, exactly four are off the line, at `1/4 +/- iT, 3/4 +/- iT`; and its positive-ordinate count has the two smooth Riemann–von Mangoldt terms with `O(1)` error. For every integer `N>=1`, `T>=10N(8N^2+50)` ensures strict positivity of the first `N` Li coefficients. Increasing `T` also places the quartet above any prescribed finite verification height. This does not identify the remaining critical-line zeros with the actual zeros of zeta.

## Source and historical control

I inspected the actual page images of G. Pólya, *Bemerkung über die Integraldarstellung der Riemannschen ξ-Funktion*, Acta Mathematica **48** (1926), 305–317, DOI `10.1007/BF02565336`, specifically printed pp.306 and 315. The local source is `sources/positive_kernel_bessel_skeptic_round3/polya1926_acta.pdf`, SHA-256 `a338ba3c2d585dd6896784c85076fceb6d5710cac50642e661618fc11e651f24`; the two inspected images have the corresponding `p306.png` and `p315.png` names. This is a two-page targeted source inspection, not a full reading or audit of the thirteen-page paper.

On p.306, equation (7) defines

\[
 \mathfrak G(z;\alpha)=\int_{\mathbb R}e^{-\alpha(e^u+e^{-u})+zu}\,du,
 \quad \alpha>0.
\]

Our baseline is exactly `A(w)=mathfrak G(w/2;π)/2`. On p.315 Pólya explicitly concludes that `mathfrak G` has only simple purely imaginary zeros, and gives the positive-ordinate count
`(y/π)log(y/α)-y/π+O(1)`. The substitution `y=U/2`, `α=π` gives the baseline count used here. Consequently neither the baseline zero location/simplicity nor this sharp smooth count should be presented as new. Page 306 also presents a different, more faithful fake xi function; it must not be conflated with the bare Bessel baseline.

The review independently checks the spectral and phase arguments below rather than treating Pólya's printed conclusion as an audited proof. DLMF identities named in the drafts remain explicit classical dependencies; this adjudication makes no additional whole-source reading claims for DLMF or the Paris/SIGMA papers.

## Analytic reconstruction and possible failure points

**Integral normalization and domain.** Substituting `t=2u` in the usual `K` integral gives exactly `A(w)=K_(w/2)(c)`, with no factor two. The double exponential tail uniformly dominates all parameter derivatives on compact sets, as well as every integration-by-parts boundary term. Evenness and real symmetry follow from the actual integral. The gamma-integral majorant gives order at most one, while positive mass arbitrarily far out gives `log A(r)/r -> infinity`, hence order at least one and infinite type. Polynomial multiplication does not change these conclusions.

**All complex zeros and analytic multiplicity.** For the closed Dirichlet form of `H=-d²/dx²+c²e^(2x)` on the positive half-line, compactness follows from Rellich locally and the potential bound on the tail. If `K_ν(c)=0`, its decaying solution `K_ν(ce^x)` lies in the operator domain and has eigenvalue `-ν²`; self-adjointness and strict positivity imply `ν=+/-iτ`, `τ>c`. This excludes complex nonimaginary order zeros, rather than merely finding infinitely many imaginary ones. Conversely the unique decaying solution supplies every eigenvalue. Analytic determinant simplicity requires the additional differentiated Lagrange identity

\[
 -y_E(0)y_x(0)=\int_0^\infty y^2\,dx>0.
\]

The parameter derivative is locally uniformly decaying by the fixed-order large-argument asymptotic; `y_x(0)!=0` by ODE uniqueness. Thus `y_E(0)!=0`. Eigenspace simplicity alone would not have sufficed. The quartet is simple and cannot collide with these imaginary `w` zeros because its real parts are nonzero.

**Counting and derivatives of errors.** In the exact `I_(iτ)` series, `|(1+iτ)_k|>=τ^k` gives `|P-1|<=exp(c²/(4τ))-1`. Differentiating each reciprocal factor gives the separate uniform bound `|P'|<=(c²/(4τ²))exp(c²/(4τ))`. Thus the continuous phase, after the standard gamma/digamma expansion, is

\[
 \theta(\tau)=-\tau\log(2\tau/(ec))-\pi/4+O(1/\tau),\quad
 \theta'(\tau)=\log(c/(2\tau))+O(1/\tau^2)<0.
\]

The connection formula makes the zeros exactly the crossings `θ in πZ` beyond a fixed initial segment. There is no differentiation of an uncontrolled asymptotic error. The final count is `(U/(2π))log(U/(2πe))+O(1)` for `c=2π`; the two added positive-ordinate zeros change only a bounded term. No WKB approximation is needed as a rigorous premise.

**Global positivity.** Independently differentiating gives `f''/f>=-4c` and `f''''/f>=-576c³-32c` for `6<=c<=7`. For the latter inequality, on `v=cosh(2u)>=2` combine the leading two terms as `16c³(v²-1)[c(v²-1)-6v]>=0`; on `1<=v<=2` bound the two negative terms separately. Consequently

\[
 P(v):=Q_T(D)f/f > T^4-56T^2-197792\ge793440>0
\]

for `T>=32`. The lower bound is uniform over the entire real axis. Positivity of the transformed polynomial on a finite plotted interval would have been insufficient.

## Exact independent log-concavity verification

The correct reduction is

\[
 (\log(fP))''=-4R(v)/P(v)^2,
\]
\[
 R=cvP^2-vPP_v-(v^2-1)(P_{vv}P-P_v^2).
\]

The new independent verifier `experiments/code/bessel_logconcavity_third_round3.py` uses only standard-library rational arithmetic. It starts with the Laurent coordinate `r=e^(2u)`, so `D_u=2r d/dr` and `f'/f=-c(r-r^-1)`. It reconstructs all derivatives from `A_(n+1)=D_u A_n+(f'/f)A_n`, through degree four. It computes the log second derivative directly in `r`; only afterwards does it convert symmetric Laurent powers into `v` using `r^j+r^-j=2T_j(v)` and an independently generated Chebyshev recurrence.

The substitution `v=1+x`, `T²=1024+y`, `c=6+z` then produces exactly the same 199 nonzero rational monomials as the original verifier. For each of the 30 `x,y` coefficient groups, the code independently expands the supplied Bernstein representation back into ordinary powers and checks equality, instead of trusting the original forward basis conversion. Every Bernstein coefficient is strictly positive; the smallest is exactly `6`, with degree at most `9`. The `x^0 y^0` group is present. On `x,y>=0`, `z in [0,1]`, the Bernstein partition is nonnegative and sums to one, so each group is strictly positive, including both endpoints. Thus `R>0`. The elementary bounds `6<2π<7` put the intended parameter inside this certified interval. Together with the separately proved `P>0`, this proves strict log-concavity everywhere, and evenness then gives strict decrease for `u>0`.

Both verifiers were executed successfully on 2026-11-17. The independent result is `experiments/results/bessel_logconcavity_third_round3.json`. This is an exact finite sign certificate, not a claim based on floating-point signs or sample points.

## Quantitative finite Li prefix: constant checks

The paired Hadamard product is legitimate: order one and evenness leave no nonconstant exponential factor, and the count implies `sum γ_j^-2<infinity`. A pair at `s=1/2 +/- iγ` contributes exactly `2[1-cos(nθ)]`, `θ=2atan(1/(2γ))`. Each such contribution is nonnegative. Normal convergence near `s=1` justifies taking the finite-order Li derivatives.

For `j=N²+1`, the min–max estimates used in the advocate draft are valid form comparisons. The inequality `e^(2x)>=4x²` gives the lower comparison with the odd half-line oscillator, whose j-th eigenvalue is `2c(4j-1)`. The first j Dirichlet sine modes on `[0,1]`, extended by zero, are legitimate form-domain trial functions and give `E_j<=π²j²+c²e²`. Therefore `N<=γ_j=2sqrt(E_j)<G_N=8N²+50`. Since `nθ<=1` for `n<=N`, `θ>=1/(2γ_j)`, and `1-cos u>=u²/3` for `0<=u<=1`, this one pair gives the uniform margin `1/(6G_N²)`.

For the quartet, the first reciprocal sum is

\[
 S_1=\frac{1/2}{T^2+1/16}+\frac{3/2}{T^2+9/16}\le2/T^2,
\]

and `|S_k|<=4/T^k`. For `n>=2`, the higher binomial terms have sum at most `2n(n-1)T^-2(1+1/T)^(n-2)`; for `n=1` they are absent. Thus, for `T>=N`, the total perturbation is at most `(2+2e)N²/T²<8N²/T²`. At `T=10NG_N`, this is `<(2/25)G_N^-2 < (1/12)G_N^-2`, half the baseline margin. The stated finite-prefix result therefore has a genuine explicit bound, not an uncomputed existential minimum. It proves no infinite-prefix result for any one fixed `T`.

## Arithmetic and interpretive boundary

The claimed failure of the ordinary Dirichlet-series axiom also checks. The exact gamma integral gives `K_ν(2π)~Γ(ν)π^-ν/2` on the positive real ν-axis; the relative error bound `π²/(ν-1)` for `ν>1` follows directly from `1-e^-x<=x`. With `ν=s/2-1/4` and the quartet polynomial of degree four, dividing by the standard Riemann completion gives `C_T s^(7/4)`, `C_T>0`. An ordinary Dirichlet series absolutely convergent in some right half-plane tends to its finite first coefficient as real `s -> infinity`, by dominated convergence. The countermodel violates this precise arithmetic-growth requirement.

The construction therefore establishes a useful deletion test for a specified analytic class: strict log-concavity, a positive smooth double exponential kernel, symmetry, strong smooth counting asymptotics, finitely many off-line zeros, and an arbitrarily long finite Li-positive prefix do not force RH within that class. It does not delete the ordinary Dirichlet series, Euler product, prime-side explicit formula, or the exact zeta function from an RH argument. No published mathematical error was identified in this review, and no claim of novelty is justified by it.
