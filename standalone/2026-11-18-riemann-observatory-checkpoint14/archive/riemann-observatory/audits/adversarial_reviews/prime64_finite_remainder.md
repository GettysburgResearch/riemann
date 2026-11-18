# A finite-height remainder for the tapered $k=2$ prime array

Assume RH. Let $E_N=E_N(2)$ be the prescribed anchored squared error, $L=\log N$ for integer $N\ge3$, and $r_\rho=-m_\rho(2^{1-\rho}-1)$ at a distinct zero $\rho=1/2+i\gamma_\rho$ of multiplicity $m_\rho$. Both ordinate signs are included. The limit is $C_2=\sum_\rho |r_\rho\zeta'(\rho)/\rho|^2$. The summand vanishes at every multiple zero. [Definition and exact limit](director_tapered_prime_array_round9.md)

## Inputs and bound

Choose a rational cutoff $Y\ge0$. Supply a complete finite certificate for the distinct zeros with $|\gamma_\rho|\le Y$, including their multiplicities and disjoint ordinate enclosures. The certificate must settle the side of the cutoff or include any zeros equal to the cutoff. Let $\mathcal F$ be this finite set. Choose a positive rational $\delta\le1/16$ with twice $\delta$ strictly less than the gap between any two enclosures. No separation from the zeros beyond $Y$ is required.

Take $R=2\delta$. For each finite zero let $M_\rho$ bound $|\zeta|$ on the disk of radius $R$ about the true $\rho$. One can always take $2400(2+G_\rho)^{7/16}$, where $G_\rho$ bounds $|\gamma_\rho|$ from its enclosure. A tighter certified disk bound is also allowed. Define
$$
 b_\rho=\frac{r_\rho\zeta'(\rho)}{\rho},\qquad
 C_{\mathcal F}=\sum_{\rho\in\mathcal F}|b_\rho|^2,\qquad
 D_\rho=3m_\rho\left(\frac{4M_\rho}{R^2}+\frac{4M_\rho}{R}\right).
$$
Take $0\le c_-\le C_{\mathcal F}\le c_+$ using the ordinate and derivative balls. Use the exact $b_\rho=0$ at a certified multiple zero. [Effective $k=2$ disk and counting estimates](prime_array63_effective_bound_skeptic.md)

For $X=1+\lfloor Y\rfloor$, set
$$
\begin{aligned}
 B(Y)&=6\cdot10^{22}X^{-1/16},\\
 A(Y)&=\begin{cases}B(Y),&X<3,\\
 \min\{B(Y),9\cdot10^{14}X^{-1/8}(8\log X+64)\},&X\ge3,\end{cases}\\
 q&=\min\{1,4/(\pi L\delta)\},\\
 \alpha&=\sqrt{2\cdot10^{26}/L}+\sqrt{B(Y)}+\sqrt{q B(0)}
       +\sqrt{\frac{4\delta}{\pi L}\sum_{\rho\in\mathcal F}D_\rho^2},\\
 \eta&=\alpha+\sqrt{A(Y)}+(1-\sqrt{1-q})\sqrt{c_+}.
\end{aligned}
$$
Then
$$
 \sqrt{LE_N}-\sqrt{C_2}\le\alpha,\qquad
 \sqrt{C_2}-\sqrt{LE_N}\le\eta,\qquad
 \boxed{|LE_N-C_2|\le 2\sqrt{c_++A(Y)}\,\eta+\eta^2.}
$$
For fixed certified height, the background and localization terms tend to zero with $L$. The remaining bounds decrease by explicit powers of $Y$ up to the displayed logarithm.

Given a certified finite interval $0\le e_-\le LE_N\le e_+$, an enclosure for $C_2$ is
$$
 \left[\max\{c_-,(\max\{0,\sqrt{e_-}-\alpha\})^2\},\
       \min\{c_++A(Y),(\sqrt{e_+}+\eta)^2\}\right].
$$
When $q<1$, intersect the upper endpoint also with $(\sqrt{e_+}+\alpha)^2/(1-q)+A(Y)$. Existing finite error balls can be scaled outward by $\log N$. The coarse constants can leave the derivative-only interval unimproved at small $N$. Completeness and multiplicities of the finite list are hypotheses of the remainder bound. [Unconditional finite squared-error certificates](director_prime_array_effective_round9.md)

## Proof

Use boundary norm with measure $dt/(2\pi)$. Put $s=1/2+it$, $T_t=2+|t|$ and $T_\rho=2+|\gamma_\rho|$. The sharp effective proof decomposes the residual into $P_N+W_N$ with
$$
 \sqrt L\,P_N(t)=\sum_{|t-\gamma_\rho|\le1} a_\rho(t)H_L(t-\gamma_\rho),
 \quad a_\rho(t)=\frac{r_\rho\zeta(s)}{s(s-\rho)},\quad
 H_L(u)=\frac{1-e^{-iLu}}{i\sqrt L\,u}.
$$
Removable values use their continuous extensions. The regular derivative, far residues, left contour and actual anchor together satisfy $\|\sqrt L\,W_N\|\le\sqrt{2\cdot10^{26}/L}$, keeping the $L$ dependence from the pointwise bound in that proof. Plancherel gives $\|H_L\|=1$ since it is the Fourier transform of $L^{-1/2}\mathbf 1_{[0,L]}$. [Effective decomposition, equations (2)–(8) and full-norm assembly](prime_array63_effective_bound_skeptic.md)

For any subcollection of the near sum, weighted Cauchy–Schwarz with the unit-window count gives the pointwise squared bound
$$
 9\cdot10^{14}T_t^{-9/8}\log T_t
 \sum_{\rho\ {\rm selected},\ |t-\gamma_\rho|\le1}m_\rho |H_L(t-\gamma_\rho)|^2 .
$$
The bound also holds with additional distance indicators for each summand and its term on the right. On $|t-\gamma_\rho|\le1$ the outer weight is at most $5T_\rho^{-9/8}\log T_\rho$. Select $|\gamma_\rho|>Y$ and integrate each kernel with squared mass at most one. The squared near-tail norm is bounded by
$$
 9\cdot10^{14}\cdot5\sum_{|\gamma_\rho|>Y}m_\rho T_\rho^{-9/8}\log T_\rho
 \le 9\cdot10^{14}\cdot5\cdot800
     \sum_{j\ge\lfloor Y\rfloor}(j+2)^{-9/8}\log^2(j+2)
 < B(Y).
$$
The two signs in each shell $j\le|\gamma|<j+1$ give total multiplicity at most $200\log(j+3)\le400\log(j+2)$. The displayed factor 800 allows slack. Using $\log x\le32x^{1/32}$, the decreasing sum is at most $32^2\int_X^\infty x^{-17/16}dx$.

At a simple zero $|b_\rho|\le1.5\cdot10^6 T_\rho^{-9/16}$ by the derivative bound and $|\rho|^{-1}\le5/T_\rho$. The displayed weight per zero dominates $|b_\rho|^2$ by $\log T_\rho>2/3$. Alternatively, retain just one logarithm and sum using the shell bound. This gives $C_2-C_{\mathcal F}\le9\cdot10^{14}\sum_{j\ge\lfloor Y\rfloor}(j+2)^{-9/8}\log(j+2)$. For $X\ge3$ the summand function decreases on $[X,\infty)$ and its integral there is $X^{-1/8}(8\log X+64)$. Hence $0\le C_2-C_{\mathcal F}\le A(Y)$.

For the finite set, cut each kernel down to $|t-\gamma_\rho|\le\delta$. The common omitted squared mass in the full kernel satisfies
$$
 Q=\int_{|u|>\delta}|H_L(u)|^2\,\frac{du}{2\pi}\le q
$$
by $|H_L(u)|^2\le4/(Lu^2)$ and its total mass one. Applying the same weighted Cauchy–Schwarz bound to the omitted finite portions $\delta<|t-\gamma_\rho|\le1$ gives squared norm at most $qB(0)$. This accounts for overlap on all the outer regions.

For $|u|\le\delta$, Cauchy's coefficient estimate on radius $R$ gives
$$
 \left|\frac{\zeta(\rho+iu)}{iu}-\zeta'(\rho)\right|
 \le\frac{M_\rho|u|}{R^2(1-|u|/R)}
 \le\frac{2M_\rho|u|}{R^2},\qquad |\zeta'(\rho)|\le M_\rho/R.
$$
Both $\rho$ and $\rho+iu$ have modulus at least $1/2$, so the difference of their reciprocals is at most $4|u|$. With $|r_\rho|\le3m_\rho$ this yields $|a_\rho(\gamma_\rho+u)-b_\rho|\le D_\rho|u|$. The windows are disjoint. Their squared localization errors therefore add, and the contribution at $\rho$ is at most $4\delta D_\rho^2/(\pi L)$ by integration of $u^2|H_L(u)|^2\le4/L$.

The scaled full residual is thus within $\alpha$ in norm of $\sum_{\rho\in\mathcal F}b_\rho\mathbf 1_{|t-\gamma_\rho|\le\delta}H_L(t-\gamma_\rho)$. By disjointness the latter has squared norm $(1-Q)C_{\mathcal F}$. The triangle inequality gives
$$
 \sqrt{(1-q)C_{\mathcal F}}-\alpha
 \le\sqrt{LE_N}\le\sqrt{C_{\mathcal F}}+\alpha,\qquad
 C_{\mathcal F}\le C_2\le C_{\mathcal F}+A(Y).
$$
These imply the two directional inequalities. In particular $\sqrt{LE_N}+\sqrt{C_2}\le 2\sqrt{c_++A(Y)}+\eta$, which proves the squared-error remainder. Rearranging gives the enclosures.

## One evaluated enclosure

At $Y=100$, a 128-bit Arb run returned an exact count of 29 positive zeros below $100+2^{-10}$, 29 disjoint positive critical-line ordinate balls strictly below 100, and nonzero derivative balls at all 29 roots. The count exhausts the positive list and excludes an endpoint zero at 100. Reflection supplies the negative list. There is no real critical zero because $(1-2^{1-s})\zeta(s)$ is the strictly positive alternating eta series at $s=1/2$. The balls and their reflections are separated by more than $1/8$, so $\delta=1/16$ is admissible. The run verifies the outward rational assertions
$$
 0.25253801685456458<C_{\mathcal F}<0.25253801685456460,\qquad
 A(100)<5.102\cdot10^{16}.
$$
In particular under RH, $C_2\in[0.25253801685456458,5.103\cdot10^{16}]$. This enclosure uses the derivative sum and the explicit coefficient tail. It is intentionally coarse. The companion script takes the optional flag --arb to repeat the root, derivative, and bound checks with python-flint 0.9.0 and FLINT 3.6.0.

## Checks

The companion script checks the tail prefactor exactly and exercises both kernel integrals, the local replacement and the norm comparisons on synthetic inputs. Two unit-amplitude untruncated kernels separated by $d$ have real overlap $\sin(Ld)/(Ld)$. Their squared sum tends to $4$ when $Ld\to0$, while the sum of their individual squared norms stays $2$. The multiple-zero fixture has $a_\rho(t)$ vanishing linearly at the center, and the local bound remains valid when $b_\rho=0$. [Reproducible checks](../../scripts/prime64_finite_remainder_checks.py)
