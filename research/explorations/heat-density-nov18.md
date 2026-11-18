# First-Hermite positivity at almost all centers on an inverse-spacing scale

**Status.** Proposed unreviewed analytic theorem. There is an absolute $c>0$ such that, writing $L=\log X$ and $l=\log L$, outside a subset of $[X,2X]$ of measure $O(X/l)$ one has
\[
      M(q,x)>0 \quad\hbox{for all real }0<q\le c(L/l)^2 .
\]
Here $z=(\rho-1/2)/i=t+ia$ ranges over centered nontrivial zeros, with multiplicities, and $M=\sum(z-x)^2 e^{-q(z-x)^2}$. The exceptional set depends on $X$, independently of $q$. The factor $l$ in the shortest Gaussian width separates that width from the typical zero spacing. This assertion permits exceptional centers at arbitrarily great heights.

## Inputs

We use the classical Ingham zero-density theorem $N(\sigma,T)\ll T^{3(1-\sigma)/(2-\sigma)}(\log T)^5$ for $1/2\le\sigma\le 3/4$, with a uniform implied constant, and Selberg's mean-square bound $\int_T^{2T}|S(t)|^2dt\ll T\log\log T$ for the argument in the Riemann–von Mangoldt formula. We also use its pointwise remainder $S(t)=O(\log(2+t))$, the zero symmetries, and the integrated First-Hermite growing wedge. These are imported results. No zero table is used.

## A single exceptional set

Choose a fixed $B=20$ and put $\eta=B l/L$. For $X$ sufficiently large the Ingham estimate and reflection in the critical line imply
\[
 \#\{X-2\le t\le2X+2: |a|>\eta\}
 \ll X L^5 e^{-\eta L}\ll X L^{-14}.
\]
Indeed $3(1/2-\eta)/(3/2-\eta)=1-2\eta/(3/2-\eta)\le1-\eta$. We discard centers within distance one of any such ordinate. This costs $O(XL^{-14})$ in measure.

For the dyadic lengths $r=2^{-j}$ with $l/L\le r\le 2$, impose at once
\[
 \#\{|t-x|\le2r\}\le C rL,\qquad
 \#\{r<t-x\le2r\}\ge c_1 rL
\]
for absolute $C,c_1>0$. Each individual failure set has normalized measure $O(l/(rL)^2)$. In fact the smooth counting main term on the intervals has the appropriate length times $(L+O(1))/(2\pi)$, while the remainder is a difference of endpoint values of $S$, up to $O(1/X)$. Each such difference has normalized squared integral $O(l)$ by Selberg and a bounded covering by dyadic height blocks. Endpoint coincidences have measure zero. Chebyshev's inequality and the geometric sum of $r^{-2}$ give total normalized loss $O(1/l)$. The pointwise zero count also bounds the number of zeros with $k\le |t-x|<k+1$ by $O(\log(2+X+k))$ for every integer $k\ge1$, including shells that meet negative ordinates.

## Deterministic sign comparison on a retained center

For $q\le3\log\log(2+|x|)$ the integrated growing wedge already supplies positivity for $X$ large. Otherwise put $h=q^{-1/2}=o(1)$. Fix an absolute $K\ge4$ below, and then a sufficiently small $\epsilon>0$ with $2K\epsilon\le1$. Choose the theorem's constant $c>0$ so small that $h\ge\eta/\epsilon$ throughout the range. Every zero at distance at most one now has $|a|\le\epsilon h$. There is an available dyadic $r$ in $(h/2,h]$ since $h/2\ge l/L$.

Writing $v=t-x$, the real summand is
\[
 e^{-(v^2-a^2)/h^2}[(v^2-a^2)\cos(2va/h^2)+2va\sin(2va/h^2)].
\]
On the anchor interval $r<v\le2r$ it is at least $c_2 h^2$ for a fixed $c_2>0$ independent of $K$ and all $\epsilon\le1/8$. This follows from $h/2<v\le2h$, $|a|\le h/8$, and $|2va/h^2|\le1/2$. The count on that interval supplies at least $c_3 Lh^3$ in positive mass, with an absolute $c_3>0$.

For $|a|\le |v|\le Kh$ both bracketed terms are nonnegative. For $|v|<|a|$ and $|v|\le Kh$, the absolute summand is at most $2\epsilon^2e^{\epsilon^2}h^2$ since eventually $Kh<1$. Their count is at most $CrL$ since $\epsilon h<2r$. This loss is $O(\epsilon^2 Lh^3)$ with absolute constant.

For $Kh<|v|\le1$, use dyadic shells $s<|v|\le2s$ with $s=2^j r$. Every contributing shell satisfies $s/h>K/2$, and has at most $CsL$ ordinates. On it the absolute summand is at most $(4s^2+\epsilon^2h^2)e^{\epsilon^2-s^2/h^2}$. The resulting loss is $Lh^3$ times an absolute tail bound tending to zero as $K\to\infty$, uniformly in $r/h\in(1/2,1]$. For example, one may sum $C' (1+2^{3j})e^{-4^j/4}$ over $2^j>K/2$.

For $|v|>1$ the strip bound $|a|\le1/2$ and unit-shell counts give absolute total
\[
 \ll \sum_{k\ge1}(k+2)^2\log(2+X+k)e^{-(k^2-1/4)/h^2}
 \ll L e^{-3/(4h^2)}=o(Lh^3)
\]
uniformly as the lower bound on $q$ tends to infinity. Choose $K$ to make the dyadic tail at most $c_3Lh^3/4$, then $\epsilon$ to make the central loss at most $c_3Lh^3/4$. The exterior is eventually below the same budget. Symmetry makes the entire sum real, so it is strictly positive. All bounds hold simultaneously over the required continuum of $q$.

**Dependencies and scope.** See Ingham, *On the estimation of $N(\sigma,T)$*, Quart. J. Math. Oxford **11** (1940), and Selberg's mean-square theorem for $S(t)$ (also Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., Chapter IX). The previous large-values argument controls integer heat parameters with stronger exceptional measure in a smaller range. [Pointwise wedge](../integrated/heat_hermite/FIRST_HERMITE_REGIONS.md) · [Previous large-values argument](https://github.com/GettysburgResearch/riemann/blob/ea20af8867c3119c23efc27738d343aac2f79362/research/external/anthropic-zeta23/proofs/FIRST_HERMITE_LARGE_VALUES.md)

## Uniform refinement through every mesoscopic scale

For each $A>0$ there are constants $F_0,C_A,X_0$ such that if $X\ge X_0$ and $F_0\le F\le\sqrt L$, outside a set of measure at most $C_A XF^{-A}$,
\[
              M(q,x)>0\qquad(0<q\le (L/F)^2).
\]
Thus any $F(X)\to\infty$ gives a density-one conclusion, even for arbitrarily slowly growing $F$. For $F>\sqrt L$ the qualitative conclusion follows by using $\sqrt L$ instead. The constants do not give density one for a fixed $F$.

Use the uniform density estimate of Selberg–Jutila and the even increment moments of Fujii as recorded in [Rodgers, Theorems 2.2 and 2.4](https://arxiv.org/abs/1404.3080). In the forms needed here, for an absolute $b>0$ and each fixed integer $k\ge1$,
\[
 N(1/2+y,3X)\ll X L e^{-byL},\qquad
 X^{-1}\int_X^{2X}|S(x+s)-S(x)|^{2k}dx
 \ll_k [\log(2+sL)]^{2k}\quad(0\le s\le1).
\]
The second display deliberately uses a coarse logarithmic upper bound. Bounded endpoint shifts are handled by covering with a bounded number of dyadic intervals, and intervals of length in $[1,8]$ by telescoping into at most eight pieces.

Keep $K$ large and then $\epsilon$ small as in the deterministic comparison, allowing the Gaussian tail exponent there to weaken from $1$ to $1/2$. Write $h_0=F/L$, $\eta=\epsilon h_0$, and $J=K/\epsilon$. For each zero with $|a|>\eta$, discard the centers $x$ for which $|x-t|\le J|a|$. Only zeros with ordinates in $[X-J,2X+J]$ can matter. By reflection and the density estimate the discarded fraction is bounded by a constant times
\[
 J L\left(\eta e^{-b\eta L}
            +\int_\eta^{1/2}e^{-byL}\,dy\right)
 \ll (1+F)e^{-b\epsilon F}.
\]
This integrates the actual widths of the discarded intervals. It costs no factor $L$ at fixed scaled depth $|a|L$.

Impose the same two local count bounds for every dyadic $r\in[h_0/2,2]$. Now apply the increment moment at each scale and Markov's inequality. Each failure has normalized measure at most
\[
 O_k\big((\log(2+rL)/(rL))^{2k}\big).
\]
The sum over dyadic $r$ is $O_k((\log(2+F)/F)^{2k})$, by geometric decay, uniformly in the upper limit. Taking $2k>A+1$ proves the stated bound on the full exceptional set, including the depth exclusions.

On a retained center every zero satisfies either $|a|\le\eta$ or $|a|<|t-x|/J$. Hence $|a|\le\epsilon h$ whenever $h\ge h_0$ and $|t-x|\le Kh$. The central sign comparison and anchor mass carry over unchanged. In the intermediate shells $Kh<|v|\le1$, one has $|a|\le |v|/2$ in either case. The summand has absolute value at most $2v^2 e^{-v^2/(2h^2)}$. The convergent dyadic tail is still uniformly small for the chosen $K$. The unit-shell exterior and the small-$q$ wedge complete the proof.
