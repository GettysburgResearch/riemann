# A sign test on distinct integers for the Riemann hypothesis

**Proposed theorem for review.** Write $a_n=\Lambda(n)-1$, let $F(v)=\sum_{n\ge1}a_n\exp(-ne^{-v})$, and let $\Theta=\sup_\rho\Re\rho$ for the nontrivial zeta zeros. Define, for $X>1$,
\[
 C(X)=\sum_{m\ne n}\frac{a_ma_n}{m+n}\exp(-(m+n)/X).
\]
The sum runs over ordered pairs of positive integers. The two cases give opposite eventual signs.
\[
 \begin{array}{ll}
 \mathrm{RH}:& C(X)\sim-\tfrac14(\log X)^2,\\
 \neg\mathrm{RH}:& C(X)>0\ \text{eventually},\qquad
             \displaystyle\lim_{X\to\infty}\frac{\log C(X)}{\log X}=2\Theta-1.
 \end{array}                                                     \tag{1}
\]
In particular the existence of arbitrarily large $X$ with $C(X)\le0$ is equivalent to RH. The proposed sign test uses the actual prime weights. The argument establishes both implications of the equivalence. The arithmetic assertion that $C(X)\le0$ occurs arbitrarily late remains open.

## The square integral and the diagonal

Restore the diagonal and call the resulting sum $Q(X)$. Absolute convergence and integration of each exponential give
\[
 Q(X)=\int_{1/X}^{\infty}\left(\sum_{n\ge1}a_ne^{-nt}\right)^2dt
     =\int_{-\infty}^{\log X}F(v)^2e^{-v}\,dv .                \tag{2}
\]
In particular $Q$ increases with $X$. The prime number theorem and partial summation give $\sum_{n\le y}\Lambda(n)^2\sim y\log y$ from the prime terms. The higher powers contribute $O(y^{1/2}\log^3(2y))$. Hence $\sum_{n\le y} a_n^2\sim y\log y$, and
\[
 D(X)=Q(X)-C(X)=\tfrac12\sum_{n\ge1}\frac{a_n^2}{n} e^{-2n/X}
                  \sim \tfrac14(\log X)^2.                      \tag{3}
\]
Indeed the sharp sum through $X$ has this asymptotic by partial summation. On that range the exponential changes the sum by $O(X^{-1}\sum_{n\le X}a_n^2)=O(\log X)$. Dyadic summation on $n>X$ gives the same error there.

The classical smoothed explicit formula yields
\[
 F(v)=-\sum_{\rho\ \mathrm{distinct}}m_\rho\Gamma(\rho)e^{\rho v}+O(1)
 \quad (v\in\mathbb R),\qquad \sum_\rho m_\rho|\Gamma(\rho)|<\infty .
                                                                  \tag{4}
\]
For $v\ge0$ shift $\Gamma(s)(-\zeta'(s)/\zeta(s)-\zeta(s))e^{sv}$ through the zero poles to $\Re s=-1/2$. The residues at one cancel and the pole at zero contributes a constant. For $v<0$ absolute summability and the original sum suffice. In particular $F(v)\ll e^{\Theta v}$ for $v\ge0$, and (2) gives $Q(X)\ll\log X$ on RH. Equations (2) and (3) prove the first part of (1).

## An off-line zero forces a lower bound at every large scale

Fix $\rho_0=\beta+i\gamma$ with $\beta>1/2$, and write $m=m_{\rho_0}$. The classical theta kernel for $\xi$ gives a complex integrable function $K_m$ whose bilateral Laplace transform is $\xi(s)/(s-\rho_0)^m$, with $K_m(t)\ll_{\rho_0}\exp(-c e^{2|t|})$. To see this, start from $K_0(t)=e^{-t/2}\Phi(t)$, where $\xi(s)=\int e^{(s-1/2)t}\Phi(t)\,dt$ and $\Phi$ has this double-exponential decay. At each step use $K_j(t)=-e^{-\rho_0t}\int_{-\infty}^{t}e^{\rho_0u}K_{j-1}(u)\,du$. The full integral at $\rho_0$ vanishes, so the opposite tail bounds $K_j$ at positive infinity. Integration by parts divides the transform by $s-\rho_0$. Applying it to (4) gives
\[
 \int K_m(t)F(v+t)\,dt =
 -m\Gamma(\rho_0)\frac{\xi^{(m)}(\rho_0)}{m!}e^{\rho_0v}
       + O_{\rho_0}(1).                                        \tag{5}
\]
The coefficient is nonzero for every finite multiplicity, regardless of the distance to other zeros.

Put $V=\log X$, $R=\log V$, $v=V-R$. The tails $|t|>R$ in (5) cost $O_{\rho_0}(\exp(\Theta v-c'V^2))$ by (4) and the tail of $K_m$. Cauchy–Schwarz on the remaining interval now gives $\int_{v-R}^{v+R}|F(w)|^2dw\gg_{\rho_0} e^{2\beta v}$. Its right endpoint is $V$, so (2) implies
\[
 Q(X)\gg_{\rho_0}X^{2\beta-1}/(\log X)^{2\beta}.
\]
If RH fails this dominates (3) for any one off-line right-hand zero. Taking $\beta\uparrow\Theta$ and using $Q(X)\ll_\Theta X^{2\Theta-1}$ from (2) and (4) proves the ordinary limit in (1). On RH, the mean of the absolutely convergent trigonometric series $e^{-v/2}F(v)$ squared also gives the asymptotic formula $Q(X)\sim (\sum_{\rho\ \mathrm{distinct}}m_\rho^2|\Gamma(\rho)|^2)\log X$. The $O(e^{-v/2})$ error and the initial finite integral in (2) vanish after division by $\log X$.

## An independent boundary check

Put $H(s)=\int_0^\infty F(v)^2e^{-sv}\,dv$. Its abscissa of convergence is exactly $2\Theta$. Equation (4) gives the upper bound. If the integral converged at a smaller real $a$, Cauchy–Schwarz would make $\int_0^\infty F(v)e^{-sv}\,dv$ holomorphic on $\Re s>a/2$. Adding the entire integral at $v<0$ identifies this function on $\Re s>1$ with $\Gamma(s)(-\zeta'(s)/\zeta(s)-\zeta(s))$, which has a genuine pole at every nontrivial zero.

Landau's positivity theorem for Laplace transforms gives a real singularity of $H$ at $2\Theta$. On $\Re s>2\Theta$, squaring (4) and integrating gives
\[
 H(s)=\sum_{\rho,\rho'}
   \frac{m_\rho m_{\rho'}\Gamma(\rho)\Gamma(\rho')}{s-\rho-\rho'}+J(s),
       \qquad J\ \text{holomorphic on }\Re s>\Theta ,
\]
where the indices range independently over the set of distinct zeros and may be equal. At $s=2\Theta+u$, $u>0$, the factor $u/(s-\rho-\rho')$ has modulus at most one. Dominated convergence therefore gives
\[
 \lim_{u\downarrow0}uH(2\Theta+u)
       =\sum_{\Re\rho=\Theta,\ \rho\ \mathrm{distinct}}m_\rho^2|\Gamma(\rho)|^2.
                                                                  \tag{6}
\]
If the edge is unattained, this number is zero. The real singularity then admits no meromorphic continuation to a neighborhood. A pole of positive integral order contradicts (6), and Landau's theorem rules out a removable singularity. If the edge is attained, (6) gives its radial leading coefficient. It supplies no punctured neighborhood of meromorphicity by itself.

The same boundary is visible directly in an arithmetic Dirichlet series. On $\Re s>2$,
\[
 \Gamma(s)\sum_{m,n\ge1}\frac{a_ma_n}{(m+n)^s}
     = H(s)+\int_{-\infty}^{0}F(v)^2e^{-sv}\,dv .
\]
The last integral is entire by the original exponential sum. Removing the diagonal subtracts $2^{-s}\sum a_n^2n^{-s}$, holomorphic on $\Re s>1$. If RH fails, the distinct-integer series has the real singularity in (6) after division by $\Gamma(2\Theta)$. In particular a method that lists only isolated poles could overlook the boundary of holomorphy in the unattained case. For comparison, Bhowmik and Schlage-Puchta's natural-boundary results treat the uncentered Goldbach series under the respective hypotheses of their Theorem 2. [Primary paper](https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/gautami_bhowmik/Publications/gold_funct.pdf)

## Separating coprime pairs exposes a secondary term larger than the target

Let $C_{>}(X)$ and $C_{1}(X)$ be the contributions to $C(X)$ from $\gcd(m,n)>1$ and $\gcd(m,n)=1$, respectively. Put $L=\log X$, $c=1-1/\zeta(2)$, and let $B_1=\lim_{y\to\infty}(\sum_{p\le y}p^{-1}-\log\log y)$ be the prime Mertens constant. Then on the actual arithmetic coefficients,
\[
 C_{>}(X)=cX-L^2\log L+(3/2-\gamma_{\rm E}-B_1)L^2+o(L^2).                              \tag{7}
\]
Also $C_1(X)=-cX+o(X)$ unconditionally. Thus even after canceling the two linear terms, the displayed $L^2\log L$ correction in the noncoprime pairs is larger than the entire RH-scale sign test.

For the constant-weight part, the number of pairs of positive integers with sum $N\ge2$ and a common factor greater than one is $N-1-\varphi(N)$. Removing the equal pairs changes its weighted sum by $O(L)$. The resulting contribution is $cX+O(L)$, since
\[
 \sum_{N\ge1}\frac{\varphi(N)}N e^{-N/X}
   =\sum_d\frac{\mu(d)}{d(e^{d/X}-1)}
   =\frac{X}{\zeta(2)}+O(L).
\]
In the last step use $(e^{d/X}-1)^{-1}=X/d+O(1)$ for $d\le X$ and exponential decay thereafter. Distinct prime powers with a common prime must have the form $p^j,p^k$ with $j\ne k$. Their entire $\Lambda(m)\Lambda(n)$ contribution is bounded by $2\sum_p(\log p)^2\sum_{k\ge2} k p^{-k}<\infty$.

Each linear term has unsigned magnitude
\[
 U(X)=\sum_{p,k\ge1}\frac{\log p}{p}
              \sum_{j>p^{k-1}}\frac{e^{-jp/X}}{j}+O(L).
\]
Here $m=p^k$, while $n$ runs through the positive multiples of $p$. The $O(L)$ removes the possible equality $m=n$ by the classical bound $\sum_n\Lambda(n)n^{-1}e^{-2n/X}=O(L)$. Comparison with the integral of the decreasing inner summand gives $\log(X/p^k)+O(1)$ if $p^k\le X$ and an $O(e^{-p^k/X})$ upper bound otherwise. The total error is $O(L\log(2L))$ by the prime harmonic sum, the rapid decay over the remaining powers of each $p\le X$, and Chebyshev's bound for $p>X$. For $h=\log p$ the finite sum evaluates to
\[
 \sum_{1\le k\le L/h}(L-kh)
  =\frac{L^2}{2h}-\frac L2+\frac h2\{L/h\}(1-\{L/h\}).
\]
Consequently $U(X)=\tfrac12 L^2(\log L+B_1-1+I)+o(L^2)$, where $I=\int_0^1 u\{1/u\}(1-\{1/u\})\,du$. Indeed $\sum_{p\le X}\log p/p=L+O(1)$, and the measures $L^{-1}\sum_{p\le X}(\log p/p)\delta_{(\log p)/L}$ converge weakly on $[0,1]$ to uniform measure by the same estimate. Apply this to $u\{1/u\}(1-\{1/u\})$, continued by zero at $u=0$. After substituting $x=1/u$, the contribution to $I$ from $x\in[k,k+1]$ is $\tfrac12(1/k+1/(k+1))-\log(1+1/k)$. Summing gives $I=\gamma_{\rm E}-1/2$. Subtracting both linear terms now proves (7). Finally the prime number theorem gives $F(v)=o(e^v)$, which implies $Q(X)=o(X)$ by (2). Subtract (3) and (7) to get the stated leading term for $C_1$.

In particular RH is also equivalent to the existence of arbitrarily large $X$ with $C_1(X)+cX\le L^2\log L$. On RH the left side minus $L^2\log L$ is $(\gamma_{\rm E}+B_1-7/4+o(1))L^2$ by (1) and (7). Its leading coefficient is negative because $B_1=\gamma_{\rm E}+\sum_p(\log(1-1/p)+1/p)\le\gamma_{\rm E}$ and $\gamma_{\rm E}\le3/2-\log2<7/8$. Under failure of RH the positive power growth in (1) dominates the terms of order $L^2$.

The same separation identifies a genuine logarithmic singularity. Write $\Phi_>(s)=\sum_{\gcd(m,n)>1,\,m\ne n}a_ma_n/(m+n)^s$ initially for $\Re s>2$. Its continuation to $\Re s>1$ has only the simple pole at $s=2$, of residue $c$. Indeed the constant-weight series follows from $N-1-\varphi(N)$ and $\sum_N\varphi(N)N^{-s}=\zeta(s-1)/\zeta(s)$. The omitted equal pairs give a multiple of $\zeta(s)$ and finitely many entire corrections there. The two linear terms converge absolutely when $\sigma=\Re s>1$, since
\[
 \sum_p\frac{\log p}{p^\sigma}
  \sum_{k\ge1}\sum_{j>p^{k-1}}j^{-\sigma}
   \ll_\sigma\sum_p\frac{\log p}{p^\sigma(1-p^{1-\sigma})}<\infty .
\]
The prime-power pair term converges even for $\sigma>1/2$ by the distinct-power argument above. Thus every singularity of the full distinct-integer series in $1<\Re s<2$ must come from its coprime pairs.

At the critical real point, however,
\[
 \Phi_>(1+w)=-\frac2{w^2}\big(\log(1/w)+B_1+o(1)\big)
       \qquad(w\downarrow0).
\]
Indeed the Mellin transform of $C_>(1/t)$ is $\Gamma(w)\Phi_>(1+w)$ on $\Re w>1$. Subtract $c/t$ on $0<t<1$, adding back $c/(w-1)$ after continuation to $\Re w>0$. In (7) the term $-L^2\log L$ gives $-w^{-3}(2\log(1/w)+\Gamma'(3))$ and the next term gives $2(3/2-\gamma_{\rm E}-B_1)w^{-3}$. The remainder is $o(w^{-3})$ by scaling $w\log(1/t)$ in its integral. Since $\Gamma'(3)=3-2\gamma_{\rm E}$ and $\Gamma(w)=w^{-1}+O(1)$ the claimed expansion follows. This is a nonmeromorphic singularity of an actual arithmetic component independent of RH.

### The entire critical line is a natural boundary for the noncoprime block

In fact $\Phi_>$ admits no meromorphic continuation across any point of $\Re s=1$, unconditionally. This follows from the arithmetic of the actual noncoprime pairs. It concerns the separated series, whose two linear terms enter with the same sign.

Put $w=s-1$. Near any $s=1+i\tau$ with $\tau\ne0$, the only part of $\Phi_>(s)$ requiring continuation is $-2B(w)/w$, where
\[
 B(w)=\sum_p\frac{\log p}{p(p^w-1)}\qquad(\Re w>0).
\]
Indeed in the linear series above, replace each $\sum_{j>a}j^{-s}$ by $a^{1-s}/(s-1)$ with $a=p^{k-1}$. Summing that term in $k$ gives $B(w)/w$. The difference for $k\ge2$ is $O_K(a^{-\Re s})$, locally uniformly for $s$ in a compact set $K$ in $\Re s>0$, by first-order Euler summation for the Hurwitz zeta tail. Its prime sum is holomorphic in $\Re s>1/2$. For $k=1$ the difference is
\[
 \big(\zeta(s)-1-(s-1)^{-1}\big)\sum_p(\log p)p^{-s}.
\]
The prime series here is $-\zeta'(s)/\zeta(s)$ minus an absolutely convergent higher-power series in $\Re s>1/2$. This is regular at $1+i\tau$ by the classical zero-free line. Removing the equal pairs in this linear term subtracts $2^{-s}(-\zeta'(s)/\zeta(s))$, also regular there. The constant-weight and double-prime-power parts have the continuation described above.

Fix any prime $p_0$ and any nonzero integer $k$, and put $\tau=2\pi k/\log p_0$. We claim
\[
 \liminf_{u\downarrow0}u\,\Re B(u+i\tau)\ \ge\ 1/p_0 .
\]
For any fixed $\delta>0$, split the primes at $Y=\exp(\delta/u)$. The summand of $p_0$ after scaling by $u$ tends to $1/p_0$. For other $p\le Y$ use $\Re (e^{x+iy}-1)^{-1}\ge-1/2$ for $x>0$, which follows by taking the real part of $(e^{x+iy}+1)/(e^{x+iy}-1)$. Hence their total scaled real part is at least $-\tfrac12u\sum_{p\le Y}(\log p)/p=-\delta/2+o(1)$.

The scaled sum over $p>Y$ tends to zero. Expand $(p^{u+i\tau}-1)^{-1}=\sum_{j\ge1}p^{-ju-ij\tau}$. For each fixed $j$, the prime number theorem and partial summation approximate the resulting scaled prime sum by
\[
 u\int_Y^\infty x^{-1-ju-ij\tau}\,dx
       = \frac{uY^{-ju-ij\tau}}{j(u+i\tau)}\longrightarrow0 .
\]
For detail, if $\epsilon_Y=\sup_{x\ge Y}|\vartheta(x)-x|/x$, the error is at most $u\epsilon_Y e^{-j\delta}(1+|1+ju+ij\tau|/(ju))=o(1)$ for fixed $j$. Uniformly in $j$, Chebyshev's bound makes the absolute scaled prime sum $O((u+1/j)e^{-j\delta})$, a summable majorant for $0<u<1$. Dominated convergence proves the tail assertion. Now let $\delta\downarrow0$. This proves the lower bound without a hypothesis on any zeta zero in the interior strip.

The resulting nonzero singular ordinates are dense in $\mathbb R$, since their spacing for a single prime is $2\pi/\log p_0$, tending to zero as $p_0$ grows. Any meromorphic continuation across a boundary arc would have a pole at each of its indicated nonzero ordinates, contradicting isolation of poles. The real-axis expansion above identifies the additional logarithmic singularity at its center. The external analytic inputs for this boundary argument are the prime number theorem, the zero-free line at one and first-order Euler summation for the Hurwitz tail. The reduction and the radial estimate are proved here. [Prime number theorem](https://dlmf.nist.gov/25.16) · [Zeta zeros](https://dlmf.nist.gov/25.10) · [Euler–Maclaurin representation](https://dlmf.nist.gov/25.11#iii)

## Testing the sign with exact factorial inversion

The exact divisor identity gives $\Lambda=\mu*\log$. Put $S(z)=\sum a_n e^{-nz}$ for $\Re z>0$ and define
\[
 L(t)=\sum_{k\ge1}\log k\,e^{-kt},\qquad
 K(t)=L(t)+\frac{\log t+\gamma_{\rm E}}t .
\]
The subtracted continuum integral is $\int_0^\infty (\log x)e^{-tx}\,dx=(-\gamma_{\rm E}-\log t)/t$. The prime number theorem with its classical zero-free error gives the convergent sums $\sum\mu(d)/d=0$ and $\sum\mu(d)\log d/d=-1$. Indeed the series and its derivative converge up to the real point one by partial summation, where $1/\zeta$ has a simple zero of derivative one. Consequently
\[
 S(t)=\sum_{d\ge1}\mu(d)K(dt)+\frac1t-\frac1{e^t-1}.                 \tag{8}
\]
The series on the right is taken in increasing order of $d$. The last correction tends to $1/2$ as $t\downarrow0$.

For each of the two signs separately, the *actual* Möbius coefficients satisfy
\[
 \int_{1/X}^{2/X}
  \left|\sum_{\substack{X\le d\le2X\\ \mu(d)=\pm1}}K(dt)\right|^2dt
       \gg X .                                                        \tag{9}
\]
Indeed $1\le dt\le4$ throughout this block, so $K(dt)\ge\gamma_{\rm E}/4$. Each sign occurs $(3/\pi^2+o(1))X$ times by the squarefree density and $\sum_{n\le X}\mu(n)=o(X)$. This proves (9). Taking absolute values term by term in the compensated factorial inversion thus produces a squared majorant with a linear contribution just from this block. To prove $C(X)\le0$, the full square integral in (2) has to stay below $(1/4+o(1))(\log X)^2$ along the selected sequence. The positive majorant discards cancellation needed on the true integer coefficients.

Positivity of generalized divisor coefficients encounters a distinct issue. Put $Y(s)=\zeta(s)-1$, and write $A_j(n)$ for the coefficient of $n^{-s}$ in $Y(s)^j$. It counts ordered factorizations into $j$ nonunits. For integer $k\ge0$, the generalized divisor coefficients of $\zeta(s)^k$ satisfy $d_k(n)=\sum_{j=0}^k\binom{k}{j}A_j(n)$. Thus $A_j(n)$ is their $j$th forward difference at zero. For $n>1$ the coefficientwise finite identity
\[
 \Lambda(n)=(\log n)\sum_{j\ge1}(-1)^{j-1}A_j(n)/j
\]
follows from the Euler product for $\log\zeta$. Fix the first $r$ primes and restrict to their products with exactly $K+1$ prime factors counted with multiplicity. On this set the error from truncation after order $K$ has sign $(-1)^K$, since only order $K+1$ remains. Each ordered choice of $K+1$ primes occurs once, and $\log n\ge(K+1)\log2$. The total absolute error on this set is therefore at least $(\log 2)\,r^{K+1}$. These products are all $\le X=p_r^{K+1}$ and can also be given weights $e^{-n/X}\ge e^{-1}$. As $\log r/\log p_r\to1$, for every $a<1$ one can fix $r$ so this omitted contribution exceeds $X^a$ along all sufficiently large $K$. The statement concerns bounds obtained by taking absolute coefficient errors. A signed recovery from many divisor moments can still use cancellation across the omitted sets.

## An actual local minimum and the angular average

For $0<T<1$ consider the $2\pi$-periodic function
\[
 E_T(\theta)=\int_T^\infty |S(t+i\theta)|^2\,dt .
\]
Then $E_T(0)=Q(1/T)$ and its angular mean is $D(1/T)$ by Parseval. At every real zero $S(T)=0$, the angle zero is a strict local minimum of $E_T$. Indeed $E_T$ is even, and differentiation followed by integration by parts gives
\[
 E_T''(0)=4\int_T^\infty |S'(t)|^2dt+2S(T)S'(T)>0
 \quad\text{if }S(T)=0 .                                             \tag{10}
\]
All differentiations converge at fixed $T>0$, and $S$ is nonconstant. There are such $T$ arbitrarily close to zero by the [prime-sum oscillation argument](nov18b-goldbach-local.md).

One can quantify how much of the angular mean this local information sees. For every fixed $c>0$,
\[
 \int_{-cT}^{cT}E_T(\theta)\,d\theta=o(1),\qquad
 \int_{\pi-cT}^{\pi+cT}E_T(\theta)\,d\theta
     \ \longrightarrow\ \int_{-c}^{c}\frac{\arctan |u|}{|u|}\,du .    \tag{11}
\]
The fraction takes value one at zero. The prime number theorem gives $\sum_{n\le y}a_n=o(y)$. Partial summation then gives $S(t+i\theta)=o(t^{-1})$ as $t\downarrow0$, uniformly for $|\theta|\le ct$. Splitting the defining integral at small fixed $t$ shows that $T\sup_{|\theta|\le cT}E_T(\theta)\to0$. For the second limit, the only even prime powers with nonzero weight are powers of two. Thus $\sum_{n\le y}(-1)^n a_n=-y+o(y)$, and uniformly in $|\delta|\le ct$ we have $S(t+i\pi+i\delta)=-(t+i\delta)^{-1}+o(t^{-1})$ by the same partial summation. At $\delta=Tu$, change variables $t=Tx$. Chebyshev's bound gives $|S(Tx+i\pi+iTu)|\ll (Tx)^{-1}$ uniformly for $x\ge1$, also for $Tx\ge1$ by exponential decay. Dominated convergence gives $TE_T(\pi+Tu)\to\int_1^\infty (x^2+u^2)^{-1}dx=\arctan(|u|)/|u|$ and then the displayed integral limit.

There is also a resolution barrier for positive discrete angular averages. For any even $q=q(X)$, the equally weighted $q$th-root average satisfies
\[
 \frac1q\sum_{j=0}^{q-1} E_{1/X}(2\pi j/q)
       \ \ge\ \frac{E_{1/X}(\pi)}q \ =\ \frac{(1+o(1))X}{q}.
\]
Here the case $u=0$ of the preceding proof gives $E_{1/X}(\pi)\sim X$, independent of $q$. Every even mesh with $q=o(X/(\log X)^2)$ overshoots the continuous mean by a factor tending to infinity, including at the zeros in (10).

An exact three-term calculation shows why (10) alone cannot force the global comparison. Retain the actual coefficients at $n=1,2,p$ for a prime $p$, setting the others aside for this calculation. For sufficiently large $p$, the resulting exponential sum has a real zero $T_p>0$ where $e^{-T_p}+(1-\log 2)e^{-2T_p}=(\log p-1)e^{-pT_p}$. The zero is unique after multiplying by $e^{pT_p}$, and $T_p\to0$. At that zero the distinct-index energy of these three terms tends to $2(1-\log 2)/3>0$. The $(1,2)$ and $(2,1)$ terms give this limit, while the four terms involving $p$ have bounded numerators and denominators at least $p+1$. This is a statement for the subform and supplies no sign for the discarded terms.

Equation (10) gives the favorable direction at a recurring set of scales. Equation (11) shows why replacing the local test by the global angular mean still needs a new comparison. A central value growing like $T^{-(2\Theta-1)+o(1)}$ for $\Theta<1$ can fit inside the vanishing angular mass.

## Review of the sharp-cutoff inputs

For $B(N)=\sum_{m+n\le N}a_ma_n$, the signed [local Goldbach argument](nov18b-goldbach-local.md) and [cumulative version](nov18b-goldbach-review.md) use the exact identity $\int B(x)e^{-x/Y}dx=YF(\log Y)^2$. Their isolated-zero identity is (5). The positive divided difference has the stated sign at each interpolation node, and its coefficient bound has a convergent product for each fixed ratio greater than one. The compact positive zero-killing measure in the [short-window argument](nov18b-compact-zero-filter.md) needs only $\sum_{\Re\rho\ge\alpha}(1+|\Im\rho|)^{-1}<\infty$ at fixed $\alpha>1/2$, furnished by Ingham's density estimate. Multiple zeros and nearby distinct zeros preserve the limiting finite measure. On an unattained edge the support can shrink because the tail of this convergent positive sum tends to zero. Constants in those constructions depend on the requested width and chosen zero.

Coefficient extraction in Goldston and Suriajaya's (12) gives exactly $B(N)$. Their (18) bounds its magnitude by their unsigned circle integral. Their Theorems 4 and 6 give the stated upper envelopes under their corresponding hypotheses. These checks support the previous equivalence. Formula (1) gives a separate test with a purely arithmetic negative sign and requires neither their upper envelopes nor their short-interval inputs. [Goldston–Suriajaya, source](https://arxiv.org/abs/2110.14250)
