# A local defect forces a large, absolutely convergent Laguerre prime sum

**Status.** Proposed quantitative derivative test for a prescribed height and displacement. It uses classical zeta growth, local zero counting, and Carathéodory's coefficient inequality. Absolute constants are unevaluated.

## Quantities and conclusions

For $t\ge100$, $|w|<1$, let
$$
 s_t(w)=\tfrac12+it+\tfrac32{1+w\over1-w}=2+it+{3w\over1-w}.
$$
Define coefficients near $w=0$ by
$$
 c_n(t)=[w^n]{\zeta'\over\zeta}(s_t(w))
 =-\sum_{k\ge2}{\Lambda(k)\over k^{2+it}}L_n^{(-1)}(3\log k).
$$
Here $L_0^{(-1)}=1$, and for $n\ge1$,
$$
 L_n^{(-1)}(x)=\sum_{j=1}^n {n-1\choose j-1}{(-x)^j\over j!}.
$$

* Under RH, $|c_n(t)|\ll\log t$ for all $0\le n\le t/10$.
* Conversely, suppose a zero $\beta+i\gamma$ has $|\gamma-t|\le1/2$ and $|\beta-1/2|\ge d$, with $0<d<1/2$, $t\ge100/d$. Then for all integers $D\ge0$,
$$
 d+\max_{0\le n\le D}|c_n(t)|\ge c\exp(c'dD)\,t^{-C(1+\log(1/d))}
$$
for absolute $c,c',C>0$. For fixed $b>0$ a coefficient exceeds $t^b$ at some
$$n\le C_1 d^{-1}\big(b+1+\log(1/d)\big)\log t$$
up to rounding and a sufficiently large absolute $C_1$. A nearest integer $t$ to the ordinate suffices at large heights. All other zeros and multiplicities are allowed.

For fixed $d,b$, the index bound is $O_{d,b}(\log t)$. For such an index the defining arithmetic series may be cut at a fixed power of $t$ with inverse-polynomially small error.

## Arithmetic identity and truncation

Near $w=0$, absolute convergence for $\Re s>1$ permits differentiation of the Euler series. The identity follows from $\sum_{n\ge0}L_n^{(-1)}(x)w^n=\exp(-xw/(1-w))$. Each fixed-degree sum converges absolutely. Also
$$
 |L_n^{(-1)}(x)|\le \sum_{j\ge0}{(nx)^j\over(j!)^2}\le e^{2\sqrt{nx}}\quad(x\ge0),
$$
using $\binom{n-1}{j-1}\le n^j/j!$ and $\binom{2j}{j}\le4^j$. For $\log k\ge48n$ this is at most $\sqrt k$ when $x=3\log k$. Hence the tail beyond $Y\ge\max(2,e^{48n})$ costs $O((1+\log Y)Y^{-1/2})$.

## The RH implication

Under RH the Hadamard log derivative gives
$$
 \Re{\xi'\over\xi}(s)=\sum_\rho {\Re(s)-1/2\over|s-\rho|^2}\ge0
 \qquad(\Re s>1/2).
$$
The constant vanishes by the completed-xi functional equation. Therefore $G=(\xi'/\xi)\circ s_t$ has nonnegative real part on the disk, and for $n\ge1$ Carathéodory gives $|[w^n]G|\le2\Re G(0)\ll\log t$ by the absolute Euler bound at $2+it$ and Stirling. To pass to $\zeta'/\zeta$ subtract
$$ U(s)=1/s+1/(s-1)-(\log\pi)/2+\tfrac12\psi(s/2).$$
On $|w|\le1-1/(n+1)$, if $1\le n\le t/10$, $|s_t(w)-(2+it)|\le3n$. Thus $|\Im s_t(w)|\gg t$, $\Re s_t(w)>1/2$ and $|U(s_t(w))|\ll\log t$. Cauchy's estimate costs at most $(1+1/n)^n\le e$. The case $n=0$ follows by absolute convergence.

## The local converse

Reflect if necessary so $\beta\ge1/2+d$. Apply the circle construction of the [Weil contour proof, §1](weil-contour-nov18.md) in the $s$ plane, using radii in $[d/4,d/2]$ instead of $[\delta/4,\delta/2]$. Its Jensen–Blaschke and logarithmic averaging argument gives a circle of radius $r$ about $\beta+i\gamma$ on which
$$
 |\zeta(s)|\ge \exp[-C_2\log t\,(1+\log(1/d))].
$$
It encloses at least one zero and no pole. Throughout its closed disk $\Re s\ge1/2+d/2$, $\Re s\le5/4$, $|\Im s-t|\le3/4$. Its image under $w(s)=(s-2-it)/(s+1-it)$ satisfies $|w(s)|\le r_0=1-d/6$, since
$$
 1-|w|^2={6(\Re s-1/2)\over(\Re s+1)^2+(\Im s-t)^2}\ge {3d\over6}.
$$

Set $r_1=1-d/12$, $P_D(w)=\sum_{n=0}^D c_n(t)w^n$ and $E=\max_{0\le n\le D}|c_n(t)|$. On $|w|\le r_1$, $\Re s_t(w)>1/2$ and $|s_t(w)-(2+it)|\le36/d$, so $|\Im s_t(w)|\asymp t$. There are uniform bounds $|\zeta(s_t(w))|+|\zeta'(s_t(w))|\ll t^2$. For example use truncated Euler summation on $1/4\le\Re s\le3$ together with a fixed-circle Cauchy bound for $\zeta'$, and absolute convergence for $\Re s\ge2$. All points and derivative circles are away from the pole. The analytic function
$$
 J(w)=\zeta'(s_t(w))-P_D(w)\zeta(s_t(w))
$$
vanishes to order at least $D+1$ at the origin by the defining Taylor series. On $|w|\le r_1$ its maximum is at most $C_3 t^2(1+12E/d)$. Schwarz's lemma with multiplicity then gives
$$
 \max_{|w|\le r_0}|J(w)|\le C_3 t^2(1+12E/d)e^{-c'd(D+1)}
$$
since $r_0/r_1\le1-d/12$.

On the selected circle integrate $\zeta'/\zeta-P_D(w(s))$. The integral divided by $2\pi i$ is the positive multiplicity of the enclosed zero cluster, because the rational function $P_D(w(s))$ has no pole there. Divide the bound on $J$ by the minimum modulus of zeta and use $r\le d/2$: the absolute value of the normalized integral is bounded by
$$
 C_4(d+E)t^{C(1+\log(1/d))}e^{-c'dD}.
$$
It is at least one, proving the assertion. No single zero derivative is used.

**Scope.** The tested moments are based at the Euler-convergence line $\Re s=2$. Exclusion of a fixed displacement strip needs a uniform upper bound on the indicated arithmetic moments at every relevant center. Exclusion at arbitrarily small displacements also needs the dependence on $d$.

**Related coordinates.** If $\log\xi(s_t(w))=\log\xi(2+it)+\sum_{n\ge1}\lambda_n(t)w^n/n$ and $\lambda_0(t)=0$, differentiation gives $3[w^n](\xi'/\xi)(s_t(w))=\lambda_{n+1}(t)-2\lambda_n(t)+\lambda_{n-1}(t)$ for $n\ge1$. Thus the completed coefficients are local second differences of shifted Li coefficients. The repository also has an earlier safe-line Laguerre transform on $\Re s=3/2$ for Hausdorff differences of first-Hermite heat moments, using a different weight. The specific estimate above concerns the arithmetic $L_n^{(-1)}(3\log k)$ coefficients on $\Re s=2$. [Earlier safe-line transform L-91002](https://github.com/GettysburgResearch/riemann/blob/ec118df8a133a1e4800f292641d42af1ba79f938/claims/lemmas/L-91002-safe-line-laguerre-euler-weights.md)
