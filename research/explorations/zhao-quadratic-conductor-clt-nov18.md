# Joint Gaussian limits for smoothed quadratic prime sums at growing conductors

Assume GRH for primitive quadratic Dirichlet characters. Give fundamental discriminants $Q<|D|\le2Q$ equal weight, with either sign prescribed or both signs allowed. Write $\chi_D=(D/\cdot)$ and
$$
 S_D(X)=\sqrt X\sum_{n>X}\frac{\Lambda(n)\chi_D(n)}n(1-X/n).
$$
Fix $m$ positive integers $1\le j\le m$ as scale indices and set $X_j=(\log Q)^j$. Then
$$
 \left(\sqrt{3/\log X_j}\ S_D(X_j)\right)_{1\le j\le m}
 \ \Longrightarrow\ N(0,I_m).                                          \tag{1}
$$
The same proof applies to other increasing $X_j=Q^{o(1)}$ when $X_1\to\infty$ and $\sqrt{X_i/X_j}\sqrt{\log X_j/\log X_i}\to0$ for $i<j$. These assumptions suffice for the claimed independence; the proof does not assume independence of events for a fixed quadratic character.

### Orthogonality with a uniform error

Let $Z_p$ be independent with $\Pr(Z_p=0)=1/(p+1)$ and $\Pr(Z_p=1)=\Pr(Z_p=-1)=p/(2(p+1))$, including $p=2$. For a monomial $P$ in the values at primes in a finite set $\mathcal P$, with coefficient one, one has
$$
 \mathbb E_D P((\chi_D(p))_{p\in\mathcal P})
 =\mathbb E P((Z_p)_{p\in\mathcal P})
   +O\left(Q^{-1/2}\prod_{p\in\mathcal P}p^2\right).                   \tag{2}
$$
The implicit constant is absolute, including either choice of sign for $D$. Here is an elementary proof. For any modulus $M$ and residue $a$, the squarefree count in that class through $T$ equals
$$
 T\sum_{(d^2,M)\mid a}\frac{\mu(d)}{[d^2,M]}+O(\sqrt T),
$$
with an absolute error uniform in $M,a$. Insert $\mu^2(n)=\sum_{d^2\mid n}\mu(d)$, count one residue class per consistent pair up to $d\le\sqrt T$, and bound the omitted main terms by $T\sum_{d>\sqrt T}d^{-2}$. Subtract the endpoints for a dyadic interval. Apply this with $M=8\prod_{p\in\mathcal P,\ p>2}p^2$. For any local classes avoiding square factors at primes dividing $M$, the main density per class is the same, $M^{-1}\prod_{p\nmid M}(1-p^{-2})$; other classes at square multiples have zero density. The aggregate discrepancy is $O(M\sqrt Q)$.

For either sign of $D$, the fundamental-discriminant cases are $D=d$ squarefree with $d\equiv1\pmod4$, and $D=4d$ with squarefree $d\equiv2,3\pmod4$. The ranges of $|d|$ in the second case have one quarter the length of the first. At each odd prime the $p^2-1$ allowed classes have $p-1$ divisible by $p$ and equal numbers of quadratic signs. Multiplication by $4$ does not change those signs, and negating $d$ simply permutes the classes. By CRT these laws are independent across odd primes and of the case modulo eight. The first case gives two thirds of all discriminants, half at each of the signs of $\chi_D(2)$, and the remaining third are even with $\chi_D(2)=0$. More explicitly the first case has two allowed classes modulo eight and the second case four, counted over an interval one quarter as long. This gives the asserted law and a family size $\asymp Q$ with error $O(\sqrt Q)$ at fixed base modulus. Division gives (2).

### Uniform truncation and removal of powers

The GRH explicit formula gives $|\psi(v,\chi_D)|\ll\sqrt v\log^2(2Qv)$ uniformly in this family. Partial summation yields, uniformly for $Y\ge2X\ge4$,
$$
 \left|\sqrt X\sum_{n>Y}\Lambda(n)\chi_D(n)(1-X/n)/n\right|
 \ll\sqrt{X/Y}\log^2(2QY).
$$
Indeed the weight and its derivative on this tail are $O(1/v)$ and $O(1/v^2)$, and the integral of $v^{-3/2}\log^2(2Qv)$ has the same bound as its first dyadic block up to an absolute constant. Take $Y=X_m(\log Q)^6$, giving $o(1)$ uniformly for all the stated scales. The full prime powers $p^k>X$, $k\ge2$, contribute $O(1)$ absolutely after multiplication by $\sqrt X$. For $p\le\sqrt X$ the geometric tail from the first qualifying exponent is at most $2/X$; for $p>\sqrt X$ it is at most $2/p^2$. Summation with $\log p$ uses $\vartheta(v)\ll v$. Both errors vanish on normalization by $\sqrt{\log X_j}$.

### The random prime sums and transfer of moments

The unnormalized random prime coefficient at scale $X$ is $a_p(X)=\sqrt X (\log p)/p\,(1-X/p)_+$. The corresponding random variable $\sum_{p\le Y}a_p(X)Z_p$ is centered. As $X\to\infty$ its variance is $(1/3+o(1))\log X$, uniformly for the above choices. Indeed $\mathbb E Z_p^2=p/(p+1)$ can be replaced by one with error $O((\log X)^2/X)$. PNT and partial summation of $d\vartheta$ give, for every fixed $k\ge0$,
$$
 \sum_{p>X}\frac{\log^2p}{p^{2+k}}
 \sim\frac{\log X}{(1+k)X^{1+k}}.
$$
Expanding $(1-X/p)^2$ leaves coefficient $1-2/2+1/3=1/3$. Truncation costs $O(X\log Y/Y)=o(\log X)$ since $Y\ge X(\log Q)^6$ and $\log Y=o(\log Q)$. For $x\le y$ the covariance is $O(\sqrt{x/y}\log y)$ by the $k=0$ estimate, proving that normalized covariances at distinct stated scales vanish. More generally if $x/y\to r\in(0,1]$ the covariance divided by $\log y$ tends to $\sqrt r(1/2-r/6)$.

For each fixed real linear combination of normalized coordinates, write $c_p$ for its coefficient of $Z_p$. Its variance tends to the squared Euclidean norm of the vector of weights and $\max_p|c_p|\to0$, since $\sup_p a_p(X)\ll(\log X)/\sqrt X$. The sums $\sum_p c_p^2$ stay bounded since $\mathbb E Z_p^2\ge2/3$. Every fixed cumulant of order $k\ge3$ is $O_k((\max_p|c_p|)^{k-2}\sum_p c_p^2)=o(1)$ by independence and boundedness of $Z_p$. Thus all fixed moments tend to the corresponding Gaussian moments.

For any fixed $k$, expand the $k$th power of the same prime polynomial in the arithmetic and random models. The aggregate error using (2) is
$$
 \ll Q^{-1/2}Y^{2k}\left(\sum_{p\le Y}|c_p|\right)^k
 =Q^{-1/2+o(1)}.
$$
Indeed $Y=Q^{o(1)}$ and $\sum_{p\le Y}|c_p|\ll_m (1+\sqrt{X_m})(\log(2Y))^2=Q^{o(1)}$ for fixed coordinate weights. The moment-determinate Gaussian law, Cramér–Wold and the uniform removal of powers prove (1).

### Quantifiers for oscillation applications

For every fixed $B>0$, the lower proportion of discriminants in the dyadic family for which some $j\le m$ has $S_D(X_j)>B$ and some $k\le m$ has $S_D(X_k)<-B$ is at least $1-2^{1-m}$. Apply (1) to the positives and negatives separated from zero by a small fixed normalized distance, and let that distance decrease. The same prime-sum estimates apply to positive and negative discriminants separately. Letting $m$ grow *after* the conductor limit shows that for any fixed $B$ the proportion with witnesses tends to one if one allows, for example, all $X\le\exp((\log\log Q)^2)$ (this bound eventually contains the first $m$ chosen scales for each fixed $m$). The argument does not claim that a single fixed conductor has unbounded $S_D$. Transfer from these finite witnesses to arbitrarily late occurrences for a fixed conductor requires the separate explicit formula and almost-periodicity argument.

For fixed thresholds $X$ the same orthogonality and truncation give finite-dimensional convergence to the full random quadratic Euler model without normalizing by $\sqrt{\log X}$. To see the needed uniform tail control, truncate first at $(\log Q)^6$, then at fixed integer $K>2\max X$. The intervening prime polynomial has family second moment $O_X(\sum_{p>K}(\log p/p)^2)+o_Q(1)$ by (2), and all higher powers with $p^j>K$ cost $O_X(1/\sqrt K)$ absolutely. The random prime tails satisfy the same estimate by independence. Fixed truncations converge by CRT, then $K\to\infty$ gives the assertion. At each individual coordinate the limiting distribution has no atoms: condition on the occupied primes $p>X$, almost surely infinitely many, and their independent fair signs. The difference between the two local values at each such prime is positive since the terms at odd exponents have positive coefficients. On any $k$ occupied primes the sign configurations attaining one given value form an antichain, even after conditioning on all other values. Sperner's theorem bounds their probability by $2^{-k}\binom{k}{\lfloor k/2\rfloor}\to0$. Consequently joint boxes with any fixed coordinate cutoffs are continuity sets. A joint density in all dimensions is not needed.
