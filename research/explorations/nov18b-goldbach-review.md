# Both signs of the centered Goldbach residual have full cumulative growth at every large scale

Let $a_n=\Lambda(n)-1$, $B(x)=\sum_{m+n\le x}a_ma_n$, $B_\pm(x)=\max(\pm B(x),0)$, and let $\Theta$ be the supremum of the real parts of the nontrivial zeta zeros. For **each fixed nontrivial zero** $\rho=\beta+i\gamma$ and for every sufficiently large $X$,
\[
 \sum_{n\le X}B_+(n)\gg_\rho\frac{X^{1+2\beta}}{(\log X)^{16}},
 \qquad
 \sum_{n\le X}B_-(n)\gg_\rho\frac{X^{1+2\beta}}{(\log X)^{16}}.       \tag{A}
\]
In particular the two cumulative exponents have ordinary limits
\[
 \lim_{X\to\infty}\frac{\log(1+\sum_{n\le X}B_\pm(n))}{\log X}
      =1+2\Theta.                                                    \tag{B}
\]
No zero need attain $\Theta$. This strengthens the limsup in [the original estimate, (11)](nov18b-variance-goldbach.md).

## Isolating a single zero and a positive annihilating kernel

Put $F(v)=\sum_{n\ge1}a_n\exp(-ne^{-v})$. Equations (2)–(4) of the original estimate give, for every real $v$,
\[
 F(v)=-\sum_\rho\Gamma(\rho)e^{\rho v}+O(1),\qquad
 |F(v)|\ll e^{\Theta v},\qquad \sum_\rho|\Gamma(\rho)|<\infty.
 \tag{C}
\]
The global first estimate at $v<0$ follows from absolute summability and the rapid decrease of the original sum. Zeros in (C) are counted with multiplicity.

Use the classical real even theta kernel $\Phi$ normalized by
\[
 \xi(s)=\int_{\mathbb R}e^{(s-1/2)t}\Phi(t)\,dt .
\]
It is strictly positive. For $t\ge0$ its series, up to a positive normalization, is
\[
 \sum_{n\ge1}(2\pi^2n^4e^{9t/2}-3\pi n^2e^{5t/2})
                                      \exp(-\pi n^2e^{2t}).
\]
Every summand is positive on this half-line and the series gives $\Phi(t)\ll \exp(-c e^{2|t|})$ on the whole real line. This normalization of the logarithmic variable follows by inserting $y=e^{2t}$ in the usual theta Mellin integral and integrating by parts twice. Write $K(t)=e^{-t/2}\Phi(t)$, so its bilateral transform at $s$ is $\xi(s)$. Termwise integration of (C) yields the uniform identity
\[
                    \int_{\mathbb R} K(t)F(v+t)\,dt=O(1).          \tag{D}
\]
Indeed $K$ has all exponential moments, and each zero term contributes $\xi(\rho)=0$.

For a fixed zero $\rho_0$ of multiplicity $m$, define $K_0=K$ and, successively for $1\le j\le m$, let
\[
 K_j(t)=-e^{-\rho_0 t}\int_{-\infty}^t e^{\rho_0 u}K_{j-1}(u)\,du .
\]
The integral over the entire line vanishes at each step because the preceding transform $\xi(s)/(s-\rho_0)^{j-1}$ still has a zero at $\rho_0$. On $t\ge0$ one may therefore use the tail to $+\infty$. It follows inductively at both ends that $|K_j(t)|\ll_{\rho_0}\exp(-c_j e^{2|t|})$ with $c_j>0$. Integrating $K_j'+\rho_0K_j=-K_{j-1}$ gives the claimed transform quotient at the next step. The entire transform of $K_m$ thus vanishes at every distinct zero other than $\rho_0$ and takes the nonzero value $\xi^{(m)}(\rho_0)/m!$ there. Consequently
\[
 \int_{\mathbb R}K_m(t)F(v+t)\,dt
   =-m\Gamma(\rho_0)\frac{\xi^{(m)}(\rho_0)}{m!} e^{\rho_0v}+O_{\rho_0}(1).
                                                                   \tag{E}
\]
The kernel here can be complex. Only (D) uses a positive kernel. The interchanges in both identities follow from (C) and the integrable majorant $|K_j(t)|e^{|t|}\sum_\rho|\Gamma(\rho)|$ at fixed $v$.

## Uniform mass from the Laplace square

Let $V=\log X$, $R=\log V$, and $v=V-5R$. For all sufficiently large $X$, equation (E) supplies some $v_1$ in $[v-R,v+R]$ with $|F(v_1)|\gg_{\rho_0}e^{\beta v}$. Indeed the discarded tails in (E) are $\ll_{\rho_0}\exp(\Theta v-c' e^{2R})$, and $\|K_m\|_1$ is fixed. Write $Y_1=e^{v_1}$, $Y_2=e^{v_1+2R}$, and $P_\pm(Y)=\int_0^\infty B_\pm(x)e^{-x/Y}\,dx$. Both are nondecreasing, and
\[
                 P_+(Y)-P_-(Y)=YF(\log Y)^2.
\]

We claim that $P_-(Y_2)\ge\frac12Y_1F(v_1)^2$. Otherwise, throughout $0\le t\le2R$, monotonicity gives $F(v_1+t)^2\ge\frac12 e^{-t} F(v_1)^2$. The continuous real function $F$ then has constant sign throughout that interval. In (D) at $v_1+R$, its contribution for $|t|\le1$ has magnitude $\gg |F(v_1)|e^{-R/2}$, since $K$ is strictly positive there. All other contributions for $|t|\le R$ have the same sign. The exterior costs $\ll\exp(\Theta(v_1+R)-c'e^{2R})$. These estimates contradict (D) as $V\to\infty$. Also $P_+(Y_2)\ge P_+(Y_1)\ge Y_1F(v_1)^2$. Since $Y_1\ge X/V^6$ and $|F(v_1)|^2\gg_{\rho_0}X^{2\beta}/V^{10\beta}$, the lower bound for either Laplace mass is $\gg_{\rho_0}X^{1+2\beta}/V^{6+10\beta}$.

Finally $Y_2\le X/V^2$. Chebyshev's bound implies $|B(x)|\ll(1+x)^2$. Hence the tail from $x>X$ in either Laplace mass is $O((1+Y_2)^3 e^{-V^2/2})$. On $x\le X$ the weight is at most one and $B$ is constant between integers. This proves (A), even with $6+10\beta$ in place of 16. Combining (A) with the published upper envelope and then taking $\beta$ arbitrarily close to $\Theta$ proves (B).

For every $\epsilon>0$ and all sufficiently large $X$, each sign occurs at magnitude $B_\pm(n)\ge n^{2\Theta-\epsilon}$ at at least $X^{1-\epsilon}$ distinct integers in $[X^{1-\epsilon},X]$. For $0<\epsilon<1$, choose $\delta>0$ small compared with $\epsilon$. Equation (B) gives total mass at least $X^{1+2\Theta-\delta}$. The part below $X^{1-\epsilon}$ is $O_\delta(X^{(1-\epsilon)(1+2\Theta+\delta)})$, and values below threshold contribute $O(X^{1+2\Theta-\epsilon})$. Use the pointwise upper bound $O_\delta(X^{2\Theta+\delta})$ on the rest and take $2\delta<\epsilon$. Nothing in these statements establishes an upper bound of RH strength for the cumulative mass.

## Audit and source comparison

I checked the original proof at Git blob `62cd8aa813b89d0198b5689514f6317d6c9592fe`. The exponent in its Gaussian estimate (10) is valid even at $R=1$ because $195/28-(3/2)(1+1/\sqrt {14})>5$. The compact localization in (13) follows uniformly in the dyadic scale from Fourier inversion with finitely many derivatives. Its argument at an attained edge needs only compact-test convergence and summable distributional bounds on the dyadic tails. The limiting uniformly almost-periodic profile is nonzero by uniqueness of a single Fourier coefficient, has zero mean, and has a zero later than a nonzero value. This rules out a monotone nonnegative Laplace profile for a limiting one-sign distribution. I found no gap in (1)–(13).

* Goldston and Suriajaya's (12) is exactly this $B(N)$, by coefficient extraction. Their (18) bounds its magnitude by a positive circle integral. Their Theorems 4 and 6 give the third logarithmic power on RH and the fifth when $1/2<\Theta<1$, with Theorem 6 attributed to Bhowmik, Halupczok, Matsumoto and Suzuki. [Published article](https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/abs/on-an-average-goldbach-representation-formula-of-fujii/9C6EF5AA639674AD7AFF4A9F91BD72E3) · [Preprint, equations (12), (18) and (33)](https://arxiv.org/abs/2110.14250)
* Under RH, Bhowmik, Ramaré and Schlage-Puchta prove $\Omega_\pm(x)$ for the usual Fujii error and logarithmically averaged results about its large values, using the doubled first zero ordinate. The usual error and the centered convolution can differ by a term of order $N$, relevant at this endpoint. [Propositions 1.3–1.4 and Corollary 1.5](https://doi.org/10.5802/jtnb.940)
* Bhowmik and Ruzsa's Theorem 2.1 recovers a fixed zero-free strip from a two-sided power saving in the **uncentered** Goldbach sum after removing $x^2/2$. Billington, Cheng, Schettler and Suriajaya study the corresponding error and general zero-free regions. The identified sources establish neither the two one-sided full exponents for the centered residual nor (A); this source comparison does not settle priority. [Bhowmik–Ruzsa](https://arxiv.org/abs/1711.06442) · [Billington et al.](https://arxiv.org/abs/2306.09102)
