# Optimizing all exponents at a prescribed largest prime

**Status.** Proposed asymptotic lemma, unreviewed. The arithmetic input is the prime number theorem in the forms $\vartheta(y)\sim y$ and $\pi(y)\sim y/\log y$. The structural starting point is the [reviewed canonical reduction](../integrated/robin/finite-robin-foundations.md) at main commit `f99d9e3`. No global sign claim follows.

Let $x$ tend to infinity through primes. Take all integers with prime divisors exactly the primes $p\le x$, allowing arbitrary positive integral exponents $a_p$. Write $T=\vartheta(x)$, $E=\sum_{p\le x}(a_p-1)\log p$, and $D=\sum_{p\le x}-\log(1-p^{-(a_p+1)})$. In the following, $x\ge5$, so $T>1$. The exact best logarithmic Robin ratio on this support is
$$
\max_n \log\frac{\sigma(n)}{e^\gamma n\log\log n}
=N(x)-C(x),\qquad
N(x)=\log\prod_{p\le x}(1-1/p)^{-1}-\gamma-\log\log T,
$$
where $C(x)=\min_a [D+g(E)]$ and $g(u)=\log\log(T+u)-\log\log T$. The minimum exists since $g(u)\to\infty$ and bounded $E$ gives finitely many profiles.

**Proposition.** Define $b=1/(T\log T)$ and
$$
d_{pj}=\log\frac{1-p^{-(j+1)}}{1-p^{-j}},
\qquad A(x)=\sum_{p\le x}\sum_{j\ge2}\min\{b\log p,d_{pj}\}.
$$
Then
$$
C(x)=A(x)-\frac{1+o(1)}{x\log x}.
$$
The $o(1)$ is unconditional as $x\to\infty$ and involves no exponent cap. Both the linearized and true minimizers satisfy $E\sim\sqrt{2x}$. The series in $A$ is explicitly summable in each prime after its last threshold crossing by telescoping. Retaining the actual prime sum is essential to resolving the displayed curvature term.

**Proof.** For any slope $s>0$, the minimum of $D+sE$ is exactly the sum defining $A$ with $s$ in place of $b$. Indeed $-\log(1-p^{-(a+1)})=\sum_{j>a}d_{pj}$. Including level $j\ge2$ incurs $s\log p$ in place of $d_{pj}$. The gains $d_{pj}=\log(1+(1-1/p)/(p^j-1))$ decrease strictly with $j$, so every collection of cheaper levels is an admissible initial segment, with either choice at a tie.

We show that whenever $s/b\to1$, **every** linear minimizer has $E\sim\sqrt{2x}$. Level two is included if $d_{p2}>s\log p$. Since $d_{p2}\sim p^{-2}$ and $s\sim1/(x\log x)$, for each fixed $0<\epsilon<1$ it includes all $p<(1-\epsilon)\sqrt{2x}$ and excludes all $p>(1+\epsilon)\sqrt{2x}$ for sufficiently large $x$. This follows uniformly by bounding $p^2d_{p2}$ between $1\pm\delta$ for $p$ sufficiently large, using monotonicity of $p^2\log p$, and treating the finitely many smaller primes individually. The prime number theorem then gives the claimed mass for level two. For $j\ge3$ inclusion requires $p^j\le Kx\log x$ for an absolute $K$, since $d_{pj}\le 2p^{-j}$ and $\log p\ge\log2$. Thus $j=O(\log x)$ and the total additional level mass is $O((x\log x)^{1/3}\log x)=o(\sqrt x)$ by $\vartheta(y)=O(y)$.

To localize the nonlinear minimum, use the trial profile with exponent $\lceil\log x/\log p\rceil$ for $p\le\sqrt x$ and one elsewhere. It has $E=O(\sqrt x\log x)$ even by trivial prime counting, and $D=O(x^{-1/2})$ by summing $2/x$ at small primes and $2/p^2$ beyond $\sqrt x$. Therefore $C(x)=O(x^{-1/2})$. Every nonlinear minimizer satisfies $0\le g(E)\le C(x)$, which implies $\log(1+E/T)\le(\exp C(x)-1)\log T=o(1)$, hence $E=o(T)$. At such a minimizer its tangent slope $s=g'(E)=1/((T+E)\log(T+E))$ satisfies $s/b\to1$. By concavity, the tangent majorizes $g$ globally with equality at this profile. Consequently this same profile minimizes $D+sE$ and the preceding mass estimate applies.

Finally $g''(u)=-(\log(T+u)+1)/((T+u)^2\log^2(T+u))$. Taylor's theorem gives $g(E)-bE=-(1+o(1))/(x\log x)$ at either a nonlinear minimizer or a linear minimizer at slope $b$. Evaluating the nonlinear objective on the linear minimizer gives the upper bound, and evaluating $D+bE\ge A(x)$ on the nonlinear minimizer gives the lower bound. This proves the formula.

**Remaining arithmetic estimate.** An eventual bound $N(x)\le A(x)-(1+\delta)/(x\log x)$ for some fixed $\delta>0$ would settle all sufficiently large supports, with the starting threshold and the other supports still to address. The proposition supplies the exponent optimization term. It supplies no such upper bound on $N(x)$, whose fluctuations depend on the actual primes.

**Numerical check.** An exploratory binary64 calculation gave the following values of $(A-C)x\log x$ at primes $101,1009,10007,100003,1000003$, respectively: $2.1530,2.1231,1.5911,1.4385,1.2882$. To reproduce it, start at the minimizing profile for slope $b$ and compute its true cost $c=D+g(E)$. All global minimizers have $E\le U=T(\exp((\exp(c)-1)\log T)-1)$. Enumerate the crossings $d_{pj}/\log p$ from $b$ down to $g'(U)$, updating $D$ and $E$ by $-d_{pj}$ and $\log p$. Take the least true cost along the list. Equal crossings permit a simultaneous jump because the objective along tied marginal additions is concave in the accumulated extra mass and its minimum occurs at an endpoint. These floating-point checks carry no sign-certification weight.

## Locating the nonlinear optimizer more tightly

There is also an error estimate for evaluating the *true* cost on the explicit linear optimizer. For any minimizer at slope $b$ with excess $E_b$ and deficit $D_b$, put $c_b=D_b+g(E_b)$. Then
$$
0\le c_b-C(x)=O\!\left(\frac{\log\log x}{x^{3/2}}\right).
$$
This gives a directly computable approximation with a smaller asymptotic error than the leading curvature correction.

To prove this, take a nonlinear minimizer with excess $E_*$ and slope $s_*=g'(E_*)$. From $E_*\sim\sqrt{2x}$ one has $b/s_*=1+O(x^{-1/2})$. Every differing level between the two minimizers therefore has
$$
s_*\le h_j(p):=d_{pj}/\log p\le b .
$$
For real $p\ge2$ put $u=(1-1/p)/(p^j-1)$, so $d_{pj}=\log(1+u)$. Then
$$
-\frac{d\log u}{d\log p}=\frac{jp^j}{p^j-1}-\frac{1}{p-1}\ge j-1.
$$
Since $u\le1/3$ and $u/((1+u)\log(1+u))\ge1/(1+u)$, it follows that $-d\log h_j/d\log p\ge3(j-1)/4$. For each $j$ the possible primes in this slope interval thus lie in a single interval of relative width $O(x^{-1/2}/j)$. Their largest possible value is $O(\sqrt x)$ uniformly: for $j=2$ the threshold asymptotic above applies, and for $j\ge3$ one has $p\le(Kx\log x)^{1/3}$. Each interval therefore contains $O(1)$ integers. Moreover $j\log p\le\log(Kx\log x)$ and $j=O(\log x)$. Adding the possible weights over levels yields
$$
0\le E_*-E_b=O(\log x\log\log x).
$$
Here the included sets nest because $s_*<b$ for large $x$, irrespective of choices at ties. Since the linear objective at slope $b$ is minimized at $E_b$, integration of $b-g'(u)$ along $[E_b,E_*]$ gives
$$
c_b-C(x)\le (b-s_*)(E_*-E_b).
$$
Substituting $b-s_*=O(x^{-3/2}/\log x)$ proves the estimate.
