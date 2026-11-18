# Independent review of beta smoothing and the arithmetic obstruction

Reviewer: `/root/corpus`. Date: 2026-11-17. Reviewed `audits/positive_kernel_beta_smoothing_round3.md`, including its optional simplicity refinement. Classification: **independently checked with no issue found in the inspected construction**. The base Bessel quartet and exact log-concavity certificate have their separate third adjudication in `bessel_third_round3.md`. This review checks the extension, its quantifiers and its analytic limitations; it is not a novelty assessment or an RH theorem.

## 1. Exact normalization, with the factor of two pinned down

The beta probability density is proportional to `(δ²-v²)^(3/4)` on `(-δ,δ)`. Its moment recurrence gives

\[
 E v^{2k}=\delta^{2k}\frac{(1/2)_k}{(9/4)_k},\quad
 M_\delta(w)=\sum_{k\ge0}\frac{(\delta^2w^2/4)^k}{k!(9/4)_k}.
\]

Thus the claimed normalized `I_(5/4)` expression is correct, provided it is defined by this even entire series rather than by independently chosen fractional-power branches. In particular `M_delta(0)=1`. Put `c=2πe^(2δ)` and let `F` be the draft's product normalized by `F(1)=F(0)=1`.

The draft uses exactly

\[
 Z(s)=\frac{\pi^{s/2}F(s)}{s(s-1)\Gamma(s/2)}.
\]

This corresponds to `F=2ξ` in the zeta convention, not `F=ξ`. It gives residue **one** at `s=1` and `Z(0)=-1/2`. With this convention the real-axis constant is exactly

\[
 C=\frac{A\Gamma(9/4)}{\pi^{1/4}\delta^{7/4}}.
\]

Using the completion with an extra factor `1/2` would instead double both `C` and the residue. No factor-two correction to the draft's convention is required. The ordinary completed functional equation follows algebraically from `F(s)=F(1-s)`. The function `F` is strictly positive on the entire real axis, so reciprocal gamma supplies exactly simple negative-even trivial zeros; the apparent singularity at zero is removable, leaving only the simple pole at one.

## 2. Source hypotheses and an independent all-complex-zero argument

I inspected the actual official formula passages [DLMF10.32.2](https://dlmf.nist.gov/10.32.E2), [10.21.15](https://dlmf.nist.gov/10.21.E15), [10.21.19](https://dlmf.nist.gov/10.21.E19), [10.17.1–3](https://dlmf.nist.gov/10.17.E3), [10.40.1](https://dlmf.nist.gov/10.40.E1), [10.25.2](https://dlmf.nist.gov/10.25.E2), and [10.27.4](https://dlmf.nist.gov/10.27.E4). These are targeted formula inspections, not whole-chapter audits. The beta integral requires `Re ν>-1/2`; the normalized product and fixed-order root asymptotic cited here allow `ν>=0`; our fixed `ν=5/4` satisfies every such condition. The fixed-order `I` expansion is used only on the positive real axis, inside its stated sector. It is not extrapolated across a Stokes line to prove a vertical bound.

There is also an independent direct completeness check. Write

\[
 j_\nu(z)=\sum_{k\ge0}\frac{(-z^2/4)^k}{k!(\nu+1)_k},\qquad
 M_\delta(w)=j_{5/4}(i\delta w).
\]

If `j_nu(z)=0`, set `y(r)=j_nu(zr)` on `0<r<1`. Direct termwise differentiation gives

\[
 -(r^{2\nu+1}y')'=z^2r^{2\nu+1}y,\quad y(0)=1,\ y(1)=0.
\]

Multiplying by the conjugate solution and integrating gives

\[
 z^2\int_0^1r^{2\nu+1}|y|^2dr
 =\int_0^1r^{2\nu+1}|y'|^2dr>0.
\]

The zero-endpoint boundary term vanishes because `y=1+O(r²)`, `y'=O(r)` and `ν=5/4`; the one-endpoint term vanishes by its Dirichlet condition. Hence `z²` is positive real, so every nonzero zero is real. Ordinary ODE uniqueness at the nonsingular endpoint excludes simultaneous zeros of `j_nu` and its derivative. This verifies that the beta factor has only simple imaginary zeros without inferring completeness merely from a list of real Bessel zeros.

The product gives `M_delta(w)=product_k(1+δ²w²/j_(5/4,k)²)`, and the fixed-order asymptotic gives `N_beta(X)=δX/π+O(1)`. Multiplying by the Bessel factor adds its count with multiplicities. Since `log(c/(2π))=2δ`, its linear shift `-δX/π` cancels exactly. This proves the stated smooth RVM count with `O(1)` error for each fixed constructed function, not a family-uniform bound as `δ` tends to zero. Arbitrary tuned roots may have coincident line zeros; their multiplicities are at most two. This does not affect the count or Li sums.

## 3. Strict log-concavity, including the singular beta endpoints

The compact beta convolution is positive, even and smooth: derivatives fall on the smooth positive base kernel, not on the nonsmooth beta endpoints. Compact shifts preserve double exponential bounds for every derivative and every bilateral exponential moment. The parameter range is valid: `0<δ<=1/100` gives `6<c<7` using `3<π<22/7` and `e^(1/50)<50/49`, exactly within the base certificate.

I reconstructed the draft's one-dimensional Brascamp–Lieb argument. At fixed `x`, use probability density `p(v)` proportional to `k(x-v)b_delta(v)`, and set `V=-log k`, `W=-log b_delta`, `U=V(x-v)+W(v)`. Then

\[
 (\log(k*b_\delta))''=-EV''+\operatorname{Var}(V'),\quad
 U''=V''+W''>0,
\]
\[
 W''=\tfrac32(\delta^2+v^2)/(\delta^2-v^2)^2.
\]

For centered `φ(v)=V'(x-v)-EV'`, set `F(v)=integral_(-δ)^v φp` and `u=F/p`. Both endpoint values of `F` vanish. The identities

\[
 E\phi^2=E(u')^2+EU''u^2,\qquad E\phi^2=-E\phi'u
\]

follow by integrating on truncated support intervals and taking limits. Every boundary term checks: at endpoint distance `d`, `p` is comparable to `d^(3/4)`, `F=O(d^(7/4))`, `u=O(d)`, `u'=O(1)` and `U'=O(1/d)`. Hence both `φup` and `U'u²p` vanish; the squared and derivative terms are integrable. Cauchy–Schwarz then gives

\[
 \operatorname{Var}(V')\le E\frac{(V'')^2}{V''+W''},\quad
 (\log(k*b_\delta))''\le-E\frac{V''W''}{V''+W''}<0.
\]

This proves the strictly negative pointwise second logarithmic derivative, including at zero. An invocation of strict Jensen concavity alone would not have proved this stronger differential statement. No uninspected convolution theorem is needed.

## 4. The right-axis coefficient and failure of a Dirichlet expansion

For fixed constructed parameters, the gamma-expectation integral for `K_(σ/2-1/4)(c)` gives relative first correction `-c²/(2σ)` with a rigorous `O(σ^-2)` remainder: use the inverse first and second gamma moments and `0<=e^-y-1+y<=y²/2`. At the beta right endpoint the density is proportional to `y^(3/4)(1-y/(2δ))^(3/4)`. Its first two Laplace terms give relative correction `-21/(32δw)`, with the remainder justified by a Taylor bound near that endpoint and an exponentially small complementary tail.

The remaining reciprocal-σ coefficients are `5/16` from the gamma ratio, `-2` from `Q_T(σ-1/2)/σ^4`, `7/8` from `(σ-1/2)^(-7/4)/σ^(-7/4)`, and `+1` from `1/(1-1/σ)`. Their sum is exactly `3/16`. Retuning `c` cancels the real exponential and gives

\[
 Z(\sigma)=C\left[1-\frac{b}{\sigma}+O(\sigma^{-2})\right],\quad
 b=c^2/2+21/(32\delta)-3/16>0.
\]

Indeed `b>1335/16` on the allowed parameter interval. The exact standard-library Fraction checks are in `experiments/code/beta_smoothing_third_round3.py` and its result JSON; they verify the beta moments, tuning polynomial, and this finite coefficient algebra. The analytic remainder proofs remain separate from those finite checks.

Once `C=1`, a conventional Dirichlet series absolutely convergent at a real `σ0` would satisfy `a1=1` and
`|Z(σ)-1| <= 2^(-(σ-σ0)) sum_(n>=2)|an|n^(-σ0)`. This contradicts the nonzero `-b/σ` term. Conditional convergence somewhere cannot evade the conclusion: bounded terms at that point imply absolute convergence sufficiently far to its right. The obstruction is the discrete arithmetic expansion, even after its leading right-axis limit is normalized correctly.

## 5. Tuning and a uniform explicit Li prefix

The draft's explicit endpoint argument is valid. At `δ=1/100`, integrating the Bessel integral only over `[-1/10,1/10]` gives `K_(1/4)(c)>1/(5*3^9)`. Also `M_delta(1/2)>=1`, `Q_T(1/2)>=T^4`, `Γ(9/4)<2`, and `δ^(7/4)>10^-4`. Consequently `C(T,1/100)<100000*3^9/T^4<1` for `T>=256`. Meanwhile `C(T,δ)->infinity` as `δ->0`. Continuity supplies a tuned root for every such `T`. Since `T_N=10N(8N²+50)>=580`, the fixed explicit height in the main theorem really suffices for both requirements.

The stronger uniform Li proof also checks. For every allowed `c`, min–max comparison with the odd half-line oscillator and the first `j=N²` sine modes on `[0,1]` gives an ordinate between `2N` and `B_N=8N²+50`. Its single conjugate pair contributes more than `1/(6B_N²)` to each first-`N` Li coefficient. Every other Bessel pair and every beta pair contributes a nonnegative quantity. The quartet has contribution of absolute value `<8N²/T²` for `T>=N`; at `T_N` this is `<2/(25B_N²)<1/(12B_N²)`. Thus the advertised remaining margin `1/(12B_N²)` is rigorous and does not require a continuous tuning branch or locally uniform convergence of a chosen family. Paired products contain no hidden linear exponential factor because they are even of order one, and their reciprocal-square ordinates sum.

The asymptotic for any choice of tuned root also checks:

\[
 \delta_T T^{16/7}\longrightarrow
 \left[\frac{\Gamma(9/4)}{\pi^{1/4}K_{1/4}(2\pi)}\right]^{4/7}.
\]

The limit is not needed for the stronger uniform prefix proof.

## 6. Complex growth and a remaining moment obstruction

For `ν=a+ib` with bounded real `a` and large `|b|`, the exact `I` series has remainder `O(1/|b|)`, since each factor `|m+ν|>=|b|`. Gamma Stirling and the sine connection formula therefore give

\[
 |K_{a+ib}(c)|\ll e^{-\pi|b|/2}|b|^{|a|-1/2}.
\]

This uses both `I_nu` and `I_-nu`; it remains valid when `a=0`. With `a=(σ-1/2)/2`, `b=t/2`, it gives the correct Bessel exponential `e^(-π|t|/4)`.

Independently, for bounded real `q`, the beta Fourier amplitude `b_delta(v)e^(qv)` vanishes as endpoint distance `d^(3/4)`. Its first and second derivatives are bounded by constants times `d^(-1/4)` and `d^(-5/4)`. Integrate once by parts, remove endpoint layers of width `1/|t|`, then integrate once more on the remaining interval. The endpoint-layer integral of the first derivative is `O(|t|^-3/4)`; the remaining derivative and boundary terms have the same bound. Thus `M_delta(q+it)=O(|t|^-7/4)`. This directly justifies the needed vertical estimate without any inappropriate continuation of a one-exponential `I` asymptotic.

The polynomial quartet and reciprocal gamma now give exactly

\[
 Z(\sigma+it)\ll(1+|t|)^{\max(1/2-\sigma,0)}
\]

as `|t|` tends to infinity, uniformly for `σ` in a fixed finite interval, with constants depending on this fixed model. Thus its critical-line values are bounded and its critical-line squared integral over heights `[1,X]` is `O(X)`. Any additional requirement of unbounded mean square divided by `X` rules this model out. In particular it cannot reproduce zeta's second-moment asymptotic. The latter classical zeta theorem was not independently source-audited in this scoped review; the derived boundedness and `O(X)` conclusion need no such external input. Matching upper growth bounds is therefore materially weaker than matching moment asymptotics.

There is also an exact maximal-modulus statement, not just an order estimate. Let `M_F(r)=max_(|w|<=r)|F(1/2+w)|`. Positivity and evenness of the centered kernel imply `M_F(r)=F(1/2+r)`. With `C=1`, it follows that

\[
 M_F(r)=(r+1/2)(r-1/2)\pi^{-(r+1/2)/2}
 \Gamma((r+1/2)/2)\,[1-b/r+O(r^{-2})].
\]

This matches the standard `2ξ` completion's leading maximal-modulus scale, including its leading constant; in logarithmic form it has leading terms `r log(r/(2πe))/2 +(7/4)log r +(3/4)log2 +(1/4)logπ +O(1/r)`. These stronger growth facts do not repair the algebraic Dirichlet-series tail.

## 7. Optional simplicity: the change in quantifiers matters

The main fixed-height `T_N` theorem correctly permits factor collisions. The separate all-simple existence refinement is also valid. Set

\[
 H(\delta)=\frac{\Gamma(9/4)}{
 \pi^{1/4}\delta^{7/4}K_{1/4}(2\pi e^{2\delta})M_\delta(1/2)},\quad
 T(\delta)^2=\sqrt{H(\delta)+1/16}-5/16.
\]

The exact identity `Q_T(1/2)=(T²+5/16)²-1/16` enforces `C=1`, and `T(delta)->infinity` as `delta->0`. Each simple ordered Bessel ordinate `γ_j(c)` is real analytic in `c` by the implicit function theorem, and extends through `c=2π`. The collision equation `δγ_j(2πe^(2δ))=j_(5/4,m)` is therefore nonidentically real analytic: at zero its left side is zero and its right side is positive. Its zeros are discrete; the union over countably many pairs is countable. Outside this exceptional set, the two imaginary zero sets do not collide. The off-line quartet cannot meet either of them. Arbitrarily small nonexceptional `δ` therefore supply all-simple models with `T>=T_N`, retaining every other stated property.

This proves existence with an adjustable real quartet height. It does **not** certify that the tuned root at any prescribed `T_N`, or any named rational/algebraic `δ`, is nonexceptional. The distinction is preserved in the reviewed draft.

## Review conclusion and source counts

The stronger countermodel survives the independent review. Its exact standard completion, functional equation, pole/residue, trivial zeros, normalized right limit, vertical growth, sharp smooth count, positive strictly log-concave kernel, finite Li prefix and optional all-simple zero set remain compatible with four off-line zeros. The retained obstruction is explicit: a nonzero algebraic right tail prevents a discrete Dirichlet expansion, and bounded critical-line values prevent the actual zeta mean-square growth. No inference against an argument retaining genuine arithmetic information follows.

No new full-paper reading count is earned by this review. Official formula passages were actually inspected; direct attempts to fetch their `.tex` endpoints returned 403, and the web tool supplied the readable official passages. The local formula manifest records that distinction. No numerical root of the tuning equation is used as proof or claimed to have been rigorously enclosed. Novelty remains unassessed.
