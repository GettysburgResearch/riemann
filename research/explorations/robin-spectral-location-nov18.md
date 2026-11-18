# Where a sufficiently large Robin violation would force an off-line zero

**Proposed asymptotic theorem.** Put $H_0=3\cdot10^{12}$, $c_0=1/55.241$ and, for $H>e^e$, define
$$
B(H)=H^4\exp\!\left[0.14\left(\frac{\log H}{\log\log H}\right)^{1/3}\right].
$$
For every sufficiently large integer $n$ violating Robin's inequality, set $y=\log n$ and take the unique large $H$ with $B(H)=y$. Then some zeta zero $\rho=\beta+i\gamma$ satisfies
$$
H_0<\gamma\le H,\qquad
(\beta-1/2)\log\log n>26.99 .
\tag{1}
$$
Conversely, for all sufficiently large $H$, if RH has been verified through height $H$, Robin's inequality holds for **all** $5040<n\le\exp(B(H))$. The numerical lower cutoff implicit in “sufficiently large” is not computed here. The explicit finite ranges in the other notes use separate estimates. The coefficient $0.14$ can be replaced by any fixed number smaller than $8c_0$.

### High zeros beyond the verification height

Write $h=\log H$, $D=(h/\log h)^{1/3}$ and $Y=H^4 e^{dD}$, where $0<d<8c_0$. We claim, unconditionally,
$$
\sum_{|\gamma|>H}\frac{Y^{(\beta-1/2)_+}}{\gamma^2}=o(1)\qquad(H\to\infty).
\tag{2}
$$
The supplied estimates concern all zeta zeros with multiplicity. The global zero count is $O(t\log t)$. For $2/3\le\sigma\le1$ the uniform density estimate in equation (119) of Chourasiya and Simonič gives
$$
N(\sigma,t)\ll (\log t)^6 t^{(8/3)(1-\sigma)}.
$$
For $0.98\le\sigma\le1$, Bellotti's Theorem 1.2 gives the stronger uniform estimate $N(\sigma,t)\ll(\log t)^{12}t^{58(1-\sigma)^{3/2}}$. Finally every high zero satisfies $1-\beta\ge c_0 (\log |\gamma|)^{-2/3}(\log\log|\gamma|)^{-1/3}$ by Mossinghoff, Trudgian and Yang. [Density estimate (119) and Table 4](https://arxiv.org/abs/2507.15184) · [Bellotti, Theorem 1.2](https://arxiv.org/abs/2311.05136) · [Verified coefficient in the zero-free region](https://arxiv.org/abs/2212.06867)

Divide positive ordinates into $(t,2t]$ with $t=2^jH$, $u=\log(t/H)=j\log2$. Negative ordinates double the estimate. Terms with $\beta\le2/3$ cost altogether $O(Y^{1/6}\log H/H)=o(1)$. For the rest use layer integration
$$
Y^{\beta-1/2}=Y^{1/6}+\log Y\int_{2/3}^{\beta}Y^{\sigma-1/2}d\sigma.
$$
The first term has the same preceding bound. In the integral put $\delta=1-\sigma$. For each dyadic slice majorize its weighted integrand by $t^{-2}Y^{1/2-\delta}N(\sigma,2t)$. The integration is empty for $\delta<c_0(\log(2t))^{-2/3}(\log\log(2t))^{-1/3}$. Whenever the usable density exponent is $A\delta$ (that is $N\ll (\log(2t))^{12}(2t)^{A\delta}$), the exponent of the bound, excluding logarithmic factors, is at most
$$
dD/2-(4-A)\delta h-(2-A\delta)u+O(1).
\tag{3}
$$
The omitted term $-\delta dD$ is nonpositive.

Pick $\epsilon>0$ with $(4-\epsilon)c_0>d/2$, and $\delta_0>0$ small enough that $\delta_0<0.02$ and $58\sqrt{\delta_0}<\epsilon$ (taking $\epsilon<1$ causes no loss). For $\delta\ge\delta_0$ use $A=8/3$ and $\delta\le1/3$: (3) is $\le-c h-u$ for all sufficiently large $H$, with $c>0$. For $0<\delta<\delta_0$, use $A=\epsilon$. When $u\ge 2(d+1)D$ the bound is $\le-c'D-u$ for some $c'>0$, using $2-\epsilon\delta_0>3/2$. When $0\le u<2(d+1)D$, the zero-free region gives $\delta h\ge(c_0-o(1))D$ uniformly, and (3) is again at most $-c''D-u$. Multiplication by the polynomial factors $O((h+u+1)^{12}\log Y)$, integration over $\sigma$, and summation over $j$ preserve convergence to zero, since $D/\log h\to\infty$. This proves (2).

### Low zeros and the all-integer implication

Use the [arbitrary-integer tangent](robin-tangent-nov18.md) at $v=y$. By the prime number theorem and its local exponent lower bound (2),
$$
\liminf_{y\to\infty}\sqrt y\log y\,A(y)\ge2\sqrt2 .
$$
In detail, use the same proof on $[\sqrt{2y},M\sqrt{2y}]$ at any fixed $M>1$, take $y\to\infty$ and then $M\to\infty$. Moreover $(\psi(t)-\vartheta(t))/\sqrt t\to1$ by the prime number theorem at $\sqrt t$ and the elementary bound on higher powers. Hence the corresponding normalized prime-power term in $-K(y)$ tends to 2 by integration against $w(t)$, and the archimedean remainder tends to zero. The absolute zero contributions after scaling are bounded by
$$
(1+1/\log y)\sum_\rho \frac{y^{\beta-1/2}}{|\rho||1-\rho|}.
\tag{4}
$$
Above $H$ use (2). The verified zeros through $H_0$ contribute less than $0.046192$ to the sum in (4), by the positive-real-part Hadamard argument in the [finite-horizon proof](robin-finite-horizon-nov18.md). The full signed reciprocal-square tail past $H_0$ is below $2.96\cdot10^{-12}$ by the unrounded Lehman bound (4) in that proof. These constants also bound the sum with denominators $|\rho||1-\rho|$ in the respective ranges.

If (1) fails, every zero with $H_0<|\gamma|\le H$ obeys $|\beta-1/2|\log y\le26.99$, since reflection across the critical line preserves ordinates in this band. The denominators in each reflected pair are equal, so the average of $y^{\beta-1/2}$ over the pair is at most $\cosh(26.99)$. A critical-line singleton also obeys this bound. Together with all prime powers and the entire high tail, the normalized upper bound on $-K(y)$ is thus at most
$$
2+0.046192+2.96\cdot10^{-12}\cosh(26.99)+o(1)<2\sqrt2 .
$$
The tangent inequality contradicts a Robin violation, proving (1).

For the verification-to-range statement, if every zero through $H$ lies on the critical line, its entire contribution to the sum in (4) is $<0.047$, uniformly in $y$. The high tail is $o(1)$ uniformly for $1\le y\le B(H)$ by (2). Thus the same argument works for all sufficiently large $y$ with constants independent of $H$. To cover the fixed lower interval directly, on $y\ge9\cdot10^{21}$ the explicit tangent cost exceeds $2.72$ using $|\vartheta(t)-t|\le0.0001t$ for all $t\ge\sqrt{9\cdot10^{21}}$. This all-range estimate follows by joining Büthe through $e^{55}$ to Morrill–Platt Lemma 6 above $e^{55}$. The explicit normalized prime-power bound is then $2(1.002)(1+1/\log(9\cdot10^{21}))$, uniformly in $y$; the archimedean term is $O(y^{-1/2})$ with coefficient less than 2 there. These bounds leave room for $0.047(1+1/\log y)$ and the $o(1)$ tail as $H\to\infty$. The known [finite range](robin-finite-horizon-nov18.md) covers all smaller $n$. [Morrill–Platt, Lemma 6](https://arxiv.org/abs/1809.10813)

### Coupling the real part to the ordinate

The witness in (1) can also satisfy
$$
(\beta-1/2)\log y\ge (2-D(\beta))\log\gamma-15\log\log y,
\tag{5}
$$
where a uniform density exponent on $[1/2,1]$ is
$$
D(\sigma)=\min\left(1,\frac{3(1-\sigma)}{2-\sigma},
\frac83(1-\sigma),58(1-\sigma)^{3/2}\right).
$$
Indeed the global count, Corollary 1 and equation (119) of Chourasiya–Simonič, and Bellotti's Theorem 1.2 give $N(\sigma,t)\ll t^{D(\sigma)}(\log t)^{12}$ for $t\ge H_0$. In the subintervals where the last two theorems do not apply, their displayed exponents are larger than one of the available exponents. The finite minimum defining $D$ is Lipschitz. The version of $N$ counting strict inequalities in real parts gives the same bound for inclusive endpoints by approaching $\sigma$ from below whenever needed (the global count handles $\sigma=1/2$).

Retain the “narrow band” $|\beta-1/2|\log y\le26.99$ in the low-ordinate estimate just proved. The unverified left-side zeros outside that band contribute at most $2.96\cdot10^{-12}$, since $y^{\beta-1/2}\le1$ and $|\rho||1-\rho|\ge\gamma^2$; this leaves the displayed strict numerical margin intact. For the right-side zeros outside the band and below $H$, split ordinates into dyadic intervals $(t,2t]$ starting at $H_0$, and real parts into bins $[\sigma,\sigma+1/\log y]$. If every such zero fails (5), then its individual weight $y^{\beta-1/2}/\gamma^2$ is at most
$$
\gamma^{-D(\beta)}(\log y)^{-15}
\ll t^{-D(\sigma)}(\log y)^{-15},
$$
since $\log(2t)=O(\log y)$ and $D$ is Lipschitz. With multiplicities, the whole cell contributes $O((\log y)^{-3})$ by the density bound. There are $O((\log y)^2)$ cells, giving $o(1)$ in total. The tail above $H$ already costs $o(1)$ by (2). The contradiction to the exponent cost proves the simultaneous assertion.

### Unbounded arithmetic families excluded by the same estimate

Let $y=\log n$, $L=\log y$ and $W=L^{3/5}(\log L)^{-1/5}$. Put
$$
C_*=5\left(\frac{c_0}{3}(5/3)^{1/3}\right)^{3/5}>0.2580 .
$$
For every $0<c<C_*$ and all sufficiently large $n$, any violation must satisfy
$$
\operatorname{lcm}(1,2,\ldots,\lfloor e^{cW}\rfloor)\mid n .
\tag{6}
$$
In particular this gives an unbounded family on which Robin's inequality is strict, including integers with unbounded prime support and growing prime-power exponents. More generally, write $a_p=v_p(n)$, including zero when $p\nmid n$. With constants depending on $c$, a violating integer must satisfy
$$
\sum_{p\le y/2}p^{-(a_p+1)}
 +\frac{1}{yL}\sum_{p\le y/2}(a_p-1)_+\log p
 +\frac{1}{yL}\sum_{p\ge 2y}a_p\log p
 \ll_c \frac{e^{-c W}}{L}.
\tag{7}
$$

To see the analytic input, the same dyadic density argument now gives
$$
\sum_\rho \frac{y^{\beta-1}}{|\rho||1-\rho|}\ll_c e^{-cW}.
\tag{8}
$$
Here are details of the exponent optimization. In a dyadic ordinate interval $(e^h,2e^h]$ and a real-part layer $\sigma=1-\delta$, the cost is at most polynomial factors in $h,L$ times $\exp[-2h-\delta L+(8/3)\delta h]$ for $\delta\le1/3$. Layers below $2/3$, including the baseline of the layer integral, cost $O(y^{-1/3})$ after summing reciprocal squares. For $h>KW$ the trivial inverse-square tail is $O((KW+1)e^{-KW})$, negligible on choosing large fixed $K$. For $h\le KW$ the density term $(8/3)\delta h=o(\delta L)$ uniformly. The zero-free region at $2e^h$ then bounds the exponent by
$$
-2h-(c_0-o(1))L(h+\log2)^{-2/3}(\log(h+\log2))^{-1/3}.
$$
Fixed low heights have a fixed zero-free margin and cost $O(e^{-c'L})$. If $h/W\to0$, the second term divided by $W$ tends to $-\infty$; this follows by $\log(h+\log2)\le(3/5+o(1))\log L$ on the range in question. On a fixed compact positive interval for $h/W$, put $h=bW$ to find the limiting cost exponent per $W$
$$
2b+c_0(5/3)^{1/3}b^{-2/3},
$$
whose minimum over $b>0$ is $C_*$. There are only $O(W)$ dyadic intervals before the tail and elementary partial integration costs at most a polynomial in $L,h$. All such factors are absorbed by the strict slack $c<C_*$. This proves (8).

In the proof of the arbitrary-integer tangent inequality, denote the individual loss for $p\le y$ by
$$
\ell_p=b_p-s_y\log p-[\log I_p(a_p)-s_y a_p\log p].
$$
It is nonnegative. For $p\le y/2$ and $a_p=0$ it is at least $1/p-1/y\ge1/(2p)$; for $a_p\ge1$ it equals $-\log(1-p^{-(a_p+1)})+s_y(a_p-1)\log p$. The price beyond $y$ is also nonnegative and for $p\ge2y$ it is at least $(s_y/2)a_p\log p$, since every incremental log gain is at most $1/p\le(s_y/2)\log p$. At a violation the total losses are at most $-K(y)$ by the exact tangent identity and the positive omitted tail. The prime-power and archimedean terms in $-K(y)$ are $O(y^{-1/2}/L)$; (8) and the integrated zero formula bound the rest by $O_c(e^{-cW}/L)$. This proves (7). If a prime power $p^k\le e^{cW}$ failed to divide $n$, then $p^{-(a_p+1)}\ge e^{-cW}$, contradicting (7) for sufficiently large $n$. This proves (6). The upper bound on the positive part of the log Robin ratio itself is also $O_c(e^{-cW}/L)$ without assuming a violation.
