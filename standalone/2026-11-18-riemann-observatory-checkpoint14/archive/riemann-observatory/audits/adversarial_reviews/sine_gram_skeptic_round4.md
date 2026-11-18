# Independent sine-process sinc-Gram review

2026-11-17. Reviewer `/root/li_skeptic`. The thinning, interlacing and moment arguments below were reconstructed before reading the advocate's draft. Exact source definitions/theorem passages were then inspected. Scope: expected empirical spectral laws of the unit-intensity sine determinantal process. No RH claim, no proof of the arithmetic hypotheses in Alpöge–Furman, and no whole-paper audit of that preprint or the interpolation literature.

## Precise setting and conclusions

Use `sinc x=sin(pi x)/(pi x)`, with its value at zero equal to one. Let `X` be the stationary simple sine determinantal process of intensity one on `R`, with correlation densities

\[
 \rho_k(x_1,\ldots,x_k)=\det[\operatorname{sinc}(x_i-x_j)]_{i,j=1}^k.
\]

For points in `[0,R]`, let `S_R` be their finite sinc-Gram matrix, let `N_R` be their number, and put

\[
 \mu_R=\frac1R E\sum_{j=1}^{N_R}\delta_{\lambda_j(S_R)}.
\]

This is a deterministic probability measure on `[0,infinity)`, not a pathwise empirical measure normalized by the random point count. Its first moment is one. As `R` tends to infinity:

1. Every weak subsequential limit has no atom at zero.
2. For every integer `m>=1` and every `R>0`, `integral lambda^m dmu_R<=4^m m!`.
3. Every weak subsequential limit is moment determinate. The independent companion graph–Hölder proof subsequently establishes all fixed moment limits, so these limits identify a unique full weak limit; see the addendum below.
4. For any such limiting measure, the Christoffel minimum at zero over polynomials of degree at most `m` tends to zero.

The proof uses a standard, sourced interpolation theorem as an external mathematical input. It does not audit its original1989/1995 proof from inaccessible originals. There is no claim of novelty; priority for this particular sine-Gram statement remains to be investigated.

### Subsequent independent moment-existence addendum

The initially conditional moment-limit premise is now supplied, within this same probabilistic model, by `proposals/independent_campaigns/sine_gram_moment_existence_round4.md` and theorem `THM-SG309`. Each equality partition of a closed trace walk gives a connected Eulerian multigraph. After loops are discarded, its absence of bridges allows spanning-tree Hölder exponents strictly above one, precisely the integrability range of the sinc kernel. Anchored absolute integrability and the exact finite-window overlap then give all fixed moment limits by dominated convergence. The advocate challenged this argument independently before reading the proposer proof; the root separately checked all graph, integral and normalization steps. This strengthens conclusion3 to full convergence of the expected per-length laws. It supplies no almost-sure law, rate, growing-order estimate or arithmetic moment matching.

## 1. Stochastic inputs and normalization

Positive semidefiniteness and the unit diagonal give `0<=rho_k<=1` by Hadamard's determinant inequality. In particular

\[
 \rho_2(x,y)=1-\operatorname{sinc}^2(x-y)\le1.
\]

The standard correlation identities give

\[
 EN_I=|I|,\qquad
 \operatorname{Var}N_I=|I|-\int_{I^2}\operatorname{sinc}^2(x-y)dxdy\le|I|.
\]

Since `Tr S_R=N_R`, both the total mass and first spectral moment of `mu_R` are exactly one. The first moment makes this family tight; no probability mass can escape to infinity. No ergodic theorem or almost-sure density convergence is needed below.

The normalizations agree with the Hilbert space `H=PW_pi^2`, realized using Fourier frequency interval `[-1/2,1/2]` and convention `exp(2pi i x xi)`. Its evaluation vector is `k_x(y)=sinc(y-x)`, with `||k_x||=1` and inner product `sinc(x-y)`.

## 2. Exact interpolation input, and an independent PW² upgrade

Actual primary research source inspected: Frédéric Gaunard, arXiv1110.1714v1, *Minimality, (Weighted) Interpolation in Paley-Wiener Spaces and Control Theory*. Pages5–6 define `PW_tau^p` as entire functions of type at most `tau` with `L^p(R)` norm, and interpolation as solving arbitrary appropriately weighted `ell^p` data. Its Theorem3,printedp7, visually checked, states for a sequence in a finite horizontal strip:

> Uniform separation and `D^+(Lambda)<tau/pi` imply interpolation in `PW_tau^p`.

Here only `p=2`, real points and `tau=pi` are used, so all imaginary-part weights are one. The theorem explicitly attributes the result to Seip1995,Theorem2.2, based on Beurling1989. Those original sources were not successfully accessed and are not credited as read. The critical equality case `D^+=1` is **not** being asserted sufficient.

A second actual research source was obtained independently: Ortega-Cerdà and Seip, *Multipliers for entire functions and an interpolation problem of Beurling*, preprint dated15August1998, Theorem1,p2. It characterizes Bernstein interpolation by separation, a two-sided Carleson condition and `D^+<tau/pi`; for real separated sets the Carleson condition is vacuous and its separation agrees with positive Euclidean separation. Only its introduction and theorem/definitionspp1–3 were read, not the full proof. Local source and hash: `sources/sine_gram_skeptic_round4/ortega_cerda_seip.pdf`, matching retrievalJSON.

The following independent argument verifies that the real Bernstein theorem does give the exact PW² consequence needed; it avoids silently conflating the spaces. Given a separated `Lambda` with `D^+<1`, choose `tau_0<pi` still satisfying `D^+<tau_0/pi`. Bernstein interpolation and open mapping give bounded Lagrange functions `f_j` of type `tau_0`, with `f_j(lambda_k)=delta_jk` and a uniform real-axis bound. A bounded linear right inverse on all `ell^infinity` is not assumed or needed: choose each `f_j` only for datum `e_j`.

Multiply `f_j` by a squared-sinc function centered at `lambda_j`, of type `epsilon=pi-tau_0`, equal to one there. The resulting `g_j` have type at most `pi`, are in `L²`, retain exact interpolation, and satisfy

\[
 |g_j(x)|\le C(1+|x-\lambda_j|^2)^{-1}.
\]

Separation bounds the sum of these envelopes uniformly in `x`, and each envelope has bounded integral. Schur's test therefore makes `sum a_j g_j` a bounded synthesis from `ell²` into `L²`. The finite sums lie in the closed space `PW_pi²`; its continuous point evaluations pass the interpolation identities to their limit. Thus every `ell²` datum is interpolated with norm bounded by a constant times its norm.

For a finitely supported coefficient vector `a`, choose such an interpolant `f` with values `a_j`. Then

\[
 \left\|\sum_j a_jk_{\lambda_j}\right\|\,\|f\|
 \ge\left|\left\langle\sum_j a_jk_{\lambda_j},f\right\rangle\right|
 =\sum_j|a_j|^2.
\]

Hence the sinc-Gram quadratic form is bounded below by `a_Lambda sum|a_j|²`, for a positive constant depending on the whole set. Finite and empty sets are handled separately and trivially. This is exactly the global Riesz lower bound used below; no uniform bound over all possible configurations is presumed.

## 3. Global thinning with a controlled expected loss

Fix a separation `delta>0`, a small `eta in (0,1)`, and a length `L` large enough that `K=floor((1-eta)L)>=1`.

First delete every point which has any other process point within distance `delta`. This rule is applied on the **whole real line**, including neighbors outside a later window. The number deleted in `[0,R]` is at most the ordered close-pair count with first point there, so its expectation is at most `2delta R` by `rho_2<=1`.

Partition the whole line into aligned half-open cells `[jL,(j+1)L)`. After the first thinning, retain at most the leftmost `K` points of each cell. This is a measurable deterministic selection, preserves separation, and gives the global retained set `Lambda`. Its upper uniform density satisfies

\[
 D^+(\Lambda)\le K/L\le1-\eta<1,
\]

because any long interval meets at most its length divided by `L`, plus two, complete or partial cells.

For one cell the further deletion count is at most `(N_L-K)_+`. Since `EN_L=L` and `Var N_L<=L`,

\[
 E(N_L-K)_+\le L-K+E|N_L-L|
             \le\eta L+1+\sqrt L.
\]

Thus if `D_R` denotes the total deletions in `[0,R]`, complete cells and one final boundary cell give

\[
 ED_R/R\le2\delta+\eta+L^{-1}+L^{-1/2}+O(L/R).
\]

The exact boundary constant is immaterial and independent of `R`. None of these inequalities requires an independent thinning or independence of cell counts.

## 4. A measurable global lower bound, quantiles, and interlacing

The interpolation theorem gives a strictly positive global Gram lower bound for every retained configuration. To avoid any measurable-selection gap, define canonically

\[
 a(\omega)=\min\left\{1,\inf_{m\ge1}
 \lambda_{\min}S(\Lambda(\omega)\cap[-m,m])\right\},
\]

using value one for an empty matrix. Each finite-window matrix is measurable through the sorted finite point coordinates; the countable infimum is measurable. The global Riesz bound makes `a(omega)>0`. Importantly this is one random variable for the **global** retained set, independent of which `R` is later considered. Using only finite-window positive definiteness would not suffice, since its lower constants might tend to zero.

Given any small `epsilon>0`, first choose `delta,eta,L` so the limiting expected deletion fraction is below `epsilon/2`. Next choose a deterministic `b_epsilon>0` with `P(a<b_epsilon)<epsilon²/16`, possible because `a>0` almost surely.

On the event `a>=b_epsilon`, the retained principal submatrix in `[0,R]` has every eigenvalue at least `b_epsilon`. Cauchy interlacing therefore bounds the number of full Gram eigenvalues **strictly below** `b_epsilon` by `D_R`. On the bad event use the trivial bound `N_R`. Consequently

\[
 \mu_R((-1,b_\epsilon))
 \le ED_R/R+E[(N_R/R)\mathbf1_{a<b_\epsilon}].
\]

Cauchy–Schwarz and the variance estimate bound the last term by

\[
 \sqrt{1+1/R}\sqrt{P(a<b_\epsilon)}.
\]

No independence between the point count and the global lower bound is required.

Let `mu` be any weak limit along `R_j->infinity`. The interval `(-1,b_epsilon)` is open, so the correct Portmanteau direction is

\[
 \mu(\{0\})\le\mu((-1,b_\epsilon))
 \le\liminf_j\mu_{R_j}((-1,b_\epsilon))\le\epsilon.
\]

Letting the arbitrary tolerance tend to zero proves `mu({0})=0`. Closed-interval Portmanteau would have the wrong direction for this argument; strict eigenvalue counting and an open interval avoid that issue.

## 5. An explicit factorial moment bound

This proof was independently derived before reading the advocate's draft. It does not need interpolation, thinning, stationarity beyond the correlation densities, or ergodicity.

Choose

\[
 \phi(x)=2\operatorname{sinc}(2x)\operatorname{sinc}(x).
\]

Its Fourier transform is the convolution of the indicators of `[-1,1]` and `[-1/2,1/2]`, equal to one on the frequency band `[-1/2,1/2]`. Also `||phi||_infinity<=2` and, by Cauchy–Schwarz and the elementary sinc² integrals, `||phi||_1<=sqrt2<2`. Thus every `f in H` satisfies `f=phi*f`, pointwise as well as in `L²`, and weighted Cauchy–Schwarz gives

\[
 |f(x)|^2\le2\int|\phi(x-y)||f(y)|^2dy.
\]

For a finite configuration `X_R`, put `W_R(y)=sum_{x in X_R}|phi(x-y)|`. Let `P` be the orthogonal projection onto `H` and let `A_R=sum k_x tensor k_x` on `H`. Its nonzero eigenvalues equal those of `S_R`, and in quadratic-form order

\[
 A_R\le2 B_R,\qquad B_R=P M_{W_R}P.
\]

The positive operator `B_R` is trace class because `integral W_R<infinity`. For normalized eigenvectors `e_j` with eigenvalues `b_j`, scalar Jensen yields

\[
 b_j^m\le\int W_R(y)^m|e_j(y)|^2dy.
\]

Point-evaluation Bessel inequality gives `sum_j|e_j(y)|²<=||k_y||²=1`. Therefore

\[
 \operatorname{Tr}B_R^m\le\int W_R^m,
 \qquad \operatorname{Tr}S_R^m\le2^m\int W_R^m.
\]

The second inequality follows from eigenvalue min–max under `A_R<=2B_R`; operator monotonicity of the power function is not being asserted for `m>1`.

Expand `EW_R(y)^m` by partitions of the `m` factor labels into blocks of equal point indices. For a partition with `k` blocks of sizes `b_1,...,b_k`, `rho_k<=1` bounds its contribution by

\[
 \prod_{j=1}^k\int_0^R|\phi(x-y)|^{b_j}dx.
\]

Integrate in `y`. Bound all but one factor by its full-line integral; integrate the remaining factor exactly. Since
`integral|phi|^b<=||phi||_infinity^{b-1}||phi||_1<=2^b`, the result is at most `R 2^m`, for every partition. There are `Bell_m<=m!` partitions: a simple injection maps each partition to the permutation whose cycles are its blocks written in increasing order. Thus

\[
 E\int W_R^m\le R 2^m m!,\qquad
 \boxed{\int\lambda^m d\mu_R\le4^m m!.}
\]

All exchanges here are of nonnegative quantities and follow from Tonelli and the factorial moment identities.

## 6. Moment determinacy and exactly what remains conditional

The bound for order `m+1` makes the order-`m` moments uniformly integrable. Thus any weak subsequential limit inherits its limiting moments along that subsequence and the same factorial bounds. In particular

\[
 (\int\lambda^{2k}d\mu)^{1/(2k)}\le4((2k)!)^{1/(2k)}\le8k.
\]

Carleman's reciprocal sum diverges, so each weak limit is moment determinate. If the entire moment sequence of `mu_R` converges, any two weak limits have all moments in common, hence are equal; tightness then gives full weak convergence. **Existence of all those moment limits is not proved in this review.** Moment determinacy alone must not be advertised as proving their existence.

The same bound gives a finite exponential moment `integral e^{c lambda}dmu<=1/(1-4c)` for `0<c<1/4`.

## 7. Christoffel minima tend to zero: direct proof

Let

\[
 \Lambda_m(0)=\inf\{\int|p|^2d\mu:\deg p\le m,\ p(0)=1\}.
\]

These values decrease. Suppose their limit were positive. Then evaluation `p->p(0)` would be a bounded functional on the polynomial subspace of `L²(mu)`; extend it to its closure and use Riesz representation to obtain `g in L²(mu)` with `integral p g dmu=p(0)` for every polynomial. No polynomial-density assertion is required.

The signed measure `nu=g mu` has a finite exponential moment by Cauchy–Schwarz for every exponent below `1/8`. Its Laplace transform is analytic in a half-plane containing zero. Its Taylor series at zero is identically one because `integral lambda^k g dmu` is one at `k=0` and zero at all positive integers. Analytic continuation therefore makes that Laplace transform equal to one on the entire right half-plane. But as the real parameter tends to positive infinity, dominated convergence gives its limit `nu({0})=0`, since `mu({0})=0`. Contradiction. Hence `Lambda_m(0)->0`.

This supplies the abstract all-moment step behind the conditional AF§7.2 statement, for the specified expected sine-process law. It does not verify any prime-correlation or zeta trace-moment asymptotic, any claimed exact low moments, or the paper's main theorems.

## Evidence status and useful unresolved questions

The no-atom proof passes the quantifier, normalization, measurability, density and Portmanteau checks above, conditional only on the stated classical interpolation input. The factorial bound and Christoffel implication have independent elementary proofs here. Direct original Seip1995/Beurling1989 proof access remains a source-chain limitation; actual research restatements and an independent Bernstein-to-PW² conversion are preserved rather than silently substituting abstracts.

Concrete remaining questions: prove existence of all expected trace-moment limits directly for this stationary sine process; derive a quantitative small-eigenvalue bound from quantitative interpolation constants and the thinning parameters; and determine an effective decay rate of `Lambda_m(0)`. None of these improvements is assumed in the present conclusions.
