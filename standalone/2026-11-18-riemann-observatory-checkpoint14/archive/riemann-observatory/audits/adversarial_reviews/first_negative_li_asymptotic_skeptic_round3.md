# First negative Li coefficient in the tuned beta countermodel

2026-11-17. Independent proof by `/root/li_skeptic`; independent corpus scrutiny requested. This concerns only the explicitly constructed beta countermodel, not the true zeta function. The exponential masking mechanism is classical; no novelty claim. The complete model, all normalization conventions and tuning equation are in `audits/positive_kernel_beta_smoothing_round3.md`.

## Statement

For each sufficiently large real `T`, choose **any** solution `delta_T in (0,1/100)` of the beta tuning equation `C(T,delta_T)=1`. Define the corresponding normalized entire function `F_T`, with the off-line quartet at `s=1/2 +/-1/4 +/-iT`. Let

\[
 n_-(T)=\min\{n\ge1:\lambda_n(F_T)<0\}.
\]

Then this minimum exists and

\[
 \boxed{n_-(T)\sim8T^2\log T.}
\]

The conclusion is uniform over all choices of tuned root. It applies as well along the generic-parameter subfamily whose zeros are all simple. This is an asymptotic statement; no explicit error constant or numerical first-negative index is asserted.

## 1. Exact quartet expression

Keep `a=1/4`. Put

\[
 z_T=1-\frac1{1/2-a+iT}=e^{\eta_T+i\theta_T},
\]

with `eta_T>0`, `theta_T>0` the small positive argument. Reflection and conjugation give the four transformed roots `e^{+/-eta_T +/-i theta_T}`. Therefore the quartet contributes exactly

\[
 q_n(T)=4\big[1-\cosh(n\eta_T)\cos(n\theta_T)\big].
\]

Here

\[
 \eta_T=\frac12\log\frac{T^2+(1/2+a)^2}{T^2+(1/2-a)^2}
       =a/T^2+O(T^{-4}),\qquad
 \theta_T=T^{-1}+O(T^{-3}).
\]

The exponential rate, not just the oscillation frequency, is essential. In particular the onset scale is much larger than `T`.

## 2. Uniform baseline asymptotic from the zero count

For `6<=c<=7`, the positive Bessel line-ordinate count satisfies uniformly

\[
 N_c(y)=\frac{y}{2\pi}\log(y/c)-\frac{y}{2\pi}+O(1).
\]

The uniformity follows directly from the earlier I-series/gamma-phase proof: `c^2/4` stays in a compact interval, all large-order remainder estimates are uniform, and the bounded initial zero count is uniform by monotonic eigenvalue comparison. Define `theta(y)=2arctan(1/(2y))`. The normalized Bessel Li coefficient is

\[
 k_n(c)=2\int_0^\infty[1-\cos(n\theta(y))]\,dN_c(y).
\]

Subtract the differentiable main count. Its remainder is bounded on the entire positive half-line after setting `ylogy=0` at zero. Stieltjes integration by parts bounds the error by `O(n)` uniformly in `c`, since

\[
 \theta'(y)=-1/(y^2+1/4),\qquad
 \int_0^\infty |n\theta'(y)\sin(n\theta(y))|dy\le\pi n.
\]

There is no boundary contribution: the count remainder vanishes at zero and the trigonometric kernel tends to zero at infinity.

For `y>=1`, `|theta(y)-1/y|<=1/(12y^3)`. Replacing the phase by `1/y` in the smooth integral costs `O(n^{1/3}log(n+2))`, splitting at `y=n^{1/3}` and using `|cosu-cosv|<=min(2,|u-v|)`. The range `0<y<1` costs only a bounded amount because `|log y|` is integrable there. Substitute `u=n/y` in the resulting integral. Since

\[
 \int_0^\infty\frac{1-\cos u}{u^2}du=\pi/2,
 \qquad
 \int_0^\infty\frac{(1-\cos u)|\log u|}{u^2}du<\infty,
\]

one obtains

\[
 k_n(c)=\tfrac12n\log n+O(n)
\]

uniformly for `c in [6,7]`. In particular there are constants `n_0` and positive `c_0,C_0`, independent of the tuned choice, such that
`c_0 nlogn<=k_n(c)<=C_0 nlogn` for `n>=n_0`.

Every fixed `k_n(c)` is strictly positive and continuous in `c`; compactness gives a positive uniform lower margin for each finite range of `n`. Continuity follows from the analytic nonvanishing neighborhood of `s=1`, uniformly on compact positive `c` intervals.

## 3. The beta contribution is negligible on the detection scale

The exact even series gives

\[
 M_\delta(w)=1+(\delta^2/9)w^2+O(w^4).
\]

Its paired line-zero product consequently has `sum gamma_j^{-2}=delta^2/9`. Each pair contributes between zero and `n^2/gamma_j^2`, because `2(1-cosv)<=v^2` and `2arctan(1/(2gamma))<=1/gamma`. Thus

\[
 0\le b_n(\delta)\le n^2\delta^2/9.
\]

The tuning theorem gives, for every selected branch,
`delta_T~D T^{-16/7}` with a fixed positive constant `D`. Hence for `n=O(T^2logT)` the beta contribution is `O(T^{-4/7}log^2T)=o(1)`. Normalizing constants do not contribute to Li coefficients.

## 4. No earlier negative coefficient

Fix `epsilon in (0,8)` and let `L_T=(8-epsilon)T^2logT`. Since

\[
 q_n(T)\ge-4[\cosh(n\eta_T)-1]
          \ge-2(n\eta_T)^2e^{n\eta_T},
\]

it suffices to compare this bound with the baseline. For `n>=n_0>=3`, the ratio to `c_0 nlogn` is at most a constant times

\[
 \eta_T^2\frac{n e^{n\eta_T}}{\log n}.
\]

The displayed `n`-dependent expression is increasing for `n>=3`. At `n=L_T`,

\[
 L_T\eta_T=(2-a\epsilon+o(1))\log T,
\]

so this ratio is `O(T^{-a epsilon/2})`, tending to zero (using a slightly weakened exponent to absorb the remainder). All coefficients with `n_0<=n<=L_T` are therefore positive for large `T`, since the beta contribution is nonnegative. The finitely many smaller indices are positive by their compact uniform baseline margin and the quartet bound `O(n^2/T^2)`. Thus `n_-(T)>L_T` for large `T`.

## 5. A negative coefficient just above the scale

Let `U_T=(8+epsilon)T^2logT`. Choose an integer `m` nearest `U_T theta_T/(2pi)` and then an integer `n` nearest `2pi m/theta_T`. Then

\[
 n=U_T+O(T),\qquad
 |n\theta_T-2\pi m|\le\theta_T/2,
 \quad\cos(n\theta_T)=1-O(T^{-2}).
\]

Furthermore `n eta_T=(2+a epsilon+o(1))logT`. Thus the negative quartet term has magnitude of order `T^{2+a epsilon+o(1)}`, while the Bessel baseline is `O(T^2log^2T)` and the beta contribution is `o(1)`. It follows that this `lambda_n(F_T)` is negative for large `T`. In particular the minimum exists and `n_-(T)<=U_T+O(T)`.

Together the lower and upper bounds for arbitrary positive `epsilon` prove `n_-(T)/(T^2logT)->8`.

## Meaning and scope

The earlier constructive height `T_N=10N(8N^2+50)` was deliberately conservative. This asymptotic identifies the actual detection scale for this particular model: a quartet at height `T` can be hidden from a Li scan through approximately `8T^2logT` coefficients. It does not give a universal finite Li certification rule for zeta or other functions.

Discovery-only priority search found existing discussions of the heuristic scale `(T^2/a)log(nlogn)` and the classical eventual exponential domination mechanism. These snippets are not primary-source audits. Lagarias's2007 paper *Li coefficients for automorphic L-functions* is a primary lead for asymptotic/finite-height context; it was subsequently read in the precise portions recorded in the priority addendum below. The model-specific asymptotic above is an independent proof, with priority unassessed, not an asserted new theorem in the literature.

## Independently challenged refinement: the next term and constant

Corpus independently proposed the stronger expansion below. Skeptic rederived its constant and the all-earlier-index argument, and found no issue. For fixed `a=1/4`,

\[
 n_-(T)=\frac{T^2}{a}
   \left[2\log T+2\log\log T-\log a+o(1)\right].
\]

Equivalently

\[
 n_-(T)=8T^2\log T+8T^2\log\log T
            +8(\log2)T^2+o(T^2).
\]

To prove it let `L=logT`, `Y_0=2L+2logL-loga`, and define the continuous envelope ratio

\[
 R_T(n)=\frac{4e^{n\eta_T}}{n\log n}.
\]

At `n=(T^2/a)(Y_0+/-epsilon)`, `n eta_T=Y_0+/-epsilon+o(1)` and `nlogn~4T^2L^2/a`, so `R_T(n)->e^{+/-epsilon}`. The constant is `-loga`: the two `log2` terms from `log n` and `loglogn` cancel the `log4` in the envelope equation `e^{n eta}=nlogn/4`.

For `n>=T^2L/a`, the derivative of `log R_T` is `eta_T-1/n-1/(nlogn)>0` for large `T`. On the interval from that point to the minus endpoint, the exact bound `q_n>=-2e^{n eta_T}` and uniform baseline ratio `k_n/(nlogn/2)=1+O(1/logn)` therefore imply positivity: the envelope stays a fixed proportion below one. The previous all-earlier proof already covers every index below `T^2L/a`.

At the plus endpoint choose a phase-aligned integer within `O(T)`, as before. This is only `o(T^2)` displacement and changes `n eta` by `o(1)`. Thus the quartet/base ratio tends to `e^epsilon>1`; the beta term is negligible, so that coefficient is negative. Bracketing for every fixed positive `epsilon` proves the claimed `o(T^2)` remainder.

No linear coefficient in the baseline asymptotic, and no numerical zero or Li computation, is needed for this refinement. It remains a model-specific quantified obstruction, not a universal detection theorem and not a novelty assertion.


## Inverse-scale corollary and original-source checkpoint

Root independently checked the refined envelope argument. For every fixed `epsilon in (0,1/2)`, the tuned model at `T=(1/2+epsilon)sqrt(N/logN)` has its first negative index beyondN for sufficiently largeN, while at `T=(1/2-epsilon)sqrt(N/logN)` it occurs belowN. Indeed `8T²logT/N` tends to `(1+/-2epsilon)²`. These are asymptotic inequalities without an effectiveN0; they do not replace the earlier explicit finite certificate `T_N=10N(8N²+50)`.

Original-source reading was then completed for the relevant priority context: existing canonical `PAPER-L001`, Lagarias2007, introductionpp1689–1695, definitions/Theorem2.1pp1696–1699, and completeSection6pp1721–1726; page1694 additionally rendered. It explicitly records finite-height masking and credits eventual exponential domination to Bombieri–Lagarias1999,Theorem1(c). Full52-page reading is not claimed. Source and scoped contour notes: `audits/lagarias2007_contour_scope_round3.md`. This reading confirms the historical mechanism, without establishing priority for the exact beta-model first-negative asymptotic.
