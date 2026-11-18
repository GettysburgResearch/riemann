# A phase-jet repair for de Roton’s lower bound

This checks a defect in Proposition 5.1 of Anne de Roton’s *Une approche hilbertienne de l’hypothèse de Riemann généralisée*, BSMF 134 (2006), and gives a replacement for the phase-jet step under the fixed Selberg-class GRH hypotheses used in the transfer campaign. It concerns the lower bound only. The retained-edge upper construction does not use this phase argument. [Original PDF, pp. 429–444](https://www.numdam.org/item/10.24033/bsmf.2516.pdf) · [Selberg transfer](effective_cluster62_selberg_transfer.md)

## 1. The printed derivative bound fails for the primitive character modulo 4

Proposition 5.1 (12), printed p. 432, gives the decay $O(x^{-(1+1/d)/2})$ at infinity for both $\varphi=U_F1_{(0,1)}$ and $\Phi=x\varphi'$. The conclusion that $\Phi\in L^2$ is used on p. 433 to invoke Proposition 4.1.

For the primitive odd real character of conductor 4, write $F=L(s,\chi_4)$. Here $d=1$, the root number is 1, and the gamma term is $(4/\pi)^{s/2}\Gamma((s+1)/2)$ up to a constant. The unitary phase symbol is $U_F(s)=\bar F(1-s)s/[F(s)(1-s)]$. The duplication and reflection formulas give
$$
 \frac{U_F(s)}s
 =\frac{(4/\pi)^{s-1/2}\Gamma((s+1)/2)}
        {(1-s)\Gamma(1-s/2)}
 =\left(\frac2\pi\right)^s\frac{\Gamma(s)\sin(\pi s/2)}{1-s}.
$$
Here $\bar F(z)=\overline{F(\bar z)}$. The last expression is the Mellin transform of $\varphi(x)=(1-\cos(\pi x/2))/(\pi x/2)$ on $0<\Re s<1$. To check this, substitute $y=\pi x/2$, integrate by parts, and use $\int_0^\infty y^{s-1}\sin y\,dy=\Gamma(s)\sin(\pi s/2)$ on that strip. Plancherel therefore identifies precisely the source phase image. Differentiation gives $\Phi(x)=\sin(\pi x/2)-\varphi(x)$. It neither decays as $O(x^{-1})$ nor belongs to $L^2$. The elementary $\varphi$ bound itself holds for this character. This disproves the second estimate of (12), and the stated route through Proposition 4.1 needs repair.

There is also a general obstruction. For any unitary Mellin multiplier $U$, put $\varphi=U\chi_0$ and identify its dilation derivative in distributions on $(0,\infty)$. Under the logarithmic-coordinate isometry $g(u)=e^{u/2}\varphi(e^u)$, the derivative $x\varphi'(x)$ corresponds to $g'(u)-g(u)/2$. Its Mellin multiplier is $-s$ on the critical line, since the Mellin Fourier phase is $e^{itu}$. Thus
$$
 \mathcal M(x\varphi')(s)=-s\,\frac{U(s)}s=-U(s).
$$
The right side has modulus one almost everywhere and has infinite squared integral in $dt$. Hence this derivative is never an $L^2(dx)$ function for a unitary multiplier. This reflects the jump of $\chi_0$. The explicit conductor-4 example also disproves the pointwise decay claimed in print.

## 2. Mellin and dilation conventions

Use $\mathcal Mf(s)=\int_0^\infty f(x)x^{s-1}dx$ and the $L^2$ line measure $dt/(2\pi)$ at $s=1/2+it$. Write $\chi_0=1_{(0,1)}$, $P(s)=(s-1)/s$, and let $p$ be the actual pole order of $F$ at 1. Let $\psi$ be the pole-subtracted complementary function, so $\mathcal M\psi=-F/s$ in $L^2$, as justified by the tested shift in the Selberg campaign. The unitary multiplier $P^p$ sends $\psi$ to $A$ and $\chi_0$ to $T_0$. The transform $\mathcal MA=-P^pF/s$ is holomorphic on $\Re s>1/2$ and lies in its Hardy space. Under fixed Selberg GRH this follows from the uniform critical and right-strip subpower growth of the pole-canceled function and ordinary absolute convergence farther right. Paley–Wiener gives $A$ supported on $(0,1)$.

Let $Jf(x)=x^{-1}\overline{f(1/x)}$. Its Mellin transform on the critical line is $\overline{\mathcal Mf(s)}$. The phase $V$ of $A$ therefore has symbol $V(s)=P(s)^{-2p}U_F(s)$, using $\overline{P(s)}=P(s)^{-1}$ on the line. It is unitary, commutes with dilations, and $VA=JA$ is supported on $[1,\infty)$. The conjugate functional equation expresses $U_F(s)$ as $s/(1-s)$ times
$$
 \bar\omega Q^{2s-1}\prod_j
 \frac{\Gamma(\lambda_js+\mu_j)}
      {\Gamma(\lambda_j(1-s)+\bar\mu_j)} .
$$
Here the choice of $\omega$ corresponds to the relation $\Lambda(s)=\omega\overline{\Lambda(1-\bar s)}$. Both $U_F$ and $V$ are holomorphic and nonvanishing on $0<\Re s<1$. Stirling gives $|U_F(\sigma+it)|+|V(\sigma+it)|=O(T^{d(\sigma-1/2)})$ on closed substrips. The moduli on the critical line are 1, including at line zeros by analytic continuation of the gamma formula.

For $\Re w<1/2$, define $\psi_w(x)=x^{-w}\chi_0(x)$. There is an exact Bochner identity in $L^2(dx)$:
$$
 \psi_w=\chi_0+w\int_0^1 v^{-w-1}\chi_0(\,\cdot\,/v)\,dv .
$$
Indeed $\|\chi_0(\cdot/v)\|_2=\sqrt v$, so the integral converges in norm, and evaluating at $0<x<1$ integrates over $v\ge x$. Boundedness and dilation commutation thus give $U_F\psi_w=\varphi+w\int_0^1 v^{-w-1}\varphi(\cdot/v)dv$, and the same formula for $V$ and $V\chi_0$. This is a substitute for the use of Proposition 4.1 on these vectors. For continuation beyond the initial half-plane we use weighted Mellin lines, avoiding the need for pointwise claims on $\varphi$.

## 3. Analytic cutoff jets without pointwise derivative estimates

For any real $\sigma$, write $\|f\|_\sigma^2=\int_0^\infty |f(x)|^2x^{2\sigma-1}dx$. Mellin–Plancherel on that line follows by the logarithmic coordinate. Fix $0<c<1/2<\kappa<1$ with $d(\kappa-1/2)<1/2$. Such $\kappa$ exists for every finite $d$, including $d=0$. For $c<\Re w<\kappa$ define $R_w^\nu$ as the inverse Mellin transform of $V(s)/(s-w)$ on $\Re s=\nu$ for $\nu=c,\kappa$. These are holomorphic families in their respective weighted spaces. Indeed the fixed-strip gamma estimate shows integrability of the squared multiplier, and locally uniform derivatives in $w$ add further inverse powers. Pairing first against smooth compactly supported functions in logarithmic coordinates legitimizes shifting the Mellin contour, by rapid decay of the tested transform. With the right line upward, crossing the pole at $w$ gives the exact distributional relation
$$
 R_w^\kappa=R_w^c+V(w)x^{-w}.
$$
The same test proves $R_w^\kappa=V\psi_w$ when $c<\Re w<1/2$, since the critical-line Mellin transform of $\psi_w$ is $1/(s-w)$ and there is no residue between the critical line and $\kappa$.

Let $Q_\lambda$ multiply by $1_{[\lambda,\infty)}$. For fixed $0<\lambda<1$, the piecewise formula
$$
 Z_\lambda(w)=
 1_{[\lambda,1)}\bigl(R_w^c+V(w)x^{-w}\bigr)
 +1_{[1,\infty)}R_w^\kappa
$$
defines a holomorphic $L^2(dx)$ family across the line, and agrees with $Q_\lambda V\psi_w$ on the initial side. On $(0,1)$ the $\|\cdot\|_c$ norm controls ordinary $L^2$, and on $[1,\infty)$ the $\|\cdot\|_\kappa$ norm controls it. Thus for critical $\rho$ and $k\ge0$ the jet $Z_{\lambda,\rho,k}=\partial_w^k Z_\lambda(\rho)$ equals, up to a remainder uniformly bounded in $L^2(dx)$ as $\lambda\downarrow0$,
$$
 1_{[\lambda,1)}\,
 \left.\partial_w^k\big(V(w)x^{-w}\big)\right|_{w=\rho}.
 \tag{1}
$$
This uses fixed $c,\kappa$, independent of $\lambda$, and gives all fixed higher jets.

## 4. Orthogonality, limiting Gram, and target pairings

Take the Hilbert inner product linear in the first argument. Write $\mathcal C_\lambda$ for the span of $A(x/\alpha)$ with $\lambda\le\alpha\le1$. Then $V\mathcal C_\lambda$ is supported in $[\lambda,\infty)$. For $f=\sum a_j A(x/\alpha_j)\in\mathcal C_\lambda$, on the initial side $\Re w<1/2$,
$$
 \langle f,V^{-1}Z_\lambda(w)\rangle
 =\langle f,\psi_w\rangle
 =\sum_j a_j\alpha_j^{\,1-\bar w}\,(\mathcal MA)(1-\bar w).
$$
The first equality follows by moving the self-adjoint cutoff onto $Vf$. Since $\mathcal MA$ has the same critical zeros with the same multiplicities as $F$, antiholomorphic differentiation and continuation show that $Y_{\lambda,\rho,k}=V^{-1}Z_{\lambda,\rho,k}$ is orthogonal to $\mathcal C_\lambda$ for $0\le k<m_\rho$. The conjugate of the parameter enters because the second argument of the inner product is conjugate-linear.

Put $L=\log(1/\lambda)$ and scale each $Y_{\lambda,\rho,k}$ by $L^{-k-1/2}$. Its Gram matrix on any fixed finite collection tends to blocks $(1/(i+j+1))_{0\le i,j<m_\rho}$, one per distinct zero. Indeed the top term of (1) is $V(\rho)x^{-\rho}(\log(1/x))^k$ with $|V(\rho)|=1$. Equal ordinates give $\int_0^L u^{i+j}du=L^{i+j+1}/(i+j+1)$. Distinct ordinates give $\int_0^L u^{i+j}e^{i(\gamma-\gamma')u}du=O_{\gamma-\gamma',i,j}(1+L^{i+j})$ by integration by parts. Lower powers vanish after scaling, and the $L^2$ remainder in (1) vanishes after scaling by Cauchy–Schwarz. The limiting blocks are positive definite.

For the target, $VT_0$ has symbol $V(s)P(s)^p/s$ and has finite $\|\cdot\|_c$ norm, by the same tested shift with no crossed poles. For $\Re w<1/2$ the uncut pairing is $\langle T_0,\psi_w\rangle=P(1-\bar w)^p/(1-\bar w)$, since $P(s)^p/s$ lies in the right Hardy space. The cutoff error is the pairing on $(0,\lambda)$ of $VT_0$ with $V\psi_w$, and can be continued to $w=\rho$ using $R_w^c+V(w)x^{-w}$ there. More precisely, near $\rho$ choose the parameter disk so its upper real part is less than $1-c$. Cauchy–Schwarz with the $\|\cdot\|_c$ weight handles the power term and its fixed derivatives, with bound $O(\lambda^{1-c-\Re w}(1+L)^k)$ locally uniformly. The remainder is bounded by $\|1_{(0,\lambda)}VT_0\|_2\|\partial_w^kR_w^c\|_{L^2(0,1)}=O(\lambda^{1/2-c})$. Thus for each fixed jet, the cutoff error at $\rho$ is $O(\lambda^{1/2-c}(1+L)^k)$. It follows that $\langle T_0,Y_{\lambda,\rho,0}\rangle$ tends to $P(\rho)^p/\rho$ and the fixed higher jet pairings stay bounded. After the scaling in the previous paragraph and multiplication by $\sqrt L$, only the entries with $k=0$ survive.

The projection onto the span of these orthogonal witnesses is a lower bound for the distance from $T_0$ to $\mathcal C_\lambda$. The limiting inverse Hilbert block has upper-left entry $m_\rho^2$, as is seen by summing squared evaluations at zero of the normalized shifted Legendre polynomials of degrees $0,\ldots,m_\rho-1$. Since $|P(\rho)|=1$, this proves
$$
 \liminf_{\lambda\downarrow0} L D(\lambda)^2
 \ge \sum_{\rho\in\mathcal R}\frac{m_\rho^2}{|\rho|^2}
$$
for every finite set $\mathcal R$ of critical zeros. Exhaust the finite sets and use the continuous-to-integer comparison for the boundary approximation. This recovers de Roton’s lower constant in the fixed Selberg GRH scope of the transfer, without the false derivative assertion of Proposition 5.1. The proof uses no pointwise decay claim about $x\varphi'(x)$.

## 5. Lower theorem under its original square-integrability premise

The repair extends to the published lower theorem's premise $\psi\in L^2(dx)$, without GRH. We give the support justification separately because the fixed-GRH proof above used a simpler Hardy estimate. The general Selberg axioms give polynomial growth on each fixed strip by the finite-order strip maximum principle, the functional equation and Stirling, after canceling the pole at 1. The tested shift for $F(s)/s$ in §4 of the Selberg transfer therefore works distributionally on the critical line even without a pointwise subpower bound. On the initial line $\Re s>1$, use absolute Dirichlet convergence. The shift yields the inverse transform of $-F(s)/s$ equal to $\psi$, with the pole residue already included in $\psi$. Its assumed $L^2$ membership then identifies $-F(s)/s$ on the critical line as its $L^2$ Mellin transform.

To show that $A=P^p\psi$ is supported on $(0,1)$, take a test $\varphi(u)$ with compact support in $u=\log x>0$. The inverse Mellin pairing for $A(e^u)$ contains the factor $\int\varphi(u)e^{-su}du$. Shift from the critical line to any $\Re s=R>1$ in the tested integral for $-P(s)^pF(s)/s$. This crosses no poles. If the support of $\varphi$ starts at $u_0>0$, repeated integration by parts in $u$ bounds that test factor on the right line by $C_k(1+R)^k e^{-Ru_0}(1+|\Im s|)^{-k}$ for any fixed $k$. The multiplier is bounded uniformly on these far-right lines by absolute convergence. Hence the pairing tends to zero as $R\to\infty$. It follows that $A=0$ on $(1,\infty)$. On every $\sigma>1/2$ the supported $A$ lies in weighted $L^2$ and its Mellin transform there equals $-P(s)^pF(s)/s$ by the same tested fixed-line shift. This also proves its right Hardy property. The gamma ratio for the phase, the orthogonality at critical zeros, and every bound in §§3–4 now apply verbatim. Consequently the repaired argument proves the reported lower bound for critical zeros under the original square-integrability premise.

## 6. Fixed finite lower error

For a fixed finite critical-zero set $\mathcal R$, the same construction gives
$$
 L D(\lambda)^2\ge
 \sum_{\rho\in\mathcal R}\frac{m_\rho^2}{|\rho|^2}
 -\frac{C_{\mathcal R}}L
 \qquad(L=\log(1/\lambda)\ge L_{\mathcal R}).
$$
To see the $L^{-1}$ error, use the $\|\cdot\|_c$ norm for the remainders on $(0,1)$ in each Gram entry. Its cross term with a power $(\log(1/x))^j x^{-\rho}$ is bounded uniformly in $\lambda$, since the dual integral is $\int_0^1 x^{-2c}(\log(1/x))^{2j}dx<\infty$. The remainder–remainder terms are also bounded uniformly. Distinct ordinates and lower powers of the main term cost at most $O_{\mathcal R}(L^{i+j})$ in an unnormalized $(i,j)$ entry. The normalized Gram matrix therefore differs from its fixed block limit by $O_{\mathcal R}(L^{-1})$. The normalized target vector after multiplication by $\sqrt L$ differs from its limit by $O_{\mathcal R}(L^{-1})$ as well, by the exponential cutoff bound and the factor $L^{-k}$ for $k\ge1$. The inverse matrix has the same perturbation bound once the Gram error is below half the least eigenvalue of the fixed limiting matrix. This gives the displayed inequality. The finite constants can be bounded using the two gamma-line norms, the finite zero spacings and the finite block matrices. No uniformity as $\mathcal R$ grows is used.
