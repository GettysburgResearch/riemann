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

## At the natural Robin scale the count retains the zero frequencies

Assume RH for this section. Fix a real number $b$ and let $L_b(x)$ count integers with $|\log n-x|\le x^{3/4}\log x$ and
$$
 B(n)\ge -b/(\sqrt{\log n}\log\log n).
$$
Set $F(t)=\sum_\rho e^{i\gamma t}/|\rho|^2$, counting both signs and all multiplicities. This is a real uniformly almost-periodic function since the coefficients are absolutely summable. The local statement, with an error tending to zero along every real $x\to\infty$, is
$$
 \frac{\log x}{x^{3/4}}\log(1+L_b(x))
 = \pi\sqrt{2/3}\,\sqrt{[b+2-2\sqrt2+F(\log x)]_+}+o(1).
 \tag{4}
$$

**Cost that must be paid by every exponent profile.** Put $E_0=1/(\sqrt x\log x)$. The tangent estimate charges the primes $p\le x/2$ at least $A(x)=\sum\min(s\log p,p^{-2})$. The crossing $q^2\log q=x\log x$ has $q\sim\sqrt{2x}$. The two sums $s\vartheta(q)$ and $\sum_{q<p\le x/2}p^{-2}$ are each asymptotic to $\sqrt2 E_0$ by the prime number theorem. Omitting $p>x^{2/3}$ costs $O(x^{-2/3})=o(E_0)$. Thus the small primes alone consume $(2\sqrt2+o(1))E_0$. Equation (2) and the [integrated critical-line formula](robin-lcm-nov18.md) give $-K(x)/E_0=2+F(\log x)+o(1)$: the square primes account for $2$, and integration of the critical zeros gives $F$. In each unit bin described by (2), the remaining primes therefore have total deficit at most $[b+2-2\sqrt2+F(\log x)+o(1)]E_0$.

There are at most $\exp(O(x^{2/3}\log x))$ choices for the exponents below $x^{2/3}$ since each exponent is $O(x)$. This is negligible on the log count scale $S=x^{3/4}/\log x$. Use (3) on the other primes with $h=x^{3/4}$, $\lambda=tx^2/h$. The same partition-product limit holds with this $S$ and $\lambda E_0=tS$, since RH gives the needed prime number theorem on intervals of length $h$. For a fixed nonnegative residual budget $g$, optimization gives $\inf_{t>0}(tg+\pi^2/(6t))=\pi\sqrt{2g/3}$. These upper bounds are uniform over the bounded range of residual budgets: first cover $g\ge\epsilon$ by finitely many slopes to any fixed accuracy, and use the slope optimal for $\epsilon$ when $g<\epsilon$. Negative budgets exclude the bin. In summing over the polynomially many bins of the slab, $F(\log x)$ changes by $o(1)$ uniformly, by uniform continuity. This proves the upper bound in (4).

**A matching exponent profile.** Start from the LCM and multiply by $\prod_{\sqrt x<p\le\sqrt{2x}}p$. This raises the specified exponents from one to two. The extra log abundancy is $\sum\log(1+1/(p^2+p))=(2-\sqrt2+o(1))E_0$ by the prime number theorem. The extra log of the integer is $(\sqrt2-1+o(1))\sqrt x$ and increases $\log\log(\log n)$ by $(\sqrt2-1+o(1))E_0$. The [LCM formula](robin-lcm-nov18.md) gives its original log Robin ratio $(F(\log x)-1+o(1))E_0$. Thus the modified integer starts at $(F(\log x)+2-2\sqrt2+o(1))E_0$ and its log differs from $x$ by $O(\sqrt x\log^2x)$.

Toggle primes within $Mh$ of $x$ as in the preceding lower bound. The linearization error from using $s$ is $o(E_0)$ uniformly over all toggles, by the preceding bound on the log of the modified integer; their total log change is $O_M(h)$. All configurations fit inside the stipulated slab. To see uniformity when the available budget varies with $x$, pass along any subsequence on which $g=b+2-2\sqrt2+F(\log x)$ converges. For a strictly positive limit the Bernoulli proof above works with $\pi^2/(6t^2)$ tending to that limit from below, giving $\pi\sqrt{2g/3}$ in the limit. A nonpositive limit requires only the trivial lower bound zero. Compactness proves (4) along all $x$.

For $b=1$ the positive part can be removed: $|F|\le 2+\gamma_E-\log(4\pi)<0.047<3-2\sqrt2$. Under RH, squaring the normalized log count and subtracting its known constant thus recovers $F(\log x)$ up to $o(1)$. Its Fourier–Bohr mean at any nonzero frequency $\gamma$ is the critical-zero multiplicity at that ordinate divided by $1/4+\gamma^2$. The arithmetic count uses just $\sigma(n)$ and $n$. Quantitative recovery from a finite interval would require estimates for the remainder and for separation of frequencies.

## The same asymptotics in short intervals at every prescribed integer scale

For $x=\log N$ and any nonnegative function $d(x)=o(\sqrt x)$, replace the slab in (4) by the one-sided interval
$$
 N\le n\le N\big(1+e^{-d(x)}\big).
 \tag{5}
$$
The full formula (4), including its constant and varying profile, still holds for this count under RH. For the tolerance in (1) and $\Theta\le a$, the same replacement gives (1) even for every $d(x)=o(x^a\log x)$. These statements concern every sufficiently large real $N$, with the tolerances evaluated at each actual integer as before.

The upper estimates apply by inclusion in the slab or by the bound on the one or two unit log bins. For the lower bound, use the central $x=\log N$ for the prime toggles instead of backing away from the right endpoint. Choose $D\to\infty$ with $D\ge d(x)$, $D\gg\sqrt S\log x$ with ratio tending to infinity, and $D=o(\sqrt x)$ at the natural tolerance or $D=o(x^a\log x)$ at the tolerance in (1). This is possible because the standard-deviation exponent $r/2=(1+a)/4$ is strictly below $a$, and in the natural case $3/8<1/2$. In both cases $D=o(S)$ and $D=o(h)$.

Keep $M,t$ fixed in a lower-bound ensemble with a fixed positive slack in its budget. Give each toggle the slightly altered probability
$$
 q_p(\beta)=(1+\exp(tu_p-\beta\epsilon_p))^{-1},\qquad
 \epsilon_p=\begin{cases}1,&p>x,\\-1,&p\le x.\end{cases}
$$
The mean log of the uncorrected integer $n'$ is the log of the starting integer plus $\sum\epsilon_p q_p(\beta)\log p$. At $\beta=0$ this is $x+o(h)$ by the equal limiting prime measures on both sides and the bounds on the starting integer. The derivative in $\beta$ is $\sum q_p(1-q_p)\log p\asymp_{M,t} h$ on $|\beta|\le1$ (take $M>0$). Thus one can choose $\beta=o(1)$ to make the mean exactly $x-2D$. The variance of $\log n'$ is $O_M(S\log^2x)=o(D^2)$. With probability tending to one, $x-3D\le\log n'\le x-D$. The change of tilt by $o(1)$ modifies the mean energy by $o(S)$ in the units $u_p$, and modifies the negative log probability of each configuration by $o(S)$ uniformly, so the entropy lower bound and the positive slack persist.

Set $k=\lceil N/n'\rceil$ and use the actual integer $n=kn'$. It satisfies (5) since $n'\le N e^{-D}$. The ratio $\sigma(n)/n$ is nondecreasing under divisibility, even when $k$ shares factors with $n'$. The change of $\log\log(\log n)$ is $O(D/(x\log x))$, negligible compared with the slack at the respective tolerance. All resulting integers therefore qualify. For each fixed output $n$, its input $n'$ is determined by $k\le e^{3D}+1$, so collisions cost at most $3D+O(1)=o(S)$ in log cardinality. This proves the lower bounds. In (4) use the subsequence argument for positive limiting budget as before.

## A certified finite interval

At the actual integer $N=10^{4,342,945}$ there are **more than $10^{1145}$ distinct integers** in $[N,(1+5\cdot10^{-48})N]$ satisfying
$$
 -1 < B(n)\sqrt{\log n}\log\log n <0 .
$$
The lower inequality is an unconditional directed computation. Strict negativity throughout this finite range also follows from the published Morrill–Platt verification quoted in the [finite Robin note](robin-finite-horizon-nov18.md).

Take $x=10^7$ and the modified LCM of the preceding proof. Pair the 4,000 nearest primes below $x$ with the 4,000 nearest above, in order of increasing distance on their respective sides. In each pair either retain the low prime or replace it with the high prime. The $2^{4000}$ resulting integers $n'$ are distinct. Their largest possible log is $9,999,891.490$ rounded up, and their smallest possible log is $9,999,865.561$ rounded down. The minimum abundancy and maximum log both occur when every pair is switched. Multiply each by $\lceil N/n'\rceil$ as above. The [128-bit certificate](check_robin_entropy_family_nov18.py) gives relative overshoot below $4.939\cdot10^{-48}$. Using the minimum abundancy and the upper endpoint of the final interval gives normalized log Robin ratio greater than $-0.994991$. Dividing the configuration count by the maximum possible compensating multiplier gives a base-ten log count greater than $1145.5529$. The checker sums over an ordinary sieve of primes and prime powers and certifies all bounds jointly without enumerating the configurations.
