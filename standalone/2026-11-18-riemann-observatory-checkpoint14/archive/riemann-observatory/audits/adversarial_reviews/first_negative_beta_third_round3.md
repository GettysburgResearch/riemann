# Independent reconstruction of the first negative Li index

Reviewer: `/root/corpus`. Date: 2026-11-17. Task: adversarially check the proposed asymptotic first-negative index in the beta-smoothed quartet model, including **every earlier integer index**, phase alignment, uniformity of the Bessel contribution and the beta error. The proof below was reconstructed from the model and the requested leading asymptotic, before reading a final first-negative draft. It uses the independently reviewed beta construction in `beta_smoothing_third_round3.md` and the baseline source/reconstruction in `bessel_third_round3.md`. Novelty is unassessed; this is a model calculation, not a zeta theorem.

## Precise result and assumptions

Fix `a=1/4`. For each sufficiently large real `T`, take **any** tuned root `δ_T in (0,1/100]` of the beta normalization equation `C(T,δ_T)=1`, and form the normalized completed entire function

\[
 F_T(s)=A_T K_{(s-1/2)/2}(c_T)Q_T(s-1/2)M_{\delta_T}(s-1/2),
 \quad c_T=2\pi e^{2\delta_T}.
\]

The tuning proof supplies `6<c_T<7` and `δ_T=O(T^(-16/7))`, uniformly over all choices of the tuned root. Normalization constants have no positive-index Li contribution. Write `n_-(T)=min{n>=1:lambda_n(F_T)<0}`. Then this minimum exists for all sufficiently large `T`, and the proposed leading constant is correct:

\[
 \frac{n_-(T)}{T^2\log T}\longrightarrow 8.
\]

The same reconstruction gives a more precise statement:

\[
 \boxed{\displaystyle
 n_-(T)=\frac{T^2}{a}
 \big[2\log T+2\log\log T-\log a+o(1)\big].}
 \tag{1}
\]

For `a=1/4`, this is
`8T²log T + 8T²log log T + 8T²log 2 + o(T²)`.
The refined statement was proposed by this independent reconstruction; its independent team review status is recorded separately below. No named individual zeta zero or arithmetic conclusion is involved.

## 1. Exact quartet expression and its branches

For the left upper root `rho=1/2-a+iT`, define

\[
 z=1-1/\rho=e^{\eta_T+i\theta_T},
\]
\[
 \eta_T=\tfrac12\log
 \frac{T^2+(1/2+a)^2}{T^2+(1/2-a)^2}
 =a/T^2+O(T^{-4})>0,
\]
\[
 \theta_T=\arctan((1/2+a)/T)+\arctan((1/2-a)/T)
 =T^{-1}+O(T^{-3})>0.
\]

For `a=1/4` the more detailed coefficients are `η=1/(4T²)-5/(64T⁴)+O(T^-6)` and `θ=1/T-7/(48T³)+O(T^-5)`, though they are not needed for (1). These arguments are the actual small positive arguments of `z` for large positive `T`, not branches defined modulo an unspecified multiple of `2π`.

Conjugation and reflection give the four transformed roots `e^(+/-η +/- iθ)` with the corresponding signs. The exact polynomial Li coefficient is therefore

\[
 \lambda_n(Q_T)=4\big[1-\cosh(n\eta_T)\cos(n\theta_T)\big].
 \tag{2}
\]

Two lower bounds used below hold for every integer `n>=1`:

\[
 \lambda_n(Q_T)\ge-2(n\eta_T)^2e^{n\eta_T},\qquad
 \lambda_n(Q_T)\ge-2e^{n\eta_T}.
 \tag{3}
\]

The first follows from `cosh x-1<=x²e^x/2`. The second follows from
`4-4cosh x=4-2e^x-2e^-x>=-2e^x`. Replacing the exact oscillatory term by one of these lower bounds handles all phases, including an unexpectedly well-aligned early integer.

## 2. Uniform Bessel Li growth: proof of the needed input

Let `N_c(t)` count positive ordinates of `K_(w/2)(c)`, with `6<=c<=7`. The exact `I`-series phase reconstruction gives uniformly on this compact parameter interval

\[
 N_c(t)=\frac{t}{2\pi}\log(t/c)-\frac{t}{2\pi}+O(1).
 \tag{4}
\]

Here is why the parameter uniformity is legitimate. In the factorized `I_(iτ)(c)` series the bounds on the series remainder and its τ derivative depend on `c²/4<=49/4`, so a single sufficiently large τ threshold ensures nonvanishing and monotone phase for all such `c`. The gamma/digamma remainders have no c dependence; `log c` is bounded. The number of remaining initial zeros is uniformly bounded by the `c=6` Dirichlet spectrum, because the confining potentials increase with c. Thus the bounded phase-to-count error can be chosen uniformly; merely quoting a fixed-c asymptotic without this step would not suffice.

Write the positive ordinates as `γ_j(c)` and `θ(γ)=2atan(1/(2γ))`. The paired product gives

\[
 L_c(n):=\lambda_n\!\left(
 \frac{K_{(s-1/2)/2}(c)}{K_{1/4}(c)}\right)
 =2\sum_j[1-\cos(n\theta(\gamma_j(c)))].
\]

All terms are nonnegative. Moreover
`|θ(γ)-1/γ|<=1/(12γ³)` and `sum_j γ_j(c)^(-3)` is uniformly finite by (4) (also by spectral monotonicity and the c=6 sum). Consequently replacement of `θ(γ)` by `1/γ` costs `O(n)`, uniformly in c.

Use (4) in the Stieltjes integral `2 integral(1-cos(n/t))dN_c(t)`. Integration by parts against its uniformly bounded count remainder costs `O(n)`: the lower spectral endpoint is uniformly bounded away from zero and `integral |d(1-cos(n/t))|<=O(n)`. Extending the smooth main integral down to zero costs only `O(1)`, since `|1-cos|<=2` and `integral_0^12|log(t/c)|dt` is uniformly finite. The main integral is

\[
 \frac1\pi\int_0^\infty[1-\cos(n/t)]\log(t/c)\,dt
 =\frac n\pi\left[
 \log(n/c)\int_0^\infty\frac{1-\cos u}{u^2}du
 -\int_0^\infty\frac{(1-\cos u)\log u}{u^2}du\right].
\]

The first integral is `π/2`, and the second is absolutely convergent. Therefore

\[
 L_c(n)=\tfrac12 n\log n+O(n)
 \quad\text{uniformly for }6\le c\le7.
 \tag{5}
\]

In particular there is one constant `b0>0` such that

\[
 L_c(n)\ge b_0 n\log(n+1)
 \quad\text{for every }n\ge1,\ 6\le c\le7.
 \tag{6}
\]

To justify the finitely many small n in (6), use the previously checked uniform min–max paired-zero margin for an entire finite prefix; each coefficient has a strictly positive uniform lower bound. Thus (6) does not assume pointwise strict positivity automatically gives a compact-uniform bound without proof.

The coarse `O(n)` error in (5) suffices even for the constant term inside the bracket in (1). A finer error or an explicit linear term is unnecessary here.

## 3. Beta contribution is nonnegative and negligible at the transition

The normalized beta product has `M_delta(w)=1+δ²w²/9+...`, so its positive ordinates satisfy

\[
 \sum_j\gamma_{\beta,j}^{-2}=\delta^2/9.
\]

For each line pair, `2(1-cos(nθ))<=n²θ²<=n²/γ²`. Hence exactly

\[
 0\le\lambda_n(M_\delta)\le n^2\delta^2/9.
 \tag{7}
\]

For `n=O(T²log T)` and any tuned root, this is
`O(T^(-4/7)(log T)²)=o(1)`. No limit interchange between an infinite Li sum and a tuning sequence is needed. The rate bound on δ follows directly from `C=1`, `Q_T(1/2)>=T^4`, `M_delta(1/2)>=1`, and a compact-uniform positive lower bound on `K_(1/4)(c)`.

## 4. All earlier indices, including early favorable phases

Put `L=log T` and `b_T=(T²/a)L`. This is half the leading transition scale. For `1<=n<=b_T`, combine the first bound in (3) and (6). The ratio of the possible negative quartet contribution to the Bessel lower bound is at most

\[
 \frac2{b_0}\frac{n\eta_T^2e^{n\eta_T}}{\log(n+1)}.
\]

For fixed `η>0`, `n e^(nη)/log(n+1)` is strictly increasing for real `n>0`, since `(n+1)log(n+1)>n`. Its maximum here occurs at `b_T`, where `b_T η=L+o(1)`; the displayed ratio is `O(T^-1)`. Therefore **every integer `n<=b_T` is strictly positive** for sufficiently large T, regardless of phase. Beta contributes only a nonnegative quantity.

For the rest of the lower region, define

\[
 Y_0=2L+2\log L-\log a,\qquad
 p_\pm(T,\varepsilon)=\frac{T^2}{a}(Y_0\pm\varepsilon),
\]

where `ε>0` is fixed. For real `n>=b_T`,

\[
 R_T(n)=\frac{4e^{n\eta_T}}{n\log n}
\]

is increasing for large T: its logarithmic derivative is
`η_T-1/n-1/(n log n)>0`, because `nη_T>=L+o(1)`. At the proposed endpoints,

\[
 R_T(p_\pm)\longrightarrow e^{\pm\varepsilon}.
 \tag{8}
\]

Indeed `p_±η=Y0±ε+o(1)`, so its numerator is
`4T²L² e^(±ε)/a [1+o(1)]`, while its denominator is `4T²L²/a [1+o(1)]`.

By (5), the Bessel contribution divided by `n log n/2` is `1+O(1/L)`, uniformly for `b_T<=n<=p_-`. The second lower bound in (3) and monotonicity of R then imply

\[
 \lambda_n(F_T)\ge\tfrac12 n\log n
 [1+O(1/L)-R_T(p_-)]>0
\]

for **every** integer in this interval. This excludes premature negative coefficients from Bessel fluctuations, from any tuned branch, or from exceptional phase coincidences. Merely finding a later aligned negative coefficient would not have proved that its scale describes the first negative one.

## 5. An aligned negative integer within O(T)

Choose an integer m nearest to `p_+ θ_T/(2π)`, and then an integer n nearest to `2πm/θ_T`. This gives

\[
 |n-p_+|\le\pi/\theta_T+1/2=O(T),\quad
 |n\theta_T-2\pi m|\le\theta_T/2=O(T^{-1}).
\]

Thus `cos(nθ)=1-O(T^-2)`, `n=p_++o(T²)`, and `R_T(n)->e^ε`. Using the exact quartet formula, (5), and (7),

\[
 \frac{\lambda_n(F_T)}{n\log n/2}
 =1-e^\varepsilon+o(1)<0.
\]

The omitted `e^(-nη)` and constant terms in the quartet formula tend to zero after this normalization. Hence a negative integer coefficient exists within `O(T)` of the upper endpoint.

Combining the all-index lower bound through `p_-` and this aligned upper bound gives
`p_- < n_-(T) <= p_++O(T)`. Since ε is arbitrary and `T=o(T²)`, this proves (1), including its `-log a` constant. Integer rounding and phase alignment contribute only `o(T²)`, so neither changes that constant.

## Findings and scope

The leading `8T²log T` proposal survives the independent adversarial reconstruction. The refined logarithmic correction (1) follows from the same inputs; it does not require a new source theorem, a numerical root, or an assumption about a randomly distributed phase. The result is uniform over every tuned-root choice in the stated parameter interval, and factor collisions on the line are harmless because the products and counts retain multiplicity.

The proof gives no uniform finite-prefix criterion for the actual zeta function, no bound on the height of a hypothetical off-line zeta zero, and no arithmetic interpretation of the polynomial/quartet parameter T. The construction's failure of the Dirichlet-series axiom remains essential. Prior first-negative Li asymptotic literature was not fully investigated by this reviewer; no originality or publication-priority assertion is supported.

Review status: independent proof supplied. After writing this reconstruction, I read the completed independent skeptic proof and refinement in `audits/adversarial_reviews/first_negative_li_asymptotic_skeptic_round3.md`; the normalizations, constant and all-index argument agree. The skeptic separately rederived the `-log a` constant and found no issue. Parent review remains separately recorded; no message requesting review is counted as a completed review.
