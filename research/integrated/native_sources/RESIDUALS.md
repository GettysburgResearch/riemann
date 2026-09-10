# Native arithmetic residuals, annular signs and complete lifts

[Guide](README.md) · [Proof library](SOURCE_INDEX.md) · [Evidence](EVIDENCE.md)

**Status:** reviewed component selections in an integration candidate. The full arithmetic upper estimates below remain open. Finite optimization, a paid infinite tail, or a growth formula containing the unknown zero edge does not evaluate that edge.

## 1. The original physical residual and its exact constraints

For an integer $Y\ge2$, let $\mathcal C_Y$ be the class of finite real Dirichlet polynomials

$$p(s)=\sum_n a_n n^{-s},\qquad a_n=\mu(n)\ (n<Y),\qquad p(1)=0,\quad p'(1)=1.$$

Every finite tail index is allowed, including nonsquarefree indices. The complete physical residual is

$$E(p)=\int_1^\infty\left|1-\sum_n a_n\lfloor x/n\rfloor\right|^2\frac{dx}{x^2}.$$

The exact prefix makes the residual zero for $1\le x<Y$. Balance removes the linear growth at infinity; the full future is retained. Every such finite polynomial has positive error, but this does not establish a positive infimum over all finite supports.

For each hypothetical zero $\rho$ with $\beta=\Re\rho>1/2$, the reviewed source/Hardy argument gives, simultaneously for every $p\in\mathcal C_Y$,

$$E(p)\ge\frac{2\beta-1}{|1-\rho|^2}\,Y^{2\beta-1}.$$

**Proof route.** Use the exact floor Mellin identity and the zero initial horizon to shift the residual into a half-plane Hardy space. The derivative normalization gives an additional vanishing value at the safe point. Project the evaluation kernel against that constraint before applying Cauchy–Schwarz. The full source, normalization and future determine the lower bound. A native subpower upper bound on an unbounded sequence would contradict every fixed off-line zero, but that upper bound is not supplied.

[Positive residual and source interpretation](../../../standalone/2026-09-06-logarithmic-core/positive-residual-review/PROOF.md) · [normalization, finite coercivity and minima](../../../standalone/2026-09-08-residual-normalization-and-minima/PROOF.md).

### A complete growth classification, not an evaluated exponent

Let $\Theta$ be the supremum of real parts of nontrivial zeta zeros. Allow a nonattained supremum and $\Theta=1$. Define

$$e_2(Y)=\min_{\substack{p\in\mathcal C_Y\\\operatorname{supp}p\subseteq[1,2Y]}}E(p),\qquad
 e_\infty(Y)=\inf_{p\in\mathcal C_Y}E(p).$$

The second infimum ranges over all finite supports and need not be attained. Set

$$M_Y=\sum_{n<Y}\frac{\mu(n)}n,\quad F_Y=\sum_{n<Y}\frac{\mu(n)}n\log(Y/n),\quad
b_Y=\frac{F_Y-1}{\log2},\quad a_Y=-M_Y-b_Y,$$

$$p_Y^\sharp(s)=\sum_{n<Y}\mu(n)n^{-s}+Ya_YY^{-s}+2Yb_Y(2Y)^{-s}.$$

This explicit polynomial is admissible without solving an optimization. At the reviewed scope, the three limits exist and equal

$$\lim_{Y\to\infty}\frac{\log(1+e_\infty(Y))}{\log Y}
=\lim_{Y\to\infty}\frac{\log(1+e_2(Y))}{\log Y}
=\lim_{Y\to\infty}\frac{\log(1+E(p_Y^\sharp))}{\log Y}=2\Theta-1.$$

**Proof route.** Combine the source-qualified zero lower bounds with the classical reciprocal-zeta/Mertens estimates strictly to the right of the unknown edge and the explicit two-endpoint completion. The endpoint $\Theta=1$ is handled by unconditional elementary bounds, not by invoking a nonexistent intervening zero-free half-plane. Constants are not uniform as the distance from the edge vanishes. The identity is an unconditional classification **in terms of an unknown**, not a proof that the exponent is zero.

[Complete all-scale theorem and endpoint cases](../../../standalone/2026-09-08-residual-spectral-exponent/PROOF.md).

## 2. Uniform finite arithmetic capture pays the tail before minimization

For $N\ge2$, $b\in\mathbb C$, and $a\in\mathbb C^N$ satisfying $\sum a_n/n=0$, put $u(x)=b-\sum a_n\lfloor x/n\rfloor$. Let $h_N=\lceil\log_2N\rceil$, $C_N=N^2(1+2h_N)$, and

$$V(b,a)=\left|b+\frac12\sum_n a_n\right|^2+
\frac1{12}\sum_{d\le N}J_2(d)\left|\sum_{\substack{d\mid n\\n\le N}}\frac{a_n}{n}\right|^2,$$

where $J_2(d)=d^2\prod_{p\mid d}(1-p^{-2})$. For an integer $H\ge1$, define

$$Q_H(b,a)=\sum_{j=1}^{H-1}\frac{|u(j)|^2}{j(j+1)},\qquad
\widehat E_H(b,a)=Q_H(b,a)+\frac{V(b,a)}H.$$

The selected complete-tail theorem is the uniform quadratic-form bound

$$|E(b,a)-\widehat E_H(b,a)|\le\frac{C_NV(b,a)}{H(H+1)}.$$

**Proof route.** The exact finite-period covariance is $(\gcd(m,n)^2-1)/(12mn)$. Balance removes its rank-one subtraction, and Jordan divisor inversion gives $V$. Combine equal rational Fourier frequencies before using their spacing to bound every finite interval discrepancy by $C_NV$. Abel summation of the entire infinite future gives the displayed bound. The common period is used for the proof, not enumerated in the algorithm.

The stronger comparison $V\le4C_NE$ gives

$$|\widehat E_H-E|\le\eta_HE,\qquad \eta_H=\frac{4C_N^2}{H(H+1)}.$$

Taking $H=2C_N\lceil\sqrt N\rceil$ gives $\eta_H<1/N$. These estimates hold before optimization, uniformly over all coefficients. Any fixed nonempty compatible affine class can therefore be optimized with certified relative error. The derivative constraint still contains exact logarithms; only a rational balance/prefix class makes the whole finite solve rational. This controls approximation of a minimum, not its size.

[Full theorem, mean-square identity and comparison forms](../../../standalone/2026-09-08-rational-residual-capture/PROOF.md).

<a id="minimum-repair"></a>
### Current numerical statement: two feasible classes and repair R01

The balance-only examples retain the native prefix and $p(1)=0$, but do **not** impose $p'(1)=1$. At $H=4096$ their full minimum enclosures are

| $Y$ | $N$ | Full balance-only minimum |
|---:|---:|---|
| 2 | 8 | $[0.025607338825,0.025616531671]$ |
| 3 | 12 | $[0.021620272026,0.021647203122]$ |
| 4 | 16 | $[0.019070164807,0.019120804411]$ |

**R01:** these tight brackets use separately minimized lower and upper comparison forms in equation **(18)** of the original manuscript, not equation (8) alone. The reviewed independent reconstruction supports the stated brackets through that proof route; the original attribution remains preserved as history.

The four derivative-normalized examples instead impose both jets, with $(Y,N)=(2,4),(4,8),(8,16),(16,32)$. Their complete Gram and stationarity-residual certificates are in the [reviewed finite-minimum reconstruction](../../../reviews/2026-09-08-postintegration/pass3/REPORT.md). They are not the three balance-only problems above. In both panels the prefix changes with $Y$; decreasing displayed values do not prove convergence in one fixed nested class. The original accepting packages are not all approved by the independent numerical reconstructions.

## 3. A genuine native improvement and a sharp obstruction to a uniform adapter

The explicit three-block completion $p_Y^c$ preserves the actual prefix and satisfies $p_Y^c(1)=0$, $(p_Y^c)'(1)=1$, and $p_Y^c(0)=-2$. Its support is below $8Y$ and its coefficients are bounded independently of $Y$. Classical unconditional Mertens cancellation and critical-line convexity give the complete physical bound

$$E(p_Y^c)\ll Y\exp\{-c(\log Y)^{3/5}(\log\log Y)^{-1/5}\}=o(Y).$$

**Proof route.** Retain the complete moment tails and the $(1+|t|)$ factor from twisted partial summation. Use the minimum of the absolute coefficient bound and the cancellation bound, then split the entire critical-line integral at the inverse small parameter. All frequencies are included. This is an application of classical cancellation, not a new Mertens theorem, fixed-power saving or subpower estimate. No numerical constant or starting height is certified.

For balanced tail variations supported in $[Y,N]$ with $N\le AY$ and fixed $A$, distinguish the physical response $R(q)$, coefficient energy $S(q)=\sum|c_n|^2/n$, and **complete** divisor energy

$$G_N(q)=\sum_{p^kj\le N}\frac{\log p}{p^kj}|c_{p^kj}-c_j|^2.$$

Vertices below $Y$ remain present with coefficient zero. The selected comparison gives $R(q)\le A^2YS(q)$ and $G_N(q)=(\log Y)S(q)+O_A(S(q))$. An explicit variation

$$q_Y(s)=Q_Y(s)(1-2^{1-s})^2(1-2^{-s}),\qquad
Q_Y(s)=Y^{-1}\sum_{Y\le n<2Y}n^{1-s}$$

has $q_Y(1)=q_Y'(1)=q_Y(0)=0$, bounded coefficients and support below $16Y$, yet $R(q_Y)\ge Y/24$. Therefore the sharp **order** of the coefficient-uniform comparison loss is $Y/\log Y$, not polylogarithmic. Analogous obstructions survive any fixed number of the stated jets; no growing-jet theorem is claimed.

Adding or subtracting this variation preserves the actual prefix and all three normalizations. The parallelogram identity forces one of the two perturbed physical energies to be large. This rejects a uniform shortcut, **not** a better estimate for a selected native completion or its optimum.

The complete variation-profile certificate, with 4,095 rational cells and the infinite tail retained, gives $1.704219450036<C_*<1.704219498544$. This is a profile constant, not an actual-zeta norm, an optimized minimum, or the optimal leading constant of the comparison supremum.

[Complete native bound, sharp transfer loss and profile proof](../../../standalone/2026-09-08-arithmetic-norm-transfer/PROOF.md) · [source-preserving synthesis](../../../standalone/2026-09-08-arithmetic-norm-transfer/SYNTHESIS.md).

## 4. Fixed annular signs and the stronger sparse-failure target

For each integer $m\ge2$, define nonnegative rational weights

$$a_m(n)=\begin{cases}
64n-m^6/n^2,&m^2/4<n\le m^2,\\
64m^6/n^2-n,&m^2<n\le4m^2,\\
0,&\text{otherwise},
\end{cases}\qquad
D_m=\frac{\sum_n a_m(n)\Lambda(n)}{192m^3}-\frac{45m}{128}+\frac14.$$

The fixed-source criterion equates eventual $D_m\ge0$ with RH; under RH the chosen offset gives a uniform strictly positive safety margin. The implication is reviewed, but the arithmetic inequality is not proved by its formulation. Every prime power in the annulus must remain.

**Proof route.** Apply the fixed autocorrelation filter whose zeros lie outside the sensitive strip. It annihilates the complete safe tail and deterministic exponentials without canceling a hypothetical off-line pole. The resulting finite annular scalar has a fixed noncancelling transform. Source growth and interpolation allow the Landau argument to consume the prescribed sampled sign. The [height-transfer theorem](../../../standalone/2026-09-06-logarithmic-core/height-transfer-and-prime-squares/PROOF.md) combines imported zero verification through height $3\cdot10^{12}$ with a complete analytic tail bound to cover the stated continuous range through $X=10^{22}$. This is not a fresh zero census or a direct prime scan to that endpoint.

The later sparse-sign theorem requires only **any fixed power saving** in the specified negative-failure count on its prescribed grids. That saving remains open. Nonattainment of the rightmost zero edge is treated; positive-density conclusions need their separate attained-edge hypotheses. The fixed-moment obstruction limits a proposed method, not the criterion itself. [Annular criterion](../../../standalone/2026-09-06-logarithmic-core/annular-scalar-route/PROOF.md) · [curvature and interpolation](../../../standalone/2026-09-06-logarithmic-core/prime-curvature-and-failure-count/PROOF.md) · [sparse-sign bootstrap](../../../standalone/2026-09-06-logarithmic-core/sparse-sign-bootstrap/PROOF.md) · [failed fixed-moment attack](../../../standalone/2026-09-06-logarithmic-core/fixed-moment-counting-attempt/PROOF_ATTEMPT.md).

The signed contour functional in the completion-rigidity paper is a different object from $E(p)$. Its rank-one Hessian leaves the unknown intercept unchanged after both jets are fixed. Optimizing the remaining coefficients cannot improve that intercept; a positive Hessian is not a sign theorem for the minimum. [Contour identity](../../../standalone/2026-09-06-logarithmic-core/balanced-mobius-contour/PROOF.md) · [rigidity and precise obstruction](../../../standalone/2026-09-06-logarithmic-core/completion-rigidity-review/PROOF.md).

## 5. The detail problem is solved; its direct lift need not improve the full error

In $H=\ell^2(\mathbb N_{\ge1},[n(n+1)]^{-1})$, put $h_k(n)=\{n/k\}$, $\chi(n)=1$ and $B_N=\operatorname{span}(h_2,\ldots,h_N)$. The squared full distance is $\delta_N=\operatorname{dist}(\chi,B_N)^2$. The even-dilation/odd-birth decomposition retains all original coefficients. Its exact coupled block recursion includes a coarse projection term; dropping that term changes the optimization.

The odd-detail problem has explicit Jordan/divisor weights and an all-scale positive tail estimate. Nevertheless, at the actual stage $8\to16$, lifting its exact optimizer followed by the best allowed old-coarse correction gives

$$0.025491663369<U_8<0.025491663370,\qquad
0.024244525306<\delta_8<0.024244525307,$$

whereas $\delta_{16}<0.017936267021$. Thus this detail-driven lift can be worse than the old full optimum even though the full coupled optimization improves it. The full optimizer has a nonzero coefficient at index 9; deleting nonsquarefree coordinates is valid for the relaxed formula, not for every finite optimum. A separate squarefree target-closure statement is conditional on RH and is not a claim of ambient density.

[Dilation and source-space proof](../../../standalone/2026-09-06-astra-dilation-observability/PROOF.md) · [complete block recursion and finite obstruction](../../../standalone/2026-09-06-astra-block-gain/PROOF.md) · [full-to-full growth transfer and nonconvergence](../../../standalone/2026-09-06-astra-growth-transfer/PROOF.md). The raw explicit lifts fail to converge strongly even under the intended RH scenario; their subpower-growth criterion is different from strong convergence. The original uniform full-source block gain remains open.

## 6. Balanced rational sources, complete Green energy and repairs R02–R03

For odd $k\le M$, the balanced source fixes $\lambda_{1,M}=1$ and $\sum_k\lambda_{k,M}/k=0$. Its coefficients are explicitly rational. With sums over odd $d\le M$, put

$$S_M=\sum\mu(d)^2/J_2(d),\quad A_M=\sum\mu(d)\varphi(d)/J_2(d),\quad
D_M=\sum\varphi(d)^2/J_2(d),\quad K_M=S_MD_M-A_M^2>0,$$

$$v_k=k^2\sum_{k\mid d}\frac{\mu(d/k)\mu(d)}{J_2(d)},\quad
w_k=k^2\sum_{k\mid d}\frac{\mu(d/k)\varphi(d)}{J_2(d)},\quad
\lambda_{k,M}=(D_Mv_k-A_Mw_k)/K_M.$$

For $M\ge3$ this is the unique constrained **detail** optimizer, not the full-space optimizer. Its actual full lift is $F_M=\sum_k\lambda_{k,M}(h_{2k}-h_k)$. Exact balance cancels the linear slope and supplies the native primitive. The later bounds $|\lambda_{k,M}-\mu(k)|<72k/M$ and detail error $<18/M$ hold for $M\ge128$, without a Mertens cancellation estimate.

The full energy has a finite Green representation. For reduced fractions $x=r/q\in(0,1/2)$ with odd $3\le q\le M$, set

$$L_q=\sum_{q\mid k}\lambda_k/k,\quad t_x=\tan(\pi x),\quad
\sigma_x=(-1)^{r+1}L_q\cot(\pi x),\quad C(t)=\sum_{t_x\ge t}\sigma_x.$$

Then, for **any** finite balanced odd source,

$$E[\lambda]=\|F[\lambda]\|_H^2=\frac\pi2\int_0^\infty C(t)^2dt.$$

This is a finite interval-square sum with all original cross terms, not a truncated numerical Gram. Its ordered Green matrix has an explicit tridiagonal inverse. For the specified rational optimizer, the full contribution above $1/\log(2M)$ is $O(\log^3M)$; the shrinking endpoint energy is still open at the required scale.

<a id="balanced-lift-repair"></a>
**R02, squared-norm qualification.** The nearly optimal-detail counterfamily gives full **energy** of order at least $\sqrt M$ along its specified sequence. The unsquared norm lower growth is order $M^{1/4}$. It is not a lower bound against the exact native optimizer. The displayed parallelogram construction, not the original ambiguous prose, controls this statement.

For $h(u)=\log2-\sum_{1\le r<u}(-1)^{r+1}/r$, define $W_\lambda(x)=\sum_k\lambda_kh(kx)$, $\mathcal H[\lambda]=\int_0^{1/4}W_\lambda(x)^2dx$ and $B[\lambda]=\sum_k|\lambda_k|/k$. The complete harmonic transfer is

$$\sqrt{E[\lambda]}\le\sqrt{\mathcal H[\lambda]}+4B[\lambda],\qquad
\sqrt{\mathcal H[\lambda]}\le\sqrt{2E[\lambda]}+2B[\lambda].$$

**R03, interval qualification.** When $M\ge5$ is merely an upper support bound, the current is constant on the **prescribed interval $(0,1/M)$** and its contribution is $(\log2)^2(\sum_k\lambda_k)^2/M$. The entire first active mesh interval can be longer. This fixes the interval wording without changing the norm comparison.

[Balanced construction and obstruction](../../../standalone/2026-09-06-astra-balanced-lift/PROOF.md) · [complete Green form and sharper bounds](../../../standalone/2026-09-06-astra-green-energy/PROOF.md) · [harmonic replacement](../../../standalone/2026-09-06-astra-terminal-endpoint/PROOF.md). Positivity of a Green form is not the missing upper bound on this particular arithmetic vector.

## 7. A different terminal family gives a prescribed sparse-grid criterion

For odd $M\ge3$ define $m_o(x)=\sum_{n\le x,\ n\text{ odd}}\mu(n)/n$, $M_o(x)=\sum_{n\le x,\ n\text{ odd}}\mu(n)$ and $Q(x)=M_o(x)-xm_o(x)$. The **new** terminal coefficients are

$$\lambda^{\rm term}_{k,M}=\mu(k)-Mm_o(M)\mathbf1_{k=M},\qquad k\le M\text{ odd}.$$

They are exactly balanced and give $F_M(n)=1$ for $1\le n<M$. The terminal correction is retained even when $M$ is nonsquarefree. This family differs from the constrained detail optimizer above.

The scalar transform is

$$\int_1^\infty Q(x)x^{-s-1}dx=-\frac1{s(s-1)(1-2^{-s})\zeta(s)}\qquad(\Re s>1).$$

Its numerator does not cancel any nontrivial zeta zero. Exact piecewise-linear interpolation shows that the prescribed grid $M_j=2j^4+1$ suffices: $Q(M_j)^2/M_j=M_j^{o(1)}$ on every grid point is RH-equivalent, with the reverse direction importing the classical RH-to-Mertens implication. The required upper bound is not proved. Small values on an arbitrary subsequence are not this sampling theorem. [Complete terminal-source theorem](../../../standalone/2026-09-06-astra-terminal-endpoint/PROOF.md).

The balanced hyperbola hierarchy shortens the arithmetic input and cancels every pole main term before estimating. Its exact quadratic identity is $\mathcal B_Y=Q(Y^2)-2Q(Y)$. The compact continuum remainder has norm at most $1/8$, but the corresponding unweighted sampled matrix has growing norm. Explicit balanced sources have either quadratic sign with order $Y^2$ size. That is not a near-linear estimate for the actual Möbius orientation.

The later critical-line formula retains $P_Y(s)^2$, **not** $|P_Y(s)|^2$, and its complete high-frequency tail is $O(Y)$ at the prescribed cutoff. The remaining signed integral is still open at the necessary scale. Either fixed one-sided near-linear bound on the stated grid would suffice; selecting the favorable sign separately at each point would not. [Balanced hyperbola proof](../../../standalone/2026-09-07-astra-balanced-hyperbola/PROOF.md) · [critical-line formula and one-sided alternative](../../../standalone/2026-09-07-astra-critical-line-attempt/PROOF.md).

**Useful next contribution:** a bound for one literal native residual, coherent correlation or prescribed-grid work term, with all constraints and the full norm retained. A faster finite solver or positive detail identity is useful infrastructure, but does not supply that arithmetic estimate.
