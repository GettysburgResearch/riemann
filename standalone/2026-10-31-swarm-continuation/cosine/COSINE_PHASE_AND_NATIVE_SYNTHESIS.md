# A lossless cosine phase and an exact native sine-synthesis problem

Status: proposed component theorems, with complete proofs below. The construction replaces the earlier exponentially ill-conditioned *noise-removal* route by a deterministic cosine transform. It carries the actual Bagchi source and its target, not only the high-height limiting law. No RH proof or improved zero-free boundary is asserted.

The new ingredients assembled here are: an explicit whole-strip polynomial-cost factorization of the native arithmetic law; its lossless realization at alpha=3/2; the exact transformed native generators including their necessary logarithmic compensation; a complete-source frequency-tail bound; and a quantitative audit of why compact Möbius synthesis has not yet solved the norm problem. Classical cosine/Mellin, Nyman–Beurling, and co-Poisson machinery is credited in SOURCES.md. No worldwide priority claim is made.

## 1. The whole-strip factorization

For Fourier multipliers use `hat f(t)=(2*pi)^(-1/2) integral_R f(x)e^(itx) dx`. For a probability density its characteristic function uses the same positive exponential without the prefactor. The Mellin convention is `Mf(s)=integral_0^infinity f(u)u^(s-1)du`; these conventions fix the signs in (3), (7), and (8).

Recall the actual high-height arithmetic law from the previous packet:

\[
 C(\alpha)=\frac{\pi}{\Gamma(1+\alpha)\sin(\pi\alpha/2)},\qquad
 p_\alpha(x)=\frac2{C(\alpha)}e^{-\alpha x}(1-\cos(e^x)).
\]

Here the zeta off-line strip corresponds to `1<alpha<2`. Its characteristic function is

\[
 \varphi_\alpha(t)=\frac{C(\alpha-it)}{C(\alpha)}.
\tag{1}
\]

Let `theta=2-alpha`, so `0<theta<1`, and define

\[
 m(s)=\sqrt{\frac2\pi}\,\Gamma(s)\cos\frac{\pi s}{2},\qquad
 q_\alpha(x)=\alpha(\alpha-1)
  \big(e^{-(\alpha-1)x}-e^{-\alpha x}\big)\mathbf1_{x>0}.
\tag{2}
\]

The density q is the convolution of independent exponential laws of rates alpha and alpha-1. In particular it is positive and infinitely divisible. Its characteristic function is

\[
 \widehat q_\alpha(t)=
 \frac{\alpha(\alpha-1)}{(\alpha-it)(\alpha-1-it)}.
\]

**Theorem 1 (polynomial-cost exact phase transfer).** For every `1<alpha<2`,

\[
 \varphi_\alpha(t)=
 \widehat q_\alpha(t)\frac{m(\theta+it)}{m(\theta)}.
\tag{3}
\]

The multiplier `M_alpha(t)=m(theta+it)/m(theta)` is nonzero on the real line, and for constants `0<c_alpha<=C_alpha<infinity`,

\[
 c_\alpha(1+t^2)^{(3/2-\alpha)/2}
 \le |M_\alpha(t)|\le
 C_\alpha(1+t^2)^{(3/2-\alpha)/2}.
\tag{4}
\]

If T_alpha is the corresponding Fourier multiplier, then for every real u it is an isomorphism

\[
 T_\alpha:H^u(\mathbb R)\longrightarrow
 H^{u-(3/2-\alpha)}(\mathbb R).
\tag{5}
\]

At alpha=3/2 it is unitary on every Sobolev space H^u, with exactly unit norm and unit inverse norm. This is an operator statement, not a positivity-preserving convolution assertion.

**Proof.** Two integrations by parts in the absolutely convergent integral defining C, with the last cosine integral understood by Abel convergence, give for `1<Re a<2`

\[
 C(a)=\frac{2\Gamma(2-a)\cos(\pi(2-a)/2)}{a(a-1)}.
\tag{6}
\]

The first integration has boundary term zero because `(1-cos u)u^{-a}` vanishes at zero and infinity. The second has zero boundary terms because `sin(u)u^{1-a}` does likewise; the remaining integral is the standard Mellin cosine integral in `0<Re(2-a)<1`. Dividing (6) at `a=alpha-it` and `a=alpha` proves (3).

Neither gamma nor cosine vanishes on the line `theta+iR`, since `0<theta<1`. Stirling and the elementary cosine asymptotic give

\[
 |m(\theta+it)|=|t|^{\theta-1/2}(1+O_\theta(|t|^{-1})).
\]

Indeed `sqrt(2/pi)*sqrt(2*pi)/2=1`, and the exponential growth of cosine cancels gamma's exponential decay. Continuity and nonvanishing on any compact t interval prove the global two-sided bound (4). Multiplication by this symbol and its reciprocal proves (5) directly from the Fourier definition of H^u. At theta=1/2 the reflection and duplication formulas give

\[
 m(\tfrac12+it)
 =2^{it}\frac{\Gamma(1/4+it/2)}{\Gamma(1/4-it/2)},
\tag{7}
\]

which has modulus one, and `m(1/2)=1`. This proves the unitary assertion. ∎

### Concrete operator, not only a gamma quotient

The scale-invariant cosine/inversion unitary and its gamma phase are classical; Burnol's treatment cited in SOURCES.md explicitly uses Fourier followed by inversion. The present source-specific calculation uses the unitary cosine transform and inversion

\[
 (\mathcal C f)(u)=\sqrt{\frac2\pi}\int_0^\infty f(v)\cos(uv)\,dv,
 \qquad (If)(u)=u^{-1}f(1/u).
\]

For `W_theta f(x)=e^{theta x}f(e^x)`, initially on compact smooth functions away from zero,

\[
 T_\alpha=\frac1{m(\theta)}W_\theta\mathcal C I W_\theta^{-1}.
\tag{8}
\]

The Mellin formula `M(Cf)(s)=m(s)Mf(1-s)` proves (8); the right side is then extended through (5). The weighted physical norm corresponding to W_theta is `L²((0,infinity),u^(2theta-1)du)`. W_(1/2), C, and I are all unitary for their indicated unweighted L² spaces.

For the compact triangular function `h(u)=(1-u)_+`, direct integration gives

\[
 (\mathcal C h)(u)=\sqrt{\frac2\pi}\frac{1-\cos u}{u^2},
 \qquad q_\alpha=\alpha(\alpha-1)W_\theta Ih.
\]

Thus `T_alpha q_alpha=p_alpha` exactly. This realizes the native density without adding log-gamma noise. The earlier exponential factor `exp(pi |t|/4)` was the cost of undoing that particular positive convolution, not a universal cost for every deterministic source transformation.

Unitary does not mean causal or pointwise positive. For example, (7) has poles in the upper half-plane. T does not preserve products, and a Gram form with multiplication by p does not turn into the analogous Gram form with multiplication by q by merely substituting (3). Any positivity transfer must conjugate the entire operator and the test vectors.

## 2. Carrying the exact arithmetic source and target

Let

\[
 H=\ell^2\bigl(\mathbb N,1/[k(k+1)]\bigr),\quad
 b_n(k)=\{k/n\},\quad n\ge2.
\]

Let `E_N` be the squared H distance of 1 to the span of `b_2,...,b_N`. Define isometries onto closed subspaces by

\[
 (Ef)(u)=f(\lfloor1/u\rfloor)\mathbf1_{0<u\le1},\qquad
 (Jf)(x)=e^{-x/2}f(\lfloor e^x\rfloor)\mathbf1_{x\ge0}.
\tag{9}
\]

Their norm identities follow from the cell lengths
`1/k-1/(k+1)=1/[k(k+1)]`; also `J=W_(1/2) I E`.

Write `U=T_(3/2)`. Since I²=1,

\[
 UJ=W_{1/2}\mathcal C E.
\tag{10}
\]

**Theorem 2 (exact native sine synthesis).** Define the entire odd function

\[
 S(y)=\sum_{k\ge1}\left(\sin(y/k)-y/k\right)
 =\sum_{j\ge1}\frac{(-1)^j\zeta(2j+1)}{(2j+1)!}y^{2j+1},
\tag{11}
\]

and, for integers n>=2,

\[
 V_n(y)=\frac yn\log n+\frac1nS(y)-S(y/n).
\tag{12}
\]

Then

\[
 (UJ1)(\log y)=\sqrt{\frac2\pi}\,y^{-1/2}\sin y,
\]

\[
 (UJb_n)(\log y)=\sqrt{\frac2\pi}\,y^{-1/2}V_n(y),
\tag{13}
\]

and for every N,

\[
 E_N=\frac2\pi\inf_{c_2,\ldots,c_N}
 \int_0^\infty
 \left|\sin y-\sum_{n=2}^Nc_nV_n(y)\right|^2\frac{dy}{y^2}.
\tag{14}
\]

This is an equality of the complete native finite minimization problems, with the same coefficients and the exact target. No limit or asymptotic source replacement occurs.

**Proof.** The series (11) is locally normally convergent by the cubic Taylor bound. Termwise expansion on compact disks gives its displayed zeta series. Integrating the literal reciprocal cells gives

\[
 y\int_0^1(Eb_n)(u)\cos(yu)\,du
 =\sum_{k\ge1}b_n(k)
  \left(\sin(y/k)-\sin(y/(k+1))\right).
\tag{15}
\]

This converges absolutely for real y, because its terms are bounded by `|y|/[k(k+1)]`. Its complex version converges locally normally with an additional compact exponential constant. Summation by parts uses

\[
 b_n(k)-b_n(k-1)=\frac1n-\mathbf1_{n\mid k}.
\]

The resulting harmonic sums cannot be rearranged separately. At cutoff K their difference is

\[
 \frac1n\sum_{k\le K}\sin(y/k)
 -\sum_{j\le K/n}\sin(y/(nj)).
\]

The boundary term from summation by parts tends to zero. Subtract the linear terms inside each sum. The nonlinear sums converge to `S(y)/n-S(y/n)`, while the remaining harmonic difference is

\[
 \frac yn\bigl(H_K-H_{\lfloor K/n\rfloor}\bigr)
 \longrightarrow\frac yn\log n.
\]

This proves (12)–(13). Applying the unitary map (10) to the residual and changing variable `y=e^x` proves (14). ∎

The compensator is essential. In particular `V_n'(0)=(log n)/n`, equal to the exact native mean `L_1(b_n)`. Omitting it changes the source. The finite cutoff identity in the proof makes its origin unambiguous.

### Dilation structure and discrete sampling

The generators satisfy the exact cocycle identity

\[
 V_{mn}(y)=\frac1nV_m(y)+V_n(y/m).
\tag{16}
\]

In the native space it corresponds to
`b_(mn)(k)=b_m(k)/n+b_n(floor(k/m))`. For arbitrary f with f(0)=0, the operator `P_m f(k)=f(floor(k/m))` satisfies

\[
 \|P_m f\|_H^2=\frac1m\|f\|_H^2,
\tag{17}
\]

by telescoping the weights on each block `mj<=k<m(j+1)`. Hence the actual arithmetic dilation action survives the transform.

Since Ef is supported on (0,1), ordinary cosine-series Parseval gives another exact complete norm formula for the residual:

\[
 \left\|1-\sum c_nb_n\right\|_H^2
 =\left|1-\sum c_n\frac{\log n}{n}\right|^2
 +\frac2{\pi^2}\sum_{m\ge1}\frac1{m^2}
   \left|\sum c_nV_n(\pi m)\right|^2.
\tag{18}
\]

The infinite sum is retained. Finite sampled agreement is not a density theorem.

## 3. Zero-functionals are transported, with target one

For `Re s>1/2`, the bounded native functional is

\[
 L_s(f)=\sum_{k\ge1}f(k)(k^{-s}-(k+1)^{-s})
       =s\int_0^1(Ef)(u)u^{s-1}\,du.
\tag{19}
\]

It obeys

\[
 L_s(1)=1,\qquad L_s(b_n)=\zeta(s)(n^{-1}-n^{-s}).
\tag{20}
\]

The usual summation-by-parts proof first applies for Re s>1 and then continues analytically. Its continuous representer has squared norm `|s|²/(2Re s-1)`; orthogonal projection to the native step subspace gives the smaller exact norm from the previous packet.

Under (10), transform that representer as well as the source. Equivalently, pair `C Ef` with `C[conjugate(s)u^(conjugate(s)-1)1_(0,1)]`. The target remains one. At a hypothetical zero rho, every finite residual in (14) still evaluates to one. Derivative functionals at multiple zeros transport in the same way. Unitarity cannot erase this information.

### Polynomial smoothing also retains the zero obstruction

The weighted family T_alpha has a particularly useful property that the former gamma-noise inverse did not provide by itself.

**Theorem 3 (continuous dual evaluation after polynomial transfer).** Fix `1<alpha<2` and `Re s>1/2`. There is an explicitly defined `h_(alpha,s) in L²(R)` such that, for every bounded native f,

\[
 L_s(f)=\langle T_\alpha Jf,h_{\alpha,s}\rangle_{L^2}.
\tag{21}
\]

All finite native residuals lie in the domain in (21). Consequently, at every zeta zero rho with Re rho>1/2,

\[
 \left\|T_\alpha J\left(1-\sum c_nb_n\right)\right\|_2^2
 \ge \|h_{\alpha,\rho}\|_2^{-2}>0.
\tag{22}
\]

For `3/2<=alpha<2`, T_alpha is bounded on L², and therefore

\[
 \mathrm{RH}\ \Longleftrightarrow\
 \inf_{c_2,\ldots,c_N}
 \left\|T_\alpha J\left(1-\sum_{n=2}^Nc_nb_n\right)\right\|_2
 \longrightarrow0.
\tag{23}
\]

No coefficient-budget assumption is required in (22) or (23). This is a transported classical criterion, not a proof that its minima tend to zero.

**Proof.** Use the inner product linear in the first argument. Choose one real smooth cutoff chi equal to zero on `(-infinity,-1]` and one on `[0,infinity)`, and put

\[
 w_s(x)=\overline s\,e^{(1/2-\overline s)x}\chi(x).
\]

It is a Schwartz function because Re s>1/2. Since Jf vanishes on the negative half-line, direct cell integration gives `L_s(f)=<Jf,w_s>`. Define, with any fixed unitary Fourier normalization,

\[
 \widehat h_{\alpha,s}(t)=
 \frac{\widehat w_s(t)}{\overline{M_\alpha(t)}}.
\tag{24}
\]

The reciprocal multiplier grows only polynomially by (4), so (24) belongs to L². Plancherel proves (21). The native domain assertion follows from the regularity lemma below, because the positive order `3/2-alpha`, when positive, is less than 1/2. Equations (20)–(21) prove (22).

For alpha>=3/2, boundedness and the classical native criterion give the forward implication in (23). Conversely, if the transformed minima tend to zero, (22) excludes every off-line zero in Re s>1/2; the functional equation gives RH. For alpha<3/2, (22) still holds, but the converse density implication from RH is not asserted here, since T_alpha then has positive order. ∎

The cutoff extension in (24) matters: zero extension of the exponential would have an artificial boundary jump. The native support allows a smooth extension on the unused negative half-line. This is why polynomial deconvolution of the dual functional is harmless at every fixed s.

## 4. Native regularity and quantitative stability

**Lemma.** If `|f(k)|<=B` and `E=||f||_H²`, then for every `0<r<1/2`,

\[
 \|Jf\|_{H^r}^2\le A_r B^{4r}E^{1-2r}.
\tag{25}
\]

The constant is independent of f and its period or support.

**Proof.** On the logarithmic cell `I_k=[log k,log(k+1))`, write `g_k(x)=f(k)e^{-x/2}1_(I_k)`. The Gagliardo seminorm of this single cell is at most

\[
 C_r |f(k)|^2 k^{-1}|I_k|^{1-2r}
 \le C_r |f(k)|^2 k^{-2+2r}.
\]

For completeness, the integral with one argument outside the cell is bounded by a constant times the integral of the distances to its two endpoints to power -2r. This is finite precisely for r<1/2 and scales as `|I_k|^(1-2r)`. The within-cell integral is bounded using the derivative of `e^{-x/2}` and is smaller. For points in different cells, `|G(x)-G(y)|²<=2 sum_k |g_k(x)-g_k(y)|²`; hence summing these bounds controls the full seminorm. The L² term obeys the same weighted-sum bound.

Split the sum at `K=ceil(B²/E)` for E>0. Since E<=B², K>=1. For k<=K use `k^(-2)<=2/[k(k+1)]`; for k>K use |f(k)|<=B and the convergent power tail. This gives a constant times `B^(4r)E^(1-2r)`. The case E=0 is immediate. ∎

For `1<alpha<3/2`, (4) and (25) give, with beta=3/2-alpha,

\[
 \|T_\alpha Jf\|_2^2\le C_\alpha B^{4\beta}E^{1-2\beta}.
\tag{26}
\]

For `3/2<alpha<2`, put r=alpha-3/2 and delta=`||T_alpha Jf||²`. Interpolating between H^(-r) and H^s, using any fixed `0<s<1/2`, and applying (25), gives

\[
 E\le C_\alpha B^{4r/(1+2r)}\delta^{1/(1+2r)}.
\tag{27}
\]

To see the exponent, the squared interpolation inequality is
`E<=||Jf||_(H^-r)^(2s/(r+s))*||Jf||_(H^s)^(2r/(r+s))`.
Substituting (4) and (25) leaves a power of E on the right; moving it to the left gives (27). This is a direct finite-residual estimate. The qualitative zero-functional argument in Theorem 3 is stronger for the RH implication because it needs no bound on B across the sequence.

For a finite native residual, the explicit safe budget is
`B=1+sum_(n=2)^N |c_n|`. A smaller actual supremum can be substituted if established.

## 5. A complete-source frequency-tail estimate

**Theorem 4.** For every bounded native f, `|f(k)|<=B`, and every Y>=2,

\[
 \int_Y^\infty |(\mathcal C Ef)(y)|^2dy
 \le \frac{16B^2}{\sqrt Y}.
\tag{28}
\]

In particular, for the residual with coefficients c_n and budget B,

\[
 \left\|1-\sum c_nb_n\right\|_H^2
 \le \frac2\pi\int_0^Y
  \left|\sin y-\sum c_nV_n(y)\right|^2\frac{dy}{y^2}
  +\frac{16B^2}{\sqrt Y}.
\tag{29}
\]

This is an unconditional complete-source upper bound. The finite integral still has to be bounded for useful coefficients; its existence does not prove an improving sequence.

**Proof.** Extend Ef evenly to `F(u)=Ef(|u|)` on the real line, with zero outside [-1,1]. For `0<h<=1`, take `K=ceil(h^(-1/2))`. Outside a central interval of length at most `2/K+h`, a translation by h changes a step value only when it crosses one of the at most 2K boundaries ±1/k. The total exceptional measure is at most

\[
 2Kh+2/K+h\le8\sqrt h.
\]

The pointwise difference has absolute value at most 2B, so

\[
 \|F(\cdot+h)-F\|_2^2\le32B^2\sqrt h.
\tag{30}
\]

For the unitary Fourier transform, `hat F(y)=C Ef(y)` on positive y. Averaging the translation multiplier over `0<h<2/Y` gives

\[
 \frac Y2\int_0^{2/Y}|e^{iyh}-1|^2dh
 =2\left(1-\frac{\sin(2y/Y)}{2y/Y}\right)\ge1
 \quad(|y|\ge Y).
\]

By Plancherel, (30), and symmetry,

\[
 2\int_Y^\infty|\mathcal C Ef(y)|^2dy
 \le\frac Y2\int_0^{2/Y}32B^2\sqrt h\,dh
 =\frac{64\sqrt2}{3}\frac{B^2}{\sqrt Y}.
\]

Since `32 sqrt(2)/3<16`, this proves (28), hence (29). ∎

For real y the entire source S also has the elementary tail bound

\[
 \left|S(y)-\sum_{k=1}^K(\sin(y/k)-y/k)\right|
 \le\frac{|y|^3}{12K^2}.
\tag{31}
\]

It follows from `|sin v-v|<=|v|³/6` and `sum_(k>K) k^-3<=1/(2K²)`. Thus finite computations of the complete generators have a simple certified remainder, with the separate logarithmic compensator retained. This remainder bound and the frequency-tail bound are different obligations.

## 6. Exact Möbius synthesis, and the unresolved coupling of ranges

Let mu be the Möbius function. Absolute convergence of the cubic tails gives the entire identity

\[
 \sum_{n\ge1}\mu(n)S(y/n)=\sin y-y.
\tag{32}
\]

Indeed the double series may be regrouped by the product nk, after which `sum_(n|m)mu(n)=1_(m=1)`. For real y, truncation at n=N costs at most `zeta(3)|y|³/(12N²)`.

Put

\[
 A_N=\sum_{n\le N}\frac{\mu(n)}n,\qquad
 B_N^{\log}=\sum_{n\le N}\frac{\mu(n)\log n}{n}.
\]

For the natural coefficients `c_n=-mu(n)`, equations (12) and (32) give the exact finite residual

\[
 \sin y+\sum_{n=2}^N\mu(n)V_n(y)
 =y(1+B_N^{\log})+A_NS(y)
   +\sum_{n>N}\mu(n)S(y/n).
\tag{33}
\]

The classical quantitative prime number theorem implies `A_N->0` and `B_N^log->-1`; therefore these residuals tend to zero on every fixed compact y interval. To justify both endpoint limits, use the standard unconditional bound `sum_(n<=x)mu(n)=O(x exp(-c sqrt(log x)))`: partial summation gives convergence of both endpoint series, and their Abel limits are respectively `lim_(epsilon->0)1/zeta(1+epsilon)=0` and `lim_(epsilon->0)zeta'(1+epsilon)/zeta(1+epsilon)^2=-1`. A primary reference for the imported Mertens estimate is given in SOURCES.md. Formula (33) makes every endpoint term visible. It does not give small error on a window growing fast enough for (29).

The obstruction is visible *before* transforming. For `1<=k<=N`, the exact divisor identity yields

\[
 1+\sum_{n=2}^N\mu(n)b_n(k)=kA_N.
\tag{34}
\]

Consequently these particular approximants have the unconditional lower bound

\[
 \left\|1+\sum_{n=2}^N\mu(n)b_n\right\|_H^2
 \ge |A_N|^2\bigl(N+1-H_{N+1}\bigr).
\tag{35}
\]

PNT's endpoint limits alone do not force this expression to zero. The safe budget in (29) is at most N, so using that general tail bound to force convergence asks for `Y/N^4->infinity`, while the compact remainder estimate (33) contains an increasing term of order `Y³/N²` and the slow endpoint errors. The separate compact and tail statements do not close this coupled range.

This is not just a poor choice of sign when exact prefix interpolation is imposed. If a finite native combination has residual zero for every `1<=k<=K`, difference equations and Möbius inversion force

\[
 c_n=-\mu(n),\qquad2\le n\le K,
 \quad\sum_n c_n/n=1.
\tag{36}
\]

Thus its l1 coefficient budget is already at least `sum_(2<=n<=K)|mu(n)|`, which grows linearly with K. The elementary squarefree identity `mu(n)^2=sum_(d²|n)mu(d)` gives `sum_(n<=K)|mu(n)|=(6/pi²)K+O(sqrt(K))` by summing over d first. Extra coefficients above K may adjust the last scalar condition, but cannot change the forced initial coefficients. A sharp source-dependent tail estimate must use cancellation beyond the safe supremum budget, or avoid exact prefix interpolation.

## 7. What has actually advanced

The exponential noise inversion is bypassed by an explicit deterministic transform. At alpha=3/2 the transformation is lossless and carries every actual generator, the target, the dilation action, and every zero-functional exactly. Away from that parameter, the whole off-critical arithmetic range costs less than half a Sobolev derivative; the transformed zero evaluations remain continuous. The native complete norm has an explicit finite-frequency remainder bound.

The outstanding mathematical task is now concrete: construct coefficients for which the full sine-synthesis error in (14), or the polynomially transferred native norm in (23), tends to zero, with coherent tail control. Equations (33)–(36) show why the naive Möbius compact limit does not establish that. No such all-range upper bound is proved here, and no zero-free endpoint follows from the factorization or the finite checks alone.
