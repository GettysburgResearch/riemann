# A polynomial phase transition in the common-rough-part trace

**Status.** Proposed unconditional theorem for a specified part of the actual odd Möbius trace. The complete trace includes every cross term between unequal rough parts. Its upper exponent remains open.

Let $L=\log N$, write $Q=\prod_{3\le p\le y}p$, and call $s$ admissible if it is squarefree and every prime dividing it exceeds $y$ (include $s=1$). For $N\le j<2N$, $1<t<3$, use the [TC26 integrated Legendre columns](https://github.com/GettysburgResearch/riemann/blob/a27285abe428835ac0171fe9eb8cbbc97a64a33a/standalone/2026-09-13-astra-trace-covariance/PROOF.md) $\psi_j(x)=\int_x^1\phi_j(u)\,du/u$ on $[0,1]$, extended by zero for $x>1$. Define
$$
 U_s(j,t)=\frac{\mu(s)}s\sum_{d\mid Q}\frac{\mu(d)}d\psi_j(t/(sd)),
 \quad G_N(y)=\sum_{s\text{ admissible}}\sum_{j=N}^{2N-1}\int_1^3|U_s(j,t)|^2dt.
$$
This is precisely the sum over pairs with the same part supported on primes larger than $y$ in the completed native degree block. Each fixed-$N,y$ group contains finitely many divisors and the sum of squared group norms converges absolutely. Distinct-group interactions use the native common source cutoff in [the ratio note](trace-nov18.md).

For each fixed $A>0$ and $y=L^A$,
$$
 \lim_{N\to\infty}\frac{\log G_N(y)}{\log N}=\max(0,1-2/A).
\tag{1}
$$
More precisely, if $0<A<2$, or if $y=a^2L^2$ with fixed $0<a<1/2$, then
$$
 \log G_N(y)=(4+o(1))\frac{\sqrt y}{\log y}.
\tag{2}
$$
In particular at each cutoff $y=(\log N)^{2+\epsilon}$, treating different rough parts as orthogonal already gives a positive power of $N$. The true signs and the correlations induced by *every* smaller prime are retained within the groups. The native subpower criterion would require cancellation with unequal rough parts at this cutoff. Equation (1) does not bound that remainder.

## Column estimates and the direct upper bound

We use the elementary estimates proved in (10)–(11) of [the ratio note](trace-nov18.md): $|\psi_j(x)|\ll\min(1,(jx)^{-1})$ and $|\phi_j(x)|\ll\min(1,jx)$ for $0<x\le1/2$, and $\|\psi_j\|_{L^2(1/2,1)}\ll j^{-1}$. Uniformly for integer $n\ge1$, therefore
$$
 \|\psi_j(t/n)\|_{L^2(1,3)}\ll \min(1,n/j).
\tag{3}
$$
For $n\ge7$ this follows pointwise; for each $n=1,\ldots,6$ use TC26 (2) on $x\ge1/6$. For any $0<b<1/2$, use $\min(1,n/j)\le(n/j)^b$, $|\mu|\le1$ and the triangle inequality within each group. This gives
$$
 G_N(y)\ll N^{1-2b}\zeta(2-2b)
                  \prod_{3\le p\le y}(1+p^{b-1})^2 .
\tag{4}
$$
If $A>2$ take $b=1/A$. The prime sum $\sum_{p\le y}p^{b-1}=O_A(L/\log y)$ by the prime number theorem, giving upper exponent $1-2/A$. For $A\le2$ or $y=a^2L^2$, take $b=1/2-1/L$. Since $\zeta(1+2/L)=O(L)$, and $\sum_{p\le y}p^{-1/2}\sim2\sqrt y/\log y$, this gives the upper half of (2), and upper exponent zero when $A=2$. Here $\log L=o(\sqrt y/\log y)$ for each fixed positive $A$.

## Rough squarefree integers on polynomial-sized intervals

For fixed $A_0,h,C>0$, all $3\le y\le 2L^{A_0}$, and $N^h\le x\le N^C$, there is $c=c(A_0,h,C)>0$ with
$$
 R_y(x):=\#\{s\le x:\ s\text{ admissible}\}
   =\delta_y x+O_{A_0,h,C}(x^{1-c}),\qquad
 \delta_y=\prod_{p\le y}(1-1/p)\prod_{p>y}(1-1/p^2)\asymp1/\log y .
\tag{5}
$$
Here the prime two is excluded from $s$. First count all $y$-rough integers without the squarefree condition. Bonferroni with consecutive truncations of order $k=\lfloor\log x/(4\log y)\rfloor$ and $k+1$ gives corresponding bounds. The total floor error in each is $O(y^{k+1})=O(x^{1/3})$ for large $N$, since selected products are distinct integers at most $y^{k+1}$. The truncated main factors differ from the complete product by at most $(\sum_{p\le y}1/p)^k/k!$ up to a harmless constant: apply the same inclusion-exclusion bounds to independent Bernoulli events of probabilities $1/p$. Using $k!\ge(k/e)^k$ and $\sum_{p\le y}1/p\ll\log\log(3y)$ gives an error $O(x^{-c_1})$ for some $c_1>0$ uniformly, since $k\gg\log x/\log\log x$ and $\log(k/(e\sum1/p))\gg\log\log x$. If $k$ exceeds the number of eligible primes, the truncation is exact. This proves the asserted power asymptotic before imposing squarefreeness. Now expand $\mu^2(s)=\sum_{v^2\mid s}\mu(v)$. For $v\le x^{1/4}$ with all prime factors $>y$, apply the preceding count to $x/v^2\ge x^{1/2}$, using $h/2$ in place of $h$. Take $c_1<1/4$ so that the errors sum to $O(x^{1-c_1})$. The positive count for $v>x^{1/4}$ is bounded by $\sum_{v>x^{1/4}}x/v^2=O(x^{3/4})$, also bounding the extended density tail. The squarefree product and the claimed density follow. The estimate on $\delta_y$ uses only the classical Mertens product.

## A Mellin trial on a polynomial range of rough parts

Take $b$ in a fixed compact subinterval of $(0,1)$, allowing it to depend on $N$, and set $\tau=\pi/\log y$. Define
$$
 M_b=\prod_{3\le p\le y}(1+p^{b-1}),\quad
 E_b=\prod_{3\le p\le y}(1-p^{b-1-i\tau}),\quad
 w_b(d)=d^{b-1}/M_b\quad(d\mid Q).
$$
The $w_b$ are a probability law. Let $S_1=N^{h_1}$, $S_2=N^{h_2}$ for fixed $0<h_1<h_2$. Suppose that for some fixed $c_2>0$ all but probability $e^{-c_2L/\log y}$ of the $d$ satisfy, uniformly in $N\le j<2N$,
$$
 S_1 N^{c_2} \le j/d \le S_2 N^{-c_2}.
\tag{6}
$$
Constants $c_2$ can be decreased if different estimates are available for the margin and the exceptional probability. Suppose also
$$
 \log(M_b/|E_b|)=o(L/\log y).
\tag{7}
$$
For the selected range of admissible $s$ form the scalar trial
$$
 T_{j,t}=\sum_{S_1<s\le S_2\text{ admissible}}
        s^{-1-b+i\tau}\sum_{d\mid Q}\frac{\mu(d)}d\psi_j(t/(sd)).
$$
Uniformly over the degree block and $1<t<3$,
$$
 T_{j,t}=(1+o(1))\,\delta_y\,t^{-b+i\tau}
       \frac{c_j(b-i\tau)}{b-i\tau}\,E_b,\qquad
 c_j(z)=\int_0^1 \phi_j(x)x^{z-1}\,dx .
\tag{8}
$$
In (8) the error denotes a complex relative error tending to zero. The rational formula DG26 (3.2) and the gamma-ratio asymptotic give, uniformly at these compact $z=b-i\tau$,
$$
 c_j(z)=(-1)^j j^{-z}
            \frac{\Gamma((1+z)/2)}{\Gamma(1-z/2)}(1+O(1/j)).
\tag{9}
$$
In particular its modulus is comparable to $j^{-b}$. The exact integral behind (8) is
$$
 \int_0^\infty s^{-1-b+i\tau}\psi_j(t/(sd))\,ds
   =(d/t)^{b-i\tau}\int_0^1 x^{b-i\tau-1}\psi_j(x)\,dx
   =(d/t)^{b-i\tau}c_j(b-i\tau)/(b-i\tau).
$$
The final equality uses ordinary integration of the primitive on its proper domain.

Here are uniform error bounds for replacing the rough sum by this integral. Write $r=sd/j$. For $s\ge S_1$ the interior estimates give $|\psi_j(t/(sd))|\ll\min(1,r)$ and $|s\partial_s\psi_j(t/(sd))|\ll\min(1,1/r)$. The sum over integers or the integral on this range with absolute weight $s^{-1-b}$ is $O((d/j)^b)$, by splitting at $s=j/d$ and using $b$ in a compact subset of $(0,1)$. The same bound for the integral on the full positive axis follows from (3)'s interior estimates and the $L^2$ bound on $[1/2,1]$ after substitution $x=t/(sd)$. Consequently the total absolute cost of exceptional $d$ from (6) is $O(j^{-b} M_b e^{-c_2L/\log y})$.

For each nonexceptional $d$, the full integral outside $[S_1,S_2]$ is $O((d/j)^b N^{-c_3})$ for some $c_3>0$: below $S_1$ integrate the bound $r$ wherever $sd\ge6$, and above $S_2$ use the bound one. The region $sd<6$ in the integral costs $O(d^b j^{-1})$ by TC26 (2) on $x\ge1/6$. Within $[S_1,S_2]$, discard for the moment $r<N^{-e}$ with fixed small $e>0$. The absolute costs of its integral and integer sum are $O((d/j)^b N^{-e(1-b)})$. On the rest put $h(s)=s^{-1-b+i\tau}\psi_j(t/(sd))$. Its derivative satisfies $|s h'(s)|\ll N^e s^{-1-b}\min(1,r)$. Partial summation using (5) on this interval bounds the discrepancy by $O((d/j)^b N^e S_1^{-c})$, including both endpoints: at an endpoint $|s h(s)|\ll(d/j)^b$. Choose $e<ch_1/2$. All nonexceptional errors are thus $O((d/j)^b N^{-c_4})$ for some fixed $c_4>0$. Sum the errors with weights $1/d$; (7), (9) and $\delta_y\asymp1/\log y$ show they are $o(\delta_y j^{-b}|E_b|)$. The main terms multiply to the product in (8).

Finally Cauchy–Schwarz with test vector $\mu(s)s^{-b-i\tau}$ bounds, pointwise,
$$
 \sum_{s\text{ admissible}}|U_s(j,t)|^2
 \ge |T_{j,t}|^2\bigg/\sum_{S_1<s\le S_2}s^{-2b}.
\tag{10}
$$
Summing $N$ degrees and integrating $1<t<3$ therefore gives the desired positive lower bound wherever the two trial conditions hold.

## Tilting the divisor law and completing the bounds

Under $w_b$, the random variable $\log d$ is a sum of independent prime contributions $\log p$ with success probability $p^{b-1}/(1+p^{b-1})$. Its mean $m_b$ satisfies
$$
 m_b=(1+o(1))y^b/b,\qquad
 \sum_{p\le y}p^{b-1}=(1+o(1))y^b/(b\log y)
\tag{11}
$$
uniformly on compact subintervals of $(0,1)$ by partial summation of the prime number theorem. The omission of 2 is negligible here. If $m_b=O(L)$ then for every fixed $\eta>0$ there is $c_\eta>0$ with
$$
 \Pr(|\log d-m_b|>\eta L)\le2\exp(-c_\eta L/\log y).
\tag{12}
$$
Indeed at $z=\pm\kappa/\log y$, the log moment of the centered sum is at most $C_\kappa z^2\sum p^{b-1}(\log p)^2\ll_\kappa z^2 L\log y$, using the second-order bound on each bounded Bernoulli exponential. Apply the exponential Markov inequality with sufficiently small positive $\kappa$ in each direction.

For these choices of $b$ with $m_b=O(L)$, condition (7) holds. The difference of prime log factors is bounded in aggregate by
$$
 O\left(\sum_{p\le y}p^{b-1}(1+\cos(\tau\log p))
            +\sum_{p\le y}p^{2b-2}\right)
  =o(y^b/\log y).
$$
The square-weight sum is little-oh of the first-degree mass by boundedness of $b$ away from one and (11). For $p<y^{1-\epsilon}$ the first-degree mass is little-oh of the full mass at each fixed $\epsilon>0$. On the remaining primes $1+\cos(\tau\log p)=O(\epsilon^2)$; let $\epsilon\downarrow0$. In fact $\log|E_b|=(1+o(1))y^b/(b\log y)$.

If $A>2$ fix $0<\theta<1/4$ and choose the unique real $b$ with $m_b=(1-\theta)L$. It exists for large $N$ and $b\to1/A$ by monotonicity and (11) applied on either side of $1/A$. For $A=2$ the same choice has $b\to1/2$ and $b<1/2$ eventually since $m_{1/2}\sim 2L$. Set $h_1=\theta/2$, $h_2=3\theta/2$. Equation (12) with deviation at most $\theta L/4$ gives (6), including the bounded factor $j/N$. The denominator in (10) is at most $O(\log N)N^{h_2(1-2b)}$ for $b\le1/2$. Since $\log|E_b|=o(L)$, (8)–(10) yield
$$
 \liminf \frac{\log G_N(L^A)}L
 \ge (1-2/A)(1-3\theta/2).
$$
Let $\theta\downarrow0$ and combine with (4). This proves (1) for $A\ge2$.

For $0<A<2$, fix $b=1/2$ in the trial only. Its mean $m_b\sim2\sqrt y=o(L)$; for $y=a^2L^2$ with $a<1/2$ the mean is $(2a+o(1))L$. In both cases choose $h_1>0$ sufficiently small that $m_b<(1-2h_1)L$ eventually and take $h_2=2$. Equation (12) with deviation $h_1L/2$ gives (6). The denominator in (10) costs $O(\log N)$; (8) and $|c_j(1/2-i\tau)|\asymp j^{-1/2}$ give
$$
 \log G_N(y)\ge 2\log|E_{1/2}|-O(\log\log N+\log\log(3y)).
$$
The right side is $(4+o(1))\sqrt y/\log y$. This and the upper bound (4) prove (2) and the remaining range of (1).

**Scope of verification.** The proof uses classical PNT, Mertens, Legendre normalization and an elementary squarefree sieve. Its trial in the rough-part index is a lower bound for the positive grouped quantity only. It makes no statistical assumption on actual Möbius signs and does not infer cancellation in the omitted unequal-part interaction from randomization.
