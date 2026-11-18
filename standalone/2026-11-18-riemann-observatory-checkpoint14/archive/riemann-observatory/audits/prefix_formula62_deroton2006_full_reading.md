# Whole-work reading of de Roton's generalized lower bound

Anne de Roton, *Une approche hilbertienne de l'hypothèse de Riemann généralisée*, BSMF 134(3) (2006), 417–445, DOI 10.24033/bsmf.2516. I read all 29 published pages, including the Stirling and Bessel preparations, the invariant-operator proof, the phase and jet construction, the closing Gram argument, and the bibliography. The proof below reconstructs the decisive chain. It does not audit every cited antecedent or every constant in the auxiliary contour estimates. [Published source](../sources/prefix_formula62_generalL/deroton_lower.pdf)

## Subsequent source challenge

The source's joint decay assertion (12) for $\varphi$ and $\Phi=x\varphi'$ is false for its own admissible zeta specialization. The whole-work audit originally reproduced that printed assertion. The $\varphi$ bound survives and suffices for the subsequent zero-jet argument through the layer representation below. The director independently verified this source failure and adjudicated a complete two-line Mellin replacement for the lower theorem. [Phase adjudication](adversarial_reviews/director_deroton_phase_round6.md) · [Hardy adjudication](adversarial_reviews/director_deroton_hardy_round6.md) [Status and repair](prefix_formula62_deroton2006_phi_status.md)

## Scope and the split at off-line zeros

For a nonzero Selberg-class function $F$, write $\Psi_F(u)=\operatorname{Res}_{s=1}(F(s)u^s/s)-\sum_{n\le u}a_F(n)$ and assume $\Psi_F(1/x)\in L^2(dx)$. The distance $D_F(\lambda)$ is from $\chi=\mathbf1_{(0,1)}$ to the finite complex span of $\Psi_F(\alpha/x)$ with $\lambda\le\alpha\le1$. There is no discrete restriction in the source theorem. There is no GRH, simplicity, separation, or reciprocal-derivative hypothesis in the lower bound.

Theorem 2 on p.420 says *bande critique*, while its following explanation and the proof use the critical-line zeros. Section 6.1, p.434, resolves the apparent discrepancy. If any zero lies to the right of the critical line, Theorem 1 gives $\lim_{\lambda\downarrow0}D_F(\lambda)>0$, since the distance is monotone as the span grows and the equivalent zero-limit criterion fails. The logarithmically normalized distance then diverges. In the other case, the functional equation reflects any interior left-hand zero to the right, so all interior strip zeros are on the line. The finite-block construction concerns the nontrivial lower-rate case. A degree-zero constant has no line zeros and its lower bound is vacuous. [Theorems 1–2 and §6.1](../sources/prefix_formula62_generalL/deroton_lower.pdf)

## Sections 2–3. Gamma quotient and the contour model

Use $\bar G(s)=\overline{G(\bar s)}$. The completion and its functional equation are
$$
\Lambda(s)=Q^s\Delta(s)F(s),\quad
\Lambda(s)=\omega\bar\Lambda(1-s),\qquad
\Delta(s)=\prod_{j=1}^r\Gamma(\lambda_j s+\mu_j),
$$
where $\lambda_j>0$, $\Re\mu_j\ge0$, $Q>0$, and $|\omega|=1$. The phase symbol in (2), p.421, is
$$
U_F(s)=\bar\omega Q^{2s-1}\frac{\Delta(s)}{\bar\Delta(1-s)}\frac{s}{1-s}.
$$
The denominator uses the conjugated shifts $\bar\mu_j$. The bars are visible in the PDF and can disappear in text extraction. On $\Re s=1/2$ this symbol has modulus one.

Write $d=2\sum_j\lambda_j$, $\mu=\sum_j(\mu_j-1/2)$, and for $k=0,1$ set
$$
\nu_k=2\Re\mu+d/2+k,\qquad
\beta_k=2k-1+2\mu,\qquad
a=d\Bigl(Q^{-2}\prod_j\lambda_j^{-2\lambda_j}\Bigr)^{1/d}.
$$
The Bessel comparison symbol is
$$
f_{a,\nu}(z)=\tfrac12 (2/a)^{z-\nu}\frac{\Gamma(z/2)}{\Gamma(1+\nu-z/2)}.
$$
The matching terms of the logarithmic expansions of $U_F(s)/s^{2-k}$ and $f_{a,\nu_k}(ds+\beta_k)$ are
$$
\tfrac d2s\{\log s+\log(-s)\}
+\bigl(2\log Q+2\sum_j\lambda_j\log\lambda_j-d\bigr)s
+(\mu+k-1)\log s-(\bar\mu+d/2+1)\log(-s).
$$
The first-order difference is a constant plus a term proportional to $s^{-1}$ with $O(s^{-2})$ remainder. Exponentiation gives Proposition 2.2, uniformly away from the two real rays. Proposition 2.3 gives $|U_F(\sigma+i\tau)|\asymp|\tau|^{d(\sigma-1/2)}$ on fixed real strips. The conjugation ensures that the gamma exponential factors cancel in this quotient.

In §3 the contour runs up a left vertical line with a finite detour to the right of the poles. Lemma 1 permits contour changes when the outer vertical tails are absolutely integrable. As $x\to\infty$, move the tail abscissa close to the integrability threshold from below while keeping the finite detour farther right. For the Bessel symbol the numerator has poles at $z=-2n$, subject to cancellation by the reciprocal denominator. Moving the center of the contour left and taking residues gives the series of $x^{-\nu}J_\nu(ax)$. Proposition 2.4 and Lemmas 2–3 show that the integral on $\Re z=-2N+1$ tends to zero locally uniformly in $x>0$. Proposition 3.1 is stated for real $\nu$. Lemma 3 initially writes $\nu\ge0$, but its displayed argument uses $N\ge 2|\nu|+1$ and works for each fixed real $\nu$. This extension is relevant even to $\zeta$, for which $\nu_0=-1/2$. [§§2–3, pp.421–427](../sources/prefix_formula62_generalL/deroton_lower.pdf)

## Sections 4–5. Bounded multiplier and kernel decay

The unitary dilations are $D_\alpha f(x)=\alpha^{-1/2}f(x/\alpha)$ and the antiunitary involution is $Jf(x)=x^{-1}\overline{f(1/x)}$. Mellin Plancherel uses $d\tau/(2\pi)$ on $\Re s=1/2$. For an $L^2$ vector $A$ with a.e. nonzero Mellin transform the phase symbol is $\overline{\mathcal MA(s)}/\mathcal MA(s)$ on that line. Its unitary multiplier sends $A$ to $JA$ and commutes with all dilations.

The identity $\mathcal M[\Psi_F(1/x)](s)=-F(s)/s$ for $1/2<\Re s<1$ and the functional equation identify this phase with $U_F$. Put $\varphi=U_F\chi$ and $\Phi(x)=x\varphi'(x)$. In §5 the inverse Mellin contours for $U_F(s)/s$ and $-U_F(s)$ pass to the right of gamma poles and to the left of the possible pole at 1 over the finite middle segment for the small-$x$ estimates. Thus both $\varphi(x)$ and $\Phi(x)$ are $O_\epsilon(x^{-\epsilon})$ as $x\downarrow0$. The large-$x$ contour crosses at most the pole at one, contributing $O(x^{-1})$. The remainders after the two Bessel terms have vertical growth $O(|\tau|^{d(\sigma-1/2)+k-3})$ and hence inverse transforms $O_\epsilon(x^{-1/2-(2-k)/d+\epsilon})$.

In the model term, $z=ds+\beta_k$ transforms the inverse Mellin kernel to
$$
\frac1d x^{(\beta_k-\nu_k)/d}J_{\nu_k}(ax^{1/d})
=\frac1d x^{-1/2+(k-1)/d+2i\Im\mu/d}J_{\nu_k}(ax^{1/d}).
$$
The other model term is obtained by applying $-x\,d/dx$. In this derivative the Bessel argument contributes a factor $x^{1/d}$. Thus the derivative term has order $x^{-1/2+(k-1/2)/d}$, using the real-argument bound $J_\nu'=O(x^{-1/2})$ in its own argument. For $k=0$ this verifies the source's bound $\varphi(x)=O(x^{-1/2-1/(2d)})$. For $k=1$ it does not give the printed bound for $\Phi$, and in zeta the latter bound fails. The source invoked §4 Proposition 4.1 to obtain its (18) from $\Phi\in L^2$. A layer representation instead uses only $\varphi$: for $\Re w<1/2$, the identity
$$
\chi(x)x^{-w}=\chi(x)+w\int_0^1v^{-w-1}{\bf1}_{(0,v)}(x)\,dv
$$
holds in $L^2$ by Bochner integration, since the indicator has norm $\sqrt v$. Applying the unitary $U_F$ sends the indicator to $\varphi(x/v)$. This yields the kernel formula actually needed for the jets, without $\Phi\in L^2$. [§§4–5, pp.427–433](../sources/prefix_formula62_generalL/deroton_lower.pdf) · [Subsequent challenge](prefix_formula62_deroton2006_phi_status.md)

## Section 6. Projection that preserves each zero jet

Write $m=m_F$ for the pole order at 1. The unitary multiplier $P(s)=(s-1)/s$ removes the pole from the Mellin transform by setting $A_F=P^m\Psi_F(1/x)$ and $\chi_m=P^m\chi$. Proposition 6.1 places $A_F$ in $L^2(0,1)$ by Hardy Paley–Wiener and gives $\mathcal M A_F(s)=P(s)^m[-F(s)/s]$. The support also follows directly without a Hardy membership inference. On the critical line the multiplier $1/s$ acts as $(H^*f)(x)=\int_x^\infty f(v)\,dv/v$, so $P=1-H^*$. For $x>1$ the complementary function consists only of the pole term $x^{-1}p(\log x)$, with $\deg p\le m-1$. The operator $H^*$ replaces $p$ by $p+p'+\cdots+p^{(m-1)}$ there by direct integration. Thus $P$ reduces the tail degree by at least one, and $P^m$ kills it. This is an independent check of the support premise used by the cutoff projection. The phase of $A_F$ is
$$
V_F(s)=\left(\frac{s}{1-s}\right)^{2m}U_F(s)
=(1-H)^{2m}U_F(s),\qquad H(s)=\frac1{1-s}.
$$
Here $P^{-1}=1-H$. The opposite sign in the sentence near Definition 7 is inconsistent with these symbols, but §7, p.443, uses the correct identity.

For $\Re w<1/2$, let $\psi_{w,k}(x)=\chi(x)x^{-w}(\log(1/x))^k$. Let $Q_\lambda$ be multiplication by $\mathbf1_{(\lambda,\infty)}$. The candidate is
$$
Y_{s,k}^{\lambda,F}=\lim_{w\to s,\ \Re w<1/2}V_F^{-1}Q_\lambda V_F\psi_{w,k},
\qquad \Re s=1/2 .
$$
The key exact inclusion is $V_F D_\alpha A_F=D_\alpha JA_F$, supported on $(\alpha,\infty)$. Since $\alpha\ge\lambda$, its inner product with $Q_\lambda V_F\psi_{w,k}$ is unchanged on removing $Q_\lambda$. Unitarity and invariance identify it with the original Mellin jet of $D_\alpha A_F$ at $1-\bar w$. With inner product linear in the first variable, the corresponding jet is $(-1)^k(\mathcal M f)^{(k)}(1-\bar w)$. At $w=s$ the limiting point is $s$. Thus $Y_{\rho,k}^{\lambda,F}$ is orthogonal to the whole truncated span for every line zero $\rho$ and $k<m_\rho$, once the limit exists. This is the exact use of the lower cutoff.

By the layer representation above, on compact subsets of $0<\Re w<\kappa=1/2+1/(2d)$ the pointwise continuation of $U_F\psi_{w,k}$ is
$$
\partial_w^k\left[\varphi(x)+w\int_0^1 v^{-w-1}\varphi(x/v)\,dv\right].
$$
Substitute $y=x/v$ and write the integral over $[x,\infty)$ as the full Mellin transform minus its $[0,x]$ part. The full transform is $\mathcal M\varphi(w)=U_F(w)/w$ on the continuation strip by the near-zero and tail bounds. The removed integral and its derivatives after the $x^{-w}$ prefactor are $O_\epsilon(x^{-\epsilon})$ for sufficiently small $\epsilon>0$ relative to the compact set, by substituting $y=xv$. The continued jet is therefore $\partial_w^k[U_F(w)x^{-w}]+O_\epsilon(x^{-\epsilon})$ near zero and is $O(x^{-\kappa})$ for $x\ge1$. This recovers the estimates for the subsequent jet limit using $\varphi$ alone.

Applying $H^j$ to the leading term gives
$$
\partial_w^k\left[(1-w)^{-j}U_F(w)x^{-w}\right],
$$
since $H(x^{-w})=x^{-w}/(1-w)$ and differentiation commutes with the locally dominated integral. The placement of the derivative matters. Taken literally, the displayed expression in Proposition 6.4 puts $(1-w)^{-j}$ outside the derivative and misses lower-order log terms. For example $H[x^{-w}\log(1/x)]=x^{-w}\{\log(1/x)/(1-w)+(1-w)^{-2}\}$. Moving the factor inside the derivative repairs the calculation and gives the full symbol $V_F$ in Proposition 6.5. For $d=1$ the tail may gain at most $(1+\log x)^j$ by Hardy iteration, while for $d>1$ it stays $O(x^{-\kappa})$. The bounds needed are local on compact neighborhoods of each fixed $s$, so no uniformity at the edges of the continuation strip is necessary. Dominated convergence on $(\lambda,\infty)$ now gives the required strong $L^2$ limit and the local form
$$
V_FY_{s,k}^{\lambda,F}(x)
=\mathbf1_{x>\lambda}\left(\partial_s^k[V_F(s)x^{-s}]+O_\epsilon(x^{-\epsilon})\right)
\quad (0<x\le1),
$$
with the corresponding square-integrable tail bound for $x>1$. [§6, pp.434–441](../sources/prefix_formula62_generalL/deroton_lower.pdf)

## Section 7. Asymptotic Gram blocks and the strongest reusable finite-set estimate

Let $L=\log(1/\lambda)$ and $X_{\rho,k}=L^{-k-1/2}Y_{\rho,k}$. On $(\lambda,1)$, the leading monomial of the jet is $V_F(\rho)x^{-\rho}(\log(1/x))^k$. Terms in which a derivative hits $V_F$ have lower log degree. The remainders are integrable in every cross product against these leading monomials for $\epsilon<1/2$, and the tails on $(1,\infty)$ have uniformly bounded inner products for each fixed set of labels. Changing variables $v=\log(1/x)$ therefore leaves the moment
$$
L^{-1-k-\ell}\!\int_0^L v^{k+\ell}e^{iv(\Im\rho_1-\Im\rho_2)}\,dv.
$$
At the same zero its value is $1/(k+\ell+1)$. For distinct zeros fixed before $L\to\infty$, integration by parts bounds it by $O(L^{-1})$, with constants depending on their ordinates. At the same zero the phase has modulus one, so the limiting block is the Hilbert matrix of size $m_\rho$. Positivity of this Gram matrix gives invertibility for sufficiently large $L$ for any fixed finite union of blocks.

For the target, $V_F\chi_m=(1-H)^mU_F\chi$. Its near-zero and tail bounds permit passage to the boundary in $\langle V_F\chi_m,Q_\lambda V_F\psi_{w,k}\rangle$. In fact, for $\Re w<1/2$ the untruncated inner product is exactly $\langle\chi_m,\psi_{w,k}\rangle$ by unitarity. Dominated convergence at fixed $k,\rho$ identifies the limiting boundary pairing. The omitted integral over $(0,\lambda)$ is $O_{\rho,k,\epsilon}(\lambda^{1/2-\epsilon}(1+L)^k)$ after taking the boundary. Thus
$$
\sqrt L\,\langle\chi_m,X_{\rho,0}\rangle\ \longrightarrow\ P(\rho)^m/\rho,\qquad
\sqrt L\,\langle\chi_m,X_{\rho,k}\rangle=O_{\rho,k}(L^{-k})\quad(k\ge1).
$$
The size-$m_\rho$ Hilbert matrix is the Gram matrix of monomials on $[0,1]$. The $(0,0)$ entry of its inverse is the reproducing kernel at $(0,0)$, or $\sum_{j=0}^{m_\rho-1}(2j+1)=m_\rho^2$ in a shifted orthonormal Legendre basis. The pole-removal factor does not affect the coefficient because $|P(\rho)|=1$.

**Reusable finite-set estimate.** Fix a finite set $R$ of distinct critical-line zeros, and keep all jets through order $m_\rho-1$ of each chosen zero. Under the preceding complementary-function and phase hypotheses,
$$
D_F(\lambda)^2\ \ge\ \frac1L\sum_{\rho\in R}\frac{m_\rho^2}{|\rho|^2}
-O_{F,R}(L^{-2}).
$$
Indeed the Gram matrix differs from the positive definite block limit by $O_{F,R}(L^{-1})$, and the scaled target vector differs from its limiting vector by $O_{F,R}(L^{-1})$. Projecting onto their exact orthogonal span gives the inequality. The error estimate is a finite-set refinement from the preceding fixed-zero bounds. It is not uniform for a growing set or merging ordinates. Taking the limit first and increasing the finite set afterwards yields Theorem 2. The conclusion line on p.444 elides the $\sqrt L$ normalization in the prose. Equations (19) and the two limits state the normalization needed for the squared distance. [§7, pp.441–445](../sources/prefix_formula62_generalL/deroton_lower.pdf)

## Burnol comparison and the upper degree threshold

Burnol's original zeta result already proves the same multiplicity-squared lower constant in $L^2(dx)$ for a **continuous** lower dilation cutoff. It also builds the invariant phase, pole-removal map, $Q_\lambda$-projected boundary jets and Hilbert Gram blocks. Its §2 provides a distinct finite prediction-error analogue with unit-circle polynomial zeros. De Roton's analytic addition is the gamma quotient with general complex shifts, the Bessel contour reduction, and the decay of the resulting phase kernel. The discrete Dirichlet-character lower bound follows by restriction of her span. Neither source gives the optimal upper in that discrete norm. [Burnol, arXiv v2, Theorem 1.3 and §§3–5](../sources/equivalences/burnol.pdf)

Precisely where is $d<4$ used? It is not a hypothesis in Theorem 2 or a cutoff in the gamma-phase method. Remark 1, p.419, invokes reference [10] only to supply its separate unsmoothed integrability premise. The actual final bibliography reverses the venues for references [9] and [10]. The mean-square work is Acta Arithmetica 126 (2007), 27–55. Its $S^{\#\flat}$ axiom is $\sum_{n\le x}|a_n|^2=O_\epsilon(x^{1+\epsilon})$, weaker than the Ramanujan axiom. If $E(u)=\sum_{n\le u}'a_n-F(0)-\operatorname{Res}_{s=1}(F(s)u^s/s)$, then $\Psi_F(u)=-E(u)-F(0)$ almost everywhere. Its Theorem 2.2 gives an exponent strictly below two for $0<d<4$ after choosing $\epsilon$ small, so dyadic summation against $du/u^2$ proves the missing tail integrability. At $d=4$ its bound is $O_\epsilon(x^{2+\epsilon})$ and this dyadic deduction stops. If the unsmoothed integrability is available by another estimate for a higher-degree $F$, the phase argument still applies. For fixed nonprincipal Dirichlet $\chi$ bounded partial sums furnish the premise directly. [BSMF Remark 1 and bibliography](../sources/prefix_formula62_generalL/deroton_lower.pdf) · [Acta Arithmetica Theorem 2.2 and p.53](../sources/prefix_formula62_generalL/deroton_meansquare.pdf)
