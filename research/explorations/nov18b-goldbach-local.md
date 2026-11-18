# Localizing both signs of the centered Goldbach convolution with positive divided differences

Let $B,B_\pm,F$ and $\Theta$ be as in the [cumulative estimate](nov18b-goldbach-review.md). For each fixed nontrivial zeta zero $\rho=\beta+i\gamma$, every sufficiently large $X$ satisfies
\[
 \int_{Xe^{-C\sqrt{\log X\,\log\log X}}}^{Xe^{C\sqrt{\log X\,\log\log X}}}
              B_\pm(x)\,dx
       \gg_\rho \frac{X^{1+2\beta}}{\log X} .                         \tag{1}
\]
The same window and lower bound apply to both signs. The constant $C$ can be chosen absolute, with the threshold allowed to depend on the zero. This first version uses only the classical theta kernel and the zeta explicit formula.

A compact zero filter further gives the following result when $\Theta>1/2$. For each fixed zero with $\beta>1/2$, every sufficiently large $X$ satisfies
\[
 \int_{X\exp(-C\sqrt{\log X})}^{X\exp(C\sqrt{\log X})}
                 B_\pm(x)\,dx \gg_\rho X^{1+2\beta}.                   \tag{2}
\]
Here $C$ may depend on the filter. Under RH the attained-edge recurrence already gives this conclusion in every sufficiently wide fixed-factor interval with $\beta=1/2$. The off-line case of (2) uses the zero-density bound behind the [compact zero filter](nov18b-compact-zero-filter.md).

## Real zeros of the prime exponential sum

Write $V=\log X$, $R=\log V$. For every large $V$ and the specified $\rho$, the twisted theta kernel in the cumulative estimate gives a real $w$ with
\[
              |w-V|\le R,\qquad |F(w)|\gg_\rho e^{\beta V}.            \tag{3}
\]
The same explicit formula gives $|F'(s)|\ll e^{\Theta s}$ for real $s\ge0$. Shift the Mellin contour as for $F$ with the integrand multiplied by its Mellin variable. This costs one power of its ordinate, absorbed by the gamma factor.

For every sufficiently large real $u$, there is also a **real zero** of $F$ within $2\log u$ of $u$. Choose a fixed zero $\rho_a$ with $\beta_a>\Theta/2$ and apply (3) at the center $u$ to get a point $w_a$. On a subinterval of $[w_a-1,w_a+1]$ of length $\gg_{\rho_a}\min(1,e^{\beta_a u-\Theta w_a})$, the derivative bound gives $|F|\ge|F(w_a)|/2$. Suppose there is no real zero on $[w_a-\log u,w_a+\log u]$. The function has constant sign throughout. In the identity $\int K(t)F(w_a+t)\,dt=O(1)$, the mass on that subinterval alone has magnitude at least $\exp((2\beta_a-\Theta)u-O_{\rho_a}(\log u))$ times a positive fixed constant. Here $K$ has positive minimum on $[-1,1]$. All the other contributions inside the larger interval have the same sign. Its tails cost $O(\exp(\Theta w_a-c u^2))$. This contradiction proves the real-zero assertion.

## A positive kernel with a prescribed sign against the convolution

Fix $w$ as in (3). For $\lambda>0$ let $A(\lambda)=\int_0^\infty B(x)e^{-\lambda x}\,dx=\lambda^{-1}F(-\log\lambda)^2$. Include $\lambda_*=e^{-w}$ among $k+1$ distinct positive numbers $\lambda_0<\cdots<\lambda_k$, with successive ratios at least two. Take each other node to be $e^{-u}$ for an actual real zero $u$ of $F$. Put
\[
 K_*(x)=(-1)^k\prod_{j:\lambda_j\ne\lambda_*}|\lambda_*-\lambda_j|
  \sum_{i=0}^{k}\frac{e^{-\lambda_i x}}{\prod_{j\ne i}(\lambda_i-\lambda_j)} .
\]
The ordinary mean-value formula for a $k$th divided difference on the real line gives
\[
             0\le K_*(x)\le (x\lambda_k)^k/k!\quad(x\ge0).           \tag{4}
\]
The sign of its integral against $B$ can be chosen while keeping the kernel positive. If $\lambda_*=\lambda_i$, its coefficient is $(-1)^i$. Every other node has $A(\lambda_j)=0$. Thus
\[
        \int_0^\infty B(x)K_*(x)\,dx=(-1)^i e^wF(w)^2.              \tag{5}
\]

There is a uniform second bound $K_*(x)\ll e^{-\lambda_0 x}$ for either $i=0$ or $i=1$. To see it, put $a_j=\prod_{h\ne j}|\lambda_j-\lambda_h|^{-1}$ and $p=\prod_{d\ge1}(1-2^{-d})>0$. Splitting the denominator at $j$ gives
\[
 \frac{a_j}{a_0}
 \le p^{-2}\frac{\prod_{h=1}^j\lambda_h}{\lambda_j^j}
 \le p^{-2}2^{-j(j-1)/2}.
\]
Also $a_1/a_0=\prod_{h\ge2}(\lambda_h-\lambda_0)/(\lambda_h-\lambda_1)\ge1$. The normalized coefficients therefore have uniformly bounded total absolute value for either witness location.

## Packing the nodes and bounding the tails

Take $D=12\log V$, $k=\lceil\sqrt{V/D}\rceil$, and $W=8kD$. To put the witness first in slope order, choose $k$ different real zeros near $w-3jD$, $1\le j\le k$. To put the witness second, use $k-1$ such zeros and one near $w+3D$. For large $V$ these centers lie between $V/2$ and $2V$. The real-zero bound gives a displacement at most $D/4$ from each center, so the slopes meet the separation condition and
\[
              e^{-w-W/2}\le\lambda_0\le\lambda_k\le e^{-w+W/2}.
\]
Use $|B(x)|\ll(1+x)^2$. For $x\le e^{w-2W}$, (4) bounds the contribution of $|B|K_*$ by $O(e^{3w-3kW/2})=o(1)$ since $kW\ge8V$. For $x\ge e^{w+2W}$, use $K_*\ll e^{-\lambda_0 x}$ and $\lambda_0 e^{w+2W}\ge e^{3W/2}$. This contributes $O((1+\lambda_0^{-1})^3\exp(-e^{3W/2}/2))=o(1)$. Equation (5), the nonnegativity and the uniform upper bound on $K_*$ now give
\[
               \int_{e^{w-2W}}^{e^{w+2W}}B_\pm(x)\,dx
                        \gg e^wF(w)^2.
\]
The two choices of nodes use the same $w$. Since $w\ge V-\log V$, this implies (1).

For (2), the compact zero filter supplies (3) with $|w-V|\ll_\rho1$ for $\beta>1/2$, and places a real zero of $F$ in each interval of some fixed sufficient length at all large centers. These are precisely the two inputs used to pack the nodes. Choose $D$ a sufficiently large fixed constant in the same construction, giving $W\ll\sqrt V$ and $e^w\asymp X$. This proves (2). If the real-zero gaps can be prescribed arbitrarily short, the slope-ratio requirement of two can be weakened to any fixed ratio greater than one: replace $2$ in the convergent product by that ratio. This changes the constants in (4)–(5)'s accompanying upper bound; no uniformity as the ratio tends to one is needed.

For every $\epsilon>0$ choose $\beta$ within a sufficiently small fixed distance of $\Theta$. Estimate (1), together with the pointwise envelope $|B(n)|\ll_\delta n^{2\Theta+\delta}$, yields at least $X^{1-\epsilon}$ integers of each sign with $B_\pm(n)\ge n^{2\Theta-\epsilon}$ in the indicated window, for every sufficiently large $X$. Integer endpoints can be absorbed by any fixed enlargement of its constant. This describes the amount and location of oscillation that a proof of an RH-strength one-sided Goldbach bound would have to exclude.

## A one-sided test on a subsequence

In fact for every prescribed constant $c>0$, every fixed nontrivial zero of real part $\beta$, and both signs, one has
\[
 \int_{X\exp(-c\sqrt{\log X})}^{X\exp(c\sqrt{\log X})}
                    B_\pm(x)\,dx \gg_{c,\rho}X^{1+2\beta}
                  \qquad(X\ \hbox{sufficiently large}).               \tag{6}
\]
If the supremum is attained, (12) of the [first Goldbach argument](nov18b-variance-goldbach.md) already gives this in a fixed-factor interval contained in the displayed one. If it is unattained, it exceeds $1/2$ by the existence of critical-line zeros and zeta symmetry. The compact filter then provides strong witnesses for the given exponent and real zeros of $F$ in every sufficiently late interval of **any prescribed positive log length**. This includes the case $\beta\le1/2$ by using a zero farther right. In the node construction take a small constant $D>0$, use zero displacements at most $D/4$, and use the slope ratio $r=\exp(D)$ in the coefficient bound. The constants acquire the positive product $\prod_{j\ge1}(1-r^{-j})$. The exponent $kW\ge8V$ in the small-$x$ estimate is unaffected. The log half-width is $16\sqrt{VD}+O_D(1)$ plus the bounded witness displacement. Choosing $16\sqrt D<c$ proves (6).

In particular, with $c$ fixed arbitrarily, RH is equivalent to the existence of an unbounded sequence $X_j$ on which the **negative-part mass** in the interval in (6) is $\le X_j^{2+o(1)}$. Replacing the negative part by the positive part gives a second individual equivalence. On RH the published pointwise bound $|B(n)|\ll n\log^3 n$ gives this on all sufficiently large scales. A right-hand zero with $\beta>1/2$ violates the proposed subsequence bound by (6).
