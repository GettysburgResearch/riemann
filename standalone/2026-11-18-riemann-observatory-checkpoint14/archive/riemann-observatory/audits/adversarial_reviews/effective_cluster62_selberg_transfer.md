# Adaptive approximation for fixed Selberg-class functions

Let $F$ be one fixed Selberg-class Dirichlet series and assume its GRH in the zero-free-half-plane form $F(s)\ne0$ on $\Re s>1/2$, with its pole at 1 allowed. Let $\Delta_{N,F}^2$ be the infimum of $\|1-FA\|_*^2$ over ordinary Dirichlet polynomials of integer length at most $N$, using the same critical-line Cauchy norm as the zeta and fixed-character campaigns. The retained-edge construction gives
$$
 \limsup_{N\to\infty}(\log N)\Delta_{N,F}^2
 \le \sum_{\rho\ {\rm distinct}}\frac{m_\rho^2}{|\rho|^2},
 \tag{1}
$$
with the zeros of the pole-removed completion on the critical line. De Roton’s lower theorem and the Mellin argument below give equality in the limit. The argument covers poles of arbitrary fixed order and each fixed degree. The constants are allowed to depend on the function and its data. [RST048v2](https://rstation.ai/problems/riemann_hypothesis/papers/48/v2) · [Fixed-character transfer](effective_cluster62_dirichlet_transfer.md)

## 1. An explicit sufficient interface for the upper proof

The cluster proof can run without Selberg axioms once the following inputs are available. These are sufficient conditions for the stated estimates, without a necessity assertion.

- An ordinary reciprocal series $G=1/F=\sum b_n n^{-s}$ converges absolutely on some right half-plane and is bounded uniformly far to its right. No pointwise Ramanujan-type bound is required on $b_n$.
- Put $e=10^{-4}$. The function $F$ is holomorphic in a fixed neighborhood of the critical line, and $G$ is meromorphic on the search region to the right of a fixed left edge $1/2-\delta$, with poles only at the zeros of $F$ on the critical line. A pole of $F$ to the right appears as a removable zero of $G$. On the entire left edge and both vertical cell boundaries the reciprocal is $O((2+|t|)^e)$. Between the left edge and each fixed right edge there are good horizontal heights at both signs at arbitrarily small fixed mesh with the same reciprocal bound. The chosen mesh is fixed throughout each limit.
- For a fixed $0<D\le10^{-4}$, $0<\delta\le D/100$, adjacent good heights have spacing in $[2D/3,4D/3]$. On disks of radius $D$ centered on the line and on the critical line itself, the bounds are respectively $O((2+|t|)^{10^{-4}+e})$ and $O((2+|t|)^e)$. The near-cell multiplicity satisfies $k_C\le 10^{-4}\log(2+|\tau_C|)$ eventually. The finite exceptions can have arbitrary multiplicities.

The cutoff choices $H=N^{1/20}$ and $K=N^{3/20}$ then work directly. All parts of the upper proof need only these inputs and the ordinary integer grid. In particular a spectral symmetry between positive and negative ordinates and coefficient bounds on the optimized perturbations are unnecessary.

## 2. Verifying the interface for a Selberg-class function under GRH

Use Selberg’s gamma data $Q>0$, $\lambda_j>0$, $\Re\mu_j\ge0$, degree $d=2\sum_j\lambda_j$, and actual pole order $p\ge0$ at 1. The completion
$$
 \Lambda(s)=Q^s\prod_j\Gamma(\lambda_js+\mu_j)F(s),\qquad
 X(s)=s^p(s-1)^p\Lambda(s)
$$
satisfies the conjugate functional equation about $1/2$, with a constant of modulus one. The completion is meromorphic with poles only at 0 and 1 of order $p$ when $p>0$. Indeed on the right closed half-plane beyond the center the gamma factors are regular, and on the left use the functional equation. The two polynomial factors remove exactly these poles, so $X$ is entire. It has order at most one by the usual gamma growth bound, absolute convergence far right, the functional equation far left, and polynomial bounds in the intervening fixed strips. For the latter bounds first apply the functional equation and Stirling on a fixed left line, absolute convergence on a fixed right line, and the finite-order strip maximum principle to $(s-1)^p F(s)$, dividing out the polynomial at high height. These estimates also justify the order bound $|X(s)|\le \exp(O(R\log(2+R)))$ for $|s|\le R$, using fixed-strip Stirling in the middle. GRH makes every zero of $X$ critical by the same conjugate symmetry. This formulation includes the edges of the critical strip through the stated half-plane assumption.

The reciprocal series converges absolutely on every $\Re s>1$. In the Selberg Euler logarithm, the $p'$-prime coefficient is $a_{p'}$ by exponentiating in a far-right strip and taking the prime coefficient. Ramanujan bounds the prime terms at every such $\sigma>1$. Higher powers converge absolutely since their Euler-log coefficients are $O((p'^k)^\vartheta)$ with $\vartheta<1/2$ and $2(\sigma-\vartheta)>1$. Thus the Euler logarithm converges absolutely on $\Re s>1$. Exponentiating its negative in the algebra of absolutely convergent ordinary Dirichlet series gives the required $b_n$. The letter $p'$ here denotes a varying prime; it plays no role in the pole order $p$.

For control near the critical line let
$$
 H_0(s)=F(s)\left(\frac{s-1}{s+2}\right)^p .
$$
It is holomorphic and nonvanishing on $\Re s>1/2$, including $s=1$. Choose its analytic logarithm using the absolutely convergent Euler logarithm and the bounded rational-factor logarithm in a sufficiently far right half-plane. Borel–Carathéodory on fixed-radius disks centered at $2+it$ gives $O_\eta(\log(2+|t|))$ for that logarithm on each fixed smaller disk remaining in $\Re s>1/2+\eta/2$, by the polynomial growth just established and bounded center values. A fixed inner disk contained in $\Re s>1$ has logarithm bounded uniformly in $t$. Three circles then gives $O_\eta((\log(2+|t|))^\theta)$ for some $\theta<1$ on an intermediate disk containing $1/2+\eta+it$ with a fixed positive margin. For example take outer radius $3/2-\eta/8$, Borel–Carathéodory radius $3/2-\eta/4$, and three-circles radius $3/2-\eta/2$ for $0<\eta<1/2$. Cauchy’s derivative estimate gives $F'/F(1/2+\eta+it)=o_\eta(\log(2+|t|))$ at high height. The rational factor and its derivative are harmless in these high-height estimates. The same bounds apply on the fixed right strips, and yield subpower growth for both $F$ and $G$ there at high height.

The functional equation and Stirling give the fixed-strip factor $T^{d(1/2-\sigma)}$ at high height, where $T=2+|t|$. Interpolate between $1/2\pm\eta$ with $\eta$ arbitrarily small and use the functional equation again on the left. Equivalently strip interpolation uses $H_0$ to remove any pole if the right comparison strip includes 1. The result is
$$
 |F(\sigma+it)|\ll_\varepsilon T^{d\max(1/2-\sigma,0)+\varepsilon}
$$
on bounded real strips at high height. On the left edge the inverse factor is $T^{-d\delta}$ times a fixed-right subpower bound. Compact heights are controlled on the required contours and near-line disks by holomorphy and the chosen avoidance of line zeros.

For the short-window count use the real Hadamard identity
$$
 \Re(X'/X)(1/2+\eta+it)
 =\sum_\gamma\frac{\eta}{\eta^2+(t-\gamma)^2}.
$$
In the canonical product centered at $1/2$, the nonzero canonical correction terms at zeros on the imaginary axis have zero real part. The possible central factor contributes the $\gamma=0$ kernel. The remaining real constant vanishes by the horizontal modulus symmetry at a point on the line off zeros. Real summands converge using the order-one bound, which implies convergence of the inverse-square sum over distant zeros. From Stirling, the logarithmic derivative bound for $F$ and the polynomial factors, the right-hand sum is $(d/2)\log T+o_\eta(\log T)$, at both signs. For fixed $h,\kappa>0$, integrate over $[t-h-\kappa,t+h+\kappa]$. Each zero of $[t-h,t+h]$ contributes at least $2\arctan(\kappa/\eta)$. Divide by $\log T$, send $|t|$ to infinity with all parameters fixed, then send $\eta$ to 0 and $\kappa$ to 0 in this order. It follows that
$$
 \#\{\gamma:|\gamma-t|\le h\}\le (dh/\pi+o_h(1))\log T
$$
for every fixed $h>0$, including multiplicities. The argument gives a unit-window $O(\log T)$ bound also when $d=0$.

To obtain good heights, average $\sum_\gamma\log(1+\eta^2/(t-\gamma)^2)$ on any high fixed interval $J$ of length $\ell_0$. Nearby terms have whole-line integral $2\pi\eta$ each. The remote quadratic tails and the unit-window count give average $O_{\ell_0}((\eta/\ell_0+\eta^2)\log T)$. Choose $\eta$ small after fixing $\ell_0$ and the error exponent. Integrate the real Hadamard identity horizontally from $1/2+\eta$ towards the line. The gamma and polynomial-factor ratio adds $-d(\eta-u)\log T/2+O_\eta(1)$ to the logarithm of the reciprocal at $1/2+u+it$. Together with the $e/2$ reciprocal bound at the right offset this gives exponent $e$ on a chosen horizontal edge, and then on its left part by the functional equation. The finitely many compact heights are chosen off zeros. Select positive and negative heights independently in each $[jD+D/3,jD+2D/3]$, with $D=10^{-4}/(1+d)$ and $\delta=D/100$. Apply the fixed-window count at $h=2D/3$ to bound $k_C$ by $10^{-4}\log T_C$ eventually, since $2dD/(3\pi)<10^{-4}$. The radius-$D$ growth costs at most $dD+e\le10^{-4}+e$. This verifies every interface condition.

## 3. Exponent budget and transfer of the construction

Use $G=1/F$ and the base coefficients $b_n(1-\log n/\ell)$, $\ell=\log N$. The derivative Cauchy and Perron shifts of source (94)–(97) cross only the line-zero poles of $G$. A pole of $F$ makes $G$ holomorphic with a zero, so any fixed pole order contributes no residue. Choose the initial Perron right line strictly beyond the reciprocal series’ abscissa of absolute convergence. The derivative Cauchy contour may send the right line to infinity because $G$ is uniformly bounded there. The retained left edge is upward in the integral formula, and combining the two formulas gives the residual identity in §2 of the fixed-character transfer with $U=F$. The absolute left-edge convolution gives $O(\ell^{-1})$ in norm. Independently chosen positive and negative heights delimit the high strips. Empty cells cancel by their complete contour expressions. For $H=N^{1/20}$ the high-strip squared bound is
$$
 O\!\left(H^{-1}+N^{2\delta}\ell^{-2}H^{-1+4e}+N^{2\delta}H^{-2+4e}\right).
$$
Since $\delta\le10^{-6}$, the slowest squared exponent is at most $-0.049978$.

The rational taper estimate, Newton interpolation of a grouped principal part, and the divided-difference estimate for $F/\prod(s-\rho_i)$ depend only on the analytic interface. Put $c_0=10^{-4}$ and let $a_0\le10^{-4}$ be the excess exponent on a radius-$D$ disk above the shared growth exponent $e$. In the Selberg specialization $a_0=dD$. The near-cell estimate of source (36)–(37) has exponent $-2+2a_0+5e+2c_0\log1200$ after absorbing its $k_C^4$ factor into $T_C^e$. The far-cell estimate of source (38)–(40) has exponent $-2+2\beta+2e$ with $\beta=2e+c_0\log200$. Both exponents are at most $-2+1/100$. For the near cells use bounded overlap. For the far cells use Cauchy–Schwarz with the separated kernels $(1+|t-\tau_C|)^{-2}$, followed by the convolution estimate in the fixed-character proof. The squared norm bound for an arbitrary subset of corrected clusters is therefore
$$
 O\!\left(\ell^{-1}\sum_C (2+|\tau_C|)^{-2+1/100}\right)
$$
with the sum over that subset. The omitted tail beyond fixed $Y$ costs $O(Y^{-99/100}/\ell)$ in squared norm. High multiplicity in a finite collection of cells affects only the prefactor.

For the low-cell delayed correction, use the ordinary coefficients of source (53)–(54), with contour kernel $h_C(x)=(2\pi i)^{-1}\int_{\Gamma_C}G(z)e^{zx}dz$. No Euler restrictions are imposed on correction coefficients. The collective derivative bound in §3 of the fixed-character transfer still uses $H^{2+e}(1+|t|)N^{-(1-\delta)/4}$, because $c_0\log200<1$ and delayed profiles start at $1/4$. The large-$t$ direct bound is $O(H^{1+e}N^\delta)$. Split at $K=N^{3/20}$. The two squared errors have powers of $N$ at most $-0.1499595$ and $-0.049958$, using $\delta\le10^{-6}$. The construction stays in the class of ordinary length-$N$ polynomials.

For each fixed set of complete cells, the top Laurent taper replacements by $(1-u)^{m_\rho}$ and the fixed quadrature cost $O_F(\ell^{-1})$ in norm follow from source (63)–(73). The coefficient bound depends also on the chosen fixed cells. Off a fixed zero window expand into singleton Laurent terms; their separate far bounds also cover gaps inside an original cell hull. Inside a fixed window, scaling by $\ell$ in frequency and applying Plancherel gives the local leading squared constant $m_\rho^2/|\rho|^2$. Lower Laurent orders and cross terms vanish at scale $1/\ell$. Thus fixing all cells up to $Y$, letting $N\to\infty$ with that fixed correction and then sending $Y\to\infty$ proves (1). Convergence of the zero sum follows from the unit-window count.

## 4. Matching lower bound and the pole correction

For $x>0$ put $S(x)=\sum_{n\le x}a_n$ and $R(x)=\operatorname{Res}_{s=1}F(s)x^s/s$, with $R=0$ in the entire case. Define $\psi(t)=R(1/t)-S(1/t)$ for every $t>0$. This is exactly de Roton’s complementary function. Her Theorem 2 applies to every Selberg-class member for which $\psi\in L^2(dt)$. Degree less than four is an unconditional sufficient condition cited on p. 419. Under the growth bounds here, that degree restriction can be removed using a distributional Mellin shift.

In detail, set $v=\log x$, $c>1$, and $B(s)=F(s)/s$. Absolute Dirichlet convergence gives the ordinary Fourier transform
$$
 \int_{\mathbb R}e^{-itv}e^{-cv}S(e^v)\,dv=B(c+it).
$$
Indeed the underlying weighted sum of integrals is at most $\sum |a_n|n^{-c}/c$. Pair the inverse transform of $S(e^v)$ with an arbitrary smooth compactly supported function $\varphi(v)$. The resulting vertical integral contains $B(s)\int\varphi(v)e^{sv}dv$, whose second factor decays faster than every inverse power of $|\Im s|$ throughout the fixed strip $1/2\le\Re s\le c$. Polynomial growth of $F$ permits a contour shift down to the critical line in this tested integral. The residue at 1 is exactly the pairing with $R(e^v)$, for every pole order. Hence $e^{-v/2}[S(e^v)-R(e^v)]$ is the distributional inverse Fourier transform of $B(1/2+it)$. The critical-line subpower bound makes this transform square integrable by Plancherel. The original functions are locally integrable, so the distributional identification holds almost everywhere. Changing variables $t=e^{-v}$ gives
$$
 \|\psi\|_{L^2(dt)}^2=\int_{\mathbb R}e^{-v}|S(e^v)-R(e^v)|^2dv<\infty ,
 \qquad
 \int_0^\infty \psi(t)t^{s-1}dt=-F(s)/s
$$
on the critical line in the $L^2$ Mellin sense. The Mellin integral is interpreted by Plancherel, with no assertion of absolute convergence on that line.

The target $1_{(0,1)}$ transforms to $1/s$, and a dilation $\psi(t/\alpha)$ contributes the factor $\alpha^s$. Thus de Roton’s continuous span with $1/N\le\alpha\le1$ contains the integer dilates $\alpha=1/n$. In the exact given norm the continuous distance satisfies $D(1/N)\le \Delta_{N,F}$. Applying de Roton’s Theorem 2 and squaring proves the matching liminf under GRH. The square-integrability argument applies for any one fixed degree once critical growth has been established. [De Roton, Theorem 2, original PDF](https://www.numdam.org/item/10.24033/bsmf.2516.pdf)

More generally, if the principal part of $F(s)/s$ at 1 is $\sum_{j=1}^p d_j(s-1)^{-j}$, then $R(x)=x\sum_{j=1}^p d_j(\log x)^{j-1}/(j-1)!$. The contribution of $t>1$ to the Mellin transform of $\psi$ is $\sum_j(-1)^{j-1}d_j/(1-s)^j=-\sum_j d_j/(s-1)^j$. This identifies the entire pole part independently of its order.

For example, $F=\zeta^2$ has double pole and $R(x)=x(\log x+2\gamma_{\rm E}-1)$. For $t>1$ the complementary function is $\psi(t)=(2\gamma_{\rm E}-1-\log t)/t$, since $S(1/t)=0$. Its contribution to the Mellin transform on the critical line is
$$
 \frac{2\gamma_{\rm E}-1}{1-s}-\frac{1}{(1-s)^2}.
$$
This has precisely the principal part of $-\zeta(s)^2/s$ at 1. Removing the $t>1$ part would remove this pole and change the approximation model. For the full boundary norm no coefficient conditions $A(1)=A'(1)=0$ are imposed. The formula here concerns a Cauchy-weighted boundary norm rather than a Hardy-space norm requiring the residual to be holomorphic inside the right half-plane. The prediction for $\zeta^2$ under RH is the constant $4\sum_\rho m_\rho(\zeta)^2/|\rho|^2$.

## Provenance and scope

The method of the upper estimate is rStation 48 v2’s adaptive construction, with its retained-left-edge version (94)–(97) and the finite singleton repair from the director reconstruction. The Selberg-class lower bound is de Roton’s published result. De Roton’s sequential criterion is prior work on the qualitative discrete approximation problem. The bounded literature search did not identify an equivalent sharp upper theorem for this whole stated class. Priority remains open. Neither the estimates nor the exhaustion steps are uniform in degree, conductor, gamma data or pole order. [Adaptive construction](https://rstation.ai/problems/riemann_hypothesis/papers/48/v2) · [De Roton lower bound](https://www.numdam.org/articles/10.24033/bsmf.2516/) · [De Roton sequential criterion](https://hal.science/hal-00091966v2)
