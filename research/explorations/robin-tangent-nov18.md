# A tangent inequality for Robin on arbitrary integers

**Proposed arithmetic lemma.** This version of the [finite-horizon argument](robin-finite-horizon-nov18.md) works with $y=\log n$ directly. It removes the pointwise error in $\vartheta(y)$ and allows positive averaging in an auxiliary real parameter. The remaining input is an upper bound for a signed integrated prime discrepancy. All logarithms are natural.

Let $v\ge4$, $y=\log n>1$, $s_v=1/(v\log v)$, and $b_p=-\log(1-1/p)$. With the notation $K(v)=\int_v^\infty(\vartheta(t)-t)t^{-2}((\log t)^{-1}+(\log t)^{-2})dt$ define
$$
A(v)=\sum_{p\le v/2}\min(s_v\log p,p^{-2}),\qquad
R(v)=\sum_{p>v}\sum_{k\ge2}\frac1{kp^k}.
$$
For **every** integer $n$ as above and every $v\ge4$ we have
$$
\log\frac{\sigma(n)}{e^\gamma n\log y}
\le -K(v)-A(v)-R(v)
 +\log\log v-\log\log y+s_v(y-v).
\tag{1}
$$
In particular, at $v=y$ there is no tangent error and there is no restriction on the prime support or the exponents of $n$.

**Proof.** For $p^a\Vert n$ put $I_p(a)=1+\cdots+p^{-a}$, setting $I_p(0)=1$. For $p>v$, each successive increment in $\log I_p(a)$ is at most $\log(1+1/p)<1/p<s_v\log p$, hence $\log I_p(a)-s_v a\log p\le0$. For $p\le v$ the baseline $b_p-s_v\log p$ is nonnegative, since $b_p\ge1/p\ge1/v\ge s_v\log p$. It bounds $\log I_p(a)-s_v a\log p$ also when $a\ge1$.

For $p\le v/2$ the baseline exceeds the actual contribution by at least $\min(s_v\log p,p^{-2})$. If $a=0$, then $b_p-s_v\log p\ge2/v-1/v\ge s_v\log p$. If $a=1$ the difference is $-\log(1-p^{-2})\ge p^{-2}$. If $a\ge2$ the extra exponent price alone is at least $s_v\log p$. Summing over primes gives
$$
\log(\sigma(n)/n)-s_v y\le\log M(v)-s_v\vartheta(v)-A(v),
\quad M(v)=\prod_{p\le v}(1-1/p)^{-1}.
$$
The exact identity
$$
\log M(v)-\gamma-\log\log v
=s_v(\vartheta(v)-v)-K(v)-R(v)
$$
follows by partial summation of $\sum_{p\le v}1/p$ from $v$ to infinity, since $d\vartheta(t)/(t\log t)$ has mass $1/p$ at each prime. The constant follows from Mertens' product theorem. This proves (1).

### A local lower bound on the exponent cost

Put $q=\sqrt{2v}$ and $z=100q$. Suppose $z\le v/2$ and $|\vartheta(t)-t|\le\eta t$ on $[q,z]$, with $0<\eta<1$. For $p\le q$ one has $p^{-2}\ge (1+\log2/\log v)^{-1}s_v\log p$. For $p>q$ one has $s_v\log p\ge p^{-2}$. The same Stieltjes estimate used in the preceding note thus gives
$$
\begin{aligned}
\sqrt v\log v\, A(v)\ge\frac{\sqrt2}{1+\log2/\log v}
\left[(1-\eta)+(1-\eta)(1-1/\log q)-2\eta-1/100\right].
\tag{2}
\end{aligned}
$$
Here $\int_z^\infty dt/(t^2\log t)\le 1/(100q\log q)$ accounts for the finite right endpoint. The right side is increasing in $v$ with $\eta$ fixed. Only the prime-counting estimate between $\sqrt{2v}$ and $100\sqrt{2v}$ enters this step.

For example, set $B=9\cdot10^{21}$. With $B\le v\le10^{40}$, Büthe's verified-height theorem covers $[q,z]$ and gives $\eta=0.0001$. Equation (2) then exceeds $2.72$. In the same range split prime powers at $Y=10^{48}$ as before. Since $\sqrt B>9\cdot10^{10}$, Büthe gives $\vartheta(\sqrt t)/\sqrt t\le1.0001$ for $v\le t\le Y$; the elementary cubic and higher-power terms give
$$
\frac{\psi(t)-\vartheta(t)}{\sqrt t}
\le1.0001+2B^{-1/6}
 +2\frac{\log B}{\log 2}B^{-1/4}<1.002 .
$$
For $t>Y$ use $3\sqrt t$ as in the preceding note. Equations (2)–(4) of that note now give, on $B\le v\le U\le10^{40}$,
$$
-\sqrt v\log v\,K(v)\le
\left(1+\frac1{\log B}\right)
\left[0.047+\mathcal T(U)+\frac{\log(2\pi)}{\sqrt B}+2(1.002+3\sqrt{U/Y})\right],
\tag{3}
$$
where
$$
\mathcal T(U)=\sum_{|\Im\rho|>3\cdot10^{12}}\frac{U^{(\Re\rho-1/2)_+}}{(\Im\rho)^2}.
$$
This is an explicit remaining scalar requirement for extending the horizon. For $v=y$, a bound $\mathcal T(U)<0.60$ already suffices in (3) for all $B\le y\le U$. Since $B<0.99\cdot10^{22}$, these ranges overlap the preceding finite theorem.

### Explicit zero density and the pointwise horizon

**Finite consequence.** Robin's strict inequality holds for every integer $5040<n\le\exp(10^{38})$.

Write $H=3\cdot10^{12}$ and $S(\sigma)=\sum_{|\Im\rho|>H,\Re\rho>\sigma}|\Im\rho|^{-2}$. Then $\mathcal T(U)$ equals the full reciprocal-square mass plus $\int_{1/2}^1 S(\sigma)d(U^{\sigma-1/2})$ by integration of each positive summand. The full mass is below $3.1\cdot10^{-12}$ and $S(\sigma)$ is at most half of this for $\sigma\ge1/2$ by reflection across the critical line. For a positive-height zero-density bound $N(\sigma,t)\le\sum c\,t^b(\log t)^k$, partial summation bounds $S(\sigma)$ by $4\int_H^\infty N(\sigma,t)t^{-3}dt$. Each monomial consequently contributes at most
$$
\frac{4cH^{b-2}(\log H)^k}{2-b-k/\log H},
$$
provided the denominator is positive: use $(\log t/\log H)^k\le(t/H)^{k/\log H}$.

The [density checker](check_robin_density_nov18.py) uses the two explicit density estimates of Chourasiya and Simonič on a mesh of $1/6400$ in $\sigma$. On each cell $S$ is decreasing, so its left endpoint bound times the exact increment of $U^{\sigma-1/2}$ is an upper bound. It follows that $\mathcal T(10^{38})<0.554$. The [tangent checker](check_robin_tangent_nov18.py) verifies the remaining monotone endpoint constants in (2) and (3) with Arb. This proves the consequence, with the low range covered by the preceding finite theorem. [Density inputs: Corollary 1 and equation (119), Tables 1 and 4](https://arxiv.org/abs/2507.15184)
