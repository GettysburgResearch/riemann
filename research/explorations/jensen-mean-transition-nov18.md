# Filling the small-root edge in Ono's Jensen polynomial count

**Status.** Proposed unconditional refinement for the Riemann zeta function. Write $J_d(x)=\sum_{k\le d}\binom dk\gamma(k)x^k$ for the classical unshifted polynomial, where $\xi(1/2+w)=\sum_{k\ge0}\gamma(k)w^{2k}/k!$. Then
$$
 \#\{x<0:J_d(x)=0\}\ \ge\ d-o\big(\sqrt{d\log d}\big).
 \tag{1}
$$
Roots on the left are counted without multiplicity. Ono's October 2026 preprint proves $d-O(\sqrt{d\log d})$ for Dedekind zeta functions, including the Riemann case, and his bulk count is an input here. The added argument recovers the main part of his small-root endpoint loss on average. The little-oh is ineffective in this presentation. [Ono](https://arxiv.org/abs/2610.38870)

## Transition estimate

Set $P_d(y)=J_d(-y^2/d)$ and let $U\asymp\sqrt{d/\log d}$. Fix $0<a<b<\infty$. There are at least
$$
 (b-a-o(1))\,\frac{U\log U}{2\pi}
 \tag{2}
$$
distinct roots of $P_d$ in $[aU,bU]$. The implicit thresholds may depend on $a,b$ and the constants in $U\asymp\sqrt{d/\log d}$.

For real $y$ in this band put
$$
 \tau=\frac{y^2}{8d},\quad s=\tfrac12+iy,\quad
 \alpha(s)=\frac1{2s}+\frac1{s-1}+\tfrac12\log(s/(2\pi)),\quad
 c(y)=2\tau\Re\alpha(s).
$$
There exist fixed $0<c_-<c_+<\infty$ with $c_-\le c(y)\le c_+$, and $\tau=O(1/\log U)$. In the notation of Polymath's equations (8)–(10), let $M=M_{4\tau}(s)=M_0(s)\exp(\tau\alpha(s)^2)$, and write $\phi(y)=\arg M$ continuously. Uniformly,
$$
 \phi'(y)=\tfrac12\log(y/(2\pi))+O((\log U)/U).
 \tag{3}
$$
Indeed $(\log M_0)'=\alpha$, $\alpha'=O(1/U)$, and $\tau'=2\tau/y$; the imaginary part of $\alpha^2$ is $O(\log U)$. Stirling gives the amplitude used in the [complex-box heat comparison](jensen-heat-nov18.md). That comparison (1), applied at $T=y$ pointwise, and the real-axis case of Polymath's Theorem 1.3 give
$$
 \frac{P_d(y)}{8|M|}=2\Re\{e^{i\phi(y)}A(y)\}+o(1),
 \quad
 A(y)=\sum_{k\le N(y)}
 \frac{\exp(\tau\log^2 k)}{k^{s+2\tau\alpha(s)}},\qquad
 N(y)=\left\lfloor\sqrt{y/(2\pi)+(4\tau)/16}\right\rfloor .
 \tag{4}
$$
The two sums in their formula are conjugate on the real axis. Their error terms (23)–(24) after normalization are $o(1)$ uniformly: (23) is $\ll U^{-1}\log^2 U$ times the sum of absolute weights, which is $O(U^{1/4+o(1)})$, since $2\Re\alpha(s)\ge\log N(y)$ for large $U$. Equation (24) is $O(U^{-1/4})$. The heat approximation contributes $O(U^{-1/4}\log^3 U)$. [D. H. J. Polymath, Theorem 1.3](https://arxiv.org/abs/1904.12438)

## Mean-square approximation and a mollifier

For a positive integer $K$ define the fixed-length polynomial
$$
 A_K(y)=\sum_{k\le K}k^{-1/2-c(y)-iy}.
$$
The following two bounds use the normalized quadratic mean on $I=[aU,bU]$, denoted by $\|\cdot\|_2$:
$$
 \lim_{K\to\infty}\limsup_{d\to\infty}\|A-A_K\|_2=0,
 \qquad
 \lim_{\lambda\downarrow0}\limsup_{K\to\infty}\limsup_{d\to\infty}
 \frac{|\{y\in I:|A_K(y)|<\lambda\}|}{|I|}=0.
 \tag{5}
$$

Here are details accounting for the variable weights and cutoff. Choose $\delta=c_-/4$. On a dyadic block $k\in[L,2L]$, $k\le N(y)$, factor out $k^{-1/2-\delta-iy}$. The remaining multiplier is
$$
 h_y(v)=\exp[-(c(y)-\delta)v+\tau v^2-2i\tau\Im\alpha(s)v],\quad v=\log k.
$$
Since $\tau\log N(y)\le c(y)/2+o(1)$, this multiplier has modulus at most one. Its derivative in $v$ is uniformly bounded there, so its total variation on each dyadic block is bounded by a fixed constant. Partial summation, including the moving upper cutoff, therefore bounds the block by a constant times the maximal partial sum of $k^{-1/2-\delta-iy}$. For coefficients supported on $[L,2L]$ with $L\ll\sqrt U$, Montgomery–Vaughan's mean value inequality gives normalized $L^2(I)$ norm at most $C(\sum|b_k|^2)^{1/2}$ for every subsum. Binary decomposition of each initial subinterval and Cauchy–Schwarz give its maximal version with factor $C\log(2L)$: at each depth the squared norms of disjoint blocks sum to $O(\sum|b_k|^2)$ and there are $O(\log(2L))$ depths. Thus the $L^2$ contribution of this full dyadic block is $O(\log(2L)L^{-\delta})$. Summing dyadically above $K$ tends to zero uniformly. For $k\le K$ fixed the omitted multiplier $\exp(\tau\log^2 k-2i\tau\Im\alpha(s)\log k)$ tends uniformly to one. This proves the first assertion in (5).

For the second assertion fix $m$ and let $B_m(y)=\sum_{j\le m}\mu(j)j^{-1/2-c(y)-iy}$. The same dyadic argument gives $\|B_m\|_2\le C$ uniformly in $m$ after taking $\limsup_{d\to\infty}$; the multiplier $e^{-(c(y)-\delta)v}$ has uniformly bounded variation. For $K\ge m$, the product $A_K B_m-1$ has zero coefficients at integers $2,\ldots,m$ and all its coefficients before the common weight have modulus $\le d(k)$, the divisor function. With $m,K$ fixed and $d$ sufficiently large, every contributing block $L\le mK$ is much shorter than $U$. The same maximal estimate and $d(k)\ll_\delta k^{\delta/2}$ show
$$
 \limsup_{d\to\infty}\|A_K B_m-1\|_2
 \ll_\delta \sum_{2^j\ge m/2}\log(2^{j+1})\,2^{-j\delta/2}\longrightarrow0
$$
uniformly for fixed $K\ge m$ in this iterated limit. If $|A_K|<\lambda$, either $|B_m|>1/(2\lambda)$ or $|A_K B_m-1|\ge1/2$. Chebyshev proves (5).

## Turning quadratic mean into a distinct-root count

Fix $\eta>0$. By (5) choose $\lambda>0$ sufficiently small, and then a fixed $K$ sufficiently large, such that for large $d$ the fraction where $|A_K|\le 2\lambda$ is at most $\eta$, and $\|A-A_K\|_2^2\le\eta\lambda^2$. Constants in these choices can be tightened arbitrarily. The derivative of $A_K$ is $O_K(1)$ since $c'(y)=O(1/U)$.

Partition $I$ into intervals of length $(\log U)^{-1/2}$, discarding a final shorter fragment. Discard each subinterval where $|A_K|$ ever falls below $\lambda$. For large $d$ its entirety lies in $|A_K|\le2\lambda$, so their total discarded length is at most $\eta|I|$. On each remaining subinterval replace $A_K$ by its value at the midpoint at uniform cost $o_K(1)$. The phase in (4) is now compared to $\phi(y)$ plus the fixed midpoint argument. By (3) it increases through $(1+o(1))\sqrt{\log U}/2$ on each subinterval. Around each consecutive multiple of $\pi$ take the arc in $y$ where the phase differs from that multiple by less than $\pi/6$, using only full arcs. Their lengths are $\asymp1/\log U$, and their midpoint-model values have alternating signs and magnitude at least $\lambda$. The number of full arcs in the retained intervals is at least their total length times $(1+o(1))\log U/(2\pi)$, less $O(U\sqrt{\log U})$ for boundaries.

If some arc contains no point with the predicted strict sign for $P_d$, (4) forces $|A-A_K|\gg\lambda$ throughout it for all sufficiently large $d$. There are $O(\eta U\log U)$ such arcs by (5). Removing one arc breaks at most two adjacent alternating pairs. Each surviving pair supplies a distinct real zero strictly between its sign witnesses. This proves (2) by sending $\eta$ to zero after $d$ tends to infinity.

## Matching the two endpoints

Use $T,\Lambda,Q=c_0T,q_e,\tau_e=M\sqrt{\log d/d}$ as in Ono §2.2 and §5. Here $\tau_e$ is his edge parameter, distinct from the heat time above. Put $U=T/\sqrt Q$ so that Ono's counted real roots have positive frequencies $y\ge U$, whereas (2) with $b=1$ supplies roots below $U$. The possible common endpoint costs at most one. By Ono's Corollary 16 and Lemmas 11,17 the number of roots above $U$ counted on his phase interval is at least
$$
 \frac d\pi\{S(Q)-S(q_e+\tau_e)\}-O(1).
$$
The edge loss $dS(q_e+\tau_e)=O(d^{1/4}(\log d)^{3/4})$ is $o(U\log U)$. The needed leading constant at the other endpoint follows from his exact saddle identities. In the notation of (3.4)–(3.6) of his paper, $r=(1+o(1))/\sqrt Q$, $\Lambda=2(\log(T/(2\pi))-1)$, $\kappa=\pi/2$ and $\alpha\to\pi/2$. Dividing (3.4) by $\Lambda$ gives
$$
 \frac{\cos\alpha}{\kappa r}=\tfrac12+\frac{\log r+1-\alpha\cot\alpha}{\Lambda}
 =\tfrac14+o(1)
$$
because $\log r\sim-\frac12\log T$. In (3.21), $\pi-2\alpha+\sin(2\alpha)\sim4\cos\alpha$ and its last term is $O(r/\Lambda)$. Hence $\pi-S(Q)\sim\kappa/\sqrt Q$. Since $4\pi d=T\Lambda$ and $\log U\sim\Lambda/4$,
$$
 d(\pi-S(Q))\sim U\log U/2 .
$$
For each fixed $a>0$, combining this exact loss with (2) on $[aU,U]$ leaves at most $(a+o(1))U\log U/(2\pi)$ missing roots. Send $a$ to zero, using $U\log U\asymp\sqrt{d\log d}$, to obtain (1).

This argument estimates a count. It permits a sublinear, unbounded exceptional set and supplies no evidence that every Jensen polynomial is hyperbolic.
