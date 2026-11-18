# Fixed primitive Dirichlet characters and adaptive upper approximation

Let $\chi$ be a fixed primitive character and $L_\chi(s)=L(s,\chi)$. Put
$$
d_{N,\chi}^2=\inf_{A\in\mathcal D_N}\|1-L_\chi A\|_*^2,\qquad
\|f\|_*^2=\int_{\mathbb R}\frac{|f(1/2+it)|^2}{1/4+t^2}\,\frac{dt}{2\pi},
$$
where $A(s)=\sum_{n\le N}a_n n^{-s}$ with arbitrary complex coefficients. The adaptive upper construction of RST048 transfers under GRH for this $L_\chi$ and gives
$$
\limsup_{N\to\infty}(\log N)d_{N,\chi}^2
\le \sum_{\rho\ {\rm distinct}}\frac{m_\rho^2}{|\rho|^2}.
$$
The sum uses both signs of the ordinates, with a central zero included once if present. The exact matching lower bound follows from de Roton's continuous Selberg-class result via integer dilations. The case of conductor 1 reduces to the zeta upper and lower bounds in the source theorem. The rest of this audit treats primitive nonprincipal $\chi$. [RST048 v2, Theorem 1 and §§2–7, 9.2](../sources/ratio62_q1_priority/rstation_48_v2.md) · [Independent reconstruction of the zeta proof](adversarial_reviews/director_rstation48_main_theorem_round6.md)

## Fixed-strip bounds and signed good heights

Write $q$ for the conductor, $a_\chi=(1-\chi(-1))/2$, $F_\chi=1/L_\chi$, and $\Xi_\chi(w)=\Lambda_\chi(1/2+w)$ for the completed primitive $L$-function centered at $1/2$. Its functional equation is $\Xi_\chi(w)=\epsilon_\chi\overline{\Xi_\chi(-\bar w)}$, with $|\epsilon_\chi|=1$. This is reflection across the imaginary axis in the $w$-plane. For complex $\chi$, the ordinates of a single $L_\chi$ need not be symmetric under sign change.

Here is a direct derivation of the source's two analytic inputs. For fixed $0<\eta<1/2$, anchor an analytic logarithm of $L_\chi$ at $2+it$ by its absolutely convergent Euler logarithm. GRH together with classical nonvanishing on $\Re s=1$ gives an analytic branch on the disk of radius $3/2-\eta/8$. A crude fixed-strip polynomial bound gives $\Re\log L_\chi=O_\chi(\log(2+|t|))$ there. Borel–Carathéodory gives this absolute bound for the logarithm on the smaller radius $3/2-\eta/4$; on radius $1/2$ the Euler logarithm is bounded. Three circles then gives $|\log L_\chi|\ll_{\chi,\eta}(\log(2+|t|))^\theta$ on radius $3/2-\eta/2$ for fixed $\theta<1$. Cauchy's estimate on a smaller disk gives $L'_\chi/L_\chi(1/2+\eta+it)=o_{\chi,\eta}(\log(2+|t|))$. The same logarithm bound gives $L_\chi$ and $F_\chi$ of subpower growth on $\Re s\ge1/2+\eta$. It extends to the right by absolute convergence. Apply the primitive functional equation with the conjugate character and Stirling's formula to bound $L_\chi$ on $1/2-\eta$ by $O_{\chi,\eta,\varepsilon}((2+|t|)^{\eta+\varepsilon})$; the conjugate character inherits GRH by conjugation. Phragmén–Lindelöf between the two lines, choosing $\eta$ small for each desired exponent, gives the critical-line subpower bound. Stirling and the functional equation then give the source's full bounded-strip majorant $L_\chi(\sigma+it)\ll(2+|t|)^{\max(1/2-\sigma,0)+\varepsilon}$. They also give the left fixed-offset subpower reciprocal bound.

Hadamard factorization of the entire order-one function $\Xi_\chi$ gives, for $u>0$,
$$
\Re \frac{\Xi'_\chi(u+it)}{\Xi_\chi(u+it)}
=\sum_\gamma\frac{u}{u^2+(t-\gamma)^2}.
$$
Under GRH all canonical-product zeros are purely imaginary, so the canonical correction terms have zero real part. The real part of the remaining constant vanishes because $\Xi_\chi(it)$ has fixed phase modulo sign on each zero-free interval of the imaginary axis, and hence $\Re(\Xi'_\chi/\Xi_\chi)(it)=0$ there. This argument retains the term of a possible zero at 0 in the $w$-plane. The gamma factor and the logarithmic derivative bound just proved give
$$
\sum_\gamma\frac{\eta}{\eta^2+(t-\gamma)^2}
=\tfrac12\log\frac{q|t|}{2\pi}+o_{\chi,\eta}(\log |t|).
$$
For fixed $h,\kappa>0$, integrate over $t\in[T-h-\kappa,T+h+\kappa]$. Every zero with $|\gamma-T|\le h$ contributes at least $2\arctan(\kappa/\eta)$. Divide by $\log |T|$ and take $|T|\to\infty$ with all parameters fixed, then $\eta\to0$ and $\kappa\to0$. This proves
$$
\#\{\gamma:|\gamma-T|\le h\}\le (h/\pi+o_{\chi,h}(1))\log |T|.
$$
All counts include multiplicity. In particular unit-window counts are $O_\chi(\log(2+|T|))$. Either proof by Hadamard identities uses the whole signed zero set, even at negative heights. [For the standard completed primitive $\xi_\chi$ factorization, Dimitrov–Oliveira (2.5)–(2.6)](../sources/ratio62_rstation48/dimitrov_oliveira.txt)

To obtain good horizontal lines, integrate the real logarithmic derivative between $1/2+u$ and $1/2+\eta$ as in source (12). The gamma contribution is $-(\eta-u)\log(q|t|/2\pi)/2+O_\chi(\eta)$. On a fixed interval $J$ of length $\ell$, the average of $\sum_\gamma\log(1+\eta^2/(t-\gamma)^2)$ is $O_\chi((\eta/\ell+\eta^2)\log(2+|T|))$, using the integral $2\pi\eta$ of each kernel and the unit-window count for the tails. Choose $\eta$ sufficiently small after fixing $\ell$ and the desired exponent. This supplies $F_\chi\ll T^\varepsilon$ at one ordinate in each sufficiently high interval $J$ over the segment $1/2\le\sigma\le2$. The same bound on the bounded left segment follows by the functional equation in its conjugate form, with reciprocal gamma factor of size $O_{\chi}((2+|t|)^{\sigma-1/2})$. The right follows from absolute convergence. Select heights independently for all integer $j$ from $[jD+D/3,jD+2D/3]$, with $D=e=10^{-4}$ and error exponent $e$. For the finitely many low intervals, select any height that avoids zero ordinates. In particular the panel containing ordinate zero lies between $j=-1$ and $j=0$. Take $\delta=10^{-6}$. The bounding rectangle sides are $1/2\pm\delta$; each cluster satisfies $k_C\le D\log T_C$ eventually because its height is at most $4D/3$ and the fixed-window coefficient is $2D/(3\pi)<D$. The contour bound is $O_\chi(T_C^e)$, where $T_C=2+|\tau_C|$ and $\tau_C$ is its midheight. [RST048 §§2.1–2.2](../sources/ratio62_q1_priority/rstation_48_v2.md)

## Retained edge, high tail and actual coefficients

Use $L=\log N$ for the logarithmic cutoff, $\sigma_l=1/2-\delta$, and upward orientation on the left line. There is no need to track trivial zeros, which are to its left. In the notation of (94)–(97), take $G=F_\chi$ and $W=1$. Cauchy's second-order integral gives $F'_\chi=\sum_C R_C'-J_0$, where $R_C$ is the grouped principal part and $J_0$ the left-edge integral. The right line can be sent to infinity in this derivative formula because $F_\chi$ is bounded there by its absolutely convergent Dirichlet series. Fix $N$ when taking the horizontal heights to infinity. The Perron integral on $\Re z=2$ has value $L V_N$, with
$$
V_N(s)=\sum_{n\le N}\mu(n)\chi(n)n^{-s}(1-\log n/L).
$$
Indeed the reciprocal Euler product has coefficient $\mu(n)\chi(n)$, also at integers sharing factors with the conductor. Shifting only to the retained left edge gives $L V_N=L F_\chi+F'_\chi+\sum_C B_C+J_N$. Combining with the finite rational identity (44) gives
$$
1-L_\chi V_N=\sum_C E_C^{(1)}
+\frac{L_\chi(s)}{2\pi i L}\int_{(\sigma_l)}
\frac{F_\chi(z)(1-e^{L(z-s)})}{(z-s)^2}\,dz .
$$
The left norm is $O_\chi(L^{-1})$: the absolute convolution of $(2+|y|)^e$ with $(\delta^2+(t-y)^2)^{-1}$ is $O((2+|t|)^e)$, and the multiplier $L_\chi$ contributes another subpower $(2+|t|)^e$. Keeping this integral is necessary for the identity. The lack of a pole at $s=1$ carries no cost, since the polynomial class has no anchoring requirement. [RST048 equations (44), (94)–(97)](../sources/ratio62_q1_priority/rstation_48_v2.md)

For the tail of clusters with $|\tau_C|>H$, keep empty rectangles to telescope both end strips. The boundaries are independently selected $h_+=H+O(D)$ and $h_-=-H+O(D)$; the indicator is $\mathbf1_{\{t>h_+\ {\rm or}\ t<h_-\}}$. The source's vertical kernel estimate and the horizontal numerator cancellation $e^{Lw}-1=w\int_0^Le^{vw}\,dv$ depend only on absolute height. Together they give squared norm
$$
O_\chi\big(H^{-1}+N^{2\delta}L^{-2}H^{-1+4e}+N^{2\delta}H^{-2+4e}\big).
$$
This preserves the two actual endpoints without reflecting either good-height family.

For the corrected clusters, RST048 Lemma 3 uses causal exponentials with frequencies given by the zeros after shifting by $1/2$. All are real frequencies regardless of signs. The Newton coefficients are bounded by $C_\chi T_C^e(2D)^j$ for a denominator of degree $j$, and dividing $L_\chi$ by the full zero product on the near window uses Cauchy on radius-$D$ disks. The ratio is a divided difference and the simplex volume cancels the derivative factorial. Thus the source's exponential multiplicity costs, including $1200^{2k_C}$ in the near squared norm, are unchanged. The constant from the strip growth of $L_\chi$ and reciprocal occurs as a fixed prefactor. With $k_C\le D\log T_C$ the resulting norm inequality (41) is $C_\chi L^{-1}\sum_{C\in\mathcal B}T_C^{-2+1/100}$ for any subset $\mathcal B$. This both provides a summable corrected tail and avoids any bound on inverse individual derivatives.

For $H=N^{1/20}$ the delayed correction is exactly an integer Dirichlet polynomial with coefficients
$$
n^{-1}\sum_{|\tau_C|\le H}h_C(\log n)
     (w_{k_C}(\log n/L)-(1-\log n/L)),\qquad
h_C(x)=\frac1{2\pi i}\oint_{\Gamma_C} F_\chi(z)e^{zx}\,dz.
$$
The coefficients can be complex and need have no multiplicative, ramified-prime, or conjugation symmetry. The continuous integral with the same integrand realizes the profile substitution; it is a comparison quantity, and the polynomial above is the admissible approximant. The derivative bound for their quadrature is $O_\chi(H^{2+e}(1+|t|)N^{-b(1-\delta)})$ after integrating in $y$, with $b=1/4$. For the high-$t$ bound, the direct sum and integral are $O_\chi(H^{1+e}N^\delta)$. Splitting at $N^{3/20}$ as in (59)–(61) gives squared powers $-0.1499595$ and $-0.049958$, and the slowest high-cluster first-order squared power is $-0.049978$. These strict inequalities are unchanged by fixed-character constants. [RST048 equations (25)–(41), (46)–(49), (51)–(61)](../sources/ratio62_q1_priority/rstation_48_v2.md)

## Fixed repair and limiting coefficient

At each zero of multiplicity $m$, the top coefficient of $F_\chi$ is $m!/L_\chi^{(m)}(\rho)$. The multiplier after multiplying by $L_\chi$ takes value 1 at $\rho$. The same rescaling and Plancherel argument as (69)–(73) therefore gives a local squared leading term $c_m(w)/(L|\rho|^2)$. For fixed finite neighborhoods, use the singleton Laurent expansion, so the far estimates apply even in a gap inside a cluster hull. Lower Laurent terms have a positive power of $s-\rho$, giving local squared $O(L^{-2})$ as in (71). The argument works at $\rho=1/2$ because $|\rho|^2=1/4$.

For finitely many fixed whole clusters, replace the top profile at each zero by $(1-u)^m$ and achieve $c_m=m^2$. Their fixed-profile quadrature still uses the Euler difference $\zeta(1+s-\rho)-1/(s-\rho)$, because the sampling is over ordinary integers. Its fixed derivatives on the boundary grow at most logarithmically as in (65)–(68). The factor multiplying this quadrature difference is $L_\chi$; its subpower bound gives $O_\chi(L^{-1})$ norm exactly as needed. The fixed-Laurent qualification is sufficient, and no uniform estimate in growing fixed-repair data is used.

For a fixed repair set, pass to $N\to\infty$ first. Equation (41) bounds the remaining scaled norm of any corrected clusters beyond height $Y$ by $C_\chi Y^{-99/200}$. Let $Y\to\infty$, then exhaust the fixed repair sets. This gives the asserted limsup. The limiting multiplicity-square sum converges by the unit-window counts, since the sum of $m_\rho^2$ in a unit window is bounded by the square of the total count. [RST048 §§7.1–7.3](../sources/ratio62_q1_priority/rstation_48_v2.md) · [Fixed-Laurent qualification](adversarial_reviews/director_rstation48_main_theorem_round6.md)

## Exact lower bound and provenance

For nonprincipal $\chi$ the complementary function used in de Roton's Theorem 2 is $\psi(x)=-\sum_{n\le1/x}\chi(n)$. It is bounded by $q$ because the sum over a period vanishes, and it is supported in $0<x\le1$. Its Mellin transform is $-L_\chi(s)/s$, first by termwise integration for $\Re s>1$ and then by holomorphy for $\Re s>0$. The dilation $\psi(x/\alpha)$ contributes a factor $\alpha^s$, and the target indicator has Mellin transform $1/s$. Thus Mellin–Plancherel sends the distance from the indicator to the span of $\psi(nx)$, $1\le n\le N$, to $d_{N,\chi}$ with precisely the norm above. De Roton's continuous space with scales $\alpha\in[1/N,1]$ contains these generators, so its distance $D(1/N)\le d_{N,\chi}$. Primitive Dirichlet $L_\chi$ belongs to the Selberg class and $\psi\in L^2(0,\infty)$, as required. Theorem 2, printed p. 420, yields the lower bound for $D(\lambda)\sqrt{\log(1/\lambda)}$; squaring yields the exact matching liminf at $\lambda=1/N$. Under GRH there is no ambiguity between the source's strip terminology and its discussion of critical zeros. [De Roton, Bull. Soc. Math. France 134 (2006), Thm. 2](https://smf.emath.fr/system/files/2017-08/smf_bull_134_417-445.pdf)

Dimitrov and Oliveira formulate the exact integer norm and establish zero-free/density criteria but cite de Roton for the lower bound. The upper construction here is a fixed-character transplant of RST048, with the signed and fixed-edge inputs proved above. A bounded search for the same upper statement found the available zeta-source result and general Dirichlet density/lower-bound literature. Publication priority for a fixed-character upper theorem remains unadjudicated. The construction assumes GRH for the fixed character and has constants depending on it. It gives the limit for the optimized distance over arbitrary coefficients, rather than an asymptotic for the reciprocal taper $V_N$ alone. [Dimitrov–Oliveira, Theorem 2](../sources/ratio62_rstation48/dimitrov_oliveira.txt) · [RST048 v2](https://rstation.ai/problems/riemann_hypothesis/papers/48/v2)
