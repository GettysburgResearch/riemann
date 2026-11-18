# Adaptive Nyman–Beurling approximation for a fixed primitive character

Fix a primitive Dirichlet character $\chi$ and assume GRH for $U=L(\cdot,\chi)$. In the source norm $\|f\|_*^2=(2\pi)^{-1}\int_{\mathbb R}|f(1/2+it)|^2\,dt/(1/4+t^2)$, let $\Delta_{N,\chi}^2$ be the infimum of $\|1-UA\|_*^2$ over ordinary Dirichlet polynomials of integer length at most $N$, with complex coefficients. The retained-edge proof of rStation 48 v2 transfers to give
$$
 \limsup_N(\log N)\Delta_{N,\chi}^2\le
 C_\chi:=\sum_{\rho\ {\rm distinct}}\frac{m_\rho^2}{|\rho|^2}.
$$
The sum includes both signs and any central zero. De Roton’s published theorem gives the reverse liminf, as verified below. Constants may depend on the fixed character. For the primitive principal character of conductor 1, use the source zeta theorem. Henceforth $\chi$ is nonprincipal. [rStation 48 v2](https://rstation.ai/problems/riemann_hypothesis/papers/48/v2) · [main proof reconstruction](director_rstation48_main_theorem_round6.md)

## 1. GRH estimates and contours

Put $F=1/U$, $T=2+|t|$, and let $\kappa\in\{0,1\}$ denote character parity. The order-one entire completion is
$$
 \Xi_\chi(s)=(q/\pi)^{(s+\kappa)/2}\Gamma((s+\kappa)/2)U(s).
$$
It satisfies $\Xi_\chi(s)=\epsilon_\chi\Xi_{\bar\chi}(1-s)=\epsilon_\chi\overline{\Xi_\chi(1-\bar s)}$. In particular GRH transfers to $\bar\chi$ by conjugation. The same-character modulus symmetry is horizontal at fixed ordinate. A complex character need not have zeros paired at opposite ordinates.

For fixed $\eta,\varepsilon>0$ the functions $U,F$ are $O_{\chi,\eta,\varepsilon}(T^\varepsilon)$ on bounded strips with $\sigma\ge1/2+\eta$. On the zero-free right half-plane choose the holomorphic logarithm with its Euler-product value on $\Re s>1$. For $0<\eta\le1$, Borel–Carathéodory on disks centered at $2+it$ with outer radius $3/2-\eta/4$ and inner radius $3/2-\eta/2$ gives $\log U=O_{\chi,\eta}(\log T)$ on the line $1/2+\eta/2$. The real part is bounded above by the logarithm of the standard polynomial growth from the functional equation, Stirling, absolute convergence and the strip maximum principle. The logarithm is bounded at the disk centers by absolute convergence. Apply three-lines between this line and $2$ to $\log U(z)e^{(z-it)^2}$ for each target ordinate $t$. The respective outer norms are $O_{\chi,\eta}(\log T)$ and $O_\chi(1)$ since the Gaussian absorbs the ordinate difference. Thus $\log U=O_{\chi,\eta}((\log T)^\theta)$ for $\sigma\ge1/2+\eta$ up to 2, with a fixed $\theta<1$. Beyond 2 use absolute convergence. This yields both reciprocal and direct growth. The functional equation and Stirling give the corresponding direct bound on $1/2-\eta$ with the additional factor $T^\eta$. Interpolate across $1/2\pm\eta$ with $\eta$ small, then use the functional equation on the fixed left strip. This proves the requisite all-strip bound $|U(\sigma+it)|\ll_{\chi,\varepsilon} T^{\max(1/2-\sigma,0)+\varepsilon}$. On the fixed left edge $1/2-\delta$, the reciprocal bound is $O_{\chi,\delta,\varepsilon}(T^\varepsilon)$ by Stirling and the reciprocal for $\bar\chi$ on $1/2+\delta$. Compact heights on either vertical edge are harmless by nonvanishing.

The requisite zero count follows without a variable-window estimate. For fixed $h,\Delta>0$, the Beurling–Selberg majorant for $[-h,h]$ has integral $2h+\Delta^{-1}$, Fourier support $[-\Delta,\Delta]$ with convention $e^{-2\pi i u\xi}$, and quadratic decay on horizontal strips. Apply the primitive Dirichlet Weil explicit formula to its translate by $t$. GRH lets it majorize the real ordinates term by term, with multiplicity. The prime sum is bounded independently of $t$ because only $n\le e^{2\pi\Delta}$ occur and translation changes only the Fourier phase. The gamma and conductor weight is $\log(q/\pi)+\Re(\Gamma'/\Gamma)((1/2+\kappa+iu)/2)=\log(2+|u|)+O_\chi(1)$. Its integral against the translated majorant, including the factor $1/(2\pi)$, gives
$$
 \#\{\gamma:|\gamma-t|\le h\}
 \le \frac{2h+\Delta^{-1}}{2\pi}\log(2+|t|)+O_{\chi,h,\Delta}(1).
$$
Indeed the shifted logarithm differs from $\log(2+|t|)$ by at most $\log(2+|u-t|)$, integrable against the original majorant. The formula applies for either sign; see Lemmas 3–4 of Zhao for the explicit normalization and its reference to Iwaniec–Kowalski, Theorem 5.12. [Zhao, *Conditional estimates on the argument of Dirichlet L-functions with applications to low-lying zeros*](https://doi.org/10.1112/blms.70360)

Hadamard gives $\Re(\Xi_\chi'/\Xi_\chi)(1/2+u+it)=\sum_\gamma u/[u^2+(t-\gamma)^2]$. The real constant vanishes by the same-character horizontal modulus symmetry, evaluated off zeros on the line. The real Hadamard constants and remote summands converge absolutely by the unit-window count. Average $K_\eta(t)=\sum_\gamma\log(1+\eta^2/(t-\gamma)^2)$ over any interval $J$ at large height modulus of fixed length $\ell_0$. Count nearby zeros using the unit-window bound and the whole-line integral $2\pi\eta$ of each kernel. Bound the rest by the quadratic tails and unit-window count. The average is $O_{\chi,\ell_0}((\eta/\ell_0+\eta^2)\log T)$. Choose $\eta$ sufficiently small so some $t_J$ off all zeros has $K_\eta(t_J)\le e\log T$. In moving horizontally left from $1/2+\eta$ to $1/2+u$, $0\le u\le\eta$, inverse completion gains at most $K_\eta(t_J)/2$ in logarithm. The gamma and conductor ratio adds $-(\eta-u)\log T/2+O_{\chi,\eta}(1)$ to the inverse of $U$. Start with reciprocal exponent $e/2$ at $1/2+\eta$. This gives $|F|\ll T^e$ throughout the chosen horizontal edge on the right, and on the fixed left portion by the same-character completion symmetry and Stirling.

Set $D=e=10^{-4}$ and $\delta=10^{-6}$. For every integer $j$, select the horizontal edge inside $[jD+D/3,jD+2D/3]$. Apply the high-height construction independently at both signs. On the finite compact range choose edges off the finitely many zero ordinates. Adjacent rectangles have vertical edges $1/2\pm\delta$, center $\tau_C$, perimeter below $4D$, and every boundary-to-root distance below $2D$. The centers are separated by $2D/3$ and the cell containing ordinate 0 is an ordinary finite cell. With $T_C=2+|\tau_C|$ the contour bound is $|F|\ll_\chi T_C^e$. Use the count with $h=2D/3$ and fixed $\Delta$ large enough that $(4D/3+\Delta^{-1})/(2\pi)<D$. Then the total multiplicity satisfies $k_C\le D\log T_C$ eventually. The finitely many exceptions are absorbed into constants. Retain empty rectangles for cancellation.

## 2. Retained edge and high strips

Write $\ell=\log N$, $a=1/2-\delta$ and $R_C$ for the principal part of $F$ in $C$. The absolutely convergent reciprocal series on $\Re s>1$ has coefficients $\mu(n)\chi(n)$. Set $V_N=\sum_{n\le N}\mu(n)\chi(n)n^{-s}(1-\log n/\ell)$, and set
$$
 J_\nu(s)=\frac1{2\pi i}\int_{(a)} F(z)e^{\nu(z-s)}(z-s)^{-2}\,dz
 \quad(\nu=0,\ell)
$$
on the upward line. Shift derivative Cauchy contours, sending independently chosen top and bottom heights to infinity first and then the right edge to infinity. The remote grouped derivatives are $O_K(D T_C^{-2+e})$, horizontal edges tend to zero by the reciprocal estimate, and the right edge tends to zero by absolute convergence. The downward left edge gives $F'=\sum_C R_C'-J_0$. Perron shifted only to $a$ gives $\ell V_N=\ell F+F'+\sum_C B_C+J_\ell$, where $B_C$ is the sum of the residues at cluster poles of $F(z)e^{\ell(z-s)}/(z-s)^2$. The endpoint weight vanishes. At fixed $N$ the horizontal integrals vanish and remote grouped residues converge by the same estimates with a fixed $N^\delta$ factor. Trivial zeros lie left of $a$. The nonprincipal $U$ is regular and nonzero at 1, so there is no residue or cap correction there.

For a proper rational function $R$, let $T_{\ell,w}R$ be its causal Laplace transform truncated with taper $w(x/\ell)$. The termwise rational identity of source (44) gives $T_{\ell,w_1}R_C=R_C+(R_C'+B_C)/\ell$ for $w_1(u)=1-u$. Consequently
$$
 1-UV_N=\sum_C E_C^{(1)}+\frac{U}{\ell}(J_0-J_\ell),\qquad
 E_C^{(1)}=U(R_C-T_{\ell,w_1}R_C).
$$
The left contribution has norm $O_\chi(\ell^{-1})$ by $|e^{\ell(z-s)}|=N^{-\delta}$ and convolution of $(2+|y|)^e$ with $(\delta^2+(t-y)^2)^{-1}$. The resulting pointwise majorant after multiplication by $U$ is $O_\chi(\ell^{-1}(2+|t|)^{2e})$.

The complete cell expression is its inside indicator minus
$U(s)/(2\pi i\ell)$ times the contour integral of $F(z)(e^{\ell(z-s)}-1)/(z-s)^2$. The indicator arises from the residue at $s$ and cancels the integral when the cell is empty. Telescope shared edges over two separately bounded exterior strips with inner heights $h_\pm$ satisfying $|h_\pm|=H+O(D)$. At fixed $N$ the same estimates below on the receding outer edges show convergence in norm. For the remaining vertical sides, Cauchy–Schwarz with kernel $(\delta^2+v^2)^{-1}$ bounds the squared norm by $O_\chi(N^{2\delta}\ell^{-2} H^{-1+4e})$. On horizontal sides retain $e^{\ell w}-1=w\int_0^\ell e^{vw}dv$. The real kernel is $2\operatorname{arsinh}(\delta/|t-h_\pm|)$, whose square has an integrable logarithmic singularity and quadratic decay. Both convolution bounds follow by splitting near 0, near the translated height, and in the remainder against $(2+|t|)^{-2+2e}$. The horizontal cost is $O_\chi(N^{2\delta}H^{-2+4e})$ and the indicator cost is $O(H^{-1})$, both in squared norm. This reproduces (46)–(49) independently for either sign.

## 3. Delayed profiles and actual coefficient support

Use exactly the source profiles (22)–(23). For $k\ge2$ they agree with $1-u$ up to $1/4$, are $C^{k-1}$, and vanish to order $k$ at 1. The source rational estimates (25)–(26) apply without change to each product $P_m(s)=\prod_{i=1}^m(s-\rho_i)$, with $m\le k$, because their convolution and bounded-variation proof uses only real ordinates and admits repeated nodes. They give squared unweighted error $k^2 200^{2k}/\ell$ for $1-P_mT_{\ell,w_k}(1/P_m)$ and pointwise error $4k^2200^k/(\ell d^{m+1})$ for $1/P_m-T_{\ell,w_k}(1/P_m)$ off the ordinate hull at distance $d$.

The Newton principal-part representation (32)–(33) follows by integrating the expansion of the Cauchy kernel against $F$. Its coefficient of degree $m$ has bound $C_\chi T_C^e(2D)^m$. On $|t-\tau_C|\le5D$ the quotient $U/\prod_i(s-\rho_i)$ is a divided difference and has bound $C_\chi D^{-k}T_C^{D+e}$ from the radius-$D$ Cauchy estimate and Hermite–Genocchi. The simplex volume cancels the derivative factorial. Removing the unused factors costs $(6D)^{k-m}$. Together the squared weighted near-cell contribution is bounded by $C_\chi\ell^{-1}T_C^{-2+2D+5e+2D\log1200}$, after absorbing the polynomial factors in $k$. Off the near window $2D/d<1/2$, so the geometric sum and the pointwise rational bound give $C_\chi |U| T_C^\beta/[\ell(1+|t-\tau_C|)^2]$ with $\beta=2e+D\log200$. The near windows overlap a bounded number of times, and Cauchy–Schwarz for the far kernel uses $\sum_C(1+|t-\tau_C|)^{-2}\ll_D1$. The resulting far convolution against the weight $(2+|t|)^{-2+2e}$ gives squared bound $C_\chi\ell^{-2}\sum_{C\in B}T_C^{-2+2\beta+2e}$ for any subset $B$. Both losses are below $1/100$. Thus in the full weighted norm,
$$
 \left\|\sum_{C\in B}U(R_C-T_{\ell,w_{k_C}}R_C)\right\|_*^2
 \ll_\chi \ell^{-1}\sum_{C\in B}T_C^{-2+1/100}.
$$
The squared tail above $Y$ is $O_\chi(Y^{-99/100}/\ell)$ by separation of centers. All estimates use contours rather than inverse derivatives.

For $H=N^{1/20}$ define $h_C(x)=(2\pi i)^{-1}\int_{\Gamma_C}F(z)e^{zx}dz$ and add the polynomial
$$
 D_N(s)=\sum_{n\le N}n^{-s-1}\sum_{|\tau_C|\le H}h_C(\log n)
 \left[w_{k_C}(\log n/\ell)-(1-\log n/\ell)\right].
$$
The integral over $1\le y\le N$ in place of the sum is exactly the delayed-taper correction to the retained-edge base. The bracket vanishes at the endpoints and is supported on $N^{1/4}\le y\le N$. The contour gives summed bounds $H^{1+e}y^{1/2+\delta}$ and $H^{2+e}y^{1/2+\delta}$ for $h_C(\log y)$ and $h_C'(\log y)$, respectively. Profile derivative growth costs at most $T_C^{D\log200}$ up to fixed constants, within the second bound since $D\log200<1$. The extended critical-line integrand has integrated absolute derivative at most $C_\chi H^{2+e}(1+|t|)N^{-(1-\delta)/4}$. Euler quadrature is valid across the fixed profile knots by continuity. For $|t|\le K=N^{3/20}$ use this bound. For larger $|t|$ the absolute size of the sum and integral is $O_\chi(H^{1+e}N^\delta)$. The resulting squared weighted $U$-multiplied errors are
$$
 O_\chi(H^{4+2e}N^{-(1-\delta)/2}K^{1+2e})
      =O_\chi(N^{-0.1499595}),\qquad
 O_\chi(H^{2+2e}N^{2\delta}K^{-1+2e})
      =O_\chi(N^{-0.049958}).
$$
The high-strip exponents have a strict negative margin as well. The coefficient corrections are supported on ordinary integers up to $N$ and are allowed at integers divisible by primes dividing $q$.

## 4. Fixed optimal profiles

Fix finitely many complete cells $\mathcal F$. At a distinct zero $\rho$ of order $m$ in cell $C$, let $a_{\rho,m}$ be the top Laurent coefficient of $F$. The polynomial replacing its leading profile by $(1-u)^m$ is
$$
 a_{\rho,m}\sum_{n\le N}n^{\rho-1-s}
 \frac{(\log n)^{m-1}}{(m-1)!}
 \left[(1-\log n/\ell)^m-w_{k_C}(\log n/\ell)\right].
$$
Source (63)–(68) uses the same untwisted integer grid here. For each fixed bracket polynomial by pieces $q$, with $q(0)=q(1)=0$, the first piece contributes $O(\ell^{-1})$ coefficients to the derivatives of the regular term $\zeta(1+s-\rho)-1/(s-\rho)$. The remaining pieces cancel those regular terms between their endpoints. The remainder is $O((1+|s-\rho|)\ell^{m-1}N^{-\alpha})$ up to $|t|\le N^{\alpha/2}$, where $\alpha>0$ is the first positive fixed knot. On the higher tail the absolute size of the sum and integral is $O((1+\ell)^m)$. The critical-line growth of $U$ gives $O_{\mathcal F}(\ell^{-1})$ weighted quadrature cost in norm. This step introduces no uniform estimates for the finite Laurent coefficients.

Write $U(s)=(s-\rho)^m G_\rho(s)$. The top error on a fixed window about $\gamma$ is $[G_\rho(s)/G_\rho(\rho)]e_{m,w}(\ell(t-\gamma))$. The singleton profile estimates give $|e_{j,w}(v)|\ll(1+|v|)^{-1}$ by bounded variation and Fourier Plancherel gives squared integral $c_m(w)$ in measure $dv/(2\pi)$. For $w(u)=(1-u)^m$, $c_m(w)=m^2$ by the shifted Legendre calculation (70), (73). Therefore the scaled squared local norm tends to $m^2/|\rho|^2$. Each lower Laurent order has an extra factor $(s-\rho)$, so its squared local cost is $O(\ell^{-2})$. Outside a term’s own fixed window the singleton bound gives $O(|U|/[\ell|t-\gamma|^{j+1}])$ for Laurent order $j$, including points in any gap inside a cell hull. Thus on disjoint fixed zero windows the cross contributions vanish at the leading squared scale, and the complements have $O_{\mathcal F}(\ell^{-1})$ norm. A central root has the ordinary weight $4m^2$.

Take $\mathcal F$ to be the cells up to a fixed $Y$. For large $N$ these are low cells. The constructed approximants give a limsup for $\sqrt{\ell}\Delta_{N,\chi}$ at most $(\sum_{\rho\in\mathcal F}m_\rho^2/|\rho|^2)^{1/2}+O_\chi(Y^{-99/200})$. Then send $Y$ to infinity. The series converges because the unit-window count bounds the sum of squared multiplicities in a unit window by $O_\chi(\log^2(2+|\gamma|))$. This proves the claimed upper bound.

## 5. Published lower bound and priority scope

Anne de Roton’s *Une approche hilbertienne de l’hypothèse de Riemann généralisée*, BSMF 134 (2006), pp. 417–445, defines the complementary functions and continuous scale-$\lambda$ distance on p. 419 and proves the multiplicity-squared lower bound in Theorem 2, p. 420. A primitive Dirichlet $U$ belongs to the Selberg class. For nonprincipal $\chi$ the pole residue at 1 vanishes, hence its complementary function is $\Psi_U(1/t)=-\sum_{n\le1/t}\chi(n)$. This function is bounded by period cancellation, supported in $0<t\le1$, and belongs to $L^2(0,\infty;dt)$. Its Mellin transform is $-U(s)/s$ by partial summation. The dilate with scale $\alpha$ gives a factor $\alpha^s$, so the continuous class for $1/N\le\alpha\le1$ contains all integer scales $\alpha=1/n$ for $n\le N$. Complex coefficients absorb the sign. The target Mellin transforms to $1/s$, and Mellin–Plancherel gives exactly $D(1/N)\le\Delta_{N,\chi}$ in the stated norm. Under GRH the theorem’s critical zeros are all the nontrivial ones. Squaring its nonnegative lower bound proves the reverse liminf. [De Roton’s original PDF](https://www.numdam.org/item/10.24033/bsmf.2516.pdf) · [Preserved primary copy](../../sources/effective_cluster62_dirichlet/de_roton_2006_numdam.pdf)

The unanchored distance and its qualitative zero-free criterion already occur in Dimitrov–Oliveira Theorem 2. Their Theorem 3 is a separate interpolation problem. De Roton’s 2009 sequential criterion treats discrete approximation in the broader Selberg setting. Delaunay–Fricain–Mosaki–Robert treat zero-free regions and criteria for broader Dirichlet series. A bounded search for an equivalent sharp upper theorem found the zeta-specific rStation 48 v2 as the direct source of this transfer. Priority of the upper transfer remains open. [Dimitrov–Oliveira](https://arxiv.org/abs/1608.07887) · [De Roton 2009](https://hal.science/hal-00091966v2) · [Delaunay–Fricain–Mosaki–Robert](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/emmanuel_fricain/Dirichlet-SeriesII.pdf)
