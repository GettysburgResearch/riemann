# An Erlang prime moment with a fixed frequency law

Write $\Theta=\sup_\rho\Re\rho$ over nontrivial zeta zeros, $d=2-\Theta$,
and $\kappa(t)=1/(\pi(1+t^2))$. At orders $n\ge1$ put
$$
 P_n(x)=\frac1{n!}\left(\sum_{k\le e^x}\frac{\Lambda(k)}{k}(\log k)^n
                     -\frac{x^{n+1}}{n+1}\right),\quad
 E_n=2\int_0^\infty e^{-2x}|P_n(x)|^2dx .
$$
These quantities use no zero ordinates or frequency truncations. The
following are proposed analytic consequences of the classical zeta
partial fractions and the unit-interval zero count:
$$
 \lim_{n\to\infty} E_n^{1/(2n)}=\frac1d,\qquad
 \lim_{n\to\infty}\sqrt n\,d^{2n+2}E_n
 =d\sqrt{\pi}\sum_{\substack{\rho\ {\rm distinct}\\\Re\rho=\Theta}}
             m_\rho^2\,\kappa(\Im\rho).
 \tag{1}
$$
The sum includes both ordinate signs and is zero if the supremum is
unattained. Thus a cofinal upper root bound $2/3$ is equivalent to RH.
Even the unconditional bound $E_n\ll d^{-2n}/\sqrt n$ implied by (1)
retains the unknown abscissa. No bound $2/3$ for the actual root is known
from this argument.

## Exact positive arithmetic integral

Let $F(s)=\zeta'(s)/\zeta(s)+1/(s-1)$ and
$C_n(t)=(-1)^n F^{(n)}(2+it)/n!$. The signed measure
$$
 \mu_n(dv)=\frac{v^n e^{-2v}}{n!}\{e^v\,dv-d\psi(e^v)\},
 \qquad v\ge0 ,
$$
has Fourier transform $C_n(t)$ using $e^{-itv}$. Convolution with
$\mathbf 1_{[0,\infty)}(v)e^{-v}$ gives precisely $-e^{-x}P_n(x)$
for $x\ge0$. Hence Plancherel gives
$$
 E_n=\int_{\mathbb R}|C_n(t)|^2\kappa(t)\,dt.
 \tag{2}
$$
In particular all frequencies have already been integrated in the physical
formula. The upper estimate in (1) does not require a supremum over them.

## Vertical poles and integrable control of their total contribution

For $n\ge1$ the classical Hadamard expansion of $\xi'/\xi$ and the
digamma expansion give exactly
$$
 C_n(t)=\sum_{\rho}\frac{m_\rho}{(2+it-\rho)^{n+1}}
          +\sum_{k=1}^\infty\frac1{(2+2k+it)^{n+1}} .
 \tag{3}
$$
The first sum is over distinct nontrivial zeros. Both sums converge
absolutely locally uniformly. The constants in the genus-one partial
fractions disappear on differentiation, $1/(s-1)$ cancels the pole
of zeta, and the remaining gamma factors yield the simple trivial
zero terms as written. On multiplying by $d^{n+1}$ the second sum is
uniformly exponentially small for $n\ge2$ since $d\le3/2$.

Define $K_j(u)=(1+(u/d)^2)^{-j/2}$. The absolute value of a single
normalized term in the first sum of (3) is bounded by $m_\rho
K_{n+1}(t-\gamma)$. For a set $S$ of distinct zeros, Cauchy–Schwarz gives
$$
 \left(\sum_{S}m_\rho K_{n+1}(t-\gamma)\right)^2
 \le \left(\sum_{\rho}m_\rho K_2(t-\gamma)\right)
      \left(\sum_{S}m_\rho K_{2n}(t-\gamma)\right).
$$
The first factor is $O(\log(2+|t|))$ by the unit-interval zero count.
For $q(t)=\kappa(t)\log(2+|t|)$, the elementary bound
$q(\gamma+u)\ll q(\gamma)(1+|u|)^3$ gives
$$
 \int_{\mathbb R}q(t)K_{2n}(t-\gamma)\,dt
 \ll \frac{q(\gamma)}{\sqrt n}\qquad(n\ge4).
$$
On $|u|\le d$ use Gaussian domination, and on $|u|>d$
factor out $2^{-(n-3)}$ leaving an integrable polynomially weighted
$K_6$. Thus the squared $L^2(\kappa)$ norm of the normalized omitted
zeros, multiplied by $\sqrt n$, is at most $C\sum_S m_\rho q(\gamma)$.
This series converges by the same unit-interval count, uniformly controlling
the tail for every $n\ge4$.

## Gaussian concentration at each rightmost zero

In a fixed finite subset, any pole with $\Re\rho<\Theta$ has exponentially
small normalized contribution because $\Re(2-\rho)>d$. Each pole with
$\Re\rho=\Theta$ gives exactly
$$
 \sqrt n\int_\mathbb R m_\rho^2\kappa(t)K_{2n+2}(t-\gamma)\,dt
 \longrightarrow d\sqrt\pi\,m_\rho^2\kappa(\gamma).
$$
This follows by setting $t=\gamma+du/\sqrt n$, or from the beta integral
and approximate-identity convergence. Distinct rightmost poles have
distinct ordinates. Outside disjoint neighborhoods of their centers at
least one factor of every cross product is exponentially small. The same
holds inside any one of these neighborhoods for all factors centered at
the other ordinates. Thus the integrated cross terms vanish even after
multiplication by $\sqrt n$. The uniform tail estimate and the triangle
inequality in $L^2(\kappa)$ now prove the second limit in (1), by first
truncating the zeros at a fixed height and then removing this truncation.

For the lower root rate even if the supremum is unattained, take $r>d$,
chosen less than 2, and any zero with $2-\beta<r$. In some real interval
about its ordinate the nearest pole of $F$ to $2+it$ has distance
less than $r$. Only a finite set of poles can compete there. Equalities
of distances of two distinct poles occur at isolated real $t$, unless
they have the same ordinate and real part: their squared distance
difference is affine in $t$ and $2-\beta$ is positive. Choose a compact
subinterval of positive length with the same unique nearest pole and a
uniform multiplicative gap to all competitors. By (3), its term then
dominates the other terms exponentially as $n\to\infty$, uniformly on
that subinterval; bound the residual using the absolute sum of inverse
squared distances times the largest remaining inverse distance to the
power $n-1$. Thus $E_n^{1/(2n)}$ has liminf at least $1/r$. Send
$r\downarrow d$, and use the uniform bound already proved for the limsup.

## An unconditional upper bound using only the physical prime discrepancy

There are absolute $c,C>0$ for which, at all sufficiently large orders,
$$
 E_n\le \frac{C}{\sqrt n}\exp\!\left(
       -c\, n^{3/5}(\log n)^{-1/5}\right).
$$
Indeed the classical Vinogradov–Korobov PNT and partial summation give
$A(x)=\sum_{k\le e^x}\Lambda(k)/k-x=A_\infty+
O(\exp[-c_0 x^{3/5}(\log(2+x))^{-1/5}])$. Integration by parts with
weight $v^n$ uses only $A(v)-A_\infty$ since $n\ge1$. For $x\ge n/2$
split the derivative integral at $x/2$. The lower part costs
$O(2^{-n}x^n)$, the upper part and boundary cost
$O(x^n\exp[-c_1 n^{3/5}(\log n)^{-1/5}])$. For $0\le x<n/2$ use the
uniform crude bound $n!|P_n(x)|\ll x^n$. The squared norm of
$e^{-x}x^n/n!$ is $(2n)!/(2^{2n+1}(n!)^2)\asymp n^{-1/2}$, and the
fraction of this gamma integral in $[0,n/2]$ is exponentially small
in $n$ by the exponential Markov inequality. Combining both ranges proves
the bound. Its saving in $n$ is subexponential; the critical upper root
$2/3$ requires an exponential saving.

## A Cauchy parameter that also detects simplicity

Replace the frequency density in (2) by
$\kappa_a(t)=a/(\pi(a^2+t^2))$, $a>0$. The physical energy is now
$$
 E_{n,a}=\frac{2a}{(n!)^2}\int_0^\infty e^{-2ax}
  \left|\int_0^x v^ne^{-(2-a)v}\{d\psi(e^v)-e^v\,dv\}\right|^2 dx.
$$
Indeed convolution with $e^{-av}\mathbf1_{v\ge0}$ and Plancherel give
this identity. All arguments for (1) transfer since $\kappa_a/\kappa$
is bounded above and below by positive constants and $\kappa_a$ is
continuous. Choose $a=1/2$ and normalize on the critical scale. Then
$$
 \liminf_n \sqrt n(3/2)^{2n+2} E_{n,1/2}
 \ \ge\ \frac{3}{4\sqrt\pi}(2+\gamma_E-\log(4\pi)),
$$
with equality if and only if RH holds and every nontrivial zero is simple.
Indeed off RH the left side is infinite by the root rate. On RH it equals
$3/(4\sqrt\pi)\sum_{\rho\ {\rm distinct}}m_\rho^2/|\rho|^2$
by the second limit in (1). The classical identity
$\sum_{\rho\ {\rm distinct}}m_\rho/[\rho(1-\rho)]
=2+\gamma_E-\log(4\pi)$ follows from the Hadamard logarithmic derivative
and functional equation of $\xi$ at zero and one. On RH its denominators
are $|\rho|^2$, giving the assertion. The same zero mass with squared
multiplicities appears in [Burnol's lower bound for the Nyman–Beurling
distance](https://doi.org/10.1006/aima.2001.2066); the prime energy here is
an independently defined explicit positive integral.

## High frequencies and the Montgomery form factor

Assume RH in this section and keep $d=3/2$. Let integers $n=n(T)$ satisfy
$n/\log T\to\lambda>0$. Under the established Montgomery theorem, for
$0<\lambda<3/2$ the moving high-frequency interval has the asymptotic
$$
 \frac1T\int_T^{2T}|C_n(t)|^2dt
 \sim\frac{2\sqrt n}{9\sqrt\pi}(4/9)^n .
 \tag{4}
$$
No simplicity or negative moment hypothesis is used. This is the same
leading term as the prime diagonal
$\sum_k\Lambda(k)^2(\log k)^{2n}/((n!)^2 k^4)$. Indeed partial summation
of $\sum\Lambda(k)^2$ with its quantitative PNT gives the equivalent
$(2n+1)!/((n!)^2 3^{2n+2})$: to see the relative error split the gamma
integral into $v=\log k$ between $n/3$ and $4n/3$, and its exponentially
small complementary tails, using the bounded cumulative error against
the derivative of $v^{2n}e^{-3v}$. On the middle range that cumulative
error after subtracting its constant is exponentially small in $\sqrt n$
times a polynomial. The direct bilinear Dirichlet-series mean-value
inequality gives relative error $O((9/4)^n/T)$ up to polynomial factors
by applying the same calculation with an extra $k$ in the diagonal sum.
Thus (4) continues the diagonal regime from
$\lambda<1/\log(9/4)$ to $\lambda<3/2$ under RH.

Here is the reduction, including the large-frequency cutoffs. For
$H=T$ or $2T$, restrict the nontrivial-zero sum in (3) to $0<\gamma\le H$
and denote it $B_H(t)$. Plancherel, or direct Laplace integration, gives
$$
 \int_\mathbb R|B_H(t)|^2dt
 =I_n\sum_{0<\gamma,\gamma'\le H}K(\gamma-\gamma'),\qquad
 I_n=\frac{2\pi(2n)!}{(n!)^2(2d)^{2n+1}},
 \quad K(u)=(1-iu/(2d))^{-2n-1}.
$$
Here and below sums over ordinates count multiplicities. The left side
differs from $\int_0^H|C_n(t)|^2dt$ by $o(I_n H\log H)$.
For details, insert end buffers of length $\sqrt H$. In either buffer
the complete and truncated nontrivial-zero sums are
$O(d^{-n-1}\log(2+H))$ by their absolute normalized $K_2$ majorants.
At interior points all omitted zeros are at distance $\ge\sqrt H$, so
their normalized total is bounded by $O(\log(2+H)(1+H/d^2)^{-(n-1)/2})$
using the same $K_2$ majorant. The complete trivial-zero terms on
$[0,H]$ cost $O((d/4)^{n-1})$ after normalization, hence are negligible
even when squared and integrated over $H$ (recall $n\asymp\log H$).
Outside the buffers and $[0,H]$, the truncated sum is at most
$O(H\log H)\operatorname{dist}(t,[0,H])^{-n-1}$, whose squared integral
is negligible. Since $I_n\asymp d^{-2n}/\sqrt n$ these comparisons
also hold for the cross terms by Cauchy–Schwarz.

Write $w(u)=4/(4+u^2)$. In the pair sum we may replace $K$ by $wK$
at a cost $o(H\log H)$ absolutely. In fact
$\sup_u|(1-w(u))K(u)|\ll1/n$. For each zero there are
$o(\log H)$ zeros within $|u|\le(\log H)^{-1/4}$ uniformly, by the
Riemann–von Mangoldt formula and Littlewood's RH bound on its remainder
(use compactness for bounded heights and the trivial unit count for
heights below $\exp(\sqrt{\log H})$). Up to distance one the rest
costs $O(\log H)e^{-c\sqrt{\log H}}$ per zero. For distances exceeding
one use the integrable inverse-square tail times an exponentially small
factor and the unit-interval count. This proves the replacement.

Now $K(u)=\mathbb E e^{iXu}$ where $X$ has gamma law of shape
$2n+1$ and rate $2d$. Consequently the pair sum divided by
$H\log H/(2\pi)$ is, up to $o(1)$, the expectation of Montgomery's
form factor $F_H(X/\log H)$ in its standard normalization. The gamma
variable divided by $\log H$ concentrates inside any fixed neighborhood
of $\lambda/d$, with exponential tail in $n$. The absolute pair bound
$\sum_{\gamma,\gamma'}w(\gamma-\gamma')\ll H\log^2 H$ controls that
tail. Montgomery's theorem under RH gives $F_H(\alpha)=\alpha+o(1)$
uniformly on compact subsets of $0<\alpha<1$. Thus the pair sum is
$(H\log H/(2\pi))(\lambda/d+o(1))$. Subtract the two endpoint formulas
and apply Stirling to $I_n$ to obtain (4).
[Montgomery, The pair correlation of zeros of the zeta function](https://doi.org/10.1090/pspum/024/9944)

For $\lambda>3/2$, the additional strong pair-correlation conjecture
$F_H(\alpha)=1+o(1)$ uniformly near $\lambda/d$ would instead give
$I_n\log T/(2\pi)$ as the equivalent of the left side in (4). More
generally only convergence of the gamma-weighted average of the form
factor is required. The established subcritical result concerns a
moving high-frequency band. It leaves the proposed critical root upper
bound for the full physical prime energy open.
