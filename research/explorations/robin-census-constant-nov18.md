# A sharp counting constant for integers near Robin's bound

**Proposed theorem.** Fix $1/2\le a<1$. Let $V_a(N)$ count $5040<n\le N$ such that
$$
 B(n):=\log\frac{\sigma(n)}{e^{\gamma_E}n\log\log n}\ge -(\log n)^{a-1}.
$$
Write $\Theta=\sup_\rho\Re\rho$. If $\Theta\le a$, then
$$
 \log V_a(N)\sim \pi\sqrt{\frac23}\,
 \frac{(\log N)^{(1+a)/2}}{\sqrt{\log\log N}}.
 \tag{1}
$$
If $\Theta>a$, the ratio of the left side to the right side tends to infinity by the [strict-violation counting theorem](robin-violation-count-nov18.md). In particular (1) at $a=1/2$ is equivalent to RH. The proof of (1) uses the explicit formula and arithmetic counting, independently of the oscillation arguments needed for its converse. The comparison with earlier work on strict violations is in the linked counting note.

## The arithmetic budget

In the remainder assume $\Theta\le a$. Set $x=\lfloor\log n\rfloor$, $y=\log n$, $s=1/(x\log x)$, and $I_p(j)=\sum_{k=0}^j p^{-k}$. Relative to the baseline $b_p-s\log p$ for $p\le x$, where $b_p=-\log(1-1/p)$, and zero for $p>x$, define the deficit $D_x(n)$ as the sum of the baselines minus $\log I_p(v_p(n))-s v_p(n)\log p$. All local deficits are nonnegative by the [tangent argument](robin-tangent-nov18.md). Its exact identity gives
$$
 B(n)=-K(x)-R(x)-D_x(n)+\log\log x+s(y-x)-\log\log y .
 \tag{2}
$$
Here $R\ge0$. Uniformly, $|K(x)|\ll x^{\Theta-1}/\log x$. Indeed $K$ uses $\vartheta$ while the integrated explicit formula for $J$ uses $\psi$; the difference costs $O(x^{-1/2}/\log x)$ by $\psi(t)-\vartheta(t)\ll\sqrt t$. Each zero contributes $O(x^{\Re\rho-1}/(|\rho||1-\rho|\log x))$ by integration by parts in the integrated formula, and the reciprocal weights are summable. The archimedean contribution is $O(1/(x\log x))$. [Integrated formula](robin-finite-horizon-nov18.md)

The last three terms after $D_x(n)$ in (2) form a tangent error $O(1/(x^2\log x))$ since $0\le y-x<1$. Thus every counted $n$ has $D_x(n)\le (1+o(1))E$, where $E=x^{a-1}$. Put
$$
 r=(1+a)/2,\qquad h=x^r\sqrt{\log x},\qquad S=h/\log x,
 \qquad \lambda=t x^2/h
$$
for a fixed $t>0$, so $\lambda E=tS$. The local costs for omitting a prime below $x$ and inserting one above $x$ are respectively
$$
 w_p=b_p-s\log p\quad(p\le x),\qquad
 w_p=s\log p-\log(1+1/p)\quad(p>x).
$$
At $p\le x$ the deficit for exponent $j\ge1$ is at least $(j-1)s\log p$. At $p>x$, subsequent increments of $\log I_p(j)$ after $j=1$ cost at most $p^{-2}\le s\log p/2$ for large $x$. Summing nonnegative products over all integers therefore gives
$$
 \sum_n e^{-\lambda D_x(n)}
 \le \zeta(\lambda s/2)\prod_p(1+e^{-\lambda w_p}).
 \tag{3}
$$
Here $\lambda s\to\infty$. Although the sum includes all integers at fixed $x$, it bounds the count in the required bin $x\le\log n<x+1$ after multiplication by $\exp((1+o(1))\lambda E)$.

## Evaluation of the partition product

For each fixed $M>0$ and $|p-x|\le Mh$, put $u_p=|p-x|/h$. Differentiation of the two local costs gives uniformly $\lambda w_p=tu_p+o(1)$. On either side the measures $S^{-1}\sum_{u_p\le M}\delta_{u_p}$ converge to Lebesgue measure on $[0,M]$. In fact $\vartheta(v)=v+O_\alpha(v^\alpha)$ for any $\Theta<\alpha<r$, and $h\gg x^\alpha\log x$ at fixed $\alpha<r$. Partial summation proves the claim and bounds the prime count on each length-$h$ subinterval of $[x/2,2x]$ by $O(S)$.

On this larger interval $w_p\gg (|p-x|-2)/x^2$, by the same derivatives. The log product from $Mh<|p-x|\le x$ there costs $O_t(Se^{-c_t M})$. For $p<x/2$ use $w_p\ge1/x$. For $p>2x$ use $w_p\ge (s/2)\log p$ and sum over all integers beyond $2x$. Both tails are $o(1)$ since $x/h$ grows as a positive power of $x$. It follows by letting $M\to\infty$ that
$$
 S^{-1}\sum_p\log(1+e^{-\lambda w_p})\longrightarrow
 2\int_0^\infty\log(1+e^{-tu})\,du=\frac{\pi^2}{6t}.
$$
Consequently the log count in the bin is at most $(t+\pi^2/(6t)+o(1))S$. Take $t_0=\pi/\sqrt6$ and sum over the at most $1+\log N$ bins using eventual monotonicity of $S$. This proves the upper bound in (1).

## A matching family of actual integers

Write $Y=\log N$ and now take $x=Y-Y^r(\log Y)^2$. Start at $m=\operatorname{lcm}(1,\ldots,\lfloor x\rfloor)$ with $y_0=\log m=\psi(x)$. The [LCM identity](robin-lcm-nov18.md) and the integrated bound for $J$ above give $B(m)\ge-O(x^{\Theta-1}/\log x)= -o(E)$. Fix $M>0$. Permit each prime $x-Mh\le p\le x$ to be deleted once, and each prime $x<p\le x+Mh$ to be inserted once. A prime in the first range occurs to exponent one in $m$, so distinct configurations give distinct integers. The prime count proves $|\log n-y_0|=O_M(h)$ for every configuration. Also $y_0=x+O_\alpha(x^\alpha)$ with $\Theta<\alpha<r$. All the resulting integers lie below $N$.

By concavity of $v\mapsto\log\log v$, linearizing at $y_0$ bounds the total loss in $B$ from above. Replacing that slope by $s$ costs $O_{M,\alpha}(x^{\alpha-2}h/\log x)=o(E)$. For either a deletion or an insertion the resulting loss is $(h/x^2)(u_p+o(1))$ uniformly for $u_p\le M$, by Taylor expansion of $\log(1+1/p)-s\log p$. The sum of uniform errors is $o(E)$ since there are $O_M(S)$ possible toggles and $hS/x^2=E$. Thus it suffices for inclusion that $\sum_{p\text{ toggled}}u_p\le (1-\epsilon)S$ for any fixed $\epsilon>0$. The threshold tolerance uses $\log n\sim x$ uniformly.

Choose the toggles independently with probabilities $(1+e^{tu_p})^{-1}$ for a fixed $t>t_0$. The mean of their sum of $u_p$, divided by $S$, tends to
$$
 b_M(t)=2\int_0^M\frac{u}{1+e^{tu}}du
 \le\frac{\pi^2}{6t^2}<1.
$$
The variance is $O_M(S)$. With probability tending to one the sum divided by $S$ differs from $b_M(t)$ by $o(1)$, for example within the mean error plus $S^{-1/4}$. Each such configuration has negative log probability
$$
 S\left(2\int_0^M\log(1+e^{-tu})du+t b_M(t)+o(1)\right),
$$
by the product law. The number of eligible configurations has log at least this leading exponent, since their total probability tends to one. Let $M\to\infty$ and then $t\downarrow t_0$. The resulting lower constant is $\pi^2/(3t_0)=\pi\sqrt{2/3}$, and $S\sim Y^r/\sqrt{\log Y}$. This proves (1).
