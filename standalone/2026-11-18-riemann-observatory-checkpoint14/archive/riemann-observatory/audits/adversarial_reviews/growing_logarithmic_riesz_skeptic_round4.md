# Independent review: growing logarithmic Riesz order under RH

2026-11-17. Reviewer: `/root/li_skeptic`. Classification: **independently checked with no issue found in the inspected argument**, conditional on RH and the explicitly identified classical inputs. No claim of priority, a new arithmetic bound, or a proof of RH is made.

The Perron representation, saddle kernel, central ratio argument and possible global-height obstruction were reconstructed before reading `proposals/independent_campaigns/growing_logarithmic_riesz_round3.md`. That complete proposal and its finite-height dependency were then read. The source images of Titchmarsh's printed pp217 and354–355 were independently inspected, including the short proof of Theorem9.6(A). This is partial source reading, not a whole-monograph audit.

## Statement checked

Assume RH. For one sufficiently large fixed constant `c`, let

\[
 L=\log N,\quad \epsilon=c/\log\log N,
 \quad \alpha=\epsilon L,
\]

\[
 V_N(s)=\sum_{n\le N}\mu(n)
       \left(1-\frac{\log n}{\log N}\right)^{\alpha}n^{-s}.
\]

Then, as integers `N` tend to infinity,

\[
 \frac1{2\pi}\int_{\mathbb R}
 \frac{|1-\zeta(\tfrac12+it)V_N(\tfrac12+it)|^2}
 {|\tfrac12+it|^{2q}}\,dt\longrightarrow0
 \qquad(q\ge1\text{ fixed}).
\]

The proof is asymptotic. Its constants are symbolic and may give enormous unspecified thresholds. It does not claim a usable numerical value of `c` or a uniform conclusion for growing `q`. The summand at `n=N` is zero. Powers are real powers of nonnegative weights. This is a moving logarithmic-order array, so a fixed-order multiplicity obstruction cannot simply be applied to it.

**Subsequent strengthening, independently challenged:** the same conclusion holds for **each fixed `c>0`**, not only sufficiently large `c`. The proof below first checks the submitted large-`c` version. The final addendum removes the artificial `N^4` auxiliary-height choice and gives the complete all-positive-`c` argument. This does not assert uniformity as `c` varies with `N`.

## 1. The global reciprocal bound is sufficient and is uniform

The chief issue in the independent reconstruction was the inverse zeta factor at arbitrary heights `t+v`. A bound of the form `(|t+v|+3)^(C/epsilon)` would be insufficient for the weighted integral. The actual proof uses the stronger, independently reconstructed finite-height lemma in `audits/baez_uniform_dependency_round2.md`:

\[
 \sup_{|u|\le H,\,1/2+1/\log\log H\le\sigma\le2}
 |1/\zeta(\sigma+iu)|
 \le\exp\{K\log H/\log\log H\}.
 \tag{R1}
\]

Here `K,H_0` are fixed under RH. The lemma's proof was independently checked. Its high-height portion uses the actual regions in Titchmarsh14.14.2–5, rather than quoting the equality-line formula14.14.4 as a half-plane statement. For low heights put `U=exp(sqrt(log H))`. The nonvanishing analytic function `(s-1)zeta(s)` has a holomorphic logarithm in `Re(s)>1/2` under RH. Borel–Carathéodory on concentric disks about `2+iu`, of radii `3/2-delta/2` and `3/2-delta`, where `delta=1/loglog H`, gives

\[
 |\log((s-1)\zeta(s))|
 \ll\delta^{-1}\log(|u|+3).
\]

The center value is bounded by the principal `Log(1+iu)` plus the absolutely convergent Euler logarithm at real part2. The bound on the real part follows from polynomial growth on a fixed strip. For `|u|<U` this is `O(loglog H sqrt(log H))=o(log H/loglog H)`. The apparent pole at1 is removed before taking the logarithm; the reciprocal zeta function itself vanishes there, which is harmless. For `U<=|u|<=H`, one has `delta>=1/(2 loglog|u|)`, giving the needed near-line source-region comparison. These details eliminate a hidden fixed-height or fixed-epsilon constant.

For any real `u`, set `H=|u|+N^4+3`. When `c>=1` and `N` is large, `epsilon>=1/loglog H`. The elementary monotonicity/doubling bound for `phi(x)=log x/loglog x` gives

\[
 \phi(H)\le8\frac{L}{\log\log N}+2\ell(u),
 \qquad \ell(u)=\frac{\log(|u|+3)}{\log\log(|u|+3)}.
\]

Consequently fixed constants `A=8K,b=2K` give

\[
 |1/\zeta(\tfrac12+\epsilon+iu)|
 \le \exp\{(A/c)\alpha+b\ell(u)\}.
 \tag{R2}
\]

The same estimate holds throughout the contour strip `epsilon<=Re(w)<=1/2+1/L`, since the corresponding real part of zeta lies between `1/2+epsilon` and `1+1/L<2`. In particular it applies at every height, not merely at `|u|<=N^4`. For fixed `N`, the right side is subpower in `|u|`. This independently resolves the possible infinite-tail obstruction.

## 2. Perron formula, legal contour, exact kernel

On `Re(w)=1/2+1/L`, the Möbius Dirichlet series is absolutely convergent for `Re(s)=1/2`. The ordinary inverse-Laplace formula for `w^(-alpha-1)` therefore gives

\[
 V_N(s)=\frac{\Gamma(\alpha+1)}{2\pi i L^\alpha}
 \int e^{Lw}w^{-\alpha-1}\zeta(s+w)^{-1}\,dw.
\]

This formula also follows directly by integrating each absolutely convergent Dirichlet term: the inverse transform is `log(N/n)^alpha/Gamma(alpha+1)` for `n<N` and zero for `n>=N`. The complex power uses the holomorphic principal logarithm on `Re(w)>0`.

Under RH no zero of zeta is crossed in moving this contour to `Re(w)=epsilon`; its pole at1 becomes a zero of the integrand's reciprocal factor. No branch cut or `w=0` is crossed. For fixed `N` the bound(R2) is subpower at the top and bottom of the rectangle. With `alpha>=4`, horizontal integrals tend to zero and both vertical integrals are absolutely convergent. Neither an unproved growth bound on the critical line nor a contour passing through zero ordinates is used.

After writing `w=epsilon+iv`, the exact formula is

\[
 V_N(s)=\int_{\mathbb R}K(v)\zeta(s+\epsilon+iv)^{-1}\,dv,
\quad
 K(v)=\frac{\Gamma(\alpha+1)e^{\alpha+iLv}}
 {2\pi L^\alpha(\epsilon+iv)^{\alpha+1}}.
 \tag{R3}
\]

Since `alpha=epsilon L`, scalar inverse Laplace gives `integral K=1`. Its absolute density after `v=epsilon y` is exactly

\[
 |K(v)|\,dv=B_\alpha(1+y^2)^{-(\alpha+1)/2}\,dy,
\quad B_\alpha=\frac{\Gamma(\alpha+1)e^\alpha}{2\pi\alpha^\alpha}.
\]

Stirling and `log(1+y^2)>=y^2/2` on `|y|<=1`, with the elementary power tail on `|y|>1`, give `integral|K|<=3` for `alpha>=2`. For fixed `0<eta<=1`, `0<delta<=1/8`, and `epsilon<=1`, reserving `alpha/4` of the exponent gives

\[
 \int_{|v|>\eta\epsilon}|K(v)|(3+|v|)^\delta\,dv
 \le C_\delta\sqrt\alpha e^{-\kappa_\eta\alpha},
\quad \kappa_\eta=\tfrac14\log(1+\eta^2)>0.
 \tag{R4}
\]

The remaining power is at least one when `alpha>=4`, so its whole-line integral is at most pi. This proves a bound on the entire noncompact tail; no Gaussian approximation or finite vertical cutoff is being substituted for it.

## 3. Central part: a uniform weighted majorant

Under RH the even paired xi product converges normally because `sum gamma^(-2)<infinity`:

\[
 \xi(\tfrac12+w)=\xi(\tfrac12)
 \prod_{\gamma>0}(1+w^2/\gamma^2),
\]

with multiplicities. Evenness removes any possible nonconstant exponential factor in the order-one product. Also `xi(1/2)!=0`, for example from the positive alternating eta-series and `zeta(1/2)<0`. For each factor the modulus-square increase from `w=it` to `w=epsilon+it` is

\[
 2\epsilon^2(\gamma^2+t^2)+\epsilon^4\ge0.
\]

Hence the horizontal xi ratio has modulus at most one. Dividing completion factors, uniform gamma-ratio Stirling and a compact-height bound yield

\[
 |\zeta(\tfrac12+it)/\zeta(\tfrac12+\epsilon+it)|
 \le C(|t|+3)^{\epsilon/2}
 \quad(0<\epsilon\le1/8).
 \tag{R5}
\]

The direction of the gamma exponent is important and is correct. The factors `s(s-1)` stay bounded away from zero on the relevant compact horizontal strips, and have bounded ratios at large height.

Titchmarsh Theorem9.6(A), Eq9.6.1, printedp217, explicitly gives

\[
 \zeta'(s)/\zeta(s)
 =\sum_{|t-\gamma|\le1}(s-\rho)^{-1}+O(\log t)
\]

uniformly for `-1<=sigma<=2` at sufficiently large positive height. The proof printed immediately below was read. Riemann–von Mangoldt bounds the local number of zeros, with multiplicity, by `O(log t)`. RH makes their distances from `1/2+epsilon+it` at least `epsilon`, so

\[
 |\zeta'/\zeta(\tfrac12+\epsilon+it)|
 \le D\log(|t|+3)/\epsilon.
 \tag{R6}
\]

Negative height follows by conjugation. On bounded heights a finite-zero partial fraction subtraction leaves a bounded analytic function on a compact neighborhood; the possible zero terms are `O(1/epsilon)`. The pole at1 is outside the strip `1/2<=sigma<=5/8`, so no pole is hidden in this patch.

Integrating(R6) for `|v|<=eta epsilon` and using(R5), with a harmless fixed enlargement `D_1`, gives a ratio bound `C(|t|+3)^(epsilon/2+D_1 eta)`. Fix `eta<=1/(16D_1)` as well as `eta<=1`. For sufficiently large `N`, the exponent is at most1/8. The central contribution is consequently bounded by `C(|t|+3)^(1/8)` independently of `N`.

For every fixed `t` that is not a zero ordinate, the ratio tends uniformly to one on `|v|<=eta epsilon`. The central kernel mass tends to one by(R4), while its absolute mass stays bounded. Thus the central contribution tends pointwise to one almost everywhere. The weighted square is dominated by

\[
 C\frac{1+(|t|+3)^{1/4}}{1/4+t^2},
\]

which is integrable. Dominated convergence gives central convergence in the required `q=1` weighted norm. At a zero ordinate the numerator ratio is zero and the desired pointwise value fails, but those isolated ordinates form a null set; the proof correctly requires only almost-everywhere convergence.

## 4. Noncompact tail: the N-dependent loss is paid

For every fixed `delta>0`, `exp(b ell(u))<=C_delta(|u|+3)^delta`. The RH critical-line bound from Titchmarsh14.14.1 similarly gives `|zeta(1/2+it)|<=C_delta(|t|+3)^delta`. Taking `delta=1/16`, using(R2) and `|t+v|+3<=(|t|+3)(|v|+3)`, one obtains

\[
 \left\|\frac{\zeta(\tfrac12+it)}
 {\zeta(\tfrac12+\epsilon+i(t+v))}\right\|_
 {L^2(dt/(2\pi|1/2+it|^2))}
 \le C\exp\{(A/c)\alpha\}(3+|v|)^\delta.
\]

The height integrand is bounded by a constant times `(3+|t|)^(4delta)/(1/4+t^2)`, so this norm bound is finite uniformly in the kernel variable apart from the stated power. Minkowski and(R4) now give the tail norm bound

\[
 C\sqrt\alpha\exp\{(A/c-\kappa_\eta)\alpha\}.
\]

Choosing the one fixed constant `c>=max(1,2A/kappa_eta)` makes this tend to zero. The integral is an absolutely norm-integrable Bochner integral, so no conditionally convergent interchange or unsupported exchange of two limits occurs. Combining with the central part proves `d_1(V_N)->0`. Finally `|1/2+it|>=1/2` gives `d_q<=2^(q-1)d_1`, which proves every fixed integer `q>=1` using the same `c`.

## Review conclusion and provenance limits

No counterexample or missing hypothesis was found within this RH-conditional statement. The exact fixed constant in the kernel-tail condition, the global reciprocal bound and the noninteger contour power were checked independently. The root has separately reported matching central and global reconstructions. This is suitable for promotion as a fully written conditional approximation proposition after the root's final adjudication.

This review does not establish historical novelty, effective constants, RH itself, an unconditional Möbius estimate, or the original proofs of all classical RH consequences. Source access was the actual local scan of Titchmarsh1986, existing canonical `PAPER-M001`; no duplicate paper record is created. Its exact inspected scope is Theorem9.6(A) and proof onp217, plus Theorems14.14(A),(B) and displayed discussion onpp354–355. The finite-height lemma and its Phragmén–Lindelöf/Borel–Carathéodory bridge were mathematical reconstructions, clearly distinguished from literal quotations of the source.

## Addendum: every fixed positive c works

The root proposed this strengthening after the preceding independent review. The parameter comparisons and every use of the auxiliary height were reconstructed independently before acceptance.

For **any fixed `a>0`**, the same finite-height argument proves constants `K_a,H_a` such that

\[
 \sup_{|u|\le H,\,1/2+a/\log\log H\le\sigma\le2}
 |1/\zeta(\sigma+iu)|\le\exp\{K_a\phi(H)\}.
 \tag{R7}
\]

For clarity, no universal bound on `K_a` as `a` tends to zero is claimed or required. In the high-height range `exp(sqrt(log H))<=|u|<=H`, one has `a/loglog H>=a/(2 loglog|u|)`, so the source consequence is invoked with the fixed parameter `a/2`. Titchmarsh14.14.2 provides the corresponding constant when that parameter is small;14.14.4–5 handle the adjacent regions as in the original finite-height proof. In the low-height range, Borel–Carathéodory now has loss `O((loglog H)/a)`. For fixed `a` its bound is still `o(phi(H))`. Thus(R7) is a genuine fixed-`a` version of the same proved lemma.

Now fix **an arbitrary `c>0`** and set `a=c/2`. Choose an auxiliary exponent `r>0`, fixed throughout the limit, so small that

\[
 \frac{4K_a r}{c}<\frac{\kappa_\eta}{2}.
 \tag{R8}
\]

This is possible since `K_a` and the central-cutoff constant `kappa_eta>0` are fixed. Set `H=|u|+N^r+3`. For sufficiently large `N`,

\[
 \log\log H\ge\log\log(N^r)
 =\log\log N+\log r\ge\tfrac12\log\log N.
\]

Hence `epsilon=c/loglog N>=a/loglog H`, exactly the real-part condition for(R7). The same monotonicity and doubling estimate gives, once `N^r` is sufficiently large,

\[
 \phi(H)\le2\phi(N^r)+2\ell(u)
 \le4r\frac{L}{\log\log N}+2\ell(u).
\]

The last inequality uses `loglog(N^r)>=.5loglog N`; it is valid even when `r<1`, after taking the threshold sufficiently large. Thus throughout the contour strip,

\[
 |1/\zeta(\tfrac12+\epsilon+iu)|
 \le\exp\left\{\frac{4K_a r}{c}\alpha+2K_a\ell(u)\right\}.
 \tag{R9}
\]

There is **no** truncation at height `N^4` in the Riesz proof: the contour is an absolutely convergent infinite vertical integral, and its horizontal sides are sent to infinity for each fixed `N`. The `N^4` appearing in the submitted version was inherited from an earlier truncated ordinary Perron argument and imposes no constraint here. Replacing it by `N^r` changes only the fixed constants in the reciprocal bound; it leaves contour legality unchanged because `exp(2K_a ell(u))` remains subpower as `|u|` tends to infinity.

The central kernel argument needs only `epsilon->0` and `alpha->infinity`, both valid for every fixed positive `c`. Apply the same weighted Minkowski estimate to(R9). The tail is now bounded by

\[
 C_{a,r}\sqrt\alpha
 \exp\left\{\left(\frac{4K_a r}{c}-\kappa_\eta\right)\alpha\right\}
 \longrightarrow0
\]

by(R8). Constants from absorbing `exp(2K_a ell(u))` into an arbitrarily small fixed polynomial power may be large and depend on `c`; they are independent of `N`. The proof therefore establishes the proposed convergence for **every fixed `c>0`**. It supplies no statement for a sequence `c=c_N->0`, no effective threshold, and no uniform-in-`c` rate.
