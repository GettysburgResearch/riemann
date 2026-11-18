# Effective finite-height lower bound for the zeta approximation distance

Put $\lambda=1/N$, $L=\log(1/\lambda)$, and let $D_\zeta(\lambda)$ be the continuous-dilation distance in $L^2(dx)$ from $\chi=\mathbf1_{(0,1)}$ to the span of $\{\alpha/x\}$ for $\lambda\le\alpha\le1$. Mellin Plancherel gives $D_\zeta(\lambda)^2\le\Delta_N^2\le d_N^2$, where $\Delta_N$ and $d_N$ are the ordinary and anchored distances in $dt/[2\pi(1/4+t^2)]$. Fix a finite set $R$ of distinct genuine line zeros with certified multiplicities. No RH is needed for the lower bound. [Burnol §§3–5](../../sources/equivalences/burnol.pdf)

## Exact projection and finite quadrature

Let $Hf(x)=x^{-1}\int_0^x f(y)\,dy$, $P(s)=(s-1)/s$, and let $U$ denote Burnol's zeta phase. Its multiplier is $U(s)=\frac{s}{1-s}\pi^{1/2-s}\Gamma(s/2)/\Gamma((1-s)/2)$, and
$$
p(x)=U\chi(x)=\frac{\sin(2\pi x)}{\pi x},\qquad
V=(1-H)^2U,\qquad g=V(P\chi)=(1-H)p.
$$
Here $P$ also denotes the multiplier with symbol $P(s)$. For $i=(\rho,k)$ with $0\le k<m_\rho$, put $D_i(u)=\rho(\log u)^k+k(\log u)^{k-1}$, omitting the second term for $k=0$, and define
$$
f_i(x)=\delta_{k0}p(x)+\int_1^\infty D_i(u)u^{\rho-1}p(xu)\,du,
\qquad h_i=(1-H)^2 f_i .
$$
The exact formula follows by applying $U$ to the indicator-layer representation of $\chi x^{-w}$ for $\Re w<1/2$, differentiating $k$ times, and continuing the absolutely convergent integral to $\Re w=1/2$. This uses $p(x)=O(1/x)$ and does not need decay of $xp'(x)$. Burnol's projected jet is $V^{-1}(\mathbf1_{x>\lambda}h_i)$. The $V$ images of the pole-removed generators at $\alpha$ have support in $(\alpha,\infty)$, so the cutoff does not change their Mellin-jet inner products. The jets therefore annihilate the candidate space. [Burnol Theorems 4.2 and 4.11](../../sources/equivalences/burnol.pdf) · [Indicator-layer justification](../prefix_formula62_deroton2006_phi_status.md)

Use the inner product linear in the first argument and define
$$
(G_\lambda)_{ij}=\int_\lambda^\infty h_j(x)\overline{h_i(x)}\,dx,\qquad
(b_\lambda)_i=\int_\lambda^\infty g(x)\overline{h_i(x)}\,dx .
$$
For every trial column $a$, completing the square on the orthogonal span gives $D_\zeta(\lambda)^2\ge 2\Re(a^*b_\lambda)-a^*G_\lambda a$. If the matrix is positive definite, optimization gives $D_\zeta(\lambda)^2\ge b_\lambda^*G_\lambda^{-1}b_\lambda$. A certified approximate optimizer can be used in the trial form, without proving matrix invertibility.

For finite quadrature put $q=(1-H)^2p$. Dilation-commutation and absolute Fubini give
$$
h_i(x)=\delta_{k0}q(x)+\int_1^\infty D_i(u)u^{\rho-1}q(xu)\,du .
$$
Indeed the integral for $Hp(xu)$ is bounded absolutely by a multiple of $(1+\log(xu))/(xu)$ for $xu\ge1$ by splitting at $y=1/(xu)$ in its averaging parameter. The factor $-\log y$ for $H^2p$ gives at most one more log. The resulting majorants are integrable against $|D_i(u)|u^{-1/2}$. On bounded intervals the functions $p,g,q$ are given by the entire series
$$
p(x)=2\sum_{n\ge0}\frac{(-1)^n(2\pi x)^{2n}}{(2n+1)!}
$$
with coefficients multiplied by $1$, $1-1/(2n+1)$, or its square, respectively. Use the absolute factorial-series tail after the successive ratios on the entire interval are at most $1/2$. Elementary bounds are
$$
\begin{aligned}
|g(x)|&\le4 \quad(0<x\le1),&
|g(x)|&\le [2+(1+\log x)/\pi]/x \quad(x\ge1),\\
|q(x)|&\le Q(\log x)/x \quad(x\ge1),&
Q(v)&=6+\pi^{-1}+(2+2/\pi)v+v^2/(2\pi).
\end{aligned}
$$
They follow by integrating $|p(x)|\le2$ near zero and $|p(x)|\le1/(\pi x)$ on the tail. For outer interval $[\lambda,T]$, $T\ge1$, an inner cutoff $U_0\ge1/\lambda$ discards at most
$$
\lambda^{-1}\int_{U_0}^\infty
 [|\rho|(\log u)^k+k(\log u)^{k-1}]
 u^{-3/2}Q(\log T+\log u)\,du .
$$
Again omit the $k$ term for $k=0$. This is explicitly integrable as an exponential times a polynomial in $\log u$. The outer tails have polynomial envelopes given below. Compact interval Riemann sums converge using subdivision and certified arithmetic, since all finite integrands are continuous there. True zero labels are required for exact jet orthogonality. Isolating intervals can be refined for integration, but replacing a true zero by an uncertified approximate ordinate would not preserve orthogonality.

## Explicit bounds for the scaled Gram and target

Set $F_j=2^{j+1}j!=\int_0^1x^{-1/2}\log^j(1/x)\,dx$. Omit $kF_{k-1}$ for $k=0$. Define
$$
\begin{aligned}
A_i&=(\delta_{k0}+|\rho|F_k+kF_{k-1})/\pi,&
B_i&=2(\delta_{k0}+|\rho|F_k+kF_{k-1}),\\
C_i&=B_i+\sum_{j=0}^k\binom kj|U^{(k-j)}(\rho)|F_j,&
C_i'&=B_i+\sum_{j=0}^k\binom kj
      |\partial_\rho^{k-j}(U(\rho)/(1-\rho))|F_j,\\
R_i&=4B_i,&
a_{ij}&=\binom kj V^{(k-j)}(\rho), \qquad 0\le j\le k .
\end{aligned}
$$
Use $V(s)=(s/(1-s))^2U(s)$ here. For $x\ge1$, $|f_i(x)|\le A_i/x$ since $\int_1^\infty u^{-3/2}\log^j u\,du=F_j$. For $0<x\le1$, complete the $u$ integral across $(0,1)$ and use $\mathcal M p(w)=U(w)/w$ for $0<\Re w<1$. The remainder has magnitude at most $B_i$ by $|p|\le2$ and $\int_0^1u^{-1/2}|\log u|^jdu=F_j$. Applying one Hardy average to the leading term inserts $(1-\rho)^{-1}$ inside the derivative. It follows that $\int_0^1|f_i|\le C_i$, $\int_0^1|Hf_i|\le C_i'$, and
$$
h_i(x)=x^{-\rho}\sum_{j=0}^k a_{ij}\log^j(1/x)+r_i(x),\qquad |r_i(x)|\le R_i
\quad (0<x\le1).
$$
For $x\ge1$, $|h_i(x)|\le T_i(\log x)/x$ with
$$
T_i(v)=A_i+2C_i+C_i'+(2A_i+C_i)v+(A_i/2)v^2 .
$$
For example the Hardy averages are bounded respectively by $(C_i+A_i\log x)/x$ and $(C_i'+C_i\log x+(A_i/2)\log^2x)/x$. Thus the outer quadrature tails after $T$ are finite sums of $\int_{\log T}^\infty e^{-v}v^j\,dv$ with explicit polynomial coefficients, for both Gram and target.

Let $\widehat G_{ij}=L^{-1-k_i-k_j}(G_\lambda)_{ij}$ and $\widehat b_i=L^{-k_i}(b_\lambda)_i$. Let $G_0$ have one Hilbert matrix $(1/(k_i+k_j+1))$ per distinct zero, zero elsewhere. Let $b_{0,i}=P(\rho_i)/\rho_i$ when $k_i=0$, zero otherwise. For $L\ge1$, an entry bound $|\widehat G_{ij}-(G_0)_{ij}|\le D_{ij}/L$ results from
$$
D_{ij}^{\rm rem}
=R_iR_j+R_i\sum_b|a_{jb}|F_b+R_j\sum_a|a_{ia}|F_a
+\sum_{r,s}[v^r]T_i[v^s]T_j\,(r+s)!.
$$
If $\rho_i=\rho_j$, add $\sum_{(a,b)\ne(k_i,k_j)}|a_{ia}a_{jb}|/(a+b+1)$ to obtain $D_{ij}$. The sums range over $0\le a\le k_i$, $0\le b\le k_j$. If the roots differ, instead add $2\sum_{a,b}|a_{ia}a_{jb}|/|\Im\rho_i-\Im\rho_j|$. To verify, use the log moments on $(\lambda,1)$. The same-root leading term has $|V(\rho)|=1$. For $\Delta\ne0$, integration by parts gives $|\int_0^L v^n e^{i\Delta v}\,dv|\le2L^n/|\Delta|$ for $n\ge0$. The two remainder cross terms use $F_a,F_b$ and the tail uses $\int_0^\infty e^{-v}v^{r+s}dv=(r+s)!$.

The uncut pairing $\int_0^\infty g(x)\overline{h_i(x)}dx$ equals $(-1)^k\partial_\rho^k[P(\rho)/\rho]$. At $\Re w<1/2$ first use unitarity against the genuine jet. Then pass to the line using the locally uniform integrable products from the kernel formulas. The near-zero powers for a compact neighborhood can be chosen less than one against bounded $g$. The removed part over $(0,\lambda)$ gives $|\widehat b_i-b_{0,i}|\le d_i/L$ with
$$
d_i=
\begin{cases}
16+4R_i,&k_i=0,\\
|\partial_{\rho_i}^{k_i}(P(\rho_i)/\rho_i)|+
 4(\sum_j|a_{ij}|F_j+R_i),&k_i\ge1 .
\end{cases}
$$
For $k_i=0$ use $\int_0^\lambda x^{-1/2}dx=2\sqrt\lambda$, $|a_{i0}|=1$, and $Le^{-L/2}\le2$, $Le^{-L}\le1$. For $k_i\ge1$ bound the removed integral over $(0,1)$ and use $L^{-k_i}\le L^{-1}$.

Let $a_0=G_0^{-1}b_0$ and set
$$
C_R=2\sum_i|(a_0)_i|d_i+\sum_{i,j}|(a_0)_i(a_0)_j|D_{ij}.
$$
Apply the variational lower bound to the jets $L^{-k_i-1/2}h_i$ with trial column $L^{-1/2}a_0$. This gives
$$
\boxed{L D_\zeta(\lambda)^2\ge S_R-C_R/L,\qquad
 S_R=\sum_{\rho\in R}m_\rho^2/|\rho|^2.}
$$
Indeed the inverse Hilbert block's first diagonal entry is $m_\rho^2$, so $a_0^*G_0a_0=S_R$. The error bounds apply entrywise. No assertion of finite-$\lambda$ invertibility is needed. The inverse Hilbert blocks are rational. Phase derivatives can be bounded by interval gamma Taylor evaluation or Cauchy estimates on small discs inside $0<\Re s<1$. The bound depends on the fixed zero labels, certified separations and multiplicities.

## Instantiated certificate and two-sided tolerance

Use the zeta zero with ordinate in the Conrey–Li box at $111.029535543169674524656$ of half-width $10^{-20}$. Opposite strict endpoint signs certify existence, and the derivative product excluding zero establishes simplicity. Retain just this zero and $k=0$. Since $111<|\rho|<112$, $\pi>3$, and $|U(\rho)|=|V(\rho)|=1$, one may take $A_i\le75$, $B_i\le450$, $C_i\le452$, $C_i'\le454$, $R_i\le1800$, and $T_i(v)\le1433+602v+38v^2$. Here $|1-\rho|^{-1}\le2$ suffices. Consequently
$$
D_{ii}\le 8277813,\qquad d_i\le7216,\qquad
C_R\le 2(7216)/111+8277813/111^2=3293255/4107<802.
$$
For every $N\ge3$, $(\log N)\Delta_N^2\ge |\rho|^{-2}-802/\log N$. The same bound holds for $d_N$. This is a coarse numerical certificate, with positive content only for very large $N$. The full height list's constant has not been instantiated. [Certified root and derivative boxes](../../experiments/results/witness62_conrey_li_deep.json)

Assume RH and supply the numerical inputs of the effective upper theorem. Take $R=\mathcal F_Y$ of its complete clusters. A certified multiplicity-tail estimate gives $0\le C_\zeta-S_R\le\Theta_Y$, with the stated offset between the cell centers and zero ordinates. Hence $L\Delta_N^2\ge C_\zeta-\Theta_Y-C_R/L$, and (A) bounds $Ld_N^2$ from above. Choose fixed $Y$ so both $\Theta_Y$ and $B Y^{-99/100}$ are within their allocations. With the other fixed-height certificates, choose $N_0$ by decreasing envelopes for $C_R/L$ and the remaining upper terms. This is a two-sided conditional tolerance procedure for both optimized distances. Global upper constants and a final two-sided threshold have not been instantiated. [Effective upper proof (A) and inputs](effective_cluster62_proof.md)

## Exact subtraction on the short interval

The independent $\chi_4$ review suggested avoiding tail quadrature altogether by cancelling the uncut Gram pairing before taking the boundary. Here is the corresponding zeta calculation. Define $h(w,x)$ by the $k=0$ formula, for $w$ near the critical line. For $x\le\lambda$ write $h(w,x)=V(w)x^{-w}+E(w,x)$, where
$$
E(w,x)=2\sum_{n\ge1}\frac{(-1)^n(2\pi x)^{2n}}{(2n+1)!}
       \frac{2n}{w+2n}\left(1-\frac1{2n+1}\right)^2 .
$$
This follows by completing the layer integral and expanding $p(xu)$ for $0<u<1$. For $\Re w,\Re v<1/2$, unitarity gives $\int_0^\infty h(w,x)h^\#(v,x)\,dx=(1-w-v)^{-1}$, where $h^\#(v,x)=\overline{h(\bar v,x)}$. Removing the interval $(0,\lambda)$ gives
$$
\begin{aligned}
\int_\lambda^\infty h(w,x)h^\#(v,x)\,dx
&=\frac{1-V(w)V^\#(v)\lambda^{1-w-v}}{1-w-v}\\
&\quad-\int_0^\lambda\left[
 V(w)x^{-w}E^\#(v,x)+V^\#(v)x^{-v}E(w,x)+E(w,x)E^\#(v,x)
 \right]dx.
\end{aligned}
$$
The apparent pole in the first expression is removable by $V(w)V^\#(1-w)=1$, which follows from boundary unitarity and analytic continuation. The integral on the right is evaluated by absolutely convergent power series with elementary monomial integrals. Derivatives in $w,v$ insert the log polynomials and give all finite Gram entries at the certified zeros. The uncut target pairing is already explicit and its correction likewise integrates only over $(0,\lambda)$. Thus a sharper interval algorithm needs no unbounded or oscillatory quadrature. Bounds for the short series and their derivatives follow from uniform factorial tails on compact complex parameter discs strictly within the continuation strip. This is useful for calculation even though the less sharp bounds above already prove the finite-set result.

For the same simple root as above, the leading term on the diagonal is $L+V'(\rho)/V(\rho)$, with real logarithmic derivative by boundary unitarity. The logarithmic derivative is
$$
\frac{V'(\rho)}{V(\rho)}
=3\left(\frac1\rho+\frac1{1-\rho}\right)-\log\pi
+\tfrac12\left[\psi(\rho/2)+\psi((1-\rho)/2)\right].
$$
The supplied root box and 160-bit interval evaluation give a real value strictly between $0$ and $3$. Elementary near-zero bounds sharpen the preceding constant. Use $p(x)=2\int_0^1\cos(2\pi x v)\,dv$ to get $|p(x)-2|\le4\pi^2x^2/3$ and $|p'(x)|\le8\pi^2x/3$. Thus $|g(x)|\le16\pi^2x^2/9<18x^2$. Before the two Hardy operations, integration by parts in the zero-end correction gives
$$
p(x)-\rho\int_0^1u^{\rho-1}p(xu)\,du
=x\int_0^1 u^\rho p'(xu)\,du,
$$
of magnitude at most $16\pi^2x^2/15$. The two Hardy operations increase this envelope by at most $(1+1/3)^2$, hence $|E(\rho,x)|\le20x^2$. The short-interval Gram correction is bounded by $16\lambda^{5/2}+80\lambda^5$, and the target correction by $(36/5)\lambda^{5/2}+72\lambda^5$. For $L\ge1$, $Le^{-5L/2}<1/10$ and $Le^{-5L}<1/100$. Consequently $|G_\lambda-L|<27/5$ and $L|b_\lambda-b_0|<36/25$. The one-label trial-vector bound now instantiates
$$
C_{\{\rho\}}<
\frac{2(36/25)}{111}+\frac{27/5}{111^2}
=\frac{903}{34225}<0.027 .
$$
Thus the prior $802$ can be replaced by $0.027$ for this selected zero. This sharpens a one-zero example only. [Phase derivative replay](../../experiments/code/prefix_formula62_effective_lower_example.py) · [Retained output](../../experiments/results/prefix_formula62_effective_lower_example.txt)

Restricting to $L\ge10$ improves the same numerical example substantially. The decreasing functions $Le^{-5L/2}$ and $Le^{-5L}$ are then less than $10^{-9}$ and $10^{-19}$, respectively, since $e^{5/2}>10$. Thus $|G_\lambda-L|<3.000001$, $L|b_\lambda-b_0|<8\cdot10^{-9}$, and the trial constant is less than $1/4000$. In particular, for $\log N\ge10$ the explicit one-zero bound
$$
(\log N)\Delta_N^2 \ge \frac1{112^2}-\frac1{4000\log N}
$$
is positive. Its leading term uses only the certified inequality $|\rho|<112$.
