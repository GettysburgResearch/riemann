# Logarithmic trace growth is equivalent to the weak Mertens hypothesis

**Status.** Proposed two-sided growth-class adapter and conditional asymptotic. The arithmetic hypothesis in the title is open. The equivalence does not establish it.

Let $m_o(x)=\sum_{n\le x,n\text{ odd}}\mu(n)/n$, let $m_a$ denote the same sum over all positive integers, and let $M(x)=\sum_{n\le x}\mu(n)$. Extend the sums by zero for $x<1$. Use the ordinary odd Legendre trace $S_N=\sum_{j<N}\|K\phi_j\|_{L^2(1,3)}^2$ of [#866](https://github.com/GettysburgResearch/riemann/blob/a27285abe428835ac0171fe9eb8cbbc97a64a33a/standalone/2026-09-12-astra-polynomial-degree-growth/PROOF.md), where $Kp(t)=\int_0^1m_o(t/u)p(u)\,du/u$ on odd polynomials. The classical bound $|m_o|\le2$ suffices below. Define $F_o(X)=\int_1^X |m_o(x)|^2\,dx$.

For every real $X\ge3$ and integer $D\ge X$, with an absolute implied constant,
$$
 (\log3)\int_3^X|m_o(x)|^2\,dx
 \ \le\int_1^3\frac{dt}{t}\int_t^{tX}|m_o(x)|^2\,dx
 \ \le S_D+O(X^2/D).
\tag{1}
$$
Thus an all-degree trace bound transfers back to the genuine reciprocal-Möbius energy. The other direction already has an explicit finite bound in [#869, arithmetic Theorem 4](https://github.com/GettysburgResearch/riemann/blob/5e559c9cbf5aee84ff7ed78dc91b55df744aef56/standalone/2026-09-12-three-route-completion/arithmetic/PROOF.md). Together these show, for every fixed $k\ge0$, the equivalence
$$
 S_N\ll(\log(2N))^k
 \quad\Longleftrightarrow\quad F_o(X)\ll(\log(2X))^k
 \quad\Longleftrightarrow\quad
 \int_1^X |M(x)/x|^2\,dx\ll(\log(2X))^k .
\tag{2}
$$
The quantifiers are all $N$ or all $X$ with a constant independent of cutoff. For $k=1$ the right side is the classical weak Mertens hypothesis. The reverse estimate (1) uses a polynomial scale but incurs only additive error. An $N^{o(1)}$ multiplicative loss alone could erase logarithmic growth information.

## Proof of the reverse estimate

Fix $1<t<3$, put $G_t(u)=\mathbf1_{u\ge1/X}m_o(t/u)/u^2$ on $0\le u\le1$, and put $g_t(u)=uG_t(u)$. Let $H_t(\theta)=G_t(|\cos\theta|)$ on the circle. Uniformly in $t$, $\|G_t\|_\infty\le2X^2$ and the total variation of $H_t$ is $O(X^2)$. In fact the variation of $G_t$ consists of a cutoff jump $O(X^2)$, the smooth derivative bounded in absolute integral by $\int_{1/X}^1 4u^{-3}\,du$, and jumps of size at most $n/t^2$ at $u=t/n$ for $n\le3X$. These sum to $O(X^2)$. Taking the cosine composition traverses $[0,1]$ only four times on the circle.

Convolve $H_t$ with the nonnegative circle kernel $J_D(\theta)$ proportional to $(\sin(D\theta/2)/\sin(\theta/2))^4$, normalized to unit integral. It has trigonometric degree $2D-2$ and, on $|\theta|\le\pi$, satisfies $J_D(\theta)\ll D(1+D|\theta|)^{-4}$. Indeed its unnormalized fourth power is $O(\min(D^4,|\theta|^{-4}))$ and its integral is comparable to $D^3$ by also restricting to $|\theta|\le 1/D$. The result of the convolution is an even, $\pi$-periodic cosine polynomial, hence $P_t(\cos\theta)$ for an even algebraic polynomial of degree at most $2D-2$. Bounded variation gives $\int|H_t(\theta-z)-H_t(\theta)|\,d\theta\le |z|\operatorname{Var}(H_t)$, by integrating the total variation measure over translated arcs. Since $|du|\le d\theta$ on a single traversal, the kernel's first absolute moment yields
$$
 \int_0^1 |P_t(u)-G_t(u)|\,du\ll X^2/D .
\tag{3}
$$
There is also a uniform weighted supremum $u^2|P_t(u)|\ll1$. To check it take $u=\cos\theta\ge0$. For $|z|\le u/2$, $|\cos(\theta-z)|\ge u/2$ and the integrand $|H_t(\theta-z)|\le8/u^2$. For $|z|>u/2$, it costs at most $2X^2$ times kernel mass $O((1+Du)^{-3})$. Multiplying by $u^2$ bounds this contribution by $O(X^2/D^2)$, uniformly bounded by $D\ge X$.

The allowed polynomial $p_t(u)=uP_t(u)$ therefore satisfies
$$
 \|p_t-g_t\|_2^2
 \le\big(\sup_u u^2|P_t-G_t|\big)\int_0^1|P_t-G_t|\,du\ll X^2/D .
$$
On $0<u<1/X$ the pairing with the untruncated singular row is a convergent ordinary integral. Its absolute value is at most $2\int_0^{1/X}|P_t|\,du\ll X^2/D$ by (3), since $G_t$ vanishes there. For each fixed $t$ the finite-dimensional row norm satisfies
$$
 \sum_{j<D}|K\phi_j(t)|^2
 \ge 2\Re (Kp_t)(t)-\|p_t\|_2^2
 \ge \|g_t\|_2^2-O(X^2/D).
$$
The family $p_t$ is chosen only for this rowwise variational inequality; no common optimizer across different $t$ is assumed. Integrate in $t$ and put $x=t/u$ to obtain (1). The left inequality there follows from $[3,X]\subset[t,tX]$ throughout the output interval.

## The three growth classes

Use $D=\lceil X^2\rceil$ in (1) for the trace-to-source direction. For the converse, the proof of #869 Theorem 4 above its equation (5.6) gives for every $Y\ge2$, $N\ge2$,
$$
 \sqrt{S_N}\le\sqrt{(\log3)F_o(3Y)}
                 +18\sqrt2\,(2N-1)^{3/2}/Y .
$$
Taking $Y=(2N)^{3/2}$ gives the required growth bound. The identities $m_a(x)=m_o(x)-\tfrac12 m_o(x/2)$ and $m_o(x)=\sum_{j\ge0}2^{-j}m_a(x/2^j)$ show that the bound on $F_o$ is equivalent to the corresponding all-integer bound. In the reverse sum Minkowski costs only the convergent geometric factor $\sum_j 2^{-j/2}$ after dilation in $L^2(0,X)$.

For the last conversion write $f(x)=M(x)/x$. Partial summation gives
$$
 f(x)=m_a(x)-x^{-1}\int_1^x m_a(u)\,du,\qquad
 m_a(x)=f(x)-\int_x^\infty f(u)\,du/u .
$$
For the second identity use the classical PNT bound $M(u)\ll_A u/(\log(2u))^A$, the limit $m_a(\infty)=0$ and partial summation. On $[1,X]$ the forward and adjoint Hardy operators truncated to this interval have $L^2$ norm at most two (by extension by zero to the positive half-line and the classical Hardy inequality). Only the constant tail in the second identity needs payment beyond $X$. If $\int_1^Y |f|^2\ll(\log(2Y))^k$ at every $Y$, Cauchy–Schwarz on successive $[2^i X,2^{i+1}X]$ bounds the tail by $O_k(X^{-1/2}(\log(2X))^{k/2})$ after summing a geometrically convergent series. Its squared $L^2(1,X)$ contribution is $O_k((\log(2X))^k)$. This proves (2).

## A leading coefficient under a stronger source hypothesis

If $L=\limsup_{X\to\infty}F_o(X)/\log X<\infty$, then
$$
 \limsup_{N\to\infty} S_N/\log N\le (\log3)L.
\tag{4}
$$
Indeed truncate the input at $u=1/Y$ for $Y=N^{1+\epsilon}$ with fixed $\epsilon>0$. The high-input Hilbert–Schmidt norm is at most $\sqrt{(\log3)F_o(3Y)}$. On the low input the projection row norm $(\sum_{j<N}|\phi_j(u)|^2)^{1/2}$ is $O(N^{3/2}u)$ by DG26 (2.5), and $\int_1^3 |m_o(t/u)|^2dt\le u F_o(3/u)\ll u\log(3/u)$. Minkowski for the rank-one integral bounds its Hilbert–Schmidt norm by $O(N^{3/2}Y^{-3/2}\sqrt{\log(3Y)})=o(1)$. Divide by $\sqrt{\log N}$ and let $\epsilon\downarrow0$. This proves (4). Conversely (1) always gives $\limsup S_N/\log N\ge (\log3)L/2$ with the same $L$.

One sufficient source hypothesis for an exact coefficient is that $L$ equals the finite sum of squared reciprocal leading coefficients $\sum_{\rho}|(\rho-1)(1-2^{-\rho})\zeta'(\rho)|^{-2}$ over simple critical zeros (the sum may have infinitely many terms). In that case (4) and [the simultaneous critical-zero lower bound](trace-zero-residues-nov18.md) force $S_N/\log N\to(\log3)L$. Identifying $L$ with that sum is an additional arithmetic condition. A weak-Mertens upper bound alone gives only boundedness of the normalized energies here.

**Verification scope.** The proof is analytic. The cutoff row is constructed using the full primitive odd Möbius source through $3X$ and the uniform $|m_o|\le2$ bound for the part below the cutoff. The finite-scale estimate retains that origin cost. No power saving or effective numerical value of $L$ is established.

## Matching full upper bound from the necessary residue sum

**Proposed spectral converse.** Suppose RH holds, all nontrivial zeros are simple, and
$$
 B=\sum_{\rho}\frac1{|\rho\zeta'(\rho)|^2}<\infty.
\tag{5}
$$
Then
$$
 \frac1{\log X}\int_1^X|M(x)/x|^2\,dx\ \longrightarrow B,
 \qquad
 \frac{F_o(X)}{\log X}\ \longrightarrow B_o,\qquad
 \frac{S_N}{\log N}\ \longrightarrow(\log3) B_o,
\tag{6}
$$
where $B_o=\sum_{\rho}|(\rho-1)(1-2^{-\rho})\zeta'(\rho)|^{-2}$. All sums count both signs of the ordinates. On RH the factors $|\rho-1|=|\rho|$ and $1-2^{-1/2}\le |1-2^{-\rho}|\le1+2^{-1/2}$ give equivalent convergence.

Conversely, the weak Mertens bound implies RH, simplicity and (5) by the classical theorem of Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Chapter XIV, pp. 376–380. Thus (2), (5) together with its zero hypotheses, and the respective asymptotics (6) at finite coefficients yield the same logarithmic upper-bound threshold. The conjectural zero hypotheses and the convergence in (5) have not been proved. Ng's Theorem 3 obtains the first asymptotic under RH and $J_{-1}(T)=\sum_{0<\gamma\le T}|\zeta'(\rho)|^{-2}\ll T$. Meng's Theorem 6 subsequently obtained the weak Mertens bound and the same ordinary asymptotic under $J_{-1}(T)\ll T^{2-\delta}$ for fixed $\delta>0$. The argument below uses the necessary weighted sum directly, including growth for which no fixed $\delta$ power saving holds. It does not assert worldwide priority for a converse. [Ng, Theorems 1–3 and discussion of the classical necessity](https://arxiv.org/abs/math/0310381) · [Meng, Theorem 6](https://arxiv.org/abs/1408.0429) · [Bui–Florea–Milinovich §1.2 on the same necessity](https://arxiv.org/abs/2310.03949)

Iksanov, Kabluchko and Marynych construct a Besicovitch almost-periodic residue process under RH and the same square summability in (5). Identifying its mean-square expansion with the ordinary summatory Möbius function on growing logarithmic intervals is the additional transfer used here. [Iksanov–Kabluchko–Marynych, §4.2, Proposition 4.4](https://do.csc.knu.ua/iksan/wp-content/uploads/sites/3/2025/03/KabIksMar140325_final.pdf)

### Two adjacent zeros control the reciprocal

Write $\xi(s)=h(s)\zeta(s)$ with $h(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/2$, and $\Xi(z)=\xi(1/2+iz)$. On RH its even Hadamard product is $\Xi(0)\prod_{\gamma>0}(1-z^2/\gamma^2)$, locally uniformly convergent. Here $\Xi(0)\ne0$. Let $a<b$ be adjacent real zeros and $Q(z)=\Xi(z)/((z-a)(z-b))$. Then $\log|Q(x)|$ is concave on $[a,b]$ and $|Q(x+iy)|\ge|Q(x)|$ there. Indeed each finite product containing $a,b$ has these properties after the two factors are removed: all its other roots are real and outside $(a,b)$, and each linear factor increases in modulus on vertical displacement. Pass to the limit using simplicity at the endpoints.

For $a\le x\le b$, $z=x+iy$, and $z$ distinct from the endpoints, this implies
$$
 \frac1{|\Xi(z)|}\le
 \frac1{|\Xi'(a)|\,|z-a|}+\frac1{|\Xi'(b)|\,|z-b|}.
\tag{7}
$$
In fact write $\lambda=(x-a)/(b-a)$. After multiplying the right side by $|\Xi(z)|$ it is at least
$$
 (1-\lambda)\frac{|Q(x)|}{|Q(a)|}
       +\lambda\frac{|Q(x)|}{|Q(b)|}\ge1
$$
by weighted AM–GM and log concavity. The endpoint statements follow by continuity for $y\ne0$. The estimate accounts for the complete product outside the adjacent zeros; it charges at most two reciprocal derivatives at any ordinate.

### Uniformly localizing the Laplace transform

Work in either of two cases. Put the physical function $g(u)$ equal to $e^{-u/2}M(e^u)$ in the ordinary case and to $e^{u/2}m_o(e^u)$ in the odd case, with $g=0$ for $u<0$. Its Laplace transform $G(z)$, with $s=1/2+z$, respectively equals
$$
 G(z)=\frac1{s\zeta(s)}
 \quad\hbox{or}\quad
 G(z)=\frac1{(s-1)(1-2^{-s})\zeta(s)}.
$$
Direct summation proves this for $\Re z>1/2$. The classical Littlewood implication under RH gives $M(x)\ll_\delta x^{1/2+\delta}$ for every $\delta>0$. Partial summation using $\sum\mu(n)/n=0$, followed by the odd powers-of-two convolution above, gives $m_o(x)\ll_\delta x^{-1/2+\delta}$ for $0<\delta<1/2$. Hence the Laplace integral is absolutely convergent for $\Re z>0$, with the same identities by continuation. The residues $c_\gamma$ at $z=i\gamma$ are respectively $1/(\rho\zeta'(\rho))$ and $1/((\rho-1)(1-2^{-\rho})\zeta'(\rho))$.

For $0<\epsilon\le1/4$, let $a\le t\le b$ bracket $t$ by consecutive critical ordinates. Uniformly in $t,\epsilon$,
$$
 |G(\epsilon+it)|^2\le C(2+|t|)^\epsilon
 \sum_{\gamma\in\{a,b\}}\frac{|c_\gamma|^2}{(t-\gamma)^2+\epsilon^2}.
\tag{8}
$$
To see the weight, write $G(z)=H(s)/\xi(s)$ with $H=h/s$ or $h/((s-1)(1-2^{-s}))$. The distance between successive ordinates is bounded by an absolute constant under RH: the Riemann–von Mangoldt formula with error $O(\log(2+T))$ puts a zero in every sufficiently high interval $[T,T+C_0]$ for a sufficiently large fixed $C_0$. Enlarge the bound for the finite central region. For $\gamma=a,b$, Stirling's formula thus gives
$$
 |H(1/2+\epsilon+it)/H(1/2+i\gamma)|
       \ll (2+|t|)^{\epsilon/2}.
$$
Both elementary denominator factors have uniformly bounded ratios in this positive-real-part strip at large heights. On compact ranges simplify $h/(s-1)$ before evaluation, and use the fact that $s=0,1$ are outside $1/2\le\Re s\le3/4$. Now apply (7) at the complex coordinate $t-i\epsilon$, using $|c_\gamma|=|H(\rho)|/|\Xi'(\gamma)|$, and square.

### The fine Gaussian removes the gamma-factor loss on the required horizon

For $R\to\infty$, set $T=e^R$, $\epsilon=1/R$, and let $k_T(v)=T e^{-T^2v^2/4}/(2\sqrt\pi)$. Its bilateral Laplace transform is $e^{z^2/T^2}$. The fine smoothing satisfies
$$
 \int_0^R |g(u)-(k_T*g)(u)|^2\,du=O(1).
\tag{9}
$$
Indeed for $u\ge0$, $|v|\le1$, the integer count between $e^{u-v}$ and $e^u$ is at most $O(e^u|v|+1)$. Using $|M(x)|\le x$, $|m_o(x)|\le2$ and the reciprocal weight of each jump in the odd case gives in either case
$$
 |g(u-v)-g(u)|\ll e^{u/2}|v|+e^{-u/2}.
$$
This includes crossing $u=0$ by increasing the absolute constant. For $|v|>1$ the crude $|g(u-v)|+|g(u)|\ll e^{(u+|v|)/2}$ suffices with the Gaussian. Thus the convolution error is $O(e^{u/2}/T+e^{-u/2})$ for $0\le u\le R$, giving (9).

The bilateral Plancherel identity on $\Re z=\epsilon$ applies to the smoothed function, since $e^{-\epsilon u}g(u)$ is in $L^1\cap L^2$ by the RH growth estimate and the exponentially tilted Gaussian is integrable. Its right side is
$$
 \frac1{2\pi}\int_{\mathbb R}e^{2(\epsilon^2-t^2)/T^2}
                                |G(\epsilon+it)|^2\,dt .
$$
The weight in (8) is harmless here: uniformly in $t$,
$e^{-2t^2/T^2}(2+|t|)^\epsilon\ll T^\epsilon=e$.
Each ordinate can occur only on the two adjacent intervals. Integrating its Cauchy kernel there costs at most $\pi/\epsilon$. Therefore the displayed integral is $O(\epsilon^{-1}\sum |c_\gamma|^2)$. On $[0,R]$ the Laplace weight $e^{-2\epsilon u}$ is at least $e^{-2}$. Together with (9) this already proves the full logarithmic upper bound.

For the sharp coefficient choose $V>0$ away from every ordinate. Put $g_V(u)=\mathbf 1_{u\ge0}\sum_{|\gamma|<V}c_\gamma e^{i\gamma u}$ and $G_V(z)=\sum_{|\gamma|<V}c_\gamma/(z-i\gamma)$. The finite trigonometric sum obeys the smoothing approximation (9) with an $O_V(1)$ bound, by its bounded derivative away from zero and its single bounded jump there. In Plancherel for $g-g_V$, the integral at $|t|\le V$ is $O_V(1)$ as $\epsilon\downarrow0$, since $G-G_V$ extends holomorphically across that compact segment. At $|t|>V$ the rational $G_V$ has an $O_V(1)$ squared integral even without smoothing, since all its poles are separated from that region. When using (8) there, any adjacent ordinate from inside $[-V,V]$ also costs only $O_V(1)$ since the Cauchy kernel is separated from its center. All remaining ordinates are bounded with the same absolute constant in (8). Hence
$$
 \limsup_{R\to\infty}\frac1R\int_0^R |g(u)-g_V(u)|^2\,du
       \le C'\sum_{|\gamma|>V}|c_\gamma|^2
$$
with $C'$ independent of $V$. The squared mean of the finite trigonometric sum tends to $\sum_{|\gamma|<V}|c_\gamma|^2$ by elementary orthogonality in the growing interval. Let $V\to\infty$ and use the triangle inequality in mean square. In the ordinary and odd cases, changing $x=e^u$ proves the first two limits in (6). The third follows from (4) and the critical-residue lower bound. This proves a matching upper estimate for the complete signed trace under precisely the stated spectral assumptions.

### Bounded multiplicities and higher logarithmic orders

There is also an upper bound that allows multiple zeros. Assume RH, fix $m\ge1$, and suppose the multiplicity $r_\gamma$ of every zero is at most $m$. In either of the preceding two cases, write $c_{\gamma,r_\gamma}=\lim_{z\to i\gamma}(z-i\gamma)^{r_\gamma}G(z)$ for the leading Laurent coefficient. Assume for each $1\le r\le m$ that
$$
 A_r(T)=\sum_{|\gamma|\le T,\ r_\gamma=r}|c_{\gamma,r}|^2
       =O\big((\log(2+T))^{2(m-r)}\big)
\tag{10}
$$
where each distinct ordinate is used once. Then the corresponding complete physical energy is $O((\log X)^{2m-1})$ and the odd trace is $O((\log N)^{2m-1})$. The hypotheses in the ordinary and odd cases are equivalent because the leading coefficients differ by a uniformly bounded invertible factor on the critical line.

If for $r<m$ the bound in (10) is little-oh instead, then
$$
 \lim_{R\to\infty}R^{1-2m}\int_0^R |g(u)|^2\,du
       =\frac{\sum_{\gamma:r_\gamma=m}|c_{\gamma,m}|^2}
                     {(2m-1)((m-1)!)^2}.
\tag{11}
$$
For the odd source the trace normalized by $(\log N)^{2m-1}$ tends to $\log3$ times this coefficient. In particular a finite polylogarithmic upper bound places restrictions on multiplicities even when RH is assumed; unbounded multiplicities would make every fixed logarithmic power too small by [the lower bound](trace-zero-residues-nov18.md).

To verify the change to (7), let the adjacent distinct zeros $a,b$ have orders $r,s\le m$. Remove all factors at both endpoints in $Q$. Write $d_a=\lim_{z\to a}(z-a)^r/\Xi(z)$ and $d_b=\lim_{z\to b}(z-b)^s/\Xi(z)$. The same product proof gives
$$
 1/|\Xi(z)|\le 2^{m-1}\left(|d_a|/|z-a|^r+|d_b|/|z-b|^s\right).
$$
Indeed, with $q=|Q(b)|/|Q(a)|$, multiplying the right side without its factor $2^{m-1}$ by $|\Xi(z)|$ gives at least $(1-\lambda)^s q^\lambda+\lambda^r q^{-(1-\lambda)}$. This is at least the sum of the $m$th powers of $(1-\lambda)q^{\lambda/m}$ and $\lambda q^{-(1-\lambda)/m}$. Those two positive numbers sum to at least one by weighted AM–GM, giving the result by convexity. Thus (8) holds with denominators $((t-\gamma)^2+\epsilon^2)^{r_\gamma}$ and constant depending on $m$. The gap bound still follows from the Riemann–von Mangoldt count with multiplicities.

Keep half of the Gaussian decay in Plancherel. For adjacent $t,\gamma$,
$$
 e^{-2t^2/T^2}(2+|t|)^\epsilon
      \ll T^\epsilon e^{-\gamma^2/(2T^2)} .
$$
The Cauchy kernel to power $r$ integrates to $O_r(\epsilon^{1-2r})$. Hypothesis (10), by summing over dyadic height shells beyond $T$, gives $\sum_{r_\gamma=r}e^{-\gamma^2/(2T^2)} |c_{\gamma,r}|^2=O((\log(2+T))^{2(m-r)})$, or the corresponding little-oh when assumed. At $T=e^R$, $\epsilon=1/R$, this proves the stated big-oh bound for the smoothed and unsmoothed energies. In the little-oh case truncate at a fixed $V$ as above, subtracting the full principal part at each retained pole: its inverse Laplace transform is the exponential times $\sum_{k=1}^{r_\gamma}c_{\gamma,k}u^{k-1}/(k-1)!$ on $u\ge0$. Its smoothing error on $[0,R]$ is $O_V(1)+O_V(R^{2m}/T^2)$ in squared norm by differentiating the finite polynomial sum away from its jump. The order-$m$ tail after normalization costs at most a constant times $\sum_{|\gamma|>V,r_\gamma=m}|c_{\gamma,m}|^2$, and lower-order tails tend to zero. Only order-$m$ leading terms contribute to the normalized mean of the finite sum, giving (11) by the integral of $u^{2m-2}$ and integration by parts in the oscillating cross terms. Finally the input cutoff in (4) applies with any fixed power of $\log X$ in place of the first: its low-input bound becomes $O(N^{-3\epsilon/2}(\log N)^{m-1/2})$ for fixed cutoff slack $\epsilon>0$. The matching trace lower bound is (1) of the linked critical-residue note.

### Which ordinates can obstruct the sum

Assume RH and simplicity. For any fixed $c>0$, the part of (5) from ordinates $\gamma\in(T,2T]$ at distance at least $c/\log T$ from all other ordinates costs $O_{c,\delta}(T^{-1/2+\delta})$ on that dyadic interval. Indeed Bui–Florea–Milinovich Theorem 1.1 with $k=1$ bounds the corresponding unweighted sum of $|\zeta'(\rho)|^{-2}$ by $O_{c,\delta}(T^{3/2+\delta})$. Dyadic summation with $0<\delta<1/2$ pays this entire class. Thus testing the weighted residue criterion only requires the complementary close ordinates for any fixed choice of $c$. Their relative density alone cannot pay arbitrarily small derivatives. [Bui–Florea–Milinovich, Theorem 1.1](https://arxiv.org/abs/2310.03949)

One can quantify the remaining obstruction using only local zero locations, up to $T^{o(1)}$ factors. Write $d=1/\log\log T$, $T<\gamma\le2T$, and
$$
 C_T(\gamma)=\sum_{0<|\gamma-\gamma'|<d}
                      \log\frac{d}{|\gamma-\gamma'|}.
$$
Then uniformly at all these simple zeros,
$$
 \log\frac1{|\zeta'(1/2+i\gamma)|}=C_T(\gamma)+o(\log T).
\tag{12}
$$
In particular a power margin $\sum_{T<\gamma\le2T}e^{2C_T(\gamma)}\ll T^{2-\eta}$ for some fixed $\eta>0$ suffices for (5) and (6), and growth at least $T^{2+\eta}$ on an unbounded subsequence precludes the weak Mertens bound. Equation (12) by itself does not decide a borderline logarithmic growth rate.

For a proof, the Hadamard product at $t=\gamma$ gives the exact identity
$$
 \log\frac{|\Xi(\gamma-id)|}{d|\Xi'(\gamma)|}
   =\tfrac12\sum_{\gamma'\ne\gamma}\log(1+d^2/(\gamma-\gamma')^2).
$$
The terms from distances less than $d$ are $C_T(\gamma)+O(\log T/\log\log T)$: the error per term is bounded and the RH counting formula with Littlewood's $S(t)=O(\log t/\log\log t)$ gives $O(\log T/\log\log T)$ such neighbors. For the rest use dyadic distances $h\le|\gamma-\gamma'|<2h$ from $d$ to $T/4$. Each contains $O(h\log T+\log T/\log\log T)$ ordinates and each term costs $O(d^2/h^2)$. The sum is $O(d\log T+\log T/\log\log T)$. The far tail is $O(d^2\log T/T)$ by the global zero-count bound. Stirling changes the gamma factors at $\gamma$ and $\gamma-id$ by $O(d\log T)=o(\log T)$. Also $\log d=o(\log T)$.

For completeness, the needed $\log|\zeta(1/2+d+i\gamma)|=o(\log T)$ uniformly follows from the same product and Littlewood counting estimate. Compare $\Xi(\gamma-id)$ with $\Xi(\gamma-i)$, using the weight $h_d(v)=\tfrac12\log((v^2+1)/(v^2+d^2))$. On $|v|\le T/4$, replace the zero count by density $(2\pi)^{-1}\log((\gamma+v)/(2\pi))$ with error $O((\log T/\log\log T)\log(1/d))=o(\log T)$ by integration by parts, since the total variation of $h_d$ is $2\log(1/d)$. Replacing the density by $(2\pi)^{-1}\log(\gamma/(2\pi))$ costs $O(1)$ because the log ratio is bounded and $\int_{\mathbb R}h_d(v)\,dv=\pi(1-d)$. The distant tails of the sum and this constant-density integral are $O(\log T/T)$ using $h_d(v)\ll v^{-2}$. Thus the log ratio of the two $\Xi$ moduli equals $(1-d)\log(\gamma/(2\pi))/2+o(\log T)$, which is precisely canceled by the gamma ratio in the comparison of zeta moduli. The remaining $\zeta(3/2+i\gamma)$ is bounded above and below by its absolutely convergent Euler product. This completes (12). The comparison is related to the shifted-value formula in equation (2.1) of Bui–Florea–Milinovich; the present choice of $d$ retains an explicit logarithmic cost for all neighbors.
