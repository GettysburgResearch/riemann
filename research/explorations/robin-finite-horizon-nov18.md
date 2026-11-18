# A finite Robin range from the verified zeta height

**Proposed theorem, unreviewed.** For every integer $5040<n\le\exp(0.99\cdot10^{22})$,
$$
\sigma(n)< e^\gamma n\log\log n .
$$
More specifically, all arbitrary positive exponent profiles with prime support exactly $\{p:p\le x\}$ satisfy this inequality if $10^{13}\le x\le10^{22}$. This is a finite conclusion using published computer-assisted theorems. The zero census and the published low-range Robin computation are imported. No historical priority is claimed. The [constant checker](check_robin_finite_nov18.py) verifies the numerical relaxations by Arb intervals.

Set $x_0=10^{13}$, $U=10^{22}$, $H=3\cdot10^{12}$, $Y=10^{40}$, $L=\log x$, $T=\vartheta(x)$ and $M(x)=\prod_{p\le x}(1-1/p)^{-1}$. Write
$$
N(x)=\log M(x)-\gamma-\log\log T.
$$
We first prove $\sqrt{x} L N(x)<2.59$ for every real $x\in[x_0,U]$.

### Integrated prime error

Use $S(t)=\vartheta(t)-t$, $R(t)=\psi(t)-t$ and $w(t)=t^{-2}((\log t)^{-1}+(\log t)^{-2})$. Put $J(x)=\int_x^\infty R(t)w(t)dt$ and $K(x)=\int_x^\infty S(t)w(t)dt$. These improper integrals converge by the classical quantitative prime number theorem. Since $N=-\log f$ in Nicolas's notation, his **unconditional** Lemma 2.1 for $x\ge121$ gives
$$
N(x)\le -J(x)+\int_x^\infty(\psi(t)-\vartheta(t))w(t)dt+S(x)^2/(x^2L).
\tag{1}
$$
[Source: Nicolas, definitions (1.8), (1.9), (1.15)–(1.17) and Lemma 2.1](https://arxiv.org/abs/1202.0729)

For $\Re z<1$ write $F_z=\int_x^\infty t^z w(t)dt$. With $u=\log t$ use $u^{-1}+u^{-2}=\int_0^\infty(1+v)e^{-uv}dv$. Absolute convergence for each $z$ gives
$$
F_z=x^{z-1}\int_0^\infty\frac{(1+v)e^{-Lv}}{1-z+v}dv,
\qquad |F_z|\le\frac{x^{\Re z-1}}{|1-z| L}(1+1/L).
\tag{2}
$$
The classical von Mangoldt formula gives
$$
-J(x)=\sum_\rho F_\rho/\rho+
\int_x^\infty\left(\log(2\pi)+\tfrac12\log(1-t^{-2})\right)w(t)dt .
\tag{3}
$$
Here the sum ranges over signed ordinates with multiplicity and is absolutely convergent. To justify (3) without RH, first integrate on $[L,V]$ in the logarithmic variable. The distributional explicit formula pairs with this piecewise smooth weight by approximation: smooth the two endpoints with uniformly bounded total variation, then integrate the individual exponential terms by parts, giving a summable $O_{L,V}(1/(|\rho||1-\rho|))$ majorant. Bounded local integrability of $\psi(e^u)-e^u$ makes endpoint values immaterial. On the unsmoothed finite interval, integration by parts against $e^{-(1-\rho)u}$ and monotonicity of $u^{-1}+u^{-2}$ bound the integral by $2(1/L+1/L^2)x^{\Re\rho-1}/|1-\rho|$, uniformly in $V$. Dominated convergence as $V\to\infty$ proves the assertion. The last term in (3) is at most $\log(2\pi)F_0$.

For $|\Im\rho|\le H$ every zero is on the critical line by Platt and Trudgian. The exact classical Hadamard identity $\sum_\rho 1/(\rho(1-\rho))=2+\gamma-\log(4\pi)<0.047$ holds without RH. Every summand has positive real part because $\Re(\rho(1-\rho))=\Re\rho(1-\Re\rho)+(\Im\rho)^2>0$. Thus the low zeros contribute at most $0.047$ to $\sum1/(|\rho||1-\rho|)$ on that restricted set. For high zeros use the full signed-ordinate tail, without any location assumption:
$$
\sum_{|\Im\rho|>H}\frac1{|\rho||1-\rho|}
\le \sum_{|\Im\rho|>H}\frac1{(\Im\rho)^2}
\le \frac{\log(H/(2\pi))+1}{\pi H}
 +\frac{0.56(2\log H+1/2)}{H^2}<3.1\cdot10^{-12}.
\tag{4}
$$
This is Lehman's lemma as quoted by Brent, Platt and Trudgian with $\phi(t)=t^{-2}$, $A=0.28$, doubled for negative ordinates. The half-weight endpoint convention gives an upper bound for the strict tail. Equations (2)–(4) give
$$
\sqrt x L(-J)\le(1+1/L)
 \left(0.047+3.1\cdot10^{-12}\sqrt{x}+\log(2\pi)/\sqrt{x}\right).
\tag{5}
$$
[Platt–Trudgian verified height](https://arxiv.org/abs/2004.09765) · [Brent–Platt–Trudgian, Lemma 1 and footnote 1](https://arxiv.org/abs/2009.13791) · [Nicolas, Hadamard identity (1.3)](https://arxiv.org/abs/1202.0729)

### Prime powers and quadratic remainder

Büthe's Theorem 2 and the verified height give
$$
|\vartheta(v)-v|\le\sqrt v\,\log^2 v/(8\pi)\qquad(599<v\le U),
\tag{6}
$$
since $4.92\sqrt{U/\log U}<H$ and $v/\log v$ is increasing in this range. The ratio $\log^2v/\sqrt v$ is decreasing for $v>e^4$. Also $\vartheta(v)\le2v$ for all $v\ge1$: use induction on integers, since primes in $(m,2m]$ divide $\binom{2m}m$, and primes in $(m+1,2m+1]$ divide $\binom{2m+1}m$. Both binomials are at most $2^n$ with $n$ their top index; $2\lceil n/2\rceil+n\log2\le2n$ for $n\ge4$, and the smaller cases are direct. [Büthe, Theorem 2](https://arxiv.org/abs/1410.7015)

For $x_0\le t\le Y$, we have $\sqrt{x_0}\le\sqrt t\le10^{20}<U$. Equation (6) gives $\vartheta(\sqrt t)\le1.006\sqrt t$. The cubic powers contribute at most $2t^{1/3}$ and all powers of degree at least four at most $2t^{1/4}\log t/\log2$. Dividing by $\sqrt t$ gives
$$
(\psi(t)-\vartheta(t))/\sqrt t
\le1.006+2x_0^{-1/6}+2x_0^{-1/4}\log x_0/\log2<1.069 .
$$
For $t>Y$ the same argument with $2\sqrt t$ for the first term gives a bound $3\sqrt t$. Consequently
$$
\sqrt x L\int_x^\infty (\psi-\vartheta)w
\le 2(1+1/L)\big(1.069+3\sqrt{U/Y}\big).
\tag{7}
$$
The quadratic term on the right side of (1), after scaling, is at most $(\log x_0)^4/(64\pi^2\sqrt{x_0})$ by (6) and monotonicity. Substituting $L\ge\log x_0$ and $x\le U$ into (5), (7) and this last bound yields $\sqrt{x}L N(x)<2.59$.

### Cost of insufficient exponents

Take $n=\prod_{p\le x}p^{a_p}$ with integral $a_p\ge1$. Let $E=\sum(a_p-1)\log p$, $D=-\sum\log(1-p^{-(a_p+1)})$, $g(E)=\log\log(T+E)-\log\log T$. Direct factorization gives the exact log Robin ratio $N(x)-D-g(E)$.

By (6), $T\le1.00002x$ on our range. For $0\le v\le3\sqrt x$ one consequently has $g'(v)=1/((T+v)\log(T+v))\ge s=0.999/(xL)$. Thus if $E\ge3\sqrt x$ then $g(E)\sqrt x L\ge2.997$. Otherwise $D+g(E)\ge D+sE$. Every prime's contribution to this latter sum is at least $\min(s\log p,d_p)$ with $d_p=\log(1+1/(p(p+1)))$: if $a_p\ge2$ the extra mass alone pays $s\log p$; if $a_p=1$, the deficit $-\log(1-p^{-2})$ is at least $d_p$.

Set $y=\sqrt{2x}$, $y_0=\sqrt{2x_0}$. For $p\le y$, $d_p\ge1/(y^2+y+1)\ge0.97s\log y$ by $\log(1+u)\ge u/(1+u)$; it suffices to bound $0.97(0.999)(1+\log2/L)(1+1/y+1/y^2)<1$ at $L=\log x_0,y=y_0$. For $p>y$ one has $d_p\ge0.999/p^2$ and $s\log p\ge0.999/(2x)\ge0.999/p^2$. Hence
$$
D+sE\ge0.97s\vartheta(y)+0.999\sum_{y<p\le x}p^{-2}.
$$
For every $v\in[y,U]$, (6) gives $|\vartheta(v)-v|\le\eta v$ with $\eta=0.005$. Integrating $f(v)=v^{-2}/\log v$ against $d\vartheta(v)$ on $(y,x]$ and bounding both endpoint terms by $\eta v f(v)$ gives
$$
\sum_{y<p\le x}p^{-2}\ge(1-\eta)\int_y^x f(v)dv-2\eta/(y\log y).
$$
One integration by parts shows $\int_y^\infty f(v)dv\ge(1-1/\log y)/(y\log y)$, and $\int_x^\infty f(v)dv\le1/(x\log x)$. Combining these bounds and $\vartheta(y)\ge(1-\eta)y$ yields
$$
\begin{aligned}
\sqrt x L(D+sE)\ge{}&
0.97(0.999)(1-\eta)\sqrt2\\
&+\frac{0.999\sqrt2}{1+\log 2/\log x_0}
\left[(1-\eta)(1-1/\log y_0)-2\eta\right]
-\frac1{\sqrt{x_0}}>2.63.
\end{aligned}
$$
This proves strict Robin for all full-support profiles in the stated range.

### From prime support to all integers

For $5040<n\le\exp(2x_0)$ use Morrill and Platt's Theorem 13, which covers $n\le10^{10^{13.11485}}$. For a canonical integer $n>\exp(2x_0)$ whose largest prime is below $x_0$, we have $\sigma(n)/n\le M(x_0)$. The bound on $N(x_0)$ and $\vartheta(x_0)\le1.00002x_0$ give
$$
M(x_0)/e^\gamma\le \log(1.00002x_0)\exp(2.59/(\sqrt{x_0}\log x_0))<\log(2x_0)<\log\log n.
$$
Finally a canonical integer with largest prime greater than $U$ satisfies $\log n\ge\vartheta(U)>0.99U$ by (6). This exhausts all canonical integers through $\exp(0.99U)$. The reviewed reduction sends any hypothetical violation at $n>5040$ to a canonical violating integer still greater than 5040 and no larger than $n$. [Morrill–Platt, Theorem 13](https://arxiv.org/abs/1809.10813) · [Canonical reduction](../integrated/robin/finite-robin-foundations.md)
