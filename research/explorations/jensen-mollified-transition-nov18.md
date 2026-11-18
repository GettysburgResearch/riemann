# A multiplicatively mollified transition bound for Jensen roots

Let $J_d$ denote the unshifted even Jensen polynomial of the Riemann $\xi$ function. With distinct roots counted once, the preceding [mean transition argument](jensen-mean-transition-nov18.md) sharpens to
$$
 d-\#\{x<0:J_d(x)=0\}\ \ll\sqrt{d\log\log d}.
 \tag{1}
$$
This proposed unconditional bound uses Ono's bulk oscillatory formula and D. H. J. Polymath's heat approximation through exactly the normalization and phase matching in the linked note. The new step is a mollified estimate in the range of small effective real-part shifts.

## The local arithmetic estimates

As in the preceding note let $U\asymp\sqrt{d/\log d}$ be Ono's matching frequency, $L=\log U$, and let $Y\le U$ with $I=[Y,2Y]$ inside the transition region. Write
$$
 h=\min_{y\in I}2\tau(y)\Re\alpha(1/2+iy),\quad
 u(y)=1/2+iy+2\tau(y)\alpha(1/2+iy),\qquad \tau(y)=y^2/(8d).
$$
For the intervals below, $h\asymp Y^2L/d$, $\log y=L+O(\log L)$, and $\tau_{\max}=\max_I\tau\asymp h/L$. Assume $hL\ge C_0\log L$ for a sufficiently large absolute constant and $h=O(1)$. Choose $K=\lfloor Y^\kappa\rfloor$ with a sufficiently small fixed $\kappa>0$ that $2\tau_{\max}\log K\le h/4$ for large $d$. The true heat amplitude and two ordinary polynomials are
$$
 A=\sum_{k\le N(y)}e^{\tau\log^2 k} k^{-u(y)},\quad
 S=\sum_{k\le K}k^{-u(y)},\quad B=\sum_{k\le K}\mu(k)k^{-u(y)}.
$$
In the normalized quadratic mean on $I$ we have
$$
 \|AB-1\|_2\ll (hL)^{-1/2},\qquad
 \|SB-1\|_2+\|(SB)'\|_2\ll L^{-10},\qquad
 \|SB'\|_2\ll h^{-1},\qquad
 \|B\|_2\ll h^{-1/2}+1 .
 \tag{2}
$$
Constants can depend on the fixed upper bound for $h$.

To check near-orthogonality one may use (8) of the preceding note with distinct majorants for diagonal terms and total variation. If the length is $N_0\le Y^{2/3}$ and $E_k$ bounds the supremum and $L^{-C}$ times the total variation of the $k$th coefficient after removing $k^{-iy}$, the off-diagonal contribution to the squared normalized mean is $O(N_0L^{C+1}Y^{-1}\sum E_k^2)$. For all four estimates in (2) one can use
$$
 E_k\ll (1+\log k)^2 d(k) k^{-1/2-b h}
$$
for a fixed sufficiently small $b>0$, where $d(k)$ counts divisors. Indeed each Dirichlet convolution term has absolute weight at most $k^{-1/2-bh}$ because $\tau(y)\log N(y)\le(\Re u(y)-1/2)/2+o(h)$ and differentiating a smooth coefficient after removing $k^{-iy}$ costs at most $O(L^C/Y)$ times its absolute majorant. For the differentiated products one first differentiates with the phase $k^{-iy}$ present, which costs at most powers of $\log k$; variation of the remaining factor again costs $O(L^C/Y)$. A moving cutoff on a divisor contributes at most one jump per divisor. Since $\sum_{k\le x}d(k)^2\ll x\log^3(2x)$, the sum $\sum E_k^2$ is polynomial in $L$. Every off-diagonal contribution is therefore negligible. Diagonal contributions with $k>K$ are likewise $O(L^{-30})$ upon enlarging $C_0$, since $h\log K\gg C_0\log L$. These statements also apply to the $k>K$ terms when the product length is $K N(y)$, which is $O(Y^{2/3})$.

On $k\le K$, the product $SB$ has just its constant term, and the coefficients of $SB'$ before the common weight are $u'(y)\Lambda(k)$, since $\sum_{m|k}\mu(m)\log m=-\Lambda(k)$ for $k\ge2$. We have $|u'|\ll1$ and $\sum_{k\ge1}\Lambda(k)^2 k^{-1-2h}\ll1+h^{-2}$ by Chebyshev's bound and partial summation. For $B$ the ordinary square sum is $\ll1+h^{-1}$. These estimates prove the last three claims in (2).

For $AB$, the multiplier before $k^{-u(y)}$ on $k\le K$ is $\mathbb E C_k(V)$, where $V$ is a real centered normal of variance $2\tau(y)$ and
$$
 C_k(v)=\sum_{m|k}\mu(m)(k/m)^v
 =\prod_{p^j\Vert k}p^{(j-1)v}(p^v-1).
$$
The constant coefficient is one. On $|V|>h/2$, use $|C_k(V)|\le d(k)\max(1,k^V)$. Exponential tilting of the Gaussian by $k^V$ shifts its mean by $2\tau(y)\log k\le h/4$. Hence this part of the expectation is $\ll d(k)e^{\tau\log^2 k}e^{-c hL}$; its weighted square sum is negligible by our choice of $C_0$. On $|V|\le h/2$ couple $V=\sqrt{2\tau(y)}Z$ with one standard real Gaussian $Z$ and put $w=\min(\sqrt{2\tau_{\max}}|Z|,h/2)$. The prime-factor formula gives $|C_k(V)|\le C_k(w)$ on the retained event, because its absolute prime factors increase when $v$ is replaced by $|v|$ and then increased. For $0\le w\le h/2$,
$$
 \sum_{k\ge1}C_k(w)^2 k^{-1-2h}
 =\prod_p\left(1+\frac{(1-p^{-w})^2}{p^{1+2(h-w)}-1}\right)
 \le\exp(Cw^2/h^2).
$$
Indeed $1-p^{-w}\le w\log p$, and $\sum_p(\log p)^2p^{-1-h}\ll1+h^{-2}$. After subtracting the $k=1$ term, the square sum is $O(w^2/h^2)$ uniformly here. Minkowski's inequality now gives an $\ell^2$ bound on the diagonal majorants $\{k^{-1/2-h}\mathbb E C_k(w)\}_{k\ge2}$ of size $O(\mathbb E w/h)\ll(hL)^{-1/2}$. This proves the first bound of (2), with an actual coefficientwise majorant valid for every $y$.

## Sign changes after mollification

Partition $I$ into chunks of length $\ell=(h^2/L)^{1/3}$, with a possible incomplete chunk at the end. Apart from a fraction $O(L^{-10})$ of the length, the full chunks satisfy $|SB-1|\le1/2$ everywhere. In fact, if the supremum on a chunk exceeds $1/2$, either its mean square exceeds a fixed constant or its oscillation exceeds $1/4$; the fraction lost is $O(\|SB-1\|_2^2+\ell^2\|(SB)'\|_2^2)$. On the good chunks $B$ never vanishes and $|(\arg B)'|\le 2|SB'|$. Discard the chunks with total variation of $\arg B$ greater than $1/10$. By Cauchy–Schwarz and (2), this costs a fraction $O(\ell^2/h^2)=O((hL)^{-2/3})$.

On each remaining chunk freeze $\arg B$ at its midpoint. The real sign of $P_d(y)$ is tested after multiplication by the positive factor $|B|/(8|M|)$, where $M$ is the heat gamma factor. Equation (4) of the preceding note yields
$$
 \frac{|B|P_d}{8|M|}=
 2\Re\{e^{i(\phi-\arg B)}AB\}+O(Y^{-1/5}|B|).
$$
The error follows from the uniform real-axis error estimates there, absorbing logarithms. Around consecutive multiples of $\pi$ of the frozen phase, use disjoint arcs of angular half-width $\pi/6$. Boundary losses per chunk give a relative cost $O((\ell L)^{-1})=O((hL)^{-2/3})$. If no point on a full arc has the expected sign, then $|AB-1|+Y^{-1/5}|B|\gg1$ everywhere on it. By (2) such arcs constitute a fraction $O((hL)^{-1})$. The true phase derivative of the carrier is $L/2+O(\log L)$, so the number of distinct sign-changing roots on $I$ is at least
$$
 \frac{YL}{2\pi}-O\big(YL(hL)^{-2/3}+Y\log L+1\big).
 \tag{3}
$$

Sum over disjoint dyadic intervals descending from $U$, stopping at $Y_0\asymp\sqrt{d\log L}/L$ with a large fixed lower constant so $hL\ge C_0\log L$. The unfilled lower interval costs $O(Y_0 L)=O(\sqrt{d\log L})$ reference oscillations. Since $hL\asymp Y^2L^2/d$, the sum of the first errors in (3) is $O(d^{2/3}L^{-1/3}Y_0^{-1/3})=O(\sqrt d\,(\log L)^{-1/6})$. The other local errors total $O(U\log L)$. The previous note's phase matching has error $O(U)$, plus Ono's other endpoint $O(d^{1/4}(\log d)^{3/4})$. These are all $O(\sqrt{d\log L})$, proving (1).

The remaining logarithmic factor here comes from taking $h\log K$ large enough to absorb polynomial-in-$L$ errors in the truncated Möbius product. There is no assertion of full hyperbolicity.
