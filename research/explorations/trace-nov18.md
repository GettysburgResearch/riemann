# The odd Möbius trace on rational ratios and common rough parts

**Status.** Proposed component proofs for the native trace in #866. The estimate for the complete signed block and RH remain open.

**Source.** We use the odd Möbius trace, integrated Legendre columns, and common square cutoff of [TC26, §§1–3, frozen at a27285a](https://github.com/GettysburgResearch/riemann/blob/a27285abe428835ac0171fe9eb8cbbc97a64a33a/standalone/2026-09-13-astra-trace-covariance/PROOF.md). Issue [#902, §7](https://github.com/GettysburgResearch/riemann/issues/902) asks for degree-block bounds on specified arithmetic classes with their residuals retained. We evaluate such classes below. Classical inputs are Legendre orthogonality, squarefree counting, the prime number theorem and the prime harmonic sum.

## An integrated column paired with a dilation

Let $l=2j+1$, $\phi_j=\sqrt{2l+1}\,P_l$ and $\psi_j(x)=\int_x^1\phi_j(u)\,du/u$ on $[0,1]$, extended by zero on $[1,\infty)$. Put $b_j=\psi_j(0)$. For $0<r\le 1$,

$$
I_j(r)=\int_0^1\psi_j(x)\psi_j(rx)\,dx
=\frac{2l+1-r^l}{l(l+1)}.
\tag{1}
$$

Indeed, integrate the derivative of $x\psi_j(x)\psi_j(rx)$ over $[0,1]$. The endpoints vanish. This writes $I_j$ as the sum of $\int\phi_j(x)\psi_j(rx)\,dx$ and $\int\psi_j(x)\phi_j(rx)\,dx$. For the first integral subtract from $b_j\int\phi_j$ the projection of the odd polynomial $\int_0^{rx}\phi_j(u)\,du/u$ onto $\phi_j(x)$. Its top coefficient is $r^l/l$ times that of $\phi_j$ and every lower odd degree is orthogonal. The second integral, by reversing the elementary polynomial integrals, is the projection of $u^{-1}\int_0^u\phi_j(rx)\,dx$ onto $\phi_j(u)$, equal to $r^l/(l+1)$. TC26 §1 gives $b_j\int\phi_j=(2l+1)/(l(l+1))$. In particular,

$$
0\le I_j(r)-\frac1{j+1}=\frac{1-r^l}{l(l+1)}\le\frac1{l(l+1)}.
\tag{2}
$$

## Uniform block estimate for a reduced ratio

For odd coprime squarefree $1\le a\le b$, let $T_j(a,b)$ be the **ordered** class in the squared column with $n=ak,m=bk$. Thus it contains the weight $\mu(ak)\mu(bk)/(abk^2)$ times $\int_1^3\psi_j(t/(ak))\psi_j(t/(bk))\,dt$, summed over all positive odd $k$. The $n=1$ term vanishes by the extension at one. Ratios with nonsquarefree numerator or denominator contribute zero. Reverse the arguments to define $T_j(b,a)=T_j(a,b)$. For each class the series converges absolutely. Write

$$
\alpha=4/\pi^2,\quad c_0=\alpha\log3,\qquad
w(d)=\prod_{p\mid d}\frac p{p+1}.
$$

Then with an absolute implied constant, $q=2ab$ and $r=a/b$,

$$
 T_j(a,b)=\frac{c_0\mu(a)\mu(b)w(ab)}{b}I_j(r)
   +O\left(\frac{\tau(q)}{(ab)^{1/4}(j+1)^{6/5}}\right).
\tag{3}
$$

To check the arithmetic, $\mu(ak)\mu(bk)=\mu(a)\mu(b)\mu(k)^2$ when $(k,ab)=1$, and is zero otherwise. For $q=2ab$ the count $A_q(z)=\sum_{k\le z,(k,q)=1}\mu(k)^2$ equals $\alpha w(ab)z+O(\tau(q)\sqrt z)$ for all $z>0$. For $z\ge1$, expand $\mu(k)^2=\sum_{d^2\mid k}\mu(d)$ and count coprime multiples with $\sum_{e\mid q}\mu(e)\lfloor z/(d^2e)\rfloor$ for $(d,q)=1$. Summing the floor errors over $d\le\sqrt z$ and extending the main series gives the stated error and the Euler product $(1/\zeta(2))\prod_{p\mid q}p/(p+1)$. For $z<1$ the bound follows directly. Partial summation gives

$$
\sum_{z<k\le3z,(k,q)=1}\frac{\mu(k)^2}{k}
=\alpha w(ab)\log3+O(\tau(q)/\sqrt z).
$$

Change variables $x=t/(ak)$ in $T_j$. The resulting measure has the last harmonic sum with $z=1/(ax)$, divided by $b$. Endpoints have measure zero. By Cauchy–Schwarz and TC26 §1 equation (5),

$$
\int_0^1\sqrt{x}\,|\psi_j(x)\psi_j(rx)|\,dx
 \le (11/2) r^{-3/4}(j+1)^{-6/5}.
$$

Multiplication by $\sqrt{a}/b$ gives exactly $(ab)^{-1/4}$. This proves (3), including its scale dependence. Each $T_j$ can be deleted from the original common square cutoff by first taking the finite-cutoff difference and then letting that cutoff tend to infinity with the degree block fixed.

## Opposite contributions from specified native classes

Put $h_N=H_{2N}-H_N$ and $B_N=S_{2N}-S_N\ge0$ for the full trace of #866. Let $P_N$ include both orientations of all prime ratios $p\le N^{1/8}$, with $p$ odd, in the degree block $N\le j<2N$. Equations (2)–(3) give

$$
 P_N=-2c_0 h_N\sum_{3\le p\le N^{1/8}}\frac1{p+1}
          +o(1)
     =-2c_0(\log2)\log\log N+O(1).
\tag{4}
$$

The errors from (3) are $O(N^{-1/5}N^{1/8})$ since $\tau(2p)=4$. The errors from (2) are $O(N^{-1}N^{1/8})$. The positive diagonals have block size $c_0h_N+O(N^{-1/5})$ by TC26. Thus the completed off-diagonal remainder *after removal of these prime ratios* is at least $2c_0(\log 2)\log\log N-O(1)$. This conclusion uses only $B_N\ge0$. The common-cutoff remainder can contain cancellation of either sign before completion.

There is a larger family with an arithmetic factorization. For $y\ge3$ let $Q=\prod_{3\le p\le y}p$ and split odd squarefree integers according to their common part supported on primes $>y$. Thus $n=ds$ with $d\mid Q$ and $(s,Q)=1$. Define $G_N(y)$ as the sum of squared degree-block norms within each fixed $s$, before summing over $s$. Explicitly the vector for $s$ has columns $\sum_{d\mid Q}\mu(ds)\psi_j(t/(ds))/(ds)$. This positive quantity is also the sum over precisely the ordered reduced ratios $a/b$ with $a,b\mid Q$ and $(a,b)=1$. Indeed equality of the two rough parts is equivalent to this reduced-ratio condition. There are finitely many ratios for fixed $Q$, and their separate $k$ sums converge absolutely.

Uniformly for $Q\le N^{1/100}$, (2)–(3) yield

$$
 G_N(y)=c_0 h_N L(Q)+O(N^{-1/5}Q^4+N^{-1}Q^2),
 \quad L(Q)=\sum_{a,b\mid Q,(a,b)=1}
 \frac{\mu(a)\mu(b)w(ab)}{\max(a,b)}.
\tag{5}
$$

Indeed there are at most $Q^2$ ordered ratios, each with $\tau(2ab)\le2Q^2$ and $(ab)^{-1/4}\le1$. The replacements in (2) have total cost $O(Q^2/N)$. The crude cutoff suffices here.

The Cauchy density $d\nu(t)=dt/(2\pi(t^2+1/4))$ has Fourier transform $e^{-|u|/2}$. Applying this to $1/\max(a,b)=e^{-|\log(a/b)|/2}/\sqrt{ab}$ gives the exact positive integral

$$
 L(Q)=\int_{\mathbb R}
 \prod_{3\le p\le y}
 \left(1-\frac{2\sqrt p}{p+1}\cos(t\log p)\right)d\nu(t).
\tag{6}
$$

Each prime divides at most one of $a,b$ in the finite expansion, which accounts for all three local terms. For all sufficiently large $y$ this integral is at least $\exp(c\sqrt y/\log y)$ for some absolute $c>0$. Restrict $t$ to $[0.95\pi/\log y,1.05\pi/\log y]$. For $y^{3/4}\le p\le y$ the cosine is bounded above by a fixed negative constant. The primes in $[y/2,y]$ alone contribute $\gg\sqrt y/\log y$ to the log product by the prime number theorem. The smaller primes $p<y^{3/4}$ together cost at most $C\sum_{3\le n<y^{3/4}}n^{-1/2}\ll y^{3/8}$, since $2\sqrt p/(p+1)\le\sqrt3/2<1$. The $\nu$-mass of the restricted interval is $\gg1/\log y$, absorbed by decreasing $c$.

Take $y=(\log N)/300$. For large $N$, $\log Q\le2y$ by the prime number theorem, and the errors in (5) tend to zero. Consequently for an absolute $c'>0$,

$$
 G_N((\log N)/300)
 \ge\exp\left(c'\frac{\sqrt{\log N}}{\log\log N}\right).
\tag{7}
$$

This rules out a polylogarithmic block upper bound after orthogonalizing distinct rough parts at this explicit cutoff. For the full trace the exact decomposition is $B_N=G_N(y)+R_N(y)$, where $R_N(y)$ is the common-cutoff limit of *all* pairs with unequal rough parts. Existence follows by subtracting the absolutely convergent grouped contribution from the full cutoff of TC26. No sign for $R_N(y)$ follows from (7). The lower bound itself is subpower, compatible even with the desired subpower upper bound. A complete native covariance upper bound still requires control of the interactions across different rough parts.

**Verification scope.** The arguments above are analytic. Exact symbolic monomial integration verified (1) for $0\le j\le8$ and $r=1,1/3,9/11$. A separate enumeration of the signed coprime divisor pairs and the three local choices per prime in (6) agreed for the initial sets of one through four odd primes. It gave $1/2,1/2,7/12,191/288$. These 31 finite checks do not verify the asymptotic bounds. No independent mathematical review has been performed.

## A larger prime cutoff and the size of the grouped contribution

The dependence on $Q$ in (5) can be replaced by a substantially smaller elementary product. This gives the sharper native lower bound
$$
\log G_N(y_N)=(4+o(1))\frac{\sqrt{y_N}}{\log y_N},
\qquad y_N=\tfrac1{100}(\log N\log\log N)^{4/3}.
\tag{8}
$$
Indeed (3) summed over all ordered allowable ratios costs at most
$$
C N^{-1/5}\prod_{3\le p\le y}(1+4p^{-1/4}).
$$
Here $\tau(2ab)=2\cdot 2^{\omega(ab)}$ and each prime can go to either argument or neither. Equation (2) costs at most $CN^{-1}\prod_{3\le p\le y}(1+2p^{-1/2})$, using $\max(a,b)\ge\sqrt{ab}$. These bounds only use the finitely many ratios at each $N$. By partial summation of the prime number theorem, for each fixed $0<\delta<1$ one has
$$
 \sum_{p\le y}p^{-\delta}\sim\frac{y^{1-\delta}}{(1-\delta)\log y}.
$$
At $y=y_N$ the log of the first product is at most $(4\cdot100^{-3/4}+o(1))\log N$; the leading coefficient is below $1/5$. The second product is $\exp(o(\log N))$. Thus the summed errors are $o(1)$.

It remains to evaluate (6) to leading exponential order. The upper bound $\log L(Q)\le(4+o(1))\sqrt y/\log y$ follows from $\log(1+u)\le u$. Fix $0<\delta<1/5$ and restrict $t$ to $[(1-\delta)\pi,(1+\delta)\pi]/\log y$. On $p\ge y^{1-\delta}$ one has $-\cos(t\log p)\ge \cos(2\pi\delta)>0$. The quadratic error in expanding the log product there is $O(\sum_{p\le y}1/p)=O(\log\log y)$. The primes below $y^{1-\delta}$ can cost at most $O(y^{(1-\delta)/2})$ in its log, by the same estimate as in (7). The $\nu$-mass of this interval is $\gg_\delta1/\log y$. Consequently the lower limit of $(\log y)\log L(Q)/\sqrt y$ is at least $4\cos(2\pi\delta)$. Letting $\delta$ decrease to zero proves the matching lower bound. Since $c_0h_N$ has a finite positive limit and $L(Q)$ grows without bound, (8) follows. The entire unequal-rough-part remainder is still present in $B_N$.

## Complete cancellation on one divisibility cone

Let $V_N$ denote the contribution of all ordered pairs $n\mid m$ to the degree block $N\le j<2N$, **including the diagonal once**. Both indices use the original common square cutoff before its limit. For every fixed $A>0$,
$$
 V_N=O_A((\log N)^{-A}).
\tag{9}
$$
Thus the complete contribution of distinct comparable pairs in both orientations is $-2(D_{2N}-D_N)+O_A((\log N)^{-A})$. This cancels a specified nonzero piece of the actual native block. It leaves all pairs where neither integer divides the other in the exact remainder.

Here are the uniform tail details. First, the normalized columns satisfy, with $J=j+1$,
$$
 |\psi_j(x)|\ll\min(1,(Jx)^{-1})\quad(0<x\le1/2),\qquad
 \int_0^{1/2}|\phi_j(x)|\,dx/x\ll\log(2J).
\tag{10}
$$
For these estimates, the elementary Laplace integral for the Legendre polynomials gives $|P_l(x)|\ll(l+1)^{-1/2}$ on $|x|\le1/2$ by Gaussian comparison, and $|P_l'(x)|\ll\sqrt{l+1}$ there by differentiation (see [DG26 §2.1 at the same source revision](https://github.com/GettysburgResearch/riemann/blob/a27285abe428835ac0171fe9eb8cbbc97a64a33a/standalone/2026-09-12-astra-polynomial-degree-growth/PROOF.md)). Consequently $|\phi_j(x)|\ll\min(1,Jx)$ by oddness. The primitive $F_j(x)=\int_x^1\phi_j$ is $(P_{l-1}-P_{l+1})/\sqrt{2l+1}$, so it is $O(J^{-1})$ on $|x|\le1/2$; its full $L^2(0,1)$ norm is also $O(J^{-1})$ by TC26 (4). For $x\le1/2$ integrate by parts as $\psi_j=F_j(x)/x-\int_x^1 F_j(u)\,du/u^2$, using the interior bound below $1/2$ and Cauchy–Schwarz above $1/2$. This gives $O((Jx)^{-1})$. For $x<1/J$, instead use $|b_j|=O(1)$ from TC26 (3) and Stirling's formula, and integrate $|\phi_j(u)|/u\ll J$ from zero. This proves (10). It follows that
$$
 \sum_{k\text{ odd}} k^{-2}\int_1^3|\psi_j(t/k)|\,dt
 \ll \frac{\log(2J)}J .
\tag{11}
$$
In fact, $k=1$ vanishes, and $k=3,5$ cost $O(J^{-1})$ by TC26 (2) restricted away from zero. For $k\ge7$, sum $k^{-2}\min(1,k/J)$ using (10).

For $H=N^{1/8}$, $k\le N^3$, and $v\ge H$, classical prime number theorem estimates give
$$
 \left|\sum_{b\le v,(b,2k)=1}\frac{\mu(b)}b\right|
   \ll_A(\log N)^{-A}.
\tag{12}
$$
Indeed the sum is the convolution of $m_{\rm all}(v)=\sum_{n\le v}\mu(n)/n$ with the reciprocal-weighted positive integers supported on primes dividing $2k$. The classical zero-free region and partial summation give $m_{\rm all}(v)\ll_A (\log(2v))^{-A}$ for every fixed $A$. The support weights have total mass $\prod_{p\mid 2k}(1-1/p)^{-1}\ll\log(2k)$ by Mertens. For support indices $d>\sqrt v$, their total mass is at most
$$
 v^{-1/8}\prod_{p\mid2k}(1-p^{-3/4})^{-1}
 \le v^{-1/8}\exp(C(\log(2k))^{1/4}).
$$
To see the last inequality, order the prime factors increasingly. The $i$th is at least $i+1$ and there are at most $\log(2k)/\log 2$. For $d\le\sqrt v$ the arbitrary inverse-log decay absorbs the support mass, proving (12). For general $k$, independent of $v$, the same convolution and boundedness of $m_{\rm all}$ give the elementary bound $O(\log(2k))$.

For a finite common cutoff $R$, put $n=k$, $m=kb$ with $k$ odd squarefree. For each $k$ the sum on $H<b\le R/k$ has inner weight $\mu(b)/b$ with $(b,2k)=1$, multiplied by $\psi_j(t/(kb))$. On this interval the multiplier is $O(1)$ and has total variation $O(\log(2J))$ by (10), since $0<t/(kb)\le3/H\le1/2$ for large $N$. Partial summation and (12) bound this inner sum by $O_A((\log N)^{-A}\log(2J))$ for $k\le N^3$. Multiply by $k^{-2}\mu(k)^2|\psi_j(t/k)|$, integrate, and apply (11). After summing the block, the loss is $O((\log N)^2)$, absorbed by taking $A$ larger in (12). For $k>N^3$ use the general $O(\log(2k))$ bound instead, $|\psi_j(t/k)|\ll1$ and the $k^{-2}$ weight. The cost after summing the block is $O(N^{-2}(\log N)^2)$. These estimates are uniform in $R$. The limit exists for each $j,N$: at each fixed $k$ the inner series converges by partial summation, and the general bound just given yields a summable majorant over $k$. Here and below the complete source limit precedes any limit in $N$.

For $b\le H$, (2)–(3) and both indices tending to the common cutoff give
$$
 c_0h_N\sum_{b\le H,\,b\text{ odd}}\frac{\mu(b)w(b)}b
 +O\left( (N^{-1/5}+N^{-1})H\log(2H)\right).
$$
The sum of $\tau(2b)$ up to $H$ is $O(H\log(2H))$. Finally the odd Dirichlet series for $\mu(b)w(b)$ factors as the series of the odd Möbius function times one with local factors
$$
 1+\frac1{p+1}\sum_{d\ge1}p^{-ds}\quad (p\ge3).
$$
The latter has nonnegative coefficients $h(d)$ and $\sum h(d)d^{-1/2}<\infty$. Splitting its convolution at $d=\sqrt H$ and using (12) with $k=1$ (or directly the odd PNT estimate) shows that the displayed main sum is $O_A((\log H)^{-A})$. This proves (9). As the diagonal block tends to $c_0\log2$, the distinct comparable pairs in both orientations tend to $-2c_0\log2$ and the full comparable class including the diagonal tends to $-c_0\log2$. These signed limits are compatible with $B_N\ge0$ because the incomparable pairs remain.
