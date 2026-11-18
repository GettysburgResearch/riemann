# A certified finite-cutoff lower bound for the Dirichlet beta function

Let $F(s)=L(s,\chi_4)$ and let $d_N^2$ be the optimized ordinary Dirichlet-polynomial distance with boundary measure $dt/[2\pi(1/4+t^2)]$. At four integer cutoffs the following unconditional lower bounds use a certified pair of critical-line zeros. Each table entry is rounded down from an interval-enclosed projection onto two exact orthogonal-complement vectors.

| $N$ | Lower bound for $d_N^2$ |
|---:|---:|
| 10 | 0.01463 |
| 100 | 0.00903 |
| 1,000 | 0.00665 |
| 1,000,000 | 0.00362 |

The construction adapts the phase vectors of de Roton, §§4–7. For this character the kernel is elementary, and unitarity allows cancellation of the infinite Gram integral before evaluation. The certificate does not assume global GRH, simplicity of either zero, or a uniform estimate for increasing numbers of jets. [De Roton’s primary paper](../sources/prefix_formula62_generalL/deroton_lower.pdf) · [Reproduction script](../scripts/chi4_phase_certificate_skeptic62.py)

## Elementary phase kernel and a derivative-bound witness

Write $\chi_0(x)=\mathbf1_{(0,1]}(x)$, $a=\pi/2$, and $Q=\sqrt{4/\pi}$. As $F$ has no pole at 1, de Roton's phase $V_F$ equals $U_F$, whose symbol is
$$
U(s)=\left(\frac{4}{\pi}\right)^{s-1/2}
 \frac{\Gamma((s+1)/2)}{\Gamma((2-s)/2)}
 \frac{s}{1-s}.
$$
The root number is 1. Duplication and reflection yield $U(s)/s=(2/\pi)^s\Gamma(s)\sin(\pi s/2)/(1-s)$. The sine Mellin identity on $0<\Re s<1$ and integration by parts for the next kernel give
$$
\varphi(x)=(U\chi_0)(x)=\frac{1-\cos(ax)}{a x}.
$$
For example, the Mellin integral of $\varphi$ is absolutely convergent for $0<\Re s<1$. Integrating by parts reduces it to $1/(1-s)$ times the standard conditionally convergent sine Mellin integral, which is valid in this strip. Hence Mellin–Plancherel identifies this explicit $\varphi$ with $U\chi_0$.

This calculation also checks a source estimate. The derivative $\Phi(x)=x\varphi'(x)=\sin(ax)-\varphi(x)$ does not satisfy the degree-one $O(x^{-1})$ bound asserted for $\Phi$ in Proposition 5.1(12). In particular its values at $x=1+4j$ tend to 1. Its squared integral diverges because $\varphi\in L^2$ while $\sin(ax)\notin L^2$. The corresponding source bound on $\varphi$ itself holds in this example. The certificate uses the following representation, which only requires that bound on $\varphi$. [Printed pp. 431–433, Proposition 5.1](../sources/prefix_formula62_generalL/deroton_lower.pdf)

## Exact orthogonality without a global derivative estimate

Take $\psi_w(x)=\chi_0(x)x^{-w}$. For $0<\Re w<1/2$ one has the Bochner identity in $L^2(dx)$
$$
\psi_w(x)=\chi_0(x)+w\int_0^1 v^{-w-1}\chi_0(x/v)\,dv.
$$
The identity follows by direct scalar integration. The norm of $\chi_0(x/v)$ is $\sqrt v$, so the Bochner integral converges. The unitary phase commutes with all dilations. Hence
$$
g_w(x)=U\psi_w(x)=\varphi(x)+w\int_1^\infty u^{w-1}\varphi(xu)\,du.
$$
This continues pointwise and locally holomorphically to $0<\Re w<1$. On any compact subset there the explicit inequality $|\varphi(xu)|\le2/(a x u)$ controls the tail and all fixed $w$-derivatives. Consequently their cutoff versions on $x>\lambda$ converge in $L^2$ as $w$ tends to a fixed critical-line point. Derivatives of the identity give $g_{\rho,k}=\partial_w^k g_w|_{w=\rho}$. An analogous argument using $\varphi=O(x^{-\kappa})$ and the original strip is available for the general phase, without needing a global bound on $x\varphi'$.

For the dilation generator $f_\alpha$ of the bounded complementary function $-\sum_{n\le1/x}\chi_4(n)$, $Uf_\alpha$ is the corresponding dilation of its antiunitary reciprocal reflection. It is supported on $x\ge\alpha$. This follows directly from $U$ being its Mellin phase and the complementary function being supported on $x\le1$. If $\alpha\ge\lambda$, then
$$
\langle Uf_\alpha,\mathbf1_{x>\lambda}\partial_w^k g_w\rangle
=\langle f_\alpha,\partial_w^k\psi_w\rangle .
$$
The right side is the signed $k$-th Mellin derivative at $1-\bar w$, and its boundary limit vanishes at a zero $\rho$ for $k<m_\rho$. Here the Mellin transform of $f_\alpha$ is a dilation factor times $-F(s)/s$. Thus $Y_{\rho,k}=U^{-1}\mathbf1_{x>\lambda}g_{\rho,k}$ annihilates the entire allowed dilation span exactly. In particular it annihilates the ordinary integer span for $\lambda=1/N$. For target vector $b_i=\langle\chi_0,Y_i\rangle$ as a row and Gram $G_{ij}=\langle Y_i,Y_j\rangle$, the projection gives $d_N^2\ge bG^{-1}b^*$ whenever the finite positive Gram is invertible. [De Roton, Definition 10 and Proposition 6.2](../sources/prefix_formula62_generalL/deroton_lower.pdf)

## Exact Gram from cancellation on the small interval

Put $p_j=2j-1$ and $d_j=(-1)^{j+1}a^{2j-1}/(2j)!$. Mellin splitting of the formula for $g_w$ gives on $0<x\le1$
$$
g_w(x)=U(w)x^{-w}+R_w(x),\qquad
R_w(x)=\sum_{j\ge1}\frac{p_j d_j}{w+p_j} x^{p_j}.
$$
The series is absolutely convergent, locally uniformly in $w$, and $\varphi(x)=\sum_j d_jx^{p_j}$. For $w,z$ initially to the left of the critical line, unitarity gives the uncut Gram $\langle g_w,g_z\rangle=1/(1-w-\bar z)$. Introduce $v=\bar z$ as a separate complex variable and $U^\#(v)=\overline{U(\bar v)}$. After removing the integral over $(0,\lambda)$, the only apparently singular term in the resulting cutoff Gram is
$$
\frac{1-U(w)U^\#(v)\lambda^{1-w-v}}{1-w-v}.
$$
It is actually analytic across $w+v=1$, because $U(w)U^\#(1-w)=1$. This identity follows from the phase symbol, or by multiplying the two gamma quotients. A Taylor expansion in $1-w-v$ gives the exact same-ordinate term $\log(1/\lambda)+U'(w)/U(w)$. The other terms are just integrals of $U(w)x^{-w}\overline{R_z(x)}$, the swapped cross term, and $R_w(x)\overline{R_z(x)}$ on $(0,\lambda)$. They are convergent termwise sums of powers of $x$. The same argument gives the target pairing
$$
b_w=\frac1{1-\bar w}-\int_0^\lambda\varphi(x)\overline{g_w(x)}\,dx.
$$
Boundary existence already established above identifies these analytic expressions with the Gram and target of the actual vectors. Applying $\partial_w^k\partial_v^\ell$ gives each fixed finite higher-jet Gram entry. Dividing out the removable factor should precede any interval evaluation near the diagonal.

For the real character the two conjugate zeros $\rho,\bar\rho$ have $g_{\bar\rho}=\overline{g_\rho}$. The Gram is $G=\begin{pmatrix}g&h\\\bar h&g\end{pmatrix}$, and the target row is $(b,\bar b)$. The code computes $h$ using the formula above at $w=v=\rho$, where $1-2\rho\ne0$, and evaluates the exact projection
$$
\frac{2(g|b|^2-\Re(hb^2))}{g^2-|h|^2}.
$$

## Certified arithmetic and an interior Hardy obstruction

The computation uses Arb complex and real balls with 192-bit precision. The Hurwitz formula $F(s)=4^{-s}[\zeta(s,1/4)-\zeta(s,3/4)]$ evaluates $Q^{s+1}\Gamma((s+1)/2)F(s)$ at exact rational heights $6.02094890469$ and $6.02094890471$. The completed function is real on the line. The signed interval enclosures are approximately $+3.47542\cdot10^{-13}$ and $-5.67445\cdot10^{-13}$, so some zero lies in the interval by continuity. The arithmetic uses the whole ordinate bracket and uses only $k=0$. The exact location and multiplicity are unnecessary.

For series cutoff $M$, the omitted absolute coefficients sum to at most $D_M x^{2M+1}$, where
$$
D_M=\frac{a^{2M+1}}{(2M+2)!}
 \left(1-\frac{a^2}{(2M+3)(2M+4)}\right)^{-1}.
$$
This applies to both series because $p_j/|\rho+p_j|\le1$. Each full or truncated series is bounded by $Bx$, $B=(\cosh a-1)/a$, on $[0,1]$. Multiplication by the leading power contributes an integrated error at most $D_M\lambda^{2M+3/2}/(2M+3/2)$ per term, while a quadratic product contributes at most $2BD_M\lambda^{2M+3}/(2M+3)$. The script encloses every projection entry with those analytic error radii. It checks strict positive definiteness and yields approximate two-jet projection values $0.0146318470$, $0.00903583232$, $0.00665531896$, and $0.00362027999$ at the four cutoffs. All table bounds above are strictly below the certified lower endpoints. [Interval arithmetic implementation](../scripts/chi4_phase_certificate_skeptic62.py)

A bare Hardy reproducing kernel at an interior point $w=\rho+\eta$ would fail the exact orthogonality test. For instance its evaluation on a single nonzero generator is a nonzero multiple of $F(w)$ whenever $F(w)\ne0$. Its squared norm is $1/(2\eta)$, and the residual contains the term $F(w)A(w)/w$. Boundary zero multiplicity alone supplies no uniform estimate on this term over admissible polynomials at $\eta\asymp1/\log N$. The cutoff-dependent phase projection supplies exact annihilation and the correct finite Gram. This obstruction leaves open methods that pay for an additional coefficient or interpolation estimate.
